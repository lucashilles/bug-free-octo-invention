# Professional Cloud Architect — Practice Exam 2

62 questions.

## Question 1

*Domain 5: Managing Implementation*

**You are developing an App Engine application that uses Cloud Datastore as its persistence layer. You need to retrieve multiple root entities using their identifiers while minimizing the operational overhead in Cloud Datastore.**

**What should you do?**

- [x] A. Create a **Key object** for each entity and perform a **batch get operation**.
- [ ] B. Create a **Key object** for each entity and run **multiple get operations**, one per entity.
- [ ] C. Use the **identifiers** to create a **query filter** and execute a **batch query operation**.
- [ ] D. Use the **identifiers** to create a **query filter** and run **multiple query operations**, one per entity.

### Explanation

**Correct Answer:**

✅ **A. Create a Key object for each entity and perform a batch get operation.**

**Explanation:**

When retrieving **multiple root entities by their identifiers** in **Cloud Datastore**, the most efficient way is to use a **batch get operation** with **Key objects**.

✅ **Why Batch Get with Key Objects?**

- **Efficient retrieval:** A batch get operation retrieves multiple entities in a **single request**, reducing **latency** and **operational overhead**.
- **Cost-effective:** **Uses fewer Datastore read operations** than running separate queries for each entity.
- **Optimized for indexed lookups:** Fetching by **Key object** is **faster** than querying with filters.

**Implementation in Python (Example):**

```
from google.cloud import datastore client = datastore.Client() # List of entity keyskeys = [    client.key('Employee', 101),    client.key('Employee', 102),    client.key('Employee', 103)] # Perform batch get operationemployees = client.get_multi(keys) # Process retrieved entitiesfor employee in employees:    print(employee)
```

✅ **Supporting Documentation:**

- **Batch Get Operations in Cloud Datastore:**
  **https://cloud.google.com/datastore/docs/concepts/entities#retrieving_entities**

**Why Other Options Are Incorrect?**

**B. Create a Key object for each entity and run multiple get operations, one per entity.** ❌

- **Less efficient** because it makes **multiple separate API calls** instead of a **single batch request**.
- **Higher latency and operational overhead** compared to batch get.

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/concepts/entities#retrieving_entities**

**C. Use the identifiers to create a query filter and execute a batch query operation.** ❌

- **Datastore queries are not optimized for lookups by key**—queries require scanning indexes, which is slower.
- **Using Keys directly is much more efficient.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/concepts/queries**

**D. Use the identifiers to create a query filter and run multiple query operations, one per entity.** ❌

- **Running multiple queries is inefficient**, leading to **higher read costs and increased API latency**.
- **A batch get operation using Keys is significantly faster** than filtering by identifiers in queries.

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/concepts/queries**

**Conclusion:**

The best approach is **A. Create a Key object for each entity and perform a batch get operation**, because:
✔ **Retrieves multiple entities efficiently in a single request**.
✔ **Reduces operational overhead and API latency**.
✔ **Optimized for indexed lookups in Cloud Datastore**.

📌 **Final Reference:**
**https://cloud.google.com/datastore/docs/concepts/entities#retrieving_entities**

---

## Question 2

*Domain 3: Designing for Security and Compliance*

**You need to upload files from your on-premises environment to Cloud Storage while ensuring that the files are encrypted using customer-supplied encryption keys (CSEK).**

**What should you do?**

- [x] A. Specify the **encryption key** in a **.boto configuration file** and use **gsutil** to upload the files.
- [ ] B. Configure the **encryption key** using **gcloud config**, then use **gsutil** to upload the files to the bucket.
- [ ] C. Use **gsutil** to upload the files and provide the encryption key using the `--encryption-key` flag.
- [ ] D. Use **gsutil** to create a bucket with the `--encryption-key` flag, then upload the files to that bucket using **gsutil**.

### Explanation

Correct Answer: **A**

**Specify the encryption key in a `.boto` configuration file and use gsutil to upload the files.**

Why option A is correct

For **customer-supplied encryption keys (CSEK)**, **gsutil does not support a `--encryption-key` flag** for `cp` or `mv`.

Instead, gsutil looks for CSEK configuration in the `.boto` **file**, where encryption keys are supplied via specific settings. When properly configured, gsutil automatically includes the required encryption headers during object upload.

Example `.boto` configuration:

```
[GSUtil]encryption_key = <base64-encoded-key>
```

This is the **only supported and documented mechanism** for using CSEK with gsutil uploads from an on-premises environment.

Official documentation:
[https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#gsutil](https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#gsutil)

Why the other options are incorrect

**Option B**
`gcloud config` does not support configuring customer-supplied encryption keys for Cloud Storage. CSEK is not a project-level or CLI-level setting.

Documentation:
[https://cloud.google.com/storage/docs/encryption](https://cloud.google.com/storage/docs/encryption)

**Option C**
Incorrect because **gsutil does not provide a `--encryption-key` flag** for `cp` or `mv`. CSEK handling is done via headers derived from `.boto` configuration, not command-line flags.

Documentation:
[https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#gsutil](https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#gsutil)

**Option D**
Incorrect because **CSEK cannot be applied at the bucket level**. Customer-supplied keys apply only to individual objects at upload or access time, not during bucket creation.

Documentation:
[https://cloud.google.com/storage/docs/encryption#encryption_keys](https://cloud.google.com/storage/docs/encryption#encryption_keys)

Key takeaway

With **gsutil + CSEK**:

- Encryption keys are **object-level**, not bucket-level
- Keys are **not passed via CLI flags**
- Keys must be configured in the `.boto` **file**
- gsutil automatically injects the required encryption headers

This makes **Option A** the only correct and fully supported solution.

**⚠️ Note:** gsutil is now legacy. With the current `gcloud storage cp`, you pass a customer-supplied key with the `--encryption-key` flag. For gsutil, the `.boto` file is still the way.

---

## Question 3

*Domain 6: Ensuring Solution and Operations Excellence*

**Your customer wants to capture multiple gigabytes of real-time key performance indicators (KPIs) from their game servers running on Google Cloud Platform (GCP) and monitor these KPIs with low latency.**

**How should they capture and monitor the KPIs?**

- [ ] A. Store **time-series data** from the game servers in **Google Bigtable** and visualize it using **Google Data Studio**.
- [x] B. Output **custom metrics** to **Stackdriver** from the game servers and create a **dashboard in Stackdriver Monitoring Console** to view them.
- [ ] C. Schedule **BigQuery load jobs** to ingest **analytics files** uploaded to **Cloud Storage** every **ten minutes**, then visualize the results in **Google Data Studio**.
- [ ] D. Insert the **KPIs into Cloud Datastore entities** and perform **ad hoc analysis and visualizations** in **Cloud Datalab**.

### Explanation

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

---

## Question 4

*Domain 5: Managing Implementation*

**You have a Python web application with many dependencies that requires 0.1 CPU cores and 128 MB of memory to run in production. You want to monitor and maximize machine utilization while also ensuring reliable deployment of new versions of the application.**

**Which approach should you take?**

- [ ] A. **Managed Instance Group approach** Create a **managed instance group** using **f1-micro** machines. Use a **startup script** to clone the repository, check out the production branch, install dependencies, and start the Python app. Restart the instances to deploy new production releases.
- [ ] B. **Compute Engine Image approach** Create a **managed instance group** using **n1-standard-1** machines. Build a **Compute Engine image** from the production branch with all dependencies and auto-start the Python app. Rebuild the Compute Engine image and update the **instance template** to deploy new releases.
- [x] C. **Google Kubernetes Engine (GKE) with versioning approach** Create a **Google Kubernetes Engine (GKE) cluster** using **n1-standard-1** machines. Build a **Docker image** from the **production branch**, including all dependencies, and tag it with a **version number**. Create a **Kubernetes Deployment** with `imagePullPolicy: IfNotPresent` in the **staging namespace**, and then promote it to **production** after testing.
- [ ] D. **GKE with always pulling latest image approach** Create a **GKE cluster** using **n1-standard-4** machines. Build a **Docker image** from the **master branch**, including all dependencies, and tag it as `'latest'`. Create a **Kubernetes Deployment** in the **default namespace** with `imagePullPolicy: Always`, and restart the pods to deploy new production releases.

### Explanation

**Correct Answer:**

✅ **C. Google Kubernetes Engine (GKE) with versioning approach**

**Explanation:**

The **best approach** should:

1. **Maximize machine utilization** by running multiple lightweight workloads efficiently.
2. **Ensure reliable deployments** with version control and controlled rollouts.
3. **Efficiently manage dependencies** without excessive overhead.

✅ **Why GKE with Versioning is the Best Choice?**

- **Kubernetes efficiently utilizes resources**—multiple instances of the app can run on a shared machine.
- **Using Docker images ensures dependency consistency** across environments.
- **Versioning and staged deployments (staging → production) minimize downtime** and deployment risks.
- **imagePullPolicy: IfNotPresent** ensures new deployments use **tested and stable images** instead of always fetching the latest, reducing downtime risks.

**Implementation Steps:**

1. **Create a GKE cluster with n1-standard-1 machines** to balance cost and performance.
  ```
  gcloud container clusters create my-cluster --machine-type=n1-standard-1
  ```
2. **Build a versioned Docker image from the production branch:**
  ```
  docker build -t gcr.io/my-project/my-app:v1 .docker push gcr.io/my-project/my-app:v1
  ```
3. **Create a Kubernetes Deployment with versioned images:**
  ```
  apiVersion: apps/v1kind: Deploymentmetadata:  name: my-app  namespace: productionspec:  replicas: 3  selector:    matchLabels:      app: my-app  template:    metadata:      labels:        app: my-app    spec:      containers:      - name: my-app        image: gcr.io/my-project/my-app:v1        imagePullPolicy: IfNotPresent
  ```
4. **Test in the staging namespace before promoting to production:**
  ```
  kubectl apply -f my-app.yaml --namespace=staging
  ```
5. **After verification, promote to production.**

✅ **Supporting Documentation:**

- **GKE Best Practices for Deployment:**
  **https://cloud.google.com/kubernetes-engine/docs/best-practices/deploying**
- **Container Versioning and Rollout Strategies:**
  **https://cloud.google.com/kubernetes-engine/docs/concepts/deployment-strategies**

**Why Other Options Are Incorrect?**

**A. Managed Instance Group (MIG) with f1-micro machines.** ❌

- **f1-micro machines are too small** and may not handle production workloads reliably.
- **Startup scripts are inefficient**—managing dependencies via scripts is slower and more error-prone than using containers.
- **Restarting instances to deploy new releases is disruptive**—rolling updates in Kubernetes are better.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-groups**

**B. Compute Engine Image approach.** ❌

- **Building new Compute Engine images for each deployment is slow and inefficient.**
- **Machine images are more suited for OS-level updates, not frequent application updates.**
- **Does not maximize resource utilization**—dedicated VMs are less efficient than containerized workloads in Kubernetes.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/images**

**D. GKE with always pulling latest image (`imagePullPolicy: Always`).** ❌

- **Pulling the "latest" image can introduce untested changes**—risking stability.
- **Increases network overhead**—every pod restart requires an image pull.
- **Using versioned images ensures reliability and controlled rollouts.**

✅ **Reference:**

- **https://kubernetes.io/docs/concepts/configuration/overview/#container-images**

**Conclusion:**

The best approach is **C. Google Kubernetes Engine (GKE) with versioning approach**, because:
✔ **Maximizes resource utilization with containerized workloads.**
✔ **Ensures reliable deployments with versioning and staged rollouts.**
✔ **Uses Kubernetes best practices for application management and scaling.**

📌 **Final Reference:**
**https://cloud.google.com/kubernetes-engine/docs/best-practices/deploying**

---

## Question 5

*Domain 3: Designing for Security and Compliance*

**Your company wants to start using Google Cloud resources while retaining its on-premises Active Directory (AD) domain controller for identity management.**

**What should you do?**

- [ ] A. Use the **Admin Directory API** to authenticate against the **Active Directory domain controller**.
- [x] B. Use **Google Cloud Directory Sync** to **synchronize Active Directory usernames** with **Cloud Identities** and configure **SAML SSO**.
- [ ] C. Use **Cloud Identity-Aware Proxy (IAP)** and configure it to use the **on-premises Active Directory domain controller** as an **identity provider**.
- [ ] D. Use **Compute Engine** to create an **Active Directory (AD) domain controller replica** in Google Cloud, and sync it with the on-premises AD using **Google Cloud Directory Sync**.

### Explanation

**Correct Answer:**

✅ **B. Use Google Cloud Directory Sync to synchronize Active Directory usernames with Cloud Identities and configure SAML SSO.**

**Explanation:**

Your **company wants to use Google Cloud resources while retaining its on-premises Active Directory (AD) domain controller for identity management**. The best approach is to **synchronize AD accounts with Google Cloud using Google Cloud Directory Sync (GCDS) and configure SAML SSO** for authentication.

✅ **Why This Works?**

1. **Google Cloud Directory Sync (GCDS)** ensures that on-prem AD users can access Google Cloud without manually creating accounts.
2. **SAML-based Single Sign-On (SSO)** allows users to log in to Google Cloud services using their existing AD credentials.
3. **No need to maintain additional infrastructure**—users authenticate via AD while Google Cloud manages access.

**Implementation Steps:**

1. **Install Google Cloud Directory Sync (GCDS)** on a Windows Server connected to Active Directory.
2. **Sync AD users and groups with Google Cloud**:
  ```
  gcloud identity groups create --email mycompany.com --description "GCDS Synced Group"
  ```
3. **Enable SAML SSO in Google Cloud Identity**:
  - Configure **SAML authentication provider** to use **Active Directory Federation Services (AD FS)**.
  - **Users authenticate via AD FS**, but their access is managed through Google Cloud IAM.

✅ **Supporting Documentation:**

- **Google Cloud Directory Sync Overview:**
  **https://cloud.google.com/architecture/identity/federating-gcp-with-active-directory**
- **Setting Up SAML SSO for Google Cloud:**
  **https://cloud.google.com/identity/docs/setup-sso**

**Why Other Options Are Incorrect?**

**A. Use the Admin Directory API to authenticate against the Active Directory domain controller.** ❌

- **The Admin Directory API is for managing Google Workspace accounts**, not authenticating users against on-prem AD.
- **It does not provide SSO functionality for Google Cloud services.**

✅ **Reference:**

- **https://developers.google.com/admin-sdk/directory/**

**C. Use Cloud Identity-Aware Proxy (IAP) and configure it to use the on-premises Active Directory domain controller as an identity provider.** ❌

- **Cloud Identity-Aware Proxy (IAP) is used for application-level access control**, not for integrating Active Directory authentication with Google Cloud IAM.
- **IAP requires Google Identity or a federated SAML/OIDC provider, which still needs Cloud Identity integration.**

✅ **Reference:**

- **https://cloud.google.com/iap/docs/concepts-overview**

**D. Use Compute Engine to create an Active Directory (AD) domain controller replica in Google Cloud, and sync it with the on-premises AD using Google Cloud Directory Sync.** ❌

- **Creating a domain controller replica in Compute Engine is complex and requires managing AD replication manually.**
- **Google Cloud Directory Sync (GCDS) does not sync AD servers—it only syncs users and groups.**
- **A simpler and recommended approach is to use SAML-based federation instead of replicating AD.**

✅ **Reference:**

- **https://cloud.google.com/architecture/identity/federating-gcp-with-active-directory**

**Conclusion:**

The best approach is **B. Use Google Cloud Directory Sync to synchronize Active Directory usernames with Cloud Identities and configure SAML SSO**, because:
✔ **Ensures AD users can access Google Cloud services without manual user creation.**
✔ **Uses SAML SSO to allow authentication via existing AD credentials.**
✔ **Reduces administrative overhead compared to managing AD replicas.**

📌 **Final Reference:**
**https://cloud.google.com/identity/docs/setup-sso**

---

## Question 6

*Domain 6: Ensuring Solution and Operations Excellence*

**You are running a Google Kubernetes Engine (GKE) cluster that serves a web application. Users report that a specific part of the application is not responding. Upon investigation, you notice that all pods of the affected deployment keep restarting every 2 seconds. The application writes logs to standard output, and you need to inspect these logs to identify the issue.**

**Which approach should you take?**

- [ ] A. **Check Stackdriver logs** for each **Compute Engine instance** that serves as a **node** in the cluster.
- [x] B. **Review Stackdriver logs** for the specific **GKE container** running the unresponsive part of the application.
- [ ] C. **Use `gcloud` to connect to the cluster**, access a container in one of the pods, and read the logs.
- [ ] D. **Review Serial Port logs** for each **Compute Engine instance** serving as a node in the cluster.

### Explanation

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

---

## Question 7

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You are using a single Cloud SQL instance to serve your application from a specific zone. You need to introduce high availability to ensure reliability in case of failures.**

**What should you do?**

- [ ] A. Create a **read replica** in a **different region**.
- [ ] B. Create a **failover replica** in a **different region**.
- [ ] C. Create a **read replica** in the **same region but in a different zone**.
- [x] D. Create a **failover replica** in the **same region but in a different zone**.

### Explanation

**Correct Answer:**

✅ **D. Create a failover replica in the same region but in a different zone.**

**Explanation:**

To ensure **high availability (HA) and reliability in case of failures**, Google Cloud SQL provides **HA configurations** using **failover replicas**.

**Why Use a Failover Replica?**

- **Ensures automatic failover** in case of primary instance failure.
- **Deployed in a different zone within the same region**, providing **zonal redundancy**.
- **Google Cloud SQL automatically promotes the failover replica to primary** when needed.

**Implementation Steps:**

1. **Enable high availability (HA) during Cloud SQL instance creation:**
  ```
  gcloud sql instances create my-instance --region=us-central1 --availability-type=REGIONAL
  ```
2. **Verify that the failover replica is set up in a different zone within the same region:**
  ```
  gcloud sql instances describe my-instance
  ```

✅ **Supporting Documentation:**

- **High Availability in Cloud SQL:**
  **https://cloud.google.com/sql/docs/mysql/high-availability**

**Why Other Options Are Incorrect?**

**A. Create a read replica in a different region.** ❌

- **Read replicas are used for scaling read operations, not high availability.**
- **Read replicas do not provide automatic failover.**
- **If the primary instance fails, a read replica does not automatically become the new primary.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**B. Create a failover replica in a different region.** ❌

- **Cloud SQL failover replicas must be in the same region** to provide automatic failover.
- **Cross-region failover is not supported for Cloud SQL HA.**
- **For disaster recovery, use cross-region read replicas, but they require manual promotion.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/high-availability**

**C. Create a read replica in the same region but in a different zone.** ❌

- **Read replicas do not support automatic failover.**
- **If the primary instance fails, the read replica will not be automatically promoted to primary.**
- **Read replicas are useful for load balancing read traffic but not for HA.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**Conclusion:**

The best approach is **D. Create a failover replica in the same region but in a different zone**, because:
✔ **Ensures automatic failover in case of primary instance failure.**
✔ **Provides zonal redundancy within the same region.**
✔ **Recommended by Google Cloud for high availability.**

📌 **Final Reference:**
**https://cloud.google.com/sql/docs/mysql/high-availability**

**⚠️ Note:** "Failover replica" is legacy Cloud SQL wording. Today you enable high availability (availability type `REGIONAL`), which creates a standby in another zone of the same region with automatic failover.

---

## Question 8

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your company is running a stateless application on a Compute Engine instance. The application experiences heavy usage during business hours and light usage outside of business hours. Users have reported that the application slows down during peak hours. You need to optimize performance dynamically.**

**What should you do?**

- [ ] A. **Create a snapshot** of the existing disk, then create an **instance template** from the snapshot. Use this template to create an **autoscaled managed instance group**.
- [ ] B. **Create a snapshot** of the existing disk, then create a **custom image** from the snapshot. Use this image to create an **autoscaled managed instance group**.
- [x] C. **Create a custom image** from the existing disk, then create an **instance template** from the custom image. Use this template to create an **autoscaled managed instance group**.
- [ ] D. **Create an instance template** from the existing disk, then create a **custom image** from the instance template. Use this image to create an **autoscaled managed instance group**.

### Explanation

**Correct Answer:**

✅ **C. Create a custom image from the existing disk, then create an instance template from the custom image. Use this template to create an autoscaled managed instance group.**

**Explanation:**

To **dynamically optimize performance** based on traffic fluctuations, the best solution is to:

1. **Use an autoscaled managed instance group (MIG)** to dynamically adjust resources based on demand.
2. **Create a custom image** to ensure consistent and rapid deployment of new instances.
3. **Use an instance template** to define machine specifications for autoscaling.

**Why This Approach?**

✅ **Custom Image → Faster and Consistent Scaling:**

- A **custom image** captures the entire system state (OS, application, and configuration).
- Enables **rapid provisioning** of instances in the managed instance group (MIG).
- More efficient than snapshots for scaling because snapshots require an additional bootstrapping step.

✅ **Instance Template → Automates Autoscaling:**

- An **instance template** is used by MIGs to launch new instances automatically during peak hours.
- Defines **machine type, boot disk, network configuration, and scaling policies**.

✅ **Managed Instance Group (MIG) → Auto-Scaling for Traffic Spikes:**

- MIG **scales out (adds instances) during business hours** when traffic is high.
- MIG **scales in (removes instances) during off-peak hours**, reducing costs.

**Implementation Steps:**

1. **Create a custom image from the existing Compute Engine instance:**
  ```
  gcloud compute images create my-custom-image \    --source-disk=my-instance-disk \    --source-disk-zone=us-central1-a
  ```
2. **Create an instance template from the custom image:**
  ```
  gcloud compute instance-templates create my-instance-template \    --image=my-custom-image \    --machine-type=n1-standard-2
  ```
3. **Create a managed instance group with autoscaling:**
  ```
  gcloud compute instance-groups managed create my-instance-group \    --base-instance-name=my-instance \    --template=my-instance-template \    --size=1 \    --zone=us-central1-a \    --autoscaling-policy-cpu-utilization-target=0.6 \    --autoscaling-policy-min-num-replicas=1 \    --autoscaling-policy-max-num-replicas=10
  ```

✅ **Supporting Documentation:**

- **Google Cloud Managed Instance Groups (MIGs):**
  **https://cloud.google.com/compute/docs/instance-groups**
- **Creating and Using Custom Images:**
  **https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images**

**Why Other Options Are Incorrect?**

**A. Create a snapshot of the existing disk, then create an instance template from the snapshot. Use this template to create an autoscaled managed instance group.** ❌

- **Snapshots are not ideal for scaling** because they capture only disk data—not configurations or metadata.
- **Creating instances from snapshots is slower** than using a custom image.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/create-snapshots**

**B. Create a snapshot of the existing disk, then create a custom image from the snapshot. Use this image to create an autoscaled managed instance group.** ❌

- **Snapshots are unnecessary in this scenario** because we can directly create a custom image from the disk.
- **Creating an image from a snapshot adds an extra step** without benefits.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images**

**D. Create an instance template from the existing disk, then create a custom image from the instance template. Use this image to create an autoscaled managed instance group.** ❌

- **Instance templates cannot be used as a source for creating images.**
- **Custom images should be created directly from the disk.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instance-templates**

**Conclusion:**

The best approach is **C. Create a custom image from the existing disk, then create an instance template from the custom image. Use this template to create an autoscaled managed instance group**, because:
✔ **Custom images ensure rapid instance creation.**
✔ **Instance templates automate scaling with MIGs.**
✔ **MIG dynamically optimizes performance based on usage.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/instance-groups**

---

## Question 9

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your web application is running on multiple VM instances within a VPC. You need to restrict communication between instances to only the authorized paths and ports while ensuring that your solution does not depend on static IP addresses or subnets, since the application autoscale dynamically.**

**How should you enforce these restrictions?**

- [ ] A. Use **separate VPCs** to control traffic flow.
- [x] B. Use **firewall rules based on network tags** attached to the compute instances.
- [ ] C. Use **Cloud DNS** and allow connections **only from authorized hostnames**.
- [ ] D. Use **service accounts** and configure the web application to **authorize specific service accounts** for access.

### Explanation

**Correct Answer:**

✅ **B. Use firewall rules based on network tags attached to the compute instances.**

**Explanation:**

Since the **application auto-scales dynamically**, using **static IPs or subnets is not reliable**. The best approach is to use **Google Cloud VPC firewall rules** based on **network tags**, which provide **flexibility** and **scalability** without depending on IP addresses.

**Why Use Firewall Rules with Network Tags?**

- **Dynamic Scaling Support** → Tags automatically apply to new instances without requiring IP changes.
- **Granular Traffic Control** → Allows precise control over which instances can communicate over specific ports.
- **Easier Management** → No need to update firewall rules manually when instances are created or terminated.

**Implementation Steps:**

1. **Attach network tags to compute instances dynamically via instance templates**:
  ```
  gcloud compute instances add-tags my-instance --tags web-server
  ```
2. **Create firewall rules using network tags:**
  ```
  gcloud compute firewall-rules create allow-web-traffic \    --direction=INGRESS \    --priority=1000 \    --network=default \    --action=ALLOW \    --rules=tcp:80,tcp:443 \    --source-tags=load-balancer \    --target-tags=web-server
  ```
3. **Ensure only authorized services communicate with each other** using additional firewall rules.

✅ **Supporting Documentation:**

- **Google Cloud VPC Firewall Rules:**
  **https://cloud.google.com/vpc/docs/firewalls**

**Why Other Options Are Incorrect?**

**A. Use separate VPCs to control traffic flow.** ❌

- **Overly complex and unnecessary**—separate VPCs are used for **isolation**, not intra-service communication control.
- **Managing inter-VPC communication via VPC peering is not ideal for autoscaling applications.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/vpc-peering**

**C. Use Cloud DNS and allow connections only from authorized hostnames.** ❌

- **Cloud DNS does not provide network-level security controls**—it resolves domain names but does not restrict network access.
- **Attackers could still bypass DNS controls by connecting directly via IP addresses.**

✅ **Reference:**

- **https://cloud.google.com/dns/docs**

**D. Use service accounts and configure the web application to authorize specific service accounts for access.** ❌

- **Service accounts control application access, not network traffic.**
- **While IAM roles and service accounts manage authentication, they do not enforce VPC network traffic restrictions.**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/service-accounts**

**Conclusion:**

The best approach is **B. Use firewall rules based on network tags attached to the compute instances**, because:
✔ **Supports autoscaling by dynamically applying rules to new instances.**
✔ **Provides precise control over network traffic without relying on static IPs.**
✔ **Recommended best practice for managing intra-VPC security.**

📌 **Final Reference:**
**https://cloud.google.com/vpc/docs/firewalls**

---

## Question 10

*Domain 6: Ensuring Solution and Operations Excellence*

**You are using Cloud SQL as the database backend for a large CRM deployment. As usage increases, you need to ensure:**

- **Automatic storage scaling to prevent running out of space.**
- **CPU usage remains at 75% or below.**
- **Replication lag stays under 60 seconds.**

**Which steps should you take to meet these requirements?**

- [x] A. **Enable automatic storage increase** for the instance. **Create a Stackdriver alert** when CPU usage exceeds 75%, and change the instance type to **reduce CPU usage**. **Create a Stackdriver alert** for replication lag, and **shard the database** to reduce replication time.
- [ ] B. **Enable automatic storage increase** for the instance. **Change the instance type to a 32-core machine** to keep CPU usage below 75%. **Create a Stackdriver alert** for replication lag and **deploy memcached** to reduce load on the primary instance.
- [ ] C. **Create a Stackdriver alert** when storage usage exceeds 75% and **manually increase** available storage. **Deploy memcached** to reduce CPU load. **Change the instance type to a 32-core machine** to reduce replication lag.
- [ ] D. **Create a Stackdriver alert** when storage usage exceeds 75% and **manually increase** available storage. **Deploy memcached** to reduce CPU load. **Create a Stackdriver alert** for replication lag and **change the instance type to a 32-core machine** to reduce lag.

### Explanation

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

---

## Question 11

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You have been assigned to develop an online analytical processing (OLAP) marketing analytics and reporting tool. The solution requires a relational database capable of handling hundreds of terabytes of data efficiently.**

**Which Google-recommended tool should you use for this application?**

- [ ] A. **Cloud Spanner**, because it is **globally distributed**.
- [ ] B. **Cloud SQL**, because it is a **fully managed relational database**.
- [ ] C. **Cloud Firestore**, because it provides **real-time synchronization across devices**.
- [x] D. **BigQuery**, because it is designed for **large-scale processing of tabular data**.

### Explanation

**Correct Answer:**

**D. BigQuery, because it is designed for large-scale processing of tabular data.**

**Explanation:**

The best choice for an OLAP (Online Analytical Processing) tool is BigQuery because:

- It is designed for large-scale analytics with petabyte-scale support.
- It is optimized for analytical queries (OLAP), supporting complex aggregations, joins, and window functions.
- It is serverless and fully managed, requiring no infrastructure maintenance.
- It uses massively parallel processing (MPP), enabling fast queries on large datasets.

**Why BigQuery is Best for OLAP?**

FeatureBigQuerySupports OLAP WorkloadsYesHandles Hundreds of TerabytesYesHighly ScalableYesOptimized for Analytical QueriesYesFully Managed & ServerlessYesSupports Standard SQLYes

**Supporting Documentation:**

- BigQuery Overview:
  https://cloud.google.com/bigquery/docs/introduction
- Best Practices for OLAP in BigQuery:
  https://cloud.google.com/bigquery/docs/querying-data

**Why Other Options Are Incorrect?**

**A. Cloud Spanner, because it is globally distributed.**

- Cloud Spanner is an OLTP (Online Transaction Processing) system, not optimized for analytical queries.
- It is best for transactional workloads requiring strong consistency and high availability.
- It is not optimized for large-scale analytical processing.

**Reference:**

- https://cloud.google.com/spanner/docs

**B. Cloud SQL, because it is a fully managed relational database.**

- Cloud SQL is designed for OLTP, not OLAP.
- It does not scale efficiently for hundreds of terabytes of data.
- Query performance degrades significantly for large analytical workloads.

**Reference:**

- https://cloud.google.com/sql/docs

**C. Cloud Firestore, because it provides real-time synchronization across devices.**

- Cloud Firestore is a NoSQL document database, not designed for relational OLAP workloads.
- It is optimized for real-time mobile and web applications, not large-scale analytical queries.

**Reference:**

- https://cloud.google.com/firestore/docs

**Conclusion:**

The best choice is **D. BigQuery**, because:

- It is designed specifically for OLAP workloads and large-scale analytical processing.
- It supports SQL-based queries and massive parallel processing (MPP).
- It scales efficiently for hundreds of terabytes of data.

**Final Reference:**
[https://cloud.google.com/bigquery/docs/introduction](https://cloud.google.com/bigquery/docs/introduction)

---

## Question 12

*Domain 6: Ensuring Solution and Operations Excellence*

**You have deployed an application on Google Kubernetes Engine (GKE) and are using the Cloud SQL proxy container to enable communication between the Cloud SQL database and the Kubernetes services. You receive a notification that the application is experiencing database connection issues. As per company policy, you must perform a post-mortem analysis.**

**What should you do?**

- [ ] A. Run `gcloud sql instances restart` to restart the Cloud SQL instance.
- [ ] B. Verify that the **Service Account** used by the Cloud SQL proxy container still has the **Cloud Build Editor** role.
- [x] C. In the **Google Cloud Console**, navigate to **Stackdriver Logging** and review the logs for **Google Kubernetes Engine (GKE) and Cloud SQL**.
- [ ] D. In the **Google Cloud Console**, go to **Cloud SQL**, restore the latest backup, and use `kubectl` to restart all pods.

### Explanation

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

---

## Question 13

*Domain 3: Designing for Security and Compliance*

**Your company processes batches of sensitive transaction data by pushing them from application server VMs to Cloud Pub/Sub for further processing and storage. You need to ensure that your application authenticates securely to the required Google Cloud services following Google-recommended best practices.**

**What is the best approach?**

- [x] A. Ensure that **VM service accounts** have the appropriate **Cloud Pub/Sub IAM roles** assigned.
- [ ] B. Ensure that **VM service accounts do not have direct access** to Cloud Pub/Sub and use **VM access scopes** to assign the appropriate **Cloud Pub/Sub IAM roles**.
- [ ] C. Generate an **OAuth2 access token** for Cloud Pub/Sub, **encrypt it**, and store it in **Cloud Storage** for access from each VM.
- [ ] D. Create a **gateway to Cloud Pub/Sub** using a **Cloud Function** and grant the **Cloud Function service account** the required **Cloud Pub/Sub IAM roles**.

### Explanation

**Correct Answer:**

**A. Ensure that VM service accounts have the appropriate Cloud Pub/Sub IAM roles assigned.**

**Explanation:**

Google Cloud **recommends using service accounts** for authentication when applications running on Compute Engine need to access Google Cloud services securely. Service accounts enable **secure, role-based access control** while avoiding hardcoded credentials.

**Why Using VM Service Accounts with IAM Roles is Best Practice?**

- **Secure authentication** → Compute Engine VMs can automatically authenticate to Cloud Pub/Sub using their **attached service account**.
- **Granular IAM control** → You can **assign specific IAM roles** (such as `roles/pubsub.publisher`) to limit permissions.
- **No need to manage credentials manually** → Service accounts authenticate using **Application Default Credentials (ADC)**, reducing security risks.

**Steps to Implement:**

1. **Create a service account for Compute Engine VMs:**
  ```
  bashCopyEditgcloud iam service-accounts create transaction-vm-sa \    --display-name "Transaction Processing VM Service Account"
  ```
2. **Grant the appropriate IAM roles to the service account:**
  ```
  bashCopyEditgcloud projects add-iam-policy-binding my-project \    --member="serviceAccount:transaction-vm-sa@my-project.iam.gserviceaccount.com" \    --role="roles/pubsub.publisher"
  ```
3. **Assign the service account to the VM:**
  ```
  bashCopyEditgcloud compute instances set-service-account my-vm \    --service-account=transaction-vm-sa@my-project.iam.gserviceaccount.com \    --scopes=https://www.googleapis.com/auth/cloud-platform
  ```
4. **Ensure the application running on the VM uses ADC for authentication:**
  ```
  pythonCopyEditfrom google.cloud import pubsub_v1 publisher = pubsub_v1.PublisherClient()topic_path = publisher.topic_path("my-project", "my-topic") data = "Transaction data"future = publisher.publish(topic_path, data.encode("utf-8"))future.result()
  ```

**Supporting Documentation:**

- **Service Accounts Best Practices:**
  https://cloud.google.com/iam/docs/best-practices-for-managing-service-accounts
- **Compute Engine Service Accounts:**
  https://cloud.google.com/compute/docs/access/service-accounts

**Why Other Options Are Incorrect?**

**B. Ensure that VM service accounts do not have direct access to Cloud Pub/Sub and use VM access scopes to assign the appropriate Cloud Pub/Sub IAM roles.**

- **Access scopes are NOT recommended for fine-grained IAM control.**
- **Access scopes apply at the VM level**, but **IAM roles provide better security** by controlling permissions **at the resource level** (such as a specific Pub/Sub topic).

✅ **Reference:**

- https://cloud.google.com/compute/docs/access/service-accounts#accesscopes

**C. Generate an OAuth2 access token for Cloud Pub/Sub, encrypt it, and store it in Cloud Storage for access from each VM.**

- **Manually managing OAuth2 tokens is insecure and error-prone.**
- **Service accounts with IAM roles provide automated authentication** without needing to store or encrypt credentials.
- **Cloud Storage is not meant for secure credential management**.

✅ **Reference:**

- https://cloud.google.com/iam/docs/authentication

**D. Create a gateway to Cloud Pub/Sub using a Cloud Function and grant the Cloud Function service account the required Cloud Pub/Sub IAM roles.**

- **This adds unnecessary complexity**—there is no need for an intermediary Cloud Function when VMs can authenticate directly using service accounts.
- **It introduces latency** and additional failure points.

✅ **Reference:**

- https://cloud.google.com/functions/docs/securing/authenticating

**Conclusion:**

The best approach is **A. Ensure that VM service accounts have the appropriate Cloud Pub/Sub IAM roles assigned**, because:

- It follows **Google-recommended best practices** for authentication.
- It **avoids manual credential management**, improving security.
- It allows **fine-grained IAM role assignment**, enhancing security control.

**Final Reference:**- [https://cloud.google.com/iam/docs/understanding-service-accounts](https://cloud.google.com/iam/docs/understanding-service-accounts)

---

## Question 14

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need to deploy a Compute Engine application in a single VPC that spans two regions. The application must be able to communicate with an on-premises network over VPN.**

**How should you configure the VPN?**

- [ ] A. Use **VPC Network Peering** to establish connectivity between the **VPC and the on-premises network**.
- [ ] B. Expose the **VPC to the on-premises network** using **IAM and VPC Sharing**.
- [ ] C. Create a **global Cloud VPN Gateway** and establish **VPN tunnels from each region** to the **on-premises peer gateway**.
- [x] D. Deploy a **Cloud VPN Gateway** in **each region**, ensuring that each region has **at least one VPN tunnel** to the **on-premises peer gateway**.

### Explanation

**Correct Answer:**

**D. Deploy a Cloud VPN Gateway in each region, ensuring that each region has at least one VPN tunnel to the on-premises peer gateway.**

**Explanation:**

Since the **Compute Engine application is deployed in a single VPC spanning two regions**, and it **must communicate with the on-premises network over VPN**, the best approach is to:

1. **Deploy a Cloud VPN Gateway in each region** → Ensures that instances in both regions can communicate with the on-premises network.
2. **Establish VPN tunnels from each region to the on-premises peer gateway** → Ensures high availability and redundancy.
3. **Use dynamic routing with Cloud Router** → Allows efficient routing of traffic across regions without needing manual static routes.

**Why This Approach?**

- **High Availability**: If one VPN tunnel fails, traffic can still flow through the other region.
- **Better Performance**: Traffic from each region does not have to be routed through another region before reaching on-premises.
- **Scalability**: Supports **auto-scaling and redundancy** without requiring manual reconfiguration.

**Implementation Steps:**

1. **Create a Cloud VPN Gateway in each region:**
  ```
  gcloud compute vpn-gateways create vpn-gateway-us-east1 \    --region=us-east1 \    --network=my-vpc gcloud compute vpn-gateways create vpn-gateway-us-west1 \    --region=us-west1 \    --network=my-vpc
  ```
2. **Establish VPN tunnels between Cloud VPN and on-premises VPN Gateway:**
  ```
  gcloud compute vpn-tunnels create tunnel-to-onprem-us-east1 \    --region=us-east1 \    --peer-address=<on-prem-peer-ip> \    --ike-version=2 \    --shared-secret=<shared-secret> gcloud compute vpn-tunnels create tunnel-to-onprem-us-west1 \    --region=us-west1 \    --peer-address=<on-prem-peer-ip> \    --ike-version=2 \    --shared-secret=<shared-secret>
  ```
3. **Enable Cloud Router for dynamic routing:**
  ```
  gcloud compute routers create router-us-east1 \    --region=us-east1 \    --network=my-vpc \    --asn=65001 gcloud compute routers create router-us-west1 \    --region=us-west1 \    --network=my-vpc \    --asn=65002
  ```
4. **Attach Cloud Routers to VPN tunnels for dynamic routing (BGP):**
  ```
  gcloud compute vpn-tunnels update tunnel-to-onprem-us-east1 \    --region=us-east1 \    --router=router-us-east1 gcloud compute vpn-tunnels update tunnel-to-onprem-us-west1 \    --region=us-west1 \    --router=router-us-west1
  ```

**Supporting Documentation:**

- **Google Cloud VPN Overview:**
  https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview
- **Using Cloud Router with Cloud VPN:**
  https://cloud.google.com/network-connectivity/docs/router/how-to/configure-cloud-vpn

**Why Other Options Are Incorrect?**

**A. Use VPC Network Peering to establish connectivity between the VPC and the on-premises network.**

- **VPC Peering only connects two VPC networks**—it **cannot connect a VPC to an on-premises network**.
- **VPN is required to establish a secure connection between on-premises and Google Cloud.**

**Reference:**
https://cloud.google.com/vpc/docs/vpc-peering

**B. Expose the VPC to the on-premises network using IAM and VPC Sharing.**

- **IAM and VPC Sharing allow resource sharing within Google Cloud, not connectivity with on-premises networks.**
- **VPN is required for secure hybrid cloud connectivity.**

**Reference:**
https://cloud.google.com/vpc/docs/vpc-sharing

**C. Create a global Cloud VPN Gateway and establish VPN tunnels from each region to the on-premises peer gateway.**

- **Cloud VPN Gateways are regional**, meaning a **single global VPN gateway does not exist**.
- **Each region needs its own Cloud VPN Gateway** for direct connectivity.

**Reference:**
https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-vpn

**Conclusion:**

The best approach is **D. Deploy a Cloud VPN Gateway in each region, ensuring that each region has at least one VPN tunnel to the on-premises peer gateway**, because:

- It ensures **high availability** by setting up VPN tunnels in both regions.
- It allows **low-latency regional access** to on-premises resources.
- It follows **Google Cloud best practices** for hybrid network connectivity.

**Final Reference:**

[https://cloud.google.com/vpn/docs/how-to/creating-static-vpns](https://cloud.google.com/vpn/docs/how-to/creating-static-vpns)

---

## Question 15

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your applications will be writing logs to BigQuery for analysis, with each application having its own table. You need to automatically remove logs older than 45 days, while optimizing storage and following Google-recommended best practices.**

**What should you do?**

- [ ] A. Set the **expiration time** for each table to **45 days**.
- [x] B. Use **time-partitioned tables** and configure the **partition expiration** to **45 days**.
- [ ] C. Rely on **BigQuery’s default behavior**, which automatically removes logs older than 45 days.
- [ ] D. Create a **script** using the **BigQuery command-line tool (bq)** to delete records older than **45 days**.

### Explanation

**Correct Answer:**

**B. Use time-partitioned tables and configure the partition expiration to 45 days.**

**Explanation:**

To **automatically remove logs older than 45 days** while **optimizing storage** and **following Google-recommended best practices**, the best approach is to:

- **Use time-partitioned tables** to organize log data efficiently.
- **Set partition expiration to 45 days**, ensuring automatic deletion of outdated logs.

**Why Use Time-Partitioned Tables?**

1. **Storage Optimization:** Data is automatically divided into partitions based on a timestamp column.
2. **Performance Improvement:** Queries are **faster and cheaper** because they scan only relevant partitions.
3. **Automatic Expiration:** Logs older than 45 days are **automatically deleted**, reducing manual effort.
4. **Recommended by Google for log retention management.**

**Implementation Steps:**

1. **Create a time-partitioned table with expiration set to 45 days:**
  ```
  bq mk --time_partitioning_field timestamp \     --time_partitioning_type DAY \     --time_partitioning_expiration 3888000 \     my_dataset.my_table
  ```
  - `timestamp` → The column used for partitioning.
  - `DAY` → Creates daily partitions.
  - `3888000` → **45 days in seconds** (45 * 24 * 60 * 60).
2. **Verify partition expiration settings:**
  ```
  bq show --format=prettyjson my_dataset.my_table
  ```

**Supporting Documentation:**

- **BigQuery Partitioned Tables:**
  https://cloud.google.com/bigquery/docs/partitioned-tables
- **Setting Partition Expiration:**
  https://cloud.google.com/bigquery/docs/managing-partitioned-tables

**Why Other Options Are Incorrect?**

**A. Set the expiration time for each table to 45 days.**

- **Table expiration removes the entire table, not just old data.**
- **If a table is expired, all logs (including recent ones) will be lost.**
- **Time-based partitioning is more efficient for managing log retention.**

**Reference:**
https://cloud.google.com/bigquery/docs/managing-tables

**C. Rely on BigQuery’s default behavior, which automatically removes logs older than 45 days.**

- **BigQuery does not automatically delete old logs** unless explicitly configured.
- **Without setting an expiration, logs will accumulate indefinitely, increasing storage costs.**

**Reference:**
https://cloud.google.com/bigquery/docs/introduction

**D. Create a script using the BigQuery command-line tool (`bq`) to delete records older than 45 days.**

- **Manually running a deletion script is inefficient and unnecessary.**
- **Deletes require full table scans, which are costly and slow.**
- **Partition expiration is the recommended automated approach.**

**Reference:**
https://cloud.google.com/bigquery/docs/managing-partitioned-tables#setting_partition_expiration

**Conclusion:**

The best approach is **B. Use time-partitioned tables and configure the partition expiration to 45 days**, because:

- It **automates log retention management**.
- It **improves query performance and reduces storage costs**.
- It **follows Google-recommended best practices**.

**Final Reference:**
**https://cloud.google.com/bigquery/docs/partitioned-tables**

---

## Question 16

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need your Google Kubernetes Engine (GKE) cluster to automatically scale nodes up or down based on CPU load.**

**What should you do?**

- [x] A. Configure a **HorizontalPodAutoscaler** with a **target CPU usage** and enable **Cluster Autoscaler** from the **Google Cloud Console**.
- [ ] B. Configure a **HorizontalPodAutoscaler** with a **target CPU usage** and enable **autoscaling on the managed instance group** for the cluster using the **gcloud** command.
- [ ] C. Create a **Deployment** and set the **maxUnavailable** and **maxSurge** properties, then enable **Cluster Autoscaler** using the **gcloud** command.
- [ ] D. Create a **Deployment** and set the **maxUnavailable** and **maxSurge** properties, then enable **autoscaling on the cluster's managed instance group** from the **Google Cloud Console**.

### Explanation

**Correct Answer:**

**A. Configure a HorizontalPodAutoscaler with a target CPU usage and enable Cluster Autoscaler from the Google Cloud Console.**

**Explanation:**

To **automatically scale nodes** in a **Google Kubernetes Engine (GKE) cluster** based on **CPU load**, two levels of autoscaling are required:

1. **Horizontal Pod Autoscaler (HPA):** Scales **pods** based on CPU or memory utilization.
2. **Cluster Autoscaler (CA):** Adjusts the **number of nodes** based on pending pods.

**Why This Approach?**

- **HPA ensures that application workloads scale dynamically** based on demand.
- **Cluster Autoscaler ensures sufficient nodes** are available to run the required pods.
- **Both HPA and Cluster Autoscaler are Google Cloud best practices for autoscaling GKE clusters.**

**Implementation Steps:**

1. **Enable Cluster Autoscaler on a node pool:**
  ```
  gcloud container clusters update my-cluster \    --enable-autoscaling \    --min-nodes 1 \    --max-nodes 5 \    --node-pool default-pool
  ```
2. **Create a Horizontal Pod Autoscaler (HPA):**
  ```
  kubectl autoscale deployment my-app \    --cpu-percent=50 \    --min=1 --max=10
  ```
3. **Verify HPA status:**
  ```
  kubectl get hpa
  ```
4. **Verify Cluster Autoscaler logs:**
  ```
  gcloud logging read "resource.type=gke_nodepool"
  ```

**Supporting Documentation:**

- **Cluster Autoscaler:**
  https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler
- **Horizontal Pod Autoscaler:**
  https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

**Why Other Options Are Incorrect?**

**B. Configure a HorizontalPodAutoscaler with a target CPU usage and enable autoscaling on the managed instance group for the cluster using the gcloud command.**

- **Managed Instance Groups (MIGs) do not directly manage GKE nodes**—Cluster Autoscaler should be used instead.
- **HPA does not control instance groups; it controls pod scaling.**

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler

**C. Create a Deployment and set the maxUnavailable and maxSurge properties, then enable Cluster Autoscaler using the gcloud command.**

- **maxUnavailable and maxSurge control rolling updates**, not autoscaling.
- **They do not impact scaling behavior based on CPU load.**

✅ **Reference:**
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-update-deployment

**D. Create a Deployment and set the maxUnavailable and maxSurge properties, then enable autoscaling on the cluster's managed instance group from the Google Cloud Console.**

- **maxUnavailable and maxSurge are related to deployment strategy, not autoscaling.**
- **Cluster Autoscaler should be enabled on the GKE cluster, not on a MIG.**

✅ **Reference:**
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

**Conclusion:**

The best approach is **A. Configure a HorizontalPodAutoscaler with a target CPU usage and enable Cluster Autoscaler from the Google Cloud Console**, because:

- It **dynamically scales both pods and nodes based on demand**.
- It **follows Google Cloud best practices for GKE autoscaling**.
- It **ensures cost efficiency by optimizing resource usage**.

**Final Reference:**
[https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)

---

## Question 17

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**You need to develop procedures to verify the resilience of disaster recovery for remote recovery using Google Cloud Platform (GCP). Your production environment is hosted on-premises, and you must establish a secure, redundant connection between your on-premises network and GCP.**

**What should you do?**

- [ ] A. Verify that **Dedicated Interconnect** can **replicate files to GCP**. Ensure that **Direct Peering** can establish a **secure backup connection** if **Dedicated Interconnect fails**.
- [x] B. Verify that **Dedicated Interconnect** can **replicate files to GCP**. Ensure that **Cloud VPN** can establish a **secure backup connection** if **Dedicated Interconnect fails**.
- [ ] C. Verify that the **Transfer Appliance** can **replicate files to GCP**. Ensure that **Direct Peering** can establish a **secure backup connection** if the **Transfer Appliance fails**.
- [ ] D. Verify that the **Transfer Appliance** can **replicate files to GCP**. Ensure that **Cloud VPN** can establish a **secure backup connection** if the **Transfer Appliance fails**.

### Explanation

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

---

## Question 18

*Domain 3: Designing for Security and Compliance*

**Your company operates nationally and plans to use Google Cloud Platform (GCP) for multiple batch workloads, including some that are not time-sensitive. You also need to ensure that all GCP services used are HIPAA-certified while managing service costs efficiently.**

**How should you design your solution following Google best practices?**

- [x] A. **Use preemptible VMs** to reduce costs and **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.
- [ ] B. **Use preemptible VMs** to reduce costs, **disable** and then **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.
- [ ] C. **Use standard VMs** in the **same region** to reduce costs and **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.
- [ ] D. **Use standard VMs** in the **same region** to reduce costs, **disable** and then **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.

### Explanation

**Correct Answer:**

**A. Use preemptible VMs to reduce costs and discontinue all GCP services and APIs that are not HIPAA-compliant.**

**Explanation:**

The **best approach** ensures **cost efficiency** while meeting **HIPAA compliance requirements** on Google Cloud Platform (GCP).

**Why This Approach?**

1. **Use Preemptible VMs for Cost Savings:**
  - **Preemptible VMs** are significantly **cheaper** than standard VMs.
  - Since **batch workloads are not time-sensitive**, interruptions are acceptable.
  - **Ideal for batch processing, data transformation, and analytics.**
2. **Discontinue Non-HIPAA-Compliant Services:**
  - **Google Cloud provides a Business Associate Agreement (BAA)** for HIPAA compliance.
  - **Only use GCP services listed as HIPAA-compliant** in Google's documentation.
  - **Discontinuing non-HIPAA services** reduces compliance risks.

**Implementation Steps:**

**1. Use Preemptible VMs for Batch Workloads**

- Create preemptible instances using `gcloud`:
  ```
  gcloud compute instances create batch-instance \    --machine-type=e2-standard-4 \    --preemptible \    --zone=us-central1-a
  ```
- Use **Compute Engine Autoscaler** to dynamically provision preemptible instances.
- Store job checkpoints in **Cloud Storage** or **BigQuery** to handle instance termination.

**2. Identify and Disable Non-HIPAA-Compliant Services**

- List all active APIs:
  ```
  gcloud services list
  ```
- Disable non-compliant APIs:
  ```
  gcloud services disable <api-service-name>
  ```
- Confirm that all enabled services comply with HIPAA.

**Google Cloud HIPAA Compliance Reference:**

- **HIPAA-Eligible Services on GCP:**
  https://cloud.google.com/security/compliance/hipaa
- **Preemptible VM Documentation:**
  https://cloud.google.com/compute/docs/instances/preemptible

**Why Other Options Are Incorrect?**

**B. Use preemptible VMs to reduce costs, disable and then discontinue all GCP services and APIs that are not HIPAA-compliant.**

- **Disabling APIs is enough; discontinuing is unnecessary.**
- **Disabling prevents accidental use, while discontinuation might cause issues for dependent workloads.**

✅ **Reference:**
https://cloud.google.com/security/compliance/hipaa

**C. Use standard VMs in the same region to reduce costs and discontinue all GCP services and APIs that are not HIPAA-compliant.**

- **Standard VMs are more expensive than preemptible VMs.**
- **Using standard VMs increases costs unnecessarily for batch workloads.**

✅ **Reference:**
https://cloud.google.com/compute/docs/instances/preemptible

**D. Use standard VMs in the same region to reduce costs, disable and then discontinue all GCP services and APIs that are not HIPAA-compliant.**

- **Same issues as Option C (higher costs due to standard VMs).**
- **Discontinuing APIs is unnecessary when disabling them is sufficient.**

✅ **Reference:**
https://cloud.google.com/security/compliance/hipaa

**Conclusion:**

The best approach is **A. Use preemptible VMs to reduce costs and discontinue all GCP services and APIs that are not HIPAA-compliant**, because:

- Preemptible VMs **maximize cost savings** for batch workloads.
- Discontinuing **non-HIPAA-compliant services** ensures regulatory compliance.
- **Aligns with Google Cloud best practices** for security and cost efficiency.

**Final Reference:**
[https://cloud.google.com/security/compliance/hipaa](https://cloud.google.com/security/compliance/hipaa)

**⚠️ Note:** Preemptible VMs are now Spot VMs. Options A and B differ only in the wording 'disable and then discontinue', which isn't a meaningful technical difference. Learn the real point: interruptible VMs for non-urgent batch, and use only HIPAA-covered services under a BAA.

---

## Question 19

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**Your customer wants to perform resilience testing on their authentication layer, which consists of a regional managed instance group serving a public REST API that interacts with a Cloud SQL instance for reading and writing data.**

**What should you do?**

- [ ] A. Work with a **security firm** to run **web scrapers** that search for users' **authentication data** on **malicious websites** and notify you if any data is found.
- [ ] B. Deploy **intrusion detection software** on the virtual machines to **detect and log unauthorized access attempts**.
- [x] C. **Schedule a disaster simulation** where you **shut down all VMs** in a zone to observe how the application behaves under failure conditions.
- [ ] D. **Set up a Cloud SQL read replica** in a different **zone** from the primary instance, then manually **trigger a failover** while monitoring **KPIs for the REST API**.

### Explanation

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

---

## Question 20

*Domain 6: Ensuring Solution and Operations Excellence*

**Your BigQuery project has multiple users, and for audit purposes, you need to determine how many queries each user ran in the last month.**

**What should you do?**

- [ ] A. **Connect Google Data Studio** to BigQuery, create a **dimension for users**, and define a **metric** for the number of queries per user.
- [x] B. In the **BigQuery interface**, execute a query on the `JOBS` **table** to retrieve the required information.
- [ ] C. Use `bq show` to list all jobs, then use `bq ls` to obtain job details and extract the necessary information.
- [ ] D. Use **Cloud Audit Logging** to view **Cloud Audit Logs** and create a **filter on query operations** to extract the required information.

### Explanation

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

---

## Question 21

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need to automate the creation of a managed instance group (MIG). The VMs in this group have many OS package dependencies, and you want to minimize startup time when new instances are added.**

**What should you do?**

- [ ] A. Use **Terraform** to create the **managed instance group** and a **startup script** to install the OS package dependencies.
- [x] B. Create a **custom VM image** that includes all OS package dependencies, then use **Deployment Manager** to create the **managed instance group** with this VM image.
- [ ] C. Use **Puppet** to create the **managed instance group** and install the OS package dependencies.
- [ ] D. Use **Deployment Manager** to create the **managed instance group** and **Ansible** to install the OS package dependencies.

### Explanation

**Correct Answer:**

**B. Create a custom VM image that includes all OS package dependencies, then use Deployment Manager to create the managed instance group with this VM image.**

**Explanation:**

The goal is to **automate the creation of a Managed Instance Group (MIG)** while **minimizing startup time** when new instances are added. The best approach is to:

1. **Create a custom VM image** that includes all **OS package dependencies**.
2. **Use Deployment Manager** to deploy the MIG using this pre-configured VM image.

**Why This Approach?**

- **Minimizes startup time:** New instances **start quickly** because all required dependencies are already installed.
- **Reduces external dependency failures:** No need to download/install packages at startup, **avoiding package repository issues.**
- **Optimized for scaling:** MIG instances boot faster and are **ready to serve traffic immediately**.
- **Uses Google-recommended best practices** for managing infrastructure as code.

**Implementation Steps:**

**1. Create a Custom VM Image with Preinstalled Dependencies**

- Start a VM and install the required dependencies:
  ```
  gcloud compute instances create my-instance \    --image-family=debian-11 \    --image-project=debian-cloud \    --machine-type=e2-standard-4 \    --zone=us-central1-a
  ```
- SSH into the VM and install required packages:
  ```
  sudo apt-get updatesudo apt-get install -y my-package1 my-package2
  ```
- Create a custom image from the configured VM:
  ```
  gcloud compute images create my-custom-image \    --source-disk=my-instance \    --source-disk-zone=us-central1-a
  ```
- Delete the VM after creating the image:
  ```
  bashCopyEditgcloud compute instances delete my-instance --zone=us-central1-a
  ```

**2. Use Deployment Manager to Create the Managed Instance Group**

- Define a **Deployment Manager YAML template** (`mig-template.yaml`):
  ```
  resources:- name: my-mig  type: compute.v1.instanceGroupManager  properties:    baseInstanceName: my-instance    instanceTemplate: $(ref.my-template.selfLink)    targetSize: 3- name: my-template  type: compute.v1.instanceTemplate  properties:    properties:      machineType: e2-standard-4      disks:      - boot: true        initializeParams:          sourceImage: my-custom-image      networkInterfaces:      - network: global/networks/default
  ```
- Deploy the MIG using Deployment Manager:
  ```
  gcloud deployment-manager deployments create my-mig-deployment --config=mig-template.yaml
  ```

**Supporting Documentation:**

- **Creating and Using Custom VM Images:**
  https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images
- **Deployment Manager for MIGs:**
  https://cloud.google.com/deployment-manager/docs

**Why Other Options Are Incorrect?**

**A. Use Terraform to create the managed instance group and a startup script to install the OS package dependencies.**

- **Startup scripts increase boot time** as they execute package installations at instance launch.
- **External dependency failures can delay instance startup.**
- Terraform is great for infrastructure automation, but **pre-baked images are better for fast scaling**.

✅ **Reference:**
https://cloud.google.com/compute/docs/startupscript

**C. Use Puppet to create the managed instance group and install the OS package dependencies.**

- **Configuration management tools like Puppet add complexity.**
- **Puppet runs post-instance startup**, increasing boot time.
- **Not necessary when a preconfigured image already has all required dependencies.**

✅ **Reference:**
https://puppet.com/docs/puppet/latest/puppet_intro.html

**D. Use Deployment Manager to create the managed instance group and Ansible to install the OS package dependencies.**

- **Ansible still installs dependencies post-boot, increasing startup time.**
- **Requires additional network configuration for agentless Ansible execution.**
- **Using a pre-built image eliminates the need for post-boot configuration.**

✅ **Reference:**
https://docs.ansible.com/ansible/latest/user_guide/index.html

**Conclusion:**

The best approach is **B. Create a custom VM image that includes all OS package dependencies, then use Deployment Manager to create the managed instance group with this VM image**, because:

- **It ensures the fastest instance startup time.**
- **It avoids dependency failures during boot.**
- **It follows Google Cloud best practices for managing MIGs efficiently.**

**Final Reference:**
[https://cloud.google.com/compute/docs/instance-groups](https://cloud.google.com/compute/docs/instance-groups)

**⚠️ Note:** Deployment Manager reached end of support in 2026; Google points users to **Infrastructure Manager** (managed Terraform) or Terraform itself. The tested idea is unchanged: bake OS dependencies into a **custom image** so new MIG instances boot fast.

---

## Question 22

*Domain 3: Designing for Security and Compliance*

**Your company collects all web traffic data using Google Analytics 360 and stores it in BigQuery. Each country has its own dataset, and each dataset contains multiple tables. You need to ensure that analysts from each country can only view and query the data relevant to their respective countries.**

**How should you configure access rights?**

- [x] A. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery jobUser IAM role**. Share the appropriate **dataset** with **view access** for each respective **analyst country-group**.
- [ ] B. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery jobUser IAM role**. Share the appropriate **tables** with **view access** for each respective **analyst country-group**.
- [ ] C. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery dataViewer IAM role**. Share the appropriate **dataset** with **view access** for each respective **analyst country-group**.
- [ ] D. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery dataViewer IAM role**. Share the appropriate **table** with **view access** for each respective **analyst country-group**.

### Explanation

**Correct Answer:**

**A. Create a group per country and add analysts to their respective country-groups. Create a single group `all_analysts` and add all country-groups as members. Grant the `all_analysts` group the BigQuery `jobUser` IAM role. Share the appropriate dataset with view access for each respective analyst country-group.**

**Explanation:**

To **restrict analysts to view and query only their respective country datasets** while ensuring they can run queries, the best approach is:

1. **Create a Google Group per country** (e.g., `analysts_usa`, `analysts_uk`).
2. **Create a global group (`all_analysts`)** and add all country-specific groups as members.
3. **Grant the `jobUser` role to** `all_analysts` → Required to run queries but does not grant dataset access.
4. **Grant dataset-level `VIEW` access to respective country groups** → Ensures analysts can query only their country's dataset.

**Why This Approach?**

**RequirementHow This Solution Meets ItAnalysts should only query their country’s dataset**Each country-specific group has `VIEW` access to its respective dataset.**Analysts need permission to run queries**The `jobUser` role allows running queries but does not grant dataset access.**Easy management of users per country**Users are managed at the group level, reducing manual access control.**Minimal overhead and follows best practices**Uses IAM and dataset-level permissions effectively.

**Implementation Steps:**

**1. Create country-specific groups**

- Create a **Google Group** per country (e.g., `analysts_usa`, `analysts_uk`).

**2. Create a global analysts group**

- Add all country-specific groups to `all_analysts`.

**3. Grant the `jobUser` IAM role to** `all_analysts`

- The `jobUser` role allows users to **run queries without dataset access**.
  ```
  gcloud projects add-iam-policy-binding my-bigquery-project \    --member=group:all_analysts@example.com \    --role=roles/bigquery.jobUser
  ```

**4. Grant dataset `VIEW` access to country groups**

- Grant **dataset-level `roles/bigquery.dataViewer` permissions** to each country group.
  ```
  gcloud projects add-iam-policy-binding my-bigquery-project \    --member=group:analysts_usa@example.com \    --role=roles/bigquery.dataViewer \    --condition="resource.name:datasets/usa_dataset"
  ```

**5. Verify Access**

- Run a test query to confirm that analysts can access only their assigned datasets.

**Supporting Documentation:**

- **IAM Roles in BigQuery:**
  https://cloud.google.com/bigquery/docs/access-control
- **Restricting Access at the Dataset Level:**
  https://cloud.google.com/bigquery/docs/dataset-access-controls

**Why Other Options Are Incorrect?**

**B. Share the appropriate tables instead of datasets.**

- **Managing table-level permissions is impractical** for large datasets.
- **Dataset-level permissions simplify access management** while still maintaining security.
- **Google Cloud recommends using dataset-level access** over table-level access where possible.

✅ **Reference:**
https://cloud.google.com/bigquery/docs/table-access-controls

**C. Grant the `dataViewer` role instead of `jobUser`.**

- `dataViewer` allows **viewing datasets** but does **not allow running queries**.
- Analysts need the **jobUser role** to execute queries.

✅ **Reference:**
https://cloud.google.com/bigquery/docs/access-control

**D. Share the appropriate table instead of the dataset and grant the `dataViewer` role.**

- **Table-level access control is complex to manage**.
- `dataViewer` **alone is insufficient**—analysts also need `jobUser` to run queries.

✅ **Reference:**
https://cloud.google.com/bigquery/docs/table-access-controls

**Conclusion:**

The best approach is **A. Create a group per country and add analysts to their respective country-groups. Create a single group `all_analysts` and add all country-groups as members. Grant the `all_analysts` group the BigQuery `jobUser` IAM role. Share the appropriate dataset with view access for each respective analyst country-group.**

**Why?**
✔ Ensures **each analyst can only access their country’s dataset**.
✔ **Grants the necessary permissions to run queries** (`jobUser` role).
✔ **Uses dataset-level access control** for easy management.
✔ **Follows Google Cloud’s recommended best practices** for access control.

**Final Reference:**
[https://cloud.google.com/bigquery/docs/dataset-access-controls](https://cloud.google.com/bigquery/docs/dataset-access-controls)

---

## Question 23

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your client has engaged you to lead the migration of their application infrastructure to Google Cloud Platform (GCP). One of their current challenges is that their on-premises high-performance SAN requires frequent and costly upgrades to support their varied workloads, which include:**

- **20 TB of log archives (retained for legal compliance).**
- **500 GB of VM boot/data volumes and templates.**
- **500 GB of image thumbnails.**
- **200 GB of customer session state data (to allow customers to resume sessions even after being offline for several days).**

**Which storage allocation strategy would provide the most cost-effective solution?**

- [ ] A. Use **Local SSD** for **customer session state data**. Use **lifecycle-managed Cloud Storage** for **log archives, thumbnails, and VM boot/data volumes**.
- [x] B. Use **Memcache backed by Cloud Datastore** for **customer session state data**. Use **lifecycle-managed Cloud Storage** for **log archives, thumbnails, and VM boot/data volumes**.
- [ ] C. Use **Memcache backed by Cloud SQL** for **customer session state data**. Use **local SSD-backed instances** for **VM boot/data volumes**. Use **Cloud Storage** for **log archives and thumbnails**.
- [ ] D. Use **Memcache backed by Persistent Disk SSD storage** for **customer session state data**. Use **local SSD-backed instances** for **VM boot/data volumes**. Use **Cloud Storage** for **log archives and thumbnails**.

### Explanation

**Correct Answer:**

**B. Use Memcache backed by Cloud Datastore for customer session state data. Use lifecycle-managed Cloud Storage for log archives, thumbnails, and VM boot/data volumes.**

**Explanation:**

The **best approach optimizes cost, scalability, and performance** while addressing **different workload requirements**:

1. **Customer Session State Data (200 GB)**
  - **Best Choice: Memcache + Cloud Datastore**
  - **Why?**
    - **Session data needs to persist for days**, so an **in-memory cache alone is not enough**.
    - **Memcache speeds up access**, while **Cloud Datastore ensures durability**.
    - **Cloud Datastore is cost-effective and scales seamlessly**.
    - **Persistent storage is required in case Memcache resets**.
2. **Log Archives (20 TB)**
  - **Best Choice: Lifecycle-managed Cloud Storage**
  - **Why?**
    - **Cold storage tiers (Nearline, Coldline, Archive) reduce costs**.
    - **Compliance logs are rarely accessed** → Move older logs to cheaper tiers.
    - **Lifecycle policies automatically transition storage classes**.
3. **VM Boot/Data Volumes (500 GB) & Templates**
  - **Best Choice: Cloud Storage with Lifecycle Management**
  - **Why?**
    - **VM images & snapshots can be stored in Cloud Storage**.
    - **Coldline or Archive tiers reduce costs** for rarely accessed backups.
    - **Compute Engine can boot directly from Cloud Storage-based VM images**.
4. **Image Thumbnails (500 GB)**
  - **Best Choice: Lifecycle-managed Cloud Storage**
  - **Why?**
    - **Cloud Storage is highly available, scalable, and low-cost**.
    - **Use multi-regional storage for fast delivery** if images need frequent access.
    - **Use lifecycle policies to move infrequently accessed thumbnails to Nearline/Coldline.**

**Implementation Details:**

**1. Configure Cloud Datastore for Session Data**

- Use **Memorystore (Memcache) for low-latency caching**:
  ```
  gcloud redis instances create session-cache \    --size=5 \    --region=us-central1 \    --tier=STANDARD
  ```
- Store **persistent session data in Cloud Datastore**:
  ```
  from google.cloud import datastore client = datastore.Client()session = datastore.Entity(client.key("UserSession", "session123"))session["user_id"] = "user_456"session["last_active"] = "2025-03-16"client.put(session)
  ```

**2. Configure Lifecycle Policies for Log Archives and Images**

- Example **lifecycle policy for log retention** (move to Archive after 1 year):
  ```
  {  "rule": [    {      "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},      "condition": {"age": 365}    }  ]}
  ```
  ```
  gsutil lifecycle set lifecycle-policy.json gs://log-archives
  ```

**3. Store VM Boot/Data Volumes in Cloud Storage**

- **Upload VM snapshots** to Cloud Storage:
  ```
  gcloud compute images export --destination-uri gs://vm-backups/my-vm-image.tar.gz --image my-vm
  ```

**Why Other Options Are Incorrect?**

**A. Use Local SSD for customer session state data.**

- **Local SSD is ephemeral** → Data is **lost if the VM restarts**.
- **Session data must persist across reboots**, so **Cloud Datastore is a better choice**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/local-ssd

**C. Use Memcache backed by Cloud SQL for session state data.**

- **Cloud SQL is not optimized for NoSQL session storage.**
- **Cloud Datastore is a better choice** because:
  - **Supports flexible schemas** (ideal for session data).
  - **Scales automatically** without manual sharding.
  - **Cheaper for infrequent access**.

✅ **Reference:**
https://cloud.google.com/datastore/docs/concepts/overview

**D. Use Persistent Disk SSD for session state data.**

- **Persistent Disk is not ideal for session storage**:
  - More **expensive than Cloud Datastore**.
  - Does **not scale as well as Datastore**.

✅ **Reference:**
https://cloud.google.com/datastore

**Conclusion:**

The best approach is **B. Use Memcache backed by Cloud Datastore for customer session state data. Use lifecycle-managed Cloud Storage for log archives, thumbnails, and VM boot/data volumes.**

✔ **Ensures cost-effective storage** for different workloads.
✔ **Balances performance, scalability, and durability**.
✔ **Uses Google-recommended best practices**.

**Final Reference:**
[https://cloud.google.com/solutions/best-practices-for-compute](https://cloud.google.com/solutions/best-practices-for-compute)

**⚠️ Note:** VMs boot from Persistent Disk, not Cloud Storage; Cloud Storage can hold the VM images and templates. App Engine memcache is a legacy bundled service (Memorystore is the general cache today). B is still the least-wrong option.

---

## Question 24

*Domain 2: Managing and Provisioning a Solution Infrastructure*

Your **web application** is deployed on **Google Kubernetes Engine (GKE)** and manages **multiple workloads**. One of the workloads **requires a consistent set of hostnames**, even when **pods scale or relaunch**.

Which **Kubernetes feature** should you use to achieve this?

- [x] A. StatefulSets
- [ ] B. Role-Based Access Control (RBAC)
- [ ] C. Container Environment Variables
- [ ] D. Persistent Volumes

### Explanation

**Correct Answer:**

**A. StatefulSets**

**Explanation:**

**StatefulSets** are the correct choice when a **workload requires a consistent set of hostnames, even when pods scale or relaunch**.

**Why Use StatefulSets?**

- **Pods get stable network identities** → Each pod has a **persistent and predictable hostname** (e.g., `pod-0`, `pod-1`).
- **Pods maintain the same identity across restarts** → Ensures **consistent hostnames** for workloads that require stable network references.
- **Useful for stateful applications** → Examples: **databases, distributed systems, and caching layers**.

**Implementation:**

1. **Define a StatefulSet with a stable hostname template:**
  ```
  apiVersion: apps/v1kind: StatefulSetmetadata:  name: my-stateful-appspec:  serviceName: "my-service"  replicas: 3  selector:    matchLabels:      app: my-app  template:    metadata:      labels:        app: my-app    spec:      containers:      - name: my-container        image: my-app-image  volumeClaimTemplates:  - metadata:      name: my-storage    spec:      accessModes: ["ReadWriteOnce"]      resources:        requests:          storage: 10Gi
  ```
2. **Pods receive predictable hostnames:**
  - `my-stateful-app-0`
  - `my-stateful-app-1`
  - `my-stateful-app-2`
3. **DNS resolution remains stable:**
  - Pods can communicate using stable names like:
    ```
    my-stateful-app-0.my-service.default.svc.cluster.local
    ```

**Supporting Documentation:**

- **StatefulSets in Kubernetes**
  https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/

**Why Other Options Are Incorrect?**

**B. Role-Based Access Control (RBAC)**

- **RBAC controls access to Kubernetes resources** but **does not provide persistent hostnames**.
- **It is a security feature, not a workload management solution.**

✅ **Reference:**
https://kubernetes.io/docs/reference/access-authn-authz/rbac/

**C. Container Environment Variables**

- **Environment variables do not ensure stable hostnames across pod restarts.**
- **They are useful for configuration, but they do not persist network identity.**

✅ **Reference:**
https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/

**D. Persistent Volumes**

- **Persistent Volumes (PVs) ensure data persistence, not hostname stability.**
- **PVs are storage solutions, whereas StatefulSets manage pod identity and networking.**

✅ **Reference:**
https://kubernetes.io/docs/concepts/storage/persistent-volumes/

**Conclusion:**

The best approach is **A. StatefulSets**, because:

- It **ensures stable hostnames for pods**, even when they scale or restart.
- It **follows Kubernetes best practices for managing stateful applications**.
- It **is the recommended solution for workloads requiring persistent network identity**.

**Final Reference:**
[https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)

---

## Question 25

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You are using Cloud CDN to serve static HTTP(S) content from a Compute Engine instance group. You need to improve the cache hit ratio to enhance performance and reduce backend load.**

**What should you do?**

- [x] A. **Customize the cache keys** to **omit the protocol** from the key.
- [ ] B. **Shorten the expiration time** of cached objects.
- [ ] C. Ensure the **HTTP(S) header** `Cache-Region` points to the region **closest to your users**.
- [ ] D. **Replicate the static content** in a **Cloud Storage bucket** and point **Cloud CDN** to a **load balancer** on that bucket.

### Explanation

**Correct Answer:**

**A. Customize the cache keys to omit the protocol from the key.**

**Explanation:**

To **improve cache hit ratio** and **reduce backend load**, you should **customize the cache keys** to ensure that **protocol variations (HTTP vs. HTTPS) do not create separate cache entries**.

**Why This Works?**

- By default, **Cloud CDN uses the full URL** (including protocol) as part of the cache key.
- This means that the same resource accessed via **HTTP and HTTPS is cached separately**.
- **Omitting the protocol from the cache key ensures a single cached version** is used for both protocols, improving the cache hit ratio.

**How to Implement?**

Modify the cache key policy:

```
gcloud compute backend-buckets update my-backend-bucket \    --cache-key-policy=includeProtocol=false
```

**Supporting Documentation:**

- **Cloud CDN Cache Key Customization**:
  https://cloud.google.com/cdn/docs/customizing-caching

**Why Other Options Are Incorrect?**

**B. Shorten the expiration time of cached objects.**

- **Shortening expiration time reduces cache hit ratio**, as objects are removed from the cache more frequently.
- **To improve cache hit ratio, you should increase expiration times** where appropriate.

✅ **Reference:**
https://cloud.google.com/cdn/docs/caching#cache-expiration

**C. Ensure the HTTP(S) header Cache-Region points to the region closest to your users.**

- **Cloud CDN automatically routes requests to the nearest edge cache.**
- **There is no `Cache-Region` header in Cloud CDN.**
- **Custom headers do not impact cache hit ratio.**

✅ **Reference:**
https://cloud.google.com/cdn/docs/overview

**D. Replicate the static content in a Cloud Storage bucket and point Cloud CDN to a load balancer on that bucket.**

- **While Cloud Storage can serve static content efficiently**, this **does not directly improve the cache hit ratio** of the existing CDN setup.
- **Moving content to Cloud Storage is a different architectural change**, not an optimization for an existing Compute Engine-backed CDN setup.

✅ **Reference:**
https://cloud.google.com/cdn/docs/using-cloud-cdn-with-cloud-storage

**Conclusion:**

The best approach is **A. Customize the cache keys to omit the protocol from the key**, because:

- It **ensures a single cached version for both HTTP and HTTPS**.
- It **reduces redundant cache entries**, improving **cache hit ratio**.
- It **aligns with Google Cloud's best practices for optimizing Cloud CDN performance**.

**Final Reference:**
[https://cloud.google.com/cdn/docs/customizing-caching](https://cloud.google.com/cdn/docs/customizing-caching)

---

## Question 26

*Domain 6: Ensuring Solution and Operations Excellence*

**Your architecture requires centralized collection of all admin activity logs and VM system logs within your Google Cloud project.**

**How should you collect these logs from both VMs and cloud services?**

- [ ] A. **All admin and VM system logs** are automatically collected by **Stackdriver Logging**.
- [x] B. **Stackdriver Logging automatically collects admin activity logs** for most services, but the **Stackdriver Logging agent must be installed** on each instance to collect system logs.
- [ ] C. Deploy a **custom syslogd Compute Engine instance** and configure your **Google Cloud project and VMs** to forward all logs to it.
- [ ] D. Install the **Stackdriver Logging agent** on a **single Compute Engine instance**, allowing it to collect **all audit and access logs** for your environment.

### Explanation

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

---

## Question 27

*Domain 5: Managing Implementation*

**You need to update an App Engine application while testing the new version with production traffic before fully replacing the current version.**

**What should you do?**

- [ ] A. Deploy the update using the **Instance Group Updater** to create a **partial rollout**, allowing for **canary testing**.
- [x] B. Deploy the update as a **new version** in the **App Engine application**, and **split traffic** between the new and current versions.
- [ ] C. Deploy the update in a **new VPC** and use **Google's global HTTP load balancer** to split traffic between the updated and current applications.
- [ ] D. Deploy the update as a **new App Engine application** and use **Google's global HTTP load balancer** to split traffic between the new and current applications.

### Explanation

**Correct Answer:**

**B. Deploy the update as a new version in the App Engine application, and split traffic between the new and current versions.**

**Explanation:**

To **test a new version of an App Engine application with live production traffic before fully replacing the current version**, the best approach is to:

1. **Deploy the update as a new version** within the existing App Engine service.
2. **Use traffic splitting** to gradually shift requests between the old and new versions.

**Why This Works?**

- **App Engine supports multiple versions within the same service**, allowing easy A/B testing.
- **Traffic splitting lets you send a percentage of live requests to the new version**, helping detect issues before a full rollout.
- **You can route traffic by percentage, IP, or session affinity** to control user experience.

**How to Implement Traffic Splitting in App Engine**

**1. Deploy the New Version**

Run the following command to deploy the updated application as a new version in App Engine:

```
gcloud app deploy --version=new-version
```

**2. Split Traffic Between Versions**

Use **manual traffic splitting** to send a percentage of traffic to the new version:

```
gcloud app services set-traffic default \    --splits current-version=80,new-version=20
```

This **sends 80% of traffic to the old version and 20% to the new version**, allowing gradual rollout and testing.

**3. Monitor and Adjust Traffic**

- Use **Cloud Logging and Monitoring** to track performance.
- Gradually **increase traffic** to the new version if testing is successful.
- If issues occur, **revert all traffic to the stable version**.

**Supporting Documentation:**

- **Traffic Splitting in App Engine**
  https://cloud.google.com/appengine/docs/standard/python/splitting-traffic

**Why Other Options Are Incorrect?**

**A. Deploy the update using the Instance Group Updater to create a partial rollout, allowing for canary testing.**

- **App Engine does not use instance groups directly**—it **manages instances dynamically**.
- **Instance Group Updater is for Compute Engine-managed instances**, not App Engine deployments.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups/updating-instances

**C. Deploy the update in a new VPC and use Google's global HTTP load balancer to split traffic between the updated and current applications.**

- **Unnecessary complexity**—App Engine **already has built-in traffic splitting**, eliminating the need for an external load balancer.
- **Creating a new VPC is redundant** because App Engine **runs on Google’s managed infrastructure** without direct VPC configuration.

✅ **Reference:**
https://cloud.google.com/load-balancing/docs/

**D. Deploy the update as a new App Engine application and use Google's global HTTP load balancer to split traffic between the new and current applications.**

- **A new App Engine application means a separate project**, which is unnecessary.
- **Traffic splitting is already built into App Engine**, so a global load balancer is not required.

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard/python/splitting-traffic

**Conclusion:**

The best approach is **B. Deploy the update as a new version in the App Engine application, and split traffic between the new and current versions**, because:

- **It allows gradual rollout and canary testing using built-in App Engine traffic splitting.**
- **It simplifies deployment without needing external load balancers or separate projects.**
- **It follows Google-recommended best practices for App Engine updates.**

**Final Reference:**
[https://cloud.google.com/appengine/docs/standard/python/splitting-traffic](https://cloud.google.com/appengine/docs/standard/python/splitting-traffic)

---

## Question 28

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You need to ensure that all Compute Engine instances in your VPC can connect to an Active Directory server on specific ports, while blocking all other outbound traffic. You want to enforce this using VPC firewall rules.**

**How should you configure the egress firewall rules?**

- [x] A. **Create an egress rule** with **priority 1000** to **deny all traffic** for all instances. Then, create another **egress rule** with **priority 100** to **allow Active Directory traffic** for all instances.
- [ ] B. **Create an egress rule** with **priority 100** to **deny all traffic** for all instances. Then, create another **egress rule** with **priority 1000** to **allow Active Directory traffic** for all instances.
- [ ] C. **Create an egress rule** with **priority 1000** to **allow Active Directory traffic**. Rely on the **implied deny egress rule** with **priority 100** to **block all other traffic** for all instances.
- [ ] D. **Create an egress rule** with **priority 100** to **allow Active Directory traffic**. Rely on the **implied deny egress rule** with **priority 1000** to **block all other traffic** for all instances.

### Explanation

**Correct choice → A**

**A.** Create an egress rule with priority **1000** that **denies all** traffic for all instances, and then add a second egress rule with priority **100** that **allows the required Active Directory ports** for all instances.

Why option A works

1. **Firewall-rule evaluation order**
  - Priorities are integers **0 – 65535**; **lower numbers mean higher priority** and are matched first. [Google Cloud](https://cloud.google.com/firewall/docs/firewalls)
2. **Implied egress behaviour**
  - Every VPC automatically has an ***implied allow-egress* rule** (priority 65535) that lets all outbound traffic through unless a higher-priority rule blocks it. [Google Cloud](https://cloud.google.com/firewall/docs/firewalls)
3. **Result of the two explicit rules in option A**

![](https://img-c.udemycdn.com/redactor/raw/practice_test_question_explanation/2025-05-14_14-43-40-d4206bf78011a5b4d45318b8dcfc08d6.JPG)

Thus all VMs can talk only to the specified AD ports, and everything else is dropped.

**Why the other options are incorrect:**

![](https://img-c.udemycdn.com/redactor/raw/practice_test_question_explanation/2025-05-14_14-43-40-1cff14f5558d076e8e08d6e3df22d8e5.JPG)

---

## Question 29

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your customer operates a web service that provides product recommendations to e-commerce websites. They have started experimenting with a machine learning model on Google Cloud Platform (GCP) to enhance recommendation quality.**

**What should they do to improve the model's results over time?**

- [ ] A. **Export Cloud Machine Learning Engine performance metrics** from **Stackdriver to BigQuery** for **efficiency analysis**.
- [ ] B. **Plan a migration** of the **model training** from **Cloud GPUs to Cloud TPUs**, as TPUs **offer better results**.
- [ ] C. **Monitor Compute Engine announcements** for **newer CPU architectures** and deploy the model on them as soon as they become available to enhance performance.
- [x] D. **Store historical recommendations and their outcomes in BigQuery**, using this data as **training input** to refine the model over time.

### Explanation

**Correct Answer:**

**D. Store historical recommendations and their outcomes in BigQuery, using this data as training input to refine the model over time.**

**Explanation:**

To **improve a machine learning (ML) model's results over time**, **continuous retraining with fresh, high-quality data** is essential.

- **Historical recommendations and user interactions (clicks, purchases, conversions, etc.) provide valuable feedback.**
- **BigQuery serves as a scalable and cost-effective data warehouse** for storing large datasets and running analytical queries.
- **Retraining the model using actual outcomes refines its accuracy**, making recommendations more relevant over time.

**How This Works?**

1. **Store recommendation results and user interactions** in **BigQuery**.
2. **Analyze the data** to identify patterns (e.g., which recommendations led to purchases).
3. **Use this data as labeled training input** to improve the machine learning model.
4. **Automate retraining** using tools like **Vertex AI Pipelines** or **Cloud Composer**.

**Implementation Steps:**

**1. Store Recommendation Data in BigQuery**

Create a table in **BigQuery** to store **historical recommendation data**:

```
CREATE TABLE ecommerce_recommendations.history (  user_id STRING,  product_id STRING,  recommended_at TIMESTAMP,  clicked BOOLEAN,  purchased BOOLEAN);
```

- `recommended_at`: When the recommendation was made.
- `clicked`: Whether the user clicked the recommendation.
- `purchased`: Whether the user bought the product.

**2. Analyze Model Performance**

Query past recommendations and their outcomes: product_id, COUNT(*) AS total_recommendations, SUM(CASE WHEN clicked THEN 1 ELSE 0 END) AS total_clicks, SUM(CASE WHEN purchased THEN 1 ELSE 0 END) AS total_purchases FROM ecommerce_recommendations.history GROUP BY product_id ORDER BY total_purchases DESC;

- Helps **identify high-performing recommendations** for refining the model.

**3. Retrain the Model with Updated Data**

- Use **BigQuery ML** or export refined data to **Vertex AI** for training.
- Automate training jobs using **Vertex AI Pipelines**.
- Deploy updated models via **CI/CD pipelines**.

**Supporting Documentation:**

- **BigQuery for ML Pipelines**:
  https://cloud.google.com/vertex-ai/docs/pipelines/introduction
- **BigQuery for Machine Learning (BigQuery ML)**:
  https://cloud.google.com/bigquery-ml/docs

**Why Other Options Are Incorrect?**

**A. Export Cloud Machine Learning Engine performance metrics from Stackdriver to BigQuery for efficiency analysis.**

- **Performance metrics (latency, CPU usage, etc.) do not directly improve ML model accuracy.**
- **Model accuracy improves with better training data, not infrastructure monitoring.**

✅ **Reference:**
https://cloud.google.com/monitoring

**B. Plan a migration of the model training from Cloud GPUs to Cloud TPUs, as TPUs offer better results.**

- **TPUs improve training speed, not recommendation accuracy.**
- **A poorly trained model on a TPU is still inaccurate.**
- **Data quality, not hardware, is the key factor in improving results.**

✅ **Reference:**
https://cloud.google.com/tpu/docs

**C. Monitor Compute Engine announcements for newer CPU architectures and deploy the model on them as soon as they become available to enhance performance.**

- **Newer CPUs improve inference speed but do not improve model accuracy.**
- **ML models improve by training on better, more relevant data, not by switching CPU architectures.**

✅ **Reference:**
https://cloud.google.com/compute/docs/machine-types

**Conclusion:**

The best approach is **D. Store historical recommendations and their outcomes in BigQuery, using this data as training input to refine the model over time**, because:

- **It enables continuous learning**, ensuring **recommendations improve over time**.
- **BigQuery efficiently handles large-scale data analysis** for ML model training.
- **It follows Google Cloud’s best practices for machine learning lifecycle management.**

**Final Reference:**
[https://cloud.google.com/bigquery-ml/docs](https://cloud.google.com/bigquery-ml/docs)

---

## Question 30

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your company's development team has built a dockerized HTTPS web application. You need to deploy the application on Google Kubernetes Engine (GKE) while ensuring that it scales automatically.**

**How should you deploy it to GKE?**

- [x] A. Use the **Horizontal Pod Autoscaler (HPA)** and enable **Cluster Autoscaler**. Use an **Ingress resource** to load-balance HTTPS traffic.
- [ ] B. Use the **Horizontal Pod Autoscaler (HPA)** and enable **Cluster Autoscaler** on the **Kubernetes cluster**. Use a **Service resource of type LoadBalancer** to distribute HTTPS traffic.
- [ ] C. Enable **autoscaling on the Compute Engine instance group**. Use an **Ingress resource** to load-balance HTTPS traffic.
- [ ] D. Enable **autoscaling on the Compute Engine instance group**. Use a **Service resource of type LoadBalancer** to distribute HTTPS traffic.

### Explanation

**Correct Answer:**

**A. Use the Horizontal Pod Autoscaler (HPA) and enable Cluster Autoscaler. Use an Ingress resource to load-balance HTTPS traffic.**

**Explanation:**

To deploy a **dockerized HTTPS web application** on **Google Kubernetes Engine (GKE) with automatic scaling**, you need to:

1. **Use the Horizontal Pod Autoscaler (HPA) for pod scaling**
  - Ensures the number of application pods **scales based on CPU/memory utilization**.
2. **Enable Cluster Autoscaler for node scaling**
  - Ensures **Compute Engine instances (nodes) scale dynamically** when more pods are scheduled.
3. **Use an Ingress resource for HTTPS load balancing**
  - Ingress **provides a Layer 7 HTTP(S) Load Balancer**.
  - **Automatically provisions an HTTPS load balancer and manages SSL certificates**.

**Implementation Steps**

**1. Deploy the Web Application to GKE**

- Create a Kubernetes **Deployment** for the application:
  ```
  apiVersion: apps/v1kind: Deploymentmetadata:  name: web-appspec:  replicas: 2  selector:    matchLabels:      app: web-app  template:    metadata:      labels:        app: web-app    spec:      containers:      - name: web-app        image: gcr.io/my-project/web-app:v1        ports:        - containerPort: 443
  ```

**2. Create an Externally Accessible Service**

- Expose the app using a **Service of type** `NodePort` (Ingress requires `NodePort` or `ClusterIP`).
  ```
  apiVersion: v1kind: Servicemetadata:  name: web-app-servicespec:  type: NodePort  selector:    app: web-app  ports:    - protocol: TCP      port: 443      targetPort: 443
  ```

**3. Set Up an Ingress Resource for HTTPS Load Balancing**

- Configure an **Ingress resource** to automatically create an HTTPS Load Balancer.
  ```
  apiVersion: networking.k8s.io/v1kind: Ingressmetadata:  name: web-app-ingress  annotations:    kubernetes.io/ingress.class: "gce"spec:  rules:  - host: example.com    http:      paths:      - path: /        pathType: Prefix        backend:          service:            name: web-app-service            port:              number: 443
  ```

**4. Enable Horizontal Pod Autoscaler (HPA)**

- Automatically **scales pods based on CPU utilization**:
  ```
  kubectl autoscale deployment web-app --cpu-percent=50 --min=2 --max=10
  ```

**5. Enable Cluster Autoscaler**

- Scale node pools automatically based on pod demand:
  ```
  gcloud container clusters update my-cluster --enable-autoscaling \    --min-nodes 1 --max-nodes 5 --node-pool default-pool
  ```

**Supporting Documentation:**

- **Ingress for HTTPS Load Balancing**
  https://cloud.google.com/kubernetes-engine/docs/concepts/ingress
- **Horizontal Pod Autoscaler**
  https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler
- **Cluster Autoscaler**
  https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler

**Why Other Options Are Incorrect?**

**B. Use the Horizontal Pod Autoscaler (HPA) and enable Cluster Autoscaler on the Kubernetes cluster. Use a Service resource of type LoadBalancer to distribute HTTPS traffic.**

- **A Service of type `LoadBalancer` creates an L4 (TCP/UDP) Load Balancer, not L7 (HTTP/S)**.
- **Ingress is required for HTTPS traffic termination** with SSL certificate management.

✅ **Reference:**
[https://cloud.google.com/kubernetes-engine/docs/concepts/service](https://cloud.google.com/kubernetes-engine/docs/concepts/service)

---

## Question 31

*Domain 5: Managing Implementation*

**Your application makes HTTP requests to Cloud Storage, but occasionally, these requests fail with HTTP status codes 5xx and 429.**

**How should you handle these errors?**

- [ ] A. Use **gRPC** instead of **HTTP** to improve performance.
- [x] B. Implement **retry logic** using a **truncated exponential backoff strategy**.
- [ ] C. Ensure the **Cloud Storage bucket is multi-regional** for geo-redundancy.
- [ ] D. Monitor **Google Cloud Status** and only make requests when **Cloud Storage is not reporting an incident**.

### Explanation

**Correct Answer:**

**B. Implement retry logic using a truncated exponential backoff strategy.**

**Explanation:**

When making **HTTP requests to Cloud Storage**, encountering **5xx errors (server errors) or 429 errors (Too Many Requests)** is common due to:

- **Temporary service disruptions** (5xx).
- **Rate limiting** when too many requests are sent in a short period (429).

**Google Cloud Best Practice:**

To **gracefully handle these transient failures**, **implement a truncated exponential backoff strategy**:

- **Wait before retrying** (instead of immediately retrying).
- **Exponentially increase wait time** after each failure (e.g., 1s, 2s, 4s, 8s).
- **Cap the maximum wait time** (e.g., 32 seconds).
- **Randomize the delay slightly** to avoid congestion.

**Implementation Example (Python)**

Using the **Google Cloud Storage Python Client Library**:

```
import timeimport randomfrom google.cloud import storage client = storage.Client()bucket = client.bucket("my-bucket")blob = bucket.blob("my-file.txt") def download_blob_with_retry():    max_retries = 5    base_delay = 1  # Start with 1 second    max_delay = 32  # Cap delay at 32 seconds     for attempt in range(max_retries):        try:            return blob.download_as_text()        except Exception as e:            wait_time = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)            print(f"Retrying in {wait_time:.2f} seconds due to error: {e}")            time.sleep(wait_time)        raise Exception("Failed after multiple retries.") download_blob_with_retry()
```

**Supporting Documentation:**

- **Google Cloud Storage Error Handling Best Practices**
  https://cloud.google.com/storage/docs/retry-strategy
- **Using Exponential Backoff**
  https://cloud.google.com/iot/docs/how-tos/exponential-backoff

**Why Other Options Are Incorrect?**

**A. Use gRPC instead of HTTP to improve performance.**

- **gRPC does not resolve HTTP 5xx or 429 errors**—these are service-level or rate-limiting issues.
- Cloud Storage **does not natively support gRPC**; it uses RESTful APIs over HTTP(S).

✅ **Reference:**
https://cloud.google.com/storage/docs/json_api/v1/how-tos

**C. Ensure the Cloud Storage bucket is multi-regional for geo-redundancy.**

- **Multi-regional storage improves availability but does not prevent transient errors** like **5xx and 429.**
- **Retry logic is still necessary, even with multi-regional storage.**

✅ **Reference:**
https://cloud.google.com/storage/docs/availability

**D. Monitor Google Cloud Status and only make requests when Cloud Storage is not reporting an incident.**

- **429 errors are caused by rate limiting**, not service outages.
- **5xx errors can be temporary and retryable**, even if no major incident is reported.
- **Waiting for an incident to clear is impractical**, as many failures are transient.

✅ **Reference:**
https://status.cloud.google.com/

**Conclusion:**

The best approach is **B. Implement retry logic using a truncated exponential backoff strategy**, because:

- **It handles transient failures efficiently.**
- **It prevents overwhelming Cloud Storage with repeated requests.**
- **It follows Google Cloud best practices for error handling.**

**Final Reference:**
[https://cloud.google.com/storage/docs/retry-strategy](https://cloud.google.com/storage/docs/retry-strategy)

---

## Question 32

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**You need to develop procedures to test a disaster recovery plan for a mission-critical application. You want to follow Google-recommended best practices and use native GCP capabilities.**

**What should you do?**

- [ ] A. Use **Deployment Manager** to **automate service provisioning** and monitor/debug tests with **Activity Logs**.
- [x] B. Use **Deployment Manager** to **automate service provisioning** and monitor/debug tests with **Stackdriver**.
- [ ] C. Use **gcloud scripts** to **automate service provisioning** and monitor/debug tests with **Activity Logs**.
- [ ] D. Use **gcloud scripts** to **automate service provisioning** and monitor/debug tests with **Stackdriver**.

### Explanation

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

---

## Question 33

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company develops rendering software that customers can download from the company website. Since you have customers worldwide, you need to minimize latency for all users while following Google-recommended best practices.**

**How should you store the files?**

- [x] A. Save the files in a **Multi-Regional Cloud Storage bucket**.
- [ ] B. Save the files in a **Regional Cloud Storage bucket**, with **one bucket per zone** within the region.
- [ ] C. Save the files in **multiple Regional Cloud Storage buckets**, with **one bucket per zone per region**.
- [ ] D. Save the files in **multiple Multi-Regional Cloud Storage buckets**, with **one bucket per multi-region**.

### Explanation

**Correct Answer:**

**A. Save the files in a Multi-Regional Cloud Storage bucket.**

**Explanation:**

To **minimize latency for customers worldwide** while following **Google-recommended best practices**, the best approach is to **store the files in a Multi-Regional Cloud Storage bucket**.

**Why Use Multi-Regional Cloud Storage?**

- **Geo-redundancy:** Data is automatically replicated **across multiple locations within a multi-region** for **high availability and low latency**.
- **Optimized for frequently accessed content:** Ideal for **public-facing files** like software downloads, as Google Cloud **serves data from the nearest available location**.
- **No need to manage multiple buckets manually**—Google Cloud automatically routes requests to the nearest copy.

**Implementation Steps:**

**1. Create a Multi-Regional Cloud Storage Bucket**

Use the **multi-region closest to your users** (e.g., `us`, `eu`, or `asia`).

```
gcloud storage buckets create my-software-bucket \    --location=US \    --storage-class=MULTI_REGIONAL
```

**2. Upload Software Files**

```
gsutil cp my-rendering-software.zip gs://my-software-bucket/
```

**3. Enable Public Access (Optional, for public downloads)**

```
gsutil iam ch allUsers:objectViewer gs://my-software-bucket
```

**Supporting Documentation:**

- **Google Cloud Multi-Regional Storage**:
  https://cloud.google.com/storage/docs/storage-classes#multi-regional
- **Choosing a Storage Class**:
  https://cloud.google.com/storage/docs/storage-classes

**Why Other Options Are Incorrect?**

**B. Save the files in a Regional Cloud Storage bucket, with one bucket per zone within the region.**

- **Regional buckets are confined to a single region**, which **does not optimize performance for global customers**.
- **Zonal buckets do not exist in Cloud Storage**—Google Cloud Storage works at the **regional and multi-regional level**.

✅ **Reference:**
https://cloud.google.com/storage/docs/storage-classes

**C. Save the files in multiple Regional Cloud Storage buckets, with one bucket per zone per region.**

- **Requires manual setup and maintenance**, increasing operational complexity.
- **Google Cloud Storage Multi-Regional already handles distribution automatically**, making this unnecessary.

✅ **Reference:**
https://cloud.google.com/storage/docs/locations

**D. Save the files in multiple Multi-Regional Cloud Storage buckets, with one bucket per multi-region.**

- **Unnecessary duplication**—a **single Multi-Regional bucket is sufficient** for global distribution.
- **Google automatically directs traffic to the nearest available storage location** within a multi-region.

✅ **Reference:**
https://cloud.google.com/storage/docs/request-endpoints

**Conclusion:**

The best approach is **A. Save the files in a Multi-Regional Cloud Storage bucket**, because:

- **It provides automatic geo-redundancy and low-latency access worldwide.**
- **It minimizes management overhead**—Google Cloud handles traffic routing.
- **It aligns with Google’s best practices for globally distributed content.**

**Final Reference:**
[https://cloud.google.com/storage/docs/storage-classes#multi-regional](https://cloud.google.com/storage/docs/storage-classes#multi-regional)

---

## Question 34

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your company has acquired a healthcare startup and must retain customer medical information for up to 4 more years, based on when the data was created. Corporate policy requires secure data retention and automatic deletion as soon as regulations permit.**

**Which approach should you take?**

- [ ] A. Store the data in **Google Drive** and **manually delete** records as they expire.
- [ ] B. **Anonymize the data** using the **Cloud Data Loss Prevention (DLP) API** and **store it indefinitely**.
- [x] C. Store the data in **Cloud Storage** and use **lifecycle management** to **automatically delete files** when they expire.
- [ ] D. Store the data in **Cloud Storage** and run a **nightly batch script** to delete **all expired data**.

### Explanation

**Correct Answer:**

**C. Store the data in Cloud Storage and use lifecycle management to automatically delete files when they expire.**

**Explanation:**

To **securely retain customer medical information for up to 4 years** and **automatically delete it when regulations permit**, **Google Cloud Storage lifecycle management** is the best approach.

- **Cloud Storage Lifecycle Management** allows you to define **rules to automatically delete files** based on **age, creation date, or other criteria**.
- **Ensures compliance** with regulatory requirements by **removing data exactly when allowed** without manual intervention.
- **More secure than manual deletion** because **lifecycle policies prevent accidental data retention beyond the required period**.

**How to Implement Cloud Storage Lifecycle Management**

**1. Create a Cloud Storage Bucket**

```
gcloud storage buckets create my-healthcare-data \    --location=us \    --storage-class=ARCHIVE
```

**2. Define a Lifecycle Policy for Automatic Deletion**

Create a `lifecycle.json` file:

```
{  "rule": [    {      "action": { "type": "Delete" },      "condition": { "age": 1460 }  # 4 years (1460 days)    }  ]}
```

**3. Apply the Lifecycle Policy**

```
gcloud storage buckets update my-healthcare-data \    --lifecycle-file=lifecycle.json
```

- **Files older than 4 years are automatically deleted**.
- **No manual intervention is needed**, reducing human error.

**Supporting Documentation:**

- **Google Cloud Storage Lifecycle Management**:
  https://cloud.google.com/storage/docs/lifecycle
- **Storage Class for Long-Term Retention (ARCHIVE)**:
  https://cloud.google.com/storage/docs/storage-classes#archive

**Why Other Options Are Incorrect?**

**A. Store the data in Google Drive and manually delete records as they expire.**

- **Google Drive is not designed for regulatory compliance storage.**
- **Manual deletion introduces human error and compliance risks.**
- **Google Cloud Storage provides better security and lifecycle automation.**

✅ **Reference:**
https://cloud.google.com/security/compliance

**B. Anonymize the data using the Cloud Data Loss Prevention (DLP) API and store it indefinitely.**

- **Anonymization does not eliminate the need for regulatory data retention policies.**
- **Some regulations require deletion even if data is anonymized.**
- **Cloud Storage lifecycle policies ensure compliance by enforcing automatic deletion.**

✅ **Reference:**
https://cloud.google.com/dlp/docs/

**D. Store the data in Cloud Storage and run a nightly batch script to delete all expired data.**

- **Batch scripts require manual scheduling and monitoring.**
- **Lifecycle policies are more reliable, automated, and prevent errors.**
- **Running a script nightly incurs unnecessary compute costs.**

✅ **Reference:**
https://cloud.google.com/storage/docs/lifecycle

**Conclusion:**

The best approach is **C. Store the data in Cloud Storage and use lifecycle management to automatically delete files when they expire**, because:

- **It ensures regulatory compliance with automatic, time-based deletion.**
- **It eliminates the need for manual intervention, reducing human error.**
- **It aligns with Google Cloud best practices for secure data retention.**

**Final Reference:**
[https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)

---

## Question 35

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You are deploying a PHP App Engine Standard service with Cloud SQL as the backend database. You need to minimize the number of queries sent to Cloud SQL to optimize performance.**

**What should you do?**

- [x] A. **Set the memcache service level to dedicated**. Create a **key from the hash of the query** and **return database values from memcache** before issuing a query to **Cloud SQL**.
- [ ] B. **Set the memcache service level to dedicated**. Configure a **cron job** that runs **every minute** to **pre-populate the cache** with keys containing **query results**.
- [ ] C. **Set the memcache service level to shared**. Configure a **cron job** that runs **every minute** to **save all expected queries** to a key called **"cached_queries"**.
- [ ] D. **Set the memcache service level to shared**. Create a **key called "cached_queries"** and **return database values from that key** before issuing a query to **Cloud SQL**.

### Explanation

**Correct Answer:**

**A. Set the memcache service level to dedicated. Create a key from the hash of the query and return database values from memcache before issuing a query to Cloud SQL.**

**Explanation:**

To **optimize performance and minimize the number of queries sent to Cloud SQL**, the best approach is to:

1. **Use Memcache (Google Cloud Memorystore) to cache query results.**
2. **Generate a unique key based on the query (e.g., using a hash).**
3. **Check the cache first** before making a request to Cloud SQL.
4. **If the result is not in the cache, fetch from Cloud SQL and store the result in Memcache.**

This **reduces database load**, improves response time, and follows **Google-recommended best practices for Cloud SQL optimization**.

**Implementation Steps:**

**1. Enable Memcache with a Dedicated Tier**

- **Dedicated Memcache provides higher performance** and **better eviction policies** compared to shared Memcache.

```
runtime: phpenv: standardentrypoint: serveautomatic_scaling:  min_instances: 1  max_instances: 10beta_settings:  cloud_sql_instances: my-project:us-central1:my-cloudsql-instance  memcache_service: dedicated
```

**2. Implement Query Caching in PHP**

```
$memcache = new Memcached();$memcache->addServer('localhost', 11211); $query = "SELECT * FROM users WHERE id = 123";$cacheKey = md5($query);  // Create a hash of the query // Check if result is in cache$cachedResult = $memcache->get($cacheKey);if ($cachedResult) {    echo "Cache Hit: Returning data from Memcache";    return $cachedResult;} // If not in cache, fetch from Cloud SQL$db = new PDO('mysql:unix_socket=/cloudsql/my-project:us-central1:my-cloudsql-instance;dbname=mydb', 'root', '');$stmt = $db->prepare($query);$stmt->execute();$result = $stmt->fetchAll(PDO::FETCH_ASSOC); // Store result in cache for future requests$memcache->set($cacheKey, $result, 600); // Cache for 10 minutesecho "Cache Miss: Fetched from Cloud SQL";return $result;
```

- **Generates a unique cache key for each query** using `md5($query)`.
- **Checks the cache first** before querying Cloud SQL.
- **Caches results for 10 minutes** to avoid unnecessary database queries.

**Supporting Documentation:**

- **Using Memcache with App Engine**:
  https://cloud.google.com/appengine/docs/standard/php/memcache
- **Best Practices for Cloud SQL Performance**:
  https://cloud.google.com/sql/docs/mysql/performance

**Why Other Options Are Incorrect?**

**B. Set the memcache service level to dedicated. Configure a cron job that runs every minute to pre-populate the cache with keys containing query results.**

- **Inefficient approach** because **not all queries are predictable** or needed every minute.
- **Caches unnecessary data**, leading to **wasted memory**.

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard/php/memcache

**C. Set the memcache service level to shared. Configure a cron job that runs every minute to save all expected queries to a key called "cached_queries".**

- **Shared Memcache is less reliable and has more evictions** than dedicated Memcache.
- **Storing all queries in a single key ("cached_queries") is inefficient**, making retrieval slow.
- **Cron jobs every minute add unnecessary overhead** without guaranteeing relevant data is cached.

✅ **Reference:**
https://cloud.google.com/memorystore/docs/memcached

**D. Set the memcache service level to shared. Create a key called "cached_queries" and return database values from that key before issuing a query to Cloud SQL.**

- **A single cache key for all queries ("cached_queries") is not scalable**.
- **Each query should have its own cache key (hashed query).**
- **Shared Memcache is not ideal for production workloads with high query volume.**

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/performance

**Conclusion:**

The best approach is **A. Set the memcache service level to dedicated. Create a key from the hash of the query and return database values from memcache before issuing a query to Cloud SQL**, because:

- **It follows best practices for caching database queries.**
- **It reduces Cloud SQL queries and improves response times.**
- **It ensures query results are stored efficiently using a hashed key.**

**Final Reference:**
[https://cloud.google.com/appengine/docs/standard/php/memcache](https://cloud.google.com/appengine/docs/standard/php/memcache)

**⚠️ Note:** App Engine memcache is a legacy bundled service. Outside legacy App Engine runtimes, use the same read-through pattern with Memorystore.

---

## Question 36

*Domain 1: Designing and Planning a Cloud Solution Architecture*

You need to **ensure reliability** for your **application and operations** by implementing **reliable task scheduling** for **compute workloads** on **Google Cloud Platform (GCP)**. You want to follow **Google-recommended best practices**.

What should you do?

- [ ] A. Use the **Cron service in App Engine** to **publish messages directly** to a **message-processing utility service** running on **Compute Engine instances**.
- [x] B. Use the **Cron service in App Engine** to **publish messages to a Cloud Pub/Sub topic**. Subscribe to that topic using a **message-processing utility service** running on **Compute Engine instances**.
- [ ] C. Use the **Cron service in Google Kubernetes Engine (GKE)** to **publish messages directly** to a **message-processing utility service** running on **Compute Engine instances**.
- [ ] D. Use the **Cron service in Google Kubernetes Engine (GKE)** to **publish messages to a Cloud Pub/Sub topic**. Subscribe to that topic using a **message-processing utility service** running on **Compute Engine instances**.

### Explanation

**Correct Answer:**

**B. Use the Cron service in App Engine to publish messages to a Cloud Pub/Sub topic. Subscribe to that topic using a message-processing utility service running on Compute Engine instances.**

**Explanation:**

To ensure **reliable task scheduling for compute workloads** on **Google Cloud Platform (GCP)**, the best practice is to:

1. **Use App Engine's Cron Service** for scheduled task execution.
2. **Publish tasks to a Cloud Pub/Sub topic**, which provides a **reliable, distributed message queue**.
3. **Subscribe to Pub/Sub messages** from a message-processing utility running on **Compute Engine instances**.

This approach ensures:

- **Scalability:** Pub/Sub allows multiple subscribers, distributing the workload efficiently.
- **Reliability:** Pub/Sub guarantees **at least-once delivery**, ensuring no tasks are lost.
- **Decoupling:** App Engine's Cron service triggers tasks **without depending on Compute Engine directly**.

**Implementation Steps**

**1. Define a Cron Job in App Engine**

Create a `cron.yaml` file:

```
cron:- description: "Run scheduled compute workload"  url: /task  schedule: every 5 minutes
```

- This triggers an HTTP request every **5 minutes**.

**2. Publish Messages to Cloud Pub/Sub in App Engine**

Modify the App Engine **handler (`main.py`)** to publish to **Pub/Sub**:

```
from google.cloud import pubsub_v1from flask import Flask app = Flask(__name__) @app.route('/task')def schedule_task():    publisher = pubsub_v1.PublisherClient()    topic_path = publisher.topic_path("my-project", "my-topic")     message = "Run compute job"    publisher.publish(topic_path, message.encode("utf-8"))        return "Task scheduled", 200
```

- This **publishes a message** to a Cloud Pub/Sub topic.

**3. Create a Cloud Pub/Sub Subscriber on Compute Engine**

On Compute Engine, **subscribe and process messages**:

```
from google.cloud import pubsub_v1 def callback(message):    print(f"Received message: {message.data}")    message.ack()  # Acknowledge the message after processing subscriber = pubsub_v1.SubscriberClient()subscription_path = subscriber.subscription_path("my-project", "my-subscription") streaming_pull = subscriber.subscribe(subscription_path, callback=callback)print("Listening for messages...")streaming_pull.result()
```

- **Processes the scheduled task reliably** on Compute Engine.

**Supporting Documentation:**

- **Using App Engine Cron Jobs**:
  https://cloud.google.com/appengine/docs/standard/python3/scheduling-jobs-with-cron-yaml
- **Cloud Pub/Sub for Asynchronous Messaging**:
  https://cloud.google.com/pubsub/docs/overview

**Why Other Options Are Incorrect?**

**A. Use the Cron service in App Engine to publish messages directly to a message-processing utility service running on Compute Engine instances.**

- **Direct HTTP requests from App Engine to Compute Engine introduce tight coupling.**
- **Compute Engine instances may be unavailable at the scheduled time**, leading to **failed tasks**.
- **Cloud Pub/Sub provides a more reliable, decoupled mechanism.**

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard/python/taskqueue/

**C. Use the Cron service in Google Kubernetes Engine (GKE) to publish messages directly to a message-processing utility service running on Compute Engine instances.**

- **Using GKE's CronJobs requires running Kubernetes, which adds operational overhead.**
- **Directly invoking Compute Engine instances is unreliable.**
- **Cloud Pub/Sub provides a better event-driven architecture.**

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/how-to/cron-jobs

**D. Use the Cron service in Google Kubernetes Engine (GKE) to publish messages to a Cloud Pub/Sub topic. Subscribe to that topic using a message-processing utility service running on Compute Engine instances.**

- **Using GKE just for scheduling tasks is unnecessary overhead** when **App Engine's Cron service is simpler and fully managed**.
- **App Engine Cron is more cost-effective and efficient for scheduling periodic tasks.**

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs/concepts/jobs

**Conclusion:**

The best approach is **B. Use the Cron service in App Engine to publish messages to a Cloud Pub/Sub topic. Subscribe to that topic using a message-processing utility service running on Compute Engine instances**, because:

- **It ensures reliable, event-driven scheduling.**
- **It decouples scheduling from Compute Engine instances, improving flexibility.**
- **It follows Google Cloud best practices for scalable task scheduling.**

**Final Reference:**
[https://cloud.google.com/pubsub/docs/overview](https://cloud.google.com/pubsub/docs/overview)

**⚠️ Note:** Google's managed cron today is **Cloud Scheduler**, which can publish straight to a Pub/Sub topic. The pattern (scheduler → Pub/Sub → workers) is the same.

---

## Question 37

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company is building a new architecture to support its data-centric business operations. You are responsible for network setup.**

- **Mobile and web-facing applications will be hosted on-premises.**
- **All data analysis will be conducted in Google Cloud Platform (GCP).**
- **You need to process and upload 7 years of archived .csv files totaling 900 TB to Cloud Storage.**
- **Additionally, you will be ingesting 10 TB of new data daily.**
- **Your current internet connection is 100 Mbps.**

**What actions will best meet your company’s needs?**

- [ ] A. **Compress and upload** both **archived** and **daily files** using the **gsutil -m** option.
- [x] B. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a connection using **Dedicated Interconnect** or **Direct Peering** to upload **daily files**.
- [ ] C. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a **Cloud VPN Tunnel** over the **public internet** and **compress and upload daily files** using **gsutil -m**.
- [ ] D. **Lease a Transfer Appliance**, upload **archived files** to it, and send it to **Google** for **Cloud Storage transfer**. Establish a **Cloud VPN Tunnel** over the **public internet** and **upload daily files**.

### Explanation

**Correct Answer:**

**B. Lease a Transfer Appliance, upload archived files to it, and send it to Google for Cloud Storage transfer. Establish a connection using Dedicated Interconnect or Direct Peering to upload daily files.**

**Explanation:**

To efficiently handle **900 TB of archived data transfer** and **10 TB of new daily data ingestion**, Google Cloud recommends:

1. **Using Transfer Appliance for large-scale archival data transfer**
  - **900 TB of data is too large for an internet transfer**, which would take **over 2.5 years** with a **100 Mbps connection**.
  - **Google Transfer Appliance** allows you to **physically ship data** to Google, significantly reducing transfer time.
2. **Using Dedicated Interconnect or Direct Peering for daily data ingestion**
  - **10 TB daily data transfer over 100 Mbps internet is infeasible** (would take **over 9 days per batch**).
  - **Dedicated Interconnect (10 Gbps or more) or Direct Peering** ensures **high-speed, secure, and reliable data transfer**.

**Implementation Steps:**

**1. Transfer 900 TB Archived Data Using Google Transfer Appliance**

- **Order a Transfer Appliance** (up to **1 PB storage capacity**) from Google.
  ```
  gcloud transfer-appliance orders create --region=us-central1
  ```
- **Copy data to the appliance** locally using rsync:
  ```
  rsync -av /local/data /mnt/transfer-appliance/
  ```
- **Ship the appliance to Google for upload to Cloud Storage.**

✅ **Reference:** https://cloud.google.com/transfer-appliance

**2. Establish a High-Speed Connection for Daily 10 TB Transfers**

- **Dedicated Interconnect (10–100 Gbps)**
  ```
  gcloud compute interconnects create my-interconnect \    --customer-name=my-company \    --description="Dedicated Interconnect for 10TB Daily Transfer" \    --requested-link-count=2 \    --interconnect-type=DEDICATED
  ```
  - **Best for consistent, high-volume data transfer**.
  - **Secure, private connection** directly to Google Cloud.

OR

- **Direct Peering (1–10 Gbps)**
  - Connect **your on-premises network directly to Google's network**.
  - Lower latency compared to VPN.

✅ **Reference:** https://cloud.google.com/interconnect/docs/concepts/overview

**Why Other Options Are Incorrect?**

**A. Compress and upload both archived and daily files using the gsutil -m option.**

- **900 TB over a 100 Mbps connection would take ~2.5 years to upload**.
- **10 TB daily over 100 Mbps would take ~9+ days per batch**, making real-time ingestion impossible.
- **Not a practical solution for large-scale data transfers**.

✅ **Reference:**
https://cloud.google.com/storage/docs/gsutil/commands/cp

**C. Lease a Transfer Appliance for archives, then use Cloud VPN + gsutil -m for daily uploads.**

- **Cloud VPN is limited to 3 Gbps per tunnel (max 50 Gbps with multiple tunnels)**, which is **not sufficient for 10 TB daily ingestion**.
- **gsutil -m is inefficient for large daily data ingestion compared to Dedicated Interconnect or Peering**.

✅ **Reference:**
https://cloud.google.com/vpn/docs/concepts/overview

**D. Lease a Transfer Appliance for archives, then use Cloud VPN for daily uploads.**

- **Cloud VPN bandwidth limitations (3 Gbps per tunnel) make it unsuitable for sustained 10 TB daily transfers**.
- **Dedicated Interconnect or Direct Peering is the recommended solution for high-volume, reliable transfers**.

✅ **Reference:**
https://cloud.google.com/vpn/docs/concepts/overview

**Conclusion:**

The best solution is **B. Lease a Transfer Appliance, upload archived files to it, and send it to Google for Cloud Storage transfer. Establish a connection using Dedicated Interconnect or Direct Peering to upload daily files.**

This approach ensures:

- **Efficient bulk data transfer for 900 TB archived files**.
- **Fast and reliable daily ingestion of 10 TB via high-speed network connectivity**.
- **Compliance with Google Cloud best practices for data migration**.

✅ **Final Reference:**
[https://cloud.google.com/architecture/migrating-data-to-google-cloud](https://cloud.google.com/architecture/migrating-data-to-google-cloud)

---

## Question 38

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**You are developing a globally scaled frontend for a legacy streaming backend data API. The API requires events to arrive in strict chronological order with no duplicate data for proper processing.**

**Which Google Cloud products should you deploy to ensure guaranteed-once FIFO (first-in, first-out) delivery of data?**

- [ ] A. **Cloud Pub/Sub** alone.
- [x] B. **Cloud Pub/Sub** connected to **Cloud Dataflow**.
- [ ] C. **Cloud Pub/Sub** connected to **Stackdriver**.
- [ ] D. **Cloud Pub/Sub** connected to **Cloud SQL**.

### Explanation

**Correct Answer:**

**B. Cloud Pub/Sub connected to Cloud Dataflow.**

**Explanation:**

To ensure **guaranteed-once FIFO (first-in, first-out) delivery** of streaming events to a **legacy backend API**, you need a **reliable event processing pipeline** that guarantees:

1. **Strict chronological order** of events.
2. **No duplicate messages** (exactly-once delivery).
3. **Scalability for global operations**.

**How Cloud Pub/Sub + Cloud Dataflow Ensures FIFO & Exactly-Once Processing**

**1. Use Cloud Pub/Sub for Event Messaging**

- **Scalable, durable, and globally distributed message broker**.
- **However, it does not natively guarantee strict ordering or exactly-once delivery**.
- **Messages can be duplicated or delivered out of order.**

**2. Use Cloud Dataflow (Apache Beam) for Ordering & Deduplication**

- **Reorders messages based on timestamps before forwarding them**.
- **Ensures exactly-once processing with built-in deduplication**.
- **Applies event-time windowing to maintain strict order**.
- **Automatically scales for large data streams**.

**3. Send Processed Events to the Backend API**

- **The API receives correctly ordered, non-duplicate events**.

**Implementation Example (Apache Beam in Cloud Dataflow)**

This **Python Dataflow pipeline** enforces **FIFO ordering and deduplication** before sending data to the backend API:

```
import apache_beam as beamfrom apache_beam.options.pipeline_options import PipelineOptionsimport json # Define processing functiondef process_event(event):    # Extract timestamp and data    return (event['timestamp'], event['data']) pipeline_options = PipelineOptions(streaming=True) with beam.Pipeline(options=pipeline_options) as p:    (p     | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic="projects/my-project/topics/my-topic")     | "Parse JSON" >> beam.Map(lambda x: json.loads(x.decode('utf-8')))     | "Deduplicate" >> beam.Distinct()  # Removes duplicate events     | "Sort Chronologically" >> beam.transforms.combiners.Top.Largest(1000)  # Ensures FIFO order     | "Send to Backend" >> beam.io.WriteToText("gs://my-bucket/sorted-events.txt")  # Replace with API call    )
```

- **Uses `Distinct()` to remove duplicates**.
- **Sorts messages using timestamps to maintain FIFO order**.
- **Ensures reliable event delivery to the backend API**.

✅ **Reference:**
https://cloud.google.com/dataflow/docs/guides

**Why Other Options Are Incorrect?**

**A. Cloud Pub/Sub alone**

- **Cloud Pub/Sub does NOT guarantee FIFO order**.
- **Messages may arrive out of order or be duplicated due to retries**.
- **Cloud Dataflow is needed to enforce ordering and deduplication**.

✅ **Reference:**
https://cloud.google.com/pubsub/docs/ordering

**C. Cloud Pub/Sub connected to Stackdriver**

- **Stackdriver (Cloud Logging) is for monitoring and logging, not for data processing**.
- **It cannot enforce FIFO ordering or deduplicate messages**.

✅ **Reference:**
https://cloud.google.com/logging/docs

**D. Cloud Pub/Sub connected to Cloud SQL**

- **Cloud SQL does not process streaming data efficiently**.
- **It cannot enforce FIFO guarantees at scale**.
- **Cloud Dataflow is required to preprocess and order events before storage.**

✅ **Reference:**
https://cloud.google.com/sql/docs

**Conclusion:**

The best choice is **B. Cloud Pub/Sub connected to Cloud Dataflow**, because:

- **Cloud Dataflow ensures strict ordering and exactly-once delivery**.
- **Cloud Pub/Sub provides scalable, durable messaging**.
- **Meets Google Cloud best practices for real-time, ordered event processing**.

✅ **Final Reference:**
[https://cloud.google.com/dataflow/docs/guides](https://cloud.google.com/dataflow/docs/guides)

**⚠️ Note:** Pub/Sub alone now supports message ordering (ordering keys) and exactly-once delivery (pull subscriptions, within one region). The keyed Pub/Sub + Dataflow remains a safe answer when deduplication and global scale are needed.

---

## Question 39

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company plans to lift and shift its Linux RHEL 6.5+ virtual machines from an on-premises VMware environment to Google Cloud Compute Engine. You want to follow Google-recommended best practices for migration.**

**What should you do?**

- [ ] A. **Define a migration plan** based on a **list of applications and their dependencies**. **Migrate each virtual machine** individually to **Compute Engine** using **Migrate for Compute Engine**.
- [ ] B. **Assess the virtual machines** running in the **current VMware environment**. **Create images of all disks** and **import them into Compute Engine**. **Create standard virtual machines**, using the **imported boot disks**.
- [x] C. **Perform an assessment** of virtual machines in the **current VMware environment**. **Define a migration plan**, prepare a **Migrate for Compute Engine RunBook**, and **execute the migration**.
- [ ] D. **Assess the virtual machines** in the **current VMware environment**. **Install a third-party agent** on all selected virtual machines. **Migrate all virtual machines** to **Compute Engine**.

### Explanation

**Correct Answer:**

**C. Perform an assessment of virtual machines in the current VMware environment. Define a migration plan, prepare a Migrate for Compute Engine RunBook, and execute the migration.**

**Explanation:**

To successfully **lift and shift** RHEL **6.5+ virtual machines from an on-premises VMware environment to Google Cloud Compute Engine**, Google Cloud recommends using **Migrate for Compute Engine** (formerly Velostrata).

This approach ensures:

- **Automated, minimal-downtime migration.**
- **Preserving existing VM configurations.**
- **Post-migration testing to validate workloads in Compute Engine.**

**Key Steps for Best-Practice Migration Using Migrate for Compute Engine**

**1. Perform a Pre-Migration Assessment**

- **Use Migrate for Compute Engine’s assessment tools** to analyze the **VMs, dependencies, OS versions, and application requirements**.
- **Identify compatibility issues with Compute Engine** (e.g., deprecated drivers, OS requirements).
- **Determine networking, firewall, and storage configurations**.

**2. Define a Migration Plan**

- **Prioritize workloads based on business requirements** (e.g., critical apps first).
- **Prepare a RunBook** that includes:
  - **VM settings, dependencies, and expected downtime.**
  - **Network configuration in Google Cloud.**
  - **Testing and rollback plans.**

**3. Prepare for Migration**

- **Set up Google Cloud infrastructure**: VPC, subnets, firewall rules, and IAM permissions.
- **Deploy Migrate for Compute Engine Manager** in Google Cloud.
- **Install Migrate for Compute Engine components** in VMware.

**4. Execute the Migration**

- **Migrate workloads in batches** using Migrate for Compute Engine.
- **Validate VM functionality in Compute Engine** before finalizing the cutover.
- **Monitor the migration process via Google Cloud Console.**

**5. Optimize Post-Migration**

- **Upgrade or modernize VMs** to take advantage of cloud-native capabilities.
- **Decommission on-premises VMs after successful migration.**

**Supporting Documentation:**

- **Migrate for Compute Engine Overview**:
  https://cloud.google.com/migrate/compute-engine/docs/
- **VMware to Compute Engine Migration Guide**:
  https://cloud.google.com/migrate/compute-engine/docs/vmware-migration

**Why Other Options Are Incorrect?**

**A. Define a migration plan based on a list of applications and their dependencies. Migrate each virtual machine individually to Compute Engine using Migrate for Compute Engine.**

❌ **Incorrect:**

- **Migrating VMs one by one without a proper RunBook is inefficient.**
- **Does not mention pre-migration assessment**, which is critical for success.

✅ **Reference:**
https://cloud.google.com/migrate/compute-engine/docs/plan-migration

**B. Assess the virtual machines running in the current VMware environment. Create images of all disks and import them into Compute Engine. Create standard virtual machines, using the imported boot disks.**

❌ **Incorrect:**

- **Manual image creation is not efficient for large-scale migrations.**
- **Migrate for Compute Engine provides an automated, structured approach.**

✅ **Reference:**
https://cloud.google.com/migrate/compute-engine/docs/architecture

**D. Assess the virtual machines in the current VMware environment. Install a third-party agent on all selected virtual machines. Migrate all virtual machines to Compute Engine.**

❌ **Incorrect:**

- **Google recommends using Migrate for Compute Engine rather than third-party tools.**
- **Does not account for pre-migration planning and RunBook creation.**

✅ **Reference:**
https://cloud.google.com/migrate/compute-engine/docs/how-to/

**Conclusion:**

The best approach is **C. Perform an assessment of virtual machines in the current VMware environment. Define a migration plan, prepare a Migrate for Compute Engine RunBook, and execute the migration**, because:

- **It follows Google Cloud's best practices for VMware migration**.
- **Ensures minimal downtime and risk** through structured migration.
- **Utilizes Migrate for Compute Engine for automation and efficiency.**

✅ **Final Reference:**
[https://cloud.google.com/migrate/compute-engine/docs/vmware-migration](https://cloud.google.com/migrate/compute-engine/docs/vmware-migration)

**⚠️ Note:** Migrate for Compute Engine is now **Migrate to Virtual Machines**, part of Migration Center.

---

## Question 40

*Domain 1: Designing and Planning a Cloud Solution Architecture*

You need to **deploy an application** on **Google Cloud** that:

- **Receives traffic via TCP**
- **Reads and writes data** to the **filesystem**
- **Does not support horizontal scaling**
- **Requires full control over the filesystem data** (concurrent access causes corruption)
- **Must be available 24/7** but **can tolerate downtime** in case of an incident

How should you **design the architecture** for this application on **Google Cloud**?

- [ ] A. Use a **managed instance group** with instances in **multiple zones**, use **Cloud Filestore**, and deploy an **HTTP load balancer** in front of the instances.
- [ ] B. Use a **managed instance group** with instances in **multiple zones**, use **Cloud Filestore**, and deploy a **network load balancer** in front of the instances.
- [ ] C. Use an **unmanaged instance group** with an **active and standby instance** in different zones, use a **regional persistent disk**, and deploy an **HTTP load balancer** in front of the instances.
- [x] D. Use an **unmanaged instance group** with an **active and standby instance** in different zones, use a **regional persistent disk**, and deploy a **network load balancer** in front of the instances.

### Explanation

**Correct Answer:**

**D. Use an unmanaged instance group with an active and standby instance in different zones, use a regional persistent disk, and deploy a network load balancer in front of the instances.**

**Explanation:**

This application has several key requirements:

1. **Receives traffic via TCP** → Requires a **network load balancer** (not HTTP load balancer).
2. **Reads and writes to the filesystem** → Requires **persistent disk** (not shared storage like Filestore).
3. **Does not support horizontal scaling** → Must use **an active-standby architecture**.
4. **Full control over filesystem data (concurrent access causes corruption)** → **A single active writer setup** is needed.
5. **Must be available 24/7 but can tolerate downtime in case of an incident** → **Regional persistent disk with failover** is required.

**Why This Architecture Works**

**1. Use an Unmanaged Instance Group with Active/Standby Setup**

- Since **horizontal scaling is not supported**, a **managed instance group (MIG) is unnecessary**.
- **Unmanaged instance groups allow manual failover** between the **active and standby** instances.

**2. Use a Regional Persistent Disk for Data Storage**

- **A single active VM should access the disk at a time** (to prevent corruption).
- **Regional Persistent Disks are automatically replicated** across two zones for **high availability**.
- **Failover is manual** but ensures **data consistency** when switching to the standby instance.

**3. Use a Network Load Balancer for TCP Traffic**

- **The application uses TCP**, so a **network load balancer** is required.
- **HTTP load balancers only work for HTTP(S) traffic**, making them unsuitable for this scenario.

**Supporting Documentation:**

- **Regional Persistent Disk Overview:**
  https://cloud.google.com/compute/docs/disks#replication
- **Unmanaged Instance Groups:**
  https://cloud.google.com/compute/docs/instance-groups/unmanaged
- **Network Load Balancer (TCP/UDP Load Balancing):**
  https://cloud.google.com/load-balancing/docs/network

**Why Other Options Are Incorrect?**

**A. Use a managed instance group with instances in multiple zones, use Cloud Filestore, and deploy an HTTP load balancer in front of the instances.**

❌ **Incorrect:**

- **Filestore is a shared filesystem**, which **allows concurrent writes**, making it **unsuitable for applications that require exclusive filesystem access**.
- **HTTP Load Balancer does not support TCP traffic**.

✅ **Reference:**
https://cloud.google.com/filestore/docs/instances

**B. Use a managed instance group with instances in multiple zones, use Cloud Filestore, and deploy a network load balancer in front of the instances.**

❌ **Incorrect:**

- **Cloud Filestore does not guarantee exclusive access** to the filesystem.
- **Managed instance groups are designed for stateless applications that scale horizontally**, which **this application does not support**.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups

**C. Use an unmanaged instance group with an active and standby instance in different zones, use a regional persistent disk, and deploy an HTTP load balancer in front of the instances.**

❌ **Incorrect:**

- **HTTP Load Balancer is not designed for TCP-based applications**.
- **Network Load Balancer is the correct choice for handling TCP traffic.**

✅ **Reference:**
https://cloud.google.com/load-balancing/docs/network

**Conclusion:**

The best solution is **D. Use an unmanaged instance group with an active and standby instance in different zones, use a regional persistent disk, and deploy a network load balancer in front of the instances**, because:

- **It ensures high availability** via **active-standby failover**.
- **It prevents filesystem corruption** using a **regional persistent disk with a single writer**.
- **It supports TCP traffic** using a **network load balancer**.
- **It aligns with Google Cloud best practices for stateful workloads**.

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/instance-groups/unmanaged](https://cloud.google.com/compute/docs/instance-groups/unmanaged)

---

## Question 41

*Domain 2: Managing and Provisioning a Solution Infrastructure*

Your company has an **application running on multiple Compute Engine instances**. The application must **communicate with an on-premises service** that requires **high throughput** using **internal IP addresses**, while also **minimizing latency**.

What should you do?

- [ ] A. **Use OpenVPN** to set up a **VPN tunnel** between the **on-premises environment and Google Cloud**.
- [ ] B. **Configure a Direct Peering connection** between the **on-premises network and Google Cloud**.
- [ ] C. **Use Cloud VPN** to establish a **VPN tunnel** between the **on-premises environment and Google Cloud**.
- [x] D. **Set up a Cloud Dedicated Interconnect** between the **on-premises environment and Google Cloud**.

### Explanation

**Correct Answer:**

**D. Set up a Cloud Dedicated Interconnect between the on-premises environment and Google Cloud.**

**Explanation:**

The **key requirements** in this scenario are:

1. **High throughput** → Requires **a dedicated, high-bandwidth connection**.
2. **Internal IP communication** → **Traffic must not go over the public internet**.
3. **Minimized latency** → Needs a **low-latency, direct network path**.

The best solution is **Cloud Dedicated Interconnect**, which provides:

- **High-bandwidth options (10 Gbps or 100 Gbps)**, ideal for high-throughput applications.
- **Lower latency than VPN-based solutions**.
- **Direct, private communication using internal IP addresses** (no public internet).

**Implementation Steps**

**1. Order Dedicated Interconnect Capacity**

```
gcloud compute interconnects create my-interconnect \  --customer-name="My Company" \  --interconnect-type=DEDICATED \  --link-type=LINK_TYPE_ETHERNET_10G_LR \  --requested-link-count=2 \  --location=example-region
```

- **Provides a direct physical connection to Google Cloud.**
- **Supports 10 Gbps or 100 Gbps per link.**

**2. Configure VLAN Attachments**

```
gcloud compute interconnects attachments dedicated create my-vlan \  --region=example-region \  --interconnect=my-interconnect
```

- **Connects the on-prem network to Google Cloud VPC via VLAN attachments.**

✅ **Reference:**
https://cloud.google.com/interconnect/docs/concepts/dedicated-overview

**Why Other Options Are Incorrect?**

**A. Use OpenVPN to set up a VPN tunnel between the on-premises environment and Google Cloud.**

❌ **Incorrect:**

- **OpenVPN is a software-based VPN solution** that relies on the public internet.
- **High throughput is not guaranteed**, and **latency is higher** compared to Dedicated Interconnect.

✅ **Reference:**
https://cloud.google.com/vpn/docs/concepts/overview

**B. Configure a Direct Peering connection between the on-premises network and Google Cloud.**

❌ **Incorrect:**

- **Direct Peering does not allow access to internal IP addresses** (only Google public services).
- **It is not a private connection to Google Cloud VPC.**
- **Traffic is still routed over the internet** (not suitable for minimizing latency).

✅ **Reference:**
https://cloud.google.com/network-connectivity/docs/direct-peering

**C. Use Cloud VPN to establish a VPN tunnel between the on-premises environment and Google Cloud.**

❌ **Incorrect:**

- **Cloud VPN runs over the public internet**, which results in **higher latency**.
- **Cloud VPN supports only up to 3 Gbps per tunnel**, which is **insufficient for high throughput** workloads.

✅ **Reference:**
https://cloud.google.com/vpn/docs/concepts/overview

**Conclusion:**

The best solution is **D. Set up a Cloud Dedicated Interconnect between the on-premises environment and Google Cloud**, because:

- **It provides a private, high-speed connection using internal IP addresses.**
- **It minimizes latency and supports high throughput.**
- **It follows Google Cloud's best practices for hybrid connectivity.**

✅ **Final Reference:**
[https://cloud.google.com/interconnect/docs/concepts/dedicated-overview](https://cloud.google.com/interconnect/docs/concepts/dedicated-overview)

---

## Question 42

*Domain 5: Managing Implementation*

You are managing an **application deployed on Cloud Run for Anthos**. You need to define a **deployment strategy** that allows you to **evaluate a new version of the application** by **sending a subset of production traffic** before proceeding with a full rollout.

What should you do?

- [x] A. **Deploy a new revision** of the application to **Cloud Run** with the updated version and **configure traffic splitting** between the current and new revisions.
- [ ] B. **Deploy a new service** to **Cloud Run** with the updated version and use **Cloud Load Balancing** to distribute traffic between both services.
- [ ] C. In the **Google Cloud Console**, enable **continuous deployment** using **Cloud Build** for the development branch. As part of the **Cloud Build trigger**, configure the **TRAFFIC_PERCENTAGE** substitution variable to control the amount of traffic sent to the new version.
- [ ] D. In the **Google Cloud Console**, configure **Traffic Director** with a **new Service** that points to the updated application version on **Cloud Run**. Use **Traffic Director** to send a **small percentage of traffic** to the new version.

### Explanation

**Correct Answer:**

**A. Deploy a new revision of the application to Cloud Run with the updated version and configure traffic splitting between the current and new revisions.**

**Explanation:**

Cloud Run for Anthos **supports gradual rollouts** using **traffic splitting** between different revisions of a service. This allows you to **route a percentage of production traffic** to the new version **before completing a full rollout**, which is a **best practice for canary deployments**.

By **deploying a new revision and splitting traffic**, you can:

1. **Send a small percentage of users** to the new version.
2. **Monitor performance and errors** in the new version.
3. **Gradually increase traffic allocation** until full deployment.
4. **Roll back quickly** in case of failures.

**How to Implement Traffic Splitting in Cloud Run for Anthos**

**1. Deploy a new revision of the application**

Run the following command to deploy the new version:

```
gcloud run deploy my-service \  --image=gcr.io/my-project/new-version-image \  --platform=gke \  --namespace=my-namespace
```

**2. Configure Traffic Splitting Between Revisions**

Set **90% traffic** to the current revision and **10% traffic** to the new revision:

```
gcloud run services update-traffic my-service \  --to-revisions=current-revision=90,new-revision=10 \  --platform=gke \  --namespace=my-namespace
```

- This **routes 10% of live traffic** to the new version for testing.
- **If no issues are detected**, gradually increase the percentage.

✅ **Reference:**
https://cloud.google.com/run/docs/rollouts-rollbacks

**Why Other Options Are Incorrect?**

**B. Deploy a new service to Cloud Run with the updated version and use Cloud Load Balancing to distribute traffic between both services.**

❌ **Incorrect:**

- Cloud Run services **cannot be directly used with Cloud Load Balancer** for traffic splitting.
- **Cloud Run handles traffic routing via revisions, not multiple services**.

✅ **Reference:**
https://cloud.google.com/run/docs/rollouts-rollbacks

**C. Enable continuous deployment using Cloud Build for the development branch and configure the TRAFFIC_PERCENTAGE variable.**

❌ **Incorrect:**

- **Cloud Build does not control traffic splitting directly.**
- **TRAFFIC_PERCENTAGE is not a valid Cloud Run deployment parameter**.
- **Traffic splitting must be configured at the service level in Cloud Run.**

✅ **Reference:**
https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run

**D. Configure Traffic Director with a new service that points to the updated application version on Cloud Run.**

❌ **Incorrect:**

- **Traffic Director is used for advanced service mesh scenarios (e.g., GKE, hybrid environments)**, but **not required for basic Cloud Run traffic splitting**.
- **Cloud Run has built-in traffic management capabilities** without needing Traffic Director.

✅ **Reference:**
https://cloud.google.com/traffic-director/docs/overview

**Conclusion:**

The best choice is **A. Deploy a new revision of the application to Cloud Run with the updated version and configure traffic splitting between the current and new revisions**, because:

- **It follows Google Cloud best practices for gradual rollouts**.
- **It allows controlled testing before a full deployment**.
- **It provides an easy rollback mechanism if needed**.

✅ **Final Reference:**
[https://cloud.google.com/run/docs/rollouts-rollbacks](https://cloud.google.com/run/docs/rollouts-rollbacks)

**⚠️ Note:** Cloud Run for Anthos is now Knative serving on GKE Enterprise, and Traffic Director is now Cloud Service Mesh. The rule is unchanged: deploy a new revision and split traffic between revisions.

---

## Question 43

*Domain 6: Ensuring Solution and Operations Excellence*

You are **monitoring Google Kubernetes Engine (GKE) clusters** in a **Cloud Monitoring workspace**. As a **Site Reliability Engineer (SRE)**, you need to **triage incidents quickly**.

What should you do?

- [x] A. Use the **predefined dashboards** in the **Cloud Monitoring workspace**, then **add relevant metrics** and **create alert policies**.
- [ ] B. Use the **predefined dashboards** in the **Cloud Monitoring workspace**, create **custom metrics**, and **install alerting software** on a **Compute Engine instance**.
- [ ] C. Develop a **shell script** that gathers **GKE node metrics**, publishes the data to **Pub/Sub**, exports it to **BigQuery**, and visualizes it in **Data Studio**.
- [ ] D. Create a **custom dashboard** in the **Cloud Monitoring workspace** for **each incident**, then **add relevant metrics** and **set up alert policies**.

### Explanation

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

---

## Question 44

*Domain 3: Designing for Security and Compliance*

You are working for a **sports association** with **members aged 8 to 30**. The organization **collects health-related data**, including **sustained injuries**, and stores it in **BigQuery**.

Legislation requires that **personal health data must be deleted upon request** of the individual. You need to **design a solution** that allows for compliance with these requests.

What should you do?

- [x] A. Use a **unique identifier** for each individual. When a **deletion request** is received, **delete all rows** in **BigQuery** that contain this identifier.
- [ ] B. Before storing new data in **BigQuery**, process it through the **Data Loss Prevention (DLP) API** to identify personal information. Save the results in **Data Catalog**, and upon a **deletion request**, query **Data Catalog** to identify and remove the relevant personal data.
- [ ] C. Create a **BigQuery view** over the original data table. Upon a **deletion request**, modify the view to **exclude rows** related to the subject while keeping the original data intact. Use this view for all analysis tasks.
- [ ] D. Use a **unique identifier** for each individual. Upon a **deletion request**, replace the identifier with a **salted SHA256 hash** instead of deleting the data.

### Explanation

**Correct Answer:**

**A. Use a unique identifier for each individual. When a deletion request is received, delete all rows in BigQuery that contain this identifier.**

**Explanation:**

The **key legal requirement** is to **delete personal health data upon an individual's request**, which aligns with **data privacy laws like GDPR (Right to Erasure) and HIPAA**.

- **BigQuery does not support row-level deletions automatically**, so you must explicitly delete affected rows.
- The **best approach is to use a unique identifier** for each individual so that all relevant records can be deleted efficiently when requested.

**Implementation Steps in BigQuery**

1. **Ensure all records have a unique identifier (e.g., `member_id`)**.
2. **Use a DELETE statement to remove records when a request is received**:
  ```
  DELETE FROM `project.dataset.health_data`WHERE member_id = '12345';
  ```
3. **Regularly audit the dataset** to ensure compliance with deletion requests.

✅ **This method ensures complete data deletion, fulfilling the legal requirement.**

**Why Other Options Are Incorrect?**

**B. Before storing new data in BigQuery, process it through the Data Loss Prevention (DLP) API to identify personal information. Save the results in Data Catalog, and upon a deletion request, query Data Catalog to identify and remove the relevant personal data.**

❌ **Incorrect:**

- **DLP API is used for detecting and classifying sensitive data**, not for managing deletions.
- **Data Catalog stores metadata, not actual data**, so it cannot be used to remove personal records from BigQuery.

✅ **Reference:** https://cloud.google.com/data-catalog/docs

**C. Create a BigQuery view over the original data table. Upon a deletion request, modify the view to exclude rows related to the subject while keeping the original data intact. Use this view for all analysis tasks.**

❌ **Incorrect:**

- **Views do not delete the underlying data**—they just filter it.
- **The original data remains stored**, which does not comply with legal deletion requirements.

✅ **Reference:** https://cloud.google.com/bigquery/docs/views-intro

**D. Use a unique identifier for each individual. Upon a deletion request, replace the identifier with a salted SHA256 hash instead of deleting the data.**

❌ **Incorrect:**

- **Hashing the identifier does not remove personal health data**.
- **Other personally identifiable information (PII) still exists in the record**, violating legal requirements.

✅ **Reference:** https://cloud.google.com/security/compliance

**Conclusion:**

The best approach is **A. Use a unique identifier for each individual and delete all rows associated with it upon request**, because:

- **It fully complies with legal requirements (GDPR, HIPAA, etc.).**
- **It ensures that personal health data is completely removed.**
- **It follows Google Cloud best practices for data deletion in BigQuery.**

✅ **Final Reference:**
[https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#delete](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#delete)

---

## Question 45

*Domain 1: Designing and Planning a Cloud Solution Architecture*

Your company has decided to **outsource operations functions**. You need a solution that allows **developers to stage new versions** of a **cloud-based application** in the **production environment**, while enabling the **outsourced operations team** to **autonomously promote staged versions to production**.

You also want to **minimize operational overhead**.

Which **Google Cloud product** should you migrate to?

- [x] A. App Engine
- [ ] B. GKE On-Prem
- [ ] C. Compute Engine
- [ ] D. Google Kubernetes Engine (GKE)

### Explanation

**Correct Answer:**

**A. App Engine**

**Explanation:**

The **key requirements** in this scenario are:

1. **Developers can stage new versions** of an application in the **production environment**.
2. **The outsourced operations team** must have control to **promote staged versions to production**.
3. **Minimize operational overhead** → Requires a **fully managed** solution.

Google **App Engine** is the **best choice** because:

- **Supports versioning & traffic splitting**: Developers can **deploy multiple versions**, and the **operations team can promote a new version** with **zero downtime**.
- **Fully managed (low operational overhead)**: **No infrastructure management** is needed, unlike Compute Engine or GKE.
- **Automatic scaling** and **integrated monitoring** simplify **deployment and operations management**.

**How App Engine Meets the Requirements**

**1. Staging New Versions in Production**

- Developers can **deploy multiple versions** of the application:
  ```
  gcloud app deploy app-v2.yaml --version=v2
  ```
- **The application runs in production**, but traffic is **not yet switched**.

**2. Operations Team Can Promote the Version Autonomously**

- The outsourced team **can shift traffic** to the new version **gradually**:
  ```
  gcloud app services set-traffic my-service --splits v1=50,v2=50
  ```
- **Zero downtime switching** ensures a smooth transition.

**3. Minimal Operational Overhead**

- **No need to manage VMs, clusters, or networking**.
- **Google automatically handles scaling, updates, and security patches**.

✅ **Reference:**
https://cloud.google.com/appengine/docs/standard

**Why Other Options Are Incorrect?**

**B. GKE On-Prem**

❌ **Incorrect:**

- **Requires managing Kubernetes clusters on-prem**, which increases **operational overhead**.
- **Does not minimize infrastructure management**, violating the requirement.

✅ **Reference:**
https://cloud.google.com/anthos/gke/docs/on-prem

**C. Compute Engine**

❌ **Incorrect:**

- **Requires manual instance management**.
- **No built-in versioning or traffic splitting** → Promotions require **manual orchestration**.
- **Higher operational overhead compared to App Engine**.

✅ **Reference:**
https://cloud.google.com/compute

**D. Google Kubernetes Engine (GKE)**

❌ **Incorrect:**

- **Requires managing Kubernetes clusters** → **higher operational complexity**.
- **Needs manual CI/CD setup for versioning and promotions**.
- **More suited for microservices rather than simple versioned deployments**.

✅ **Reference:**
https://cloud.google.com/kubernetes-engine/docs

**Conclusion:**

The best option is **A. App Engine**, because:

- **It allows developers to stage new versions** while the **operations team promotes them autonomously**.
- **Traffic splitting ensures smooth rollouts**.
- **Fully managed with minimal operational overhead**.

✅ **Final Reference:**
[https://cloud.google.com/appengine/docs/standard](https://cloud.google.com/appengine/docs/standard)

---

## Question 46

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

Your company runs **application workloads** on **Compute Engine** across **production, acceptance, and development environments**.

- The **production environment** is **business-critical** and operates **24/7**.
- The **acceptance and development environments** are only **critical during office hours**.
- Your **CFO** has asked you to **optimize costs** by **reducing expenses during idle times**.

What should you do?

- [ ] A. **Create a shell script** that uses the **gcloud command** to **change the machine type** of **development and acceptance instances** to a **smaller machine type** outside office hours. Schedule the script on a **production instance** to automate this task.
- [x] B. **Use Cloud Scheduler** to trigger a **Cloud Function** that **stops the development and acceptance environments after office hours** and **starts them before office hours**.
- [ ] C. **Deploy the development and acceptance applications** on a **managed instance group** and **enable autoscaling** to scale down resources during idle times.
- [ ] D. Use **regular Compute Engine instances** for the **production environment**, and **preemptible VMs** for the **acceptance and development environments** to reduce costs.

### Explanation

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

---

## Question 47

*Domain 3: Designing for Security and Compliance*

Your organization has decided to **restrict the use of external IP addresses** on Compute Engine instances, allowing **only approved instances** to have external access. You need to **enforce this policy** across **all Virtual Private Clouds (VPCs)**.

What should you do?

- [ ] A. **Remove the default route** on all **VPCs** and move all **approved instances** into a **new subnet** that has a **default route to an internet gateway**.
- [ ] B. **Create a new VPC** in **custom mode**, then create a **new subnet** for the **approved instances**, and set a **default route to the internet gateway** for this subnet.
- [ ] C. **Implement a Cloud NAT solution** to **eliminate the need for external IP addresses** entirely.
- [x] D. **Set an Organization Policy** with a **constraint on** `constraints/compute.vmExternalIpAccess`, and list the **approved instances** in the **allowedValues list**.

### Explanation

**Correct Answer:**

**D. Set an Organization Policy with a constraint on constraints/compute.vmExternalIpAccess, and list the approved instances in the allowedValues list.**

**Explanation:**

The **best approach** to **enforce** the restriction of external IPs **across all Virtual Private Clouds (VPCs)** is to use **Google Cloud Organization Policy Service**, specifically the **compute.vmExternalIpAccess constraint**.

✅ **Organization Policy allows centralized enforcement** of security policies across all **projects and VPCs**.
✅ **The `compute.vmExternalIpAccess` constraint restricts the assignment of external IPs**, except for **approved instances** that are explicitly allowed.
✅ **Ensures compliance and security**, preventing unauthorized access to external networks.

**How to Implement This?**

**1. Set an Organization Policy to Restrict External IP Access**

Run the following **gcloud command** to **enforce the policy** and allow only **approved instances**:

```
gcloud org-policies set-policy compute-vm-external-ip.yaml
```

Where `compute-vm-external-ip.yaml` contains:

```
constraint: constraints/compute.vmExternalIpAccesslistPolicy:  allowedValues:    - projects/project-id/zones/zone/instances/approved-instance-1    - projects/project-id/zones/zone/instances/approved-instance-2  deniedValues:    - "*"
```

- **Only `approved-instance-1` and `approved-instance-2` are allowed external IPs**.
- **All other instances are denied from getting an external IP**.

✅ **Reference:**
https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints

**Why Other Options Are Incorrect?**

**A. Remove the default route on all VPCs and move all approved instances into a new subnet that has a default route to an internet gateway.**

❌ **Incorrect:**

- **Default routes control internet access, not external IP assignment**.
- **Removing the default route would prevent all instances (even approved ones) from accessing the internet**.
- **Does not scale well** if new VPCs are created in the future.

✅ **Reference:**
https://cloud.google.com/vpc/docs/routes

**B. Create a new VPC in custom mode, then create a new subnet for the approved instances, and set a default route to the internet gateway for this subnet.**

❌ **Incorrect:**

- **Creating a new VPC does not enforce policy across all existing VPCs**.
- **It does not prevent unapproved instances from having external IPs**.
- **New instances in other VPCs could still get external IPs**, making this ineffective for enforcement.

✅ **Reference:**
https://cloud.google.com/vpc/docs/vpc

**C. Implement a Cloud NAT solution to eliminate the need for external IP addresses entirely.**

❌ **Incorrect:**

- **Cloud NAT is used for outbound internet access without external IPs**, but it **does not restrict external IP assignments**.
- **Unapproved instances could still be assigned external IPs**, violating the policy requirement.

✅ **Reference:**
https://cloud.google.com/nat/docs/overview

**Conclusion:**

The best approach is **D. Set an Organization Policy with a constraint on** `constraints/compute.vmExternalIpAccess`, because:

- **It applies across all projects and VPCs** within the organization.
- **Only approved instances are allowed external IPs**.
- **It enforces security best practices in Google Cloud**.

✅ **Final Reference:**
[https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)

---

## Question 48

*Domain 6: Ensuring Solution and Operations Excellence*

Your company is using **Firewall Insights** in **Google Network Intelligence Center** to analyze **firewall rules applied to Compute Engine instances**.

You need to **evaluate the efficiency** of your **firewall ruleset**, but when you open the **Firewall Insights page** in the **Google Cloud Console**, **no log entries** are displayed.

How should you troubleshoot this issue?

- [ ] A. Enable Virtual Private Cloud (VPC) flow logging.
- [x] B. Enable Firewall Rules Logging for the firewall rules you want to monitor.
- [ ] C. Verify that your user account has the compute.networkAdmin IAM role.
- [ ] D. Install the Google Cloud SDK and check for Firewall logs using the command-line output.

### Explanation

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

---

## Question 49

*Domain 3: Designing for Security and Compliance*

Your company stores **sensitive data** in **Cloud Storage buckets**, and **data analysts** have **IAM permissions** to **read** from these buckets. You need to **prevent analysts from accessing the data from outside the office network** while maintaining access from within the office.

What should you do?

- [x] A. **Create a VPC Service Controls perimeter** that includes the **projects containing the Cloud Storage buckets**. **Define an access level** that restricts access based on the **CIDR range of the office network**.
- [ ] B. **Create a firewall rule** for all **Compute Engine instances** in the **VPC network**. **Use the office network's CIDR range** as the **source range** in the firewall rule.
- [ ] C. **Create a Cloud Function** to **remove IAM permissions** from the buckets, and another **Cloud Function** to **restore IAM permissions**. **Use Cloud Scheduler** to automatically **add permissions at the start of business hours** and **remove them at the end of business hours**.
- [ ] D. **Set up a Cloud VPN connection** to the **office network**. **Enable Private Google Access** for **on-premises hosts** to restrict access to **Cloud Storage** through the VPN.

### Explanation

**Correct Answer:**

**A. Create a VPC Service Controls perimeter that includes the projects containing the Cloud Storage buckets. Define an access level that restricts access based on the CIDR range of the office network.**

**Explanation:**

The **best approach** to **restrict access to Cloud Storage data based on the office network** is to use **VPC Service Controls (VPC-SC)**.

✅ **VPC Service Controls enhances security** by **preventing unauthorized data access from outside the defined network perimeter**.
✅ **Access Context Manager allows you to define an access level** based on **the office network’s CIDR range**, ensuring analysts can **only access Cloud Storage from within the office**.
✅ **IAM permissions alone do not restrict access based on location**, so **VPC-SC is needed**.

**How to Implement This?**

**1. Create a VPC Service Controls Perimeter**

Run the following command to **enforce a security perimeter** around Cloud Storage:

```
gcloud access-context-manager perimeters create sensitive-data-perimeter \  --policy=YOUR_ORG_POLICY_ID \  --resources=projects/YOUR_PROJECT_ID \  --restricted-services=storage.googleapis.com
```

**2. Define an Access Level Restricting Access to the Office Network**

```
gcloud access-context-manager levels create office-access \  --policy=YOUR_ORG_POLICY_ID \  --title="Office Network Access" \  --conditions='ipSubnetworks=["203.0.113.0/24"]'
```

- Replace `203.0.113.0/24` with **your office network’s CIDR range**.

**3. Attach the Access Level to the VPC Service Controls Perimeter**

```
gcloud access-context-manager perimeters update sensitive-data-perimeter \  --policy=YOUR_ORG_POLICY_ID \  --add-access-levels=office-access
```

✅ **Reference:**
https://cloud.google.com/vpc-service-controls/docs/overview

**Why Other Options Are Incorrect?**

**B. Create a firewall rule for all Compute Engine instances in the VPC network. Use the office network's CIDR range as the source range in the firewall rule.**

❌ **Incorrect:**

- **Firewall rules apply to Compute Engine instances** but **do not restrict access to Cloud Storage**.
- **Cloud Storage is a managed service**, and **firewall rules do not apply to Google-managed services like Cloud Storage**.

✅ **Reference:**
https://cloud.google.com/vpc/docs/firewalls

**C. Create a Cloud Function to remove IAM permissions from the buckets, and another Cloud Function to restore IAM permissions. Use Cloud Scheduler to automatically add permissions at the start of business hours and remove them at the end of business hours.**

❌ **Incorrect:**

- **IAM permissions control user access but do not enforce network-based restrictions**.
- **This approach is complex and error-prone**—if permissions are not restored properly, analysts may lose access when needed.
- **Data analysts could still access Cloud Storage from outside the office while IAM permissions are active**.

✅ **Reference:**
https://cloud.google.com/iam/docs/granting-changing-revoking-access

**D. Set up a Cloud VPN connection to the office network. Enable Private Google Access for on-premises hosts to restrict access to Cloud Storage through the VPN.**

❌ **Incorrect:**

- **Private Google Access allows private network access but does not restrict public access**.
- **Cloud VPN alone does not enforce access restrictions**—users can still connect from outside if they have IAM permissions.
- **Does not prevent data access from non-office networks**.

✅ **Reference:**
https://cloud.google.com/vpc/docs/private-google-access

**Conclusion:**

The best approach is **A. Create a VPC Service Controls perimeter that includes the projects containing the Cloud Storage buckets and define an access level restricting access to the office network**, because:

- **It enforces security at the service level, beyond IAM permissions**.
- **Prevents unauthorized access from non-office networks**.
- **It is a Google-recommended best practice for securing sensitive data in Cloud Storage**.

✅ **Final Reference:**
[https://cloud.google.com/vpc-service-controls/docs/overview](https://cloud.google.com/vpc-service-controls/docs/overview)

---

## Question 50

*Domain 5: Managing Implementation*

You have developed a **non-critical update** for your **application running in a managed instance group (MIG)** and have created a **new instance template** containing the update.

To **avoid any disruption**, you **do not** want to update **existing instances**. However, you want **any newly created instances** in the **managed instance group** to use the **new instance template**.

What should you do?

- [ ] A. **Start a rolling restart operation** to apply the new template to instances.
- [ ] B. **Start a rolling replace operation** to replace instances one at a time with the new template.
- [ ] C. **Start a rolling update** and select the **Proactive update mode** to immediately update instances.
- [x] D. **Start a rolling update** and select the **Opportunistic update mode** to apply the new template only to newly created instances.

### Explanation

**Correct Answer:**

**D. Start a rolling update and select the Opportunistic update mode to apply the new template only to newly created instances.**

**Explanation:**

The **requirement** is to ensure **new instances** in the **Managed Instance Group (MIG)** use the **new instance template**, while **existing instances remain unchanged**.

✅ **Opportunistic update mode** allows you to **apply the new instance template only to newly created instances**, **without modifying existing ones**.
✅ This **avoids service disruption** while ensuring that **future scaling uses the updated configuration**.
✅ **Existing instances continue running normally**, and only when **autoscaling or manual scaling adds new instances, they will use the new template**.

**How to Implement This?**

**Update the Instance Template in Opportunistic Mode**

Run the following command:

```
gcloud compute instance-groups managed rolling-action start-update MIG_NAME \    --version=template=NEW_INSTANCE_TEMPLATE \    --type=opportunistic
```

- Replace `MIG_NAME` with the name of the **managed instance group**.
- Replace `NEW_INSTANCE_TEMPLATE` with the **new instance template** you want to apply.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#update_policy

**Why Other Options Are Incorrect?**

**A. Start a rolling restart operation to apply the new template to instances.**

❌ **Incorrect:**

- **Rolling restart only restarts instances—it does not apply a new instance template**.
- **It does not ensure that new instances use the new template**.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#rolling-restart

**B. Start a rolling replace operation to replace instances one at a time with the new template.**

❌ **Incorrect:**

- **Rolling replace replaces all existing instances, which is disruptive**.
- **The requirement is to keep existing instances running**—this option does not meet that condition.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#rolling-replace

**C. Start a rolling update and select the Proactive update mode to immediately update instances.**

❌ **Incorrect:**

- **Proactive update mode immediately replaces instances**—causing **disruption**.
- **We need to ensure existing instances remain unchanged**—this option **does not meet the requirement**.

✅ **Reference:**
https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#proactive

**Conclusion:**

The best approach is **D. Start a rolling update and select the Opportunistic update mode**, because:

- **It ensures only new instances use the new template**.
- **Existing instances remain unchanged, avoiding disruption**.
- **It follows Google Cloud best practices for non-disruptive updates**.

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#update_policy](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#update_policy)

---

## Question 51

*Domain 2: Managing and Provisioning a Solution Infrastructure*

Your company has **acquired another company**, and you need to **integrate their existing Google Cloud environment** with your **on-premises data center**.

Upon investigation, you find that some of the **RFC 1918 IP ranges** in the **new company's Virtual Private Cloud (VPC)** **overlap** with the **IP space** in your **data center**.

To enable **connectivity** while ensuring that there are **no routing conflicts**, what should you do?

- [ ] A. **Create a Cloud VPN connection** from the new VPC to the data center, then **set up a Cloud Router** and **assign new IP addresses** to avoid overlapping IP space.
- [x] B. Create a Cloud VPN connection between the new VPC and the data center, and configure **Cloud NAT Private NAT / Hybrid NAT** to translate the overlapping IP ranges to non-overlapping address ranges.
- [ ] C. **Create a Cloud VPN connection** from the new VPC to the data center, then **set up a Cloud Router** and apply a **custom route advertisement** to **block the overlapping IP space**.
- [ ] D. **Create a Cloud VPN connection** from the new VPC to the data center, and configure a **firewall rule** to **block traffic from the overlapping IP space**.

### Explanation

**Correct Answer:**

**B. Create a Cloud VPN connection from the new VPC to the data center, and configure Cloud NAT Private NAT / Hybrid NAT to translate the overlapping IP ranges to non-overlapping address ranges.**

**Explanation:**

The problem arises due to **overlapping RFC 1918 IP ranges** between the **new company's VPC and the on-premises data center**. This causes **routing conflicts**, preventing proper network communication.

✅ **Cloud NAT (Network Address Translation) is the best solution** because:

- It allows **translation of overlapping IP addresses** so that both environments can communicate **without conflicts**.
- **Ensures that source and destination IPs do not overlap** when packets are forwarded.
- NAT **enables private workloads in the VPC to communicate with on-premises systems via VPN without IP conflicts**.

**How to Implement This Solution?**

**1. Establish a Cloud VPN Connection to the On-Premises Data Center**

Run the following command to create a **Cloud VPN gateway**:

```
gcloud compute vpn-gateways create my-vpn-gateway \    --network=my-vpc-network \    --region=us-central1
```

**2. Configure a Cloud NAT Instance for IP Address Translation**

Run the following command to **create a Cloud NAT instance**:

```
gcloud compute routers create my-cloud-router \    --network=my-vpc-network \    --region=us-central1 gcloud compute routers nats create my-nat \    --router=my-cloud-router \    --region=us-central1 \    --nat-custom-subnet-ip-ranges=my-subnet
```

- **This NAT instance translates overlapping IP addresses**, avoiding conflicts.

✅ **Reference:**
https://cloud.google.com/nat/docs/overview

**Why Other Options Are Incorrect?**

**A. Create a Cloud VPN connection from the new VPC to the data center, then set up a Cloud Router and assign new IP addresses to avoid overlapping IP space.**

❌ **Incorrect:**

- **Assigning new IP addresses requires re-architecting the network**, which is complex and disruptive.
- **Renumbering IP addresses in a production environment is not practical.**
- **Cloud Router does not automatically resolve IP conflicts**—it only manages BGP route advertisements.

✅ **Reference:**
https://cloud.google.com/network-connectivity/docs/router/concepts/overview

**C. Create a Cloud VPN connection from the new VPC to the data center, then set up a Cloud Router and apply a custom route advertisement to block the overlapping IP space.**

❌ **Incorrect:**

- **Blocking overlapping IPs prevents communication entirely**, which is not the goal.
- **The requirement is to enable connectivity while avoiding conflicts, not to block communication**.
- **Cloud Router manages dynamic routing but does not resolve overlapping IP issues.**

✅ **Reference:**
https://cloud.google.com/network-connectivity/docs/router/concepts/advertising-routes

**D. Create a Cloud VPN connection from the new VPC to the data center, and configure a firewall rule to block traffic from the overlapping IP space.**

❌ **Incorrect:**

- **Blocking traffic defeats the purpose of integrating both networks**.
- **Firewalls control access but do not resolve overlapping IP issues**.
- **The requirement is to ensure seamless connectivity, not to block traffic.**

✅ **Reference:**
https://cloud.google.com/vpc/docs/firewalls

**Conclusion:**

The best solution is **B. Create a Cloud VPN connection from the new VPC to the data center, and configure Cloud NAT Private NAT / Hybrid NAT to translate the overlapping IP ranges to non-overlapping address ranges**, because:

- **It enables communication between the networks while resolving IP conflicts.**
- **Cloud NAT ensures that overlapping IPs do not interfere with routing.**
- **This follows Google Cloud best practices for handling overlapping IP ranges in hybrid networks.**

✅ **Final Reference:**
[https://cloud.google.com/nat/docs/overview](https://cloud.google.com/nat/docs/overview)

**⚠️ Note:** **Hybrid NAT** is Private NAT for traffic from a VPC to on-premises or other-cloud networks over Cloud VPN or Cloud Interconnect. It translates VPC source addresses into a non-overlapping `PRIVATE_NAT` subnet range and needs dynamic (Cloud Router) routing. It only translates traffic that starts in the VPC.

---

## Question 52

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Which solution should you choose to ensure the application is quickly restored in another zone with the latest data whenever a zonal outage occurs on Compute Engine?**

- [ ] A. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in the same zone.
- [x] B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another zone in the same region. Use the regional persistent disk for the application data.
- [ ] C. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in another zone within the same region.
- [ ] D. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another region. Use the regional persistent disk for the application data.

### Explanation

**Correct Answer:**

**B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another zone in the same region. Use the regional persistent disk for the application data.**

**Explanation:**

The **best way to ensure high availability in case of a zonal outage** is to use:

- **Regional Persistent Disks (PDs)**: These **synchronously replicate** data across two zones in a **single region** to ensure the latest data is always available in another zone.
- **Instance Templates**: These allow for rapid provisioning of **Compute Engine instances** in another zone **automatically** when a failure occurs.
- **Multi-Zone Deployment**: Ensures the application can be **quickly restored within the same region** without manual intervention.

✅ **Key Advantages of This Approach:**

- **Regional PDs automatically replicate data between two zones**, ensuring minimal data loss.
- **Instance templates simplify failover**, allowing new instances to be created quickly in an alternative zone.
- **This solution follows Google Cloud best practices for high availability and disaster recovery**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks#repds

**Why Other Options Are Incorrect?**

**A. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in the same zone.**

❌ **Incorrect:**

- **Snapshots are NOT real-time and do not offer high availability.** They are **asynchronous backups**, meaning data loss could occur if a failure happens between snapshots.
- **Restoring a disk in the same zone is not possible if the entire zone is down.**
- **Snapshots take time to restore, which delays recovery.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/snapshots

**C. Create a snapshot schedule for the disk containing the application data. Whenever a zonal outage occurs, use the latest snapshot to restore the disk in another zone within the same region.**

❌ **Incorrect:**

- **Snapshots are not a real-time failover mechanism.** Data loss is possible between snapshots.
- **Manually restoring a disk from a snapshot takes time**, which results in **longer downtime** compared to a **regional persistent disk** that offers **automatic failover**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/snapshots

**D. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data. Whenever a zonal outage occurs, use the instance template to spin up the application in another region. Use the regional persistent disk for the application data.**

❌ **Incorrect:**

- **Regional Persistent Disks are limited to a single region**, so they cannot be used across different regions.
- **A region-wide outage is extremely rare**, and Google Cloud **recommends a multi-zone setup within a region rather than multi-region unless necessary**.
- **For cross-region high availability, Cloud Storage, Cloud SQL, or Spanner would be better suited instead of Regional PDs**.

✅ **Reference:**
https://cloud.google.com/compute/docs/disks#repds

**Conclusion:**

The best approach is **B. Configure the Compute Engine instances with an instance template for the application, and use a regional persistent disk for the application data**, because:

- **It enables automatic failover to another zone within the same region**.
- **It ensures the latest data is available via Regional Persistent Disks**.
- **It follows Google Cloud best practices for disaster recovery and high availability**.

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/disks#repds](https://cloud.google.com/compute/docs/disks#repds)

---

## Question 53

*Domain 1: Designing and Planning a Cloud Solution Architecture*

Your company's **Data Science team** needs to **migrate Hadoop jobs** to **Google Cloud** without modifying the **underlying infrastructure**. You also want to **minimize costs** and **reduce infrastructure management efforts**.

What should you do?

- [ ] A. Create a Dataproc cluster using standard worker instances.
- [x] B. Create a Dataproc cluster using preemptible worker instances.
- [ ] C. Manually deploy a Hadoop cluster on Compute Engine using standard instances.
- [ ] D. Manually deploy a Hadoop cluster on Compute Engine using preemptible instances.

### Explanation

**Correct Answer:**

**B. Create a Dataproc cluster using preemptible worker instances.**

**Explanation:**

The **best approach** to migrate Hadoop jobs to **Google Cloud** **without modifying the underlying infrastructure** while **minimizing costs** and **reducing infrastructure management** is to use **Google Cloud Dataproc with preemptible worker instances**.

✅ **Google Cloud Dataproc** is a **fully managed Hadoop and Spark service**, which allows the **Data Science team to run existing Hadoop jobs without infrastructure modifications**.
✅ **Preemptible worker instances** **drastically reduce costs** (by up to 80%) while still allowing non-critical workloads to run efficiently.
✅ **Dataproc provides automated scaling, monitoring, and integration with other Google Cloud services**, reducing operational overhead.

**How to Implement This?**

**1. Create a Dataproc Cluster with Preemptible Workers**

Run the following command:

```
gcloud dataproc clusters create my-dataproc-cluster \    --region=us-central1 \    --num-workers=2 \    --num-preemptible-workers=4 \    --worker-machine-type=n1-standard-4 \    --image-version=2.0-debian10
```

- This command **creates a Dataproc cluster** with **2 standard workers and 4 preemptible workers**.
- **Preemptible workers handle temporary workloads at a lower cost.**

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/preemptible-vms

**Why Other Options Are Incorrect?**

**A. Create a Dataproc cluster using standard worker instances.**

❌ **Incorrect:**

- **This option is functional but not cost-effective.**
- **Standard worker instances increase costs significantly**, whereas preemptible workers reduce costs by up to 80%.
- **Preemptible instances should be used when cost optimization is a priority**.

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-pricing

**C. Manually deploy a Hadoop cluster on Compute Engine using standard instances.**

❌ **Incorrect:**

- **Manually deploying Hadoop on Compute Engine requires extensive infrastructure management**, including node provisioning, configuration, and scaling.
- **Dataproc automates Hadoop deployment, making it easier to manage and scale**.
- **Higher operational overhead** compared to a managed Dataproc solution.

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/overview

**D. Manually deploy a Hadoop cluster on Compute Engine using preemptible instances.**

❌ **Incorrect:**

- **While preemptible instances lower costs, manually deploying Hadoop increases complexity and management efforts.**
- **Dataproc automates deployment and scales dynamically, making it a better choice than manual deployment.**

✅ **Reference:**
https://cloud.google.com/dataproc/docs/concepts/overview

**Conclusion:**

The best solution is **B. Create a Dataproc cluster using preemptible worker instances**, because:

- **It enables running Hadoop jobs without modifying the infrastructure.**
- **Preemptible instances reduce costs while maintaining performance.**
- **Dataproc automates infrastructure management, reducing operational overhead.**

✅ **Final Reference:**
[https://cloud.google.com/dataproc/docs/concepts/preemptible-vms](https://cloud.google.com/dataproc/docs/concepts/preemptible-vms)

---

## Question 54

*Domain 6: Ensuring Solution and Operations Excellence*

You need to **deploy an application** on **Google Cloud** that must run on a **Debian Linux environment**.

- The application requires **extensive configuration** to function properly.
- You want to ensure that **Debian distribution updates** can be **installed with minimal manual intervention** whenever they become available.

What should you do?

- [ ] A. **Create a Compute Engine instance template** using the **latest Debian image**. Deploy an **instance from the template** and configure the application via a **startup script**. Repeat this process when a **new Google-managed Debian image** is released.
- [x] B. **Create a Debian-based Compute Engine instance**, install and configure the application, and use **OS patch management** to automatically apply available updates.
- [ ] C. **Deploy an instance with the latest Debian image**, connect via **SSH**, and manually **install and configure** the application. Repeat this process whenever a **new Google-managed Debian image** is available.
- [ ] D. **Create a Docker container** with **Debian as the base image**. Install and configure the application as part of the **Docker image creation**. Deploy the contai

### Explanation

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

---

## Question 55

*Domain 6: Ensuring Solution and Operations Excellence*

Your **application runs on Google Kubernetes Engine (GKE)**. Over the past **two weeks**, customers have reported that a **specific part of the application** is **frequently returning errors**.

- You **do not have any logging or monitoring** enabled on the GKE cluster.
- You have **not been able to replicate the issue**.
- You need to **diagnose the problem** while causing **minimal disruption** to the application.

What should you do?

- [x] A.**Enable Cloud Operations for GKE** on your **existing cluster**. Use the **GKE Monitoring dashboard** to **analyze logs** from the affected Pods.
- [ ] B.**Create a new GKE cluster** with **Cloud Operations for GKE enabled**. **Migrate the affected Pods** to the **new cluster** and **redirect traffic** to it. Use the **GKE Monitoring dashboard** to **analyze logs** from the affected Pods.
- [ ] C.**Enable Cloud Operations for GKE** on your **existing cluster** and **deploy Prometheus**. **Set an alert** to **trigger when errors occur** in the application.
- [ ] D.**Create a new GKE cluster** with **Cloud Operations for GKE enabled** and **deploy Prometheus**. **Migrate the affected Pods** to the **new cluster** and **redirect traffic** to it. **Set an alert** to **trigger when errors occur**.

### Explanation

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

---

## Question 56

*Domain 1: Designing and Planning a Cloud Solution Architecture*

You need to **deploy a stateful workload** on **Google Cloud**.

- The **workload can scale horizontally**.
- Each instance must **read and write to the same POSIX filesystem**.
- Under **high load**, the workload must support **up to 100 MB/s of writes**.

What should you do?

- [ ] A. **Use a persistent disk** for each instance.
- [ ] B. **Use a regional persistent disk** for each instance.
- [x] C. **Create a Cloud Filestore instance** and **mount it on each instance**.
- [ ] D. **Create a Cloud Storage bucket** and **mount it on each instance** using **gcsfuse**.

### Explanation

**Correct Answer:**

**C. Create a Cloud Filestore instance and mount it on each instance.**

**Explanation:**

The **best solution for a stateful workload** that requires **a shared POSIX filesystem with high write throughput** (**100 MB/s**) is **Google Cloud Filestore**.

✅ **Cloud Filestore provides a fully managed NFS (Network File System) solution**, ensuring multiple instances **can read and write to the same filesystem**.
✅ **POSIX-compliant**: Ensures that all instances **can simultaneously read and write** while maintaining filesystem consistency.
✅ **Supports high throughput**: Filestore’s **performance tier can handle up to multiple GB/s of writes**.

**How to Implement This?**

**1. Create a Cloud Filestore Instance**

```
gcloud filestore instances create my-filestore \    --zone=us-central1-a \    --tier=high-scale \    --file-share=name="myshare",capacity=5TB \    --network=name=default
```

- **This creates a Filestore instance** with **high performance** to meet the 100 MB/s write requirement.

**2. Mount Cloud Filestore on Compute Engine Instances**

```
sudo mkdir -p /mnt/filestoresudo mount -o vers=3,hard,timeo=600,retrans=2 nfs-server-ip:/myshare /mnt/filestore
```

- **This mounts the shared Cloud Filestore storage on each instance**, allowing multiple instances to read/write.

✅ **Reference:**
https://cloud.google.com/filestore/docs/creating-instances

**Why Other Options Are Incorrect?**

**A. Use a persistent disk for each instance.**

❌ **Incorrect:**

- **Persistent disks are NOT shared storage**—each instance gets a separate disk.
- **POSIX-compliant filesystem access is not possible across multiple instances.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks

**B. Use a regional persistent disk for each instance.**

❌ **Incorrect:**

- **Regional Persistent Disks are replicated across zones but are still attached to only one VM at a time.**
- **They do not support concurrent access by multiple instances.**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/regional-persistent-disk

**D. Create a Cloud Storage bucket and mount it on each instance using gcsfuse.**

❌ **Incorrect:**

- **Cloud Storage is not a POSIX-compliant filesystem.**
- `gcsfuse` **allows access to Cloud Storage, but it does not support concurrent file locking or low-latency operations required for high-throughput writes.**
- **Not designed for workloads requiring shared file storage with 100 MB/s of writes.**

✅ **Reference:**
https://cloud.google.com/storage/docs/gcs-fuse

**Conclusion:**

The best option is **C. Create a Cloud Filestore instance and mount it on each instance**, because:

- **It supports concurrent POSIX-compliant read/write access**.
- **It provides the required high throughput of 100 MB/s or more**.
- **It ensures data consistency across multiple instances**.
- **It follows Google Cloud best practices for shared storage in a stateful workload.**

✅ **Final Reference:**
[https://cloud.google.com/filestore](https://cloud.google.com/filestore)

---

## Question 57

*Domain 6: Ensuring Solution and Operations Excellence*

Your company has an **application deployed on Anthos clusters (formerly Anthos GKE)** running **multiple microservices**.

- The **cluster is configured** with **Anthos Service Mesh** and **Anthos Config Management**.
- **End users** have reported that the application is **responding very slowly**.
- You need to **identify which microservice is causing the delay**.

What should you do?

- [x] A. **Use the Service Mesh visualization** in the **Google Cloud Console** to inspect **telemetry data** between the microservices.
- [ ] B. **Use Anthos Config Management** to create a **ClusterSelector** for the relevant cluster. Then, in the **Google Kubernetes Engine (GKE) console**, navigate to **Workloads**, filter by cluster, and inspect the **workload configurations**.
- [ ] C. **Use Anthos Config Management** to create a **NamespaceSelector** for the relevant namespace. Then, in the **Google Kubernetes Engine (GKE) console**, navigate to **Workloads**, filter by namespace, and inspect the **workload configurations**.
- [ ] D. **Reinstall Istio** using the **default Istio profile** to enable **request latency tracking**, then analyze the **telemetry data** between microservices in the **Google Cloud Console**.

### Explanation

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

---

## Question 58

*Domain 3: Designing for Security and Compliance*

You are working at a **financial institution** that stores **mortgage loan approval documents** on **Cloud Storage**.

- **Any changes** to these documents must be **uploaded as separate approval files**.
- You need to ensure that **documents cannot be deleted or overwritten** for the **next 5 years**.

What should you do?

- [x] A. **Set a retention policy** on the **Cloud Storage bucket** for **5 years** and **lock the retention policy** to prevent modifications.
- [ ] B. **Create the bucket** with **uniform bucket-level access** and grant a **service account** the **Object Writer role**. Use this service account to **upload new files**.
- [ ] C. **Use a customer-managed encryption key (CMEK)** for the **bucket encryption** and **rotate the key** after **5 years**.
- [ ] D. **Create the bucket** with **fine-grained access control** and grant a **service account** the **Object Writer role**. Use this service account to **upload new files**.

### Explanation

**Correct Answer:**

**A. Set a retention policy on the Cloud Storage bucket for 5 years and lock the retention policy to prevent modifications.**

**Explanation:**

Since **mortgage loan approval documents must be retained for 5 years without deletion or modification**, the **best approach** is to **use a Cloud Storage retention policy** and **lock it** to prevent accidental or intentional modifications.

✅ **Cloud Storage Retention Policy** ensures:

- **Objects cannot be deleted or overwritten until the retention period expires.**
- **Enforcement at the bucket level**—no user, even administrators, can modify or delete objects until the retention period ends.
- **Regulatory compliance**, making it ideal for financial institutions handling sensitive documents.

Once **locked**, the retention policy **cannot be reduced or removed**, ensuring **data integrity** for the required duration.

**How to Implement This?**

**1. Create a Cloud Storage Bucket with a Retention Policy**

```
gcloud storage buckets create my-mortgage-bucket \    --location=us-central1 \    --retention-period=1825d
```

- This **creates a Cloud Storage bucket** with a **5-year (1825 days) retention policy**.

**2. Lock the Retention Policy to Prevent Modifications**

```
gcloud storage buckets lock my-mortgage-bucket
```

- **Locking the retention policy ensures that no one can delete or overwrite files before 5 years.**

✅ **Reference:**
https://cloud.google.com/storage/docs/bucket-lock

**Why Other Options Are Incorrect?**

**B. Create the bucket with uniform bucket-level access and grant a service account the Object Writer role. Use this service account to upload new files.**

❌ **Incorrect:**

- **Object Writer role allows adding new files but does NOT prevent deletions or overwrites.**
- **Without a retention policy, an admin could still delete objects manually.**

✅ **Reference:**
https://cloud.google.com/storage/docs/access-control/iam-roles

**C. Use a customer-managed encryption key (CMEK) for the bucket encryption and rotate the key after 5 years.**

❌ **Incorrect:**

- **Encryption does not prevent deletion or overwriting of files.**
- **CMEK ensures data security but does not enforce a retention period.**

✅ **Reference:**
https://cloud.google.com/storage/docs/encryption

**D. Create the bucket with fine-grained access control and grant a service account the Object Writer role. Use this service account to upload new files.**

❌ **Incorrect:**

- **Fine-grained access control is useful for access management but does not enforce data retention.**
- **Users with sufficient permissions could still delete or modify objects.**

✅ **Reference:**
https://cloud.google.com/storage/docs/access-control/iam-roles

**Conclusion:**

The best solution is **A. Set a retention policy on the Cloud Storage bucket for 5 years and lock the retention policy to prevent modifications**, because:

- **It ensures regulatory compliance and data retention.**
- **It prevents data loss by blocking deletions and overwrites before the retention period expires.**
- **It follows Google Cloud best practices for financial institutions handling sensitive documents.**

✅ **Final Reference:**
[https://cloud.google.com/storage/docs/bucket-lock](https://cloud.google.com/storage/docs/bucket-lock)

---

## Question 59

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

Your team is beginning **development of a new application** using a **microservices architecture** on **Google Kubernetes Engine (GKE)**.

- **Any code change** pushed to the **develop branch** on **GitHub** must be **automatically built and tested**.
- If the **build and test succeed**, the **corresponding microservice** should be **automatically deployed** in the **development environment**.
- You need to **enforce this process** for all **code deployed** to the **development environment**.

What should you do?

- [ ] A. Require each **developer** to install a **pre-commit hook** on their local workstation that **tests the code** and **builds the container** before committing to the **development branch**. After a **successful commit**, the developer **manually deploys** the newly built container to the **development cluster**.
- [ ] B. Set up a **post-commit hook** on the **remote GitHub repository** that **tests the code** and **builds the container** when changes are pushed to the **development branch**. After a **successful build**, the developer **manually deploys** the newly built container to the **development cluster**.
- [x] C. **Configure a Cloud Build trigger** that **automatically builds and tests** any code pushed to the **development branch**. Store the built container in **Container Registry**. Set up a **deployment pipeline** that **automatically watches for new images** and **deploys them** to the **development cluster**, ensuring that only the **deployment tool** has permissions to deploy new versions.
- [ ] D. **Set up a Cloud Build trigger** for the **development branch** that **builds a new container image** and **stores it in Container Registry**. Use **Vulnerability Scanning** to verify the code’s integrity. As the **final step of the Cloud Build process**, deploy the **new container image** to the **development cluster**, ensuring that only **Cloud Build** has permissions to deploy new versions.

### Explanation

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

---

## Question 60

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**The Director of Engineering mandates migrating all development infrastructure resources from on-premises virtual machines (VMs) to Google Cloud to reduce costs. These resources undergo multiple start/stop cycles daily and necessitate state persistence. You've been tasked with designing the process for running a development environment in Google Cloud while ensuring cost visibility for the finance department. What two steps should you take? (Choose two)**

- [x] A. Utilize persistent disks to store the state and start/stop the VMs as required.
- [ ] B. Implement the "gcloud --auto-delete" flag on all persistent disks before stopping the VMs.
- [ ] C. Apply a label for VM CPU utilization and incorporate it into the BigQuery billing export.
- [x] D. Utilize BigQuery billing export and labels to associate costs with specific groups.
- [ ] E. Store all state in a Local SSD, snapshot the persistent disks, and terminate the VMs.

### Explanation

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

---

## Question 61

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**The database administration team seeks assistance in enhancing the performance of their new database server hosted on Compute Engine. This MySQL-based database serves to import and normalize the company's performance statistics and operates on Debian Linux. The current setup consists of an n1-standard-8 virtual machine with an 80 GB SSD zonal persistent disk, which cannot be restarted until the next maintenance event. What change should they implement to promptly and cost-effectively improve system performance?**

- [ ] A. Increase the virtual machine's memory to 64 GB.
- [ ] B. Deploy a new virtual machine running PostgreSQL.
- [x] C. Dynamically resize the SSD persistent disk to 500 GB.
- [ ] D. Migrate their performance metrics warehouse to BigQuery.

### Explanation

**Correct Answer:**

**C. Dynamically resize the SSD persistent disk to 500 GB.**

**Explanation:**

The **best and most cost-effective way** to improve performance **without requiring a restart** is to **resize the SSD persistent disk**.

✅ **Why Increasing Disk Size Improves Performance?**

- **Google Cloud SSD persistent disks provide higher IOPS and throughput as size increases.**
- **Larger SSD persistent disks receive higher performance limits.**
  - Example:
    - **80 GB SSD Disk:** ~8,400 IOPS (6,000 baseline + 30 per GB)
    - **500 GB SSD Disk:** ~21,000 IOPS (higher read/write performance)
- **No VM restart is required for resizing a persistent disk.**

🔹 **Steps to Resize Persistent Disk Without Restart:**

1. **Increase disk size dynamically** using the command:
  ```
  gcloud compute disks resize my-disk --size=500GB --zone=my-zone
  ```
2. **Resize the filesystem on the disk** to utilize the new space:
  ```
  sudo resize2fs /dev/sdX  # Replace sdX with the actual device name
  ```
3. **Verify new disk performance using `fio` (optional).**

✅ **Reference:**
https://cloud.google.com/compute/docs/disks/resize-persistent-disk

**Why Other Options Are Incorrect?**

**A. Increase the virtual machine's memory to 64 GB.**

❌ **Incorrect:**

- **Cannot be done without restarting the VM** (which is not allowed until maintenance).
- **Does not necessarily improve disk I/O performance**, which is the likely bottleneck in MySQL workloads.

✅ **Reference:**
https://cloud.google.com/compute/docs/machine-types

**B. Deploy a new virtual machine running PostgreSQL.**

❌ **Incorrect:**

- **Requires major changes** (database migration from MySQL to PostgreSQL).
- **Does not address the immediate performance issue**.
- **PostgreSQL vs. MySQL performance depends on the workload**, but migration is not the fastest solution.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql

**D. Migrate their performance metrics warehouse to BigQuery.**

❌ **Incorrect:**

- **BigQuery is for analytics, not transactional workloads like MySQL.**
- **Moving to BigQuery requires schema and query rewrites**, which is not an immediate solution.
- **Does not address MySQL performance bottlenecks.**

✅ **Reference:**
https://cloud.google.com/bigquery

**Conclusion:**

The best option is **C. Dynamically resize the SSD persistent disk to 500 GB**, because:

- **It increases IOPS and throughput immediately.**
- **No VM restart is required, avoiding downtime.**
- **It is cost-effective and follows Google Cloud best practices.**

✅ **Final Reference:**
[https://cloud.google.com/compute/docs/disks/resize-persistent-disk](https://cloud.google.com/compute/docs/disks/resize-persistent-disk)

---

## Question 62

*Domain 1: Designing and Planning a Cloud Solution Architecture*

You are deploying a **single Cloud SQL MySQL second-generation database** that stores **business-critical transaction data**.

To **minimize data loss** in case of a **catastrophic failure**, which **two features** should you implement? (Choose two.)

- [ ] A. Sharding
- [ ] B. Read replicas
- [x] C. Binary logging
- [x] D. Automated backups
- [ ] E. Semisynchronous replication

### Explanation

**Correct Answers:**

**C. Binary logging**
**D. Automated backups**

**Explanation:**

For a **business-critical Cloud SQL MySQL** database, **minimizing data loss** in case of a catastrophic failure requires **proper backups and point-in-time recovery mechanisms**.

✅ **Option C: Binary Logging**

- **Enables Point-in-Time Recovery (PITR)** by logging all changes (INSERT, UPDATE, DELETE).
- **Captures transaction history**, allowing recovery up to the last committed transaction before failure.
- **Essential for disaster recovery** when used with automated backups.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/enable-binary-logging

✅ **Option D: Automated Backups**

- **Cloud SQL provides daily automated backups**, ensuring data can be restored if a failure occurs.
- **Allows full recovery of the database** in case of corruption or accidental deletion.
- **Can be combined with binary logs for point-in-time recovery**.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/backup-recovery/backups

**Why Other Options Are Incorrect?**

**A. Sharding**

❌ **Incorrect:**

- **Sharding distributes data across multiple instances** for **scalability, not disaster recovery**.
- **It does not provide data protection**—data loss can still occur if backups or binary logging are not enabled.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/scale-out-using-sharding

**B. Read replicas**

❌ **Incorrect:**

- **Read replicas improve read performance** and provide **high availability** but **are not designed for disaster recovery**.
- **Data loss can propagate to replicas if a failure occurs** (e.g., accidental DELETE operations).
- **Read replicas do not support PITR** (point-in-time recovery).

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/replication

**E. Semisynchronous Replication**

❌ **Incorrect:**

- **Provides high availability, not data recovery**.
- **Data replication is synchronous, but if both primary and replicas fail, data is still lost**.
- **Replication alone does not prevent data loss if backups are not taken**.

✅ **Reference:**
https://cloud.google.com/sql/docs/mysql/high-availability

**Conclusion:**

To **minimize data loss** in **Google Cloud SQL MySQL**, the best approach is:

1. **Enable Binary Logging (C)** for **Point-in-Time Recovery (PITR)**.
2. **Use Automated Backups (D)** for **full database recovery**.

✅ **Final References:**

- **Binary Logging:** [https://cloud.google.com/sql/docs/mysql/enable-binary-logging](https://cloud.google.com/sql/docs/mysql/enable-binary-logging)
- **Automated Backups:** https://cloud.google.com/sql/docs/mysql/backup-recovery/backups

---
