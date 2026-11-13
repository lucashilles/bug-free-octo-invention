# Questions You Missed

Your incorrect answers across all exams, grouped by domain.

## [Domain 1] Exam 2 · Q20

Your organization is building a CI/CD pipeline that deploys Google Cloud resources with Terraform. The CI/CD tooling runs on Google Kubernetes Engine (GKE), and each pipeline run executes in its own ephemeral Pod. You need to make sure that the pipelines running in these Pods hold the right Identity and Access Management (IAM) permissions to carry out the Terraform deployments, and you want to follow Google-recommended practices for identity management. Which two actions should you take? (Choose two.)

- **Your answer:** 
- **Correct:** A. Create a Kubernetes service account, associate it with the Pods, and use Workload Identity Federation for GKE to authenticate as the Google service account. | C. Create a Google service account and grant it the IAM permissions that the deployments require.

See full explanation in [01-bootstrapping-gcp-organization.md](01-bootstrapping-gcp-organization.md).

---

## [Domain 2] Exam 2 · Q21

You need to build a CI/CD pipeline in Google Cloud for a containerized application. Your development team practices trunk-based development with a central Git repository. You want every new version of the application to pass through all of your tests in the pipeline so that quality improves. What should you do?

- **Your answer:** A. First, install a Git hook that requires developers to run unit tests before pushing code to the central repository. Second, trigger Cloud Build to build the application container, deploy it to a testing environment, and run integration tests. Third, if the integration tests pass, deploy the container to production and run acceptance tests.
- **Correct:** D. First, trigger Cloud Build to run unit tests whenever code is pushed, and if all unit tests pass, build the application container and push it to a central registry. Second, trigger Cloud Build to deploy the container to a testing environment and run integration tests and acceptance tests. Third, if all tests pass, have the pipeline deploy the application to production and run smoke tests.

See full explanation in [02-cicd-pipelines.md](02-cicd-pipelines.md).

---

## [Domain 2] Exam 5 · Q2

You use a **multi-step Cloud Build pipeline** to build and deploy your application to **Google Kubernetes Engine (GKE)**. You want to **integrate with a third-party monitoring platform** by performing an **HTTP POST of the build information to a webhook**. You want to **minimize development effort**.

What should you do?

- **Your answer:** **C.** Use **Cloud Logging** to create a **logs-based metric** from the **Cloud Build logs**. Create an **alert** with a **Webhook notification type**.
- **Correct:** **D.** Create a **Cloud Pub/Sub push subscription** to the **Cloud Build**`**cloud-builds**`**Pub/Sub topic** to **HTTP POST the build information** to a webhook.

See full explanation in [02-cicd-pipelines.md](02-cicd-pipelines.md).

---

## [Domain 2] Exam 5 · Q19

**You're set to deploy a new feature of a web-based application to production and wish to utilize Google Kubernetes Engine (GKE) for a phased rollout to half of the web server pods. What is the optimal course of action?**

- **Your answer:** III. Utilize a replica set within the deployment specification.
- **Correct:** I. Employ a partitioned rolling update method.

See full explanation in [02-cicd-pipelines.md](02-cicd-pipelines.md).

---

## [Domain 2] Exam 5 · Q21

**During the migration of an on-premises containerized web application to Google Cloud, considering specific traffic direction and testing needs, which deployment strategy and platform should you opt for?**

- **Your answer:** I. Implement the canary release on Cloud Run, employing traffic splitting to route 10% of user traffic to the canary release based on the revision tag.
- **Correct:** IV. Opt for Google Kubernetes Engine with Anthos Service Mesh for deploying the canary release, employing traffic splitting to direct 10% of user traffic to the new version based on the user-agent header configured in the virtual service.

See full explanation in [02-cicd-pipelines.md](02-cicd-pipelines.md).

---

## [Domain 3] Exam 2 · Q7

Your team is writing a postmortem after an incident on your externally facing application. The team wants to improve its postmortem policy by adding triggers that indicate when an incident requires a postmortem. Based on Site Reliability Engineering (SRE) practices, which triggers should the policy define? (Choose two.)

- **Your answer:** 
- **Correct:** B. An incident results in data loss. | C. A request for a postmortem comes from an internal stakeholder.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 2 · Q10

Your organization wants to raise an application’s availability target from 99.9% to 99.99%, and the improvement would cost $2,000. The application currently generates $1,000,000 in revenue. You need to decide whether the higher availability is worth the investment over a single year of use. What should you do?

- **Your answer:** D. Calculate the value of the improved availability as $9,000, and conclude that the improvement is worth the investment.
- **Correct:** A. Calculate the value of the improved availability as $900, and conclude that the improvement is not worth the investment.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 2 · Q12

Your company runs an ecommerce website built from JVM-based applications in a microservice architecture on Google Kubernetes Engine (GKE). Traffic rises during the day and falls overnight. Your operations team currently runs enough Pods to cover the evening peak at all times. You want to automate scaling so that only the Pods and nodes needed for the current load are running. What should you do?

- **Your answer:** C. Set up the Horizontal Pod Autoscaler and leave the node pool at a fixed size.
- **Correct:** D. Set up the Horizontal Pod Autoscaler and turn on the cluster autoscaler.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 2 · Q23

You operate a globally used service that has a 99% availability target, and your team has limited engineering capacity. For the current calendar month, measured availability is 99.5%. You need to keep the service within its defined availability goals while staying able to respond to business changes, including an upcoming launch of new features. You must also reduce technical debt and keep operational costs low, and you want to follow Google-recommended practices. What should you do?

- **Your answer:** C. Establish an error budget for the service’s availability target and work to minimize the remaining error budget.
- **Correct:** B. Identify, quantify, and eliminate toil by automating repetitive operational tasks.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 2 · Q27

Your team runs microservices on Google Kubernetes Engine (GKE). You want to detect when your error budget is being consumed so that you can protect customers and establish release policies. What should you do?

- **Your answer:** A. Derive SLIs from metrics, and enable alerting policies to fire when the services fail to pass.
- **Correct:** C. Define an SLO, and create an alerting policy on select_slo_burn_rate.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 2 · Q31

You support a service that has a well-defined Service Level Objective (SLO). Over the past six months, the service has consistently met its SLO and customer satisfaction has remained high. Most of its operational tasks are automated, so few repetitive tasks occur often. You want to optimize the balance between reliability and deployment velocity while following site reliability engineering (SRE) best practices. Which two actions should you take? (Choose two.)

- **Your answer:** 
- **Correct:** B. Raise the service’s deployment velocity and/or accepted risk. | C. Reassign engineering time to other services that need greater reliability.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 2 · Q33

You support a user-facing web application. When you analyze its error budget for the past six months, you find that it has never used more than 5% of its error budget in any given time window. You hold a Service Level Objective (SLO) review with business stakeholders and confirm that the SLO is set appropriately. You want the application’s SLO to reflect its observed reliability more closely. Which two steps can you take to further that goal while balancing velocity, reliability, and business needs? (Choose two.)

- **Your answer:** 
- **Correct:** B. Make application releases more frequent or potentially riskier. | E. Announce planned downtime to use up more of the error budget, and make sure users are not depending on a tighter SLO.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 5 · Q12

**Your team has recently deployed an NGINX-based application into Google Kubernetes Engine (GKE) and has exposed it to the public via an HTTP Google Cloud Load Balancer (GCLB) ingress.**

**You want to scale the deployment of the application's frontend using an appropriate Service Level Indicator (SLI).**

**What should you do?**

- **Your answer:** **D.** Expose the **NGINX stats endpoint** and configure the **horizontal pod autoscaler** to use the **request metrics** exposed by the **NGINX deployment**.
- **Correct:** **C.** **Install the Cloud Monitoring (formerly Stackdriver) custom metrics adapter** and configure a **horizontal pod autoscaler (HPA) to use the number of requests** provided by the **Google Cloud Load Balancer (GCLB)**.

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 3] Exam 5 · Q15

**You support a web application hosted on Compute Engine that provides a booking service for thousands of users.**

**Shortly after the release of a new feature, your monitoring dashboard shows that all users are experiencing latency at login.**

**You want to mitigate the impact of the incident on the users of your service.**

**What should you do first?**

- **Your answer:** **B. Review Cloud Monitoring.**
- **Correct:** **A. Roll back the recent release.**

See full explanation in [03-sre-practices.md](03-sre-practices.md).

---

## [Domain 4] Exam 1 · Q1

You manage an application that exposes an HTTP endpoint directly, without a load balancer in front of it. HTTP response latency is critical to the user experience, and you want visibility into the latencies that all of your users are experiencing. You use Cloud Monitoring. What should you do?

- **Your answer:** A. In your application, create a metric with `metricKind` set to `DELTA` and `valueType` set to `DOUBLE`. In Cloud Monitoring’s Metrics Explorer, use a Stacked Bar chart to visualize the metric.
- **Correct:** C. In your application, create a metric with `metricKind` set to `GAUGE` and `valueType` set to `DISTRIBUTION`. In Cloud Monitoring’s Metrics Explorer, use a Heatmap chart to visualize the metric.

See full explanation in [04-observability-troubleshooting.md](04-observability-troubleshooting.md).

---

## [Domain 4] Exam 2 · Q25

Your company’s Google Cloud resource hierarchy has separate folders for production, test, and development. The cyber security team is reviewing the organization’s Google Cloud security posture and wants to find and resolve security issues faster. You need to consolidate the logs generated by Google Cloud services across all projects that sit only within the production folder, so the team can configure alerting and perform near-real-time analysis. What should you do?

- **Your answer:** C. Create an aggregated log sink on the production folder that routes to a Pub/Sub topic.
- **Correct:** D. Create an aggregated log sink on the production folder that routes to a Cloud Logging bucket.

See full explanation in [04-observability-troubleshooting.md](04-observability-troubleshooting.md).

---

## [Domain 4] Exam 2 · Q26

Your organization needs to collect system logs from its Google Cloud project to power dashboards in Google Cloud Observability. You must configure every current and future Compute Engine instance to collect these system logs, and you must make sure the Ops Agent stays up to date. What should you do?

- **Your answer:** B. On the Cloud Monitoring VM Instances dashboard, select every VM whose agent status is Not detected, then choose the option to install agents.
- **Correct:** C. Use the Google Cloud CLI to create an agent policy.

See full explanation in [04-observability-troubleshooting.md](04-observability-troubleshooting.md).

---

## [Domain 4] Exam 5 · Q1

You created a **Cloud Monitoring chart for CPU utilization** in a **dashboard** within your **workspace project**. You want to **share the chart with your Site Reliability Engineering (SRE) team only**. You want to ensure that you **follow the principle of least privilege**. What should you do?

- **Your answer:** **IV.** Click **“Share chart by URL”** and provide the **URL** to the **SRE team**. Assign the **SRE team** the **Dashboard Viewer IAM role** in the workspace project.
- **Correct:** **III.** Click **“Share chart by URL”** and provide the **URL** to the **SRE team**. Assign the **SRE team** the **Monitoring Viewer IAM role** in the workspace project.

See full explanation in [04-observability-troubleshooting.md](04-observability-troubleshooting.md).

---

## [Domain 5] Exam 5 · Q4

**You manage the backend infrastructure of a mobile game running on a Google Kubernetes Engine (GKE) cluster, serving HTTP requests from users. To optimize network expenses, what step should you take?**

- **Your answer:** IV. Implement a Google Cloud HTTP Load Balancer as Ingress.
- **Correct:** II. Set up your network services on the Standard Tier.

See full explanation in [05-performance-and-cost.md](05-performance-and-cost.md).

---
