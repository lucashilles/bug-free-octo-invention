# Domain 6 — Ensuring Solution and Operations Excellence

36 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q12

**A customer is receiving reports that their recently updated Google App Engine application is taking approximately 30 seconds to load for some users. This issue was not observed before the update. What approach should they take?**

- A. Collaborate with their ISP to diagnose the issue.
- B. Open a support ticket to request network capture and flow data for troubleshooting, then roll back the application.
- C. Initially roll back to a previously stable release, then use Stackdriver Trace and Logging to investigate the issue in a development, test, or staging environment.
- D. Roll back to a previously stable release, redeploy the update during a lower-traffic period, and then use Stackdriver Trace and Logging to diagnose the issue.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Initially roll back to a previously stable release, then use Stackdriver Trace and Logging to investigate the issue in a development, test, or staging environment.

**Correct Answer:**

**C. Initially roll back to a previously stable release, then use Stackdriver Trace and Logging to investigate the issue in a development, test, or staging environment.**

**Explanation:**

Since the **performance issue started after the update**, the best approach is to:

1. **Roll back to a previously stable release** to restore normal functionality for users.
2. **Use Google Cloud’s monitoring tools (Stackdriver Trace and Logging)** to investigate the root cause of the latency issue.
3. **Conduct debugging in a non-production environment** (development, test, or staging) to prevent further impact on users.

✅ **Why this is the best approach?**

- **Minimizes user impact** by quickly restoring a stable version.
- **Provides detailed latency analysis** using **Stackdriver Trace**.
- **Enables log-based debugging** to identify the problematic changes.
- **Prevents unnecessary redeployment** in production until the issue is resolved.

✅ **Supporting Documentation:**

- **Google Cloud Trace for latency analysis:**
  **https://cloud.google.com/trace/docs**
- **Logging for App Engine troubleshooting:**
  **https://cloud.google.com/appengine/docs/standard/python/logs**

**Why Other Options Are Incorrect:**

**A. Collaborate with their ISP to diagnose the issue.** ❌

- **Incorrect** because the **issue started after the update**, making it highly unlikely that an ISP-related issue is the cause.
- The **problem is likely in the application or backend**, not the network.

✅ **Reference:**

- **https://cloud.google.com/network-intelligence-center/docs/**

**B. Open a support ticket to request network capture and flow data for troubleshooting, then roll back the application.** ❌

- **Not the best approach initially** because:
  - The **issue is more likely in the application code or deployment configuration**, not at the network level.
  - **Rolling back is correct**, but **network capture is unnecessary** at this stage.
  - Google Cloud’s **Stackdriver Trace and Logging** are better tools to diagnose App Engine application latency.

✅ **Reference:**

- **https://cloud.google.com/trace/docs/overview**

**D. Roll back to a previously stable release, redeploy the update during a lower-traffic period, and then use Stackdriver Trace and Logging to diagnose the issue.** ❌

- **Partially correct**, but **redeploying the update before debugging is risky**.
- The issue should first be **investigated in a development/test environment** rather than redeploying directly in production.
- **Rolling back and diagnosing in a non-production environment is the best practice.**

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/troubleshooting**

**Conclusion:**

The best approach is **C. Roll back to a stable release, then use Stackdriver Trace and Logging to investigate the issue in a test environment**.

- **Minimizes downtime** and **prevents further user impact**.
- **Uses Google Cloud’s built-in debugging tools** for efficient root cause analysis.
- **Ensures that the next update is stable before re-deploying to production.**

📌 **Final Reference:**
**https://cloud.google.com/trace/docs**

</details>

---

### Exam 1 · Q22

**A **small percentage of API requests** in your **microservices-based application** are experiencing **high latency**. Each request may pass through multiple services, and you need to identify which service is causing the delay. What should you do?**

- A. Configure timeouts in your application to fail slow requests more quickly.
- B. Send **custom metrics** for each request to **Stackdriver Monitoring**.
- C. Use **Stackdriver Monitoring** to analyze insights when API latency is high.
- D. **Instrument your application with Stackdriver Trace** to break down request latencies across microservices.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Instrument your application with Stackdriver Trace** to break down request latencies across microservices.

**Correct Answer:**

**D. Instrument your application with Stackdriver Trace to break down request latencies across microservices.**

**Explanation:**

In a **microservices-based application**, where **each request may pass through multiple services**, **latency issues can originate from different components**.

✅ **Google Cloud’s Stackdriver Trace (Cloud Trace) is the best solution because:**

- It **tracks request flows across microservices**, helping **pinpoint the exact service** causing the delay.
- It provides **detailed latency breakdowns** for each API request.
- It helps **identify performance bottlenecks** in dependencies like **databases, caches, or external services**.
- **Automatically integrates with GKE, Compute Engine, App Engine, and Cloud Run.**

**How It Works:**

1. **Instrument your services** with **Stackdriver Trace SDKs** (or use built-in integration for Google Cloud services).
2. Each request generates a **trace ID** that follows the request **across all microservices**.
3. Use **Stackdriver Trace UI** to analyze end-to-end request latency and identify **slow services or operations**.

✅ **Supporting Documentation:**

- **Google Cloud Trace Overview:**
  **https://cloud.google.com/trace/docs/**
- **Distributed Tracing for Microservices:**
  **https://cloud.google.com/blog/topics/developers-practitioners/distributed-tracing-microservices-google-cloud**

**Why Other Options Are Incorrect:**

**A. Configure timeouts in your application to fail slow requests more quickly.** ❌

- **Timeouts help mitigate latency issues** but do **not diagnose the root cause** of high-latency services.
- Without identifying **which service is slow**, adding timeouts can **lead to unnecessary failures and degraded user experience**.

✅ **Reference:**

- **https://cloud.google.com/architecture/microservices-timeouts-retries**

**B. Send custom metrics for each request to Stackdriver Monitoring.** ❌

- **Metrics provide aggregated latency data**, but they **do not show per-request breakdowns across microservices**.
- Stackdriver Monitoring **does not provide trace-level visibility** like Stackdriver Trace.

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs/**

**C. Use Stackdriver Monitoring to analyze insights when API latency is high.** ❌

- **Stackdriver Monitoring detects latency spikes but does not trace requests across microservices.**
- **Stackdriver Trace is required** for **end-to-end request latency analysis**.

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs/overview**

**Conclusion:**

The best approach is **D. Instrument your application with Stackdriver Trace** to analyze **end-to-end request latency** across microservices.

- **Pinpoints slow microservices.**
- **Provides real-time tracing insights.**
- **Helps optimize API performance.**

📌 **Final Reference:**
**https://cloud.google.com/trace/docs/**

</details>

---

### Exam 1 · Q32

**Your development team has installed a new Linux kernel module on the batch servers running on Google Compute Engine (GCE) virtual machines (VMs) to improve the nightly batch process. However, two days after the installation, 50% of the batch servers failed during the nightly batch run. You need to collect detailed failure information to share with the development team.**

**Which three actions should you take? (Choose three.)**

- A. Use **Stackdriver Logging** to search for log entries related to the kernel module.
- B. Retrieve the **GCE Activity log** using the API or Cloud Console for debugging.
- C. Use **gcloud** or the **Cloud Console** to connect to the **serial console** and inspect the logs.
- D. Check the **activity log** to determine whether a **live migration event** occurred on the failed servers.
- E. Adjust the **Google Stackdriver** timeline to match the failure time and review batch server **metrics**.
- F. Export a **debug VM image**, run it on a **local server**, and observe kernel log messages on the native screen.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use **Stackdriver Logging** to search for log entries related to the kernel module. **|** C. Use **gcloud** or the **Cloud Console** to connect to the **serial console** and inspect the logs. **|** E. Adjust the **Google Stackdriver** timeline to match the failure time and review batch server **metrics**.

**Correct Answers:**

✅ **A. Use Stackdriver Logging to search for log entries related to the kernel module.**
✅ **C. Use gcloud or the Cloud Console to connect to the serial console and inspect the logs.**
✅ **E. Adjust the Google Stackdriver timeline to match the failure time and review batch server metrics.**

**Explanation:**

To **debug the batch server failures caused by a new Linux kernel module**, you need to gather **logs, metrics, and console output** to analyze system behavior before the failure.

**Why These Three Options Are Correct?**

1️⃣ **A. Use Stackdriver Logging to search for log entries related to the kernel module.** ✅

- **Stackdriver Logging (Cloud Logging)** records **system logs, kernel messages, and application logs**.
- You can search for **kernel-related errors (e.g., `dmesg`, `syslog`, or `journalctl`)** to find failures related to the module.
- **Look for `kernel panic` or `modprobe` failures** that might indicate why the batch jobs failed.

✅ **Supporting Documentation:**

- **https://cloud.google.com/logging/docs/view/advanced-queries**

2️⃣ **C. Use gcloud or the Cloud Console to connect to the serial console and inspect the logs.** ✅

- The **serial console** captures **kernel panics, boot logs, and system errors**, even when SSH is unavailable.
- If the **VM crashed due to the new kernel module**, serial console logs may provide **panic messages and backtraces**.
- **Command to enable and access serial console logs:**
  ```
  bashCopyEditgcloud compute instances get-serial-port-output INSTANCE_NAME
  ```

✅ **Supporting Documentation:**

- **https://cloud.google.com/compute/docs/troubleshooting/using-serial-console**

3️⃣ **E. Adjust the Google Stackdriver timeline to match the failure time and review batch server metrics.** ✅

- **Stackdriver (Cloud Monitoring) provides CPU, memory, disk, and network metrics.**
- Checking **performance trends before failure** might reveal **spikes in resource usage or unusual activity** caused by the kernel module.
- **Look for increased memory usage (OOM errors), CPU load, or system crashes.**

✅ **Supporting Documentation:**

- **https://cloud.google.com/monitoring/docs/viewing-metrics**

**Why Other Options Are Incorrect?**

**B. Retrieve the GCE Activity log using the API or Cloud Console for debugging.** ❌

- **GCE Activity Logs track user and API actions**, such as **instance creations, deletions, and metadata changes**.
- **They do not capture system-level failures or kernel issues.**
- **Cloud Logging (Option A) provides more relevant kernel failure details.**

✅ **Reference:**

- **https://cloud.google.com/logging/docs/audit**

**D. Check the activity log to determine whether a live migration event occurred on the failed servers.** ❌

- **Live migration does not cause kernel failures**—it is a transparent process for VMs.
- **If live migration had caused failures, all servers would be affected, not just 50%.**
- **More relevant checks include system logs (Option A) and serial console output (Option C).**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/live-migration**

**F. Export a debug VM image, run it on a local server, and observe kernel log messages on the native screen.** ❌

- **Unnecessary and impractical for debugging a production failure.**
- **Serial console logs (Option C) provide the same kernel error details without needing local debugging.**
- **Exporting and running a VM locally introduces operational overhead.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/images/export-image**

**Conclusion:**

The best troubleshooting steps are:
✔ **A. Check Stackdriver Logging for kernel-related log entries.**
✔ **C. Use serial console logs to inspect kernel panics and failures.**
✔ **E. Review Stackdriver Monitoring metrics before and during failure.**

📌 **Final References:**

- **Cloud Logging: Advanced Queries**
- **Using Serial Console for Debugging**
- **Viewing Stackdriver Monitoring Metrics**

</details>

---

### Exam 1 · Q34

**You have built a deployment pipeline that pushes source code changes to your infrastructure in instance groups with self-healing capabilities. A recent change has negatively impacted a key performance indicator (KPI), and the root cause is unknown. Investigating the issue could take up to a week.**

**What should you do?**

- A. Log in to a server and manually iterate on the fix locally.
- B. **Revert the source code change** and rerun the deployment pipeline.
- C. Log into the affected servers and manually replace the bad code with the previous version.
- D. **Change the instance group template to the previous version** and delete all instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Revert the source code change** and rerun the deployment pipeline.

**Correct Answer:**

✅ **B. Revert the source code change and rerun the deployment pipeline.**

**Explanation:**

Since the **recent deployment negatively impacted a key performance indicator (KPI)** and the root cause is **unknown**, the best approach is to:

1. **Revert the source code to the previous stable version.**
2. **Rerun the deployment pipeline to automatically push the stable version** back to production.

This ensures:

- **Minimal downtime** while the issue is investigated.
- **Automated rollback using the deployment pipeline**, which is safer and prevents manual errors.
- **Consistent deployment practices**, avoiding ad-hoc fixes on individual servers.

✅ **Supporting Documentation:**

- **Best Practices for Deployment Pipelines:**
  **https://cloud.google.com/architecture/devops/devops-tech-continuous-deployment**

**Why Other Options Are Incorrect?**

**A. Log in to a server and manually iterate on the fix locally.** ❌

- **Manually debugging in production is risky**—changes could introduce more issues.
- **Instance groups have self-healing capabilities**, meaning manual fixes may be lost when instances are recreated.
- **The deployment pipeline should be used for controlled and tested updates.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-groups**

**C. Log into the affected servers and manually replace the bad code with the previous version.** ❌

- **Manual changes to individual servers will be overridden** when the instance group recreates instances.
- **Not scalable**, as instance groups automatically replace unhealthy VMs.
- **Deployment pipelines should manage rollbacks, not manual updates on individual machines.**

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs**

**D. Change the instance group template to the previous version and delete all instances.** ❌

- **Overly disruptive**—deleting instances **can cause downtime**.
- **Changing the template is useful, but the pipeline should handle rollbacks automatically.**
- **Reverting the source code (Option B) is faster and follows DevOps best practices.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-templates**

**Conclusion:**

The best approach is **B. Revert the source code change and rerun the deployment pipeline**, because:

- **It restores a stable version quickly** while allowing investigation.
- **It prevents manual intervention in production.**
- **It aligns with best DevOps practices.**

📌 **Final Reference:**
**https://cloud.google.com/architecture/devops/devops-tech-continuous-deployment**

</details>

---

### Exam 1 · Q43

**Your Compute Engine managed instance group is experiencing an outage, where all instances restart every 5 seconds. A health check is configured, but autoscaling is disabled. Your colleague, who is a Linux expert, has offered to help diagnose the issue.**

**How can you ensure that your colleague can access the VMs to investigate the problem?**

- A. Assign your colleague the **IAM role of Project Viewer**.
- B. Perform a **rolling restart** on the instance group.
- C. **Disable the health check**, then add their SSH key to the **project-wide SSH Keys**.
- D. **Disable autoscaling**, then add their SSH key to the **project-wide SSH Keys**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Disable the health check**, then add their SSH key to the **project-wide SSH Keys**.

**Correct Answer:**

✅ **C. Disable the health check, then add their SSH key to the project-wide SSH Keys.**

**Explanation:**

Since **all instances in the managed instance group (MIG) are restarting every 5 seconds**, it's likely that the **health check is continuously failing**, causing the instances to be **terminated and recreated**.

**Why This Works:**

1. **Disabling the health check** prevents the **instance group from automatically terminating and recreating instances**.
2. **Adding an SSH key at the project-wide level** ensures **your colleague can log in** to the instances for debugging.
3. **Since autoscaling is already disabled**, we don’t need to take action on it.

**Implementation Steps:**

1. **Disable the health check:**
  ```
  gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \    --no-health-check
  ```
2. **Add your colleague’s SSH key to the project-wide metadata:**
  ```
  gcloud compute project-info add-metadata \    --metadata ssh-keys="username:ssh-rsa AAAAB3Nz..."
  ```
3. **Have your colleague SSH into an instance for investigation:**
  ```
  gcloud compute ssh INSTANCE_NAME --zone=ZONE
  ```
4. **Re-enable the health check once the issue is resolved.**

✅ **Supporting Documentation:**

- **Troubleshooting Managed Instance Groups:**
  **https://cloud.google.com/compute/docs/instance-groups/troubleshooting-instance-groups**
- **Adding SSH Keys to Metadata:**
  **https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys**

**Why Other Options Are Incorrect?**

**A. Assign your colleague the IAM role of Project Viewer.** ❌

- **IAM Project Viewer does not grant SSH access.**
- **It only allows read access to resources but does not permit login to instances.**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/understanding-roles**

**B. Perform a rolling restart on the instance group.** ❌

- **Restarting instances does not resolve the root cause** (likely a failing health check).
- **The issue will persist if the health check continues to fail.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups**

**D. Disable autoscaling, then add their SSH key to the project-wide SSH Keys.** ❌

- **Autoscaling is already disabled**, so disabling it **again does not help.**
- **The issue is the health check causing frequent instance terminations, not autoscaling.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/autoscaler**

**Conclusion:**

The best solution is **C. Disable the health check, then add their SSH key to the project-wide SSH Keys**, because:

- **It prevents the instance group from continuously restarting instances.**
- **It allows your colleague to log in and diagnose the issue.**
- **Once the issue is resolved, the health check can be re-enabled.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/instance-groups/troubleshooting-instance-groups**

</details>

---

### Exam 2 · Q3

**Your customer wants to capture multiple gigabytes of real-time key performance indicators (KPIs) from their game servers running on Google Cloud Platform (GCP) and monitor these KPIs with low latency.**

**How should they capture and monitor the KPIs?**

- A. Store **time-series data** from the game servers in **Google Bigtable** and visualize it using **Google Data Studio**.
- B. Output **custom metrics** to **Stackdriver** from the game servers and create a **dashboard in Stackdriver Monitoring Console** to view them.
- C. Schedule **BigQuery load jobs** to ingest **analytics files** uploaded to **Cloud Storage** every **ten minutes**, then visualize the results in **Google Data Studio**.
- D. Insert the **KPIs into Cloud Datastore entities** and perform **ad hoc analysis and visualizations** in **Cloud Datalab**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Output **custom metrics** to **Stackdriver** from the game servers and create a **dashboard in Stackdriver Monitoring Console** to view them.

**Correct Answer:**

✅ **B. Output custom metrics to Stackdriver from the game servers and create a dashboard in Stackdriver Monitoring Console to view them.**

**Explanation:**

Since the **customer needs to capture real-time KPIs with low latency**, **Stackdriver Monitoring (now Cloud Operations Suite)** is the best solution.

✅ **Why Use Cloud Monitoring (Stackdriver) for Real-Time KPIs?**

- **Optimized for real-time monitoring with minimal latency.**
- **Supports custom metrics from game servers.**
- **Provides built-in dashboards and alerting capabilities.**
- **Scales automatically to handle high-volume KPI ingestion.**

**Implementation Steps:**

1. **Instrument game servers to send custom metrics** using Cloud Monitoring API:
  ```
  from google.cloud import monitoring_v3 client = monitoring_v3.MetricServiceClient()project_name = f"projects/{your_project_id}" series = monitoring_v3.TimeSeries()series.metric.type = "custom.googleapis.com/game/kpi_latency"series.resource.type = "global"series.points.append(    monitoring_v3.Point(        interval=monitoring_v3.TimeInterval(            end_time={"seconds": int(time.time())}        ),        value=monitoring_v3.TypedValue(double_value=12.34),    ))client.create_time_series(name=project_name, time_series=[series])
  ```
2. **Use Cloud Monitoring dashboards to visualize KPIs**.
3. **Set alerts** for specific KPI thresholds to notify teams.

✅ **Supporting Documentation:**

- **Cloud Monitoring Custom Metrics:**
  **https://cloud.google.com/monitoring/custom-metrics/**
- **Creating Dashboards in Cloud Monitoring:**
  **https://cloud.google.com/monitoring/dashboards**

**Why Other Options Are Incorrect?**

**A. Store time-series data from the game servers in Google Bigtable and visualize it using Google Data Studio.** ❌

- **Bigtable is excellent for high-throughput storage but not for real-time monitoring.**
- **Visualization in Data Studio introduces additional latency.**

✅ **Reference:**

- **https://cloud.google.com/bigtable/docs/overview**

**C. Schedule BigQuery load jobs to ingest analytics files uploaded to Cloud Storage every ten minutes, then visualize the results in Google Data Studio.** ❌

- **BigQuery is great for historical analysis but not for real-time monitoring.**
- **Batch-based ingestion (every 10 minutes) is too slow for real-time KPIs.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/loading-data**

**D. Insert the KPIs into Cloud Datastore entities and perform ad hoc analysis and visualizations in Cloud Datalab.** ❌

- **Cloud Datastore is a NoSQL database optimized for transactions, not real-time analytics.**
- **Cloud Datalab is used for interactive data exploration, not low-latency monitoring.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/concepts/overview**

**Conclusion:**

The best solution is **B. Output custom metrics to Stackdriver from the game servers and create a dashboard in Stackdriver Monitoring Console to view them**, because:
✔ **Cloud Monitoring is designed for real-time KPI tracking with low latency.**
✔ **Supports custom metrics and automated alerting.**
✔ **Provides built-in visualization dashboards without extra setup.**

📌 **Final Reference:**
**https://cloud.google.com/monitoring/custom-metrics/**

**⚠️ Note:** Google Data Studio is the current name again (it was Looker Studio from 2022 to 2026). Cloud Datastore is now Firestore in Datastore mode, and Cloud Datalab was retired in favor of Vertex AI Workbench.

</details>

---

### Exam 2 · Q6

**You are running a Google Kubernetes Engine (GKE) cluster that serves a web application. Users report that a specific part of the application is not responding. Upon investigation, you notice that all pods of the affected deployment keep restarting every 2 seconds. The application writes logs to standard output, and you need to inspect these logs to identify the issue.**

**Which approach should you take?**

- A. **Check Stackdriver logs** for each **Compute Engine instance** that serves as a **node** in the cluster.
- B. **Review Stackdriver logs** for the specific **GKE container** running the unresponsive part of the application.
- C. **Use `gcloud` to connect to the cluster**, access a container in one of the pods, and read the logs.
- D. **Review Serial Port logs** for each **Compute Engine instance** serving as a node in the cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Review Stackdriver logs** for the specific **GKE container** running the unresponsive part of the application.

**Correct Answer:**

✅ **B. Review Stackdriver logs for the specific GKE container running the unresponsive part of the application.**

**Explanation:**

The **best approach** is to use **Google Cloud Operations (formerly Stackdriver Logging)** to inspect logs for the **specific GKE container** running the affected part of the application.

✅ **Why Use Stackdriver Logging for GKE Containers?**

- **Centralized logging:** Automatically collects logs from all containers in the GKE cluster.
- **Persistent storage:** Unlike `kubectl logs`, logs are retained even if pods restart.
- **Container-specific insights:** Filters logs based on **namespace, pod, or container**.
- **Easy troubleshooting:** Helps detect errors like crashes, memory leaks, or misconfigurations.

**Steps to Inspect Logs in Cloud Logging:**

1. Open **Google Cloud Console** → Navigate to **Logging** → **Logs Explorer**.
2. Use the following filter to find logs for the affected deployment:
  ```
  resource.type="k8s_container"resource.labels.cluster_name="your-cluster-name"resource.labels.namespace_name="your-namespace"resource.labels.pod_name="your-pod-name"
  ```
3. Look for **errors** or **crash loops** in the logs to diagnose the issue.

✅ **Supporting Documentation:**

- **Google Cloud Logging for GKE:**
  **https://cloud.google.com/logging/docs/agent/logging**
- **Troubleshooting Kubernetes applications:**
  **https://cloud.google.com/kubernetes-engine/docs/troubleshooting**

**Why Other Options Are Incorrect?**

**A. Check Stackdriver logs for each Compute Engine instance that serves as a node in the cluster.** ❌

- **GKE logs are collected at the container level, not the Compute Engine instance level.**
- **Checking node logs would not directly help diagnose pod/container issues.**

✅ **Reference:**

- **https://cloud.google.com/logging/docs/kubernetes**

**C. Use `gcloud` to connect to the cluster, access a container in one of the pods, and read the logs.** ❌

- **Since pods are restarting every 2 seconds, logs may be lost before you can inspect them.**
- **Cloud Logging (Stackdriver) retains logs even after pod restarts.**
- **If logs are not centralized, using `kubectl logs` could still be useful, but Stackdriver is more efficient.**

✅ **Reference:**

- **https://kubernetes.io/docs/concepts/cluster-administration/logging/**

**D. Review Serial Port logs for each Compute Engine instance serving as a node in the cluster.** ❌

- **Serial port logs capture low-level VM boot and system messages, not application/container logs.**
- **Not useful for debugging Kubernetes pod restarts.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/troubleshooting/using-serial-console**

**Conclusion:**

The best approach is **B. Review Stackdriver logs for the specific GKE container running the unresponsive part of the application**, because:
✔ **It provides centralized logs for all containers in GKE.**
✔ **Logs persist even if pods restart frequently.**
✔ **Allows efficient troubleshooting using Google Cloud Logging.**

📌 **Final Reference:**
**https://cloud.google.com/logging/docs/kubernetes**

</details>

---

### Exam 2 · Q10

**You are using Cloud SQL as the database backend for a large CRM deployment. As usage increases, you need to ensure:**

- **Automatic storage scaling to prevent running out of space.**
- **CPU usage remains at 75% or below.**
- **Replication lag stays under 60 seconds.**

**Which steps should you take to meet these requirements?**

- A. **Enable automatic storage increase** for the instance. **Create a Stackdriver alert** when CPU usage exceeds 75%, and change the instance type to **reduce CPU usage**. **Create a Stackdriver alert** for replication lag, and **shard the database** to reduce replication time.
- B. **Enable automatic storage increase** for the instance. **Change the instance type to a 32-core machine** to keep CPU usage below 75%. **Create a Stackdriver alert** for replication lag and **deploy memcached** to reduce load on the primary instance.
- C. **Create a Stackdriver alert** when storage usage exceeds 75% and **manually increase** available storage. **Deploy memcached** to reduce CPU load. **Change the instance type to a 32-core machine** to reduce replication lag.
- D. **Create a Stackdriver alert** when storage usage exceeds 75% and **manually increase** available storage. **Deploy memcached** to reduce CPU load. **Create a Stackdriver alert** for replication lag and **change the instance type to a 32-core machine** to reduce lag.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Enable automatic storage increase** for the instance. **Create a Stackdriver alert** when CPU usage exceeds 75%, and change the instance type to **reduce CPU usage**. **Create a Stackdriver alert** for replication lag, and **shard the database** to reduce replication time.

**Correct Answer:**

✅ **A.**

- **Enable automatic storage increase for the instance.**
- **Create a Stackdriver alert when CPU usage exceeds 75%, and change the instance type to reduce CPU usage.**
- **Create a Stackdriver alert for replication lag, and shard the database to reduce replication time.**

**Explanation:**

The goal is to ensure:

1. **Automatic storage scaling** → Prevents the instance from running out of disk space.
2. **CPU usage remains at 75% or below** → Ensures stable performance.
3. **Replication lag stays under 60 seconds** → Ensures near real-time data availability.

**Why Option A is Correct?**

✅ **Enable automatic storage increase for the instance:**

- Cloud SQL can **automatically increase storage** when usage nears capacity.
- **This prevents running out of space** without manual intervention.
- **Command to enable:**
  ```
  gcloud sql instances patch my-instance --storage-auto-increase
  ```
- **Reference:**
  **https://cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase**

✅ **Create a Stackdriver (Cloud Monitoring) alert for CPU usage > 75% and upgrade instance type if needed:**

- **Monitors resource utilization** and prevents performance bottlenecks.
- **Upgrading the instance type (more CPUs/RAM) helps keep CPU below 75%.**
- **Reference:**
  **https://cloud.google.com/sql/docs/mysql/monitoring**

✅ **Create a Stackdriver alert for replication lag and shard the database if needed:**

- **Replication lag should stay under 60 seconds** to ensure data consistency.
- **Sharding distributes data across multiple instances**, reducing the replication burden.
- **Reference:**
  **https://cloud.google.com/sql/docs/mysql/replication**

**Why Other Options Are Incorrect?**

**B. Change the instance type to a 32-core machine to keep CPU usage below 75% and deploy memcached to reduce load.** ❌

- **Memcached helps reduce database queries, but does not directly improve replication lag.**
- **Upgrading to a 32-core machine is unnecessary unless CPU consistently exceeds 75%.**

✅ **Reference:**

- **https://cloud.google.com/memorystore/docs/memcached**

**C. Manually increase available storage instead of enabling auto-increase.** ❌

- **Manual storage management increases operational burden.**
- **Cloud SQL can auto-scale storage without downtime.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase**

**D. Create a Stackdriver alert when storage usage exceeds 75% and manually increase available storage.** ❌

- **Manual storage increase is not needed because auto-storage increase can be enabled.**
- **Replication lag is not resolved by upgrading to a 32-core machine.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**Conclusion:**

The best approach is **A**, because:
✔ **Automatic storage increase prevents out-of-space issues.**
✔ **Monitoring and upgrading instances keeps CPU usage optimal.**
✔ **Sharding improves replication performance.**

📌 **Final Reference:**
**https://cloud.google.com/sql/docs/mysql/high-availability**

**⚠️ Note:** Sharding is a heavy fix for replication lag; Cloud SQL guidance usually tries a larger replica, parallel replication or reduced write load first. A remains the best option because it is the only one using automatic storage increase.

</details>

---

### Exam 2 · Q12

**You have deployed an application on Google Kubernetes Engine (GKE) and are using the Cloud SQL proxy container to enable communication between the Cloud SQL database and the Kubernetes services. You receive a notification that the application is experiencing database connection issues. As per company policy, you must perform a post-mortem analysis.**

**What should you do?**

- A. Run `gcloud sql instances restart` to restart the Cloud SQL instance.
- B. Verify that the **Service Account** used by the Cloud SQL proxy container still has the **Cloud Build Editor** role.
- C. In the **Google Cloud Console**, navigate to **Stackdriver Logging** and review the logs for **Google Kubernetes Engine (GKE) and Cloud SQL**.
- D. In the **Google Cloud Console**, go to **Cloud SQL**, restore the latest backup, and use `kubectl` to restart all pods.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. In the **Google Cloud Console**, navigate to **Stackdriver Logging** and review the logs for **Google Kubernetes Engine (GKE) and Cloud SQL**.

**orrect Answer:**

C. In the Google Cloud Console, navigate to Stackdriver Logging and review the logs for Google Kubernetes Engine (GKE) and Cloud SQL.

**Explanation:**

Since the application is experiencing **database connection issues**, it is critical to **diagnose the root cause before taking any action**. The best way to perform a **post-mortem analysis** is to check logs for **both GKE and Cloud SQL** in **Cloud Logging (formerly Stackdriver Logging)** to identify potential issues.

**Why Cloud Logging for GKE and Cloud SQL?**

- Provides detailed **event and error logs** for GKE workloads and Cloud SQL connections.
- Helps determine if the issue is due to **networking, authentication, database load, or other factors**.
- Enables efficient **troubleshooting and root cause analysis** for post-mortem documentation.

**Steps to Investigate in Cloud Logging:**

1. Open **Google Cloud Console** → Navigate to **Logging** → **Logs Explorer**.
2. Apply filters for **GKE cluster logs** and **Cloud SQL instance logs**.
3. Look for errors such as:
  - **Cloud SQL Proxy connection failures**
  - **Database connection timeouts**
  - **Service account authentication issues**
4. Based on the findings, take appropriate action to fix the issue.

**Supporting Documentation:**

- **Troubleshooting Cloud SQL Proxy Issues:**
  https://cloud.google.com/sql/docs/mysql/sql-proxy#troubleshooting
- **GKE and Cloud SQL Logging:**
  https://cloud.google.com/logging/docs/logs-viewer

**Why Other Options Are Incorrect?**

**A. Run `gcloud sql instances restart` to restart the Cloud SQL instance.**

- Restarting the database **without diagnosing the issue first** may cause unnecessary downtime.
- If the problem is related to **Cloud SQL proxy, network configuration, or service account permissions**, restarting will not resolve it.
- **Better approach:** Check logs first before considering a restart.

**Reference:**
https://cloud.google.com/sql/docs/mysql/manage-instances

**B. Verify that the Service Account used by the Cloud SQL proxy container still has the Cloud Build Editor role.**

- **The Cloud Build Editor role is not relevant** for Cloud SQL proxy access.
- The correct role for Cloud SQL Proxy is **Cloud SQL Client (`roles/cloudsql.client`)**, which allows authentication and connection to the database.
- **Better approach:** Verify IAM roles only if logs indicate authentication failures.

**Reference:**
https://cloud.google.com/sql/docs/mysql/connect-kubernetes-engine

**D. Restore the latest backup and use `kubectl` to restart all pods.**

- Restoring a backup **should only be done if data loss or corruption is confirmed**.
- This action may **cause unnecessary data loss** if the issue is just a connectivity problem.
- **Better approach:** Check logs to confirm the root cause before considering a database restore.

**Reference:**
https://cloud.google.com/sql/docs/mysql/backup-recovery

**Conclusion:**

The best approach is **C. In the Google Cloud Console, navigate to Stackdriver Logging and review the logs for Google Kubernetes Engine (GKE) and Cloud SQL**, because:

- It allows for **root cause analysis** before taking corrective action.
- It helps diagnose issues related to **networking, authentication, or database performance**.
- It follows **best practices for post-mortem analysis**.

**Final Reference:**
https://cloud.google.com/logging/docs/logs-viewer

</details>

---

### Exam 2 · Q20

**Your BigQuery project has multiple users, and for audit purposes, you need to determine how many queries each user ran in the last month.**

**What should you do?**

- A. **Connect Google Data Studio** to BigQuery, create a **dimension for users**, and define a **metric** for the number of queries per user.
- B. In the **BigQuery interface**, execute a query on the `JOBS` **table** to retrieve the required information.
- C. Use `bq show` to list all jobs, then use `bq ls` to obtain job details and extract the necessary information.
- D. Use **Cloud Audit Logging** to view **Cloud Audit Logs** and create a **filter on query operations** to extract the required information.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. In the **BigQuery interface**, execute a query on the `JOBS` **table** to retrieve the required information.

**Correct Answer:**

**B. In the BigQuery interface, execute a query on the JOBS table to retrieve the required information.**

**Explanation:**

To **audit query usage** and determine how many queries each user ran in the last month, you should **query the JOBS table in** `INFORMATION_SCHEMA`.

**Why Use INFORMATION_SCHEMA.JOBS?**

- **INFORMATION_SCHEMA.JOBS** contains **metadata on BigQuery jobs**, including **query executions, timestamps, and user identities**.
- **It allows filtering by time range**, so you can extract **query counts per user for the last month**.

**Implementation Steps:**

1. **Run the following query in BigQuery UI** to get query counts per user:
  ```
  SELECT  user_email,  COUNT(*) AS query_countFROM  `region-us`.INFORMATION_SCHEMA.JOBS_BY_USERWHERE  job_type = "QUERY"  AND creation_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)GROUP BY  user_emailORDER BY  query_count DESC;
  ```
2. **Explanation of the query:**
  - `user_email` → Identifies the user who ran the query.
  - `COUNT(*)` → Counts the number of queries executed.
  - `creation_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)` → Filters queries executed in the **last month**.
  - `GROUP BY user_email` → Groups results by **individual users**.
  - `ORDER BY query_count DESC` → Sorts users based on query volume.

**Supporting Documentation:**

- **BigQuery INFORMATION_SCHEMA.JOBS:**
  https://cloud.google.com/bigquery/docs/information-schema-jobs
- **BigQuery Job Metadata Best Practices:**
  https://cloud.google.com/bigquery/docs/reference/information-schema-jobs

**Why Other Options Are Incorrect?**

**A. Connect Google Data Studio to BigQuery, create a dimension for users, and define a metric for the number of queries per user.**

- **Google Data Studio is a visualization tool**, not meant for auditing system-level operations like query execution.
- **You still need to extract query metadata from INFORMATION_SCHEMA first**, which makes this method inefficient.

✅ **Reference:**
https://support.google.com/datastudio/answer/6370294?hl=en

**C. Use `bq show` to list all jobs, then use `bq ls` to obtain job details and extract the necessary information.**

- `bq show` and `bq ls` **list jobs but do not provide structured query counts per user**.
- This method is **manual and inefficient** compared to querying `INFORMATION_SCHEMA.JOBS`.

✅ **Reference:**
https://cloud.google.com/bigquery/docs/managing-jobs

**D. Use Cloud Audit Logging to view Cloud Audit Logs and create a filter on query operations to extract the required information.**

- **Cloud Audit Logs capture broader GCP events**, not just BigQuery queries.
- **Filtering through logs is inefficient**, and **query counts per user are not directly available** in audit logs.

✅ **Reference:**
https://cloud.google.com/logging/docs/audit

**Conclusion:**

The best approach is **B. Execute a query on the JOBS table in BigQuery's INFORMATION_SCHEMA**, because:

- It **provides structured metadata on query execution**.
- It **allows efficient filtering and aggregation of query counts per user**.
- It **follows Google Cloud's best practices for auditing BigQuery usage**.

**Final Reference:**
[https://cloud.google.com/bigquery/docs/information-schema-jobs](https://cloud.google.com/bigquery/docs/information-schema-jobs)

</details>

---

### Exam 2 · Q26

**Your architecture requires centralized collection of all admin activity logs and VM system logs within your Google Cloud project.**

**How should you collect these logs from both VMs and cloud services?**

- A. **All admin and VM system logs** are automatically collected by **Stackdriver Logging**.
- B. **Stackdriver Logging automatically collects admin activity logs** for most services, but the **Stackdriver Logging agent must be installed** on each instance to collect system logs.
- C. Deploy a **custom syslogd Compute Engine instance** and configure your **Google Cloud project and VMs** to forward all logs to it.
- D. Install the **Stackdriver Logging agent** on a **single Compute Engine instance**, allowing it to collect **all audit and access logs** for your environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Stackdriver Logging automatically collects admin activity logs** for most services, but the **Stackdriver Logging agent must be installed** on each instance to collect system logs.

**Correct Answer:**

**B. Stackdriver Logging automatically collects admin activity logs for most services, but the Stackdriver Logging agent must be installed on each instance to collect system logs.**

**Explanation:**

To **centrally collect both admin activity logs and VM system logs**, Google Cloud **automatically collects admin activity logs for cloud services**, while **VM system logs require the Stackdriver Logging agent to be installed**.

**How This Works:**

**1. Admin Activity Logs (Automatically Collected by Cloud Logging)**

- **Cloud Audit Logs automatically capture admin activity logs** for most Google Cloud services without additional configuration.
- These logs are stored in **Cloud Logging (formerly Stackdriver Logging)** and can be queried using **Logs Explorer** or exported to **BigQuery or Cloud Storage**.

**Example Query to View Admin Activity Logs:**

```
resource.type="gce_instance"logName="projects/my-project/logs/cloudaudit.googleapis.com%2Factivity"
```

**2. VM System Logs (Require Logging Agent)**

- Compute Engine **does not automatically send system logs** to Cloud Logging.
- You must **install the Logging agent** on each instance to capture logs such as:
  - **syslog, auth.log, kernel logs, application logs**
  - **Custom application logs from `/var/log/` directories**

**Installation Command for Logging Agent (Debian/Ubuntu):**

```
curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.shsudo bash add-logging-agent-repo.shsudo apt-get update && sudo apt-get install google-fluentdsudo systemctl start google-fluentd
```

**Installation for CentOS/RHEL:**

```
curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.shsudo bash add-logging-agent-repo.shsudo yum install google-fluentd -ysudo systemctl start google-fluentd
```

**Supporting Documentation:**

- **Admin Activity Logs in Cloud Audit Logs:**
  https://cloud.google.com/logging/docs/audit#admin-activity
- **Installing the Logging Agent on VMs:**
  https://cloud.google.com/logging/docs/agent/installation

**Why Other Options Are Incorrect?**

**A. All admin and VM system logs are automatically collected by Stackdriver Logging.**

- **Admin logs are automatically collected**, but **VM system logs require the Logging agent**.
- **This statement is partially incorrect because system logs are not collected by default.**

✅ **Reference:**
https://cloud.google.com/logging/docs/agent/installation

**C. Deploy a custom syslogd Compute Engine instance and configure your Google Cloud project and VMs to forward all logs to it.**

- **Manually setting up a custom syslogd server is unnecessary** because **Cloud Logging already provides centralized log collection**.
- **Google-recommended best practice** is to use **Cloud Logging** instead of manually managing a separate logging server.

✅ **Reference:**
https://cloud.google.com/logging/docs/export/configure_export

**D. Install the Stackdriver Logging agent on a single Compute Engine instance, allowing it to collect all audit and access logs for your environment.**

- **The Logging agent only collects logs from the instance it is installed on.**
- **To collect logs from multiple instances, the agent must be installed on each VM.**
- **Admin logs do not require the agent**—they are collected automatically.

✅ **Reference:**
https://cloud.google.com/logging/docs/agent/

**Conclusion:**

The best approach is **B. Stackdriver Logging automatically collects admin activity logs for most services, but the Stackdriver Logging agent must be installed on each instance to collect system logs**, because:

- **Admin logs are automatically collected** by Cloud Logging.
- **VM system logs require the Logging agent** for collection.
- **It aligns with Google-recommended best practices** for log management.

**Final Reference:**
[https://cloud.google.com/logging/docs/agent/installation](https://cloud.google.com/logging/docs/agent/installation)

**⚠️ Note:** The legacy Logging agent has been replaced by the Ops Agent, which collects both logs and metrics. It still has to run on every VM.

</details>

---

### Exam 2 · Q43

You are **monitoring Google Kubernetes Engine (GKE) clusters** in a **Cloud Monitoring workspace**. As a **Site Reliability Engineer (SRE)**, you need to **triage incidents quickly**.

What should you do?

- A. Use the **predefined dashboards** in the **Cloud Monitoring workspace**, then **add relevant metrics** and **create alert policies**.
- B. Use the **predefined dashboards** in the **Cloud Monitoring workspace**, create **custom metrics**, and **install alerting software** on a **Compute Engine instance**.
- C. Develop a **shell script** that gathers **GKE node metrics**, publishes the data to **Pub/Sub**, exports it to **BigQuery**, and visualizes it in **Data Studio**.
- D. Create a **custom dashboard** in the **Cloud Monitoring workspace** for **each incident**, then **add relevant metrics** and **set up alert policies**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use the **predefined dashboards** in the **Cloud Monitoring workspace**, then **add relevant metrics** and **create alert policies**.

**Correct Answer:**

**A. Use the predefined dashboards in the Cloud Monitoring workspace, then add relevant metrics and create alert policies.**

**Explanation:**

As a **Site Reliability Engineer (SRE)**, **triaging incidents quickly** requires **real-time monitoring, alerting, and actionable insights**. The **best approach** is to:

1. **Leverage predefined dashboards in Cloud Monitoring** for **immediate visibility** into **GKE metrics (CPU, memory, networking, pod health, etc.)**.
2. **Customize dashboards by adding relevant metrics** (e.g., pod restart counts, container CPU usage, node health).
3. **Set up alert policies** to **automate incident detection** and **reduce manual triaging effort**.

✅ **Predefined dashboards provide immediate insights without requiring additional setup.**
✅ **Alert policies help SREs react quickly to critical events.**
✅ **This approach follows Google-recommended best practices for SREs.**

**How to Implement This in Cloud Monitoring?**

**1. Access Predefined Dashboards**

- Go to **Google Cloud Console** → **Cloud Monitoring** → **Dashboards**.
- Select **GKE Dashboard**, which shows cluster-wide metrics.

**2. Customize Metrics Based on Incident Needs**

Use **Cloud Monitoring Query Language (MQL)** to create custom queries, e.g.:

```
fetch k8s_container| metric 'kubernetes.io/container/cpu/core_usage_time'| group_by [resource.cluster_name, metric_name], sliding(5m)| every 1m
```

✅ **Reference:** https://cloud.google.com/monitoring/mql

**3. Set Up Alert Policies for Critical Metrics**

- Define alert policies for **pod failures, high CPU/memory usage, node health, and network latency**.
- Configure **notification channels (Slack, PagerDuty, email, etc.)**.

✅ **Reference:** https://cloud.google.com/monitoring/alerts

**Why Other Options Are Incorrect?**

**B. Use predefined dashboards, create custom metrics, and install alerting software on a Compute Engine instance.**

❌ **Incorrect:**

- **Cloud Monitoring already provides alerting**—**no need for additional software**.
- **Compute Engine is not required**; alerting can be configured **natively in Cloud Monitoring**.

✅ **Reference:**
https://cloud.google.com/monitoring/alerts

**C. Develop a shell script that gathers GKE node metrics, publishes to Pub/Sub, exports to BigQuery, and visualizes in Data Studio.**

❌ **Incorrect:**

- **Too complex and unnecessary**—Cloud Monitoring **already provides** real-time insights.
- **Cloud Monitoring offers built-in dashboards**, eliminating the need for **manual data pipelines**.

✅ **Reference:**
https://cloud.goog[le.com/monitoring/kubernetes-engineD. C](https://cloud.google.com/monitoring/kubernetes-engine)**reate a custom dashboard for each incident and set up alert policies.**

❌ **Incorrect:**

- **Inefficient and reactive**—SREs need **proactive alerting**, not dashboards created *after* incidents occur.
- **Predefined dashboards already provide key insights**, reducing setup time.

✅ **Reference:**
https://cloud.google.com/monitoring/dashboards

**Conclusion:**

The best answer is **A. Use predefined dashboards in the Cloud Monitoring workspace, then add relevant metrics and create alert policies**, because:

- **Predefined dashboards give immediate visibility into GKE health.**
- **Custom metrics allow tailored monitoring.**
- **Alert policies proactively notify SREs, reducing mean time to resolution (MTTR).**
- **Aligns with Google SRE best practices.**

✅ **Final Reference:**
[https://cloud.google.com/monitoring/kubernetes-engine](https://cloud.google.com/monitoring/kubernetes-engine)

**⚠️ Note:** Cloud Monitoring "workspaces" have been replaced by metrics scopes.

</details>

---

### Exam 2 · Q48

Your company is using **Firewall Insights** in **Google Network Intelligence Center** to analyze **firewall rules applied to Compute Engine instances**.

You need to **evaluate the efficiency** of your **firewall ruleset**, but when you open the **Firewall Insights page** in the **Google Cloud Console**, **no log entries** are displayed.

How should you troubleshoot this issue?

- A. Enable Virtual Private Cloud (VPC) flow logging.
- B. Enable Firewall Rules Logging for the firewall rules you want to monitor.
- C. Verify that your user account has the compute.networkAdmin IAM role.
- D. Install the Google Cloud SDK and check for Firewall logs using the command-line output.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Enable Firewall Rules Logging for the firewall rules you want to monitor.

**Correct Answer:**

**B. Enable Firewall Rules Logging for the firewall rules you want to monitor.**

**Explanation:**

Google **Firewall Insights** in **Network Intelligence Center** analyzes firewall rules by inspecting **firewall rule logs**. If **no log entries appear**, the most likely reason is that **Firewall Rules Logging is not enabled**.

✅ **Firewall Rules Logging must be enabled for each firewall rule** to capture traffic logs for analysis.
✅ **Firewall Insights relies on these logs** to evaluate unused rules, shadowed rules, and suboptimal rules.
✅ **Once logging is enabled, logs are stored in Cloud Logging**, which Firewall Insights uses for analysis.

**How to Enable Firewall Rules Logging?**

**1. Enable Logging for a Specific Firewall Rule Using gcloud**

Run the following command:

```
gcloud compute firewall-rules update my-firewall-rule \    --enable-logging
```

**2. Enable Logging for a Firewall Rule in the Console**

1. Go to **Google Cloud Console** → **VPC Network** → **Firewall**.
2. Select the **firewall rule** you want to log.
3. Click **Edit** → **Enable Logging**.
4. Click **Save**.

✅ **Reference:**
https://cloud.google.com/vpc/docs/firewall-rules-logging

**Why Other Options Are Incorrect?**

**A. Enable Virtual Private Cloud (VPC) flow logging.**

❌ **Incorrect:**

- **VPC Flow Logs capture network traffic metadata** but do not provide firewall-specific insights.
- **Firewall Insights does not rely on VPC Flow Logs**—it requires **Firewall Rules Logging** instead.

✅ **Reference:**
https://cloud.google.com/vpc/docs/flow-logs

**C. Verify that your user account has the compute.networkAdmin IAM role.**

❌ **Incorrect:**

- **IAM permissions determine access**, but they **do not affect firewall rule logging**.
- Even **users with full permissions** will not see logs unless **Firewall Rules Logging is enabled**.

✅ **Reference:**
https://cloud.google.com/iam/docs/understanding-roles

**D. Install the Google Cloud SDK and check for Firewall logs using the command-line output.**

❌ **Incorrect:**

- **Using gcloud or the Cloud SDK will not display logs unless logging is enabled**.
- **The issue is not related to missing tools, but missing logging configuration**.

✅ **Reference:**
https://cloud.google.com/sdk

**Conclusion:**

The best approach is **B. Enable Firewall Rules Logging for the firewall rules you want to monitor**, because:

- **Firewall Insights relies on Firewall Rules Logging, not VPC Flow Logs.**
- **Firewall Rules Logging must be manually enabled for each rule.**
- **Once enabled, logs appear in Cloud Logging and can be analyzed by Firewall Insights.**

✅ **Final Reference:**
[https://cloud.google.com/vpc/docs/firewall-rules-logging](https://cloud.google.com/vpc/docs/firewall-rules-logging)

</details>

---

### Exam 2 · Q54

You need to **deploy an application** on **Google Cloud** that must run on a **Debian Linux environment**.

- The application requires **extensive configuration** to function properly.
- You want to ensure that **Debian distribution updates** can be **installed with minimal manual intervention** whenever they become available.

What should you do?

- A. **Create a Compute Engine instance template** using the **latest Debian image**. Deploy an **instance from the template** and configure the application via a **startup script**. Repeat this process when a **new Google-managed Debian image** is released.
- B. **Create a Debian-based Compute Engine instance**, install and configure the application, and use **OS patch management** to automatically apply available updates.
- C. **Deploy an instance with the latest Debian image**, connect via **SSH**, and manually **install and configure** the application. Repeat this process whenever a **new Google-managed Debian image** is available.
- D. **Create a Docker container** with **Debian as the base image**. Install and configure the application as part of the **Docker image creation**. Deploy the contai

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Create a Debian-based Compute Engine instance**, install and configure the application, and use **OS patch management** to automatically apply available updates.

**Correct Answer:**

**B. Create a Debian-based Compute Engine instance, install and configure the application, and use OS patch management to automatically apply available updates.**

**Explanation:**

The **best approach** to **deploy and maintain an application on a Debian Linux environment** with **minimal manual intervention for updates** is:
✅ **Using OS patch management** for **automatic updates** while ensuring the application runs with **minimal downtime**.
✅ **Compute Engine provides a Debian-based VM**, allowing **configuration flexibility** and **automatic OS patching** using Google Cloud’s OS patch management.
✅ **This ensures security updates and package updates** are applied **without requiring full instance recreation**.

**How to Implement This?**

**1. Create a Debian-based Compute Engine Instance**

```
gcloud compute instances create my-debian-instance \    --zone=us-central1-a \    --image-family=debian-11 \    --image-project=debian-cloud \    --machine-type=n1-standard-1
```

**2. Enable OS Patch Management**

```
gcloud compute os-config patch-jobs execute \    --instance-filter="name=my-debian-instance" \    --reboot-config=if-needed \    --patch-config="patch_window=03:00-04:00"
```

- This **automatically applies Debian OS updates**, ensuring security and stability.
- **OS patch management minimizes manual intervention** while keeping the system updated.

✅ **Reference:**
https://cloud.google.com/compute/docs/os-patch-management

**Why Other Options Are Incorrect?**

**A. Create a Compute Engine instance template using the latest Debian image. Deploy an instance from the template and configure the application via a startup script. Repeat this process when a new Google-managed Debian image is released.**

❌ **Incorrect:**

- **Manually redeploying instances every time a new Debian image is released is inefficient**.
- **Startup scripts can configure the application**, but **do not ensure automatic OS updates**.
- **OS patch management is a better alternative than constantly recreating instances**.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-templates

**C. Deploy an instance with the latest Debian image, connect via SSH, and manually install and configure the application. Repeat this process whenever a new Google-managed Debian image is available.**

❌ **Incorrect:**

- **Manually configuring the application every time a new image is available is inefficient**.
- **No automatic patching mechanism**—updates must be done manually.
- **Time-consuming and increases the risk of errors** compared to OS patch management.

✅ **Reference:**
https://cloud.google.com/compute/docs/images

**D. Create a Docker container with Debian as the base image. Install and configure the application as part of the Docker image creation. Deploy the container.**

❌ **Incorrect:**

- **Using a container is a good approach for portability**, but **it does not automatically handle Debian OS updates**.
- **Containers are isolated environments**—OS patching for the base Debian image requires rebuilding and redeploying the container.
- **If the application requires direct interaction with the Debian OS, a Compute Engine instance is more suitable**.

✅ **Reference:**
https://cloud.google.com/run/docs/quickstarts/build-and-deploy/debian

**Conclusion:**

The best option is **B. Create a Debian-based Compute Engine instance, install and configure the application, and use OS patch management to automatically apply available updates**, because:

- **It ensures automatic updates with minimal manual intervention**.
- **OS patch management applies security patches without requiring full instance redeployment**.
- **It follows Google Cloud best practices for OS maintenance and security**.

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/os-patch-management](https://cloud.google.com/compute/docs/os-patch-management)

</details>

---

### Exam 2 · Q55

Your **application runs on Google Kubernetes Engine (GKE)**. Over the past **two weeks**, customers have reported that a **specific part of the application** is **frequently returning errors**.

- You **do not have any logging or monitoring** enabled on the GKE cluster.
- You have **not been able to replicate the issue**.
- You need to **diagnose the problem** while causing **minimal disruption** to the application.

What should you do?

- A.**Enable Cloud Operations for GKE** on your **existing cluster**. Use the **GKE Monitoring dashboard** to **analyze logs** from the affected Pods.
- B.**Create a new GKE cluster** with **Cloud Operations for GKE enabled**. **Migrate the affected Pods** to the **new cluster** and **redirect traffic** to it. Use the **GKE Monitoring dashboard** to **analyze logs** from the affected Pods.
- C.**Enable Cloud Operations for GKE** on your **existing cluster** and **deploy Prometheus**. **Set an alert** to **trigger when errors occur** in the application.
- D.**Create a new GKE cluster** with **Cloud Operations for GKE enabled** and **deploy Prometheus**. **Migrate the affected Pods** to the **new cluster** and **redirect traffic** to it. **Set an alert** to **trigger when errors occur**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A.**Enable Cloud Operations for GKE** on your **existing cluster**. Use the **GKE Monitoring dashboard** to **analyze logs** from the affected Pods.

**Correct Answer:**

**A. Enable Cloud Operations for GKE on your existing cluster. Use the GKE Monitoring dashboard to analyze logs from the affected Pods.**

**Explanation:**

Since **logging and monitoring are not currently enabled** on the **existing GKE cluster**, the best approach is to **enable Cloud Operations for GKE** on the **current cluster** and use the **GKE Monitoring dashboard** to analyze logs from affected Pods.

✅ **Why this is the best solution?**

- **Enabling Cloud Operations (formerly Stackdriver) on the existing cluster allows for immediate log collection** without disrupting the running application.
- **It provides real-time visibility into logs and metrics**, allowing you to analyze application errors.
- **Minimal disruption**: No need to migrate workloads or create a new cluster.

**How to Implement This?**

**1. Enable Cloud Operations for GKE on the Existing Cluster**

```
gcloud container clusters update my-gke-cluster \    --logging=SYSTEM,WORKLOAD \    --monitoring=SYSTEM
```

- This **enables logging and monitoring** for both **system components** and **application workloads**.

**2. View Logs and Errors in Cloud Operations (Logging and Monitoring)**

- **Navigate to Cloud Logging**:
  - Open **Google Cloud Console** → **Operations** → **Logging** → **Logs Explorer**.
  - **Filter by Kubernetes namespace and Pod name** to find logs from the affected service.
- **Analyze Metrics in Cloud Monitoring**:
  - Open **Google Cloud Console** → **Operations** → **Monitoring** → **Metrics Explorer**.
  - Select **GKE Cluster** and **filter by error logs** to identify application issues.

✅ **Reference:**
https://cloud.google.com/stackdriver/docs/solutions/gke

**Why Other Options Are Incorrect?**

**B. Create a new GKE cluster with Cloud Operations for GKE enabled. Migrate the affected Pods to the new cluster and redirect traffic to it. Use the GKE Monitoring dashboard to analyze logs from the affected Pods.**

❌ **Incorrect:**

- **Creating a new cluster is unnecessary** and increases operational overhead.
- **Migrating affected Pods and redirecting traffic can cause downtime and service disruptions**.
- **Enabling Cloud Operations on the existing cluster is faster and less disruptive**.

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/how-to/observability/gke-cloud-operations

**C. Enable Cloud Operations for GKE on your existing cluster and deploy Prometheus. Set an alert to trigger when errors occur in the application.**

❌ **Incorrect:**

- **Cloud Operations for GKE already provides logging and monitoring, so deploying Prometheus is not necessary.**
- **Setting an alert is useful for future monitoring but does not help diagnose the current issue.**
- **Cloud Logging and Monitoring already include built-in alerting features**—Prometheus is **not required** unless for custom metrics.

✅ **Reference:**
https://cloud.google.com/monitoring/alerts

**D. Create a new GKE cluster with Cloud Operations for GKE enabled and deploy Prometheus. Migrate the affected Pods to the new cluster and redirect traffic to it. Set an alert to trigger when errors occur.**

❌ **Incorrect:**

- **Unnecessary overhead**: Creating a new cluster does not solve the current issue.
- **Migration is disruptive**: Moving Pods may introduce additional complexity and downtime.
- **Cloud Operations already provides monitoring and alerting without needing Prometheus.**

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/concepts/observability

**Conclusion:**

The best approach is **A. Enable Cloud Operations for GKE on your existing cluster and use the GKE Monitoring dashboard to analyze logs from the affected Pods**, because:

- **It enables real-time logs and monitoring without disrupting the application**.
- **It allows quick diagnosis of errors with minimal intervention**.
- **It follows Google Cloud best practices for observability in Kubernetes environments**.

✅ **Final Reference:**
[https://cloud.google.com/stackdriver/docs/solutions/gke](https://cloud.google.com/stackdriver/docs/solutions/gke)

**⚠️ Note:** "Cloud Operations for GKE" is now simply the Cloud Logging and Cloud Monitoring integration for GKE, enabled by default on new clusters.

</details>

---

### Exam 2 · Q57

Your company has an **application deployed on Anthos clusters (formerly Anthos GKE)** running **multiple microservices**.

- The **cluster is configured** with **Anthos Service Mesh** and **Anthos Config Management**.
- **End users** have reported that the application is **responding very slowly**.
- You need to **identify which microservice is causing the delay**.

What should you do?

- A. **Use the Service Mesh visualization** in the **Google Cloud Console** to inspect **telemetry data** between the microservices.
- B. **Use Anthos Config Management** to create a **ClusterSelector** for the relevant cluster. Then, in the **Google Kubernetes Engine (GKE) console**, navigate to **Workloads**, filter by cluster, and inspect the **workload configurations**.
- C. **Use Anthos Config Management** to create a **NamespaceSelector** for the relevant namespace. Then, in the **Google Kubernetes Engine (GKE) console**, navigate to **Workloads**, filter by namespace, and inspect the **workload configurations**.
- D. **Reinstall Istio** using the **default Istio profile** to enable **request latency tracking**, then analyze the **telemetry data** between microservices in the **Google Cloud Console**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Use the Service Mesh visualization** in the **Google Cloud Console** to inspect **telemetry data** between the microservices.

**Correct Answer:**

**A. Use the Service Mesh visualization in the Google Cloud Console to inspect telemetry data between the microservices.**

**Explanation:**

Since the **application is deployed on Anthos clusters using Anthos Service Mesh**, the **best way to identify which microservice is causing latency issues** is by using **Service Mesh visualization** in the **Google Cloud Console**.

✅ **Anthos Service Mesh provides built-in observability** features such as **telemetry, distributed tracing, and service dependency graphs**.
✅ **The Service Mesh visualization helps quickly identify microservices with high latency** by analyzing **traffic flow, request rates, and error rates**.
✅ **Minimal disruption**: This method does **not require modifying the cluster or redeploying services**.

**How to Implement This?**

**1. Access the Anthos Service Mesh Dashboard**

- **Go to the Google Cloud Console** → **Anthos** → **Service Mesh**.
- Click on **Service Graph** to **visualize traffic between microservices**.

**2. Analyze the Telemetry Data**

- **Check the latency metrics** for each microservice.
- Identify any **high response times or request failures**.
- Drill down into **tracing data to see where delays originate**.

✅ **Reference:**
https://cloud.google.com/service-mesh/docs/observability

**Why Other Options Are Incorrect?**

**B. Use Anthos Config Management to create a ClusterSelector for the relevant cluster. Then, in the Google Kubernetes Engine (GKE) console, navigate to Workloads, filter by cluster, and inspect the workload configurations.**

❌ **Incorrect:**

- **Anthos Config Management (ACM) is for policy enforcement and configuration management**, not real-time service monitoring.
- **Does not provide latency metrics or telemetry insights.**

✅ **Reference:**
https://cloud.google.com/anthos/config-management/docs/how-to/namespace-selector

**C. Use Anthos Config Management to create a NamespaceSelector for the relevant namespace. Then, in the Google Kubernetes Engine (GKE) console, navigate to Workloads, filter by namespace, and inspect the workload configurations.**

❌ **Incorrect:**

- **NamespaceSelector helps enforce policies and configurations** but **does not analyze performance issues or service latency**.
- **Does not provide any visibility into request delays between microservices**.

✅ **Reference:**
https://cloud.google.com/anthos/config-management/docs/how-to/namespace-selector

**D. Reinstall Istio using the default Istio profile to enable request latency tracking, then analyze the telemetry data between microservices in the Google Cloud Console.**

❌ **Incorrect:**

- **Istio is already installed as part of Anthos Service Mesh**—no need to reinstall it.
- **Latency tracking is enabled by default in Anthos Service Mesh.**
- **Reinstalling Istio disrupts the application and is unnecessary for diagnosing latency issues.**

✅ **Reference:**
https://cloud.google.com/service-mesh/docs/observability/metrics

**Conclusion:**

The best approach is **A. Use the Service Mesh visualization in the Google Cloud Console to inspect telemetry data between the microservices**, because:

- **It provides real-time telemetry and latency data without disruption**.
- **It allows tracing requests between microservices** to quickly locate performance bottlenecks.
- **It follows Google Cloud best practices for diagnosing microservice performance issues.**

✅ **Final Reference:**
[https://cloud.google.com/service-mesh/docs/observability](https://cloud.google.com/service-mesh/docs/observability)

**⚠️ Note:** Anthos clusters are now GKE Enterprise, Anthos Service Mesh is now Cloud Service Mesh, and Anthos Config Management is now Config Sync + Policy Controller.

</details>

---

### Exam 3 · Q1

**The operations team at CloudNova Inc. has asked for your assistance in investigating a performance issue affecting a production application hosted on Google Compute Engine. Under heavy traffic, the application begins to drop incoming requests. System diagnostics reveal that one application process on each impacted instance is consuming 100% of CPU resources. The autoscaler has already reached its configured maximum instance count, and no anomalies are detected in connected systems like the database. You need to recommend a solution that will restore production traffic as quickly as possible.**

**What should you suggest?**

- A. Update the autoscaling policy to use the metric `agent.googleapis.com/memory/percent_used`.
- B. Initiate a phased restart of the impacted instances.
- C. Connect to each instance via SSH and manually restart the application process.
- D. Increase the autoscaling group's maximum instance limit.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Increase the autoscaling group's maximum instance limit.

**Correct Answer: D. Increase the autoscaling group's maximum instance limit**

**Explanation:**

**Scenario Summary:**

- Production application is hosted on **Google Compute Engine (GCE)**.
- **Under heavy traffic**, application is **dropping requests**.
- Diagnostics show **100% CPU usage** by the application process on each instance.
- **Autoscaler has already reached its configured max instance count**.
- No anomalies in connected systems (like the database).
- Goal: **Restore traffic quickly**.

✅ **Why Option D is Correct:**

**Increasing the autoscaling group’s maximum instance limit** is the most effective way to:

- **Allow the managed instance group to scale out** further in response to CPU saturation.
- **Immediately reduce load per instance** by adding new VM instances.
- **Preserve system stability** without downtime or manual intervention.

**Google Cloud documentation states:**

“If an autoscaler reaches its maximum number of instances and your application still experiences high load, increasing the maximum limit allows autoscaler to continue scaling out.”
— Source: Compute Engine Autoscaler – Maximum number of instances

This is the **fastest and most scalable way** to handle high CPU usage caused by traffic spikes.

❌ **Why Other Options Are Incorrect:**

**A. Update the autoscaling policy to use the metric** `agent.googleapis.com/memory/percent_used`

- The bottleneck is **CPU**, not memory.
- Changing the metric to memory usage **would delay or mislead autoscaler behavior**.
- Google recommends selecting a metric that **matches the application’s resource constraint**.

**Documentation reference:**

“Choose a metric that best reflects your application's bottleneck resource.”
— Using Cloud Monitoring Metrics with Autoscaler

So, using a memory-based metric won’t address the **CPU-bound nature** of the issue.

**B. Initiate a phased restart of the impacted instances**

- Restarting instances doesn't **add more capacity**.
- It may temporarily reduce CPU usage but **disrupts traffic and service availability**.
- The issue will **likely return** when the instance restarts and receives the same load.

**Docs for VM Troubleshooting:**

“Restart instances only when they are stuck or unresponsive.”
— Troubleshooting VM Instances

Here, the instances are responsive—they’re just **overloaded**.

**C. Connect to each instance via SSH and manually restart the application process**

- This is **manual, time-consuming, and not scalable** for production systems.
- Restarting the app doesn’t resolve **excessive load** or increase capacity.
- May offer temporary relief but doesn't solve the underlying CPU saturation.

**Docs on SSH into VM instances:**

SSH is a helpful diagnostic tool, but manual restarts are not suitable for automated, scalable solutions.
— Connecting to Instances

✅ Final Recommendation:

**Increase the autoscaler’s maximum instance count** so it can continue scaling out to meet traffic demands and reduce CPU pressure.

**Documentation:**

- [Autoscaler Overview – Compute Engine](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions)
- [Scaling based on load](https://cloud.google.com/compute/docs/autoscaler/scaling-load-balancing)

</details>

---

### Exam 3 · Q13

Your team is building a **web application** that will be deployed on **Google Kubernetes Engine (GKE)**. The **CTO anticipates high user traffic** at launch, potentially **tens of thousands of users**. You need to ensure that the application can **maintain acceptable latency** under this expected load.

How should you test your current deployment to validate that latency stays within an acceptable threshold?

- A. Use a **load testing tool** to simulate the anticipated number of **concurrent users and requests**, then analyze the performance results.
- B. Enable **GKE cluster autoscaling** and **horizontal pod autoscaling** for your application. Use `curl` commands to send requests and verify if autoscaling responds correctly.
- C. Deploy your application across **multiple GKE clusters in all Google Cloud regions** and configure a **global HTTP(S) load balancer** with a single global IP to route traffic.
- D. Use **Cloud Debugger** in your development environment to observe **latency between microservices**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use a **load testing tool** to simulate the anticipated number of **concurrent users and requests**, then analyze the performance results.

✅ **Correct Answer: A. Use a load testing tool to simulate the anticipated number of concurrent users and requests, then analyze the performance results.**

**Scenario Summary:**

- You are deploying a **web application on GKE**.
- Expecting **high traffic at launch** (tens of thousands of users).
- Goal: **Ensure acceptable latency** under anticipated load.
- Need to **validate current deployment** before going live.

✅ **Why Option A is Correct:**

**Load Testing is the Industry Best Practice**

- You need to **simulate real-world traffic patterns** with the expected number of users and requests.
- Load testing tools such as **Locust**, **k6**, **Apache JMeter**, or **Gatling** allow:
  - Simulation of **concurrent users**
  - Control over **request rate**
  - Measurement of **latency**, **error rate**, **throughput**, etc.
  - Generation of **performance reports**

This helps validate:

- Whether the app can **scale under load**
- If the system **meets latency thresholds**
- How **pods, services, and GKE autoscaling** respond under pressure

**Google Recommendation:**

"Before launching your application, use load testing tools to simulate expected workloads and verify that the application performs correctly under that load."
— Google Cloud: Testing application scalability

❌ **Why Other Options Are Incorrect:**

**B. Enable autoscaling and use `curl` to send requests**

- `curl` is **not a suitable load testing tool**.
- It simulates a **very small number of requests** and cannot replicate **tens of thousands of concurrent users**.
- Autoscaling should be part of the testing strategy, but you need a **proper load generator** to validate latency under real traffic.

**C. Deploy across multiple GKE clusters globally**

- This is a **scalability and availability strategy**, not a **testing method**.
- Global deployment helps with **geo-latency reduction**, but it does **not test or validate** latency under load.
- You must validate latency **before** global rollout using **controlled load testing**.

**D. Use Cloud Debugger to observe latency**

- Cloud Debugger is used to **inspect application state without stopping it**, typically for **debugging during development**.
- It does **not simulate traffic** or measure **request latency under load**.
- Not suitable for **performance testing**.

**Docs:** Cloud Debugger

✅ **Final Recommendation:**

Use a **load testing tool** to simulate anticipated traffic levels and measure latency. This is the most accurate and scalable way to validate system behavior before launch.

**⚠️ Note:** Cloud Debugger was shut down in 2023.

</details>

---

### Exam 3 · Q27

At DevSphere Inc., you’ve deployed a new application using **Anthos clusters (formerly Anthos GKE)**. As per your organization’s **Site Reliability Engineering (SRE)** practices, you are required to receive alerts if the **request latency** exceeds a defined threshold for a specific duration.

**What should you do to implement this requirement?**

- A. Install **Anthos Service Mesh** on your cluster. Use the **Google Cloud Console** to define a **Service Level Objective (SLO)**, and create an alerting policy based on the SLO.
- B. Enable the **Cloud Trace API** in your project, and configure **Cloud Monitoring Alerts** to trigger based on latency metrics from Cloud Trace.
- C. Use **Cloud Profiler** to monitor request latency. Define a custom metric in **Cloud Monitoring** using Profiler data, and set up an alerting policy that triggers if the threshold is exceeded.
- D. Set up **Anthos Config Management** on your cluster, and define an SLO and alerting policy using a YAML file that gets deployed to the cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Install **Anthos Service Mesh** on your cluster. Use the **Google Cloud Console** to define a **Service Level Objective (SLO)**, and create an alerting policy based on the SLO.

The correct answer is:
**A. Install Anthos Service Mesh on your cluster. Use the Google Cloud Console to define a Service Level Objective (SLO), and create an alerting policy based on the SLO.**

Justification for Correct Option (A):

- **Anthos Service Mesh (ASM)**, based on **Istio**, provides **observability features** including request latency, error rates, and availability metrics.
- ASM integrates with **Cloud Monitoring** and **Cloud Logging**, enabling you to define **Service Level Objectives (SLOs)** directly via the **Google Cloud Console**.
- You can then create **alerting policies** based on these SLOs to notify the team when **latency exceeds a predefined threshold** over a defined time window.
- This approach directly aligns with **SRE practices** for **proactive monitoring** and **reliability engineering**.

**Official Documentation:**

- Anthos Service Mesh Observability
- Create SLOs and alerting policies
- Create SLOs in Cloud Console

**Why Other Options Are Incorrect:**

B.

Enable the Cloud Trace API and configure Cloud Monitoring Alerts on latency metrics.

- While **Cloud Trace** provides **latency details**, it is not designed for **alerting** based on latency thresholds over time.
- Trace is **sampling-based**, so it **may not catch all high-latency requests**, making it unsuitable for **reliable SLO-based alerting**.

**Reference:**

- Cloud Trace Overview

C.

Use Cloud Profiler to monitor latency and define custom metrics.

- **Cloud Profiler** is used for **analyzing application performance at the code level** (CPU, heap usage) — **not request latency** or request-level observability.
- It does not emit latency metrics for creating **request-based alerting policies**.

**Reference:**

- Cloud Profiler Overview

D.

Use Anthos Config Management and define an SLO via YAML.

- **Anthos Config Management (ACM)** is used to enforce **policy-as-code**, config sync, and **RBAC controls**, not for defining SLOs or alerts.
- SLOs and alerts are configured via **Cloud Monitoring or the Cloud Console**, not ACM YAML manifests.

**Reference:**

- Anthos Config Management Overview

Final Answer: **A**

Because it uses **Anthos Service Mesh**, which provides **native observability**, **SLO definitions**, and **alerting integration** aligned with SRE best practices.

Link - [https://cloud.google.com/service-mesh/docs/observability/slo-overview](https://cloud.google.com/service-mesh/docs/observability/slo-overview)

**⚠️ Note:** Anthos clusters are now GKE Enterprise, Anthos Service Mesh is now Cloud Service Mesh, and Anthos Config Management is now Config Sync + Policy Controller.

</details>

---

### Exam 3 · Q35

Your company, **AppSphere Solutions**, runs a production application as a **Deployment in a Google Kubernetes Engine (GKE) cluster**. During **rolling deployments** of new versions, the team has been unintentionally causing **service outages**. The issue has been traced back to **misconfigured parameters** that are only present in the **production environment**.

You want to implement **preventive measures** within the platform to reduce the risk of such outages in the future.

**What should you do?**

- A.Set up **liveness and readiness probes** in the pod specifications to ensure Kubernetes routes traffic only to healthy pods.
- B.Configure **health checks** on the underlying **managed instance group**.
- C.Create a **Scheduled Task** to verify the application’s availability at regular intervals.
- D.Set up an **uptime check alert** in **Cloud Monitoring** to notify when the service becomes unavailable.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A.Set up **liveness and readiness probes** in the pod specifications to ensure Kubernetes routes traffic only to healthy pods.

The correct answer is:
**A. Set up liveness and readiness probes in the pod specifications to ensure Kubernetes routes traffic only to healthy pods.**

✅ Justification for Correct Option (A):

- **Liveness and readiness probes** are essential features in Kubernetes that allow the platform to:
  - **Detect unresponsive or misconfigured containers** (`livenessProbe`) and restart them automatically.
  - **Prevent routing traffic to containers that are not ready** to serve requests (`readinessProbe`), which is crucial during rolling updates.
- When rolling out a new version in GKE, Kubernetes replaces old pods with new ones. If the new pods are **misconfigured**, but no readiness probe is defined, traffic might be routed to these **unready** pods, causing **service outages**.
- Properly configured **readiness probes** prevent new, misconfigured pods from being added to the load balancer before they are fully ready.

This is the **Kubernetes-native and platform-recommended approach** to managing availability during rolling deployments.

**Official Documentation:**

- Kubernetes Probes: Liveness and Readiness
- Rolling Updates with Readiness Probes

❌ Why Other Options Are Incorrect:

B.

Configure health checks on the underlying managed instance group.

- GKE nodes run inside a **managed instance group (MIG)**, but configuring health checks at the MIG level **does not control Kubernetes pod traffic routing**.
- Kubernetes does not use MIG health checks for determining pod availability.

C.

Create a Scheduled Task to verify the application’s availability at regular intervals.

- A scheduled task (e.g., a cron job) could detect issues, but it is **reactive**, not **proactive**.
- It does not integrate with the rolling update mechanism and cannot prevent outages during deployment.

D.

Set up an uptime check alert in Cloud Monitoring.

- This provides **external alerting**, which is useful for monitoring, but **does not prevent traffic from being routed to failing pods**.
- It helps with **detection**, not **prevention**.

✅ Final Answer: **A**

Because **liveness and readiness probes** allow **Kubernetes to manage pod health intelligently**, ensuring that **only healthy pods receive traffic**, especially during **rolling updates**, thereby minimizing the risk of service disruption due to misconfiguration.

Hint:

[https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-creating-a-highly-available-gke-cluster](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-creating-a-highly-available-gke-cluster)

</details>

---

### Exam 3 · Q45

You are assisting the QA team at **NextGen Systems** in deploying a new load-testing tool to evaluate the scalability of key cloud services that run on **Google Compute Engine** and **Cloud Bigtable**.

Which **three** requirements should be included in the rollout plan? *(Choose three.)*

- A. Verify that the load tests measure and validate Cloud Bigtable’s performance
- B. Set up a separate Google Cloud project specifically for the load-testing environment
- C. Configure the load-testing tool to run periodically against the production environment
- D. Make sure all third-party services integrated with your application can handle increased traffic during load testing
- E. Update the production environment to log all transactions for replay during testing
- F. Add detailed logging and metrics to both the load-testing tool and the services being tested

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Verify that the load tests measure and validate Cloud Bigtable’s performance **|** B. Set up a separate Google Cloud project specifically for the load-testing environment **|** F. Add detailed logging and metrics to both the load-testing tool and the services being tested

The correct answers are:
**A. Verify that the load tests measure and validate Cloud Bigtable’s performance**
**B. Set up a separate Google Cloud project specifically for the load-testing environment**
**F. Add detailed logging and metrics to both the load-testing tool and the services being tested**

✅ Justification for Correct Answers:

**A. Verify that the load tests measure and validate Cloud Bigtable’s performance**

- The **main goal of load testing** is to understand how well services like **Cloud Bigtable** scale under pressure.
- You must design your test scenarios to **generate realistic workloads** that exercise **reads, writes, and schema usage**, and **validate throughput, latency, and CPU usage**.

**Reference:**
Cloud Bigtable performance tuning

**B. Set up a separate Google Cloud project specifically for the load-testing environment**

- Creating a **separate project** offers **resource isolation**, **billing segregation**, and **permissions control**.
- It ensures that load testing does **not affect production** or violate quota limits unexpectedly.

**Reference:**
Best practices for enterprise organizations

**F. Add detailed logging and metrics to both the load-testing tool and the services being tested**

- **Observability is essential**: you need metrics (CPU, latency, throughput) and logs to **identify bottlenecks** and verify expected behavior.
- Tools like **Cloud Monitoring**, **Cloud Logging**, and **Cloud Trace** help you **correlate test load with backend behavior**.

**Reference:**
Operations Suite overview

❌ Why the Other Options Are Incorrect:

**C. Configure the load-testing tool to run periodically against the production environment**

- This is risky. Running periodic load tests on **production** can cause **latency spikes, service degradation**, or **downtime**.
- Load tests should be conducted on **staging or mirrored environments**, unless the production environment is explicitly built to tolerate it.

**D. Make sure all third-party services integrated with your application can handle increased traffic during load testing**

- While important in **end-to-end system validation**, this is often **outside the scope** of internal service load testing.
- Many third-party services have **rate limits** and **cost implications**, and it's best to **mock or isolate** them during load tests.

**E. Update the production environment to log all transactions for replay during testing**

- Logging **all** transactions can lead to **performance degradation** and **high costs**.
- It’s better to use **representative synthetic data** or **sampled logs** for test replay scenarios.

✅ Final Answer:

**A.**, **B.**, and **F.**
These steps align with **Google Cloud best practices** for performance testing and help ensure **safe, effective, and observable load testing** of services like **Compute Engine and Cloud Bigtable**.

</details>

---

### Exam 3 · Q56

At **OpsBridge Corp.**, the operations team needs access to **logs from all production projects** within the Google Cloud Organization. These production projects are grouped under a specific **folder** in the organization structure. The goal is to **automatically collect logs from all current and future production projects**, without including logs from non-production projects.

What should you do to meet these requirements?

- A. Create an **aggregated log export** at the **Production folder** level. Set the **log sink** destination to a **Cloud Storage bucket** in a centralized operations project.
- B. Create an **aggregated log export** at the **Organization** level. Set the **log sink** destination to a **Cloud Storage bucket** in an operations project.
- C. Create **individual log exports** in each production project. Set the **log sinks** to write logs to a **Cloud Storage bucket** in the operations project.
- D. Create **log exports** in each production project that write to **BigQuery datasets** in the same projects. Grant the **operations team IAM access** to query these datasets.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create an **aggregated log export** at the **Production folder** level. Set the **log sink** destination to a **Cloud Storage bucket** in a centralized operations project.

✅ Correct Answer:

**A. Create an aggregated log export at the Production folder level. Set the log sink destination to a Cloud Storage bucket in a centralized operations project.**

✅ **Why Option A is Correct:**

- **Folder-level aggregated log sinks** automatically apply to **all projects within that folder**, including **future projects**.
- Since all **production projects** are grouped under one folder, exporting logs at the **folder level** precisely targets the required scope.
- **Aggregated log exports** can include logs from **child resources** (projects) within the folder.
- Exporting to a **centralized Cloud Storage bucket** in an operations project allows central visibility and management.

**Official Documentation:**

- Aggregated exports: Export logs for an entire folder
- Create and manage log sinks

❌ Why Other Options Are Incorrect:

**B. Organization-level log export**

- This exports **logs from all projects in the entire organization**, including **non-production** ones.
- Fails to meet the requirement to **exclude non-production logs**.
- Over-collects and can introduce **noise and compliance concerns**.

**C. Individual log exports in each production project**

- Requires **manual setup per project** and **manual updates** as new projects are added.
- **Does not scale** and **fails automation** requirement.
- Higher chance of **inconsistency or misconfiguration**.

**D. Export to BigQuery datasets in each project + IAM access**

- Again, requires **manual configuration per project**.
- Adds complexity with **IAM configuration on multiple datasets**.
- Harder to **centralize** visibility and maintain **long-term governance**.

✅ Final Answer:

**A. Create an aggregated log export at the Production folder level. Set the log sink destination to a Cloud Storage bucket in a centralized operations project.**

This satisfies all requirements: targeted, automated, scalable, and aligned with Google Cloud best practices.

</details>

---

### Exam 3 · Q62

You manage a **Compute Engine managed instance group** at **AppScale Corp.**, which automatically **scales instances up and down** based on application load. Each instance runs a **shutdown script** that is supposed to **clean up REDIS database entries** associated with that instance.

However, you've noticed that many REDIS entries remain after instance shutdowns, and you suspect the **shutdown script is not executing reliably**. To fix this, you've created a **Cloud Function** that can remove the REDIS entries.

What should you do next to **ensure reliable cleanup every time an instance is shut down**?

- A. Update the shutdown script to wait for 30 seconds before calling the Cloud Function.
- B. Discard the Cloud Function approach and instead modify the shutdown script to automatically retry if it doesn't complete within 30 seconds.
- C. Configure a **Cloud Monitoring log-based alert or sink** to **trigger the Cloud Function** whenever an **instance removal log entry** is detected in **Cloud Logging**.
- D. Change the shutdown script to **wait 30 seconds**, then **publish a message to a Pub/Sub topic**, triggering downstream cleanup.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Configure a **Cloud Monitoring log-based alert or sink** to **trigger the Cloud Function** whenever an **instance removal log entry** is detected in **Cloud Logging**.

✅ **Correct Answer:**

**C. Configure a Cloud Monitoring log-based alert or sink to trigger the Cloud Function whenever an instance removal log entry is detected in Cloud Logging.**

✅ **Why Option C is Correct:**

- When a Compute Engine VM in a MIG is deleted or terminated, a log entry is written to **Cloud Logging** (e.g., `"compute.instances.delete"` or `"compute.instances.shutdown"`).
- You can create a **log-based sink** or **alerting policy** that triggers a **Cloud Function** whenever such an event is logged.
- This approach is:
  - **Reliable** – works even if the shutdown script fails or times out
  - **Decoupled** – cleanup does not rely on the instance being healthy or responsive during shutdown
  - **Cloud-native** – aligns with **event-driven architecture** using **Cloud Logging + Cloud Functions**

**Official Docs:**

- Log-based alerts
- Triggering Cloud Functions from Cloud Logging

❌ **Why the Other Options Are Incorrect:**

**A. Update the shutdown script to wait for 30 seconds before calling the Cloud Function**

- Adding a delay **does not guarantee execution** of the shutdown script.
- If the instance is terminated abruptly or the script fails, the **Cloud Function won't be called**.
- **Still unreliable** for critical cleanup.

**B. Discard the Cloud Function and retry the shutdown script logic**

- Doubling down on the shutdown script **misses the root issue**: it's inherently unreliable in forceful shutdowns.
- Retry logic **within the instance** doesn’t help if the instance is gone before the script finishes.

**D. Change the shutdown script to wait 30 seconds, then publish a message to a Pub/Sub topic**

- Again, **relies on the shutdown script running correctly** and the instance surviving long enough.
- If shutdown is forceful, Pub/Sub message may **never be published**.

✅ **Final Answer:**

**C. Configure a Cloud Monitoring log-based alert or sink to trigger the Cloud Function whenever an instance removal log entry is detected in Cloud Logging.**

This solution ensures **reliable, event-driven cleanup** of REDIS entries, regardless of how or when the instance shuts down.

**⚠️ Note:** Strictly, the trigger is a Cloud Logging sink that routes the instance-removal audit log entry to Pub/Sub (or an Eventarc trigger on that audit log), which invokes the function. Cloud Functions is now Cloud Run functions.

</details>

---

### Exam 3 · Q65

You are responsible for managing several **internal applications running on Google Compute Engine** at **IntraTech Solutions**. Recently, some **business users** reported that one of the applications has become **significantly slower** over the last few days.

To troubleshoot and address the issue, what is the **first step** you should take?

- A. Check **Cloud Logging** and **Cloud Monitoring** to inspect logs and performance metrics from the Compute Engine instances.
- B. Upgrade the machine type for the Compute Engine instances to provide **more CPU and memory**.
- C. **Restore a backup** of the application’s database from a time when performance was not an issue.
- D. Redeploy the application using a **Managed Instance Group with autoscaling**, and place a **load balancer** in front of the group. Have users access the application through the load balancer's IP address.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Check **Cloud Logging** and **Cloud Monitoring** to inspect logs and performance metrics from the Compute Engine instances.

✅ Correct Answer:

**A. Check Cloud Logging and Cloud Monitoring to inspect logs and performance metrics from the Compute Engine instances.**

✅ **Why Option A is Correct:**

- **Cloud Monitoring** provides **metrics** like:
  - CPU utilization
  - Memory usage
  - Disk I/O
  - Network traffic
- **Cloud Logging** shows application logs and system logs, which may reveal:
  - Errors
  - Latency spikes
  - Unusual behavior

Using these tools allows you to:

- **Identify the root cause** before taking further action
- Make **data-driven decisions** on whether to scale, fix bugs, or reconfigure

This is the **recommended first step in the Google Cloud troubleshooting process**.

**Official Docs:**

- Cloud Monitoring Overview
- Cloud Logging Overview

❌ Why Other Options Are Incorrect:

**B. Upgrade the machine type for the Compute Engine instances**

- Premature optimization without knowing the root cause.
- Could increase cost without resolving the issue if it's not resource-related.

**C. Restore a backup of the application’s database**

- This action assumes a database corruption or data issue without confirmation.
- May result in **data loss** and **service disruption**.
- Not appropriate until you've **confirmed it's a DB issue**.

**D. Redeploy with Managed Instance Group and Load Balancer**

- This is a **scaling and high availability solution**, not a first troubleshooting step.
- Adds complexity and cost without confirming the cause of the slowdown.

✅ Final Answer:

**A. Check Cloud Logging and Cloud Monitoring to inspect logs and performance metrics from the Compute Engine instances.**

</details>

---

### Exam 4 · Q27

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

**Mountkirk Games' gaming servers are experiencing issues with automatic scaling, particularly after rolling out a highly popular new feature last month. Many users are encountering 503 errors and experiencing slow response times. What should they investigate as the first step?**

- A. Confirm the availability of the database.
- B. Ensure that the project quota hasn't been surpassed.
- C. Validate that the new feature code hasn't introduced any performance bugs.
- D. Verify that the load-testing team isn't running their tool against production.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Ensure that the project quota hasn't been surpassed.

The best immediate step is to

**B. Ensure that the project quota hasn't been surpassed.**

Here's why this gets priority, with considerations for other important checks:

**Why Quota is the Likely Culprit:**

- **Symptoms Match:** 503 errors and slow responses often occur when services hit resource limits imposed by quotas.
- **Feature Popularity:** The sudden surge in popularity due to the new feature indicates a likely increase in resource consumption, making hitting a quota the primary suspect.
- **Ease of Verification:** Checking the Google Cloud Console to view quota usage is a quick and decisive way to confirm or rule out this cause.

**Important Considerations for Other Options:**

- **A. Confirm the availability of the database:** A down database would certainly cause issues. However, 503 errors with *slow* response times suggest service bottlenecks rather than a completely offline resource. Checking quotas addresses a broader range of potential limits.
- **C. Validate new feature code:** Performance bugs are crucial to investigate but less likely the main cause of a sudden, massive increase in errors *immediately* after a popular new feature release.
- **D. Load-testing team:** This is a valid concern for ongoing performance issues, but not usually the primary cause of a sudden, massive spike in errors tied to user volume growth.

**What to Do Next:**

1. **Increase Quotas:** If the issue is indeed quota-related, temporarily increasing quotas can mitigate the immediate errors while the team performs root-cause analysis.
2. **Investigate Code/Architecture:** Even after increasing quotas, performance analysis to identify bottlenecks in the new feature or elsewhere is crucial for long-term scalability.
3. **Optimize Auto-Scaling:** Adjust auto-scaling rules (if applicable) for more aggressive responsiveness to changes in demand.

References:

[https://cloud.google.com/docs/quotahttps://developers.google.com/admin-sdk/alertcenter/guides/limits](https://cloud.google.com/docs/quota  https://developers.google.com/admin-sdk/alertcenter/guides/limits)

**⚠️ Note:** Quota is the bank's answer because the stem stresses autoscaling failures after sudden growth, and an exhausted quota stops the autoscaler from adding instances. A performance bug in the new feature (C) is also plausible.

</details>

---

### Exam 4 · Q41

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

**How should you establish service level indicators (SLIs) to assess the quality of new game versions running on Google Kubernetes Engine (GKE) from the user's viewpoint?**

- A. Establish CPU Utilization and Request Latency as service level indicators.
- B. Establish GKE CPU Utilization and Memory Utilization as service level indicators.
- C. Establish Request Latency and Error Rate as service level indicators.
- D. Establish Server Uptime and Error Rate as service level indicators.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Establish Request Latency and Error Rate as service level indicators.

The best approach to establish user-centric SLIs is:

**C. Establish Request Latency and Error Rate as service level indicators.**

Here's why this choice is optimal:

- **Focus on User Experience:** Request latency directly measures how long it takes for users' actions to receive a response from the game server. Error rate provides insight into how often users experience failures or unexpected behavior. These metrics directly impact the game's responsiveness and reliability from the user's point of view.
- **Actionable Metrics:** High latency or increased error rates indicate potential bottlenecks or issues within the game's infrastructure that need to be addressed to improve user experience.
- **Alignment with Business Goals:** Lower latency and reduced errors are key contributors to user retention and satisfaction, positively influencing Mountkirk Game's business requirements for improving uptime and reducing latency.

**Why Other Options Are Less Ideal:**

- **A. Establish CPU Utilization and Request Latency as service level indicators.** While CPU utilization is a helpful indicator of resource usage, it doesn't directly translate to user experience. High CPU utilization might point to potential performance issues, but could also mean efficient resource usage if the game can maintain low latency.
- **B. Establish GKE CPU Utilization and Memory Utilization as service level indicators.** These metrics are primarily focused on the health of the GKE infrastructure itself, and while they are important, they are more indirect indicators of user experience.
- **D. Establish Server Uptime and Error Rate as service level indicators.** Server uptime is important as downtime causes a complete loss of service, but it doesn't capture the nuances of degraded performance caused by high latency or partial errors throughout the user experience.

**Additional Considerations:**

- **SLI Thresholds:** Carefully define what constitutes "acceptable" latency and error rates for your specific game and audience.
- **Baseline Measurements:** Establish a performance baseline to compare against when new versions are released. This helps identify performance changes, both positive and negative.
- **Monitoring Tools:** Utilize monitoring tools that can track and measure request latency and error rates within your GKE environment.
- **Other Potential SLIs:** Consider supplementing latency and error rates with additional user-centric SLIs like:
  - **Apdex Score:** Measures overall user satisfaction based on response times.
  - **Custom Application-Specific Metrics:** Tailored to the specific gameplay actions.

References:

[https://sre.google/workbook/implementing-slos/](https://sre.google/workbook/implementing-slos/)

</details>

---

### Exam 4 · Q47

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

**In the context of the TerramEarth case study, where a legacy web application cannot be migrated to the cloud, what is the most reliable and cost-effective approach to building a cloud-native monitoring solution that ensures the URL points to a "Site is unavailable" page and notifies the Ops team promptly in case of downtime?**

- A. Develop a scheduled job in Cloud Run to trigger a container every minute. The container will inspect the application URL; if the application is inaccessible, it will switch the URL to the "Site is unavailable" page and notify the Ops team.
- B. Set up a cron job on a Compute Engine VM scheduled to run every minute. The cron job will execute a Python script to check the application URL status. Upon detecting downtime, it will switch the URL to the "Site is unavailable" page and notify the Ops team.
- C. Configure a Cloud Monitoring uptime check to monitor the application URL. Upon failure, publish a message to a Pub/Sub queue, triggering a Cloud Function to switch the URL to the "Site is unavailable" page and notify the Ops team.
- D. Utilize Cloud Error Reporting to monitor the application URL. In case of downtime, automatically switch the URL to the "Site is unavailable" page and notify the Ops team.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Configure a Cloud Monitoring uptime check to monitor the application URL. Upon failure, publish a message to a Pub/Sub queue, triggering a Cloud Function to switch the URL to the "Site is unavailable" page and notify the Ops team.

A breakdown of why option **C** is best, and why others are less suitable for TerramEarth's legacy web application monitoring:

**C. Configure a Cloud Monitoring uptime check to monitor the application URL. Upon failure, publish a message to a Pub/Sub queue, triggering a Cloud Function to switch the URL to the "Site is unavailable" page and notify the Ops team.**

- **Reliability:** Cloud Monitoring uptime checks are designed for robust monitoring with configurable intervals and failure thresholds. This aligns well with TerramEarth's need for prompt downtime detection.
- **Cloud-native Integration:** Seamless integration with Pub/Sub and Cloud Functions offers a scalable and event-driven solution, minimizing custom code dependencies.
- **Cost-Effectiveness:** Cloud Monitoring, Pub/Sub, and Cloud Functions have predictable and usage-based pricing. This solution avoids potentially idle VM resources, contributing to cost savings.
- **Manageability:** Centralized monitoring via Cloud Monitoring's interface simplifies managing alerts and configurations.

**Why Other Options Are Less Optimal:**

- **A. Develop a scheduled job in Cloud Run...** While Cloud Run offers scalability, managing a custom container adds overhead. Cloud Monitoring uptime checks provide a more focused and streamlined solution.
- **B. Set up a cron job on a Compute Engine VM...** This approach introduces unnecessary infrastructure management. VMs require maintenance (OS patch updates, etc.), increasing operational burden and potentially costs.
- **D. Utilize Cloud Error Reporting...** Cloud Error Reporting is primarily focused on error logging and analysis within applications, not uptime monitoring and URL switching.

**Additional Considerations**

- **URL Switching Mechanism:** Determine how the Cloud Function will switch the URL, whether through DNS manipulation, load balancer configuration, or another method.
- **Notifications:** Configure how the Cloud Function will alert the Ops team (email, SMS, or integration with an incident management system).

Hints:

[https://cloud.google.com/monitoring/uptime-checks?hl=enhttps://cloud.google.com/monitoring/api/resources?hl=en#tag_uptime_url https://cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane](https://cloud.google.com/monitoring/uptime-checks?hl=en  https://cloud.google.com/monitoring/api/resources?hl=en#tag_uptime_url   https://cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane)

**⚠️ Note:** Cloud Functions is now Cloud Run functions. The uptime check's alerting policy can use a Pub/Sub notification channel directly.

</details>

---

### Exam 4 · Q61

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**As your new game on Google Cloud enters public beta, you aim to establish meaningful service level objectives (SLOs) before its general availability. What approach should you take?**

- A. Set one SLO for 99.9% game server availability and another for less than 100-ms latency.
- B. Establish one SLO aligning with Google Cloud's availability and another targeting 100-ms latency.
- C. Define one SLO ensuring 99% of HTTP requests return the 2xx status code, and another for 99% of requests to complete within 100 ms.
- D. Define one SLO for the total uptime of the game server within a week and another for the mean response time of all HTTP requests under 100 ms.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Define one SLO ensuring 99% of HTTP requests return the 2xx status code, and another for 99% of requests to complete within 100 ms.

Here's the best approach for setting SLOs in this scenario:

**C. Define one SLO ensuring 99% of HTTP requests return the 2xx status code, and another for 99% of requests to complete within 100 ms.**

Let's break down why this is the most suitable choice:

- **Focus on User Experience:** HTTP request success (2xx status codes) and latency directly impact the player's experience. These metrics are strongly user-centric.
- **Beta Phase Considerations:** During the public beta, gathering data on user experience is crucial. These SLOs will provide valuable insights into areas for improvement before the full launch.

**Why other options are less optimal:**

- **A. Game Server Availability and Latency:** While important, these focus on infrastructure-level metrics rather than the direct user experience. A game server can be available but still provide a poor experience due to network issues or backend bottlenecks.
- **B. Aligning with Google Cloud Availability:** Doesn't address the specific performance expectations of your game. Google Cloud's availability might be higher, leading to an overconfident SLO that doesn't reflect the real player experience.
- **D. Uptime and Mean Response Time:** Uptime is a binary metric (up or down) and might not reveal nuanced performance issues. Mean response time can be skewed by outliers, not accurately reflecting the experience of most users.

**Important Considerations:**

- **Beta Feedback:** Use player feedback and monitoring data gathered during the beta phase to refine SLOs for the general availability launch.
- **SLIs:** Choose appropriate service level indicators (SLIs) to measure these SLOs – e.g., the proportion of successful HTTP requests, 95th percentile latency.

Hints- [https://landing.google.com/sre/workbook/chapters/implementing-slos/](https://landing.google.com/sre/workbook/chapters/implementing-slos/)

</details>

---

### Exam 5 · Q9

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

**For this question, refer to the Altostrat Media case study. Altostrat wants to evaluate the performance of its media processing pipeline running in a Java-based Cloud Run function. You must choose the most effective tool to carry out this analysis. What should you do?**

- A. Query the application logs in Cloud Logging.
- B. Analyze performance data using Cloud Profiler.
- C. Add instrumentation to the code to use Cloud Trace.
- D. Review runtime data with Snapshot Debugger.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Analyze performance data using Cloud Profiler.

**Correct option: B — Analyze performance data using Cloud Profiler**

Cloud Profiler is purpose-built for **continuous performance analysis** of production applications. It works natively with Java workloads and is designed to identify CPU usage, memory allocation patterns, and performance bottlenecks with minimal overhead. Since Altostrat wants to *evaluate the performance of a Java-based pipeline*, Profiler is the most effective and Google-recommended tool.

**Authoritative documentation:**
[https://cloud.google.com/profiler/docs](https://cloud.google.com/profiler/docs)

**Why B is correct**

- Provides **continuous CPU and memory profiling**
- Works directly with **Java applications**
- Designed for **performance optimization**, not just debugging
- Runs safely in production with low overhead
- Helps detect hot paths and inefficient code

This aligns exactly with the requirement: performance evaluation of a running pipeline.

**Why the other options are not the best choice**

A. Query logs in Cloud Logging
Logging is for **event tracking and troubleshooting**, not performance profiling. It does not reveal CPU hotspots or memory inefficiencies.

C. Add instrumentation to use Cloud Trace
Cloud Trace measures **request latency and distributed tracing**, which is useful for service timing analysis. However, it does not provide deep CPU/memory profiling like Cloud Profiler. Trace is about latency; Profiler is about performance bottlenecks.

D. Snapshot Debugger
Snapshot Debugger captures application state at specific execution points for debugging. It is not intended for continuous performance analysis.

**Need-to-know foundational concept**

Google Cloud observability tools serve different purposes:

- **Cloud Logging** → events and troubleshooting
- **Cloud Trace** → latency and request flow timing
- **Cloud Profiler** → CPU and memory performance analysis
- **Debugger/Snapshots** → runtime debugging

Exam principle:
If the question asks about **performance optimization of running code**, choose **Cloud Profiler**. If it asks about latency tracing, choose Cloud Trace.

###### Explanation

**Correct option: B — Analyze performance data using Cloud Profiler**

Cloud Profiler is purpose-built for **continuous performance analysis** of production applications. It works natively with Java workloads and is designed to identify CPU usage, memory allocation patterns, and performance bottlenecks with minimal overhead. Since Altostrat wants to *evaluate the performance of a Java-based pipeline*, Profiler is the most effective and Google-recommended tool.

> [!note]- Why the other options are wrong
> A. Query logs in Cloud Logging
> Logging is for **event tracking and troubleshooting**, not performance profiling. It does not reveal CPU hotspots or memory inefficiencies.
>
> C. Add instrumentation to use Cloud Trace
> Cloud Trace measures **request latency and distributed tracing**, which is useful for service timing analysis. However, it does not provide deep CPU/memory profiling like Cloud Profiler. Trace is about latency; Profiler is about performance bottlenecks.
>
> D. Snapshot Debugger
> Snapshot Debugger captures application state at specific execution points for debugging. It is not intended for continuous performance analysis.

</details>

---

### Exam 5 · Q31

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

**For this question, refer to the KnightMotives Automotive case study. KnightMotives has deployed a Vertex AI model that delivers personalized option recommendations in its car configurator. The model was trained using historical customer behavior data. You know that customer preferences evolve over time — for example, buyers may choose more premium options during strong economic periods. You want to detect gradual shifts in real-world behavior so the model can be adjusted accordingly. What should you do?**

- A. Configure Vertex AI Model Monitoring and enable training–serving skew detection.
- B. Configure Vertex AI Model Monitoring and enable prediction drift detection.
- C. Enable Dataplex auto data quality checks on prediction request features using row-level rules.
- D. Enable Dataplex auto data quality checks on prediction request features using aggregate rules.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure Vertex AI Model Monitoring and enable prediction drift detection.

**Correct answer: B**

Configure Vertex AI Model Monitoring and enable **prediction drift detection**.

**Authoritative documentation link:**
[https://cloud.google.com/vertex-ai/docs/model-monitoring/overview](https://cloud.google.com/vertex-ai/docs/model-monitoring/overview)

**Why option B is correct**

The problem describes **gradual behavioral change in real-world customer preferences** after deployment. That is the textbook definition of **prediction drift**:

The distribution of live production inputs changes significantly over time.

Prediction drift monitoring compares:

- the feature distribution of recent prediction requests
  vs
- the feature distribution of earlier prediction requests

(Comparing production inputs against the training data is training–serving skew.)

and alerts when statistically significant change occurs.

This is exactly what you want when:

- user behavior evolves
- market conditions change
- economic cycles influence decisions
- model relevance degrades over time

Detecting drift allows retraining before model performance collapses.

**Why the other options are not the best choice**

**A. Training–serving skew detection**

Skew detects **pipeline bugs**, not behavior change.

Example skew cases:

- feature engineered differently in training vs serving
- missing columns
- encoding mismatch
- transformation errors

The question is about *real-world preference shifts*, not data pipeline defects.

**C. Dataplex row-level rules**

Row-level quality checks validate individual records (nulls, ranges, formats). They ensure data correctness, not distribution change over time.

They answer: “Is this record valid?”
not
“Has user behavior shifted?”

**D. Dataplex aggregate rules**

Aggregate rules summarize dataset quality (counts, averages, completeness). Still data validation — not model drift detection.

They monitor data hygiene, not ML behavior evolution.

**Need-to-know foundational concept**

There are three different ML monitoring problems:

Training-serving skew → pipeline bug
Prediction drift → behavior change
Data quality → correctness/validity

Only **prediction drift** detects:

- changing customer preferences
- economic shifts
- seasonality effects
- real-world distribution movement

This is a core lifecycle concept in production ML systems:
models fail silently when the world changes. Drift monitoring is how you catch it early.

###### Explanation

**Why option B is correct**

The problem describes **gradual behavioral change in real-world customer preferences** after deployment. That is the textbook definition of **prediction drift**:

The distribution of live production inputs changes significantly over time.

Prediction drift monitoring compares:

- the feature distribution of recent prediction requests
  vs
- the feature distribution of earlier prediction requests

(Comparing production inputs against the training data is training–serving skew.)

and alerts when statistically significant change occurs.

This is exactly what you want when:

- user behavior evolves
- market conditions change
- economic cycles influence decisions
- model relevance degrades over time

Detecting drift allows retraining before model performance collapses.

> [!note]- Why the other options are wrong
> **A. Training–serving skew detection**
>
> Skew detects **pipeline bugs**, not behavior change.
>
> Example skew cases:
>
> - feature engineered differently in training vs serving
> - missing columns
> - encoding mismatch
> - transformation errors
>
> The question is about *real-world preference shifts*, not data pipeline defects.
>
> **C. Dataplex row-level rules**
>
> Row-level quality checks validate individual records (nulls, ranges, formats). They ensure data correctness, not distribution change over time.
>
> They answer: “Is this record valid?”
> not
> “Has user behavior shifted?”
>
> **D. Dataplex aggregate rules**
>
> Aggregate rules summarize dataset quality (counts, averages, completeness). Still data validation — not model drift detection.
>
> They monitor data hygiene, not ML behavior evolution.

**⚠️ Note:** Dataplex Universal Catalog is now Knowledge Catalog (April 2026); its data quality scans still validate data, not model drift.

</details>

---

### Exam 5 · Q41

**Your organization stores a large volume of log data in **Cloud Logging**. The data engineering team prefers using **SQL** for analysis and wants to build meaningful dashboards to visualize log trends and patterns. You want to implement a solution aligned with the **Google Cloud Well-Architected Framework** recommendations to support this need. What should you do?**

- A. Create a log sink and export logs to **BigQuery** through **Pub/Sub**. Query the data and build visualizations using **Cloud Monitoring dashboards**.
- B. Enable **log analytics**, run queries in **Cloud Monitoring**, and visualize results using **Vertex AI Workbench**.
- C. Enable **log analytics**, query the **linked log dataset in BigQuery**, and create dashboards using **Looker Studio**.
- D. Create a log sink and export logs to a **Cloud Storage bucket**. Create a **BigQuery external table** over the bucket data, then query and visualize using **Cloud Monitoring dashboards**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Enable **log analytics**, query the **linked log dataset in BigQuery**, and create dashboards using **Looker Studio**.

**Correct Answer: C**

**Enable Log Analytics, query the linked log dataset in BigQuery, and create dashboards using Looker Studio.**

**Why C is correct**

**This option best matches all requirements:**

- **SQL-based analysis**: Log Analytics makes logs queryable using **BigQuery SQL**.
- **Meaningful dashboards**: **Looker Studio** is the most direct, scalable, and user-friendly dashboarding tool for BigQuery datasets.
- **Well-Architected alignment**: Using managed, integrated services (Cloud Logging → BigQuery SQL → Looker Studio) supports operational excellence and observability best practices without building unnecessary ingestion pipelines.

This gives you:

- near-real-time analysis capability
- strong querying flexibility
- shareable dashboards for business and engineering users

**Why the other options are incorrect / not best fit**

**A. Export logs to BigQuery through Pub/Sub + Monitoring dashboards**

**Not best because:**

- Cloud Logging can export directly to BigQuery via a sink; Pub/Sub adds complexity.
- Cloud Monitoring dashboards are not the primary BI/dashboard tool for BigQuery log analytics.

**B. Log analytics + Cloud Monitoring queries + Vertex AI Workbench**

**Not best because:**

- Vertex AI Workbench is for notebooks/ML workflows, not dashboarding.
- Cloud Monitoring is not the standard place for SQL log trend dashboards.

D. Export to Cloud Storage + external table + Monitoring dashboards

**Not best because:**

- Adds extra steps and higher operational overhead.
- External tables are generally slower and less optimized than native BigQuery tables.
- Monitoring dashboards still aren’t ideal for SQL-based BI-style reporting.

**Need-to-know fundamentals**

- **Log Analytics** provides a BigQuery-backed dataset for log exploration using SQL.
- **Looker Studio** is a natural choice for dashboarding BigQuery data.
- Avoid building custom pipelines (Pub/Sub → BigQuery) unless you need advanced routing, enrichment, or multi-destination streaming.

**Official documentation link**

Log Analytics for Cloud Logging (BigQuery-powered SQL querying):
[https://cloud.google.com/logging/docs/log-analytics](https://cloud.google.com/logging/docs/log-analytics)

###### Explanation

**Correct Answer: C**

**Enable Log Analytics, query the linked log dataset in BigQuery, and create dashboards using Looker Studio.**

Why C is correct

This option best matches all requirements:

- **SQL-based analysis**: Log Analytics makes logs queryable using **BigQuery SQL**.
- **Meaningful dashboards**: **Looker Studio** is the most direct, scalable, and user-friendly dashboarding tool for BigQuery datasets.
- **Well-Architected alignment**: Using managed, integrated services (Cloud Logging → BigQuery SQL → Looker Studio) supports operational excellence and observability best practices without building unnecessary ingestion pipelines.

This gives you:

- near-real-time analysis capability
- strong querying flexibility
- shareable dashboards for business and engineering users

> [!note]- Why the other options are wrong
> A. Export logs to BigQuery through Pub/Sub + Monitoring dashboards
>
> Not best because:
>
> - Cloud Logging can export directly to BigQuery via a sink; Pub/Sub adds complexity.
> - Cloud Monitoring dashboards are not the primary BI/dashboard tool for BigQuery log analytics.
>
> B. Log analytics + Cloud Monitoring queries + Vertex AI Workbench
>
> Not best because:
>
> - Vertex AI Workbench is for notebooks/ML workflows, not dashboarding.
> - Cloud Monitoring is not the standard place for SQL log trend dashboards.
>
> D. Export to Cloud Storage + external table + Monitoring dashboards
>
> Not best because:
>
> - Adds extra steps and higher operational overhead.
> - External tables are generally slower and less optimized than native BigQuery tables.
> - Monitoring dashboards still aren’t ideal for SQL-based BI-style reporting.

**⚠️ Note:** Looker Studio was renamed back to Data Studio in April 2026.

</details>

---

### Exam 5 · Q49

**You are responsible for several hundred Ubuntu and Red Hat Enterprise Linux VMs running on Google Compute Engine (GCE). You need a secure, scalable approach to periodically patch the operating systems across these instances. What should you do?**

- A. Create a **Cloud Scheduler** job that runs a Bash script to securely connect to each VM and apply OS patches.
- B. Configure **Config Sync**, install the **Ops Agent** on every VM, and schedule a patch job to apply patches on each VM.
- C. Schedule a **Cloud Build** job and use **Cloud Deploy** to run a patch process that applies patches across the VMs.
- D. Use **VM Manager**, install the **OS Config agent** on each VM, and schedule a patch job to apply patches on each VM.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use **VM Manager**, install the **OS Config agent** on each VM, and schedule a patch job to apply patches on each VM.

**Correct Answer: D**

**Use VM Manager, install the OS Config agent on each VM, and schedule a patch job to apply patches on each VM.**

**Why D is correct**

For **hundreds of Ubuntu and RHEL VMs on Compute Engine**, the Google-recommended, secure, and scalable approach is:

- **VM Manager (part of OS Config)**
- **OS Config agent installed on each VM**
- Use **Patch jobs** to schedule and automate OS patching across fleets

This provides:

- centralized patch orchestration
- controlled rollout and scheduling
- reporting/compliance visibility
- secure management without manually SSH-ing into VMs

**Official documentation:**
[https://docs.cloud.google.com/compute/vm-manager/docs/setup](https://docs.cloud.google.com/compute/vm-manager/docs/setup)

**Why the other options are incorrect / not best fit**

**A. Cloud Scheduler + Bash + SSH into each VM**

Not scalable and not secure at scale:

- hard to manage credentials/keys
- brittle and error-prone
- no centralized compliance reporting

**B. Config Sync + Ops Agent + patch job**

Config Sync is for GKE configuration management, not VM OS patching. Ops Agent is for logging/monitoring, not patch management.

**C. Cloud Build + Cloud Deploy for patching VMs**

Cloud Deploy is for application delivery to targets like GKE/Cloud Run, not OS patching on VM fleets.

**Need-to-know fundamentals**

- **OS patching on GCE at scale = OS Config / VM Manager patch jobs**
- Works for **Ubuntu and RHEL**
- Gives scheduling + audit visibility + controlled rollouts

###### Explanation

**Why D is correct**

For **hundreds of Ubuntu and RHEL VMs on Compute Engine**, the Google-recommended, secure, and scalable approach is:

- **VM Manager (part of OS Config)**
- **OS Config agent installed on each VM**
- Use **Patch jobs** to schedule and automate OS patching across fleets

This provides:

- centralized patch orchestration
- controlled rollout and scheduling
- reporting/compliance visibility
- secure management without manually SSH-ing into VMs

> [!note]- Why the other options are wrong
> A. Cloud Scheduler + Bash + SSH into each VM
>
> Not scalable and not secure at scale:
>
> - hard to manage credentials/keys
> - brittle and error-prone
> - no centralized compliance reporting
>
> B. Config Sync + Ops Agent + patch job
>
> Config Sync is for GKE configuration management, not VM OS patching. Ops Agent is for logging/monitoring, not patch management.
>
> C. Cloud Build + Cloud Deploy for patching VMs
>
> Cloud Deploy is for application delivery to targets like GKE/Cloud Run, not OS patching on VM fleets.

</details>

---

### Exam 5 · Q54

**You are running an application that uses Vertex AI Feature Store to serve product features for real-time recommendations. You want visibility into system health and specifically need to understand how long a request takes from start to finish. What should you monitor?**

- A. Observe the request size in Feature Store.
- B. Monitor queries per second for Feature Store.
- C. Measure request latency.
- D. Track online serving throughput.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Measure request latency.

**Correct option: C. Measure request latency.**

**Need-to-know foundational concept**
For real-time systems like Vertex AI Feature Store online serving, the most direct indicator of system *performance* and *responsiveness* is latency — the time taken for a request to be processed from start to finish. Latency reflects how quickly a feature fetch operation completes, which directly impacts downstream inference and user experience. It is one of the core “golden signals” recommended by SRE and observability practices for tracking service health (alongside error rate and traffic). Monitoring latency lets you detect performance degradation (e.g., backend contention, lack of capacity, scaling issues) early and set appropriate alerts.

Vertex AI Feature Store emits request latency metrics to Cloud Monitoring so you can observe how long feature lookups are taking in real time. Metrics include latencies of online serving operations which you can visualize or alert on in dashboards.

**Google documents that Vertex AI serving metrics include request latency for monitoring system performance:**

[https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring)

**Why this option is correct**
Request latency measures the end-to-end time taken to complete a serve request, exactly what the question asks for: “how long a request takes from start to finish.” This is the metric you’d watch to assess responsiveness and to detect slowdowns during real-time serving.

**Why the other options are not suitable**

**A. Observe the request size in Feature Store.**
Request size tells you about how much data is being sent or received, but it does not measure *performance* or *duration*. Large or small requests alone don’t indicate how long processing takes.

**B. Monitor queries per second for Feature Store.**
Queries per second (QPS) represents *traffic volume*, not latency. A high QPS rate does not necessarily mean slow responses, and it does not directly tell you how long each request takes.

**D. Track online serving throughput.**
Throughput (e.g., number of served requests per time period) measures capacity, not the *time per request*. You could have good throughput but poor latency if requests are slow.

Monitoring request latency gives you the precise visibility into end-to-end timing needed for real-time recommendation performance assessments.

###### Explanation

**Why this option is correct**
Request latency measures the end-to-end time taken to complete a serve request, exactly what the question asks for: “how long a request takes from start to finish.” This is the metric you’d watch to assess responsiveness and to detect slowdowns during real-time serving.

> [!note]- Why the other options are wrong
> **A. Observe the request size in Feature Store.**
> Request size tells you about how much data is being sent or received, but it does not measure *performance* or *duration*. Large or small requests alone don’t indicate how long processing takes.
>
> **B. Monitor queries per second for Feature Store.**
> Queries per second (QPS) represents *traffic volume*, not latency. A high QPS rate does not necessarily mean slow responses, and it does not directly tell you how long each request takes.
>
> **D. Track online serving throughput.**
> Throughput (e.g., number of served requests per time period) measures capacity, not the *time per request*. You could have good throughput but poor latency if requests are slow.

</details>

---

### Exam 5 · Q80

**Your company operates a mission-critical ecommerce application served by a regional managed instance group (MIG) behind an external HTTP(S) Load Balancer. The operations team is overloaded with low-value alerts and is beginning to ignore notifications. Your service level objective (SLO) is 99.9% availability, measured as the ratio of successful requests (HTTP 2xx) to total requests. You want to reduce alert noise and ensure the team is only paged for actionable issues that put the SLO at risk. What should you do?**

- A. Use cause-based alerting by setting thresholds on Compute Engine instance metrics such as CPU utilization, memory usage, disk I/O, and network throughput.
- B. Create log-based alerting on all WARN and ERROR application log entries so that potential problems are always detected.
- C. Define an error budget policy tied to the availability SLO, and create a paging alert that triggers only when the error budget burn rate indicates the budget will be fully consumed within the next 24 hours.
- D. Use predictive alerting and trigger notifications primarily based on the MIG instance count metric.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Define an error budget policy tied to the availability SLO, and create a paging alert that triggers only when the error budget burn rate indicates the budget will be fully consumed within the next 24 hours.

**Correct option: C. Define an error budget policy tied to the availability SLO, and create a paging alert that triggers only when the error budget burn rate indicates the budget will be fully consumed within the next 24 hours.**

**Need-to-know foundational concept**

This question is testing **SRE alerting philosophy**.

When you define an SLO, the correct alerting strategy is:

Alert on **user-visible impact**, not infrastructure symptoms.

An SLO of 99.9% availability means you already have a quantitative reliability target. The right signal is the **error budget burn rate**, which tells you how quickly you are consuming your allowed failure margin. Paging should happen only when the SLO is truly at risk — not for every transient CPU spike or warning log.

Google’s SRE guidance explicitly recommends **burn-rate alerting tied to SLOs** to reduce noise and focus teams on actionable reliability risks:
[https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate)

**Why option C is correct**

Option C:

- aligns alerts with the SLO definition
- measures user-facing availability (2xx success ratio)
- pages only when reliability is threatened
- eliminates low-value noise
- preserves operator attention
- follows Google SRE best practices

This ensures the team is paged only when the service is truly degrading in a way customers feel.

**Why the other options are not the best choice**

**A. Infrastructure metric thresholds**
CPU and memory spikes don’t necessarily affect user experience. These are cause-based alerts, not SLO-based alerts.

**B. Log-based WARN/ERROR alerts**
This floods operators with noise. Many warnings are benign and unrelated to availability.

**D. MIG instance count alerts**
Instance count changes are not a direct measure of service availability and can trigger false alarms.

Exam principle:

Alert on SLO impact, not infrastructure symptoms.

**Final answer: C**

###### Explanation

**Correct option: C**

**Need-to-know foundational concept**

This question is testing **SRE alerting philosophy**.

When you define an SLO, the correct alerting strategy is:

Alert on **user-visible impact**, not infrastructure symptoms.

An SLO of 99.9% availability means you already have a quantitative reliability target. The right signal is the **error budget burn rate**, which tells you how quickly you are consuming your allowed failure margin. Paging should happen only when the SLO is truly at risk — not for every transient CPU spike or warning log.

**Why option C is correct**

Option C:

- aligns alerts with the SLO definition
- measures user-facing availability (2xx success ratio)
- pages only when reliability is threatened
- eliminates low-value noise
- preserves operator attention
- follows Google SRE best practices

> [!note]- Why the other options are wrong
> **A. Infrastructure metric thresholds**
> CPU and memory spikes don’t necessarily affect user experience. These are cause-based alerts, not SLO-based alerts.
>
> **B. Log-based WARN/ERROR alerts**
> This floods operators with noise. Many warnings are benign and unrelated to availability.
>
> **D. MIG instance count alerts**
> Instance count changes are not a direct measure of service availability and can trigger false alarms.

</details>

---

### Exam 5 · Q81

**You operate a large hybrid and multi-cloud environment where developers depend heavily on Prometheus. You want a managed, cloud-hosted solution that scales easily, requires minimal maintenance, supports PromQL queries, and allows fast metric exploration and troubleshooting. What should you do?**

- A. Deploy a Prometheus Operator across your Kubernetes and serverless environments in each cloud.
- B. Use Cloud Monitoring as a centralized observability dashboard across your multi-cloud estate.
- C. Enable Google Cloud Managed Service for Prometheus to collect, query, and alert on metrics at scale.
- D. Build a custom SaaS platform compatible with Prometheus to aggregate and visualize metrics from each cloud.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Enable Google Cloud Managed Service for Prometheus to collect, query, and alert on metrics at scale.

**Correct option:** **C. Enable Google Cloud Managed Service for Prometheus to collect, query, and alert on metrics at scale.**

**Need-to-know foundational concept**

The requirement is a **managed Prometheus-compatible backend** that removes operational burden while preserving developer workflows. Google’s Managed Service for Prometheus is designed specifically for this use case: it is a fully managed metrics backend that supports Prometheus scraping and **PromQL querying**, while automatically scaling and integrating with Cloud Monitoring for dashboards and alerting.
[https://cloud.google.com/stackdriver/docs/managed-prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus)

This allows teams to keep using Prometheus tools and queries without running or maintaining Prometheus infrastructure.

**Why the chosen option is correct**

- Fully managed → minimal maintenance
- PromQL-compatible → no retraining developers
- Built for large-scale environments → hybrid and multi-cloud ingestion supported
- Integrated exploration and alerting → fast troubleshooting
- Removes infrastructure burden of running Prometheus servers

It matches every requirement in the question.

**Why the other options are not the best choice**

**A. Prometheus Operator everywhere**
Still self-managed. You must run, scale, upgrade, and troubleshoot Prometheus clusters across environments.

**B. Cloud Monitoring only**
While powerful, it is not a PromQL-native Prometheus backend. Developers depend specifically on Prometheus tooling and query model.

**D. Custom SaaS platform**
Rebuilding what Google already provides introduces unnecessary engineering and operational risk.

Final answer: **C**

###### Explanation

**Correct option:** **C.**

**Need-to-know foundational concept**

The requirement is a **managed Prometheus-compatible backend** that removes operational burden while preserving developer workflows. Google’s Managed Service for Prometheus is designed specifically for this use case: it is a fully managed metrics backend that supports Prometheus scraping and **PromQL querying**, while automatically scaling and integrating with Cloud Monitoring for dashboards and alerting.

**Why the chosen option is correct**

- Fully managed → minimal maintenance
- PromQL-compatible → no retraining developers
- Built for large-scale environments → hybrid and multi-cloud ingestion supported
- Integrated exploration and alerting → fast troubleshooting
- Removes infrastructure burden of running Prometheus servers

> [!note]- Why the other options are wrong
> **A. Prometheus Operator everywhere**
> Still self-managed. You must run, scale, upgrade, and troubleshoot Prometheus clusters across environments.
>
> **B. Cloud Monitoring only**
> While powerful, it is not a PromQL-native Prometheus backend. Developers depend specifically on Prometheus tooling and query model.
>
> **D. Custom SaaS platform**
> Rebuilding what Google already provides introduces unnecessary engineering and operational risk.

</details>

---

### Exam 5 · Q85

**You are monitoring Google Kubernetes Engine (GKE) clusters in a Cloud Monitoring workspace. As a Site Reliability Engineer (SRE), you need to triage incidents as quickly as possible. What should you do?**

- A. Use the predefined dashboards in the Cloud Monitoring workspace. Add relevant metrics and configure alerting policies.
- B. Create a shell script that collects metrics from GKE nodes and publishes them to Pub/Sub. Export the data to BigQuery and visualize it in a Data Studio dashboard.
- C. Build a new custom dashboard in Cloud Monitoring for each incident. Add metrics and configure alerting policies.
- D. Use the predefined dashboards in Cloud Monitoring. Create custom metrics and deploy separate alerting software on a Compute Engine VM.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use the predefined dashboards in the Cloud Monitoring workspace. Add relevant metrics and configure alerting policies.

**Correct option: A**

**Need-to-know foundational concept**

SRE incident response is about **speed and signal clarity**, not building tooling during an outage.

Google Cloud Monitoring provides **predefined GKE dashboards** that already surface the most important cluster health signals. Best practice is to start with curated dashboards and layer alerting on top of relevant SLO/SRE metrics. This avoids reinventing observability infrastructure and reduces incident triage time.

**Predefined dashboards are designed for fast operational insight:**
[https://cloud.google.com/monitoring/dashboards/predefined-dashboards](https://cloud.google.com/monitoring/dashboards/predefined-dashboards)

**Why option A is correct**

Option A aligns with SRE principles:

- Use existing curated dashboards → instant visibility
- Add relevant metrics → tailor to workload
- Configure alerts → proactive detection
- No custom infrastructure required
- Minimal operational overhead
- Fastest path to incident triage

You’re enhancing a supported system, not replacing it.

**Why the other options are not the best choice**

**B. Script + Pub/Sub + BigQuery + Data Studio**
Over-engineered, slow, and introduces unnecessary complexity. Not suitable for rapid incident response.

**C. Build dashboards during incidents**
Too late. Observability must exist before incidents happen.

**D. Separate alerting software on VMs**
Adds maintenance burden and duplicates Cloud Monitoring capabilities.

Exam principle:

**Use managed observability first; customize only what’s needed.**

**Final answer: A**

###### Explanation

**Correct option: A**

**Need-to-know foundational concept**

SRE incident response is about **speed and signal clarity**, not building tooling during an outage.

Google Cloud Monitoring provides **predefined GKE dashboards** that already surface the most important cluster health signals. Best practice is to start with curated dashboards and layer alerting on top of relevant SLO/SRE metrics. This avoids reinventing observability infrastructure and reduces incident triage time.

**Why option A is correct**

Option A aligns with SRE principles:

- Use existing curated dashboards → instant visibility
- Add relevant metrics → tailor to workload
- Configure alerts → proactive detection
- No custom infrastructure required
- Minimal operational overhead
- Fastest path to incident triage

> [!note]- Why the other options are wrong
> **B. Script + Pub/Sub + BigQuery + Data Studio**
> Over-engineered, slow, and introduces unnecessary complexity. Not suitable for rapid incident response.
>
> **C. Build dashboards during incidents**
> Too late. Observability must exist before incidents happen.
>
> **D. Separate alerting software on VMs**
> Adds maintenance burden and duplicates Cloud Monitoring capabilities.

**⚠️ Note:** Cloud Monitoring "workspaces" have been replaced by metrics scopes.

</details>

---
