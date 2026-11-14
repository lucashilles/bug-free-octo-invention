# Domain 6 — Scaling with Google Cloud Operations

43 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q7

**PayWave Market, an online payments platform, depends on a public cloud provider for its customer-facing checkout service. The provider promised an SLA of 99.95% availability but did not meet that commitment during a busy shopping week. What is a possible impact on PayWave Market?**

- A. PayWave Market could use up its internal error budget.
- B. PayWave Market might need to renegotiate the SLA so uptime matters less.
- C. Unplanned downtime could cause customers to leave the platform.
- D. All information stored in PayWave Market’s database could be automatically deleted.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Unplanned downtime could cause customers to leave the platform.

**Correct answer: C. Unplanned downtime could cause customers to leave the platform.**

When a provider misses its SLA, the customer-facing checkout service goes down. Customers who cannot pay may go to a competitor and not come back. The question asks for the business impact, and lost customers (churn) and lost revenue are the most direct one, especially during a busy shopping week.

**Why the others are wrong:**
- **A. Use up its internal error budget**: provider downtime can count against PayWave's own SLO, but this is an internal reliability metric, not the main business impact asked for.
- **B. Renegotiate the SLA so uptime matters less**: uptime still matters to customers; a weaker SLA does not fix anything.
- **D. All database information automatically deleted**: an availability failure does not delete stored data.

**Remember:** Missed SLA → downtime → unhappy customers and lost revenue. The provider usually owes service credits.

**⚠️ Note:** Option A is not absurd, since provider downtime does count against your own SLO and error budget. C is keyed because it is the clearest business impact. Pick C on this exam.

</details>

---

### Exam 1 · Q11

**RideMango is a food-delivery mobile app running several workloads on Google Cloud. The finance team does not want to wait until the monthly invoice arrives to discover that spending has gone beyond their planned cloud budget. They want to receive a notification when costs cross a defined limit, such as ₹75,000 for the month. What should RideMango do?**

- A. Stop Compute Engine virtual machines outside peak ordering hours.
- B. Configure a budget threshold rule and alert.
- C. Change project resource quota policies.
- D. Review past billing reports to estimate future overspending.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure a budget threshold rule and alert.

**Correct answer: B. Configure a budget threshold rule and alert.**

Cloud Billing budgets let you set a planned amount and threshold rules (for example, 50%, 90% and 100% of the budget). When spending crosses a threshold, alerts go out to the chosen people. The clue is that finance wants a notification when costs cross a limit, not after the invoice arrives.

**Why the others are wrong:**
- **A. Stop VMs outside peak hours**: this may lower costs, but it does not notify anyone when spending crosses the limit.
- **C. Change resource quota policies**: quotas cap how many resources can be used; they are not a spending alert.
- **D. Review past billing reports**: looking backward is exactly what finance wants to avoid; it is not proactive.

**Remember:** "Notify me when spend crosses X" = budget + threshold alert. Budgets alert; they do not stop spending by themselves.

</details>

---

### Exam 1 · Q14

**TrailNest, a travel booking website, wants to understand what out-of-the-box observability means for its cloud operations team. The team needs a ready-to-use way to gain visibility into the health, performance, and behavior of the services running in its cloud environment. What does out-of-the-box observability mean in the context of cloud operations?**

- A. Monitoring software release schedules
- B. Monitoring IT infrastructure and applications
- C. Monitoring traveler ratings and survey responses
- D. Monitoring monthly cloud billing charges

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Monitoring IT infrastructure and applications

**Correct answer: B. Monitoring IT infrastructure and applications**

Out-of-the-box observability means you get visibility into the health and performance of your infrastructure and applications right away, with built-in metrics, logs and dashboards. On Google Cloud this comes from Google Cloud Observability (Cloud Monitoring, Cloud Logging and related tools). The clue is "health, performance, and behavior of the services".

**Why the others are wrong:**
- **A. Monitoring software release schedules**: release planning is a project management task, not observability.
- **C. Monitoring traveler ratings**: customer feedback is business data, not service health.
- **D. Monitoring monthly cloud billing**: cost tracking is billing management, not observability.

**Remember:** Observability = visibility into how your systems and apps are running.

</details>

---

### Exam 1 · Q43

**RideNest, a scooter rental mobile app, wants one fully managed place where its operations team can view the health of its Google Cloud infrastructure, create dashboards, configure alerts, and run uptime checks for customer-facing services. Which Google Cloud service should RideNest use?**

- A. Cloud Trace
- B. Cloud Monitoring
- C. Cloud Logging
- D. Cloud Profiler

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Monitoring

**Correct answer: B. Cloud Monitoring**

Cloud Monitoring collects metrics on the health and performance of infrastructure and services. It provides dashboards, alerting policies and uptime checks in one managed place. The clues are "dashboards, configure alerts, and run uptime checks".

**Why the others are wrong:**
- **A. Cloud Trace**: it tracks request latency across services; it is not the main dashboard and alerting tool.
- **C. Cloud Logging**: it collects and searches logs; metrics, dashboards and uptime checks belong to Cloud Monitoring.
- **D. Cloud Profiler**: it analyzes CPU and memory use in code to find inefficient functions.

**Remember:** Metrics, dashboards, alerts and uptime checks = Cloud Monitoring. Logs = Cloud Logging. Latency of requests = Cloud Trace.

</details>

---

### Exam 1 · Q45

**MetroPay, a mobile wallet company, notices that one of its payment-status services often makes users wait a long time before showing the final result. According to Google’s Four Golden Signals, which signal should the operations team monitor to measure this part of the service’s performance?**

- A. Saturation
- B. Errors
- C. Latency
- D. Traffic

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Latency

**Correct answer: C. Latency**

Latency is the time it takes to serve a request. Users waiting a long time for the payment status to appear is a latency problem. The Four Golden Signals from Google's SRE practice are latency, traffic, errors and saturation.

**Why the others are wrong:**
- **A. Saturation**: saturation measures how full the system is (CPU, memory, capacity).
- **B. Errors**: errors measure the rate of failed requests, not slow ones.
- **D. Traffic**: traffic measures demand, such as requests per second.

**Remember:** Slow = latency. Busy = traffic. Failing = errors. Full = saturation.

</details>

---

### Exam 1 · Q50

**BrightRide, a ride-sharing mobile app, has set an availability service level objective (SLO) of 99.999% for its customer booking service. Based on this “five nines” availability target, approximately how much downtime can riders experience in one year?**

- A. 5 minutes
- B. 500 minutes
- C. 5 hours
- D. 5 days

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. 5 minutes

**Correct answer: A. 5 minutes**

99.999% availability allows 0.001% downtime. A year has about 525,600 minutes, and 0.001% of that is about 5.26 minutes. So "five nines" means roughly 5 minutes of downtime per year.

**Why the others are wrong:**
- **B. 500 minutes**: about 500 minutes (roughly 8.3 hours) per year is closer to 99.9% availability.
- **C. 5 hours**: this is far more than five nines allows; it is between 99.9% and 99.99%.
- **D. 5 days**: this would be about 98.6% availability.

**Remember:** 99.9% ≈ 8.8 hours/year, 99.99% ≈ 53 minutes/year, 99.999% ≈ 5 minutes/year.

</details>

---

### Exam 2 · Q10

**PixovaPay, a digital payments website, is adopting Google’s Site Reliability Engineering practices to improve reliability for its transaction service. The operations team wants to know which concept is used as a direct measurement of how the service is actually performing. Which concept should they use?**

- A. Service-level agreement
- B. Service-level indicator
- C. Error reporting
- D. Service-level objective

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Service-level indicator

**Correct answer: B. Service-level indicator**

A service-level indicator (SLI) is a direct, measured value of how the service is performing, such as the percentage of successful requests or request latency. The SLO is the target for that SLI, and the SLA is the contract with customers. The clue is "direct measurement".

**Why the others are wrong:**
- **A. Service-level agreement**: An SLA is a contract with customers that includes consequences if targets are missed; it is not a measurement.
- **C. Error reporting**: Error reporting groups and shows application errors; it is a tool, not the SRE measurement concept.
- **D. Service-level objective**: An SLO is the target value for an SLI, not the measurement itself.

**Remember:** SLI = what you measure; SLO = the goal; SLA = the promise with penalties.

</details>

---

### Exam 2 · Q11

**QuickKart, an online grocery delivery platform, is moving several application teams to Google Cloud. The finance team notices that different engineering teams can create cloud resources as needed, and monthly costs change based on actual usage. What is the typical cloud spending behavior for most organizations?**

- A. Decentralized and variable
- B. Centralized and variable
- C. Decentralized and fixed
- D. Centralized and fixed

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Decentralized and variable

**Correct answer: A. Decentralized and variable**

In the cloud, many teams can create resources themselves, so spending decisions are spread out (decentralized). Bills also change month to month with actual usage (variable). The stem describes both: teams create resources "as needed" and costs "change based on actual usage".

**Why the others are wrong:**
- **B. Centralized and variable**: Spending is not controlled by one central team when many teams create resources.
- **C. Decentralized and fixed**: Usage-based billing means costs are not fixed.
- **D. Centralized and fixed**: This describes traditional on-premises budgeting, not the cloud.

**Remember:** Cloud spending = decentralized and variable; that is why FinOps and cost controls matter.

</details>

---

### Exam 2 · Q19

**ShopEase Media is organizing its Google Cloud environment for separate teams such as marketing, analytics, and payments. The cloud administrator wants to apply access rules once for the analytics team and have those rules automatically apply to every project created under the analytics group. How does the Google Cloud resource hierarchy help with this requirement?**

- A. Policies can be applied at the folder level and are inherited by projects inside the folder.
- B. Projects in the resource hierarchy are not affected by security policies.
- C. Policies can only be applied at the organization level and affect all projects.
- D. Policies can only be applied to individual projects.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Policies can be applied at the folder level and are inherited by projects inside the folder.

**Correct answer: A. Policies can be applied at the folder level and are inherited by projects inside the folder.**

The resource hierarchy is organization, then folders, then projects, then resources. Policies set on a folder are inherited by every project inside it, including new ones. So the admin sets access once on the analytics folder. The clue is "apply access rules once" and "automatically apply to every project".

**Why the others are wrong:**
- **B. Projects not affected by policies**: Projects inherit policies from their parents and can have their own.
- **C. Only at organization level**: Policies can be set at the organization, folder, project, or resource level.
- **D. Only on individual projects**: Setting policies project by project is possible, but it is not the only option and is what the admin wants to avoid.

**Remember:** Group projects in folders; policies flow down the hierarchy.

</details>

---

### Exam 2 · Q36

**FitCart, an online fitness equipment store, plans to launch a new analytics workload on Google Cloud. The team needs a reliable estimate of the expected monthly cost before they deploy the workload. How should FitCart create this estimate?**

- A. Use the Google Cloud Pricing Calculator.
- B. Deploy the workload in a test environment to observe costs.
- C. Use historical costs from an existing similar workload.
- D. Review pricing pages and manually calculate an estimate.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use the Google Cloud Pricing Calculator.

**Correct answer: A. Use the Google Cloud Pricing Calculator.**

The Google Cloud Pricing Calculator estimates monthly costs for planned services before you deploy them. You enter the products and expected usage and get an estimate. The clues are "estimate … before they deploy".

**Why the others are wrong:**
- **B. Deploy in test environment**: This costs money and time, and test usage may not match production.
- **C. Historical costs of a similar workload**: Another workload may differ in size and services, so the estimate is less reliable.
- **D. Manually calculate from pricing pages**: This is slow and easy to get wrong; the calculator does it for you.

**Remember:** Estimate cost before deploying → Pricing Calculator; track actual cost → billing reports and budgets.

</details>

---

### Exam 2 · Q48

**FreshCartGo, a grocery delivery mobile app, runs its backend on a cloud provider and has an SLA that promises a defined level of monthly service availability. During one month, the provider fails to meet the agreed availability target. What should FreshCartGo typically expect from the cloud provider?**

- A. Automatic increase in subscription fees
- B. Permanent shutdown of the affected cloud service
- C. Service credit for the service interruption
- D. Automatic expansion of the application’s error budget

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Service credit for the service interruption

**Correct answer: C. Service credit for the service interruption**

An SLA is a contract that promises a level of service. If the provider misses it, the usual remedy is a service credit, which is a discount on future bills. The clue is "fails to meet the agreed availability target".

**Why the others are wrong:**
- **A. Increase in subscription fees**: A missed SLA leads to compensation, not higher prices.
- **B. Permanent shutdown of the service**: Missing a target does not shut the service down.
- **D. Expansion of the error budget**: The error budget is an internal SRE concept tied to the SLO; it does not grow because of an outage.

**Remember:** Missed SLA → service credits for the customer.

**⚠️ Note:** Under Google Cloud SLAs, customers usually must request credits within a time window; they are not automatic. "Service credit" is still the right answer.

</details>

---

### Exam 2 · Q49

**TaskNest is a project management app that is adopting a DevOps approach for its software delivery teams. The company wants to use tools and automation to make development, testing, deployment, and operations faster and more reliable. Which operational challenge will this help TaskNest resolve?**

- A. Repetitive manual tasks that slow down workflows
- B. Continuous supervision of creative design work
- C. Vendor distribution and product supply-chain delays
- D. Faulty physical hardware that blocks new ideas

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Repetitive manual tasks that slow down workflows

**Correct answer: A. Repetitive manual tasks that slow down workflows**

DevOps uses automation, like CI/CD pipelines and automated testing, to remove slow, error-prone manual steps. This makes building, testing, and releasing software faster and more reliable. The clue is "tools and automation to make … faster and more reliable".

**Why the others are wrong:**
- **B. Supervision of creative design work**: DevOps is about software delivery and operations, not managing design work.
- **C. Supply-chain delays**: Physical product supply chains are outside DevOps.
- **D. Faulty physical hardware**: Hardware failures are an infrastructure issue, not what DevOps automation solves.

**Remember:** DevOps = automate repetitive work to ship faster and more reliably.

</details>

---

### Exam 3 · Q1

**MediCart, a healthcare shopping website, runs a production application on Google Cloud. Its developers want to understand what Cloud Debugger helped teams do when investigating application behavior. What was the main purpose of Cloud Debugger?**

- A. Apply code changes instantly in production without affecting the service level objective (SLO).
- B. Inspect running application source code and state in real time without causing user downtime.
- C. Manage source code repositories and speed up application development.
- D. Analyze live source code only after the application is taken offline for user downtime.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Inspect running application source code and state in real time without causing user downtime.

**Correct answer: B. Inspect running application source code and state in real time without causing user downtime.**

Cloud Debugger let developers take snapshots of a live application's variables and call stack, and add log points, while the app kept serving users. The stem asks about investigating behavior in production, which points to inspecting state without stopping the app.

**Why the others are wrong:**
- **A. Apply code changes instantly in production**: A debugger observes code; it never deployed or changed code.
- **C. Manage source code repositories**: That describes a source repository tool, not a debugger.
- **D. Analyze code only after taking the app offline**: The whole point was to avoid downtime, so this is the opposite.

**Remember:** Debugger = look inside a running app without stopping it.

**⚠️ Note:** Cloud Debugger was deprecated in 2022 and shut down in 2023; its open-source successor is Snapshot Debugger. The answer correctly describes what it did, so pick the keyed answer on this exam.

</details>

---

### Exam 3 · Q11

**FreshTrail Delivery is running applications and infrastructure on Google Cloud. The operations team wants to understand the health and performance of its services by gathering measurements such as CPU usage, latency, request count, and application-specific values. What does monitoring mean in this cloud operations context?**

- A. Watching cloud spending in real time to make sure budgets are not exceeded.
- B. Collecting predefined and custom metrics from applications and infrastructure.
- C. Recording user actions to guarantee compliance with privacy regulations.
- D. Tracking user locations to document regional access and usage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Collecting predefined and custom metrics from applications and infrastructure.

**Correct answer: B. Collecting predefined and custom metrics from applications and infrastructure.**

In cloud operations, monitoring means collecting metrics, both built-in ones like CPU and latency and custom application values, to see service health and performance. Cloud Monitoring does this and supports dashboards and alerts.

**Why the others are wrong:**
- **A. Watching cloud spending**: That is cost management or budgets, not operational monitoring.
- **C. Recording user actions for compliance**: That is closer to audit logging.
- **D. Tracking user locations**: That is not what operational monitoring means.

**Remember:** Monitoring = metrics. Logging = events. Tracing = request paths.

</details>

---

### Exam 3 · Q13

**FitTrackGo, a fitness tracking mobile app, runs several customer-facing services on Google Cloud. The operations team wants to measure the main SRE golden signals for the platform. They specifically need to identify how much of the available infrastructure capacity is being used and whether resources such as CPU, memory, or I/O are becoming constrained. Which metric should they focus on?**

- A. Latency
- B. Traffic
- C. Saturation
- D. Errors

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Saturation

**Correct answer: C. Saturation**

Saturation measures how full the system is: how much CPU, memory or I/O capacity is used and whether it is becoming a constraint. The clues are "how much of the available capacity is being used" and "constrained".

**Why the others are wrong:**
- **A. Latency**: Latency is how long a request takes.
- **B. Traffic**: Traffic is how much demand hits the system, such as requests per second.
- **D. Errors**: Errors is the rate of failed requests.

**Remember:** Four golden signals: latency (time), traffic (demand), errors (failures), saturation (how full).

</details>

---

### Exam 3 · Q14

**QuickFare, a ride-booking website, runs its checkout, driver-matching, pricing, and notification features as separate microservices on Google Cloud. The engineering team is investigating slow requests and wants to see how a single customer request moves through each service and how much time is spent at every step. Which Google Cloud tool should they use?**

- A. Cloud Trace
- B. Cloud Profiler
- C. Cloud Logging
- D. Google Kubernetes Engine (GKE)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cloud Trace

**Correct answer: A. Cloud Trace**

Cloud Trace is distributed tracing. It follows a single request as it moves through each microservice and shows how much time each step takes. The clues are "how a single request moves through each service" and "time spent at every step".

**Why the others are wrong:**
- **B. Cloud Profiler**: It shows which code functions use the most CPU or memory, not the request path across services.
- **C. Cloud Logging**: It stores log events but doesn't map a request's timing across services.
- **D. GKE**: It runs containers; it is not an observability tool.

**Remember:** Slow request across microservices = Cloud Trace.

</details>

---

### Exam 3 · Q17

**PulseCart, a mobile shopping app, wants to improve how it releases application updates. The engineering team wants to reduce user disruption when bugs appear after a release. What DevOps practice should PulseCart use while developing its application?**

- A. Pause production until all bugs have been eliminated
- B. Prioritize fixing large bugs during production because they are easier to review
- C. Implement small changes incrementally to reduce recovery time when bugs appear
- D. Implement large changes together to make rolling back easier when bugs appear

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Implement small changes incrementally to reduce recovery time when bugs appear

**Correct answer: C. Implement small changes incrementally to reduce recovery time when bugs appear**

A core DevOps and SRE practice is to ship small, frequent changes. Small changes are easier to test, easier to find the cause of a bug in, and faster to roll back. That reduces disruption to users.

**Why the others are wrong:**
- **A. Pause production until all bugs are gone**: Bug-free software is not realistic; this stops delivery.
- **B. Prioritize fixing large bugs in production**: Large changes and bugs are harder to review, not easier.
- **D. Large changes together make rollback easier**: Large batches make rollback harder and riskier.

**Remember:** Small, incremental releases = faster recovery, less risk.

</details>

---

### Exam 3 · Q18

**CityParkPass, a parking reservation mobile app, has recently launched on Google Cloud. The operations team is reviewing the service’s reliability signals and is specifically tracking how much time passes between a user sending a request and the application returning a response. Which performance metric are they measuring?**

- A. Traffic
- B. Saturation
- C. Latency
- D. Error rate

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Latency

**Correct answer: C. Latency**

Latency is the time between a request and its response. The stem describes exactly that: "how much time passes between a user sending a request and the application returning a response".

**Why the others are wrong:**
- **A. Traffic**: Traffic measures demand, such as requests per second.
- **B. Saturation**: Saturation measures how full the system's resources are.
- **D. Error rate**: Error rate measures how many requests fail.

**Remember:** Wait time = latency.

</details>

---

### Exam 3 · Q21

**QuickCartPay is a payment-processing website that runs business-critical services on Google Cloud in production. The operations team needs the fastest support response for urgent incidents and also wants guidance from a dedicated Technical Account Manager. Which Google Cloud Customer Care service level should QuickCartPay choose?**

- A. Enhanced
- B. Basic
- C. Premium
- D. Standard

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Premium

**Correct answer: C. Premium**

Premium Support is the Customer Care tier for business-critical workloads. It has the fastest response for critical issues and includes a dedicated Technical Account Manager (TAM). The clues are "fastest support response" and "dedicated Technical Account Manager".

**Why the others are wrong:**
- **A. Enhanced**: Faster than Standard, but it has no dedicated TAM and isn't the fastest.
- **B. Basic**: Basic covers billing support and documentation, not technical incident response.
- **D. Standard**: Meant for smaller workloads with slower response times and no TAM.

**Remember:** Fastest response + TAM = Premium.

</details>

---

### Exam 3 · Q25

**MetroNest Apps runs several workloads on Google Cloud for its product, finance, and customer support teams. Recently, leadership noticed that some teams are spending more than expected, but the teams do not clearly see how their usage affects the monthly bill. What should MetroNest Apps do to help control cloud costs?**

- A. Improve the physical server purchasing process to reduce costs.
- B. Share cost views with each department to create more accountability.
- C. Change the cost model from operational expenditure to capital expenditure.
- D. Apply one common tag to every cloud resource.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Share cost views with each department to create more accountability.

**Correct answer: B. Share cost views with each department to create more accountability.**

Teams can't control costs they can't see. Giving each department visibility into its own spending creates accountability and drives better decisions. This is a core FinOps idea: shared responsibility for cloud costs.

**Why the others are wrong:**
- **A. Improve physical server purchasing**: Buying physical servers isn't part of cloud cost control.
- **C. Change from OpEx to CapEx**: Cloud is OpEx by nature; switching models doesn't fix visibility.
- **D. One common tag on every resource**: One tag for everything can't separate costs by team. Labels must differ per team to help.

**Remember:** Visibility per team = accountability = cost control.

</details>

---

### Exam 3 · Q35

**MetroCart, a grocery delivery mobile app, wants to reduce the amount of manual operational work its engineering team performs every week. The team wants to follow a site reliability engineering practice that improves operational efficiency. Which SRE best practice should MetroCart adopt?**

- A. Rely less on operational data when deciding what to improve.
- B. Give developers sole responsibility for production systems.
- C. Reduce the effort spent understanding the impact of outages.
- D. Prioritize automating repetitive toil.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Prioritize automating repetitive toil.

**Correct answer: D. Prioritize automating repetitive toil.**

In SRE, toil is manual, repetitive operational work that adds no lasting value. SRE teams aim to automate it so engineers can spend time on improvements. The clue is "reduce the amount of manual operational work".

**Why the others are wrong:**
- **A. Rely less on operational data**: SRE is data-driven; decisions rely on metrics and SLOs.
- **B. Give developers sole responsibility**: SRE is about shared ownership between developers and operations.
- **C. Reduce effort understanding outages**: SRE uses blameless postmortems to learn from outages, not ignore them.

**Remember:** Manual, repetitive work = toil. SRE answer = automate it.

</details>

---

### Exam 3 · Q36

**CraftlyPay, a creator marketplace, earns most of its revenue from commissions on monthly sales. Because sales volume changes a lot from month to month, the company is having trouble predicting and controlling its Google Cloud costs. How can CraftlyPay optimize the use of its cloud resources?**

- A. By applying intelligent recommendations
- B. By decentralizing financial decision making
- C. By sharing project ownership across all teams
- D. By increasing their capital expenditure

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. By applying intelligent recommendations

**Correct answer: A. By applying intelligent recommendations**

Google Cloud's intelligent recommendations (Active Assist and Recommender) analyze usage and suggest actions, such as resizing oversized VMs or removing idle resources. That helps match resources to changing demand and control costs.

**Why the others are wrong:**
- **B. Decentralizing financial decisions**: This tends to make costs less controlled, not more.
- **C. Sharing project ownership across all teams**: Broad ownership blurs accountability and doesn't optimize resources.
- **D. Increasing capital expenditure**: Buying up front is the opposite of matching cloud use to variable demand.

**Remember:** Variable demand + optimize resources = intelligent recommendations.

</details>

---

### Exam 3 · Q42

**BrightCart, an online shopping platform, is organizing its Google Cloud resource hierarchy. The company has one folder named retail-apps that contains multiple projects for checkout, inventory, and analytics workloads. The cloud administrator plans to apply user access policies at the retail-apps folder level. What will happen to those access policies?**

- A. The policy will be inherited by the projects in the folder but will not affect their resources.
- B. The policy will be inherited by the projects and their resources within the folder.
- C. The policy will be applied to all folders within the organization.
- D. The policy applies to the folder only, and will not be inherited by any projects.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. The policy will be inherited by the projects and their resources within the folder.

**Correct answer: B. The policy will be inherited by the projects and their resources within the folder.**

In the Google Cloud resource hierarchy (organization, folders, projects, resources), policies flow down. A policy set on a folder is inherited by every project in it and by all resources in those projects.

**Why the others are wrong:**
- **A. Inherited by projects but not their resources**: Inheritance continues down to resources.
- **C. Applied to all folders in the organization**: Policies flow down, not up or sideways to other folders.
- **D. Folder only, not inherited**: Inheritance is how the hierarchy works.

**Remember:** Policies flow down the hierarchy: organization, folder, project, resource.

</details>

---

### Exam 3 · Q43

**SkyTrack Logistics runs containerized workloads on GKE, backend services on virtual machines, and several managed Google Cloud services. The operations team wants a single Google Cloud tool to collect, store, search, and analyze custom log entries from these environments. Which Google Cloud tool should SkyTrack Logistics use?**

- A. Dialogflow
- B. Cloud Logging
- C. Cloud SDK
- D. Data Catalog

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Logging

**Correct answer: B. Cloud Logging**

Cloud Logging is the managed service to collect, store, search and analyze logs from GKE, VMs and Google Cloud services, including custom log entries. The clues are "collect, store, search, and analyze" and "log entries".

**Why the others are wrong:**
- **A. Dialogflow**: A tool for building conversational agents and chatbots.
- **C. Cloud SDK**: Command-line tools and libraries for working with Google Cloud.
- **D. Data Catalog**: A metadata service for discovering data assets, not logs.

**Remember:** Logs from anywhere in Google Cloud = Cloud Logging.

</details>

---

### Exam 3 · Q48

**BrightCart, a grocery delivery mobile app, runs multiple backend services on Google Cloud. The developers want a tool that can automatically collect, group, and show application crashes and exceptions as they happen, so they do not have to inspect large volumes of raw logs manually. Which Google Cloud Observability tool should they use?**

- A. Cloud Profiler
- B. Error Reporting
- C. Cloud Trace
- D. Cloud Monitoring

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Error Reporting

**Correct answer: B. Error Reporting**

Error Reporting automatically collects application crashes and exceptions, groups similar ones together, and shows them as they happen. The clue is "collect, group, and show application crashes and exceptions".

**Why the others are wrong:**
- **A. Cloud Profiler**: It shows CPU and memory use by code function.
- **C. Cloud Trace**: It shows request latency across services.
- **D. Cloud Monitoring**: It tracks metrics and alerts, but doesn't group exceptions.

**Remember:** Crashes and exceptions grouped for you = Error Reporting.

</details>

---

### Exam 3 · Q49

**LumaCart, an online marketplace, wants to introduce a camera-based image recognition login feature for its internal support portal. The engineering team wants to release the feature while following SRE principles and reducing risk. What should LumaCart do?**

- A. Roll out the new system to a small group of support employees to test it first.
- B. Roll out the new system to all support employees immediately to collect the maximum amount of usage data.
- C. Avoid rolling out the new system because it may have authentication weaknesses.
- D. Avoid rolling out the new system because it may conflict with privacy requirements.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Roll out the new system to a small group of support employees to test it first.

**Correct answer: A. Roll out the new system to a small group of support employees to test it first.**

SRE favors gradual rollouts, such as a canary release to a small group first. If something goes wrong, only a few users are affected and the change is easy to roll back. The clue is "reducing risk".

**Why the others are wrong:**
- **B. Roll out to everyone immediately**: This maximizes the impact if something breaks.
- **C. Avoid rollout over authentication weaknesses**: SRE manages risk; it doesn't block innovation out of fear.
- **D. Avoid rollout over privacy conflicts**: Same: test and manage the risk rather than refusing to launch.

**Remember:** New feature + reduce risk = roll out to a small group first.

</details>

---

### Exam 3 · Q50

**MealSprint, a food delivery web app, notices that one backend service is causing unusually high cloud costs. The development team wants to inspect the running production application and continuously collect CPU usage and memory-allocation data so they can find which specific code functions are consuming the most resources. Which Google Cloud tool should they use?**

- A. Cloud Logging
- B. Cloud Trace
- C. Error Reporting
- D. Cloud Profiler

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Cloud Profiler

**Correct answer: D. Cloud Profiler**

Cloud Profiler continuously collects CPU and memory-allocation data from running production apps with low overhead. It shows which functions use the most resources. The clues are "CPU usage and memory-allocation" and "which specific code functions".

**Why the others are wrong:**
- **A. Cloud Logging**: It stores log events, not resource use by function.
- **B. Cloud Trace**: It shows request latency across services, not code-level resource use.
- **C. Error Reporting**: It groups crashes and exceptions.

**Remember:** Which code uses the most CPU or memory = Cloud Profiler.

</details>

---

### Exam 4 · Q7

**PixelKart, an online shopping mobile app, runs its checkout service across several containers on Google Kubernetes Engine. The DevOps team suspects that one container is generating errors and wants to search the application’s runtime log entries across all containers to find the issue. Which Google Cloud product should the team use?**

- A. Google Cloud Console
- B. Cloud Trace
- C. Cloud Monitoring
- D. Cloud Logging

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Cloud Logging

**Correct answer: D. Cloud Logging**

Cloud Logging collects, stores and lets you search log entries from applications and Google Cloud services, including GKE containers. The clue is "search the application's runtime log entries across all containers". Logs show the actual error messages each container wrote.

**Why the others are wrong:**
- **A. Google Cloud Console**: The console is the web interface for managing resources; the log search itself is done with Cloud Logging.
- **B. Cloud Trace**: Trace shows how long requests take as they pass through services (latency), not raw log messages.
- **C. Cloud Monitoring**: Monitoring tracks metrics, dashboards and alerts, not the text of individual log entries.

**Remember:** Search log entries / error messages → Cloud Logging. Metrics and alerts → Monitoring. Latency → Trace.

</details>

---

### Exam 4 · Q9

**PulsePay, a payment processing app, wants its engineering team to define the target reliability and performance level that its customer-facing service should meet. In Site Reliability Engineering, what is the term for this desired reliability and performance target?**

- A. Service-level objective
- B. Enhanced support
- C. Scalable infrastructure
- D. Service-level indicator

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Service-level objective

**Correct answer: A. Service-level objective**

A service-level objective (SLO) is the target level of reliability or performance a team commits to, such as 99.9% of checkout requests succeeding. The clue is "target". It is set against a measured indicator (the SLI).

**Why the others are wrong:**
- **B. Enhanced support**: This is a Google Cloud Customer Care support tier, not a reliability target.
- **C. Scalable infrastructure**: This is an infrastructure property, not an SRE term for a reliability goal.
- **D. Service-level indicator**: An SLI is the measurement itself (for example the success rate), not the target.

**Remember:** SLI = what you measure. SLO = the target. SLA = the contract with penalties.

</details>

---

### Exam 4 · Q10

**StreamCart, an online grocery delivery platform, wants its operations team to define the expected target for how reliable and responsive its checkout service should be for customers. In Site Reliability Engineering, which term describes this desired reliability and performance target?**

- A. Service-level objective
- B. Enhanced support
- C. Scalable infrastructure
- D. Service-level indicator

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Service-level objective

**Correct answer: A. Service-level objective**

A service-level objective (SLO) is the target value for reliability and responsiveness, for example 99.9% of checkouts completing in under a set time. The words "expected target" point straight to the SLO. It is the same concept as the previous question with a different company.

**Why the others are wrong:**
- **B. Enhanced support**: This is a paid Customer Care support tier, not a reliability target.
- **C. Scalable infrastructure**: This describes infrastructure that can grow, not an SRE target.
- **D. Service-level indicator**: The SLI is the measured value (like actual latency); the SLO is the goal for it.

**Remember:** "Target" → SLO. "Measurement" → SLI.

</details>

---

### Exam 4 · Q22

**SkyCart Logistics uses Google Cloud to run a package-tracking portal for its customers. The operations team is reviewing reliability targets and wants to understand how cloud service availability is commonly expressed. How is service availability measured in cloud technology?**

- A. Number of available regions
- B. Percentage of uptime
- C. Speed of response time
- D. Number of downtime incidents

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Percentage of uptime

**Correct answer: B. Percentage of uptime**

Availability is the share of time a service is up and working, expressed as a percentage, such as 99.9% or 99.99%. Each extra nine means less allowed downtime. For example, 99.99% allows roughly 52 minutes of downtime a year.

**Why the others are wrong:**
- **A. Number of regions**: More regions can help availability, but they are not how it is measured.
- **C. Speed of response**: Response time is latency, a performance metric, not availability.
- **D. Number of downtime incidents**: The count of incidents ignores how long each one lasted, so it isn't the standard measure.

**Remember:** Availability = % uptime (the "nines").

</details>

---

### Exam 4 · Q25

**PixelQuest Studio runs a cloud-native mobile game called RuneDash on Google Cloud. The team tracks service reliability using service level objectives and error budgets. During the current review period, RuneDash is meeting its service level objective and the team still has plenty of error budget remaining. What should PixelQuest Studio prioritize?**

- A. Innovation to improve user experience
- B. Hardware reliability to improve availability
- C. Stability to avoid prolonged user downtime
- D. Speed to release new features

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Innovation to improve user experience

**Correct answer: A. Innovation to improve user experience**

An error budget is the amount of unreliability the SLO allows (100% − SLO). RuneDash is meeting its SLO and has plenty of budget left, so the service is reliable enough. SRE practice says to spend the remaining budget on innovation: ship improvements and take reasonable risks, because users are already getting the reliability they were promised.

**Why the others are wrong:**
- **B. Hardware reliability**: Reliability work is the priority when the SLO is missed or the budget is used up, not when budget remains.
- **C. Stability to avoid downtime**: Same reason. The service is already within its target.
- **D. Speed to release new features**: Close, but release speed alone isn't the goal. The budget is spent on innovation that improves the user experience, and raw speed can burn the budget carelessly.

**Remember:** Budget left → innovate. SLO missed / budget gone → reliability.

</details>

---

### Exam 4 · Q40

**BrightCart runs an online grocery website on Google Cloud. The engineering team wants to copy important application components across multiple resources so the website can continue operating if one component fails. Which design consideration should BrightCart use?**

- A. Redundancy
- B. Backups
- C. Latency
- D. Security

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Redundancy

**Correct answer: A. Redundancy**

Redundancy means running duplicate copies of important components, such as instances across several zones. If one fails, another keeps serving traffic. The clue is "copy components across multiple resources" so the site "continues operating".

**Why the others are wrong:**
- **B. Backups**: Backups let you restore data later; they don't keep the site running during a failure.
- **C. Latency**: Latency is response delay, not a resilience design.
- **D. Security**: Security protects against threats, not against component failure.

**Remember:** Keep running when something fails → redundancy. Recover lost data → backups.

</details>

---

### Exam 5 · Q15

**NimbusRide runs several customer-facing applications on Google Cloud. The operations team wants to collect application metrics and resource metadata, then view that information in dashboards to understand service performance. Which Google Cloud tool should they use?**

- A. Cloud Monitoring
- B. Cloud Trace
- C. Cloud Logging
- D. Cloud Debugger

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Cloud Monitoring

**Correct answer: A. Cloud Monitoring**

Cloud Monitoring collects metrics, events and metadata from applications and Google Cloud resources. It shows them in dashboards and can send alerts. The clue is "metrics" and "dashboards" to understand performance.

**Why the others are wrong:**
- **B. Cloud Trace**: it follows single requests across services to find latency, not general metrics dashboards.
- **C. Cloud Logging**: it collects and stores log entries, not metrics.
- **D. Cloud Debugger**: it inspected running code state to find bugs (and has been retired).

**Remember:** Metrics + dashboards + alerts = Cloud Monitoring. Logs = Cloud Logging. Latency of a request = Cloud Trace.

</details>

---

### Exam 5 · Q20

**CityPulse Hosting provides a public cloud service used by several small businesses. Its service performance has dropped below the internal service level objective (SLO), but it is still above the contractual service level agreement (SLA). What is the likely result of this service performance change?**

- A. CityPulse Hosting is encouraged to release new feature updates more quickly
- B. CityPulse Hosting is encouraged to focus more on service reliability
- C. Customers experience unexpected or extended service outages
- D. Customers experience lower service latency

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. CityPulse Hosting is encouraged to focus more on service reliability

**Correct answer: B. CityPulse Hosting is encouraged to focus more on service reliability**

The SLO is the internal reliability target. Falling below it usually means the error budget (100% − SLO) is used up. The SRE response is to slow down risky changes and spend effort on reliability until performance is back on target. Being above the SLA means no contract penalty yet.

**Why the others are wrong:**
- **A. Release features faster**: that is what you do when error budget remains, not when the SLO is missed.
- **C. Unexpected or extended outages**: performance is still above the SLA, so customers aren't necessarily seeing major outages.
- **D. Lower latency**: performance dropped, so latency would not improve.

**Remember:** SLO missed = focus on reliability. Budget left = innovate.

</details>

---

### Exam 5 · Q26

**CodeNest Retail, an ecommerce company, runs a production application on Google Cloud. The development team wants to inspect how the application code behaves while it is running and analyze the application’s state to find difficult programming bugs. Which Google Cloud tool should CodeNest Retail use?**

- A. Debugger
- B. Profiler
- C. Cloud Monitoring
- D. Trace

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Debugger

**Correct answer: A. Debugger**

Cloud Debugger let developers inspect the state of running code, such as variable values at a line, without stopping the application. That helps find hard bugs in production. The clue is "inspect how the application code behaves while it is running and analyze the application's state".

**Why the others are wrong:**
- **B. Profiler**: it shows which code uses the most CPU and memory, for performance, not bug state.
- **C. Cloud Monitoring**: it tracks metrics and dashboards, not code state.
- **D. Trace**: it measures request latency across services.

**Remember:** Inspect running code state = Debugger. Resource use by code = Profiler. Latency = Trace.

**⚠️ Note:** Cloud Debugger was shut down in 2023; its open-source successor is Snapshot Debugger. The key describes what it did correctly and the other tools don't fit, so pick it on this exam.

</details>

---

### Exam 5 · Q27

**FitTrack Labs runs several wellness applications on Google Cloud. The operations team wants to collect, view, and store all logs created by these applications and Google Cloud resources in one centralized service. Which Google Cloud service should FitTrack Labs use?**

- A. Cloud Profiler
- B. Cloud Monitoring
- C. Cloud Trace
- D. Cloud Logging

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Cloud Logging

**Correct answer: D. Cloud Logging**

Cloud Logging collects, stores, searches and analyzes logs from applications and Google Cloud resources in one central place. The clue is "collect, view, and store all logs".

**Why the others are wrong:**
- **A. Cloud Profiler**: it analyzes CPU and memory use by code.
- **B. Cloud Monitoring**: it handles metrics, dashboards and alerts, not log storage.
- **C. Cloud Trace**: it measures request latency across services.

**Remember:** Logs = Cloud Logging. Metrics = Cloud Monitoring.

</details>

---

### Exam 6 · Q1

**PulseCart, an online grocery app, runs several Compute Engine VM instances for its order-processing API. The VMs usually stay active for most of each billing month, and the finance team wants to receive sustained use discounts. What should PulseCart do?**

- A. Choose Spot VMs when creating virtual machines.
- B. Choose smaller machine types with lower CPU and memory.
- C. Nothing. Sustained use discounts are automatically applied.
- D. Commit to virtual machine usage for a one-year or three-year period.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Nothing. Sustained use discounts are automatically applied.

**Correct answer: C. Nothing. Sustained use discounts are automatically applied.**

Sustained use discounts (SUDs) are applied automatically to eligible Compute Engine VMs that run for a large part of the billing month. There is no sign-up and no contract. The clue is "stay active for most of each billing month": that usage pattern earns the discount on its own.

**Why the others are wrong:**
- **A. Choose Spot VMs**: Spot VMs are a separate, deeply discounted option for interruptible workloads, not a way to get SUDs, and they can be stopped at any time.
- **B. Choose smaller machine types**: This may lower the bill, but it has nothing to do with qualifying for sustained use discounts.
- **D. Commit for one or three years**: That describes committed use discounts (CUDs), a different program that requires a commitment.

**Remember:** SUD = automatic, for running most of the month. CUD = you sign a 1- or 3-year commitment.

</details>

---

### Exam 6 · Q10

**TrailNest Tours, a travel-booking website, runs several applications on Google Cloud. The operations team wants a service that helps them inspect application events, review error messages, and find the cause of production issues faster. What does Cloud Logging help TrailNest Tours do?**

- A. Analyze live source code and record code update history.
- B. Deploy infrastructure as code.
- C. Analyze logs and accelerate application troubleshooting.
- D. Manage the storage of custom VM images.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Analyze logs and accelerate application troubleshooting.

**Correct answer: C. Analyze logs and accelerate application troubleshooting.**

Cloud Logging collects, stores, searches, and analyzes log data from applications and Google Cloud services in one place. Teams use it to review events and error messages and find the root cause of problems faster. The stem's clues are "inspect application events," "review error messages," and "find the cause of production issues."

**Why the others are wrong:**
- **A. Analyze source code and record update history**: That is the job of source control and code repositories, not logging.
- **B. Deploy infrastructure as code**: That is done with tools like Terraform, not Cloud Logging.
- **D. Manage custom VM images**: Custom images are managed in Compute Engine, not in Cloud Logging.

**Remember:** Logs in one place, faster troubleshooting → Cloud Logging. Metrics and alerts → Cloud Monitoring.

</details>

---

### Exam 6 · Q19

**TrailSnap, a travel booking website, runs several services in Google Cloud. The operations team wants to keep records of application errors, operating system messages, service activity, and other events so they can review what happened during troubleshooting. What is logging within the context of cloud technology?**

- A. Recording application and operating system events as timestamped entries
- B. Monitoring network and resource limitations
- C. Tracking source code across an organization
- D. Recording infrastructure and hardware expenditure

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Recording application and operating system events as timestamped entries

**Correct answer: A. Recording application and operating system events as timestamped entries**

Logging means recording what happened, when it happened: errors, OS messages, requests and other events. Each entry has a timestamp and can be plain text or structured data. The team can then search and review the history while troubleshooting. On Google Cloud this is Cloud Logging.

**Why the others are wrong:**
- **B. Monitoring network and resource limits**: That's monitoring with metrics, such as saturation, not logging.
- **C. Tracking source code**: That's version control, for example Git repositories.
- **D. Recording hardware expenditure**: That's billing and cost reporting.

**Remember:** Logs = what happened (events). Metrics = how much (numbers over time).

</details>

---

### Exam 6 · Q32

**GreenStay Hotels, a hospitality platform, expects a large increase in booking traffic during its summer travel campaign. The company wants to scale computing capacity quickly while also supporting its environmental sustainability goals. What should GreenStay Hotels do?**

- A. Rewrite the application code so that it consumes less energy.
- B. Use a public cloud provider that operates energy-efficient data centers.
- C. Switch the existing on-premises data center to a carbon-neutral energy supplier.
- D. Buy energy-efficient physical servers for the existing on-premises data center.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use a public cloud provider that operates energy-efficient data centers.

**Correct answer: B. Use a public cloud provider that operates energy-efficient data centers.**

A public cloud gives near-instant extra capacity for traffic peaks, without buying hardware. At the same time, large providers like Google run highly energy-efficient data centers and invest heavily in carbon-free energy. One choice meets both goals in the stem: "scale computing capacity quickly" and "sustainability goals."

**Why the others are wrong:**
- **A. Rewrite the code to use less energy**: This may help sustainability a little, but it is slow and does not add capacity.
- **C. Carbon-neutral supplier for on-premises**: This helps sustainability but does not solve fast scaling.
- **D. Buy efficient on-premises servers**: Buying hardware is slow and costly, and capacity sits idle after the peak.

**Remember:** Scale fast + sustainability → cloud provider with energy-efficient data centers.

</details>

---

### Exam 6 · Q43

**FreshBite, a food delivery website, has separate software development and operations teams that use different tools and processes. The company wants to reduce delays, misunderstandings, and production issues caused by these teams working in isolation. How can improving communication between the teams help reduce these silo-related problems?**

- A. By identifying who caused each incident and applying penalties
- B. By merging all development and operations duties into one identical job role
- C. By adding stronger encryption controls to improve team workflows
- D. By promoting shared responsibility for business results

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. By promoting shared responsibility for business results

**Correct answer: D. By promoting shared responsibility for business results**

DevOps culture breaks down silos by making development and operations jointly responsible for delivering and running reliable software. When both teams share the same goals, they communicate more, hand off less, and fix issues together. The clue is "teams working in isolation" causing "delays, misunderstandings, and production issues."

**Why the others are wrong:**
- **A. Identify who caused incidents and apply penalties**: Blame makes people hide problems. DevOps and SRE favor blameless culture.
- **B. Merge all duties into one identical role**: DevOps aligns teams. It does not require everyone to do the exact same job.
- **C. Stronger encryption controls**: Encryption is a security measure and does nothing for team communication.

**Remember:** Silos are fixed by shared responsibility for outcomes, not by blame.

</details>

---

### Exam 6 · Q50

**GameNest, a browser-based multiplayer game platform, released a new version of its matchmaking feature. After launch, the engineering team discovered a small issue that affects a limited number of players but does not cause a major outage. The team wants to handle the issue according to SRE principles. How should GameNest approach this bug?**

- A. Accept and learn from the bug because failure is normal
- B. Accept and ignore the bug because it is only minor
- C. Hold a postmortem to reprimand the employee responsible for the bug
- D. Document bug correction to eliminate all future bugs

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Accept and learn from the bug because failure is normal

**Correct answer: A. Accept and learn from the bug because failure is normal**

Site Reliability Engineering (SRE) accepts that no system is 100% reliable. Failures will happen, so teams fix the problem and learn from it, often through a blameless postmortem, to make the system more reliable. The clue is "handle the issue according to SRE principles" for a small, non-critical bug.

**Why the others are wrong:**
- **B. Accept and ignore the bug**: SRE accepts failure but does not ignore it. Every issue is a chance to learn and improve.
- **C. Postmortem to reprimand the employee**: SRE postmortems are blameless. They focus on systems and processes, not punishing people.
- **D. Eliminate all future bugs**: Zero bugs is unrealistic. SRE manages risk with error budgets instead of aiming for perfection.

**Remember:** Failure is normal: accept it, learn from it, run blameless postmortems.

</details>

---
