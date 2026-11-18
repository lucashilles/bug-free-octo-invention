# Domain 4 — Analyzing and Optimizing Technical and Business Processes

38 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q5

**Your company wants to further reduce the number of unplanned rollbacks of erroneous production deployments in its web hosting platform. Improvements to the QA and testing processes have already achieved an 80% reduction. Which two additional approaches can help minimize rollbacks? (Choose two.)**

- A. Implement a blue-green deployment strategy.
- B. Replace the QA environment with canary releases.
- C. Break down the monolithic platform into microservices.
- D. Minimize the platform’s reliance on relational database systems.
- E. Migrate from relational database systems to a NoSQL database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Implement a blue-green deployment strategy. **|** C. Break down the monolithic platform into microservices.

**Correct Answers:**

**A. Implement a blue-green deployment strategy.**
**C. Break down the monolithic platform into microservices.**

**Explanation for Correct Choices:**

**A. Implement a blue-green deployment strategy.** ✅

- **Blue-green deployments** allow for **zero-downtime releases** by maintaining two separate environments:
  - **Blue**: The current production environment.
  - **Green**: The new environment with the updated version.
- Traffic can be **switched between versions** only after validation, reducing **erroneous rollbacks** in production.
- If an issue is detected, **rolling back to the previous (stable) version is instantaneous**.
- This approach is a **Google Cloud-recommended deployment strategy** for reliability.

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**C. Break down the monolithic platform into microservices.** ✅

- Migrating from a **monolithic** to a **microservices architecture**:
  - **Reduces the blast radius** of failures by isolating components.
  - Enables **incremental deployments**, where only a small portion of the system is updated instead of the entire platform.
  - Allows for **easier rollbacks** and **smaller, independent teams** to deploy safely.
- Microservices **improve agility** and **reduce the risk of widespread failures**, leading to fewer unplanned rollbacks.

✅ **Reference:**

- **https://cloud.google.com/microservices**

**Why Other Options Are Incorrect:**

**B. Replace the QA environment with canary releases.** ❌

- **Canary releases** are useful for **gradual rollouts**, but **removing the QA environment entirely is not a best practice**.
- A QA environment is crucial for **pre-deployment validation**; eliminating it **increases production risks** rather than reducing rollbacks.

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**D. Minimize the platform’s reliance on relational database systems.** ❌

- The **database system itself is not the root cause** of unplanned rollbacks.
- **Reducing reliance on relational databases** may improve **scalability**, but it does not directly prevent **deployment rollbacks**.
- The **deployment process and application architecture** are the primary areas for reducing rollbacks.

✅ **Reference:**

- **https://cloud.google.com/sql/docs**

**E. Migrate from relational database systems to a NoSQL database.** ❌

- Migrating to NoSQL is **not a direct solution** to reducing erroneous rollbacks.
- NoSQL databases are **useful for scalability and flexibility**, but changing the database type does not inherently reduce **failed deployments**.
- A migration could introduce **more risk** and **require significant re-architecting**, potentially increasing **failures** during the transition.

✅ **Reference:**

- **https://cloud.google.com/databases/docs/choosing-database**

**Conclusion:**

The best strategies to **further minimize unplanned rollbacks** are:

1. **Implementing a blue-green deployment strategy** for **safe, reversible** rollouts (**Option A**).
2. **Breaking down the monolithic platform into microservices** for **isolated, incremental deployments** (**Option C**).

📌 **Final Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**
- **https://cloud.google.com/microservices**

</details>

---

### Exam 1 · Q6

**To reduce costs, the Director of Engineering has mandated that all developers migrate their development infrastructure from on-premises virtual machines (VMs) to Google Cloud Platform. These resources experience multiple start/stop cycles throughout the day and require persistent state. You have been tasked with designing a solution for running a development environment in Google Cloud while ensuring cost visibility for the finance team. Which two actions should you take? (Choose two.)**

- A. Use the `--no-auto-delete` flag on all persistent disks and stop the VM.
- B. Use the `--auto-delete` flag on all persistent disks and terminate the VM.
- C. Apply a VM CPU utilization label and include it in the BigQuery billing export.
- D. Leverage Google BigQuery billing export and labels to track costs by groups.
- E. Store all state in local SSD, snapshot the persistent disks, and terminate the VM.
- F. Store all state in Google Cloud Storage, snapshot the persistent disks, and terminate the VM.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use the `--no-auto-delete` flag on all persistent disks and stop the VM. **|** D. Leverage Google BigQuery billing export and labels to track costs by groups.

**Correct options: A and D**

- **A. Use the `--no-auto-delete` flag on all persistent disks and stop the VM.**
  *Why:* Dev VMs need state to persist across frequent start/stop cycles. Setting **no auto-delete** on Persistent Disks ensures disks aren’t deleted when the instance stops/terminates; stopping the VM saves compute cost while retaining the disk state for the next start.
  Ref: Stop/Start instances & disk persistence: [https://cloud.google.com/compute/docs/instances/stop-start-instance](https://cloud.google.com/compute/docs/instances/stop-start-instance)
- **D. Leverage BigQuery billing export and labels to track costs by groups.**
  *Why:* Finance needs visibility. Enable **Cloud Billing export to BigQuery** and apply **resource labels** (e.g., `env=dev`, `team=payments`) so you can attribute and report costs by team/project/group with SQL.
  Ref: Track costs with labels + BigQuery export: [https://cloud.google.com/billing/docs/how-to/export-data-bigquery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)

Why not the others

- **B** auto-deletes disks → loses dev state.
- **C** “CPU utilization label” isn’t a thing; labels are arbitrary key/values, not dynamic metrics.
- **E/F** rely on local SSD (ephemeral) or extra snapshot flows/GCS—more ops overhead and not necessary for simple persistent dev environments.

</details>

---

### Exam 1 · Q20

**Your company's user-feedback portal runs on a standard LAMP stack replicated across two zones in the us-central1 region. It is deployed using autoscaled managed instance groups for all layers except the database. Currently, only a small group of selected customers have access, and the portal meets a 99.99% availability SLA under these conditions.**

**Next quarter, the portal will be opened to all users, including unauthenticated users. To ensure the system maintains its SLA under increased load, you need to develop a resiliency testing strategy. What approach should you take?**

- A. Capture existing user input and **replay the recorded user load** until autoscaling is triggered on all layers. Simultaneously, terminate all resources in one of the zones.
- B. Generate **synthetic random user input**, replay the synthetic load until **autoscaling logic** is triggered on at least one layer, and introduce **chaos** by randomly terminating resources in both zones.
- C. Gradually **increase the exposure** of the new system to a larger user group, expanding the group daily until autoscaling is triggered on all layers. At the same time, terminate random resources in both zones.
- D. Capture existing user input, **replay the recorded load** until resource utilization exceeds **80%**, estimate the expected number of users based on current usage patterns, and provision enough resources to handle **200% of the projected load**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Gradually **increase the exposure** of the new system to a larger user group, expanding the group daily until autoscaling is triggered on all layers. At the same time, terminate random resources in both zones.

**Correct Answer:**

**C. Gradually increase the exposure of the new system to a larger user group, expanding the group daily until autoscaling is triggered on all layers. At the same time, terminate random resources in both zones.**

**Explanation:**

To **ensure 99.99% availability under increased load**, a **gradual rollout strategy** combined with **resiliency testing** is the best approach.

✅ **Why This Works:**

1. **Controlled Traffic Increase**: Gradually expanding user access allows for **monitoring and scaling adjustments** before full exposure.
2. **Observing Autoscaling Behavior**: Ensures that **autoscaling works as expected** across all layers before full public access.
3. **Resiliency Testing via Chaos Engineering**:
  - **Randomly terminating resources** tests fault tolerance and ensures that the system **handles failures gracefully**.
  - **Multi-zone replication** ensures availability despite failures in one zone.
4. **Prevents Overprovisioning**: Instead of blindly **provisioning 200% capacity**, this method allows **dynamic scaling based on real-world traffic patterns**.

✅ **Supporting Documentation:**

- **Google Cloud Autoscaling Best Practices:**
  **https://cloud.google.com/compute/docs/autoscaler**
- **Chaos Engineering on Google Cloud:**
  **https://cloud.google.com/blog/products/management-tools/chaos-engineering-and-google-cloud**

**Why Other Options Are Incorrect:**

**A. Capture existing user input and replay the recorded user load until autoscaling is triggered on all layers. Simultaneously, terminate all resources in one of the zones.** ❌

- **Why Incorrect?**
  - **Capturing existing user input is good for load testing**, but the **traffic profile changes when access is expanded to all users**.
  - **Immediately terminating an entire zone** is **too extreme** and **not realistic** for gradual traffic expansion.
  - The **gradual rollout strategy (Option C) is safer and better aligns with real-world production conditions**.

✅ **Reference:**

- **https://cloud.google.com/architecture/scalable-and-resilient-applications**

**B. Generate synthetic random user input, replay the synthetic load until autoscaling logic is triggered on at least one layer, and introduce chaos by randomly terminating resources in both zones.** ❌

- **Why Incorrect?**
  - **Synthetic load** is **less accurate** than gradually **expanding real user traffic**.
  - **Chaos engineering is important**, but it should be introduced **gradually**, not as the **primary focus**.
  - **Real user behavior is critical for autoscaling validation**, making **Option C a better choice**.

✅ **Reference:**

- **https://cloud.google.com/architecture/chaos-engineering-on-google-cloud**

**D. Capture existing user input, replay the recorded load until resource utilization exceeds 80%, estimate the expected number of users based on current usage patterns, and provision enough resources to handle 200% of the projected load.** ❌

- **Why Incorrect?**
  - **Overprovisioning resources is not cost-efficient** and **does not ensure autoscaling is working properly**.
  - **Traffic patterns will change** once unauthenticated users access the portal, making projections **unreliable**.
  - **Google Cloud autoscaler dynamically scales resources**, making **pre-provisioning unnecessary**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/autoscaler**

**Conclusion:**

The best approach is **C. Gradually increase user exposure while monitoring autoscaling and performing resiliency testing**. This method:

- **Validates real-world autoscaling behavior**.
- **Avoids sudden failures from excessive chaos testing**.
- **Ensures high availability while efficiently scaling resources**.

📌 **Final Reference:**
**https://cloud.google.com/architecture/scalable-and-resilient-applications**

</details>

---

### Exam 1 · Q21

**Your solution is encountering **performance issues in production** that were not observed in **staging or test environments**. You need to refine your **testing and deployment** procedures to **prevent this issue in the future**. What should you do?**

- A. Reduce the number of changes deployed to production.
- B. Deploy smaller, incremental changes to production.
- C. Increase the load on your **test and staging** environments.
- D. Gradually deploy changes to a **small subset of users** before rolling out to production.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Gradually deploy changes to a **small subset of users** before rolling out to production.

**Correct Answer:**

**D. Gradually deploy changes to a small subset of users before rolling out to production.**

**Explanation:**

To prevent **performance issues in production**, the best approach is to implement a **gradual rollout strategy**, also known as **canary releases** or **progressive delivery**.

✅ **Why This Works:**

- **Minimizes risk:** Deploying changes to a **small subset of users** first allows **early detection of issues** before affecting all users.
- **Real-world traffic testing:** Unlike staging or test environments, production users generate **actual workloads and edge cases** that may not have been captured in testing.
- **Fast rollback mechanism:** If issues are detected, the deployment can be **paused or rolled back** before a full rollout.
- **Automated monitoring & feedback:** Tools like **Stackdriver (Cloud Monitoring, Logging, and Trace)** help track **latency, error rates, and performance metrics** during gradual deployment.

✅ **Best Practices for Gradual Rollout:**

- **Use feature flags** (e.g., LaunchDarkly) to control feature exposure.
- **Deploy changes to a percentage of users** before full release.
- **Monitor performance metrics before continuing rollout.**

✅ **Supporting Documentation:**

- **Google Cloud Canary Deployment Guide:**
  **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**Why Other Options Are Incorrect:**

**A. Reduce the number of changes deployed to production.** ❌

- **Incorrect because reducing changes does not address the root cause of performance issues.**
- **Even small changes can introduce issues if not tested properly in a production-like environment.**
- The **real problem is insufficient production-level testing**, not the volume of changes.

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**B. Deploy smaller, incremental changes to production.** ❌

- **Smaller changes are beneficial but do not prevent performance issues alone.**
- **Gradual rollout (Option D) is still needed** to test changes in production conditions before full deployment.
- **Incremental changes help debugging but do not guarantee real-world performance testing.**

✅ **Reference:**

- **https://cloud.google.com/architecture/devops/devops-tech-continuous-deployment**

**C. Increase the load on your test and staging environments.** ❌

- **Test and staging environments cannot fully replicate production workloads.**
- Even if you simulate high traffic, **real user behavior and production-specific configurations** may differ.
- **Canary releases (Option D) provide a more reliable way to test in a live environment.**

✅ **Reference:**

- **https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

**Conclusion:**

The best approach is **D. Gradually deploy changes to a small subset of users before rolling out to production**, as it:

- **Identifies performance issues in real-world conditions.**
- **Reduces risk before full rollout.**
- **Allows monitoring and quick rollback if issues arise.**

📌 **Final Reference:**
**https://cloud.google.com/architecture/application-deployment-and-testing-strategies**

</details>

---

### Exam 1 · Q23

**During a **high-traffic period**, one of your **relational databases** crashes, but the **replica is never promoted to master**. You want to prevent this issue from happening again in the future. What should you do?**

- A. Switch to a different database.
- B. Use larger instance sizes for the database.
- C. Increase the frequency of database snapshots.
- D. Implement **routinely scheduled failovers** for your databases.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Implement **routinely scheduled failovers** for your databases.

**Correct Answer:**

**D. Implement routinely scheduled failovers for your databases.**

**Explanation:**

To ensure **high availability and automatic failover** for relational databases, **routinely scheduled failover testing** is essential. This ensures that **replica promotion** works as expected during high-traffic periods or failures.

✅ **Why This Works:**

- **Regular failover tests validate automatic promotion** of replicas, ensuring the process works during actual failures.
- **Helps identify misconfigurations** in failover mechanisms, such as **missing IAM permissions or misconfigured replication settings**.
- **Prevents downtime during real failures** by ensuring **read replicas can be promoted to primary**.
- **Google Cloud SQL, Cloud Spanner, and other managed relational databases support automated failover testing.**

✅ **Supporting Documentation:**

- **High Availability for Cloud SQL:**
  **https://cloud.google.com/sql/docs/mysql/high-availability**
- **Testing Cloud SQL Failover:**
  **https://cloud.google.com/sql/docs/mysql/failover**

**Why Other Options Are Incorrect:**

**A. Switch to a different database.** ❌

- **Changing the database is not necessary**—Google Cloud SQL, Cloud Spanner, and self-managed databases **already support failover**.
- **The issue is likely a misconfiguration or untested failover process**, not the database itself.
- **Fixing failover procedures is a better solution than migrating databases.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**B. Use larger instance sizes for the database.** ❌

- **Scaling the database may improve performance but does not guarantee failover works correctly.**
- **Failover is unrelated to instance size**—a misconfigured failover will still fail, even with larger instances.
- **High availability and replication settings are more critical than instance size.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/instance-settings**

**C. Increase the frequency of database snapshots.** ❌

- **Snapshots help with backups but do not prevent failover issues.**
- **Snapshots do not provide real-time failover**—they are used for recovery, which can lead to **downtime during restoration**.
- **Failover should be handled via automated replica promotion, not snapshots.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/backup-recovery/backups**

**Conclusion:**

The best solution is **D. Implement routinely scheduled failovers**, as it:

- **Ensures automatic failover works as expected**.
- **Prevents downtime during real failures**.
- **Identifies and resolves failover misconfigurations in advance**.

📌 **Final Reference:**
**https://cloud.google.com/sql/docs/mysql/failover**

</details>

---

### Exam 1 · Q28

**A lead engineer has developed a custom tool for deploying virtual machines in the legacy data center and now wants to migrate it to the cloud. You want to advocate for using Google Cloud Deployment Manager instead. What are two business risks associated with migrating to Cloud Deployment Manager? (Choose two.)**

- A. Cloud Deployment Manager relies on **Python**.
- B. Cloud Deployment Manager **APIs could be deprecated** in the future.
- C. Cloud Deployment Manager is **unfamiliar to the company's engineers**.
- D. Cloud Deployment Manager requires a **Google APIs service account** to operate.
- E. Cloud Deployment Manager **can permanently delete cloud resources**.
- F. Cloud Deployment Manager **only automates Google Cloud resources**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Cloud Deployment Manager **APIs could be deprecated** in the future. **|** C. Cloud Deployment Manager is **unfamiliar to the company's engineers**.

**Correct Answers:**

**B. Cloud Deployment Manager APIs could be deprecated in the future.**
**C. Cloud Deployment Manager is unfamiliar to the company's engineers.**

**Explanation:**

When advocating for **Google Cloud Deployment Manager**, it's important to consider **business risks** that could affect adoption and long-term sustainability.

✅ **Why These Are Business Risks?**

1️⃣ **B. Cloud Deployment Manager APIs could be deprecated in the future.**

- **Google occasionally deprecates services** when better alternatives emerge.
- Deployment Manager is **not actively updated** and **Google recommends Terraform** for infrastructure as code (IaC).
- If **Deployment Manager is deprecated**, the company may need to **migrate to Terraform or another tool**, increasing costs and effort.

✅ **Supporting Documentation:**

- **https://cloud.google.com/deployment-manager/docs/moving-to-terraform**

2️⃣ **C. Cloud Deployment Manager is unfamiliar to the company's engineers.**

- **Requires retraining and ramp-up time**, impacting productivity.
- The **lead engineer already has a custom deployment tool**, meaning resistance to change is possible.
- **Terraform is more widely adopted** and supports **multi-cloud deployments**, making it a more future-proof choice.

✅ **Supporting Documentation:**

- **https://cloud.google.com/docs/terraform**

**Why Other Options Are Incorrect?**

**A. Cloud Deployment Manager relies on Python.** ❌

- **Incorrect** because Deployment Manager **uses YAML and Jinja2 templates**, with **optional Python support**.
- **Python is not mandatory**—most configurations can be done in YAML alone.

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs/configuration/supported-python-runtime**

**D. Cloud Deployment Manager requires a Google APIs service account to operate.** ❌

- **Not a significant business risk** because **service accounts are a standard practice** for infrastructure automation tools.
- **Other IaC tools like Terraform also require service accounts** for authentication.

✅ **Reference:**

- **https://cloud.google.com/iam/docs/service-accounts**

**E. Cloud Deployment Manager can permanently delete cloud resources.** ❌

- **Not a risk specific to Deployment Manager**—all IaC tools (Terraform, Ansible, etc.) have the ability to **delete resources**.
- **Safe deletion mechanisms (e.g., preview mode) exist** to prevent accidental resource loss.

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs/deployments/updating-deployments**

**F. Cloud Deployment Manager only automates Google Cloud resources.** ❌

- **Not necessarily a business risk** if the company is **fully using Google Cloud**.
- **However, if multi-cloud compatibility is required, Terraform is a better choice.**

✅ **Reference:**

- **https://cloud.google.com/docs/terraform**

**Conclusion:**

The two key **business risks** of using **Cloud Deployment Manager** are:

1. **Potential deprecation** (Option B)
2. **Lack of familiarity among engineers** (Option C)

📌 **Final Reference:**

- **https://cloud.google.com/deployment-manager/docs/moving-to-terraform**

**⚠️ Note:** Deployment Manager reached end of support in March 2026, so the deprecation risk in option B has come true. Google now points to Terraform and Infrastructure Manager.

</details>

---

### Exam 1 · Q41

**You are analyzing and defining business processes to support your startup’s trial usage of Google Cloud Platform (GCP). Since consumer demand for your product is uncertain, your manager requires you to minimize GCP service costs while following Google best practices.**

**What should you do?**

- A. Utilize the **free tier** and **sustained use discounts**, and assign a **staff position** for managing service costs.
- B. Utilize the **free tier** and **sustained use discounts**, and provide **cost management training** to the team.
- C. Utilize the **free tier** and **committed use discounts**, and assign a **staff position** for managing service costs.
- D. Utilize the **free tier** and **committed use discounts**, and provide **cost management training** to the team.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Utilize the **free tier** and **sustained use discounts**, and provide **cost management training** to the team.

**Correct Answer:**

✅ **B. Utilize the free tier and sustained use discounts, and provide cost management training to the team.**

**Explanation:**

Since **consumer demand for your product is uncertain**, you need to **minimize GCP service costs** while following **Google-recommended best practices**.

**Why This is the Best Approach?**

✅ **1. Utilize the Free Tier**

- **Google Cloud Free Tier** provides **limited free usage** of key GCP services, helping **startups test workloads without initial costs**.
- **Free services include:** Compute Engine, Cloud Storage, BigQuery, and Firebase.

✅ **2. Take Advantage of Sustained Use Discounts (SUDs)**

- **Sustained Use Discounts (SUDs)** automatically apply **cost reductions** when VMs run for long periods in a month.
- **Better for unpredictable workloads**—you get discounts based on actual usage **without upfront commitments**.

✅ **3. Provide Cost Management Training**

- **Educating the team on cost optimization strategies** ensures **long-term cost control** without hiring a dedicated cost manager.
- **Tools like Cloud Billing Reports, Budgets, and Cost Insights** help teams **track and reduce spending**.

✅ **Supporting Documentation:**

- **Google Cloud Free Tier:**
  **https://cloud.google.com/free**
- **Sustained Use Discounts:**
  **https://cloud.google.com/compute/docs/sustained-use-discounts**
- **Cost Management Best Practices:**
  **https://cloud.google.com/billing/docs/how-to/manage-billing-account**

**Why Other Options Are Incorrect?**

**A. Utilize the free tier and sustained use discounts, and assign a staff position for managing service costs.** ❌

- **Hiring a dedicated staff member for cost management** increases **operational expenses**, which contradicts the goal of minimizing costs.
- **Providing training (Option B) is a more cost-effective solution.**

**C. Utilize the free tier and committed use discounts, and assign a staff position for managing service costs.** ❌

- **Committed Use Discounts (CUDs) require upfront commitments**, which **is not ideal for uncertain demand**.
- **Locking into long-term commitments** may **increase costs if workloads change**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts**

**D. Utilize the free tier and committed use discounts, and provide cost management training to the team.** ❌

- **Committed Use Discounts (CUDs) are cost-effective only for predictable workloads**, but the scenario specifies **uncertain consumer demand**.
- **Sustained Use Discounts (SUDs) are better suited for fluctuating demand.**

**Conclusion:**

The best approach is **B. Utilize the free tier and sustained use discounts, and provide cost management training to the team**, because:

- **Sustained Use Discounts (SUDs) offer flexibility for uncertain workloads.**
- **The free tier reduces initial costs.**
- **Training the team ensures long-term cost efficiency without adding extra staffing costs.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/sustained-use-discounts**

</details>

---

### Exam 1 · Q42

**You are building a continuous deployment pipeline for a project stored in a Git repository. You need to ensure that code changes are verified before being deployed to production.**

**What should you do?**

- A. Use **Spinnaker** to deploy builds to production using the **red/black deployment strategy**, allowing easy rollbacks if needed.
- B. Use **Spinnaker** to deploy builds directly to production and run tests on the production deployment.
- C. Use **Jenkins** to build both the **staging branches** and the **master branch**, then deploy changes to **10% of users** before performing a full rollout.
- D. Use **Jenkins** to monitor **repository tags**, deploy **staging tags** to a **staging environment** for testing, and after successful testing, tag the repository for **production deployment**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use **Jenkins** to monitor **repository tags**, deploy **staging tags** to a **staging environment** for testing, and after successful testing, tag the repository for **production deployment**.

**Correct Answer:**

✅ **D. Use Jenkins to monitor repository tags, deploy staging tags to a staging environment for testing, and after successful testing, tag the repository for production deployment.**

**Explanation:**

To ensure that **code changes are verified before being deployed to production**, a **controlled deployment pipeline with a staging environment** is required.

✅ **Why This Works:**

- **Jenkins automates the build and deployment process**, reducing human error.
- **Using repository tags for staged deployments** ensures **only tested and verified code is deployed to production**.
- **Deploying to a staging environment first allows for testing before production rollout.**
- **Production deployments are triggered only when a repository is tagged for release**, ensuring consistency.

**Implementation Steps:**

1. **Monitor Git repository for new tags** using Jenkins.
2. **Deploy staging tags to a staging environment** for integration and functional testing.
3. **Run automated tests and manual verification** in staging.
4. **If staging tests pass, tag the repository with a production tag.**
5. **Jenkins deploys production tags to production.**

✅ **Supporting Documentation:**

- **Jenkins Git Integration for Tag-Based Deployments:**
  **https://www.jenkins.io/doc/book/pipeline/scm**
- **CI/CD Best Practices for Jenkins:**
  **https://cloud.google.com/architecture/continuous-deployment-with-jenkins**

**Why Other Options Are Incorrect?**

**A. Use Spinnaker to deploy builds to production using the red/black deployment strategy, allowing easy rollbacks if needed.** ❌

- **Red/black (blue/green) deployment helps with rollback but does not verify code before deployment.**
- **The requirement is to verify before production, not just to handle rollbacks.**

✅ **Reference:**

- **https://spinnaker.io/docs/concepts/deployment-strategies**

**B. Use Spinnaker to deploy builds directly to production and run tests on the production deployment.** ❌

- **Testing should be done in a staging environment first, not in production.**
- **Running tests directly in production risks deploying unverified code to users.**

✅ **Reference:**

- **https://spinnaker.io/docs/setup/ci/jenkins**

**C. Use Jenkins to build both the staging branches and the master branch, then deploy changes to 10% of users before performing a full rollout.** ❌

- **Deploying changes to 10% of users first (canary deployment) is useful, but does not ensure that code is properly verified before any production deployment.**
- **The question requires full verification before deployment, which staging and tagging provide.**

✅ **Reference:**

- **https://cloud.google.com/architecture/canary-deployments-on-gke**

**Conclusion:**

The best approach is **D. Use Jenkins to monitor repository tags, deploy staging tags to a staging environment for testing, and after successful testing, tag the repository for production deployment**, because:

- **It ensures code is tested before production deployment.**
- **It provides a structured, controlled release process.**
- **It prevents unverified changes from reaching production.**

📌 **Final Reference:**
**https://cloud.google.com/architecture/continuous-deployment-with-jenkins**

</details>

---

### Exam 1 · Q59

**You need to assess your team’s readiness for a new Google Cloud Platform (GCP) project. As part of the evaluation, you must create a skills gap plan that aligns with the business goal of cost optimization. Your team has already successfully deployed two GCP projects.**

**What should you do?**

- A. **Allocate budget** for team training and **set a deadline** for the new GCP project.
- B. **Allocate budget** for team training and **develop a roadmap** for team members to obtain **Google Cloud certifications** based on their job roles.
- C. **Allocate budget** to hire **skilled external consultants** and **set a deadline** for the new GCP project.
- D. **Allocate budget** to hire **skilled external consultants** and **develop a roadmap** for team members to obtain **Google Cloud certifications** based on their job roles.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Allocate budget** for team training and **develop a roadmap** for team members to obtain **Google Cloud certifications** based on their job roles.

**Correct Answer:**

✅ **B. Allocate budget for team training and develop a roadmap for team members to obtain Google Cloud certifications based on their job roles.**

**Explanation:**

Since your **team has already successfully deployed two GCP projects**, they have **some foundational experience** but may still require **upskilling** to align with **cost optimization** and **advanced GCP best practices**.

✅ **Why Training & Certification is the Best Approach?**

1. **Cost Optimization Requires In-House Expertise:**
  - **Google Cloud certifications help team members gain expertise in cost-effective architecture and resource management.**
  - **Training ensures the team can independently manage future projects without relying on external consultants.**
2. **Long-Term Value Over External Consultants:**
  - **Hiring external consultants is expensive** and does not contribute to **team knowledge growth**.
  - **Developing in-house expertise reduces long-term operational costs.**
3. **Job Role-Based Certification Roadmap Ensures Skill Relevance:**
  - Example roadmap:
    - **Cloud Engineers** → **Associate Cloud Engineer (ACE)**
    - **Solution Architects** → **Professional Cloud Architect (PCA)**
    - **Security Teams** → **Professional Cloud Security Engineer**
    - **DevOps Teams** → **Professional Cloud DevOps Engineer**

✅ **Supporting Documentation:**

- **Google Cloud Certification Pathways:**
  **https://cloud.google.com/certification**
- **Google Cloud Cost Management Best Practices:**
  **https://cloud.google.com/billing/docs/cost-management-best-practices**

**Why Other Options Are Incorrect?**

**A. Allocate budget for team training and set a deadline for the new GCP project.** ❌

- **Training is essential, but setting a project deadline without skill assessment may result in inefficient execution.**
- **A structured roadmap for upskilling is missing, which is necessary for long-term success.**

✅ **Reference:**

- **https://cloud.google.com/certification**

**C. Allocate budget to hire skilled external consultants and set a deadline for the new GCP project.** ❌

- **External consultants provide short-term solutions but do not improve team readiness.**
- **Hiring consultants increases costs and creates long-term dependency on external expertise.**

✅ **Reference:**

- **https://cloud.google.com/training**

**D. Allocate budget to hire skilled external consultants and develop a roadmap for team members to obtain Google Cloud certifications based on their job roles.** ❌

- **Hiring external consultants is unnecessary since the team already has GCP experience.**
- **Training the in-house team provides better long-term cost optimization.**

✅ **Reference:**

- **https://cloud.google.com/training**

**Conclusion:**

The best approach is **B. Allocate budget for team training and develop a roadmap for team members to obtain Google Cloud certifications based on their job roles**, because:
✔ **It ensures cost optimization by reducing reliance on external consultants.**
✔ **It helps the team gain expertise in GCP cost management and efficiency.**
✔ **It aligns with business goals and Google Cloud best practices.**

📌 **Final Reference:**
**https://cloud.google.com/certification**

</details>

---

### Exam 2 · Q17

**You need to develop procedures to verify the resilience of disaster recovery for remote recovery using Google Cloud Platform (GCP). Your production environment is hosted on-premises, and you must establish a secure, redundant connection between your on-premises network and GCP.**

**What should you do?**

- A. Verify that **Dedicated Interconnect** can **replicate files to GCP**. Ensure that **Direct Peering** can establish a **secure backup connection** if **Dedicated Interconnect fails**.
- B. Verify that **Dedicated Interconnect** can **replicate files to GCP**. Ensure that **Cloud VPN** can establish a **secure backup connection** if **Dedicated Interconnect fails**.
- C. Verify that the **Transfer Appliance** can **replicate files to GCP**. Ensure that **Direct Peering** can establish a **secure backup connection** if the **Transfer Appliance fails**.
- D. Verify that the **Transfer Appliance** can **replicate files to GCP**. Ensure that **Cloud VPN** can establish a **secure backup connection** if the **Transfer Appliance fails**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Verify that **Dedicated Interconnect** can **replicate files to GCP**. Ensure that **Cloud VPN** can establish a **secure backup connection** if **Dedicated Interconnect fails**.

**Correct Answer:**

**B. Verify that Dedicated Interconnect can replicate files to GCP. Ensure that Cloud VPN can establish a secure backup connection if Dedicated Interconnect fails.**

**Explanation:**

The goal is to **establish a secure, redundant connection** between the **on-premises environment and Google Cloud Platform (GCP)** for **disaster recovery (DR)**. The best approach is:

1. **Use Dedicated Interconnect for primary, high-speed connectivity** to GCP.
2. **Use Cloud VPN as a secure backup connection** in case Dedicated Interconnect fails.

**Why This Approach?**

- **Dedicated Interconnect** provides **high-speed, low-latency** connectivity with a **99.99% SLA** when used with redundant links.
- **Cloud VPN** serves as a **secure failover solution** over the public internet when Dedicated Interconnect is unavailable.
- **Recommended by Google Cloud for hybrid disaster recovery architectures.**

**Implementation Steps:**

**1. Set up Dedicated Interconnect** (Primary Connection)

- **Reserve Interconnect capacity** (10 Gbps or 100 Gbps):
  ```
  gcloud compute interconnects create my-interconnect \    --location=us-central1 \    --capacity=10Gbps \    --provider=my-provider
  ```
- **Configure VLAN attachments** for connectivity to Google Cloud VPC.

**2. Set up Cloud VPN** (Backup Connection)

- **Create a VPN gateway and establish tunnels:**
  ```
  gcloud compute vpn-gateways create my-vpn-gateway \    --network=my-vpc
  ```
  ```
  gcloud compute vpn-tunnels create my-vpn-tunnel \    --peer-address=<on-prem-peer-ip> \    --ike-version=2 \    --shared-secret=<shared-secret>
  ```

**3. Configure Dynamic Routing with Cloud Router**

- **Use BGP to automatically update failover routes.**
  ```
  gcloud compute routers create my-router \    --network=my-vpc \    --region=us-central1 \    --asn=65000
  ```

**4. Verify Connectivity & Failover Testing**

- Ensure **Dedicated Interconnect is primary** and **Cloud VPN takes over during failures**.
- Use **Cloud Monitoring to track uptime and failover events**.

**Supporting Documentation:**

- **Dedicated Interconnect Best Practices:**
  https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview
- **Cloud VPN Setup:**
  https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview

**Why Other Options Are Incorrect?**

**A. Verify that Dedicated Interconnect can replicate files to GCP. Ensure that Direct Peering can establish a secure backup connection if Dedicated Interconnect fails.**

- **Direct Peering is not a failover solution** because it does not offer VPN encryption or private IPs for Google Cloud services.
- **It does not provide an SLA for availability**, making it unsuitable for disaster recovery backup.

✅ **Reference:**
https://cloud.google.com/network-connectivity/docs/overview

**C. Verify that the Transfer Appliance can replicate files to GCP. Ensure that Direct Peering can establish a secure backup connection if the Transfer Appliance fails.**

- **Transfer Appliance is for bulk offline data transfers, not real-time disaster recovery.**
- **Direct Peering lacks security and failover reliability.**

✅ **Reference:**
https://cloud.google.com/transfer-appliance/docs/

**D. Verify that the Transfer Appliance can replicate files to GCP. Ensure that Cloud VPN can establish a secure backup connection if the Transfer Appliance fails.**

- **Transfer Appliance is not designed for ongoing data replication.**
- **Cloud VPN is a good backup solution, but it should complement Dedicated Interconnect, not Transfer Appliance.**

✅ **Reference:**
https://cloud.google.com/transfer-appliance

**Conclusion:**

The best approach is **B. Verify that Dedicated Interconnect can replicate files to GCP. Ensure that Cloud VPN can establish a secure backup connection if Dedicated Interconnect fails**, because:

- **Dedicated Interconnect provides high-speed, private connectivity.**
- **Cloud VPN ensures secure failover over the internet.**
- **It follows Google Cloud best practices for disaster recovery and redundancy.**

**Final Reference:**
[https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)

</details>

---

### Exam 2 · Q19

**Your customer wants to perform resilience testing on their authentication layer, which consists of a regional managed instance group serving a public REST API that interacts with a Cloud SQL instance for reading and writing data.**

**What should you do?**

- A. Work with a **security firm** to run **web scrapers** that search for users' **authentication data** on **malicious websites** and notify you if any data is found.
- B. Deploy **intrusion detection software** on the virtual machines to **detect and log unauthorized access attempts**.
- C. **Schedule a disaster simulation** where you **shut down all VMs** in a zone to observe how the application behaves under failure conditions.
- D. **Set up a Cloud SQL read replica** in a different **zone** from the primary instance, then manually **trigger a failover** while monitoring **KPIs for the REST API**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Schedule a disaster simulation** where you **shut down all VMs** in a zone to observe how the application behaves under failure conditions.

**Correct Answer:**

**C. Schedule a disaster simulation where you shut down all VMs in a zone to observe how the application behaves under failure conditions.**

**Explanation:**

Resilience testing focuses on **evaluating system behavior under failure conditions** to ensure it can recover and continue functioning. Since the **authentication layer** consists of:

1. **A regional managed instance group (MIG) serving a public REST API**
2. **A Cloud SQL instance for reading and writing data**

A **controlled failure scenario** where all virtual machines (VMs) in a **single zone are shut down** helps assess the authentication layer's resilience.

**Why This Approach?**

- **Simulates real-world failures**, such as **zone outages**, and validates if traffic is **properly redirected** to another zone.
- **Managed Instance Groups (MIGs) should automatically scale** in a different zone if configured with multiple zones.
- **Cloud SQL's high availability (HA) setup should trigger a failover** if a zonal failure occurs.

**Implementation Steps:**

**1. Ensure the MIG is regional (multi-zone)**

- Verify that the managed instance group spans multiple zones:
  ```
  gcloud compute instance-groups managed list
  ```
- If needed, create a **multi-zone** MIG:
  ```
  gcloud compute instance-groups managed create my-auth-mig \    --template=my-instance-template \    --base-instance-name=my-auth-vm \    --size=3 \    --zones=us-central1-a,us-central1-b
  ```

**2. Simulate a zonal failure by shutting down all VMs in one zone**

- Identify VMs in a specific zone:tgcloud compute instances list --filter="zone:us-central1-a"
- Shut down all VMs in that zone:
  ```
  bashCopyEditgcloud compute instances delete <instance-name>
  ```
- Observe **how quickly the MIG spins up replacement instances in the other zone**.

**3. Validate failover for Cloud SQL (if HA is enabled)**

- Check if the **Cloud SQL instance is configured for automatic failover**:
  ```
  gcloud sql instances describe my-cloudsql-instance
  ```
- Simulate a failover manually:
  ```
  gcloud sql instances failover my-cloudsql-instance
  ```
- **Monitor API response times and error rates** to assess the impact.

**4. Analyze Results & Improve Fault Tolerance**

- Use **Cloud Monitoring and Logging** to track **latency, availability, and error rates**.
- Improve resilience by **adjusting autoscaling settings** or **adding read replicas** if needed.

**Supporting Documentation:**

- **Testing Disaster Recovery for Compute Engine:**
  https://cloud.google.com/architecture/dr-scenarios/testing-disaster-recovery
- **Managed Instance Groups High Availability:**
  https://cloud.google.com/compute/docs/instance-groups/distribute-instances-across-zones
- **Cloud SQL High Availability:**
  https://cloud.google.com/sql/docs/mysql/high-availability

**Why Other Options Are Incorrect?**

**A. Work with a security firm to run web scrapers that search for users' authentication data on malicious websites and notify you if any data is found.**

- This **focuses on security, not resilience testing**.
- **Security threat detection does not validate system failure response**.

✅ **Reference:**
https://cloud.google.com/security-command-center/docs

**B. Deploy intrusion detection software on the virtual machines to detect and log unauthorized access attempts.**

- **Intrusion detection focuses on security monitoring**, not **resilience testing**.
- **Detecting unauthorized access does not assess system behavior under failure conditions**.

✅ **Reference:**
https://cloud.google.com/security-command-center/docs/concepts#intrusion-detection

**D. Set up a Cloud SQL read replica in a different zone from the primary instance, then manually trigger a failover while monitoring KPIs for the REST API.**

- **Read replicas do not provide automatic failover**—they are meant for **read scaling, not high availability**.
- **Failover testing should be done on a Cloud SQL HA instance**, not a read replica.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/high-availability

**Conclusion:**

The best approach is **C. Schedule a disaster simulation where you shut down all VMs in a zone to observe how the application behaves under failure conditions**, because:

- It **simulates a real-world zonal failure** to assess system resilience.
- It **validates Managed Instance Group (MIG) failover capabilities**.
- It **ensures Cloud SQL high availability (HA) is properly configured**.

**Final Reference:**
[https://cloud.google.com/architecture/dr-scenarios/testing-disaster-recovery](https://cloud.google.com/architecture/dr-scenarios/testing-disaster-recovery)

</details>

---

### Exam 2 · Q32

**You need to develop procedures to test a disaster recovery plan for a mission-critical application. You want to follow Google-recommended best practices and use native GCP capabilities.**

**What should you do?**

- A. Use **Deployment Manager** to **automate service provisioning** and monitor/debug tests with **Activity Logs**.
- B. Use **Deployment Manager** to **automate service provisioning** and monitor/debug tests with **Stackdriver**.
- C. Use **gcloud scripts** to **automate service provisioning** and monitor/debug tests with **Activity Logs**.
- D. Use **gcloud scripts** to **automate service provisioning** and monitor/debug tests with **Stackdriver**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **Deployment Manager** to **automate service provisioning** and monitor/debug tests with **Stackdriver**.

**Correct option: B**

Use **Deployment Manager** to automate service provisioning, and use **Stackdriver (Google Cloud Observability: Cloud Monitoring + Cloud Logging)** to **monitor and debug** your disaster recovery (DR) tests.

Why B is correct

- Google recommends **automating provisioning** so DR tests are repeatable and consistent.
- For **monitoring and debugging**, **Stackdriver/Cloud Observability** is the right native capability because it provides operational visibility (metrics, logs, alerts), which is essential during DR testing.
- **Activity Logs** are mainly for audit trails (who did what), not full operational monitoring.

Reference: Google DR planning/testing guidance emphasizes automation and observability
[https://cloud.google.com/solutions/dr-scenarios-planning-guide](https://cloud.google.com/solutions/dr-scenarios-planning-guide?utm_source=chatgpt.com)

Why the other options are incorrect

A is incorrect

**Activity Logs** help with auditing changes, but they are not sufficient for monitoring application health, performance, and failures during DR drills.
Reference: Cloud Audit Logs purpose
[https://cloud.google.com/logging/docs/audit](https://cloud.google.com/logging/docs/audit)

C is incorrect

Same issue as A: Activity Logs aren’t the right tool for monitoring/debugging DR tests.
Reference: Cloud Audit Logs purpose
[https://cloud.google.com/logging/docs/audit](https://cloud.google.com/logging/docs/audit)

D is incorrect

Although **Stackdriver is correct**, the Google-recommended approach favors using an **infrastructure automation tool** (IaC-style provisioning) rather than ad-hoc CLI scripting for repeatable DR provisioning procedures. Deployment Manager is the native IaC-style option given here, making **B** the best match.
Reference: DR planning guide
[https://cloud.google.com/solutions/dr-scenarios-planning-guide](https://cloud.google.com/solutions/dr-scenarios-planning-guide?utm_source=chatgpt.com)

###### Explanation

**Correct option: B**

Use **Deployment Manager** to automate service provisioning, and use **Stackdriver (Google Cloud Observability: Cloud Monitoring + Cloud Logging)** to **monitor and debug** your disaster recovery (DR) tests.

Why B is correct

- Google recommends **automating provisioning** so DR tests are repeatable and consistent.
- For **monitoring and debugging**, **Stackdriver/Cloud Observability** is the right native capability because it provides operational visibility (metrics, logs, alerts), which is essential during DR testing.
- **Activity Logs** are mainly for audit trails (who did what), not full operational monitoring.

> [!note]- Why the other options are wrong
> A is incorrect
>
> **Activity Logs** help with auditing changes, but they are not sufficient for monitoring application health, performance, and failures during DR drills.
> Reference: Cloud Audit Logs purpose
> [https://cloud.google.com/logging/docs/audit](https://cloud.google.com/logging/docs/audit)
>
> C is incorrect
>
> Same issue as A: Activity Logs aren’t the right tool for monitoring/debugging DR tests.
> Reference: Cloud Audit Logs purpose
> [https://cloud.google.com/logging/docs/audit](https://cloud.google.com/logging/docs/audit)
>
> D is incorrect
>
> Although **Stackdriver is correct**, the Google-recommended approach favors using an **infrastructure automation tool** (IaC-style provisioning) rather than ad-hoc CLI scripting for repeatable DR provisioning procedures. Deployment Manager is the native IaC-style option given here, making **B** the best match.
> Reference: DR planning guide
> [https://cloud.google.com/solutions/dr-scenarios-planning-guide](https://cloud.google.com/solutions/dr-scenarios-planning-guide?utm_source=chatgpt.com)

**⚠️ Note:** Deployment Manager reached end of support in March 2026 (use Terraform or Infrastructure Manager), and Stackdriver is now Cloud Monitoring and Cloud Logging. The principle still holds: automate provisioning and monitor DR tests with Cloud Monitoring.

</details>

---

### Exam 2 · Q46

Your company runs **application workloads** on **Compute Engine** across **production, acceptance, and development environments**.

- The **production environment** is **business-critical** and operates **24/7**.
- The **acceptance and development environments** are only **critical during office hours**.
- Your **CFO** has asked you to **optimize costs** by **reducing expenses during idle times**.

What should you do?

- A. **Create a shell script** that uses the **gcloud command** to **change the machine type** of **development and acceptance instances** to a **smaller machine type** outside office hours. Schedule the script on a **production instance** to automate this task.
- B. **Use Cloud Scheduler** to trigger a **Cloud Function** that **stops the development and acceptance environments after office hours** and **starts them before office hours**.
- C. **Deploy the development and acceptance applications** on a **managed instance group** and **enable autoscaling** to scale down resources during idle times.
- D. Use **regular Compute Engine instances** for the **production environment**, and **preemptible VMs** for the **acceptance and development environments** to reduce costs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Use Cloud Scheduler** to trigger a **Cloud Function** that **stops the development and acceptance environments after office hours** and **starts them before office hours**.

**Correct Answer:**

**B. Use Cloud Scheduler to trigger a Cloud Function that stops the development and acceptance environments after office hours and starts them before office hours.**

**Explanation:**

The **goal** is to **optimize costs by reducing expenses during idle times** in **development and acceptance environments**, while ensuring that the **business-critical production environment remains operational 24/7**.

**The best approach is to schedule automatic start/stop operations using Cloud Scheduler and Cloud Functions.**

✅ **Cloud Scheduler** allows **automated, serverless scheduling** (like a cron job).
✅ **Cloud Functions** can be triggered to execute a script that **stops or starts the Compute Engine instances** at predefined times.
✅ **This method provides cost savings without requiring manual intervention.**

**How to Implement This Solution?**

**1. Create a Cloud Function to Stop Instances After Office Hours**

- This function **stops Compute Engine instances** in the **development and acceptance** environments.

```
from googleapiclient import discoveryfrom google.oauth2 import service_account PROJECT_ID = "your-project-id"ZONE = "us-central1-a"INSTANCES = ["dev-instance", "acceptance-instance"] def stop_instances(request):    credentials = service_account.Credentials.from_service_account_file('service-account.json')    compute = discovery.build('compute', 'v1', credentials=credentials)     for instance in INSTANCES:        compute.instances().stop(project=PROJECT_ID, zone=ZONE, instance=instance).execute()     return "Instances stopped"
```

**2. Create a Cloud Function to Start Instances Before Office Hours**

- Modify the above function to use `compute.instances().start(...)` instead of `stop(...)`.

**3. Set Up Cloud Scheduler to Trigger the Functions**

Run the **stop function at 6 PM (after office hours)**:

```
gcloud scheduler jobs create http stop-dev-acceptance \    --schedule "0 18 * * *" \    --uri "https://your-cloud-function-url" \    --http-method=POST
```

Run the **start function at 8 AM (before office hours)**:

```
gcloud scheduler jobs create http start-dev-acceptance \    --schedule "0 8 * * *" \    --uri "https://your-cloud-function-url" \    --http-method=POST
```

✅ **Reference:**
https://cloud.google.com/scheduler/docs

**Why Other Options Are Incorrect?**

**A. Create a shell script that uses gcloud to change the machine type of development and acceptance instances to a smaller machine type outside office hours.**

❌ **Incorrect:**

- **Changing machine type requires stopping the instance**, causing **downtime**.
- **Frequent resizing of instances is inefficient** and requires **manual intervention**.
- **Cloud Scheduler and Cloud Functions provide a better automated approach**.

✅ **Reference:**
https://cloud.google.com/compute/docs/instances/changing-machine-type

**C. Deploy the development and acceptance applications on a managed instance group and enable autoscaling to scale down resources during idle times.**

❌ **Incorrect:**

- **Autoscaling does not stop instances**—it **only reduces the number of instances** based on CPU/memory load.
- **Does not guarantee cost savings** during non-office hours if minimal traffic is present.

✅ **Reference:**
https://cloud.google.com/compute/docs/autoscaler

**D. Use regular Compute Engine instances for production, and preemptible VMs for acceptance and development environments.**

❌ **Incorrect:**

- **Preemptible VMs are automatically terminated at any time**—this can cause issues during active development/testing.
- **They are not suitable for workloads that require reliable uptime** during office hours.

✅ **Reference:**
https://cloud.google.com/compute/docs/instances/preemptible

**Conclusion:**

The best approach is **B. Use Cloud Scheduler to trigger a Cloud Function that stops the development and acceptance environments after office hours and starts them before office hours**, because:

- **It automates instance management with minimal operational overhead.**
- **Ensures predictable cost savings without impacting production.**
- **Uses a serverless approach with Cloud Scheduler and Cloud Functions for reliability.**

**Documentation Support:**

- **Cloud Scheduler:** [https://cloud.google.com/scheduler](https://cloud.google.com/scheduler)
- **Cloud Functions:** [https://cloud.google.com/functions](https://cloud.google.com/functions)
- **Compute Engine:** [https://cloud.google.com/compute](https://cloud.google.com/compute)

**⚠️ Note:** Compute Engine instance schedules can now start and stop VMs on a schedule without any code, and Cloud Functions is now Cloud Run functions. Either approach is correct if offered.

</details>

---

### Exam 2 · Q59

Your team is beginning **development of a new application** using a **microservices architecture** on **Google Kubernetes Engine (GKE)**.

- **Any code change** pushed to the **develop branch** on **GitHub** must be **automatically built and tested**.
- If the **build and test succeed**, the **corresponding microservice** should be **automatically deployed** in the **development environment**.
- You need to **enforce this process** for all **code deployed** to the **development environment**.

What should you do?

- A. Require each **developer** to install a **pre-commit hook** on their local workstation that **tests the code** and **builds the container** before committing to the **development branch**. After a **successful commit**, the developer **manually deploys** the newly built container to the **development cluster**.
- B. Set up a **post-commit hook** on the **remote GitHub repository** that **tests the code** and **builds the container** when changes are pushed to the **development branch**. After a **successful build**, the developer **manually deploys** the newly built container to the **development cluster**.
- C. **Configure a Cloud Build trigger** that **automatically builds and tests** any code pushed to the **development branch**. Store the built container in **Container Registry**. Set up a **deployment pipeline** that **automatically watches for new images** and **deploys them** to the **development cluster**, ensuring that only the **deployment tool** has permissions to deploy new versions.
- D. **Set up a Cloud Build trigger** for the **development branch** that **builds a new container image** and **stores it in Container Registry**. Use **Vulnerability Scanning** to verify the code’s integrity. As the **final step of the Cloud Build process**, deploy the **new container image** to the **development cluster**, ensuring that only **Cloud Build** has permissions to deploy new versions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Configure a Cloud Build trigger** that **automatically builds and tests** any code pushed to the **development branch**. Store the built container in **Container Registry**. Set up a **deployment pipeline** that **automatically watches for new images** and **deploys them** to the **development cluster**, ensuring that only the **deployment tool** has permissions to deploy new versions.

**Correct Answer:**

**C. Configure a Cloud Build trigger that automatically builds and tests any code pushed to the development branch. Store the built container in Container Registry. Set up a deployment pipeline that automatically watches for new images and deploys them to the development cluster, ensuring that only the deployment tool has permissions to deploy new versions.**

**Explanation:**

For **automating the build, test, and deployment process** for microservices on **Google Kubernetes Engine (GKE)**, **Cloud Build** with an automated **CI/CD pipeline** is the best approach.

✅ **Cloud Build triggers automatically build and test code when pushed to the development branch.**
✅ **The built container is stored in Container Registry** for versioning and security.
✅ **A deployment pipeline monitors the Container Registry** and **automatically deploys new images** to the development cluster.
✅ **Deployment permissions are restricted**, ensuring **only the deployment tool** can deploy updates, following security best practices.

This setup **enforces automation, improves efficiency, and reduces manual errors** in the CI/CD process.

**How to Implement This?**

**1. Create a Cloud Build Trigger**

- In **Google Cloud Console** → **Cloud Build** → **Triggers**.
- **Create a new trigger** for the `develop` branch.
- **Configure the trigger to:**
  - **Run tests.**
  - **Build the container image.**
  - **Push the image to Container Registry.**

Example **cloudbuild.yaml**:

```
steps:- name: 'gcr.io/cloud-builders/docker'  args: ['build', '-t', 'gcr.io/$PROJECT_ID/my-microservice:$SHORT_SHA', '.']- name: 'gcr.io/cloud-builders/docker'  args: ['push', 'gcr.io/$PROJECT_ID/my-microservice:$SHORT_SHA']- name: 'gcr.io/cloud-builders/kubectl'  args: ['set', 'image', 'deployment/my-microservice',         'my-microservice=gcr.io/$PROJECT_ID/my-microservice:$SHORT_SHA']
```

**2. Automate Deployment Using Cloud Build or a Watcher**

- **Set up Kubernetes Deployment Config to watch for new images.**
- **Use Cloud Build or GitOps tools (e.g., ArgoCD) to auto-deploy new images.**

✅ **Reference:**
https://cloud.google.com/cloud-build/docs/automating-builds/create-manage-triggers

**Why Other Options Are Incorrect?**

**A. Require each developer to install a pre-commit hook on their local workstation that tests the code and builds the container before committing to the development branch. After a successful commit, the developer manually deploys the newly built container to the development cluster.**

❌ **Incorrect:**

- **Relies on manual deployment**, which is **error-prone and inefficient**.
- **Pre-commit hooks only run locally**, meaning **no centralized enforcement** for all developers.
- **No automated deployment or integration testing.**

✅ **Reference:**
[https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

**B. Set up a post-commit hook on the remote GitHub repository that tests the code and builds the container when changes are pushed to the development branch. After a successful build, the developer manually deploys the newly built container to the development cluster.**

❌ **Incorrect:**

- **Manual deployment step still exists**—this does not enforce continuous deployment.
- **A post-commit hook alone does not provide automated testing and CI/CD pipeline management.**

✅ **Reference:**
[https://docs.github.com/en/actions](https://docs.github.com/en/actions)

**D. Set up a Cloud Build trigger for the development branch that builds a new container image and stores it in Container Registry. Use Vulnerability Scanning to verify the code’s integrity. As the final step of the Cloud Build process, deploy the new container image to the development cluster, ensuring that only Cloud Build has permissions to deploy new versions.**

❌ **Incorrect:**

- **Vulnerability scanning is useful but does not replace automated deployment triggers.**
- **Cloud Build should trigger the deployment pipeline, not directly deploy changes.**
- **A dedicated deployment tool should handle deployment, ensuring rollback and controlled releases.**

✅ **Reference:**
https://cloud.google.com/container-analysis/docs/container-scanning

**Conclusion:**

The best approach is **C. Configure a Cloud Build trigger that automatically builds and tests any code pushed to the development branch. Store the built container in Container Registry. Set up a deployment pipeline that automatically watches for new images and deploys them to the development cluster, ensuring that only the deployment tool has permissions to deploy new versions.**

This method ensures:

- **Automated builds and tests** using Cloud Build.
- **Reliable and secure image storage** in Container Registry.
- **Automated deployments with a dedicated deployment pipeline.**
- **Minimized manual intervention, improving efficiency and security.**

✅ **Final Reference:**
[https://cloud.google.com/cloud-build/docs/automating-builds](https://cloud.google.com/cloud-build/docs/automating-builds)

**⚠️ Note:** Container Registry was shut down in 2025; today the images go to Artifact Registry.

</details>

---

### Exam 2 · Q60

**The Director of Engineering mandates migrating all development infrastructure resources from on-premises virtual machines (VMs) to Google Cloud to reduce costs. These resources undergo multiple start/stop cycles daily and necessitate state persistence. You've been tasked with designing the process for running a development environment in Google Cloud while ensuring cost visibility for the finance department. What two steps should you take? (Choose two)**

- A. Utilize persistent disks to store the state and start/stop the VMs as required.
- B. Implement the "gcloud --auto-delete" flag on all persistent disks before stopping the VMs.
- C. Apply a label for VM CPU utilization and incorporate it into the BigQuery billing export.
- D. Utilize BigQuery billing export and labels to associate costs with specific groups.
- E. Store all state in a Local SSD, snapshot the persistent disks, and terminate the VMs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Utilize persistent disks to store the state and start/stop the VMs as required. **|** D. Utilize BigQuery billing export and labels to associate costs with specific groups.

**Correct Answers:**

**A. Utilize persistent disks to store the state and start/stop the VMs as required.**
**D. Utilize BigQuery billing export and labels to associate costs with specific groups.**

**Explanation:**

The goal is to **migrate development infrastructure to Google Cloud** while ensuring:

1. **State persistence** despite frequent start/stop cycles.
2. **Cost visibility** for the finance team.

✅ **Option A: Utilize persistent disks to store the state and start/stop the VMs as required.**

- **Persistent disks retain data even when VMs are stopped.**
- **VMs can be started/stopped without data loss**, reducing costs when resources are not in use.
- **Cost-effective approach** compared to keeping VMs running 24/7.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/persistent-disks

✅ **Option D: Utilize BigQuery billing export and labels to associate costs with specific groups.**

- **BigQuery billing export helps track costs per resource.**
- **Applying labels (e.g., `env:development`, `team:frontend`) helps associate costs with specific teams or projects.**
- **Enables finance teams to analyze and optimize resource utilization.**

✅ **Reference:**
https://cloud.google.com/billing/docs/how-to/export-data-bigquery

❌ **Why Other Options Are Incorrect?**

**B. Implement the "gcloud --auto-delete" flag on all persistent disks before stopping the VMs.**

❌ **Incorrect:**

- `--auto-delete` **deletes the disk when the VM is stopped**, causing data loss.
- **Persistent state is required, so auto-delete is not suitable.**

✅ **Reference:**
https://cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete

**C. Apply a label for VM CPU utilization and incorporate it into the BigQuery billing export.**

❌ **Incorrect:**

- **BigQuery billing export tracks billing, not CPU utilization.**
- **While tracking CPU usage helps with performance monitoring, it does not directly provide cost insights.**

✅ **Reference:**
https://cloud.google.com/billing/docs/how-to/export-data-bigquery

**E. Store all state in a Local SSD, snapshot the persistent disks, and terminate the VMs.**

❌ **Incorrect:**

- **Local SSDs are ephemeral (data is lost when VM stops).**
- **Snapshots of persistent disks increase storage costs unnecessarily.**
- **Persistent disks are better for storing state without requiring frequent snapshots.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/local-ssd

**Conclusion:**

The best approach is to:

1. **Use Persistent Disks to store state** while stopping/starting VMs dynamically (**Option A**).
2. **Use BigQuery billing export and labels** to track costs and improve visibility (**Option D**).

✅ **Final Reference:**
[https://cloud.google.com/billing/docs/how-to/export-data-bigquery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)
[https://cloud.google.com/compute/docs/disks/persistent-disks](https://cloud.google.com/compute/docs/disks/persistent-disks)

</details>

---

### Exam 3 · Q9

You are developing a **microservices-based application** running on **Google Kubernetes Engine (GKE)**. As part of testing, you want to **simulate a sudden failure of a specific microservice** to observe how your application responds under failure conditions.

What is the most appropriate way to simulate this scenario?

- A. Apply a **taint** to one of the Kubernetes nodes, and set a **pod anti-affinity rule** for the specific microservice, using the tainted node’s name as the label value.
- B. Use **Istio’s fault injection** capability to simulate failure behavior in the target microservice.
- C. **Manually delete a node** from the Kubernetes cluster to observe how the system reacts.
- D. Use **Istio's traffic management** features to redirect traffic away from the microservice that is expected to crash.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **Istio’s fault injection** capability to simulate failure behavior in the target microservice.

✅ **Correct Answer: B. Use Istio’s fault injection capability to simulate failure behavior in the target microservice.**

**Scenario Summary:**

- You're running a **microservices-based application on GKE**.
- You want to **simulate a sudden failure** of a **specific microservice** to test the resilience of your app.
- This is part of a **controlled testing environment**, not a real outage.
- You’re aiming to **observe system behavior** (e.g., retries, fallbacks, alerting).

✅ **Why Option B is Correct:**

**Istio's Fault Injection Features:**

- Istio provides a **powerful traffic management API**, including **fault injection** capabilities.
- You can simulate:
  - **Delays** (to test timeouts)
  - **HTTP errors** (e.g., 500, 404)
  - **Abort scenarios** (to simulate microservice failure)

With Istio, you can **precisely target a microservice** and control:

- The percentage of requests affected
- The type and timing of the faults
- Specific routing conditions

This makes it the most appropriate tool for **controlled and repeatable failure injection**.

**Documentation:**

- Istio: Fault Injection

"Istio’s fault injection can be used to test the robustness of your microservices by simulating failures like HTTP errors and latency."

❌ **Why Other Options Are Incorrect:**

**A. Apply a taint and set anti-affinity rule**

- Taints and anti-affinity rules are **node scheduling mechanisms**, not failure simulation tools.
- They control **where pods run**, but **do not simulate microservice failure** or unavailability at runtime.

**Docs:**

- Taints and Tolerations
- Affinity and Anti-Affinity

**C. Manually delete a node from the Kubernetes cluster**

- Deleting a node is **disruptive and not precise**.
- It can affect **multiple workloads**, not just the target microservice.
- Not recommended for simulating a failure of a **specific service** in a controlled test.

**Docs:**

- Node lifecycle management

**D. Use Istio's traffic management to redirect traffic away**

- Redirecting traffic **avoids the microservice**, rather than simulating its **failure**.
- This tests **traffic shifting**, not **failure response**.
- Doesn’t help validate how your system handles **unexpected microservice unavailability**.

**Docs:**

- Istio Traffic Routing

✅ **Final Recommendation:**

Use **Istio's fault injection** to simulate microservice failure in a **targeted, repeatable, and safe** manner.

**⚠️ Note:** Google's managed Istio offering is now Cloud Service Mesh, which supports the same fault injection.

</details>

---

### Exam 3 · Q12

Your organization has built a **monolithic, 3-tier application** that enables **external users to upload and share files**. The current system is **difficult to enhance** and suffers from **reliability issues**. The development team wants to **re-architect the application** using a **microservices model** and **fully managed cloud services**, but they need to **justify the value** of this shift to leadership.

Which key benefit(s) should the team emphasize to help gain leadership support?

- A. The new architecture will be **more cost-effective**, simplify **infrastructure management**, and provide **automated CI/CD pipeline management**.
- B. The current monolith can be **containerized using Docker**, and the resulting container can be deployed to a **Kubernetes cluster**.
- C. The new approach will allow for **decoupling infrastructure from the application**, **faster feature development and release**, easier **CI/CD and infrastructure management**, support for **A/B testing**, and **scalability on demand**.
- D. The migration process can be **automated using Migrate for Compute Engine**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. The new approach will allow for **decoupling infrastructure from the application**, **faster feature development and release**, easier **CI/CD and infrastructure management**, support for **A/B testing**, and **scalability on demand**.

✅ **Correct Answer: C. The new approach will allow for decoupling infrastructure from the application, faster feature development and release, easier CI/CD and infrastructure management, support for A/B testing, and scalability on demand.**

**Scenario Summary:**

- Organization currently runs a **monolithic 3-tier app**.
- App supports **external file uploads/sharing** but has **reliability issues** and is **hard to enhance**.
- Team proposes a **microservices-based rearchitecture** using **fully managed cloud services**.
- Leadership needs to understand the **value proposition** of this architectural shift.

✅ **Why Option C is Correct:**

**Key Benefits of Microservices and Fully Managed Services:**

1. **Decoupling of Infrastructure and Application Logic**:
  - Services can be developed and deployed independently.
  - No tight coupling to specific machines or monolithic constraints.
2. **Faster Feature Development & Release**:
  - Teams can iterate independently on different components.
  - Enables **agile development practices** and **smaller, focused deployments**.
3. **Easier CI/CD and Infrastructure Management**:
  - Fully managed services (like Cloud Run, Cloud Functions, Cloud Pub/Sub, Cloud SQL, etc.) eliminate operational overhead.
  - Better support for **automation and deployment pipelines**.
4. **Support for A/B Testing**:
  - Microservices and cloud load balancing allow **traffic splitting** for testing and gradual rollouts.
5. **Scalability on Demand**:
  - Serverless and container-based platforms scale automatically based on traffic.
  - You pay only for what you use, improving cost-efficiency.

**Official Documentation Reference:**

- Google Cloud Architecture Framework – App Modernization
- Why Microservices? – Google Cloud Architecture Center

“Microservices architectures improve agility, scalability, and reliability. They allow independent scaling and deployment of components and are well-suited to CI/CD and DevOps practices.”

❌ **Why Other Options Are Incorrect:**

**A. More cost-effective, simplify infrastructure, provide CI/CD**

- While **partially correct**, it:
  - **Overemphasizes cost** (microservices may initially **increase complexity** and cost before optimization).
  - Does not mention **key architectural benefits** like **decoupling**, **scalability**, or **faster innovation**.
  - CI/CD automation is a benefit, but **not unique** to microservices.

**B. Containerize monolith and deploy to Kubernetes**

- This is **not microservices** — it’s **“lift-and-shift”**.
- You’re still running a **monolith**, just in a container.
- It **doesn’t address** the core problems: poor reliability, slow development cycles, lack of modularity.

**D. Migrate using Migrate for Compute Engine**

- This is a **migration tool** for VMs, not a solution for **application modernization**.
- Does not help with **rearchitecting** or achieving the benefits of a **microservices-based approach**.
- Relevant only for VM-based “as-is” migrations.

✅ **Final Recommendation:**

Emphasize the **strategic technical benefits** of re-architecting to microservices using managed services:

- **Decoupling**, **agility**, **scalability**, **resilience**, **faster innovation**, and **better operational efficiency**.

</details>

---

### Exam 3 · Q15

Your organization is building a **web-based application**, and you need to ensure that **production deployments can be traced back to specific source code commits**. This traceability should support **full auditability** of what code was deployed and when.

What is the most effective approach to achieve this?

- A. Require developers to **tag each commit** with the **date and time** of the commit.
- B. Instruct developers to **include a comment in each commit** that references the corresponding **deployment**.
- C. Ensure the **container image tag** matches the **source code commit hash**.
- D. Have developers **tag all commits** with the **label “latest”**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Ensure the **container image tag** matches the **source code commit hash**.

✅ **Correct Answer: C. Ensure the container image tag matches the source code commit hash.**

**Scenario Summary:**

- You are building a **web-based application**.
- You must ensure **production deployments can be traced** to the **exact source code commit**.
- This is required to support **full auditability** of what code was deployed and **when**.

✅ **Why Option C is Correct:**

**Tagging container images with Git commit hashes is an industry best practice**:

- When you **build and deploy a container image**, tag it with the **corresponding Git commit hash** (e.g., `gcr.io/my-project/my-app:abc1234`).
- This approach provides:
  - **Immutable traceability** between deployed artifact and source code.
  - **Auditability** — you can inspect production containers and immediately know **which version of the code** is running.
  - Supports **repeatable deployments**, rollbacks, and debugging.

**Google Cloud Best Practices:**

"Tagging container images with the commit SHA (e.g. git commit hash) ensures that every deployment is traceable to the exact source code version used."
— Google Cloud: Deploying containers – best practices

**Also supported by tools like:**

- **Cloud Build**, **Cloud Deploy**, **Cloud Run**, **GKE**
- CI/CD pipelines often inject the commit SHA and use it as an image tag automatically.

❌ **Why Other Options Are Incorrect:**

**A. Require developers to tag each commit with the date and time of the commit**

- Git already records **timestamped metadata** for every commit.
- Manual tagging introduces **human error**, inconsistency, and **is not reliable for deployments**.

**B. Instruct developers to include a comment in each commit that references the corresponding deployment**

- Comments are **non-enforceable and non-unique**.
- You cannot reliably associate deployments with code.
- It’s backwards — you want the deployment to **reference the commit**, not the other way around.

**D. Have developers tag all commits with the label “latest”**

- The tag `"latest"` is **ambiguous** and **mutable**.
- It **overwrites previous versions**, which makes it **impossible to audit** what version of code was deployed.
- Using `"latest"` in production is a **well-known anti-pattern**.

✅ **Final Recommendation:**

**Tag container images with the Git commit hash** to ensure **strong traceability**, **auditability**, and **clarity** in your production deployment process.

</details>

---

### Exam 3 · Q29

At **VirtuScale Technologies**, you're migrating several **third-party applications** from **performance-optimized on-premises virtual machines** to **Google Cloud**. These applications show **consistent usage patterns** over multiple weeks, but you're uncertain about the ideal **CPU and memory configurations** in the cloud. Your goal is to **optimize resource usage** while **minimizing costs**.

**What should you do to achieve this?**

- A. Create an **instance template** with the smallest available machine type, using an image of the application from your on-premises VM. Then, set up a **managed instance group** that autoscales based on **average CPU utilization**, and adjust the utilization threshold to optimize the instance count.
- B. Deploy the application in an **App Engine flexible environment** using a **Dockerfile** and custom runtime. Define **CPU and memory settings** similar to the on-prem VM in the `app.yaml` file.
- C. Provision **multiple Compute Engine instances** with various CPU and memory settings. Install the **Cloud Monitoring agent**, deploy the application on each, run **high-traffic load tests**, and use the results to determine the most suitable configuration.
- D. Launch a **Compute Engine instance** with CPU and memory settings similar to your on-prem setup. Install the **Cloud Monitoring agent**, deploy the application, perform **normal-traffic load testing**, and follow **Rightsizing Recommendations** in the **Cloud Console**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Launch a **Compute Engine instance** with CPU and memory settings similar to your on-prem setup. Install the **Cloud Monitoring agent**, deploy the application, perform **normal-traffic load testing**, and follow **Rightsizing Recommendations** in the **Cloud Console**.

The correct answer is:
**D. Launch a Compute Engine instance with CPU and memory settings similar to your on-prem setup. Install the Cloud Monitoring agent, deploy the application, perform normal-traffic load testing, and follow Rightsizing Recommendations in the Cloud Console.**

✅ Justification for Correct Option (D):

- **Rightsizing Recommendations** in Google Cloud help optimize your VM usage based on **actual performance metrics** collected over time.
- By deploying your application with **initially estimated resources** (e.g., from your on-prem setup) and monitoring it under **real-world traffic**, you can collect **accurate usage data** using the **Cloud Monitoring agent**.
- Google Cloud then analyzes CPU and memory utilization and provides **customized recommendations** for scaling up or down to **reduce costs without impacting performance**.

This approach is **cost-effective**, **accurate**, and aligned with **Google Cloud best practices** for optimizing resource utilization.

**Official Documentation:**

- Compute Engine Rightsizing Recommendations
- Installing the Monitoring Agent

❌ Why Other Options Are Incorrect:

A.

Use the smallest machine type in an instance group with autoscaling based on CPU.

- **Incorrect** because:
  - Autoscaling is suitable for **horizontal scaling** and stateless applications, not for right-sizing individual VM **vertical resource allocation**.
  - Starting with the **smallest machine type** may lead to **performance bottlenecks** and **false autoscaling triggers**.
  - This approach does not help determine **ideal per-VM CPU/memory configuration**.

B.

Deploy to App Engine flexible environment with Dockerfile and on-prem settings.

- **App Engine flexible environment** is good for certain web apps, but not always suitable for **third-party VM-based applications**, especially those with complex dependencies.
- This method **does not help optimize** CPU/memory utilization — it just **replicates on-prem settings** without performance insight.

C.

Provision multiple instance types and run high-traffic load tests to choose the best.

- This is **labor-intensive, costly, and inefficient**.
- Running full-scale **load tests on multiple instance types** manually does not scale and wastes time/resources.
- Google Cloud’s **built-in rightsizing tools** already automate and optimize this process using actual workload patterns.

✅ Final Answer: **D**

It provides an **efficient, data-driven approach** to identifying the **most cost-effective and performance-optimized configuration** using **built-in Google Cloud tooling and monitoring**.

- Link -[https://cloud.google.com/migrate/compute-engine/docs/4.9/concepts/planning-a-migration/cloud-instance-rightsizing?hl=en](https://cloud.google.com/migrate/compute-engine/docs/4.9/concepts/planning-a-migration/cloud-instance-rightsizing?hl=en)

</details>

---

### Exam 3 · Q33

A **lead developer at CloudInnovate Systems** informs you that their new application architecture utilizes **WebSockets** and **non-distributed HTTP sessions**, meaning session state is maintained on individual web servers. You want to ensure the application will function properly when deployed to **Google Cloud Platform (GCP)**.

**What should you do to support this deployment?**

- A.Assist the developer in **modifying the WebSocket implementation** to use **HTTP streaming** instead.
- B.Coordinate with the **security team** to review **encryption requirements** for WebSocket traffic.
- C.Organize a discussion between the **cloud operations team** and the developer to explore **Google Cloud load balancing** options.
- D.Help the developer **redesign the application** to use **distributed session management** and eliminate dependencies on WebSockets and local HTTP sessions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C.Organize a discussion between the **cloud operations team** and the developer to explore **Google Cloud load balancing** options.

The correct answer is:
**C. Organize a discussion between the cloud operations team and the developer to explore Google Cloud load balancing options.**

✅ Justification for Correct Option (C):

- The application uses **WebSockets** and **non-distributed HTTP sessions** (i.e., session state is tied to individual web servers).
- In this architecture, it is **critical that clients consistently connect to the same backend server** (also known as **session affinity** or **sticky sessions**).
- **Google Cloud HTTP(S) Load Balancer** supports **WebSockets** and also provides **session affinity options** using client IP, cookies, or headers.

Thus, organizing a discussion with the cloud operations team ensures:

- The right **load balancer configuration** (such as enabling **session affinity**) is chosen.
- The team is aware of the **requirements for maintaining WebSocket connections and local session state**.
- There is **alignment between infrastructure capabilities and application architecture**.

**Official Documentation:**

- HTTP(S) Load Balancing and WebSockets
- Session Affinity with Load Balancers

❌ Why Other Options Are Incorrect:

A.

Modify WebSocket implementation to use HTTP streaming.

- **WebSockets and HTTP streaming** are **different technologies** with different use cases and capabilities.
- Replacing WebSockets with HTTP streaming could **break core application functionality**, and contradicts the application's architectural design.

B.

Review encryption requirements for WebSocket traffic.

- While security is always important, the core issue here is **application functionality**, not **data protection**.
- GCP’s HTTP(S) Load Balancer already supports **TLS termination** for secure WebSocket traffic.
- This doesn’t address the **load balancing and session affinity** needs.

D.

Redesign the app to use distributed session management and eliminate WebSockets.

- While using distributed session storage (e.g., Redis) is a good practice, this option involves **significant redesign**.
- The goal is to **support the current architecture**, not **replace** it entirely.

✅ Final Answer: **C**

It focuses on configuring Google Cloud’s infrastructure (load balancing and session affinity) to **support the existing WebSocket-based, non-distributed session architecture** with **minimal changes**, aligning with the practical deployment needs.

Ref - [https://cloud.google.com/load-balancing/docs/https#websocket_support](https://cloud.google.com/load-balancing/docs/https#websocket_support)

</details>

---

### Exam 3 · Q36

Your company, **CloudNova Technologies**, uses **Google Kubernetes Engine (GKE)** as the primary platform for running all workloads. Currently, there's a **single large GKE cluster** with a **node pool of 200 nodes** hosting a mix of **batch, stateful, and stateless workloads**.

To optimize operations, the organization wants to **reduce infrastructure costs** while ensuring **no loss of availability**.

**What should you do to meet these goals?**

- A.Create a second GKE cluster dedicated to **batch workloads**, and **split the original 200 nodes** between the two clusters.
- B.Define **CPU and memory limits** at the **namespace level**, and require that all Pods specify **CPU and memory limits** in their configurations.
- C.Configure a **HorizontalPodAutoscaler** for all **stateless** and **autoscaling-compatible stateful workloads**, and enable **cluster autoscaling** on the GKE cluster.
- D.Reconfigure the current **node pool** to use **preemptible VMs** to reduce compute costs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C.Configure a **HorizontalPodAutoscaler** for all **stateless** and **autoscaling-compatible stateful workloads**, and enable **cluster autoscaling** on the GKE cluster.

The correct answer is:
**C. Configure a HorizontalPodAutoscaler for all stateless and autoscaling-compatible stateful workloads, and enable cluster autoscaling on the GKE cluster.**

✅ Justification for Correct Option (C):

This option aligns perfectly with both goals: **reducing infrastructure costs** and **ensuring availability**.

Here's why:

- **HorizontalPodAutoscaler (HPA)** automatically adjusts the number of pod replicas based on resource utilization (like CPU, memory, or custom metrics). This ensures workloads scale **up when needed** and **down when idle**, optimizing resource usage.
- **Cluster Autoscaler** works in tandem with HPA by automatically **adding or removing nodes** based on the cluster's workload demands. It removes underutilized nodes when pods no longer need them and adds nodes when there's insufficient capacity.
- When configured correctly, this combination results in:
  - **Cost savings** during low usage periods
  - **Automatic scaling** to maintain availability during demand spikes
  - **Optimized resource usage** across the cluster

**Official Documentation:**

- Horizontal Pod Autoscaler
- Cluster Autoscaler on GKE

❌ Why Other Options Are Incorrect:

A.

Create a second GKE cluster and split the nodes.

- **Incorrect** because:
  - Maintaining multiple clusters increases **operational complexity and costs** (e.g., logging, monitoring, network overhead).
  - Splitting existing resources might **degrade performance or availability** without delivering proportional cost benefits.

B.

Define CPU and memory limits at the namespace level and require limits in pod specs.

- While this is a **good practice for resource management and quota enforcement**, it doesn’t **automatically optimize utilization or reduce costs**.
- It lacks **dynamic scaling**, so it alone won’t meet the cost-saving and availability goals.

D.

Use preemptible VMs in the node pool.

- **Preemptible VMs** (now called **Spot VMs**) can reduce costs significantly, but:
  - They are **ephemeral** and can be **terminated at any time**, making them **unsuitable for critical or stateful workloads** unless carefully isolated.
  - Using only preemptible VMs in a mixed-workload cluster can compromise **availability and stability**.

✅ Final Answer: **C**

Because it enables **dynamic workload and infrastructure scaling**, delivering both **cost efficiency** and **high availability** — a **Google Cloud best practice** for production-grade GKE environments.

</details>

---

### Exam 4 · Q1

**DataNova Corp.** uses **BigQuery** as its data warehouse in a **pay-per-query pricing model**. You want to monitor **query activity in real time**, identify the **most expensive queries**, and determine **which users are generating the highest costs**.

What should you do?

- A. Add **labels** for each user to the BigQuery dataset containing the queried tables Go to the **Billing page** of the project Select **Reports** Filter the product by **BigQuery** and select the **user** you want to analyze
- B. Create a **Cloud Logging sink** to export **BigQuery Data Access logs** to **BigQuery** Use **SQL queries** on the exported logs to extract cost and usage details per user
- C. Create a **Cloud Logging sink** to export **BigQuery Data Access logs** to **Cloud Storage** Use a **Dataflow pipeline** to analyze the exported logs and compute costs per user
- D. Enable **Billing Export to BigQuery** Query the exported **billing dataset** to extract usage and cost data per user

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a **Cloud Logging sink** to export **BigQuery Data Access logs** to **BigQuery** Use **SQL queries** on the exported logs to extract cost and usage details per user

✅ Correct Answer:

**B. Create a Cloud Logging sink to export BigQuery Data Access logs to BigQuery
Use SQL queries on the exported logs to extract cost and usage details per user**

✅ Why Option B is Correct:

- **BigQuery Data Access logs** contain **detailed per-query metadata**, including:
  - **User identity**
  - **Query text**
  - **Query execution time**
  - **Bytes processed** (used to calculate cost)
- Exporting these logs to **BigQuery** allows **real-time or near real-time querying** of log data using SQL.
- You can calculate **query cost per user** using the **bytes processed** field (`metadata.jobChange.jobStats.totalProcessedBytes`).

**Official Documentation:**

- BigQuery Audit Logs (Data Access logs)
- Analyzing BigQuery usage using audit logs

❌ Why Other Options Are Incorrect:

**A. Add labels for each user to the BigQuery dataset… then filter in the Billing page**

- **Labels apply to resources**, not individual queries or users.
- The **Billing Reports page** shows **aggregated usage** by project or label, but **not by user or query**.
- Cannot track individual query costs using this method.

**C. Export logs to Cloud Storage + analyze with Dataflow**

- Adds **unnecessary complexity** (Cloud Storage + Dataflow) for a task that can be **done entirely within BigQuery**.
- Not real-time — delayed pipeline execution and higher operational overhead.
- Costlier and harder to manage than direct BigQuery export.

**D. Enable Billing Export to BigQuery + query exported dataset**

- **Billing export shows cost per service/project**, but **does not include per-query or per-user details**.
- Cannot distinguish individual users or specific queries responsible for BigQuery costs.

**Reference:**
[https://cloud.google.com/billing/docs/how-to/export-data-bigquery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)

✅ Final Answer:

**B. Create a Cloud Logging sink to export BigQuery Data Access logs to BigQuery
Use SQL queries on the exported logs to extract cost and usage details per user**

This is the most **real-time, granular, and efficient solution** aligned with **Google Cloud best practices** for BigQuery cost monitoring.

</details>

---

### Exam 4 · Q13

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Company overview -**

Helicopter Racing League (HRL) is a global sports league for competitive helicopter racing. Each year HRL holds the world championship and several regional league competitions where teams compete to earn a spot in the world championship. HRL offers a paid service to stream the races all over the world with live telemetry and predictions throughout each race.

**Solution concept -**

HRL wants to migrate their existing service to a new platform to expand their use of managed AI and ML services to facilitate race predictions. Additionally, as new fans engage with the sport, particularly in emerging regions, they want to move the serving of their content, both real-time and recorded, closer to their users.

**Existing technical environment -**

HRL is a public cloud-first company; the core of their mission-critical applications runs on their current public cloud provider. Video recording and editing is performed at the race tracks, and the content is encoded and transcoded, where needed, in the cloud. Enterprise-grade connectivity and local compute is provided by truck-mounted mobile data centers. Their race prediction services are hosted exclusively on their existing public cloud provider. Their existing technical environment is as follows:

Existing content is stored in an object storage service on their existing public cloud provider.

Video encoding and transcoding is performed on VMs created for each job.

Race predictions are performed using TensorFlow running on VMs in the current public cloud provider.

**Business requirements -**

HRL's owners want to expand their predictive capabilities and reduce latency for their viewers in emerging markets. Their requirements are:

Support ability to expose the predictive models to partners.

Increase predictive capabilities during and before races:

- Race results
- Mechanical failures
- Crowd sentiment

Increase telemetry and create additional insights.

Measure fan engagement with new predictions.

Enhance global availability and quality of the broadcasts.

Increase the number of concurrent viewers.

Minimize operational complexity.

Ensure compliance with regulations.

Create a merchandising revenue stream.

**Technical requirements -**

Maintain or increase prediction throughput and accuracy.

Reduce viewer latency.

Increase transcoding performance.

Create real-time analytics of viewer consumption patterns and engagement.

Create a data mart to enable processing of large volumes of race data.

**Executive statement -**

Our CEO, S. Hawke, wants to bring high-adrenaline racing to fans all around the world. We listen to our fans, and they want enhanced video streams that include predictions of events within the race (e.g., overtaking). Our current platform allows us to predict race outcomes but lacks the facility to support real-time predictions during races and the capacity to process season-long results.

**Question**

In the context of the Helicopter Racing League (HRL) case study, what action should you take to establish Airwolf, the in-house penetration test Cloud Function, to run on a recurring weekly basis against the predictive capability application released every Tuesday?

- A. Establish Cloud Tasks and a Cloud Storage bucket that activates a Cloud Function.
- B. Establish a Cloud Logging sink and a Cloud Storage bucket that activates a Cloud Function.
- C. Configure the deployment job to inform a Pub/Sub queue that activates a Cloud Function.
- D. Establish Identity and Access Management (IAM) and Confidential Computing to activate a Cloud Function.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Configure the deployment job to inform a Pub/Sub queue that activates a Cloud Function.

**C. Configure the deployment job to inform a Pub/Sub queue that activates a Cloud Function.**

**Reasoning:**

- **Predictable Trigger:** The deployment of the predictive capability application is a consistent and known event occurring every Tuesday. It becomes an ideal trigger for the penetration test.
- **Pub/Sub as a Decoupling Mechanism:** Pub/Sub acts as a reliable message queue that decouples the deployment job from the Cloud Function. This allows for scalability, retries, and potential future expansion without tightly binding the components.
- **Flexibility:** The Pub/Sub model allows for fine-grained control over how and when the Cloud Function is executed. If the scheduling needs become more complex in the future, Pub/Sub can support those changes.

**Why Others Are Less Optimal:**

- **A. Cloud Tasks and Cloud Storage:** While a viable solution, the requirement for a weekly execution makes this less direct than a trigger tied to the deployment. A Cloud Storage solution would also require monitoring file changes to trigger the function.
- **B. Cloud Logging sink and Cloud Storage:** This approach focuses on reacting to log events and is not as closely aligned with the predictable nature of application deployment.
- **D. IAM and Confidential Computing:** IAM deals with authentication and authorization, and Confidential Computing focuses on encryption in use. These are not directly relevant to scheduling the penetration test.

**Additional Considerations**

- **Cloud Scheduler:** A simpler alternative would be to use Cloud Scheduler to trigger the Cloud Function directly on a weekly schedule. This removes the complexity of Pub/Sub but may be slightly less flexible long-term.

References:

[https://cloud.google.com/appengine/docs/flexible/nodejs/scheduling-jobs-with-cron-yaml https://cloud.google.com/scheduler/docs/tut-pub-sub](https://cloud.google.com/appengine/docs/flexible/nodejs/scheduling-jobs-with-cron-yaml   https://cloud.google.com/scheduler/docs/tut-pub-sub)

**⚠️ Note:** Cloud Scheduler could also run the test weekly, but triggering it from the Tuesday deployment job guarantees it runs against the new release. Cloud Functions is now Cloud Run functions. HRL is a legacy case study.

</details>

---

### Exam 4 · Q16

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Company overview -**

Helicopter Racing League (HRL) is a global sports league for competitive helicopter racing. Each year HRL holds the world championship and several regional league competitions where teams compete to earn a spot in the world championship. HRL offers a paid service to stream the races all over the world with live telemetry and predictions throughout each race.

**Solution concept -**

HRL wants to migrate their existing service to a new platform to expand their use of managed AI and ML services to facilitate race predictions. Additionally, as new fans engage with the sport, particularly in emerging regions, they want to move the serving of their content, both real-time and recorded, closer to their users.

**Existing technical environment -**

HRL is a public cloud-first company; the core of their mission-critical applications runs on their current public cloud provider. Video recording and editing is performed at the race tracks, and the content is encoded and transcoded, where needed, in the cloud. Enterprise-grade connectivity and local compute is provided by truck-mounted mobile data centers. Their race prediction services are hosted exclusively on their existing public cloud provider. Their existing technical environment is as follows:

Existing content is stored in an object storage service on their existing public cloud provider.

Video encoding and transcoding is performed on VMs created for each job.

Race predictions are performed using TensorFlow running on VMs in the current public cloud provider.

**Business requirements -**

HRL's owners want to expand their predictive capabilities and reduce latency for their viewers in emerging markets. Their requirements are:

Support ability to expose the predictive models to partners.

Increase predictive capabilities during and before races:

- Race results
- Mechanical failures
- Crowd sentiment

Increase telemetry and create additional insights.

Measure fan engagement with new predictions.

Enhance global availability and quality of the broadcasts.

Increase the number of concurrent viewers.

Minimize operational complexity.

Ensure compliance with regulations.

Create a merchandising revenue stream.

**Technical requirements -**

Maintain or increase prediction throughput and accuracy.

Reduce viewer latency.

Increase transcoding performance.

Create real-time analytics of viewer consumption patterns and engagement.

Create a data mart to enable processing of large volumes of race data.

**Executive statement -**

Our CEO, S. Hawke, wants to bring high-adrenaline racing to fans all around the world. We listen to our fans, and they want enhanced video streams that include predictions of events within the race (e.g., overtaking). Our current platform allows us to predict race outcomes but lacks the facility to support real-time predictions during races and the capacity to process season-long results.

**Question**

In reference to the Helicopter Racing League (HRL) case study, a recent finance audit of cloud infrastructure highlighted a notably high number of Compute Engine instances allocated for video encoding and transcoding. There is suspicion that these Virtual Machines may be zombie machines left undeleted after completing their workloads. An urgent need arises to compile a list of idle VM instances. What action should be taken?

- A. Access each Compute Engine instance individually and gather disk, CPU, memory, and network usage statistics for analysis.
- B. Utilize the gcloud compute instances list command to identify the virtual machine instances labeled with idle: true.
- C. Employ the gcloud recommender command to generate a list of idle virtual machine instances.
- D. Through the Google Console, pinpoint which Compute Engine instances within the managed instance groups are no longer responsive to health check probes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Employ the gcloud recommender command to generate a list of idle virtual machine instances.

**C. Employ the gcloud recommender command to generate a list of idle virtual machine instances.**

This is the most direct and efficient way to address the specific problem. Here's why:

- **Idle VM Detection:** The `gcloud recommender` command includes an "Idle VM" recommender type, which is designed to analyze usage metrics (CPU, network) and identify instances that have been underutilized for an extended period.
- **Automation:** This approach leverages automation and Google's built-in monitoring capabilities rather than individual manual checks.
- **Actionable Output:** The `gcloud recommender` command will provide a list of the potentially idle VMs along with recommendations on how to address them (e.g., stop, resize, terminate).

**Why Other Options Are Less Optimal:**

- **A. Access each Compute Engine instance individually...:** This is labor-intensive, error-prone, and doesn't scale well, especially if there are a large number of instances.
- **B. Utilize the gcloud compute instances list...:** While the list command can provide information about VM instances, it won't have built-in logic to flag them specifically as "idle" based on usage patterns.
- **D. Through the Google Console, pinpoint...:** This focuses on unresponsive VMs within managed instance groups. While useful for health checks, it doesn't directly target instances that are idle but operational.

**Important Note:** Even if there aren't strictly "zombie" machines, the `gcloud recommender` output could identify instances that are over-provisioned and underutilized, helping HRL optimize costs regardless.

References:

[https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendationshttps://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations#viewing_idle_vm_instance_recommendations](https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations  https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations#viewing_idle_vm_instance_recommendations)

</details>

---

### Exam 4 · Q24

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for the most popular mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers.

Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime, downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Connect to a managed NoSQL database service
- 3. Run customize Linux distro

Requirements for Game Analytics Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Process incoming data on the fly directly from the game servers
- 3. Process data that arrives late because of slow mobile networks
- 4. Allow SQL queries to access at least 10 TB of historical data
- 5. Process files that are regularly uploaded by users' mobile devices
- 6. Use only fully managed services

**CEO Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users.

**CTO Statement -**

Our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**CFO Statement -**

We are not capturing enough user demographic data, usage metrics, and other KPIs. As a result, we do not engage the right users, we are not confident that our marketing is targeting the right users, and we are not selling enough premium Blast-Ups inside the games, which dramatically impacts our revenue.

**Question**

**Mountkirk Games requires you to devise their new testing strategy. How should the test coverage deviate from their existing backends on other platforms?**

- A. Tests should scale well beyond the prior approaches.
- B. Unit tests are no longer necessary; only end-to-end tests.
- C. Tests should be implemented after the release is deployed in the production environment.
- D. Tests should involve directly assessing the Google Cloud Platform (GCP) infrastructure.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Tests should scale well beyond the prior approaches.

The best choice here is **A. Tests should scale well beyond the prior approaches.** Here's why, along with a breakdown of why the other options aren't optimal:

**Why Scaling Test Coverage is Key**

- **Cloud Benefits:** One of the key advantages of migrating to Google Cloud Platform is its scalability and elasticity. Testing should be designed to ensure your applications leverage this.
- **Performance Testing:** Load testing and stress testing are crucial for ensuring your applications can handle the potential scale provided by GCP.
- **Reliability:** Test for edge cases and failure scenarios to ensure the applications are robust and can recover gracefully as GCP dynamically scales resources.

**Why Other Options Are Unsuitable**

- **B. Unit tests are no longer necessary; only end-to-end tests.** Unit and end-to-end tests serve different purposes. Unit tests verify the smallest units of code in isolation, while end-to-end tests assess the entire system. Both are essential in a comprehensive testing strategy.
- **C. Tests should be implemented after the release is deployed in the production environment.** Prioritizing pre-deployment testing is always the way to go. Testing earlier in the development lifecycle can catch issues sooner, saving time, cost, and potential production failures.
- **D. Tests should involve directly assessing the Google Cloud Platform (GCP) infrastructure.** While some testing of GCP's behavior is valuable, your primary focus should be testing *your application's* functionality and performance on GCP. Google handles the underlying infrastructure testing.

**Recommendations for Mountkirk Games**

- **Expanded Load and Stress Testing:** Focus on scenarios that simulate high user traffic, spikes in demand, and the effects of autoscaling in GCP.
- **Chaos Engineering:** Consider introducing intentional failures to test how well your applications recover under unexpected conditions. This will help build resilience on GCP.
- **Shift-Left Testing:** Integrate testing early in the development process, employing test-driven development (TDD) where applicable. This helps prevent issues from reaching production.

</details>

---

### Exam 4 · Q25

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for the most popular mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers.

Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime, downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Connect to a managed NoSQL database service
- 3. Run customize Linux distro

Requirements for Game Analytics Platform:

- 1. Dynamically scale up or down based on game activity
- 2. Process incoming data on the fly directly from the game servers
- 3. Process data that arrives late because of slow mobile networks
- 4. Allow SQL queries to access at least 10 TB of historical data
- 5. Process files that are regularly uploaded by users' mobile devices
- 6. Use only fully managed services

**CEO Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users.

**CTO Statement -**

Our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**CFO Statement -**

We are not capturing enough user demographic data, usage metrics, and other KPIs. As a result, we do not engage the right users, we are not confident that our marketing is targeting the right users, and we are not selling enough premium Blast-Ups inside the games, which dramatically impacts our revenue.

**Question**

**Mountkirk Games has launched their new backend on Google Cloud Platform (GCP), and you aim to establish a comprehensive testing process for new backend versions before public release, ensuring scalable and cost-effective testing environments. How should you design the process?**

- A. Develop a scalable environment within GCP to emulate production load.
- B. Utilize the existing infrastructure to test the GCP-based backend at scale.
- C. Incorporate stress tests into each component of the application, utilizing internal GCP resources to simulate load.
- D. Establish a set of static environments within GCP to test various load levels, such as high, medium, and low.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Develop a scalable environment within GCP to emulate production load.

Here's why

**A. Develop a scalable environment within GCP to emulate production load** is the best approach, along with considerations on the other options:

**Why Option A Is Ideal:**

- **Realistic Testing:** A scalable testing environment in GCP allows you to closely mirror your production environment. This leads to more reliable test results because you can simulate realistic traffic patterns and uncover performance bottlenecks that you might not see in less representative environments.
- **Scalability for Varying Load:** GCP's flexibility allows you to easily scale up or down your testing environment to match different load levels. This allows you to test how your backend performs under both expected and peak traffic volumes.
- **Cost-Effectiveness:** While there are costs involved, replicating your production environment in GCP allows you to identify and fix performance issues before release, ultimately saving you money by preventing downtime or poor user experience in production.

**Considerations Regarding Other Options:**

- **B. Utilize the existing infrastructure to test the GCP-based backend at scale.** This assumes that your existing infrastructure has the capacity to handle both your production load and the additional testing load. This is often not the case, and overloading your production environment with tests can have negative consequences.
- **C. Incorporate stress tests into each component of the application, utilizing internal GCP resources to simulate load.** Stress tests are valuable, but they shouldn't be the sole focus. You also need test environments that closely resemble production to catch subtle integration or performance issues.
- **D. Establish a set of static environments within GCP to test various load levels, such as high, medium, and low.** Static environments can be useful, but a truly scalable environment in GCP offers greater flexibility for on-demand testing and more realistic simulation of production traffic behavior.

</details>

---

### Exam 4 · Q33

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**In the Mountkirk Games case study, Mountkirk Games tasks you with designing a method to assess the analytics platform's resilience to changes in mobile network latency. What approach should you take?**

- A. Implement failure injection software within the game analytics platform to introduce additional latency to mobile client analytics traffic.
- B. Develop a test client capable of running from a mobile phone emulator on a Compute Engine virtual machine, running multiple instances across various Google Cloud Platform regions globally to simulate realistic traffic.
- C. Incorporate the capability to introduce a random delay before processing analytics files uploaded from mobile devices.
- D. Launch an opt-in beta version of the game on players' mobile devices, gathering response times from analytics endpoints hosted in Google Cloud Platform regions worldwide.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Implement failure injection software within the game analytics platform to introduce additional latency to mobile client analytics traffic.

Let's analyze why Option A (implement failure injection software within the game analytics platform to introduce additional latency to mobile client analytics traffic) might be a strong contender. Here's a case for why it could be the best choice:

**Advantages of Failure Injection (Option A):**

- **Direct Manipulation:** Introducing latency within the analytics platform allows you to precisely target the component you want to test. It isolates the effects of latency specifically on the analytics processing.
- **Granular Control:** You have fine-grained control over the duration and distribution of injected latency. This makes it easier to conduct structured experiments and identify the analytics platform's breaking points.
- **Targeted Focus:** If the main goal is to understand how disruptions within the analytics pipeline itself impact data processing timeliness and accuracy, this is a more direct approach than simulating network conditions externally.

**Considerations: Why Option B and other Might Be Less Ideal**

While simulating user devices across regions (Option B) seems intuitive, it introduces more variables into the testing scenario:

- **External Factors:** External network latency can be inconsistent and influenced by factors outside your control. This makes it harder to pinpoint whether the analytics platform is the bottleneck or if it's the external network conditions.
- **Scope of the Problem:** If the primary issue lies with how the platform handles delays caused by external factors, then Option B is more relevant. However, if the core problem is its resilience to latency introduced within its own processes, then Option A is a better fit.

- **C. Incorporate the capability to introduce a random delay before processing analytics files uploaded from mobile devices.** This focuses on the processing side of the analytics pipeline and is less effective than simulating end-to-end latency from the user's device through the network to the backend.
- **D. Launch an opt-in beta version of the game on players' mobile devices, gathering response times from analytics endpoints hosted in Google Cloud Platform regions worldwide.** This involves real users, making results less predictable and harder to directly correlate with specific, controlled levels of latency for testing purposes.

References:

[https://istio.io/latest/docs/tasks/traffic-management/fault-injection/#injecting-an-http-delay-fault](https://istio.io/latest/docs/tasks/traffic-management/fault-injection/#injecting-an-http-delay-fault)

**⚠️ Note:** Option B also simulates real latency, but failure injection gives precise, repeatable control over the latency added, which is why it is keyed.

</details>

---

### Exam 4 · Q43

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company Overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They build all of their games using some server-side integration. Historically, they have used cloud providers to lease physical servers. Due to the unexpected popularity of some of their games, they have had problems scaling their global audience, application servers, MySQL databases, and analytics tools.

Their current model is to write game statistics to files and send them through an ETL tool that loads them into a centralized MySQL database for reporting.

**Solution Concept -**

Mountkirk Games is building a new game, which they expect to be very popular. They plan to deploy the game's backend on Google Compute Engine so they can capture streaming metrics, run intensive analytics, and take advantage of its autoscaling server environment and integrate with a managed NoSQL database.

**Business Requirements -**

- Increase to a global footprint
- Improve uptime downtime is loss of players
- Increase efficiency of the cloud resources we use
- Reduce latency to all customers

**Technical Requirements -**

Requirements for Game Backend Platform

- Dynamically scale up or down based on game activity
- Connect to a transactional database service to manage user profiles and game state
- Store game activity in a timeseries database service for future analysis
- As the system scales, ensure that data is not lost due to processing backlogs
- Run hardened Linux distro

Requirements for Game Analytics Platform

- Dynamically scale up or down based on game activity
- Process incoming data on the fly directly from the game servers
- Process data that arrives late because of slow mobile networks
- Allow queries to access at least 10 TB of historical data
- Process files that are regularly uploaded by users' mobile devices

**Executive Statement -**

Our last successful game did not scale well with our previous cloud provider, resulting in lower user adoption and affecting the game's reputation. Our investors want more key performance indicators (KPIs) to evaluate the speed and stability of the game, as well as other metrics that provide deeper insight into usage patterns so we can adapt the game to target users. Additionally, our current technology stack cannot provide the scale we need, so we want to replace MySQL and move to an environment that provides autoscaling, low latency load balancing, and frees us up from managing physical servers.

**Question**

**To efficiently and cost-effectively test the new mobile game app across various configurations on Android and iOS devices, what approach should you take?**

- A. Utilize Firebase Test Lab by uploading the mobile app and conducting testing on both Android and iOS devices.
- B. Set up Android and iOS virtual machines (VMs) on Google Cloud, install the mobile app on the VMs, and conduct testing.
- C. Deploy Android and iOS containers on Google Kubernetes Engine (GKE), install the mobile app on the containers, and conduct testing.
- D. Upload the mobile app with different configurations to Firebase Hosting and conduct testing for each configuration.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Utilize Firebase Test Lab by uploading the mobile app and conducting testing on both Android and iOS devices.

The most efficient and cost-effective approach for Mountkirk Games is:

**A. Utilize Firebase Test Lab by uploading the mobile app and conducting testing on both Android and iOS devices.**

Here's why this is the ideal solution:

- **Comprehensive Device Coverage:** Firebase Test Lab offers a wide range of physical Android and iOS devices, helping to ensure compatibility across different screen sizes, resolutions, and hardware configurations.
- **Scalability:** Testing can be run on multiple devices simultaneously, speeding up the testing process and allowing for quicker iterations to resolve compatibility issues.
- **Convenience:** Firebase Test Lab provides a user-friendly interface for uploading test builds, defining test configurations, and viewing detailed test reports with logs and screenshots.
- **Cost-Effective:** Google Firebase offers flexible pricing plans based on device time usage, allowing you to control costs.
- **Integration with Development Workflow:** Firebase Test Lab can be integrated into your CI/CD pipeline to automate testing.

**Why Other Options Are Less Optimal:**

- **B. Set up Android and iOS virtual machines (VMs) on Google Cloud, install the mobile app on the VMs, and conduct testing.** While VMs provide flexibility, managing and maintaining a pool of different Android and iOS VMs can become complex and time-consuming. Additionally, virtual machines may not always fully replicate the behavior of physical devices.
- **C. Deploy Android and iOS containers on Google Kubernetes Engine (GKE), install the mobile app on the containers, and conduct testing.** Similar to VMs, managing the containerized testing environment on GKE introduces unnecessary complexity compared to a purpose-built testing solution like Firebase Test Lab.
- **D. Upload the mobile app with different configurations to Firebase Hosting and conduct testing for each configuration.** Firebase Hosting is primarily for web app hosting. While it might allow basic manual testing, it lacks the comprehensive device coverage and advanced functionality offered by Firebase Test Lab.

**Additional Considerations**

- **Test Types:** Firebase Test Lab supports various test types:
  - *Instrumentation tests:* Code-level tests for specific app functionality.
  - *Robo tests:* Simulated user interactions to test UI flows.
  - *Game Loop tests:* Specifically for game testing, executing pre-defined gameplay scenarios at a high frame rate.
- **Reporting:** Utilize Firebase Test Lab's detailed reports to pinpoint errors and performance bottlenecks in your game across different devices.

**References:**

[https://firebase.google.com/docs/test-lab](https://firebase.google.com/docs/test-lab)

</details>

---

### Exam 4 · Q48

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company overview -**

TerramEarth manufactures heavy equipment for the mining and agricultural industries. They currently have over 500 dealers and service centers in 100 countries. Their mission is to build products that make their customers more productive.

**Solution concept -**

There are 2 million TerramEarth vehicles in operation currently, and we see 20% yearly growth. Vehicles collect telemetry data from many sensors during operation. A small subset of critical data is transmitted from the vehicles in real time to facilitate fleet management. The rest of the sensor data is collected, compressed, and uploaded daily when the vehicles return to home base. Each vehicle usually generates 200 to 500 megabytes of data per day.

**Existing technical environment -**

TerramEarth's vehicle data aggregation and analysis infrastructure resides in Google Cloud and serves clients from all around the world. A growing amount of sensor data is captured from their two main manufacturing plants and sent to private data centers that contain their legacy inventory and logistics management systems. The private data centers have multiple network interconnects configured to Google Cloud. The web frontend for dealers and customers is running in

Google Cloud and allows access to stock management and analytics.

**Business requirements -**

- Predict and detect vehicle malfunction and rapidly ship parts to dealerships for just-in-time repair where possible.
- Decrease cloud operational costs and adapt to seasonality.
- Increase speed and reliability of development workflow.
- Allow remote developers to be productive without compromising code or data security.
- Create a flexible and scalable platform for developers to create custom API services for dealers and partners.

**Technical requirements -**

- Create a new abstraction layer for HTTP API access to their legacy systems to enable a gradual move into the cloud without disrupting operations.
- Modernize all CI/CD pipelines to allow developers to deploy container-based workloads in highly scalable environments.
- Allow developers to run experiments without compromising security and governance requirements.
- Create a self-service portal for internal and partner developers to create new projects, request resources for data analytics jobs, and centrally manage access to the API endpoints.
- Use cloud-native solutions for keys and secrets management and optimize for identity-based access.
- Improve and standardize tools necessary for application and network monitoring and troubleshooting.

**Executive statement -**

Our competitive advantage has always been our focus on the customer, with our ability to provide excellent customer service and minimize vehicle downtimes. After moving multiple systems into Google Cloud, we are seeking new ways to provide best-in-class online fleet management services to our customers and improve operations of our dealerships. Our 5-year strategic plan is to create a partner ecosystem of new products by enabling access to our data, increasing autonomous operation capabilities of our vehicles, and creating a path to move the remaining legacy systems to the cloud.

**Question**

**In line with Google-recommended practices and considering the TerramEarth case study where a microservice-based application is being developed using Docker containers, what approach should you take to continuously build the application and store the build artifacts?**

- A. Set up a trigger in Cloud Build to respond to new source changes. Utilize Cloud Build to build container images for each microservice, tagging them with the code commit hash, and then push the images to the Container Registry.
- B. Configure a trigger in Cloud Build to handle new source changes. This trigger should initiate build jobs to construct container images for the microservices, tagging these images with a version number before pushing them to Cloud Storage.
- C. Establish a Scheduler job to monitor the repository every minute. Upon detecting new changes, trigger Cloud Build to build container images for the microservices. Tag the images using the current timestamp and then push them to the Container Registry.
- D. Implement a trigger in Cloud Build to handle new source changes. Utilize Cloud Build to construct a single container image, tagging it with the label 'latest,' and then push this image to the Container Registry.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up a trigger in Cloud Build to respond to new source changes. Utilize Cloud Build to build container images for each microservice, tagging them with the code commit hash, and then push the images to the Container Registry.

Here's why option **A** is the best practice for TerramEarth's container-based microservice development:

**A. Set up a trigger in Cloud Build to respond to new source changes. Utilize Cloud Build to build container images for each microservice, tagging them with the code commit hash, and then push the images to the Container Registry.**

- **Automation & Efficiency:** Triggers streamline the build process, automatically rebuilding images whenever source code changes occur, ensuring consistency.
- **Versioning:** Tagging with commit hashes provides traceability back to the source code, aiding debugging, rollbacks, and understanding what version of the code is deployed.
- **Container Registry:** Google's managed Container Registry offers secure, reliable storage, and access control for container images, crucial for managing microservices at scale.
- **Google Best Practice:** Aligns perfectly with Google-recommended practices for container image management in a CI/CD context.

**Why Other Options Are Less Optimal:**

- **B. Configure a trigger in Cloud Build...pushing them to Cloud Storage.** While Cloud Build can handle container builds, Cloud Storage is designed for general object storage, not optimized for container image management like Container Registry.
- **C. Establish a Scheduler job...** Timed triggers can lead to unnecessary builds if no code changes have occurred. This can waste resources and create redundancy.
- **D. Implement a trigger in Cloud Build...tagging it with the label 'latest,'...** Using 'latest' is problematic as it overwrites existing versions and makes rollbacks harder. Commit hashes are a superior way to track image versions.

**Additional Considerations:**

- **CI/CD Pipeline:** Integrate Cloud Build into a full CI/CD pipeline that encompasses testing, deployment, and other stages of the development lifecycle.
- **Artifact Management:** Container Registry has features like vulnerability scanning and image expiration to further optimize security and management of microservice artifacts.

References:

[https://cloud.google.com/architecture/best-practices-for-building-containers#tagging_using_the_git_commit_hashhttps://cloud.google.com/container-registry/docs/overview](https://cloud.google.com/architecture/best-practices-for-building-containers#tagging_using_the_git_commit_hash  https://cloud.google.com/container-registry/docs/overview)

**⚠️ Note:** Container Registry was shut down in 2025; today the images go to Artifact Registry.

</details>

---

### Exam 4 · Q50

A news feed web service hosted on Google App Engine is experiencing issues under peak load. Users report seeing previously viewed news articles, indicating a potential problem within the service's logic or its interaction with App Engine. Below is the code. What is the most likely cause of this issue?

```python
import news
from flask import Flask, redirect, request
from flask.ext.api import status
from google.appengine.api import users

app = Flask(__name__)
sessions = {}

@app.route("/")
def homepage():
    user = users.get_current_user()
    if not user:
        return "Invalid login", status.HTTP_401_UNAUTHORIZED
    if user not in sessions:
        sessions[user] = {"viewed": []}
    news_articles = news.get_new_news(user, sessions[user]["viewed"])
    sessions[user]["viewed"] += [n["id"] for n in news_articles]
    return news.render(news_articles)

if __name__ == "__main__":
    app.run()
```

- A. The session variable is local to just a single instance.
- B. The session variable is being overwritten in Cloud Datastore.
- C. The URL of the API needs modification to prevent caching.
- D. The HTTP Expires header needs to be set to -1 to prevent caching.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. The session variable is local to just a single instance.

The most likely cause of the problem is

**A. The session variable is local to just a single instance.**

Let's analyze why and explore how to resolve this issue:

**Understanding the Problem**

- **App Engine Scaling:** Google App Engine dynamically scales up and down the number of instances serving your application. This means requests might be handled by different instances over time.
- **In-Memory Storage:** The `sessions` dictionary is stored in the memory of each instance. This means:
  - Each instance has its own isolated copy of `sessions`.
  - A user's session data isn't shared across the different instances.
- **Incorrect Logic:** Due to this setup, if a user's subsequent requests are served by different instances, it could appear as if they haven't viewed certain news articles.

**Resolving the Issue: Shared Datastore**

To address this, you need to store sessions in a shared location accessible by all instances. Popular choices on Google App Engine include:

- **Cloud Datastore (or Firestore):** A scalable NoSQL database, perfect for storing session data.
- **Memcache:** A distributed in-memory caching system suitable for fast retrieval of session data.

**Code Modification Example (Using Datastore)**

Here's a rough idea of how you'd modify the code using Datastore. (This assumes you have the necessary Datastore models in place):

```python
from google.cloud import datastore

datastore_client = datastore.Client()

@app.route("/")
def homepage():
    # ... login logic ...
    session_key = datastore_client.key('Session', user.user_id())
    session = datastore_client.get(session_key)
    if not session:
        session = datastore.Entity(key=session_key)
        session['viewed'] = []
    news_articles = news.get_new_news(user, session["viewed"])
    session["viewed"] += [n["id"] for n in news_articles]
    datastore_client.put(session)  # shared by every instance
    return news.render(news_articles)
```

**Key Considerations**

- **Error Handling:** Be sure to implement appropriate error handling for Datastore operations.
- **Datastore Model:** You'll likely need to create a Datastore model (kind) to represent the session data.

</details>

---

### Exam 5 · Q4

**Altostrat Media Case Study**

**Company Overview**

Altostrat is a prominent player in the media industry, with an extensive collection of audio and video content that comprises podcasts, interviews, news broadcasts, and documentaries. Their success in delivering premium content to a diverse audience requires a content management system that can keep pace with the dynamic media landscape.

**Solution Concept**

Altostrat seeks to modernize its content management and user engagement strategies using Google Cloud's generative AI. They want a platform that empowers customers with personalized recommendations, natural language interactions, and seamless self-service support. Simultaneously, they want to drive revenue growth through dynamic pricing, targeted marketing, and personalized product suggestions.

The seamless integration of AI-powered tools into their existing Google Cloud environment will enable Altostrat to efficiently manage their vast media library, enhance user experiences, and unlock new revenue streams. Google Cloud’s generative AI will solidify their leadership in the media industry.

**Existing Technical Environment**

Altostrat's content management and delivery platform leverages GKE for scalability and high availability, essential for handling their vast media library. Their extensive media library, spanning various documents, audio and video formats, is stored in Cloud Storage. To gain valuable insights into user behavior, content consumption patterns, and audience demographics, Altostrat leverages BigQuery as their primary data warehouse. Additionally, they use Cloud Run functions for serverless execution of event-driven tasks such as video transcoding, metadata extraction, and personalized content recommendations.

While Altostrat has made significant strides in cloud adoption, they also maintain some legacy on-premises systems for specific workflows like content ingestion and archival. These systems are slated for modernization and migration to Google Cloud in the near future. User management and authentication are currently handled through a combination of Google Identity and third-party identity providers. For monitoring and observability, Altostrat relies on a mix of native Google Cloud tools like Cloud Monitoring and open-source solutions like Prometheus, with alerts primarily delivered via email notifications.

**Business Requirements**

- Accelerate and enhance the reliability of operational workflows across all environments. [Google Cloud + On-premises]
- Simplify infrastructure management for rapid application deployment.
- Optimize cloud storage costs while maintaining high availability and scalability for media content.
- Enable natural language interaction with the platform with 24/7 user support.
- Automatically generate concise summaries of media content.
- Extract rich metadata from media assets using NLP and computer vision.
- Detect and filter inappropriate content.
- Analyze media content to identify trends and extract insights.
- Inform content strategy and decision-making with data.

**Technical Requirements**

- Modernize CI/CD for containerized deployments with a centralized management platform.
- Secure, high-performance hybrid cloud connectivity for data ingestion.
- Provide scalable, performant kubernetes environments both on-premises and in the cloud.
- Optimize cloud storage costs for growing media volumes.
- Design AI-powered detection of harmful content.
- Ensure that AI systems are auditable and their decisions can be explained
- Leverage LLMs and conversational AI for personalized experiences and content virality.
- Develop advanced chatbots with natural language understanding to provide

personalized assistance.

- Automated summarization for diverse media.

**Executive Statement**

At Altostrat, we are embracing the next frontier of artificial intelligence to revolutionize our content strategy. By harnessing the power of generative AI, we will create an unparalleled user experience by empowering our audience with intelligent tools for content discovery, personalized recommendations, and seamless interaction. Reliability and cost management are our top priorities. This strategic initiative will deepen engagement, foster customer loyalty, and unlock new revenue streams through targeted marketing and tailored content offerings. We see a future where AI-driven innovation is central to our business, leading to greater success for our company and delivering exceptional value to our customers.

---

**Question:**

**Altostrat plans to modernize CI/CD for its containerized workloads running on GKE and Cloud Run. They want centralized control, automated security scanning, and consistent deployment practices across environments.**

**Which approach best satisfies these requirements?**

- A. Use Cloud Build with GitHub triggers, Artifact Registry for image storage, and Binary Authorization for policy enforcement.
- B. Deploy Jenkins on GKE with custom pipelines and store container images in Cloud Storage.
- C. Use Cloud Deploy without container scanning to simplify the release process.
- D. Build and deploy containers manually using Cloud Shell and gcloud commands.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use Cloud Build with GitHub triggers, Artifact Registry for image storage, and Binary Authorization for policy enforcement.

**Correct option: A**

**Why A best satisfies the requirements**

Altostrat wants **centralized CI/CD control**, **automated security scanning**, and **consistent deployments** across **GKE and Cloud Run**.

- **Cloud Build with GitHub triggers** provides a fully managed, centralized CI system with consistent, repeatable pipelines across environments.
- **Artifact Registry** is the recommended container image repository, with built-in vulnerability scanning and tight integration with Cloud Build and GKE.
- **Binary Authorization** enforces deployment policies so that **only trusted, scanned, and approved images** can be deployed to GKE, which directly addresses security and compliance requirements.
- This combination is a **Google-recommended reference architecture** for secure, enterprise-grade CI/CD on GKE and Cloud Run.

**Why the other options are not the best fit**

**B. Jenkins on GKE + Cloud Storage for images**

- Jenkins introduces **high operational overhead** (patching, scaling, securing).
- Cloud Storage is **not designed** for container image management or vulnerability scanning.
- Lacks native policy enforcement comparable to Binary Authorization.

**C. Cloud Deploy without container scanning**

- Cloud Deploy handles delivery orchestration, but **does not replace CI, scanning, or policy enforcement**.
- Omitting scanning fails the explicit requirement for automated security controls.

**D. Manual builds via Cloud Shell**

- Fully manual workflows do not provide centralized control, consistency, auditability, or security enforcement.
- Not suitable for production-scale CI/CD.

**Authoritative documentation link**
Secure CI/CD for containers on Google Cloud (Cloud Build, Artifact Registry, Binary Authorization):
[https://docs.cloud.google.com/binary-authorization/docs/cloud-build](https://docs.cloud.google.com/binary-authorization/docs/cloud-build)

###### Explanation

**Correct option: A**

**Why A best satisfies the requirements**

Altostrat wants **centralized CI/CD control**, **automated security scanning**, and **consistent deployments** across **GKE and Cloud Run**.

- **Cloud Build with GitHub triggers** provides a fully managed, centralized CI system with consistent, repeatable pipelines across environments.
- **Artifact Registry** is the recommended container image repository, with built-in vulnerability scanning and tight integration with Cloud Build and GKE.
- **Binary Authorization** enforces deployment policies so that **only trusted, scanned, and approved images** can be deployed to GKE, which directly addresses security and compliance requirements.
- This combination is a **Google-recommended reference architecture** for secure, enterprise-grade CI/CD on GKE and Cloud Run.

> [!note]- Why the other options are wrong
> **B. Jenkins on GKE + Cloud Storage for images**
>
> - Jenkins introduces **high operational overhead** (patching, scaling, securing).
> - Cloud Storage is **not designed** for container image management or vulnerability scanning.
> - Lacks native policy enforcement comparable to Binary Authorization.
>
> **C. Cloud Deploy without container scanning**
>
> - Cloud Deploy handles delivery orchestration, but **does not replace CI, scanning, or policy enforcement**.
> - Omitting scanning fails the explicit requirement for automated security controls.
>
> **D. Manual builds via Cloud Shell**
>
> - Fully manual workflows do not provide centralized control, consistency, auditability, or security enforcement.
> - Not suitable for production-scale CI/CD.

</details>

---

### Exam 5 · Q8

**Altostrat Media Case Study**

**Company Overview -**

Altostrat is a prominent player in the media industry, with an extensive collection of audio and video content that comprises podcasts, interviews, news broadcasts, and documentaries. Their success in delivering premium content to a diverse audience requires a content management system that can keep pace with the dynamic media landscape.

**Solution Concept -**

Altostrat seeks to modernize its content management and user engagement strategies using Google Cloud's generative AI. They want a platform that empowers customers with personalized recommendations, natural language interactions and seamless self-service support. Simultaneously, they want to drive revenue growth through dynamic pricing targeted marketing, and personalized product suggestions.

The seamless integration of AI-powered tools into the existing Google Cloud environment will enable Altostrat to efficiently manage their vast media library, enhance user experiences, and unlock new revenue streams. Google Cloud's generative AI will solidify their leadership in the media industry.

**Existing Technical Environment -**

Altostrat’s content management and delivery platform leverages GKE for scalability and high availability, essential for handling their vast media library. Their extensive media library spanning various documents, audio and video formats is stored in Cloud Storage. To gain valuable insights into user behavior, content consumption patterns, and audience demographics, Altostrat leverages BigQuery as their primary data warehouse. Additionally, they use Cloud Run functions for serverless execution of event-driven tasks such as video transcoding metadata extraction, and personalized content recommendations.

While Altostrat has made significant strides in cloud adoption, they also maintain some legacy on-premises systems for specific workflows like content ingestion and archival. These systems are slated for modernization and migration to Google Cloud in the near future. User management and authentication are currently handled through a combination of Google Identity and third-party identity providers. For monitoring and observability, Altostrat relies on a mix of native Google Cloud tools like Cloud Monitoring and open-source solutions like Prometheus, with alerts primarily delivered via email notifications.

**Business Requirements -**

- Accelerate and enhance the reliability of operational workflows across all environments. [Google Cloud + On-premises]
- Simplify infrastructure management for rapid application deployment.
- Optimize cloud storage costs while maintaining high availability and scalability for media content.
- Enable natural language interaction with the platform with 24/7 user support.
- Automatically generate concise summaries of media content.
- Extract rich metadata from media assets using NLP and computer vision.
- Detect and filter inappropriate content.
- Analyze media content to identify trends and extract insights.
- Inform content strategy and decision making with data.

**Technical Requirements -**

- Modernize CI/CD for containerized deployments with a centralized management platform.
- Secure, high-performance hybrid cloud connectivity for data ingestion.
- Provide scalable, performant kubernetes environments both on-premises and in the cloud.
- Optimize cloud storage costs for growing media volumes.
- Design AI-powered detection of harmful content.
- Ensure that AI systems are auditable and their decisions can be explained.
- Leverage LLMs and conversational AI for personalized experiences and content virality.
- Develop advanced chatbots with natural language understanding to provide personalized assistance.
- Automated summarization for diverse media.

**Executive Statement -**

At Altostrat, we are embracing the next frontier of artificial intelligence to revolutionize our content strategy. By harnessing the power of generative AI, we will create an unparalleled user experience by empowering our audience with intelligent toots for content discovery, personalized recommendations, and seamless interaction. Reliability and cost management are our top priorities. This strategic initiative will deepen engagement, foster customer loyalty, and unlock new revenue streams through targeted marketing and tailored content offerings. We see a future where Al-driven innovation is central to our business, leading to greater success for our company and delivering exceptional value to our customers.

---

**For this question, refer to the Altostrat Media case study. Altostrat’s development team has adopted a microservices architecture for their application. You need to choose the most appropriate testing method to verify that each microservice works correctly on its own, independent of others. What should you do?**

- A. Run unit testing.
- B. Use load testing.
- C. Perform end-to-end testing.
- D. Execute integration testing.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Run unit testing.

**Correct option: A — Run unit testing**

Unit testing verifies that **each microservice behaves correctly in isolation**, without depending on other services. In a microservices architecture, this is the primary technique used to validate the internal logic of a service independently. It matches the requirement in the question: *“verify that each microservice works correctly on its own.”*

**Authoritative documentation:**
[https://cloud.google.com/architecture/devops/devops-tech-test-automation](https://cloud.google.com/architecture/devops/devops-tech-test-automation)

Google’s DevOps testing guidance explicitly emphasizes unit testing as the foundation of validating individual components before integration.

**Why A is correct**

- Tests a service in isolation
- Fast feedback loop for developers
- Detects logic defects early
- Supports microservices autonomy
- Aligns with CI/CD best practices

Unit tests ensure each microservice is correct **before** interacting with other services.

**Why the other options are not the best choice**

B. Load testing
Load testing measures **performance and scalability**, not correctness of an individual service’s logic. It answers “how does it behave under stress?” rather than “does it work correctly by itself?”

C. End-to-end testing
End-to-end tests validate the **entire system workflow** across multiple services. They depend on many components and do not isolate a single microservice.

D. Integration testing
Integration testing verifies how services **interact with each other**. It is important, but it does not test independence. The question explicitly asks for testing a microservice *on its own*.

**Need-to-know foundational concept**

Microservices testing is layered:

- Unit tests → validate single service logic in isolation
- Integration tests → verify service-to-service communication
- End-to-end tests → validate full workflows
- Load tests → measure performance and resilience

Professional Cloud Architect exam tip:
When a question says *independent verification*, the answer is almost always **unit testing**.

###### Explanation

**Correct option: A — Run unit testing**

Unit testing verifies that **each microservice behaves correctly in isolation**, without depending on other services. In a microservices architecture, this is the primary technique used to validate the internal logic of a service independently. It matches the requirement in the question: *“verify that each microservice works correctly on its own.”*

> [!note]- Why the other options are wrong
> B. Load testing
> Load testing measures **performance and scalability**, not correctness of an individual service’s logic. It answers “how does it behave under stress?” rather than “does it work correctly by itself?”
>
> C. End-to-end testing
> End-to-end tests validate the **entire system workflow** across multiple services. They depend on many components and do not isolate a single microservice.
>
> D. Integration testing
> Integration testing verifies how services **interact with each other**. It is important, but it does not test independence. The question explicitly asks for testing a microservice *on its own*.

</details>

---

### Exam 5 · Q30

**KnightMotives Automotive Case Study**

**Company Overview**

KnightMotives is a car manufacturer specializing in autonomous, self-driving vehicles, including Battery Electric Vehicles (BEVs), hybrids, and traditional internal combustion engine (ICE) vehicles. While KnightMotives has made strides with the in-vehicle experience in their BEV fleet, the hybrid and ICE vehicles have yet to implement these new systems and are viewed poorly by critics and drivers. The lack of modern in-vehicle technology in hybrid and ICE vehicles has resulted in declining sales and customer satisfaction.

KnightMotives wants to modernize the consumer experience across all vehicles within five years. Artificial Intelligence offers a unique opportunity to revolutionize the in-vehicle experience, as well as the shopping, buying, and service/maintenance experience. Investment in this new technology will require a shift in financial priorities on a global scale.

KnightMotives also wants to improve their online ordering system, which is unreliable. Systems for customers to build their vehicle online for acquisition through a dealer are not delivering the data or reliability that dealers need, causing a strain in the relationship between KnightMotives and dealers. Service technicians and sales staff need better tooling to enhance dealer successes, including built-to-order vehicles.

**Solution Concept**

KnightMotives wants to shift from manufacturing cars to creating a complete and compelling "automotive experience." Their strategy prioritizes delivering a consistent experience across all models, developing AI-powered features, generating new revenue from data monetization, adopting a digital focus to differentiate their brand from competitors, and developing better tools for mechanics and salespeople.

**Existing Technical Environment**

KnightMotives's IT is largely on-premises with some applications on major cloud platforms. Their supply chain runs on an outdated mainframe, and Enterprise Resource Planning (ERP) is also outdated, making new promotions and dealer discounts difficult to implement. Dealers have no budget for new equipment. There is fragmentation across vehicles with multiple code bases, and significant technical debt from supporting backwards compatibility. Network connectivity to manufacturing plants and vehicle connectivity in rural areas are challenges.

**Business Requirements**

Key business requirements include fostering a personalized relationship with the driver and delivering a cohesive experience across all models. Creating a better build-to-order model will reduce time on the lot and provide transparency for both dealers and customers. Additionally, KnightMotives seeks to monetize corporate data to finance new technology investments, as their current AI infrastructure is obsolete and corporate data remains siloed. Security is a paramount concern due to past data breaches. Adherence to European Union (EU) data protection regulations, especially for emerging autonomous platforms, is critical.

KnightMotives plans to make significant investments in fully autonomous driving capabilities, with initial implementation targeting regions with favorable regulatory environments. Prioritizing employee upskilling, attracting top-tier talent, and fostering better communication between business and technical teams are also critical objectives.

**Technical Requirements**

- Modernizing the in-vehicle experience includes developing a consistent user experience (UX) that seamlessly integrates AI-powered features across all models, updating in-vehicle hardware and software in legacy models to support new UX features and AI capabilities, and ensuring reliable network connectivity, especially in rural areas, to support real-time AI features and data transmission.
- Network upgrades are necessary to support increased data traffic and improve connectivity between plants and headquarters.
- IT infrastructure modernization requires adopting a hybrid cloud strategy to leverage the benefits of both on-premises and cloud infrastructure, and gradually modernizing or replacing legacy systems to improve efficiency and agility. KnightMotives Automotive Case Study 2
- Autonomous vehicle development and testing requires investing in cutting-edge AI and machine learning technologies, building a robust simulation environment, and ensuring compliance with evolving regulations related to autonomous vehicles.
- Data monetization and insights requires implementing a robust data management platform, strict data security and privacy measures, and a scalable AI/ML infrastructure.
- Increased focus on security and risk management involves implementing a comprehensive security framework to protect against cyber threats and data breaches, developing an incident response plan, and providing security awareness training to employees.
- Providing a delightful experience for dealers and customers requires improving the online build-to-order system; developing modern dealer tools to streamline dealer operations, including sales, service, and inventory management; and implementing a comprehensive Customer Relationship Management (CRM) system to track customer interactions, personalize experiences, and improve customer satisfaction.

**Executive Statement**

KnightMotives is committed to enhancing safety and saving lives by leveraging an extensive body of data—encompassing driving, road conditions, behavioral studies, and crash safety statistics—to create compelling digital experiences for drivers. Our AI consistently outperforms national safety statistics, ensuring the unique and coveted KnightMotives experience is aligned across all our vehicle models.

Michael Knight, KnightMotives CEO

---

**For this question, refer to the KnightMotives Automotive case study. KnightMotives leadership wants to upskill engineering teams by letting each team experiment with one specific technology at a time in a Google Cloud sandbox. They also want guardrails to ensure these experimental efforts cannot evolve into production workloads or create shadow IT. You need to design a solution that supports these training goals and aligns with Google-recommended practices. What should you do?**

- A. Provide a request process for teams to obtain a sandbox for a specific technology. Automate creation of a project with only the required APIs enabled, reduce default API quotas, grant only the scoped IAM roles needed for that technology, and automatically delete the project after a defined period.
- B. Provide a request process for sandbox access and automate creation of a project where the requesting engineer receives full permissions. In the request details, emphasize expectations to limit scope to the requested services and keep costs under control.
- C. Create a dedicated billing account for sandbox projects and grant all engineers the Billing Account User role on it. In the main organization, create a “Sandboxes” folder and grant all engineers the Project Creator role on that folder.
- D. Create a separate Google Cloud organization for R&D, isolated from the production organization. Under that organization, create a folder per team and a project per team member, grant each member full access to their project, grant team managers Security Admin on the team folder, and have teams enable the needed APIs per project.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Provide a request process for teams to obtain a sandbox for a specific technology. Automate creation of a project with only the required APIs enabled, reduce default API quotas, grant only the scoped IAM roles needed for that technology, and automatically delete the project after a defined period.

**Correct answer: A**

**Provide a request process for teams to obtain a sandbox for a specific technology. Automate creation of a project with only the required APIs enabled, reduce default API quotas, grant only the scoped IAM roles needed for that technology, and automatically delete the project after a defined period.**

**Why option A is correct**

KnightMotives wants **learning sandboxes** with:

- strict guardrails
- limited blast radius
- no accidental production use
- no shadow IT
- aligned with Google best practices

Option A matches Google’s recommended **sandbox project architecture**:

- one temporary project per experiment
- minimal IAM (least privilege)
- scoped API enablement
- quota restrictions to control cost
- automated lifecycle cleanup
- centralized governance

This design encourages experimentation while ensuring sandboxes cannot quietly evolve into production environments.

This is exactly how Google recommends organizations implement controlled R&D environments.

**Why the other options are not the best choice**

**B. Full permissions with policy expectations**

Relying on human discipline is not governance. Engineers with full permissions can deploy anything, escalate scope, or accidentally build production systems. This creates shadow IT risk.

The exam strongly prefers **enforced guardrails**, not policy documents.

**C. Shared billing account + Project Creator access**

This gives engineers the power to create unlimited projects with no API/IAM restrictions. It removes central control and makes cost and security unpredictable.

This is the opposite of a controlled sandbox strategy.

**D. Separate organization for R&D**

Running a second org creates heavy operational overhead:

- duplicate IAM hierarchy
- duplicate billing governance
- duplicate security posture
- cross-org policy fragmentation

Google recommends sandbox isolation **within** the same organization using projects and folders — not separate orgs — unless you are isolating legal entities.

**Need-to-know foundational concept**

Google Cloud governance hierarchy:

Organization → Folder → Project → Resources

Sandbox best practice:

- isolate experimentation at the **project** level
- enforce least privilege IAM
- restrict APIs
- apply quotas
- automate cleanup
- keep everything inside the same org for centralized control

This pattern balances innovation and governance — a key theme of enterprise cloud architecture exams.

###### Explanation

**Correct answer: A**

Provide a request process for teams to obtain a sandbox for a specific technology. Automate creation of a project with only the required APIs enabled, reduce default API quotas, grant only the scoped IAM roles needed for that technology, and automatically delete the project after a defined period.

**Why option A is correct**

KnightMotives wants **learning sandboxes** with:

- strict guardrails
- limited blast radius
- no accidental production use
- no shadow IT
- aligned with Google best practices

Option A matches Google’s recommended **sandbox project architecture**:

- one temporary project per experiment
- minimal IAM (least privilege)
- scoped API enablement
- quota restrictions to control cost
- automated lifecycle cleanup
- centralized governance

This design encourages experimentation while ensuring sandboxes cannot quietly evolve into production environments.

This is exactly how Google recommends organizations implement controlled R&D environments.

> [!note]- Why the other options are wrong
> **B. Full permissions with policy expectations**
>
> Relying on human discipline is not governance. Engineers with full permissions can deploy anything, escalate scope, or accidentally build production systems. This creates shadow IT risk.
>
> The exam strongly prefers **enforced guardrails**, not policy documents.
>
> **C. Shared billing account + Project Creator access**
>
> This gives engineers the power to create unlimited projects with no API/IAM restrictions. It removes central control and makes cost and security unpredictable.
>
> This is the opposite of a controlled sandbox strategy.
>
> **D. Separate organization for R&D**
>
> Running a second org creates heavy operational overhead:
>
> - duplicate IAM hierarchy
> - duplicate billing governance
> - duplicate security posture
> - cross-org policy fragmentation

</details>

---

### Exam 5 · Q33

**Your product team is developing a critical, customer-facing application on Google Cloud. The engineering team wants to use **Cloud Spanner** to benefit from its horizontal scalability and reduced operational management. However, the **FinOps** team is worried about Spanner’s monthly cost and recommends running a **self-managed PostgreSQL** database on **Compute Engine VMs** instead. You need to address this disagreement and move the project forward with a database decision that is technically sound while also considering budget constraints. What should you do?**

- A. Share a reference design for running a highly available PostgreSQL cluster using a regional managed instance group (MIG).
- B. Recommend **Cloud SQL for PostgreSQL** as a middle-ground option that provides a managed database at a lower cost than Spanner.
- C. Create a **total cost of ownership (TCO)** analysis that includes operational effort, and review it in a workshop to drive a decision.
- D. Refer to the reliability and performance optimization pillars of the Google Cloud Well-Architected Framework to formally justify choosing Spanner.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a **total cost of ownership (TCO)** analysis that includes operational effort, and review it in a workshop to drive a decision.

Correct Answer: **C**

**Create a total cost of ownership (TCO) analysis that includes operational effort, and review it in a workshop to drive a decision.**

Why C is correct

This is the best way to resolve a **FinOps vs Engineering** disagreement while making a decision that is:

- **Technically sound**
- **Financially defensible**
- **Aligned with real-world delivery constraints**
- **Objective and measurable**

A proper **TCO analysis** goes beyond “monthly database cost” and includes:

- Infrastructure + licensing (if any)
- Backup/restore strategy cost
- High availability + failover architecture cost
- Operational effort (DBA + SRE time)
- Patch management + upgrades
- Monitoring + incident response overhead
- Downtime risk and business impact
- Scalability needs over time (growth curve)

Running a workshop with stakeholders ensures alignment and a decision backed by shared assumptions.

This is exactly how an architect should move the project forward.

**Why the other options are incorrect / not best fit**

A. Share a reference design for HA PostgreSQL using a regional MIG

Not best because:

- It pushes a **self-managed** approach without proving it’s cheaper *in practice*
- HA PostgreSQL on VMs adds major operational complexity (replication, failover, backups, patching)
- Doesn’t solve the root disagreement (cost vs operational value)

B. Recommend Cloud SQL for PostgreSQL as a middle-ground option

Not best because:

- It’s a **solution suggestion without analysis**
- The workload may genuinely require Spanner (global scale, strong consistency, high write throughput)
- FinOps still needs cost justification, and engineering still needs scalability justification

Cloud SQL might be right, but you must validate with requirements and cost modeling first.

D. Use Well-Architected Framework pillars to justify Spanner

Not best because:

- It supports the engineering preference but doesn’t address the **budget concern with numbers**
- FinOps will not accept “framework justification” without cost impact and tradeoff analysis
- Well-Architected is guidance, not a financial decision tool

Need-to-know fundamentals (important for architect mindset)

- **Spanner cost** is often higher, but it can reduce:
  - operational burden
  - downtime risk
  - scaling complexity
- **Self-managed PostgreSQL on Compute Engine** can look cheaper on paper but typically increases:
  - staffing effort
  - operational risk
  - incident handling cost
- A good architect makes decisions using **requirements + measurable tradeoffs**, not preferences.

Official documentation link

Google Cloud Architecture Framework (Well-Architected guidance for tradeoffs):
[https://cloud.google.com/architecture/framework](https://cloud.google.com/architecture/framework)

###### Explanation

Why C is correct

This is the best way to resolve a **FinOps vs Engineering** disagreement while making a decision that is:

- **Technically sound**
- **Financially defensible**
- **Aligned with real-world delivery constraints**
- **Objective and measurable**

A proper **TCO analysis** goes beyond “monthly database cost” and includes:

- Infrastructure + licensing (if any)
- Backup/restore strategy cost
- High availability + failover architecture cost
- Operational effort (DBA + SRE time)
- Patch management + upgrades
- Monitoring + incident response overhead
- Downtime risk and business impact
- Scalability needs over time (growth curve)

Running a workshop with stakeholders ensures alignment and a decision backed by shared assumptions.

This is exactly how an architect should move the project forward.

> [!note]- Why the other options are wrong
> A. Share a reference design for HA PostgreSQL using a regional MIG
>
> Not best because:
>
> - It pushes a **self-managed** approach without proving it’s cheaper *in practice*
> - HA PostgreSQL on VMs adds major operational complexity (replication, failover, backups, patching)
> - Doesn’t solve the root disagreement (cost vs operational value)
>
> B. Recommend Cloud SQL for PostgreSQL as a middle-ground option
>
> Not best because:
>
> - It’s a **solution suggestion without analysis**
> - The workload may genuinely require Spanner (global scale, strong consistency, high write throughput)
> - FinOps still needs cost justification, and engineering still needs scalability justification
>
> Cloud SQL might be right, but you must validate with requirements and cost modeling first.
>
> D. Use Well-Architected Framework pillars to justify Spanner
>
> Not best because:
>
> - It supports the engineering preference but doesn’t address the **budget concern with numbers**
> - FinOps will not accept “framework justification” without cost impact and tradeoff analysis
> - Well-Architected is guidance, not a financial decision tool

</details>

---

### Exam 5 · Q46

**You are building a migration plan to move your organization’s infrastructure from on-premises to Google Cloud. After the migration, you want to be able to track, understand, and control cloud costs effectively. Which two strategies should you include in the migration plan? (Choose two.)**

- A. Enable **Backup and DR Service**.
- B. Apply consistent **labels and tags** to all Google Cloud resources you provision.
- C. Schedule a recurring export of billing data to **Cloud SQL** using **Cloud Scheduler**.
- D. Create **service alerts** using **Cloud Monitoring**.
- E. Use **infrastructure as code (IaC)** to manage and provision cloud resources.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Apply consistent **labels and tags** to all Google Cloud resources you provision. **|** E. Use **infrastructure as code (IaC)** to manage and provision cloud resources.

**Correct Answers: B and E**

**B. Apply consistent labels and tags to all Google Cloud resources you provision.**
**E. Use infrastructure as code (IaC) to manage and provision cloud resources.**

Why **B** is correct (cost tracking + allocation)

Consistent **labels and tags** enable accurate **cost attribution** across teams, environments, apps, and business units (for example: `env=prod`, `bu=claims`, `app=inventory`). This is foundational for:

- chargeback / showback
- budget ownership by team
- cost reporting and filtering

**Official documentation:**
[https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing)

**Why E is correct (cost control + governance)**

Using **Infrastructure as Code (IaC)** (Terraform, Config Connector, etc.) improves cost governance by ensuring:

- repeatable, standardized provisioning (avoids “shadow resources”)
- review/approval workflows before spending changes
- consistent enforcement of cost controls (like mandatory labels, allowed machine types, etc.)
- easier cleanup and lifecycle management

**Official documentation:**
[https://cloud.google.com/docs/terraform](https://cloud.google.com/docs/terraform)

**Why the other options are incorrect / not best fit**

**A. Enable Backup and DR Service**

Important for resilience, but it does not directly help with **tracking and controlling costs**.

**C. Export billing data to Cloud SQL using Cloud Scheduler**

Not a standard or recommended pattern. The typical export destinations are **BigQuery** (for analysis) and **Cloud Storage** (for archival).

**D. Create service alerts using Cloud Monitoring**

Useful for availability and SLOs, but not the primary method for cloud cost tracking and control. For cost controls, you use budgets, billing exports, and resource governance.

###### Explanation

Why **B** is correct (cost tracking + allocation)

Consistent **labels and tags** enable accurate **cost attribution** across teams, environments, apps, and business units (for example: `env=prod`, `bu=claims`, `app=inventory`). This is foundational for:

- chargeback / showback
- budget ownership by team
- cost reporting and filtering

**Why E is correct (cost control + governance)**

Using **Infrastructure as Code (IaC)** (Terraform, Config Connector, etc.) improves cost governance by ensuring:

- repeatable, standardized provisioning (avoids “shadow resources”)
- review/approval workflows before spending changes
- consistent enforcement of cost controls (like mandatory labels, allowed machine types, etc.)
- easier cleanup and lifecycle management

> [!note]- Why the other options are wrong
> A. Enable Backup and DR Service
>
> Important for resilience, but it does not directly help with **tracking and controlling costs**.
>
> C. Export billing data to Cloud SQL using Cloud Scheduler
>
> Not a standard or recommended pattern. The typical export destinations are **BigQuery** (for analysis) and **Cloud Storage** (for archival).
>
> D. Create service alerts using Cloud Monitoring
>
> Useful for availability and SLOs, but not the primary method for cloud cost tracking and control. For cost controls, you use budgets, billing exports, and resource governance.

</details>

---

### Exam 5 · Q57

**Your company wants to reduce Google Cloud spending for its development and staging environments. These environments are developer workstations used only Monday through Friday from 9:00 AM to 6:00 PM local time. They currently run on a fleet of n1-standard-4 Compute Engine instances that stay powered on 24/7, resulting in high monthly costs even though the systems sit idle more than 70% of the time. You need a solution that cuts costs significantly without affecting developer productivity during working hours. What should you do?**

- A. Configure a schedule to automatically start and stop the virtual machines according to the team’s working hours.
- B. Purchase three-year committed use discounts for the current n1-standard-4 instances.
- C. Upgrade all instances to the N2 machine series.
- D. Redesign the environments to run in a regional managed instance group with autoscaling enabled.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure a schedule to automatically start and stop the virtual machines according to the team’s working hours.

**Correct option:** **A. Configure a schedule to automatically start and stop the virtual machines according to the team’s working hours.**

**Need-to-know foundational concept**

Compute Engine pricing is primarily **usage-based**. You pay for VM uptime, not ownership. If a VM is stopped, you stop paying for CPU and memory charges. For non-production workloads like dev and staging, the biggest cost optimization is often **eliminating idle runtime**, not resizing or discounting always-on capacity.

Google explicitly recommends scheduling start/stop for development environments that do not need to run continuously. This aligns with FinOps best practices: shut down unused resources instead of optimizing resources that shouldn’t be running at all.
[https://cloud.google.com/compute/docs/instances/schedule-instance-start-stop](https://cloud.google.com/compute/docs/instances/schedule-instance-start-stop)

**Why the correct option fits the scenario**

The environments are only needed during business hours:

- Monday–Friday, 9 AM–6 PM
- Idle more than 70% of the time

Automatically stopping VMs outside working hours removes most compute charges while preserving the same environment during active hours. Developers experience zero productivity loss because machines are available when needed and simply powered off when idle.

This delivers **immediate, predictable cost savings** without redesigning architecture.

**Why the other options are not the best choice**

**B. Purchase three-year committed use discounts**
Committed use discounts lower per-hour pricing but require **continuous usage commitment**. This locks the company into paying for capacity even when VMs are idle, which contradicts the goal of reducing waste.

**C. Upgrade to N2 machine series**
N2 may offer better price-performance, but the instances would still run 24/7. You’d optimize efficiency while keeping the largest cost driver — idle runtime — unchanged.

**D. Regional MIG with autoscaling**
Autoscaling is designed for variable traffic workloads, not developer workstations that require persistent sessions. Autoscaling may scale down instances and interrupt active work, harming productivity. It also doesn’t guarantee shutdown outside work hours unless paired with scheduling logic.

Scheduling start/stop directly targets the root cause: paying for idle compute time. It is the simplest, safest, and highest-impact optimization for dev/staging workloads.

###### Explanation

**Correct option:** **A.**

**Why the correct option fits the scenario**

The environments are only needed during business hours:

- Monday–Friday, 9 AM–6 PM
- Idle more than 70% of the time

Automatically stopping VMs outside working hours removes most compute charges while preserving the same environment during active hours. Developers experience zero productivity loss because machines are available when needed and simply powered off when idle.

This delivers **immediate, predictable cost savings** without redesigning architecture.

> [!note]- Why the other options are wrong
> **B. Purchase three-year committed use discounts**
> Committed use discounts lower per-hour pricing but require **continuous usage commitment**. This locks the company into paying for capacity even when VMs are idle, which contradicts the goal of reducing waste.
>
> **C. Upgrade to N2 machine series**
> N2 may offer better price-performance, but the instances would still run 24/7. You’d optimize efficiency while keeping the largest cost driver — idle runtime — unchanged.
>
> **D. Regional MIG with autoscaling**
> Autoscaling is designed for variable traffic workloads, not developer workstations that require persistent sessions. Autoscaling may scale down instances and interrupt active work, harming productivity. It also doesn’t guarantee shutdown outside work hours unless paired with scheduling logic.

</details>

---

### Exam 5 · Q69

**You use a GitHub repository to manage your application’s source code and want to implement a secure, efficient continuous deployment pipeline. The goal is to automatically build and deploy the application to Cloud Run whenever a pull request is merged. What should you do?**

- A. Configure a GitHub webhook trigger in Cloud Build. When a pull request is merged, have Cloud Build build a container image and store it in Artifact Registry, then use Config Sync to deploy the application to Cloud Run.
- B. Create a GitHub Actions workflow that builds and deploys the application to Cloud Run after a pull request is merged, using a service account key committed to the repository for deployment access.
- C. Set up a GitHub Enterprise trigger in Cloud Build. When a pull request is merged, trigger Cloud Build to build and deploy the application to Cloud Run, and store the deployment credentials in Secret Manager.
- D. Connect the repository using the Cloud Build GitHub app and create a Cloud Build trigger that builds and deploys the application to Cloud Run when a pull request is merged.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Connect the repository using the Cloud Build GitHub app and create a Cloud Build trigger that builds and deploys the application to Cloud Run when a pull request is merged.

**Correct option: D. Connect the repository using the Cloud Build GitHub app and create a Cloud Build trigger that builds and deploys the application to Cloud Run when a pull request is merged.**

**Need-to-know foundational concept**

Google best practice for CI/CD from GitHub to Google Cloud is:

Use **Cloud Build native GitHub integration** with triggers and avoid long-lived credentials.

Cloud Build provides a first-class GitHub App integration that:

- securely connects the repo without storing keys in code
- uses short-lived, managed credentials
- automatically triggers builds on repo events
- integrates directly with Cloud Run deployment

This follows Google’s security guidance to avoid service account keys and prefer managed identity flows.

**Official reference (Cloud Build GitHub integration & triggers):**
[https://cloud.google.com/build/docs/automating-builds/github/build-repos-from-github](https://cloud.google.com/build/docs/automating-builds/github/build-repos-from-github)

**Why the correct option fits the scenario**

Option D gives you:

- automatic trigger when PR is merged
- secure GitHub → Cloud Build integration
- no embedded credentials
- native deployment pipeline
- minimal operational overhead
- Google-recommended CI/CD path

This is the canonical GitHub → Cloud Build → Cloud Run pipeline.

**Why the other options are not the best choice**

**A. Webhook + Config Sync**
Config Sync is for Kubernetes config management, not Cloud Run deployment. It introduces unnecessary complexity.

**B. GitHub Actions + service account key in repo**
This violates Google security best practices. Service account keys in repositories are a major credential risk.

**C. GitHub Enterprise trigger + Secret Manager**
GitHub Enterprise is unnecessary unless you actually run GitHub Enterprise Server. The question says GitHub, not GitHub Enterprise. This adds complexity without benefit.

The exam principle being tested:

Prefer managed integrations and eliminate long-lived credentials.

Cloud Build’s GitHub App trigger is the secure, low-ops, recommended deployment pattern.

**Final answer: D**

###### Explanation

**Why the correct option fits the scenario**

**Option D gives you:**

- automatic trigger when PR is merged
- secure GitHub → Cloud Build integration
- no embedded credentials
- native deployment pipeline
- minimal operational overhead
- Google-recommended CI/CD path

This is the canonical GitHub → Cloud Build → Cloud Run pipeline.

> [!note]- Why the other options are wrong
> **A. Webhook + Config Sync**
> Config Sync is for Kubernetes config management, not Cloud Run deployment. It introduces unnecessary complexity.
>
> **B. GitHub Actions + service account key in repo**
> This violates Google security best practices. Service account keys in repositories are a major credential risk.
>
> **C. GitHub Enterprise trigger + Secret Manager**
> GitHub Enterprise is unnecessary unless you actually run GitHub Enterprise Server. The question says GitHub, not GitHub Enterprise. This adds complexity without benefit.

</details>

---

### Exam 5 · Q73

**You need to design a continuous delivery pipeline for a containerized application on Google Cloud. The goal is to run all tests within the pipeline to improve software quality before releasing to production. What should you do?**

- A. When developers push code to a central repository, trigger Cloud Build to run unit tests. If they pass, build the container and push it to a registry. Use Cloud Build to deploy the container to a test environment and run integration and acceptance tests. If all tests succeed, deploy to production and run smoke tests.
- B. After code is pushed, trigger Cloud Build to build the container first, then run unit tests. If unit tests pass, deploy to a test environment and run integration tests. If integration tests pass, deploy to production and run acceptance tests.
- C. Automatically run unit tests locally when code changes. If they pass, build a container. Use Cloud Build to deploy to a test environment and run integration and acceptance tests. If all tests succeed, mark the code as production-ready and trigger Cloud Build to deploy to production.
- D. Require developers to run unit tests locally before committing code. After pushing code, use Cloud Build to build and deploy to a test environment and run integration tests. If integration tests pass, deploy to production and run acceptance tests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. When developers push code to a central repository, trigger Cloud Build to run unit tests. If they pass, build the container and push it to a registry. Use Cloud Build to deploy the container to a test environment and run integration and acceptance tests. If all tests succeed, deploy to production and run smoke tests.

**Correct option: A**

**Need-to-know foundational concept**

A proper continuous delivery pipeline should enforce **progressive testing gates** inside the pipeline, not on developer machines. The key principle is:

Tests must be automated, repeatable, and executed in CI before production release.

Google’s recommended CI/CD model is to use Cloud Build to orchestrate build + test + deploy stages in sequence, ensuring artifacts are validated before promotion. Unit tests validate code correctness early, integration/acceptance tests validate system behavior in staging, and smoke tests validate production deployment.

**Cloud Build is designed to run automated build/test pipelines triggered by repository changes:**
[https://cloud.google.com/build/docs/overview](https://cloud.google.com/build/docs/overview)

**Why option A is correct**

Option A implements the proper testing pyramid and pipeline order:

1. **Unit tests first** → fast feedback, cheapest failures
2. Build artifact only after unit tests pass
3. Deploy to test environment
4. Run integration + acceptance tests
5. Deploy to production
6. Run smoke tests

All tests run **inside the pipeline**, not locally. This guarantees consistency, auditability, and quality gates before production.

This is a textbook continuous delivery workflow.

**Why the other options are not the best choice**

**B. Build container before unit tests**
You waste resources building artifacts that might fail basic tests. Tests should gate builds.

**C. Unit tests run locally**
Local tests are not enforced and cannot be trusted as a quality gate. CI must own testing.

**D. Developers required to run tests locally**
This is governance by policy, not automation. It’s not enforceable and breaks CD best practices.

Exam principle:

CI/CD pipelines must enforce automated testing stages before artifact promotion.

**Final answer: A**

###### Explanation

**Correct option: A**

**Need-to-know foundational concept**

A proper continuous delivery pipeline should enforce **progressive testing gates** inside the pipeline, not on developer machines. The key principle is:

Tests must be automated, repeatable, and executed in CI before production release.

Google’s recommended CI/CD model is to use Cloud Build to orchestrate build + test + deploy stages in sequence, ensuring artifacts are validated before promotion. Unit tests validate code correctness early, integration/acceptance tests validate system behavior in staging, and smoke tests validate production deployment.

Cloud Build is designed to run automated build/test pipelines triggered by repository changes:
[https://cloud.google.com/build/docs/overview](https://cloud.google.com/build/docs/overview)

**Why option A is correct**

Option A implements the proper testing pyramid and pipeline order:

1. **Unit tests first** → fast feedback, cheapest failures
2. Build artifact only after unit tests pass
3. Deploy to test environment
4. Run integration + acceptance tests
5. Deploy to production
6. Run smoke tests

> [!note]- Why the other options are wrong
> **B. Build container before unit tests**
> You waste resources building artifacts that might fail basic tests. Tests should gate builds.
>
> **C. Unit tests run locally**
> Local tests are not enforced and cannot be trusted as a quality gate. CI must own testing.
>
> **D. Developers required to run tests locally**
> This is governance by policy, not automation. It’s not enforceable and breaks CD best practices.

</details>

---
