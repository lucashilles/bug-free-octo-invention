# Domain 5 — Managing Implementation

33 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q39

**You are working in Cloud Shell and need to install a custom utility that will be available in the default execution path and persist across sessions for future use. Where should you store the file?**

- A. `~/bin`
- B. **Google Cloud Storage**
- C. `/google/scripts`
- D. `/usr/local/bin`

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. `~/bin`

**Correct Answer:**

✅ **A. `~/bin`

Explanation:**

In **Cloud Shell**, the best place to store a **custom utility** that should:

1. **Be available in the default execution path (`$PATH`)**
2. **Persist across Cloud Shell sessions**

is `~/bin` **(Home Directory `bin` folder)**.

✅ **Why `~/bin`?**

- **Cloud Shell home directory (`~/`) persists across sessions.**
- **Files stored in `~/bin` are automatically included in `$PATH`.**
- **Users have write permissions in** `~/bin`, unlike system directories (`/usr/local/bin`).

**Implementation:**

1. **Create the `bin` directory (if it does not exist):**
  ```
  mkdir -p ~/bin
  ```
2. **Move your custom utility to `~/bin`:**
  ```
  tmv my_custom_utility ~/bin/chmod +x ~/bin/my_custom_utility
  ```
3. **Ensure `~/bin` is in your `$PATH`:**
  ```
  echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrcsource ~/.bashrc
  ```
4. **Verify the utility is available:**
  ```
  which my_custom_utility
  ```

✅ **Supporting Documentation:**

- **Cloud Shell Environment**
- **Using Cloud Shell Home Directory**

**Why Other Options Are Incorrect?**

**B. Google Cloud Storage** ❌

- **GCS (`gs://`) is for storing objects, not for executing utilities.**
- **Cloud Shell does not execute binaries directly from Cloud Storage.**
- **Not in** `$PATH`, so the custom utility wouldn’t be easily accessible.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/**

**C.** `/google/scripts` ❌

- **This is a system directory managed by Google Cloud.**
- **Not writable by users**, so a custom utility cannot be installed there.
- **Changes here do not persist across sessions.**

✅ **Reference:**

- **https://cloud.google.com/shell/docs**

**D.** `/usr/local/bin` ❌

- **Cloud Shell does not allow writes to `/usr/local/bin/`.**
- **Files placed here do not persist across sessions.**
- **Users do not have the necessary permissions to install utilities here in Cloud Shell.**

✅ **Reference:**

- **https://cloud.google.com/shell/docs/configuring-cloud-shell**

**Conclusion:**

The best place to **store a custom utility** in **Cloud Shell** so it:
✔ **Persists across sessions**
✔ **Is in the default** `$PATH`
✔ **Is writable by the user**

is `~/bin` (**Option A**).

📌 **Final Reference:**
**https://cloud.google.com/shell/docs/configuring-cloud-shell#files-persistent-storage**

</details>

---

### Exam 1 · Q48

**You have discovered an error in your App Engine application caused by missing Cloud Datastore indexes. To resolve this, you have created a YAML configuration file specifying the required indexes.**

**How should you deploy these new indexes to Cloud Datastore?**

- A. Use the command `gcloud datastore create-indexes` and specify your configuration file.
- B. Upload the **YAML configuration file** to **App Engine’s default Cloud Storage bucket**, allowing App Engine to detect the new indexes.
- C. In the **Google Cloud Console**, navigate to **Datastore Admin**, delete the current indexes, and upload the new configuration file.
- D. Send an **HTTP request** to the **built-in Python module** to upload the index configuration file to your application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use the command `gcloud datastore create-indexes` and specify your configuration file.

**Correct Answer:**

✅ **A. Use the command `gcloud datastore indexes create` and specify your configuration file.**

**Explanation:**

To deploy new indexes to **Cloud Datastore**, you need to use the **Google Cloud CLI (`gcloud`)** to apply the YAML configuration file that defines the indexes.

**Correct Procedure to Deploy Indexes:**

1. **Create or modify an `index.yaml` file** that defines the required indexes.
2. **Deploy the indexes using the following command:**
  ```
  gcloud datastore indexes create index.yaml
  ```
3. **Verify that the indexes are being built** by checking the status in the **Google Cloud Console → Datastore → Indexes**.

✅ **Why This Works:**

- `gcloud datastore indexes create` is the recommended way to deploy index configurations.
- **Indexes must be explicitly created in Cloud Datastore** before queries can use them.
- **Once submitted, indexes are automatically built by Cloud Datastore** and available for querying.

✅ **Supporting Documentation:**

- **Managing Datastore Indexes:**
  **https://cloud.google.com/datastore/docs/tools/indexconfig**
- **Deploying Indexes Using `gcloud` CLI:**
  **https://cloud.google.com/datastore/docs/creating-indexes**

**Why Other Options Are Incorrect?**

**B. Upload the YAML configuration file to App Engine’s default Cloud Storage bucket, allowing App Engine to detect the new indexes.** ❌

- **App Engine does not automatically detect new index configurations from Cloud Storage.**
- **Cloud Datastore requires an explicit deployment using the `gcloud` CLI.**
- **Storing the YAML file in Cloud Storage has no effect on Datastore indexing.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/tools/indexconfig**

**C. In the Google Cloud Console, navigate to Datastore Admin, delete the current indexes, and upload the new configuration file.** ❌

- **There is no option to manually upload an `index.yaml` file in the Google Cloud Console.**
- **Deleting indexes can break existing queries**—instead, new indexes should be added incrementally.
- **Indexes are created and modified using the `gcloud` CLI or the Datastore Admin API.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/tools/indexconfig**

**D. Send an HTTP request to the built-in Python module to upload the index configuration file to your application.** ❌

- **There is no built-in Python module in App Engine for deploying Datastore indexes.**
- **Index creation must be explicitly managed via** `gcloud datastore indexes create`.
- **Datastore does not support uploading index configurations via HTTP requests.**

✅ **Reference:**

- **https://cloud.google.com/datastore/docs/creating-indexes**

**Conclusion:**

The best approach is **A. Use the command `gcloud datastore indexes create` and specify your configuration file**, because:

- **This is the official method to deploy Cloud Datastore indexes.**
- **It ensures the indexes are properly registered and built.**
- **It follows Google Cloud’s best practices for managing index configurations.**

📌 **Final Reference:**
**https://cloud.google.com/datastore/docs/tools/indexconfig**

**⚠️ Note:** `gcloud datastore create-indexes` is the older, deprecated form of the command; the current one is `gcloud datastore indexes create index.yaml`. Cloud Datastore is now Firestore in Datastore mode.

</details>

---

### Exam 1 · Q52

**Your company is migrating 75 TB of data to Google Cloud and plans to store it in Cloud Storage. You want to follow Google-recommended best practices for this data transfer.**

**What should you do?**

- A. Transfer the data onto a **Transfer Appliance**, then use a **Transfer Appliance Rehydrator** to decrypt and upload the data to **Cloud Storage**.
- B. Transfer the data onto a **Transfer Appliance**, then use **Cloud Dataprep** to decrypt and upload the data to **Cloud Storage**.
- C. Install **gsutil** on each **server containing data** and use **resumable transfers** to upload the data into **Cloud Storage**.
- D. Install **gsutil** on each **server containing data** and use **streaming transfers** to upload the data into **Cloud Storage**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Transfer the data onto a **Transfer Appliance**, then use a **Transfer Appliance Rehydrator** to decrypt and upload the data to **Cloud Storage**.

**Correct Answer:**

✅ **A. Transfer the data onto a Transfer Appliance, then use a Transfer Appliance Rehydrator to decrypt and upload the data to Cloud Storage.**

**Explanation:**

Since **75 TB of data is being migrated**, using **Google Transfer Appliance** is the best approach for **large-scale, offline data transfers** following **Google-recommended best practices**.

**Why Transfer Appliance?**

✅ **Designed for large data transfers (10 TB - 1 PB+).**

- **Uploading 75 TB over the internet** using `gsutil` would be **slow and unreliable** due to bandwidth constraints.
- **Transfer Appliance enables secure, offline data transfer**—no dependency on network speed.

✅ **How It Works:**

1. **Order a Transfer Appliance** from Google Cloud.
2. **Copy the 75 TB of data to the appliance** at your on-premises location.
3. **Ship the appliance back to Google.**
4. **Google uploads the data to Cloud Storage** using **Transfer Appliance Rehydrator**.

✅ **Supporting Documentation:**

- **Google Transfer Appliance Overview:**
  **https://cloud.google.com/transfer-appliance/docs/**

**Why Other Options Are Incorrect?**

**B. Transfer the data onto a Transfer Appliance, then use Cloud Dataprep to decrypt and upload the data to Cloud Storage.** ❌

- **Cloud Dataprep is a data cleaning and transformation tool, not a transfer tool.**
- **Transfer Appliance Rehydrator** is the correct tool for decrypting and uploading data.

✅ **Reference:**

- **https://cloud.google.com/dataprep/docs**

**C. Install gsutil on each server containing data and use resumable transfers to upload the data into Cloud Storage.** ❌

- **gsutil is good for small-to-medium transfers** but **not recommended for 75 TB due to network limitations**.
- **Even with resumable uploads, transferring this much data over the internet would be slow and error-prone.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/gsutil**

**D. Install gsutil on each server containing data and use streaming transfers to upload the data into Cloud Storage.** ❌

- **Streaming transfers are not recommended for massive datasets like 75 TB**—they require continuous connectivity.
- **The transfer could fail due to network issues, and there is no checkpoint restart for streamed data.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/gsutil**

**Conclusion:**

The best approach is **A. Transfer the data onto a Transfer Appliance, then use a Transfer Appliance Rehydrator to decrypt and upload the data to Cloud Storage**, because:
✔ **Transfer Appliance is built for large-scale data migrations.**
✔ **It avoids network limitations and ensures a secure, offline transfer.**
✔ **Google Cloud officially recommends Transfer Appliance for 10 TB+ data transfers.**

📌 **Final Reference:**
**https://cloud.google.com/transfer-appliance/docs/**

**⚠️ Note:** The "Transfer Appliance Rehydrator" belonged to the first-generation appliance. Today you copy data to the appliance and ship it back, and Google uploads it to your Cloud Storage bucket, encrypted with your Cloud KMS key. The rest of the answer (Transfer Appliance for tens of TB+) still holds.

</details>

---

### Exam 1 · Q53

You have an **application deployed on Google Kubernetes Engine (GKE)** using a **Deployment named** `echo-deployment`. This deployment is exposed through a **Service named** `echo-service`. You need to **update the application** while ensuring **minimal downtime**.

What should you do?

- A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image.
- B. Use the **rolling update functionality** of the **Instance Group** that supports the **Kubernetes cluster**.B. Utilize the rolling update functionality of the Instance Group behind the Kubernetes cluster.
- C. Update the **Deployment YAML file** with the **new container image**, then run **kubectl delete deployment/echo-deployment** followed by **kubectl create -f <yaml-file>**.
- D. Update the **Service YAML file** with the **new container image**, then run **kubectl delete service/echo-service** followed by **kubectl create -f <yaml-file>**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image.

**Correct Answer:**

✅ **A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image.**

**Explanation:**

To **update the application with minimal downtime**, you should use **Kubernetes rolling updates**, which **gradually replace old pods with new ones** while ensuring availability.

✅ **Why Use `kubectl set image`?**

- **Triggers a rolling update**, ensuring minimal downtime.
- **Pods are updated gradually**, avoiding service interruptions.
- **If an issue occurs, Kubernetes allows rollback to the previous version.**
- **No need to delete and recreate resources**, which could cause unnecessary downtime.

**Command to Perform Rolling Update:**

```
kubectl set image deployment/echo-deployment echo-container=<new-image>
```

- `echo-deployment` → The name of the Kubernetes Deployment.
- `echo-container=<new-image>` → Specifies the container to update with the new image.
- **Kubernetes replaces pods gradually**, ensuring seamless traffic flow.

✅ **Supporting Documentation:**

- **Kubernetes Rolling Updates:**
  **https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/**
- `kubectl set image` **Reference:**
  **https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#set-image**

**Why Other Options Are Incorrect?**

**B. Use the rolling update functionality of the Instance Group that supports the Kubernetes cluster.** ❌

- **Incorrect because Kubernetes manages rolling updates at the Deployment level**, not at the Instance Group level.
- **Instance Groups handle VM lifecycle management, not pod-level deployments.**

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/concepts/managed-instance-groups**

**C. Update the Deployment YAML file with the new container image, then run `kubectl delete deployment/echo-deployment` followed by `kubectl create -f <yaml-file>`.** ❌

- **Deleting the Deployment removes all running pods**, causing **downtime**.
- **Best practice is to update the deployment using `kubectl apply` or** `kubectl set image`, which **triggers a rolling update**.

✅ **Reference:**

- **https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment**

**D. Update the Service YAML file with the new container image, then run `kubectl delete service/echo-service` followed by `kubectl create -f <yaml-file>`.** ❌

- **Services do not manage container images**—they manage network access to Pods.
- **Updating a Service does not update the Deployment or Pods.**

✅ **Reference:**

- **https://kubernetes.io/docs/concepts/services-networking/service/**

**Conclusion:**

The best approach is **A. Run `kubectl set image deployment/echo-deployment <new-image>` to update the deployment with the new container image**, because:
✔ **It ensures a rolling update with minimal downtime.**
✔ **Kubernetes gradually replaces old pods with new ones.**
✔ **Allows easy rollback if needed.**

📌 **Final Reference:**
**https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/**

</details>

---

### Exam 1 · Q58

**The development team has provided you with a Kubernetes Deployment file, but you do not have any infrastructure set up yet. You need to deploy the application from this file.**

**What should you do?**

- A. Use `gcloud` to create a **Kubernetes cluster**, then use **Deployment Manager** to create the deployment.
- B. Use `gcloud` to create a **Kubernetes cluster**, then use `kubectl` to create the deployment.
- C. Use `kubectl` to create a **Kubernetes cluster**, then use **Deployment Manager** to create the deployment.
- D. Use `kubectl` to create a **Kubernetes cluster**, then use `kubectl` to create the deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use `gcloud` to create a **Kubernetes cluster**, then use `kubectl` to create the deployment.

**Correct Answer:**

✅ **B. Use `gcloud` to create a Kubernetes cluster, then use `kubectl` to create the deployment.**

**Explanation:**

Since you **do not have any infrastructure set up yet**, you first need to **create a Kubernetes cluster** before deploying the application using the provided **Kubernetes Deployment file**.

✅ **Correct Steps to Deploy the Application:**

1. **Create a Google Kubernetes Engine (GKE) cluster** using `gcloud`:
  ```
  gcloud container clusters create my-cluster --zone us-central1-a
  ```
2. **Authenticate `kubectl` with the cluster**:
  ```
  gcloud container clusters get-credentials my-cluster --zone us-central1-a
  ```
3. **Apply the Kubernetes Deployment YAML file** using `kubectl`:
  ```
  kubectl apply -f deployment.yaml
  ```
4. **Verify the deployment**:
  ```
  kubectl get deployments
  ```

✅ **Supporting Documentation:**

- **Creating a GKE Cluster:**
  **https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster**
- **Deploying Applications with kubectl:**
  **https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/**

**Why Other Options Are Incorrect?**

**A. Use `gcloud` to create a Kubernetes cluster, then use Deployment Manager to create the deployment.** ❌

- **Deployment Manager is not the recommended tool for deploying Kubernetes resources**—`kubectl` is the standard tool for interacting with Kubernetes.
- **Deployment Manager is primarily used for infrastructure provisioning (e.g., creating clusters, VMs), not Kubernetes workloads.**

✅ **Reference:**

- **https://cloud.google.com/deployment-manager/docs**

**C. Use `kubectl` to create a Kubernetes cluster, then use Deployment Manager to create the deployment.** ❌

- `kubectl` **cannot create Kubernetes clusters**—it is used for managing Kubernetes resources within an existing cluster.
- **You must use `gcloud` to create a GKE cluster.**

✅ **Reference:**

- **https://kubernetes.io/docs/reference/kubectl/**

**D. Use `kubectl` to create a Kubernetes cluster, then use `kubectl` to create the deployment.** ❌

- **Incorrect because `kubectl` cannot create clusters**—you must use `gcloud` to create a GKE cluster first.
- **Once the cluster is created, `kubectl` can then be used to create the deployment.**

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster**

**Conclusion:**

The best approach is **B. Use `gcloud` to create a Kubernetes cluster, then use `kubectl` to create the deployment**, because:
✔ **GKE clusters must be created using `gcloud`.**
✔ `kubectl` **is the standard tool for deploying and managing Kubernetes workloads.**
✔ **This follows Google Cloud and Kubernetes best practices.**

📌 **Final Reference:**
**https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster**

**⚠️ Note:** Cloud Deployment Manager reached end of support on March 31, 2026. Google recommends Infrastructure Manager (managed Terraform) instead. It was never the tool for Kubernetes manifests; that is `kubectl`.

</details>

---

### Exam 2 · Q1

**You are developing an App Engine application that uses Cloud Datastore as its persistence layer. You need to retrieve multiple root entities using their identifiers while minimizing the operational overhead in Cloud Datastore.**

**What should you do?**

- A. Create a **Key object** for each entity and perform a **batch get operation**.
- B. Create a **Key object** for each entity and run **multiple get operations**, one per entity.
- C. Use the **identifiers** to create a **query filter** and execute a **batch query operation**.
- D. Use the **identifiers** to create a **query filter** and run **multiple query operations**, one per entity.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a **Key object** for each entity and perform a **batch get operation**.

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

</details>

---

### Exam 2 · Q4

**You have a Python web application with many dependencies that requires 0.1 CPU cores and 128 MB of memory to run in production. You want to monitor and maximize machine utilization while also ensuring reliable deployment of new versions of the application.**

**Which approach should you take?**

- A. **Managed Instance Group approach** Create a **managed instance group** using **f1-micro** machines. Use a **startup script** to clone the repository, check out the production branch, install dependencies, and start the Python app. Restart the instances to deploy new production releases.
- B. **Compute Engine Image approach** Create a **managed instance group** using **n1-standard-1** machines. Build a **Compute Engine image** from the production branch with all dependencies and auto-start the Python app. Rebuild the Compute Engine image and update the **instance template** to deploy new releases.
- C. **Google Kubernetes Engine (GKE) with versioning approach** Create a **Google Kubernetes Engine (GKE) cluster** using **n1-standard-1** machines. Build a **Docker image** from the **production branch**, including all dependencies, and tag it with a **version number**. Create a **Kubernetes Deployment** with `imagePullPolicy: IfNotPresent` in the **staging namespace**, and then promote it to **production** after testing.
- D. **GKE with always pulling latest image approach** Create a **GKE cluster** using **n1-standard-4** machines. Build a **Docker image** from the **master branch**, including all dependencies, and tag it as `'latest'`. Create a **Kubernetes Deployment** in the **default namespace** with `imagePullPolicy: Always`, and restart the pods to deploy new production releases.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Google Kubernetes Engine (GKE) with versioning approach** Create a **Google Kubernetes Engine (GKE) cluster** using **n1-standard-1** machines. Build a **Docker image** from the **production branch**, including all dependencies, and tag it with a **version number**. Create a **Kubernetes Deployment** with `imagePullPolicy: IfNotPresent` in the **staging namespace**, and then promote it to **production** after testing.

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

</details>

---

### Exam 2 · Q27

**You need to update an App Engine application while testing the new version with production traffic before fully replacing the current version.**

**What should you do?**

- A. Deploy the update using the **Instance Group Updater** to create a **partial rollout**, allowing for **canary testing**.
- B. Deploy the update as a **new version** in the **App Engine application**, and **split traffic** between the new and current versions.
- C. Deploy the update in a **new VPC** and use **Google's global HTTP load balancer** to split traffic between the updated and current applications.
- D. Deploy the update as a **new App Engine application** and use **Google's global HTTP load balancer** to split traffic between the new and current applications.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy the update as a **new version** in the **App Engine application**, and **split traffic** between the new and current versions.

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

</details>

---

### Exam 2 · Q31

**Your application makes HTTP requests to Cloud Storage, but occasionally, these requests fail with HTTP status codes 5xx and 429.**

**How should you handle these errors?**

- A. Use **gRPC** instead of **HTTP** to improve performance.
- B. Implement **retry logic** using a **truncated exponential backoff strategy**.
- C. Ensure the **Cloud Storage bucket is multi-regional** for geo-redundancy.
- D. Monitor **Google Cloud Status** and only make requests when **Cloud Storage is not reporting an incident**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Implement **retry logic** using a **truncated exponential backoff strategy**.

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

</details>

---

### Exam 2 · Q42

You are managing an **application deployed on Cloud Run for Anthos**. You need to define a **deployment strategy** that allows you to **evaluate a new version of the application** by **sending a subset of production traffic** before proceeding with a full rollout.

What should you do?

- A. **Deploy a new revision** of the application to **Cloud Run** with the updated version and **configure traffic splitting** between the current and new revisions.
- B. **Deploy a new service** to **Cloud Run** with the updated version and use **Cloud Load Balancing** to distribute traffic between both services.
- C. In the **Google Cloud Console**, enable **continuous deployment** using **Cloud Build** for the development branch. As part of the **Cloud Build trigger**, configure the **TRAFFIC_PERCENTAGE** substitution variable to control the amount of traffic sent to the new version.
- D. In the **Google Cloud Console**, configure **Traffic Director** with a **new Service** that points to the updated application version on **Cloud Run**. Use **Traffic Director** to send a **small percentage of traffic** to the new version.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Deploy a new revision** of the application to **Cloud Run** with the updated version and **configure traffic splitting** between the current and new revisions.

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

</details>

---

### Exam 2 · Q50

You have developed a **non-critical update** for your **application running in a managed instance group (MIG)** and have created a **new instance template** containing the update.

To **avoid any disruption**, you **do not** want to update **existing instances**. However, you want **any newly created instances** in the **managed instance group** to use the **new instance template**.

What should you do?

- A. **Start a rolling restart operation** to apply the new template to instances.
- B. **Start a rolling replace operation** to replace instances one at a time with the new template.
- C. **Start a rolling update** and select the **Proactive update mode** to immediately update instances.
- D. **Start a rolling update** and select the **Opportunistic update mode** to apply the new template only to newly created instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Start a rolling update** and select the **Opportunistic update mode** to apply the new template only to newly created instances.

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

</details>

---

### Exam 3 · Q11

Your company offers a **recommendation engine** to retail clients via an **API**. Retail clients submit a **user ID** to the API and receive **personalized recommendations** in return. You are responsible for managing the **API lifecycle**, and you want to ensure that customers are not impacted by **backward-incompatible changes**. You aim to follow **Google-recommended best practices** for API stability and evolution.

What should you do?

- A. Maintain a **mailing list of all clients** and notify them at least **one month in advance** before replacing the old API with a new version that includes breaking changes.
- B. Implement an **automated CI/CD pipeline** that regenerates and publishes **API documentation** each time an update is deployed.
- C. Apply an **API versioning strategy** that **increments the version number** with every **backward-incompatible change**.
- D. Use an API versioning approach where you **append “DEPRECATED”** to the current version number when introducing a breaking change, while keeping the **same version number** for the new API.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Apply an **API versioning strategy** that **increments the version number** with every **backward-incompatible change**.

✅ **Correct Answer: C. Apply an API versioning strategy that increments the version number with every backward-incompatible change.**

**Scenario Summary:**

- You offer a **recommendation API** used by retail clients.
- Clients send a user ID and receive recommendations.
- You are responsible for **API lifecycle management**.
- You must **avoid breaking existing client integrations** during API updates.
- You aim to follow **Google Cloud–recommended API best practices** for **stability and evolution**.

✅ **Why Option C is Correct:**

**Use Explicit API Versioning for Breaking Changes**

- **Backward-incompatible changes** (such as removing fields, changing request/response structure, etc.) **must not impact current consumers**.
- The best practice is to:
  - **Increment the version number** (e.g., `/v1/`, `/v2/`) when introducing **breaking changes**.
  - **Keep the old version available** so existing clients are not disrupted.
  - Give clients time to **migrate** at their own pace.

**Google Recommendation:**

“Use versioning to help manage changes in your API, and **increment the version number** in the URI path or header for **breaking changes**.”
— Source: Google Cloud API Design Guide – Versioning

❌ **Why Other Options Are Incorrect:**

**A. Maintain a mailing list and notify clients about breaking changes in advance**

- **Communication is important**, but **not sufficient**.
- Clients should **not be forced to upgrade immediately** just because of an announcement.
- Breaks the principle of **API stability** if existing clients are impacted.

**B. Implement automated CI/CD to regenerate and publish API documentation**

- **Useful practice**, but this only improves **documentation quality**, not **API stability**.
- Does not prevent breaking changes from affecting clients.

**D. Append “DEPRECATED” to the version number while keeping the same version for the new API**

- This is **confusing** and **violates semantic versioning best practices**.
- You should not **reuse version identifiers** for updated/breaking versions.
- Proper versioning requires each major breaking change to have a **distinct version identifier**.

✅ **Final Recommendation:**

Use **explicit versioning** (e.g., `/v1/`, `/v2/`) to **safely evolve APIs** and **avoid disruptions** to existing clients.

This is the **standard best practice** followed by Google and other cloud providers.

</details>

---

### Exam 3 · Q20

Your organization is planning to **migrate a 10 TB database export** from its **on-premises environment to Cloud Storage**. You need to **minimize transfer time**, **reduce overall cost**, and **limit the load on the source database** during the migration. The available **bandwidth between the on-prem environment and Google Cloud is 1 Gbps**. You aim to follow **Google-recommended best practices** for this type of data transfer.

What is the most appropriate solution?

- A. Build a **Dataflow pipeline** that reads data directly from the source database and writes it to **Cloud Storage**.
- B. Use the **Transfer Appliance** to perform an **offline migration** of the data to Cloud Storage.
- C. Use a **third-party ETL tool** to extract data from the on-prem database and upload it to Cloud Storage.
- D. **Compress the export files** and use `gsutil -m` to upload the data to Cloud Storage using **multi-threaded transfers**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Compress the export files** and use `gsutil -m` to upload the data to Cloud Storage using **multi-threaded transfers**.

**Correct answer: D. Compress the export files and use `gsutil -m` to upload the data to Cloud Storage using multi-threaded transfers.**

For a **10 TB database export** with **1 Gbps bandwidth**, Google-recommended practice is to use an **online transfer** when the available bandwidth is sufficient to meet the migration timeline. At 1 Gbps, 10 TB is large but still practical to transfer online. Google’s migration guidance says that with reasonable network connectivity, even **100 TB at 1 Gbps** can be transferred online in a little over 10 days, and Transfer Appliance is mainly recommended when bandwidth is not enough or cannot be acquired in time.

Option D is best because:

- The data is already a **database export**, so the source database does not need to be continuously queried during transfer.
- Compression reduces the amount of data sent over the network.
- `gsutil -m` enables parallel/multi-threaded transfer behavior, reducing overall upload time.
- It avoids the cost and logistics of ordering, receiving, loading, shipping, and ingesting a Transfer Appliance.

Google’s current documentation mentions `gcloud storage` as the preferred command-line tool for small-to-medium on-premises transfers, but older PCA-style questions often use `gsutil -m` for the same concept: parallelized command-line upload to Cloud Storage. Google Cloud documentation also states that command-line Cloud Storage copy operations can perform parallel multi-threaded/multi-processing copies where appropriate.

**Why the other options are not the best choice**

A. **Incorrect.** Dataflow is not appropriate here because the data is already exported. Reading directly from the source database would increase database load, which violates the requirement to limit source database impact.

B. **Incorrect.** Transfer Appliance is useful for very large offline transfers or when network bandwidth is insufficient. Here, 10 TB over 1 Gbps is feasible online, and Transfer Appliance adds hardware, shipping, and operational overhead. Google’s guidance positions Transfer Appliance for cases where bandwidth is limited or not enough to meet the deadline.

C. **Incorrect.** A third-party ETL tool would add cost and complexity. It may also read directly from the database, increasing database load. There is no transformation requirement here, only movement of an existing export.

**Need-to-know foundational concept**

For PCA exam scenarios, choose **Transfer Appliance** when the data volume is very large and network transfer is impractical. For a manageable export such as **10 TB with 1 Gbps bandwidth**, use compressed files and a parallel command-line transfer to Cloud Storage.

###### Explanation

**Correct answer: D. Compress the export files and use `gsutil -m` to upload the data to Cloud Storage using multi-threaded transfers.**

For a **10 TB database export** with **1 Gbps bandwidth**, Google-recommended practice is to use an **online transfer** when the available bandwidth is sufficient to meet the migration timeline. At 1 Gbps, 10 TB is large but still practical to transfer online. Google’s migration guidance says that with reasonable network connectivity, even **100 TB at 1 Gbps** can be transferred online in a little over 10 days, and Transfer Appliance is mainly recommended when bandwidth is not enough or cannot be acquired in time.

Option D is best because:

- The data is already a **database export**, so the source database does not need to be continuously queried during transfer.
- Compression reduces the amount of data sent over the network.
- `gsutil -m` enables parallel/multi-threaded transfer behavior, reducing overall upload time.
- It avoids the cost and logistics of ordering, receiving, loading, shipping, and ingesting a Transfer Appliance.

Google’s current documentation mentions `gcloud storage` as the preferred command-line tool for small-to-medium on-premises transfers, but older PCA-style questions often use `gsutil -m` for the same concept: parallelized command-line upload to Cloud Storage. Google Cloud documentation also states that command-line Cloud Storage copy operations can perform parallel multi-threaded/multi-processing copies where appropriate.

> [!note]- Why the other options are wrong
> A. **Incorrect.** Dataflow is not appropriate here because the data is already exported. Reading directly from the source database would increase database load, which violates the requirement to limit source database impact.
>
> B. **Incorrect.** Transfer Appliance is useful for very large offline transfers or when network bandwidth is insufficient. Here, 10 TB over 1 Gbps is feasible online, and Transfer Appliance adds hardware, shipping, and operational overhead. Google’s guidance positions Transfer Appliance for cases where bandwidth is limited or not enough to meet the deadline.
>
> C. **Incorrect.** A third-party ETL tool would add cost and complexity. It may also read directly from the database, increasing database load. There is no transformation requirement here, only movement of an existing export.

</details>

---

### Exam 3 · Q26

At CloudOps Solutions, your team is preparing to upload a collection of critical files to **Google Cloud Storage**. After the upload completes, they want to ensure that the data in the cloud is **exactly the same** as the original files stored **on-premises**. The solution should **minimize both cost and effort** during the validation process.

**What should you do to achieve this?**

- A. Use the shasum command on Linux to generate checksums for the local files. Upload the files to Cloud Storage using gsutil -m. Download the uploaded files using gsutil cp. Run shasum again on the downloaded files. Compare the two sets of hashes.
- B. Upload the files to Cloud Storage using gsutil -m. Write a custom Java program to generate **CRC32C** hashes for the local files. Use gsutil ls -L gs://[YOUR_BUCKET_NAME] to retrieve the CRC32C hashes of the uploaded files. Compare the hashes.
- C. Upload all files using gsutil -m. Download the uploaded files using gsutil cp. Use the diff command on Linux to compare the content of the downloaded files with the originals.
- D. Upload the files using gsutil -m. Use gsutil hash -c FILE_NAME to generate **CRC32C** hashes for the local files. Use gsutil ls -L gs://[YOUR_BUCKET_NAME] to retrieve the **CRC32C** hashes of the uploaded files. Compare the hashes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Upload the files using gsutil -m. Use gsutil hash -c FILE_NAME to generate **CRC32C** hashes for the local files. Use gsutil ls -L gs://[YOUR_BUCKET_NAME] to retrieve the **CRC32C** hashes of the uploaded files. Compare the hashes.

The correct answer is:
**D.**

1. Upload the files using `gsutil -m`.
2. Use `gsutil hash -c FILE_NAME` to generate **CRC32C hashes** for the local files.
3. Use `gsutil ls -L gs://[YOUR_BUCKET_NAME]` to retrieve the **CRC32C hashes** of the uploaded files.
4. Compare the hashes.

**Justification for Correct Option (D):**

- **Google Cloud Storage** automatically calculates a **CRC32C checksum** for every uploaded object.
- You can use `gsutil hash -c` on your **original local files** to generate CRC32C hashes in the same format used by GCS.
- Use `gsutil ls -L` to fetch metadata of the uploaded objects, which includes the **CRC32C value**.
- By comparing both CRC32C values, you can **verify data integrity** efficiently **without re-downloading the files**, which is both **cost-effective and fast**.

This is a **Google-recommended method** for validating uploaded files.

**Official Documentation:**

- gsutil hash command
- gsutil ls -L for metadata including CRC32C
- Using CRC32C for integrity checking

**Why the Other Options Are Incorrect:**

**A.**

Uses `shasum` to generate hashes before and after upload.

- While SHA-1 provides a way to verify integrity, **Google Cloud Storage does not store SHA-1 hashes**.
- So, to verify integrity, this option **requires downloading the files again**, which **adds cost and effort** — violating the requirement to **minimize cost and effort**.

B.

Use a custom Java program to generate CRC32C, and compare with GCS.

- While CRC32C is the correct hash, writing a **custom Java program** adds **unnecessary complexity and effort**.
- This approach is **less efficient** than using the built-in `gsutil hash -c`.

C.

Upload, then re-download the files and use `diff`.

- This involves **downloading all files again**, which increases **network and egress costs**, especially for large datasets.
- It also adds significant **manual effort** and **processing time**.

Final Answer: **D**

Because it uses **built-in GCS tools**, leverages **matching checksum algorithms (CRC32C)**, and avoids **extra data transfers**, aligning with the goals of **minimal cost and effort** while ensuring **high confidence in data integrity**.

**Ref** - [https://cloud.google.com/storage/docs/gsutil/commands/hash](https://cloud.google.com/storage/docs/gsutil/commands/hash)

</details>

---

### Exam 3 · Q61

The **CloudOps team at SkyNet Solutions** currently stores **10 TB of data** in an **object storage service provided by a third party**. They want to **migrate this data to a Google Cloud Storage bucket** as quickly and **cost-effectively** as possible, while adhering to **Google-recommended best practices**.

What is the best approach to meet these requirements?

- A. Use the `gsutil mv` command to transfer the data to Cloud Storage.
- B. Use **Storage Transfer Service** to migrate the data directly to a Cloud Storage bucket.
- C. Transfer the data to a **Transfer Appliance**, then ship it to Google for ingestion.
- D. **Download the data** to an **on-premises data center**, then upload it to Cloud Storage manually.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **Storage Transfer Service** to migrate the data directly to a Cloud Storage bucket.

✅ Correct Answer:

**B. Use Storage Transfer Service to migrate the data directly to a Cloud Storage bucket.**

✅ Why Option B is Correct:

- **Storage Transfer Service (STS)** is **Google Cloud’s fully managed service** for transferring data from:
  - **AWS S3**
  - **Azure Blob Storage**
  - **Other HTTP/HTTPS-based storage services**
- Ideal for **large-scale transfers** (10 TB+) and designed to be:
  - **Fast** with parallelism
  - **Reliable** with retry mechanisms
  - **Cost-effective** since no intermediate storage or manual downloads are needed
- Supports **scheduling**, **filters**, and **data synchronization**, and follows **Google Cloud best practices**.

**Official Documentation:**

- Storage Transfer Service Overview
- Supported sources for Storage Transfer Service

❌ Why Other Options Are Incorrect:

**A. Use the `gsutil mv` command**

- `gsutil mv` is intended for **moving** files **between buckets** or **from local storage** to GCS.
- It **does not support third-party cloud object storage** directly.
- It requires **data to be local first**, which adds **latency and bandwidth cost**.
- Not scalable for **10 TB**, and not Google-recommended for third-party transfers.

**Reference:**
[https://cloud.google.com/storage/docs/gsutil/commands/mv](https://cloud.google.com/storage/docs/gsutil/commands/mv)

**C. Use Transfer Appliance**

- **Transfer Appliance** is designed for **extremely large datasets (100+ TB)** that cannot be moved over the network efficiently.
- For 10 TB, **network-based migration (STS)** is faster and more cost-effective.
- Using the appliance adds unnecessary **logistics, shipping time, and complexity**.

**D. Download to on-prem and upload manually**

- Highly **inefficient** and **time-consuming** for 10 TB of data.
- Introduces unnecessary **network egress costs** and **administrative overhead**.
- Not scalable or aligned with **cloud-native migration best practices**.

✅ Final Answer:

**B. Use Storage Transfer Service to migrate the data directly to a Cloud Storage bucket.**

</details>

---

### Exam 3 · Q63

You are managing **multiple Google Cloud projects** at **CloudFleet Corp.** and need to work regularly with **BigQuery**, **Cloud Bigtable**, and **Google Kubernetes Engine (GKE)** using the **gcloud CLI**. Since you frequently **travel and switch between different workstations**, you want to avoid the overhead of manually managing the gcloud installation on each machine.

What is the **best way** to interact with Google Cloud services without managing gcloud manually on every device?

- A. Use **Google Cloud Shell** from the Google Cloud Console to access gcloud from any browser, without installing anything locally.
- B. Set up a **Compute Engine VM**, install gcloud there, and SSH into the instance from any device to run gcloud commands.
- C. Install gcloud on all workstations and run `gcloud components auto-update` on each machine to keep it up to date.
- D. Use a **package manager** (like apt, yum, or brew) to install gcloud on each workstation instead of installing it manually.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use **Google Cloud Shell** from the Google Cloud Console to access gcloud from any browser, without installing anything locally.

✅ **Correct Answer:**

**A. Use Google Cloud Shell from the Google Cloud Console to access gcloud from any browser, without installing anything locally.**

✅ **Why Option A is Correct:**

- **Google Cloud Shell** is a **browser-based shell environment** with the `gcloud` CLI and other tools (e.g., `kubectl`, `bq`, `git`) **pre-installed and always up-to-date**.
- You can access it **from any device with a browser**, which is ideal for a **mobile/remote work setup**.
- It **requires no local setup or maintenance**, removing overhead entirely.
- It offers:
  - **5 GB persistent disk**
  - Integrated editor
  - Secure access to Google Cloud resources

**Official Documentation:**

- Google Cloud Shell Overview

❌ Why Other Options Are Incorrect:

**B. Set up a Compute Engine VM with gcloud installed**

- Adds **unnecessary cost and complexity**:
  - VM charges (compute, network, storage)
  - Requires secure access setup and maintenance
- Still requires **manual gcloud installation and updates** on the VM

**C. Install gcloud and use auto-update on each machine**

- Defeats the purpose of the question (avoiding manual management).
- Requires **installing and updating** `gcloud` across **all workstations**, which is **tedious and error-prone**.

**D. Use package managers (apt, yum, brew) to install gcloud**

- While easier than manual installation, it still requires:
  - **Installation on every device**
  - Periodic updates to keep versions consistent
- **Does not eliminate setup and maintenance overhead**

✅ **Final Answer:**

**A. Use Google Cloud Shell from the Google Cloud Console to access gcloud from any browser, without installing anything locally.**

</details>

---

### Exam 4 · Q6

**Your company's application, hosted on App Engine, facilitates user uploads of music files directly into Cloud Storage from their browser session, bypassing the backend. What steps should you take to accomplish this?**

- A. Configure CORS in the target Cloud Storage bucket, allowing the base URL of the App Engine application as an allowed origin. Utilize the Cloud Storage Signed URL feature to generate a POST URL for uploads.
- B. Configure CORS in the target Cloud Storage bucket, permitting the base URL of the App Engine application as an allowed origin. Grant users who upload files the Cloud Storage WRITER role.
- C. Utilize the Cloud Storage Signed URL feature to generate a POST URL for uploads. Employ App Engine default credentials to sign requests for Cloud Storage operations.
- D. Grant users who upload files the Cloud Storage WRITER role. Utilize App Engine default credentials to sign requests for Cloud Storage operations.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure CORS in the target Cloud Storage bucket, allowing the base URL of the App Engine application as an allowed origin. Utilize the Cloud Storage Signed URL feature to generate a POST URL for uploads.

**Correct Answer: A.**

**Configure CORS on the target Cloud Storage bucket, allowing the base URL of the App Engine app as an allowed origin. Use Signed URLs to generate a POST URL for direct browser upload.**

✅ **Justification for Correct Option (A):**

To **allow direct browser uploads** to a Google Cloud Storage bucket **without routing through App Engine**, the most secure and scalable pattern involves:

1. **CORS (Cross-Origin Resource Sharing)**:
  - Required because the browser makes a cross-origin request from your App Engine frontend to Cloud Storage.
  - CORS must be configured on the bucket to **allow the origin (App Engine URL)** and specify methods (`POST`, `PUT`, etc.).
2. **Signed URLs**:
  - App Engine backend generates a **Signed URL** with upload permissions (usually `POST` method).
  - The browser uses this **pre-signed URL** to upload the file directly to the bucket.
  - This avoids giving users direct IAM roles and allows **fine-grained, time-limited access**.

This approach meets all key requirements:

- **Security**: Users only get temporary access.
- **Performance**: Uploads bypass App Engine, reducing latency and load.
- **Scalability**: No need to manage IAM roles per user.

**Official Documentation References:**

- Signed URLs for uploads:
  [https://cloud.google.com/storage/docs/access-control/signed-urls#example](https://cloud.google.com/storage/docs/access-control/signed-urls#example)
- CORS configuration for browser uploads:
  [https://cloud.google.com/storage/docs/configuring-cors](https://cloud.google.com/storage/docs/configuring-cors)

❌ **Why Other Options Are Incorrect:**

**B. Configure CORS and grant Storage Object Creator (WRITER) role to each user.**

- **Incorrect**, because:
  - Granting **IAM roles to individual users** introduces **complexity and security risk**.
  - It **doesn't scale well** and **violates least privilege**.
  - Signed URLs are a better fit for **temporary, scoped access**.

**C. Use Signed URL and App Engine default credentials to sign URL requests (but no CORS setup).**

- **Incorrect**, because:
  - You **must configure CORS** on the bucket for **browser-based uploads** to avoid CORS errors.
  - Without CORS, the browser cannot successfully send cross-origin requests.

**D. Grant Storage WRITER role to each user and use App Engine credentials to sign requests.**

- **Incorrect**, due to:
  - **Over-permissioning** by assigning WRITER IAM roles to users.
  - Security and manageability concerns.
  - Signed URLs are **preferred over broad IAM roles** for user uploads.

✅ **Final Answer: A.**

**Configure CORS** on the Cloud Storage bucket and **use Signed URLs** for secure, direct uploads from the browser. This pattern is both **secure** and **scalable**, and recommended by Google Cloud.

</details>

---

### Exam 4 · Q10

**InfoPulse Corp** is planning to migrate a **10 TB on-premises database export** to **Google Cloud Storage**. The objective is to **minimize both the total transfer time and the overall cost**. The available bandwidth between their on-premises data center and Google Cloud is **1 Gbps**.

You are tasked with selecting a migration approach that aligns with **Google-recommended best practices**.

**What should you do?**

- A. Create a **Cloud Dataflow** pipeline that directly reads data from the on-premises database and writes it to Cloud Storage.
- B. Use the **Transfer Appliance** to move the data via an **offline** transfer method.
- C. Use a third-party **commercial ETL partner** solution to extract and load the data into Cloud Storage.
- D. Transfer the data using the command: `gcloud storage cp [SOURCE] [DESTINATION]`

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Transfer the data using the command: `gcloud storage cp [SOURCE] [DESTINATION]`

Correct Answer: **D**

**Upload the data with `gcloud storage cp`.**

Why D is correct

For a **10-TB** one-time export with **1 Gbps** available bandwidth, an **online transfer to Cloud Storage** is typically the fastest end-to-end option (no appliance shipping/handling delay) and also cost-efficient because you avoid standing up extra compute/services just to move bytes.

Using `gcloud storage cp` (which uses the Cloud Storage client libraries under the hood) is a Google-supported, straightforward approach for uploading objects to Cloud Storage and is commonly used for bulk uploads when you already have the export files available.

**Official documentation:**
[https://cloud.google.com/sdk/gcloud/reference/storage/cp](https://cloud.google.com/sdk/gcloud/reference/storage/cp)

Why the other options are not best fit

A. Dataflow job to read from DB and write to Cloud Storage

Adds unnecessary complexity and cost. You already have a database export; you don’t need a managed data processing pipeline just to upload files.

B. Data Transfer Appliance (offline migration)

Offline transfer is best when network bandwidth is limited or datasets are very large. With **1 Gbps** and only **10 TB**, the appliance usually increases total elapsed time due to shipping and handling.

C. Commercial partner ETL solution

Higher cost and operational overhead than needed for a straightforward export upload.

**Need-to-know fundamentals**

- At **1 Gbps**, an online transfer of **10 TB** can complete in roughly **a day or so** under ideal conditions, making it practical without offline appliances.
- For bulk uploads, prefer simple, supported tools over introducing processing services unless transformation is required.

**Official documentation (same as above):**
[https://cloud.google.com/sdk/gcloud/reference/storage/cp](https://cloud.google.com/sdk/gcloud/reference/storage/cp)

###### Explanation

Why D is correct

For a **10-TB** one-time export with **1 Gbps** available bandwidth, an **online transfer to Cloud Storage** is typically the fastest end-to-end option (no appliance shipping/handling delay) and also cost-efficient because you avoid standing up extra compute/services just to move bytes.

Using `gcloud storage cp` (which uses the Cloud Storage client libraries under the hood) is a Google-supported, straightforward approach for uploading objects to Cloud Storage and is commonly used for bulk uploads when you already have the export files available.

**Official documentation:**
[https://cloud.google.com/sdk/gcloud/reference/storage/cp](https://cloud.google.com/sdk/gcloud/reference/storage/cp)

> [!note]- Why the other options are wrong
> A. Dataflow job to read from DB and write to Cloud Storage
>
> Adds unnecessary complexity and cost. You already have a database export; you don’t need a managed data processing pipeline just to upload files.
>
> B. Data Transfer Appliance (offline migration)
>
> Offline transfer is best when network bandwidth is limited or datasets are very large. With **1 Gbps** and only **10 TB**, the appliance usually increases total elapsed time due to shipping and handling.
>
> C. Commercial partner ETL solution
>
> Higher cost and operational overhead than needed for a straightforward export upload.

</details>

---

### Exam 4 · Q21

**Introductory Info**

**Company overview -**

EHR Healthcare is a leading provider of electronic health record software to the medical industry. EHR Healthcare provides their software as a service to multi- national medical offices, hospitals, and insurance providers.

**Solution concept -**

Due to rapid changes in the healthcare and insurance industry, EHR Healthcare's business has been growing exponentially year over year. They need to be able to scale their environment, adapt their disaster recovery plan, and roll out new continuous deployment capabilities to update their software at a fast pace. Google

Cloud has been chosen to replace their current colocation facilities.

**Existing technical environment -**

EHR's software is currently hosted in multiple colocation facilities. The lease on one of the data centers is about to expire.

Customer-facing applications are web-based, and many have recently been containerized to run on a group of Kubernetes clusters. Data is stored in a mixture of relational and NoSQL databases (MySQL, MS SQL Server, Redis, and MongoDB).

EHR is hosting several legacy file- and API-based integrations with insurance providers on-premises. These systems are scheduled to be replaced over the next several years. There is no plan to upgrade or move these systems at the current time.

Users are managed via Microsoft Active Directory. Monitoring is currently being done via various open source tools. Alerts are sent via email and are often ignored.

**Business requirements -**

- On-board new insurance providers as quickly as possible.
- Provide a minimum 99.9% availability for all customer-facing systems.
- Provide centralized visibility and proactive action on system performance and usage.
- Increase ability to provide insights into healthcare trends.
- Reduce latency to all customers.
- Maintain regulatory compliance.
- Decrease infrastructure administration costs.
- Make predictions and generate reports on industry trends based on provider data.

**Technical requirements -**

- Maintain legacy interfaces to insurance providers with connectivity to both on-premises systems and cloud providers.
- Provide a consistent way to manage customer-facing applications that are container-based.
- Provide a secure and high-performance connection between on-premises systems and Google Cloud.
- Provide consistent logging, log retention, monitoring, and alerting capabilities.
- Maintain and manage multiple container-based environments.
- Dynamically scale and provision new environments.
- Create interfaces to ingest and process data from new providers.

**Executive statement -**

Our on-premises strategy has worked for years but has required a major investment of time and money in training our team on distinctly different systems, managing similar but separate environments, and responding to outages. Many of these outages have been a result of misconfigured systems, inadequate capacity to manage spikes in traffic, and inconsistent monitoring practices. We want to use Google Cloud to leverage a scalable, resilient platform that can span multiple environments seamlessly and provide a consistent and stable user experience that positions us for future growth.

**Question**

**As a developer on the EHR customer portal team, you've migrated the customer portal application to Google Cloud. Due to increased load, the application is logging many timeout errors. Although you've incorporated Pub/Sub into the architecture, the application isn't logging any Pub/Sub publishing errors. To enhance publishing latency, what action should you take?**

- A. Adjust the Pub/Sub Total Timeout retry value.
- B. Transition from a Pub/Sub subscriber pull model to a push model.
- C. Disable Pub/Sub message batching.
- D. Establish a backup Pub/Sub message queue.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Disable Pub/Sub message batching.

Here's the breakdown of why the best option is most likely C, with considerations for other situations:

**C. Disable Pub/Sub message batching.**

- **How it helps:** Pub/Sub's batching feature groups messages together to improve network efficiency. However, this introduces additional latency since messages must be accumulated before being sent. Disabling batching sends messages individually, often reducing end-to-end latency.
- **Why it's likely best:** If the problem is primarily timeout errors and there are no Pub/Sub publishing errors logged, it suggests messages might be getting 'stuck' due to batching delays rather than failing outright.

**When Other Options Might Be Better:**

- **A. Adjust the Pub/Sub Total Timeout retry value.** This is helpful if messages are legitimately failing to publish due to transient network issues or other errors. Increasing the timeout gives messages more time to successfully publish. Consider this if you are seeing publishing errors in addition to timeouts.
- **B. Transition from a Pub/Sub subscriber pull model to a push model.** Useful if the issue is subscriber-side delays in processing messages. Push subscriptions deliver messages to an HTTP endpoint, which can improve responsiveness. However, this requires rearchitecting the subscriber side of your application.
- **D. Establish a backup Pub/Sub message queue.** This is primarily a redundancy/failover solution. It wouldn't directly address latency, but it's a good practice for high-availability systems.

**Important Considerations:**

- **Load vs. Latency:** If the increased load is primarily volume-based (many messages) disabling batching might overload the system. In this case, scaling the publishing infrastructure would be necessary.
- **Error Behavior:** If you start seeing Pub/Sub publishing errors after disabling batching, it means other issues exist besides batching-induced latency.

**Recommendation:**

1. **Trial Run:** Start by disabling batching in a test environment (if possible) to assess the impact on latency and overall system behavior.
2. **Monitoring:** Closely monitor timeout errors, publishing error rates, and system performance after your change.
3. **Iterate:** If latency improves, great! Otherwise, explore options like scaling publishers, adjusting timeouts, or considering push subscriptions based on your findings.

References:

[https://cloud.google.com/pubsub/docs/publisher?hl=en#batchinghttps://cloud.google.com/pubsub/docs/publish-best-practices#configure-batch](https://cloud.google.com/pubsub/docs/publisher?hl=en#batching  https://cloud.google.com/pubsub/docs/publish-best-practices#configure-batch)

</details>

---

### Exam 4 · Q37

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

**Introductory Info**

**Company overview -**

Mountkirk Games makes online, session-based, multiplayer games for mobile platforms. They have recently started expanding to other platforms after successfully migrating their on-premises environments to Google Cloud.

Their most recent endeavor is to create a retro-style first-person shooter (FPS) game that allows hundreds of simultaneous players to join a geo-specific digital arena from multiple platforms and locations. A real-time digital banner will display a global leaderboard of all the top players across every active arena.

**Solution concept -**

Mountkirk Games is building a new multiplayer game that they expect to be very popular. They plan to deploy the game's backend on Google Kubernetes Engine so they can scale rapidly and use Google's global load balancer to route players to the closest regional game arenas. In order to keep the global leader board in sync, they plan to use a multi-region Spanner cluster.

**Existing technical environment -**

The existing environment was recently migrated to Google Cloud, and five games came across using lift-and-shift virtual machine migrations, with a few minor exceptions. Each new game exists in an isolated Google Cloud project nested below a folder that maintains most of the permissions and network policies. Legacy games with low traffic have been consolidated into a single project. There are also separate environments for development and testing.

**Business requirements -**

Support multiple gaming platforms.

Support multiple regions.

Support rapid iteration of game features.

Minimize latency.

Optimize for dynamic scaling.

Use managed services and pooled resources.

Minimize costs.

**Technical requirements -**

Dynamically scale based on game activity.

Publish scoring data on a near real-time global leaderboard.

Store game activity logs in structured files for future analysis.

Use GPU processing to render graphics server-side for multi-platform support.

Support eventual migration of legacy games to this new platform.

**Executive statement -**

Our last game was the first time we used Google Cloud, and it was a tremendous success. We were able to analyze player behavior and game telemetry in ways that we never could before. This success allowed us to bet on a full migration to the cloud and to start building all-new games using cloud-native design principles.

Our new game is our most ambitious to date and will open up doors for us to support more gaming platforms beyond mobile. Latency is our top priority, although cost management is the next most important challenge. As with our first cloud-based game, we have grown to expect the cloud to enable advanced analytics capabilities so we can rapidly iterate on our deployments of bug fixes and new functionality.

**Question**

**For Mountkirk Games' new Google Cloud solution, you need to optimize batch file transfers into Cloud Storage. The batch files contain game statistics and need to be staged in Cloud Storage for processing by an extract transform load (ETL) tool. What approach should you take?**

- A. Utilize gsutil to batch move files in sequence.
- B. Utilize gsutil to batch copy the files in parallel.
- C. Utilize gsutil to extract the files as the initial step of ETL.
- D. Utilize gsutil to load the files as the final step of ETL.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Utilize gsutil to batch copy the files in parallel.

The best approach for optimizing batch file transfers into Cloud Storage is

**B. Utilize gsutil to batch copy the files in parallel.**

Here's why this stands out and how it improves upon the other options:

**Why Parallel Copying with gsutil is Ideal:**

- **Speed:** Parallel copies (using the `gsutil -m` option) significantly increase transfer speeds by leveraging multiple connections simultaneously. This is crucial for optimizing large batch file transfers.
- **Efficiency:** Parallelism maximizes network bandwidth utilization and reduces overall transfer time, especially for large datasets like game statistics.
- **Reliability:** gsutil's built-in error handling and retry mechanisms ensure robust file transfers and minimize the impact of potential transient network issues.

**Why Other Options Are Less Optimal**

- **A. Utilize gsutil to batch move files in sequence.** Moving single files at a time is inherently slower and less efficient than parallelizing the process.
- **C. Utilize gsutil to extract the files as the initial step of ETL.** While `gsutil` can be used for file manipulation, it's not the primary purpose, and other ETL tools likely provide richer feature sets specifically for file extraction and transformation.
- **D. Utilize gsutil to load the files as the final step of ETL.** `gsutil` is great for moving files into Cloud Storage, but after the ETL process is complete, the transformed data might need to be loaded to a different storage service (BigQuery, etc.) depending on Mountkirk's architecture.

**Important Considerations**

- **File Size and Network:** If transferring many small files, the overhead of establishing multiple connections can outweigh benefits. In those cases, sequential transfers might be sufficient.
- **ETL Tool Capabilities:** Closely examine the ETL tool's ability to directly process files from Cloud Storage, potentially streamlining your workflow further.

References:

[https://cloud.google.com/storage/docs/gsutil/commands/cphttps://cloud.google.com/blog/products/gcp/optimizing-your-cloud-storage-performance-google-cloud-performance-atlas](https://cloud.google.com/storage/docs/gsutil/commands/cp  https://cloud.google.com/blog/products/gcp/optimizing-your-cloud-storage-performance-google-cloud-performance-atlas)

</details>

---

### Exam 4 · Q49

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

**In the context of the TerramEarth case study, with approximately 1 petabyte (PB) of vehicle testing data stored in a private data center, and with a 1-Gbps interconnect link available, what is the most suitable approach to move this data to Cloud Storage for the machine learning team's use within a month?**

- A. Request Transfer Appliances from Google Cloud, transfer the data to the appliances, and then return the appliances to Google Cloud for ingestion into Cloud Storage.
- B. Set up the Storage Transfer service provided by Google Cloud to facilitate the transfer of data from your data center to Cloud Storage.
- C. Ensure exclusive access to the 1-Gbps link and employ multi-threaded transfer techniques to upload the data to Cloud Storage.
- D. Export the data to an encrypted USB device, dispatch the device to Google Cloud, and request a data import to Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Request Transfer Appliances from Google Cloud, transfer the data to the appliances, and then return the appliances to Google Cloud for ingestion into Cloud Storage.

Let's break down why the best options are **A** and **B**, and the considerations for choosing between them:

**A. Request Transfer Appliances from Google Cloud, transfer the data to the appliances, and then return the appliances to Google Cloud for ingestion into Cloud Storage.**

**- This would be my choice.**

- **Speed:** Transfer Appliances are designed for large-scale data transfers, potentially completing the process within the month. They bypass limitations of the 1-Gbps internet link.
- **Security:** Appliances offer physical security during transit and encryption of data.
- **Simplicity:** Google handles the logistics and ingestion process, minimizing TerramEarth's operational involvement.

**B. Set up the Storage Transfer Service provided by Google Cloud to facilitate the transfer of data from your data center to Cloud Storage.**

- **Cost-Effectiveness:** If the transfer can be completed within a month over the existing 1-Gbps link, utilizing Storage Transfer Service might be the most cost-effective option.
- **Flexibility:** You get fine-grained control over the transfer process.
- **Managed Service:** Storage Transfer Service handles scheduling, bandwidth optimization, and potential retries.

**Decision Factors:**

- **Time Sensitivity:** If the hard deadline of one month is critical, Transfer Appliances are likely the safest option to guarantee timely completion.
- **Cost:** If the transfer can tolerate a longer duration and budget is a key concern, the Storage Transfer Service might be the better choice.
- **Operational Complexity:** If TerramEarth's team has limited resources or experience handling large-scale data transfers, the simplicity of Transfer Appliances would be a strong advantage.

**Why Other Options Are Less Optimal:**

- **C. Ensure exclusive access to the 1-Gbps link...** While maximizing the available bandwidth can help, a 1-Gbps link is unlikely to transfer 1PB of data within a month.
- **D. Export the data to an encrypted USB device...** This method is not practical at the scale of 1PB, with significant security, shipping, and logistical overheads.

**Calculation Note:** Transferring 1PB over a 1-Gbps link would theoretically take approximately 100 days, exceeding the one-month target.

Hints:

[https://cloud.google.com/transfer-appliance/docs/4.0/overview#transfer-speedshttps://cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#time](https://cloud.google.com/transfer-appliance/docs/4.0/overview#transfer-speeds  https://cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#time)

</details>

---

### Exam 4 · Q51

**A developer in your team deployed his application in Google Container Engine using the Dockerfile provided below. They have noticed that the application deployments are taking longer than desired.**

*FROM ubuntu:16.03*

*COPY . /src*

*RUN apt-get update && apt-get install -y python python-pip*

*RUN pip installl -r requirements.txt*

**Which two actions should you take to optimize this Dockerfile for faster deployment times without adversely affecting the app's functionality? (Choose two.)**

- A. Eliminate Python after pip installation.
- B. Minimize dependencies in requirements.txt.
- C. Opt for a lightweight base image like Alpine Linux.
- D. Upgrade to larger machine types for Google Container Engine node pools.
- E. Rearrange the source code copying step after installing package dependencies (Python and pip).

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Opt for a lightweight base image like Alpine Linux. **|** E. Rearrange the source code copying step after installing package dependencies (Python and pip).

**C. Opt for a lightweight base image like Alpine Linux.**

- This remains the most impactful optimization, offering the biggest reduction in image size and download time during deployments.

**E. Rearrange the source code copying step after installing package dependencies (Python and pip).**

- This leverages Docker's layer caching effectively:
  - **Initial Build:** On the first build, all the layers would need to be created.
  - **Subsequent Builds:** If only your source code (`./`) changes *and* the `requirements.txt` stays the same, the earlier layers with package installation would be reused from the cache. This speeds up builds noticeably.

**Let's revisit the other options:**

- **A. Eliminate Python after pip installation.**
  - As we discussed, this breaks functionality and isn't viable.
- **B. Minimize dependencies in requirements.txt.**
  - While important for image size and overall efficiency, its impact on deployment time is slightly less direct compared to using Alpine and optimizing layer caching.
- **D. Upgrade to larger machine types for Google Container Engine node pools.**
  - This can help with *running* containers but doesn't inherently speed up image building and the initial deployment of those images to nodes.

References:

[https://docs.docker.com/build/cache/](https://docs.docker.com/build/cache/  https://cloud.google.com/architecture/best-practices-for-building-containers)

[https://cloud.google.com/architecture/best-practices-for-building-containers](https://docs.docker.com/build/cache/  https://cloud.google.com/architecture/best-practices-for-building-containers)

**⚠️ Note:** Google Container Engine is the old name of Google Kubernetes Engine (GKE). Also note that `ubuntu:16.03` and `pip installl` are typos in the original question.

</details>

---

### Exam 4 · Q52

**You deploy your custom Java application to Google App Engine, but it fails to deploy and presents the following stack trace. What action should you take?**

java.lang.SecurityException: SHA1 digest error for com/Altostrat/CloakedServlet.class

at com.google.appengine.runtime.Request.process-cf1dd36f818a24b8 (Request.java)

at sun.security.util.ManifestEntryVerifier.verify (ManifestEntryVerifier.java:210)

at java.util.jar.JarVerifier.processEntry (JarVerifier.java:218)

at java.util.jar.JarVerifier.update (JarVerifier.java:205)

at java.util.jar.JarVerifiersVerifierStream.read (JarVerifier.java:428)

at sun.misc.Resource.getBytes (Resource.java:124)

at java.net.URLClassLoader.defineClass (URLClassLoader.java:273)

at sun.reflect.GeneratedMethodAccessor5.invoke (Unknown Source)

at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)

at java.lang.reflect.Method.invoke(Method.java:616)

at java.lang.ClassLoader.loadClass (ClassLoader.java:266)

- A. Ensure all necessary JAR files are uploaded and redeploy your application.
- B. Apply digital signatures to all JAR files and redeploy your application.
- C. Rebuild the CloakedServlet class using MD5 hashing instead of SHA1.
- D. Only Clean and Rebuild Your Project

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Apply digital signatures to all JAR files and redeploy your application.

Here's a breakdown of the error, potential causes, and the best solution:

**Understanding the Error:**

- **java.lang.SecurityException: SHA1 digest error for com/Altostrat/CloakedServlet.class** This error indicates a problem with the integrity verification of a JAR file within your application. During deployment, the App Engine runtime checks the manifest file (META-INF/MANIFEST.MF) and ensures that the integrity of the classes within the JAR is intact. The SHA1 digest in the manifest doesn't match the actual calculated digest of the `CloakedServlet.class`. This mismatch causes the deployment failure.

**Potential Causes:**

- **Corrupted JAR File:** The JAR file containing `CloakedServlet.class` might be corrupt, possibly due to incomplete download or modification.
- **Tampering:** The JAR file might have been modified intentionally or unintentionally after it was originally signed.
- **Incorrect Signing Procedure:** If the JAR was signed, an error during the signing process could lead to this issue.

**Best Solution:**

- **B. Apply digital signatures to all JAR files and redeploy your application.** This is the most likely solution. Here's why:
  - **Security:** Digitally signing your JAR files ensures their integrity and protects against modification. App Engine verifies these signatures.
  - **Best Practice:** It's strongly recommended to sign your JAR files, especially for deployment in production environments.

**Steps to Fix:**

1. **Generate Key Pair:** If you don't have one, generate a keystore with a private and public key using the `keytool` utility.
2. **Sign JAR Files:** Use the `jarsigner` tool to sign all JAR files in your application, including the one containing `CloakedServlet.class`. See here for instructions: [https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jarsigner.html](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jarsigner.html)
3. **Redeploy:** Deploy the signed application to Google App Engine.

**Why Other Options Are Less Effective:**

- **A. Ensure all necessary JAR files are uploaded and redeploy your application.** This might help if a JAR was missing entirely, but likely won't resolve the SHA1 digest error.
- **C. Rebuild the CloakedServlet class using MD5 hashing instead of SHA1.** While MD5 is another hashing algorithm, it's considered less secure and not recommended for this purpose. The issue is with the manifest and signing, not specifically the hashing algorithm.
- **D. Only Clean and Rebuild Your Project** This won't address the SHA1 digest error, as it likely lies in the integrity of the JAR file itself rather than the project code.

**⚠️ Note:** A "SHA1 digest error" means the digest recorded in a JAR's manifest no longer matches the class inside it, usually because a signed JAR was modified or corrupted after signing. The real fix is to rebuild and correctly re-sign (or strip stale signatures from) the JARs. Option B is the closest match and is the commonly accepted key, but it is worded loosely.

</details>

---

### Exam 5 · Q11

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

**For this question, refer to the Altostrat Media case study. Altostrat uses Apigee to manage its APIs and wants to prevent excessive usage that could lead to abuse and unexpected costs. You must enable an Apigee capability that limits the total number of API calls. What should you do?**

- A. Enable API key validation.
- B. Implement OAuth 2.0 authorization.
- C. Configure Quota policies.
- D. Turn on XML threat protection.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Configure Quota policies.

**Correct option: C — Configure Quota policies**

Apigee Quota policies are specifically designed to **limit the number of API calls** a consumer can make within a defined time window. This directly addresses Altostrat’s requirement to prevent abuse and control unexpected cost spikes. Quotas enforce usage limits regardless of whether the caller is authenticated via API key or OAuth.

**Authoritative documentation:**
[https://cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy)

**Why C is correct**

- Explicitly limits total API calls
- Enforces rate/volume caps per app, developer, or API product
- Prevents overuse and abuse
- Controls cost exposure
- Built-in Apigee traffic management feature

Quota is the only option that directly satisfies the requirement: *limit total number of API calls*.

**Why the other options are not the best choice**

A. API key validation
API keys identify callers but **do not limit usage**. A valid key can still generate unlimited traffic unless paired with quotas.

B. OAuth 2.0 authorization
OAuth controls **who is allowed to access** an API, not how many times they can call it. It’s an identity/authorization mechanism, not a rate limiter.

D. XML threat protection
Protects against malicious XML payload attacks. It improves security posture but does **nothing to control API volume**.

**Need-to-know foundational concept**

Apigee traffic control layers:

- Authentication → API keys / OAuth
- Authorization → access control policies
- Protection → threat protection policies
- Usage control → **Quota + Spike Arrest**

Key exam takeaway:
If the requirement says *limit API calls*, the answer is always **Quota policy**.

###### Explanation

**Correct option: C — Configure Quota policies**

Apigee Quota policies are specifically designed to **limit the number of API calls** a consumer can make within a defined time window. This directly addresses Altostrat’s requirement to prevent abuse and control unexpected cost spikes. Quotas enforce usage limits regardless of whether the caller is authenticated via API key or OAuth.

> [!note]- Why the other options are wrong
> A. API key validation
> API keys identify callers but **do not limit usage**. A valid key can still generate unlimited traffic unless paired with quotas.
>
> B. OAuth 2.0 authorization
> OAuth controls **who is allowed to access** an API, not how many times they can call it. It’s an identity/authorization mechanism, not a rate limiter.
>
> D. XML threat protection
> Protects against malicious XML payload attacks. It improves security posture but does **nothing to control API volume**.

</details>

---

### Exam 5 · Q26

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

**For this question, refer to the KnightMotives Automotive case study. KnightMotives maintains supplier and pricing data in a central MySQL database at headquarters (HQ). Only HQ staff are permitted to modify this data. Each local plant keeps its own MySQL copy, often running a different schema or MySQL version. Every night, a batch process exports product and pricing changes from the HQ database as an XML file, places it on a central FTP server, and each plant downloads the file to apply updates to its local system. Some plants now have data that does not match the HQ source due to XML parsing problems. HQ wants a simple way to confirm that each plant has applied every change correctly.**

- A. Create a Pub/Sub topic for each supplier. HQ publishes supplier-specific changes as JSON messages to the corresponding topic. Each plant uses a Pub/Sub pull subscription to consume messages for its suppliers and update its database.
- B. Create a Pub/Sub topic for each supplier. HQ publishes supplier-specific changes as JSON messages to the corresponding topic. Each plant uses a Pub/Sub push subscription to receive messages for its suppliers and update its database.
- C. Move the HQ self-managed MySQL database to Cloud SQL. Standardize the database schema across all plants, and configure each plant’s database as an external read replica for Cloud SQL.
- D. Move the HQ self-managed MySQL database to Cloud SQL. Use Database Migration Service to replicate between Cloud SQL and the on-premises plant databases, selecting continuous migration rather than a one-time migration when creating the job.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Move the HQ self-managed MySQL database to Cloud SQL. Standardize the database schema across all plants, and configure each plant’s database as an external read replica for Cloud SQL.

**Correct answer: C**

**Move the HQ self-managed MySQL database to Cloud SQL. Standardize the database schema across all plants, and configure each plant's database as an external read replica for Cloud SQL.**

**Why C is correct**

- Only HQ writes the data, and every plant needs an exact, read-only copy. That is primary/replica replication.
- Cloud SQL for MySQL supports **external replicas**: MySQL servers outside Google Cloud (here, at each plant) that replicate from a Cloud SQL primary. See https://cloud.google.com/sql/docs/mysql/replication/configure-external-replica.
- MySQL replication applies every committed change in order, and replica status (lag, errors) shows whether a plant is in sync. That is the "simple way to confirm" HQ wants, and it removes the XML export, FTP and parsing steps that caused the drift.
- Replication needs compatible schemas and versions, which is why the option standardizes the plant schemas first. The case study's schema drift is the problem to fix, not a constraint to keep.

**Why the other options are wrong**

- **A / B. Pub/Sub topics per supplier.** You would have to build your own change capture, ordering, retries and reconciliation at each plant. It replaces one custom sync process with another and gives no built-in way to prove a plant matches HQ.
- **D. Database Migration Service continuous migration to the plants.** Database Migration Service migrates *into* Google Cloud: its destinations are Cloud SQL and AlloyDB, not on-premises MySQL servers (https://cloud.google.com/database-migration/docs/overview). It cannot replicate from Cloud SQL out to the plant databases, and it is a migration tool, not a permanent multi-site distribution mechanism.

</details>

---

### Exam 5 · Q32

**You are deploying a mission-critical application with a stateless, container-based frontend running on **Cloud Run** and a **Cloud SQL for PostgreSQL** backend. The workload sees unpredictable traffic surges, and the business needs the ability to **quickly roll back** any failed release to the most recent stable version. You want a deployment approach that follows **SRE best practices** for both application releases and database schema changes while meeting these rollback requirements. What should you do?**

- A. Bundle the database schema migration script into the container image and run it automatically every time a container starts, before launching the application.
- B. Set up the CI/CD pipeline to deploy using the `:latest` container image tag, and apply database schema updates manually whenever required.
- C. Use separate CI/CD pipelines for database schema migrations and application deployments. During a new Cloud Run revision rollout, use a gradual traffic split.
- D. Use a single CI/CD pipeline that applies database schema updates first, and then deploys the new Cloud Run revision.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use separate CI/CD pipelines for database schema migrations and application deployments. During a new Cloud Run revision rollout, use a gradual traffic split.

Correct Answer: **C**

**Use separate CI/CD pipelines for database schema migrations and application deployments. During a new Cloud Run revision rollout, use a gradual traffic split.**

Why C is correct (SRE + rollback-safe design)

This option matches **SRE release best practices** for systems with:

- **Stateless app deployments (Cloud Run revisions)**
- **Stateful database changes (Cloud SQL schema migrations)**
- **Need for fast rollback to last stable version**
- **Unpredictable traffic surges (safe progressive rollout)**

Key reasons:

**1) Cloud Run supports instant rollback using revisions**
Cloud Run creates an immutable **revision** per deployment. If the new release fails, you can immediately route traffic back to the previous stable revision.

**2) Gradual rollout reduces blast radius**
Using **traffic splitting** (example: 90% old / 10% new) lets you validate behavior safely before sending 100% traffic.

**3) Database migrations must be handled separately**
Database schema changes are **not as easily rollbackable** as application code changes.
Separating pipelines allows:

- Independent control, approvals, and timing
- Safer “expand/contract” migration patterns
- Preventing schema updates from being tightly coupled to app deployment timing

This is the most reliable way to meet rollback requirements **without risking database incompatibility**.

**Why the other options are incorrect**

A. Bundle migration into container startup and run every time

**Incorrect** because:

- Cloud Run can start many instances during surges → migration could run **multiple times concurrently**
- High risk of **race conditions**, locking, and failed startups
- Violates good practice: **schema changes should not run automatically on every instance start**

This is dangerous for mission-critical systems.

B. Deploy using `:latest` tag and apply schema updates manually

**Incorrect** because:

- `:latest` breaks release traceability and rollback reliability
  You can’t guarantee what “latest” actually points to.
- Manual DB updates increase human error and slow response time during incidents
- Not aligned with controlled SRE release practices

D. Single pipeline that updates schema first, then deploys app

**Not best fit** because:

- If schema changes are applied first and deployment fails, rollback becomes risky:
  the previous app version may not work with the new schema.
- Schema rollback is usually harder than app rollback.
- Tight coupling increases outage probability.

This violates the goal of **quick rollback to last stable version**.

Need-to-know fundamentals (for PCA exam)

- **Cloud Run revisions are immutable** → perfect for fast rollback.
- **Traffic splitting is the safest rollout strategy** → supports canary releases.
- **Database schema changes must be backward compatible** during rollouts:
  - Prefer **expand → deploy → contract**
  - Example: add nullable columns first, deploy new code, then remove old fields later.
- Avoid automatic migrations at runtime in autoscaling environments.

**Official documentation (authoritative)**

Cloud Run traffic splitting and revisions:
[https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)

###### Explanation

Why C is correct (SRE + rollback-safe design)

This option matches **SRE release best practices** for systems with:

- **Stateless app deployments (Cloud Run revisions)**
- **Stateful database changes (Cloud SQL schema migrations)**
- **Need for fast rollback to last stable version**
- **Unpredictable traffic surges (safe progressive rollout)**

> [!note]- Why the other options are wrong
> A. Bundle migration into container startup and run every time
>
> **Incorrect** because:
>
> - Cloud Run can start many instances during surges → migration could run **multiple times concurrently**
> - High risk of **race conditions**, locking, and failed startups
> - Violates good practice: **schema changes should not run automatically on every instance start**
>
> This is dangerous for mission-critical systems.
>
> B. Deploy using `:latest` tag and apply schema updates manually
>
> **Incorrect** because:
>
> - `:latest` breaks release traceability and rollback reliability
>   You can’t guarantee what “latest” actually points to.
> - Manual DB updates increase human error and slow response time during incidents
> - Not aligned with controlled SRE release practices
>
> D. Single pipeline that updates schema first, then deploys app
>
> **Not best fit** because:
>
> - If schema changes are applied first and deployment fails, rollback becomes risky:
>   the previous app version may not work with the new schema.
> - Schema rollback is usually harder than app rollback.
> - Tight coupling increases outage probability.

</details>

---

### Exam 5 · Q38

**You are migrating a mission-critical on-premises inventory management application to Google Cloud. The application is a monolith backed by a traditional relational database, and the short-term priority is a fast data center exit. The monolith also exposes an API that is consumed by other business-critical systems.**

**In the long run, the plan is to refactor the monolith into globally distributed, cloud-native services to support business growth. You need to design the initial cloud architecture so that future modernization introduces the least disruption for applications that rely on inventory data, especially since the API design may change later. What should you do?**

- A. Use **Service Directory** to register the monolith endpoint so dependent applications can discover the address and call it directly.
- B. Deploy a managed **API facade using Apigee** so dependent applications call Apigee, which forwards requests to the monolith backend.
- C. Use an **internal load balancer** to provide a fixed IP address so dependent applications can call the monolith’s API directly.
- D. Allow dependent applications to access the database directly by exposing secured **SQL VIEWs** in Cloud SQL for queries.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy a managed **API facade using Apigee** so dependent applications call Apigee, which forwards requests to the monolith backend.

**Correct Answer: B**

**Deploy a managed API facade using Apigee so dependent applications call Apigee, which forwards requests to the monolith backend.**

Why B is correct

You want a **fast data center exit now**, but you also want **future modernization with the least disruption** to systems consuming the inventory API, especially because:

- the monolith will be refactored into multiple services later
- the backend API design may evolve/change

Using **Apigee as an API facade** is the best architectural move because it creates a stable, governed contract in front of the monolith:

- **Decouples consumers from the backend implementation**
  Consumers integrate with Apigee, not directly with the monolith. Later, you can swap the backend from monolith → microservices with minimal consumer changes.
- **Supports controlled API evolution**
  Apigee helps manage:
  - API versioning
  - transformations (headers, payloads)
  - routing to multiple backends
  - policy enforcement (auth, quotas, spike arrest)
  - analytics and monitoring
- **Enables a clean modernization path**
  During refactor, Apigee can progressively route endpoints to new services while keeping the external API stable.

This is a classic **strangler-fig pattern enabler** for API modernization.

**Official reference: Apigee as an API management platform**
[https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

**Why the other options are incorrect / not best fit**

**A. Service Directory for discovery**

Service Directory helps service discovery inside your environment, but it does **not** provide:

- API governance
- stable consumer contract
- versioning and transformation capabilities
  It still encourages direct coupling to the monolith endpoint.

**C. Internal load balancer with a fixed IP**

This gives a stable IP, but dependent apps are still tightly coupled to the monolith API behavior. When you refactor, consumers may still break because the **API contract** changes, not the IP.

**D. Allow direct database access via SQL VIEWs**

This is the worst for long-term modernization:

- creates extreme coupling to the database schema
- bypasses API governance and business logic
- makes refactoring risky and disruptive
  It also increases security and compliance risks.

**Need-to-know fundamentals**

- For modernization with minimal disruption, introduce an **API abstraction layer** early.
- **Apigee** is purpose-built for managing API lifecycle, security policies, and controlled evolution.
- Avoid patterns that couple consumers directly to:
  - backend endpoints (tight coupling)
  - database schemas (very tight coupling)

**Official documentation link**

**Apigee overview (API facade, policy enforcement, analytics):**
[https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

###### Explanation

**Why B is correct**

You want a **fast data center exit now**, but you also want **future modernization with the least disruption** to systems consuming the inventory API, especially because:

- the monolith will be refactored into multiple services later
- the backend API design may evolve/change

Using **Apigee as an API facade** is the best architectural move because it creates a stable, governed contract in front of the monolith:

- **Decouples consumers from the backend implementation**
  Consumers integrate with Apigee, not directly with the monolith. Later, you can swap the backend from monolith → microservices with minimal consumer changes.
- **Supports controlled API evolution**
  Apigee helps manage:
  - API versioning
  - transformations (headers, payloads)
  - routing to multiple backends
  - policy enforcement (auth, quotas, spike arrest)
  - analytics and monitoring
- **Enables a clean modernization path**
  During refactor, Apigee can progressively route endpoints to new services while keeping the external API stable.

This is a classic **strangler-fig pattern enabler** for API modernization.

> [!note]- Why the other options are wrong
> A. Service Directory for discovery
>
> Service Directory helps service discovery inside your environment, but it does **not** provide:
>
> - API governance
> - stable consumer contract
> - versioning and transformation capabilities
>   It still encourages direct coupling to the monolith endpoint.
>
> C. Internal load balancer with a fixed IP
>
> This gives a stable IP, but dependent apps are still tightly coupled to the monolith API behavior. When you refactor, consumers may still break because the **API contract** changes, not the IP.
>
> D. Allow direct database access via SQL VIEWs
>
> This is the worst for long-term modernization:
>
> - creates extreme coupling to the database schema
> - bypasses API governance and business logic
> - makes refactoring risky and disruptive
>   It also increases security and compliance risks.

</details>

---

### Exam 5 · Q43

**Your team is running applications on a Google Kubernetes Engine (GKE) cluster that uses a private endpoint. You have already configured a Cloud Deploy pipeline, but deployments to the GKE cluster are failing. You need to fix the deployment issue. What should you do?**

- A. Enable **VPC Service Controls** for Cloud Build, and update the Cloud Deploy pipeline to use **Cloud Build** as the execution environment.
- B. Create a **Cloud Build private pool** in the default VPC, and use Cloud Build to deploy applications to the GKE cluster.
- C. Create a **Cloud Build private pool** that is **peered with the same VPC network** as the GKE cluster, and update the Cloud Deploy pipeline to use this private pool as its execution environment.
- D. Create a **custom target** in Cloud Deploy and update the pipeline to deploy the application using that custom target.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a **Cloud Build private pool** that is **peered with the same VPC network** as the GKE cluster, and update the Cloud Deploy pipeline to use this private pool as its execution environment.

**Correct Answer: C**

**Create a Cloud Build private pool that is connected to (in the same VPC / peered to) the VPC network used by the private GKE cluster, and configure Cloud Deploy to use that private pool as the execution environment.**

**Why C is correct**

Your GKE cluster has a **private endpoint**, which means the Kubernetes API server is reachable only from:

- resources inside the same VPC network, or
- networks that have private connectivity to it (for example, VPC peering / shared VPC / VPN / Interconnect)

By default, Cloud Deploy executions rely on Google-managed infrastructure that may not have network access to your **private** GKE control plane endpoint. That’s why deployments fail.

A **Cloud Build private pool** runs build/deploy jobs on workers that have **private network access** to your VPC. If that private pool is attached to (or has connectivity to) the **same VPC as the GKE private endpoint**, Cloud Deploy can reach the cluster API and successfully apply manifests.

This is the Google-recommended fix pattern:
**Private GKE endpoint → use Cloud Build private pool with VPC connectivity**.

**Why the other options are incorrect / not best fit**

**A. Enable VPC Service Controls for Cloud Build**

VPC Service Controls is about **data exfiltration protection** and service perimeters. It does not solve the core issue: **network reachability to a private GKE endpoint**.

**B. Cloud Build private pool in the default VPC**

If the GKE cluster is in a different VPC (or Shared VPC), a private pool in the default VPC will still not have network access to the private endpoint. The pool must be connected to the correct network.

**D. Create a custom target in Cloud Deploy**

Custom targets change *how* deployment is executed, but they don’t automatically provide **private network connectivity** to reach the GKE API server.

Need-to-know fundamentals

- **Private GKE endpoint** blocks public access to the Kubernetes API server.
- Deployment systems must run from a network that can reach the private control plane.
- **Cloud Build private pools** provide worker nodes with VPC connectivity, enabling access to private endpoints.
- Cloud Deploy can use Cloud Build private pools as its execution environment.

**Official documentation link**

**Cloud Build private pools (private worker pool connectivity):**
[https://cloud.google.com/build/docs/private-pools/private-pools-overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview)

###### Explanation

**Why C is correct**

Your GKE cluster has a **private endpoint**, which means the Kubernetes API server is reachable only from:

- resources inside the same VPC network, or
- networks that have private connectivity to it (for example, VPC peering / shared VPC / VPN / Interconnect)

By default, Cloud Deploy executions rely on Google-managed infrastructure that may not have network access to your **private** GKE control plane endpoint. That’s why deployments fail.

A **Cloud Build private pool** runs build/deploy jobs on workers that have **private network access** to your VPC. If that private pool is attached to (or has connectivity to) the **same VPC as the GKE private endpoint**, Cloud Deploy can reach the cluster API and successfully apply manifests.

This is the Google-recommended fix pattern:
**Private GKE endpoint → use Cloud Build private pool with VPC connectivity**.

> [!note]- Why the other options are wrong
> A. Enable VPC Service Controls for Cloud Build
>
> VPC Service Controls is about **data exfiltration protection** and service perimeters. It does not solve the core issue: **network reachability to a private GKE endpoint**.
>
> B. Cloud Build private pool in the default VPC
>
> If the GKE cluster is in a different VPC (or Shared VPC), a private pool in the default VPC will still not have network access to the private endpoint. The pool must be connected to the correct network.
>
> D. Create a custom target in Cloud Deploy
>
> Custom targets change *how* deployment is executed, but they don’t automatically provide **private network connectivity** to reach the GKE API server.

</details>

---

### Exam 5 · Q56

**A financial services organization is shutting down one of its on-premises data centers. As part of the shutdown, it must perform a one-time migration of 500 TB of historical transaction archives into a Cloud Storage bucket for long-term retention. The data center has a shared 1 Gbps internet egress link that is also used by critical production systems. The transfer must be completed securely within 60 days to meet the decommissioning timeline. What should you do?**

- A. Provision a 10 Gbps Partner Interconnect connection to speed up the migration, and use Storage Transfer Service for the data transfer.
- B. Create a script that runs `gcloud storage cp --parallel` to upload the data in chunks over the public internet during off-peak hours.
- C. Use Storage Transfer Service to configure an agent-based transfer that moves data directly from on-premises file servers into the Cloud Storage bucket.
- D. Order a Transfer Appliance, copy the data to the device over your high-speed local network, and ship it to Google so the data is uploaded into your Cloud Storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Order a Transfer Appliance, copy the data to the device over your high-speed local network, and ship it to Google so the data is uploaded into your Cloud Storage bucket.

**Correct option: D. Order a Transfer Appliance, copy the data locally, and ship it to Google for ingestion into Cloud Storage.**

**Need-to-know foundational concept**

When you must move **hundreds of TB** under a firm deadline and your **WAN bandwidth is constrained (and shared with production)**, the safest architecture is **offline bulk transfer**. It avoids saturating critical internet egress, reduces operational risk, and still supports secure chain-of-custody style handling. Google explicitly positions **Transfer Appliance** as the offline method for transferring very large datasets into Cloud Storage.

**Why the correct option fits the scenario**

- You have **500 TB** and only a **shared 1 Gbps** internet link. Even if 1 Gbps were dedicated, 500 TB is borderline within 60 days; with shared production usage, it becomes operationally risky (congestion, throttling, and unpredictable completion).
- **Transfer Appliance** lets you move data over the **high-speed local network** inside the data center, then ship the encrypted appliance to Google for upload into your Cloud Storage bucket—meeting the “secure” and “finish within 60 days” constraints without impacting production traffic.
- Google’s transfer options guidance explicitly includes **Transfer Appliance** as the right choice for large on-prem transfers (especially when network is a limitation).

**Documentation Link:** [https://cloud.google.com/storage-transfer-service](https://cloud.google.com/storage-transfer-service)

**Why the other options are not the best choice**

**A. Partner Interconnect + Storage Transfer Service**
Interconnect can provide high bandwidth, but it depends on **working with a service provider and provisioning connectivity** (and operational setup) which can be non-trivial during a tight decommissioning window. Partner Interconnect provisioning is a multi-party process (you + provider + Google), and the option does not address the core risk that the org’s internet egress is shared and constrained today.

**B. gcloud storage cp --parallel during off-peak**
This still uses the **shared 1 Gbps internet link** and risks disrupting production systems. “Off-peak” is also not a formal guarantee for completing 500 TB within 60 days because real-world throughput varies (network contention, retries, overhead).

**C. Storage Transfer Service agent-based transfer from on-prem**
Agent-based Storage Transfer Service is an **online transfer over your network**. While it supports bandwidth controls, it remains constrained by the same shared egress link and therefore carries the same deadline and production-risk problems.

For a one-time, deadline-driven migration of 500 TB with limited shared internet bandwidth, **Transfer Appliance** is the most reliable and least disruptive solution.

###### Explanation

**Correct option: D**

**Why the correct option fits the scenario**

- You have **500 TB** and only a **shared 1 Gbps** internet link. Even if 1 Gbps were dedicated, 500 TB is borderline within 60 days; with shared production usage, it becomes operationally risky (congestion, throttling, and unpredictable completion).
- **Transfer Appliance** lets you move data over the **high-speed local network** inside the data center, then ship the encrypted appliance to Google for upload into your Cloud Storage bucket—meeting the “secure” and “finish within 60 days” constraints without impacting production traffic.
- Google’s transfer options guidance explicitly includes **Transfer Appliance** as the right choice for large on-prem transfers (especially when network is a limitation).

> [!note]- Why the other options are wrong
> **A. Partner Interconnect + Storage Transfer Service**
> Interconnect can provide high bandwidth, but it depends on **working with a service provider and provisioning connectivity** (and operational setup) which can be non-trivial during a tight decommissioning window. Partner Interconnect provisioning is a multi-party process (you + provider + Google), and the option does not address the core risk that the org’s internet egress is shared and constrained today.
>
> **B. gcloud storage cp --parallel during off-peak**
> This still uses the **shared 1 Gbps internet link** and risks disrupting production systems. “Off-peak” is also not a formal guarantee for completing 500 TB within 60 days because real-world throughput varies (network contention, retries, overhead).
>
> **C. Storage Transfer Service agent-based transfer from on-prem**
> Agent-based Storage Transfer Service is an **online transfer over your network**. While it supports bandwidth controls, it remains constrained by the same shared egress link and therefore carries the same deadline and production-risk problems.

</details>

---

### Exam 5 · Q66

**You are preparing to launch a data fabric platform on Google Cloud in ten weeks and must migrate 2 petabytes of historical data from your on-premises data center. The transfer must be secure and provide low latency. What should you do?**

- A. Establish a 1 Gbps VPN connection between the data center and Google Cloud and use Storage Transfer Service to move the data.
- B. Request Google Cloud Transfer Appliances and use them to copy and ship the data.
- C. Provision a 1 Gbps Dedicated Interconnect connection and use Storage Transfer Service for the on-premises transfer.
- D. Export the data to portable disks and physically ship the disks to Google for import.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Request Google Cloud Transfer Appliances and use them to copy and ship the data.

**Correct option**: **B. Request Google Cloud Transfer Appliances and use them to copy and ship the data.**

**Need-to-know foundational concept**

At **petabyte scale**, network transfers become a physics problem, not just an architecture choice.

Even with a private connection, sustained transfer of **2 PB** over a 1 Gbps link would take many months. When bandwidth is the bottleneck and the deadline is fixed, Google’s best practice is to use **offline bulk transfer** with Transfer Appliance.

Transfer Appliance is specifically designed for **multi-petabyte migrations** when:

- the dataset is extremely large
- timelines are strict
- network transfer is impractical
- security must be guaranteed

It uses encrypted hardware, chain-of-custody tracking, and direct ingestion into Cloud Storage.

**Authoritative reference:**
[https://cloud.google.com/transfer-appliance/docs/4.0/overview](https://cloud.google.com/transfer-appliance/docs/4.0/overview)

**Why B is correct**

- 2 PB in 10 weeks is too large for 1 Gbps networking
- Transfer Appliance uses high-speed local LAN copying
- Appliances can be parallelized
- Google handles ingestion securely
- No dependence on WAN throughput
- Predictable timeline
- Built for exactly this scale

This is the scenario Transfer Appliance exists for.

**Why the other options are not the best choice**

**A. 1 Gbps VPN**
Far too slow for 2 PB. Also internet-based VPN adds latency and instability.

**C. 1 Gbps Interconnect**
Interconnect is faster and private, but 1 Gbps is still insufficient for 2 PB within 10 weeks. You would need much higher capacity, and provisioning timelines may exceed your schedule.

**D. Ship portable disks**
Not a supported enterprise workflow. Transfer Appliance replaces ad-hoc disk shipping with secure, audited, encrypted hardware and managed ingestion.

This question is testing a key PCA exam principle:

When dataset size exceeds practical network transfer limits, use Transfer Appliance.

At petabyte scale with a fixed deadline, **offline transfer wins**.

###### Explanation

**Correct option**: **B. Request Google Cloud Transfer Appliances and use them to copy and ship the data.**

**Need-to-know foundational concept**

At **petabyte scale**, network transfers become a physics problem, not just an architecture choice.

Even with a private connection, sustained transfer of **2 PB** over a 1 Gbps link would take many months. When bandwidth is the bottleneck and the deadline is fixed, Google’s best practice is to use **offline bulk transfer** with Transfer Appliance.

Transfer Appliance is specifically designed for **multi-petabyte migrations** when:

- the dataset is extremely large
- timelines are strict
- network transfer is impractical
- security must be guaranteed

It uses encrypted hardware, chain-of-custody tracking, and direct ingestion into Cloud Storage.

> [!note]- Why the other options are wrong
> **A. 1 Gbps VPN**
> Far too slow for 2 PB. Also internet-based VPN adds latency and instability.
>
> **C. 1 Gbps Interconnect**
> Interconnect is faster and private, but 1 Gbps is still insufficient for 2 PB within 10 weeks. You would need much higher capacity, and provisioning timelines may exceed your schedule.
>
> **D. Ship portable disks**
> Not a supported enterprise workflow. Transfer Appliance replaces ad-hoc disk shipping with secure, audited, encrypted hardware and managed ingestion.

</details>

---

### Exam 5 · Q72

**You are building a centralized, automated infrastructure deployment pipeline using Terraform and Cloud Build. Security policy forbids long-lived service account keys in CI/CD, and developers may submit infrastructure changes for review but must not be able to directly apply changes in the production project. You need a secure workflow that enforces governance while keeping deployment automated. What should you do?**

- A. Configure Cloud Build to use service account impersonation and automatically run `terraform apply` when a pull request is merged.
- B. Use service account impersonation in Cloud Build, run `terraform plan` on pull requests, and require a manual approval step before executing `terraform apply`.
- C. Limit the pipeline to running `terraform plan`, and after approval have an authorized developer execute `terraform apply` from a secured workstation.
- D. Create a highly privileged service account, store its JSON key in Secret Manager, and configure Cloud Build to retrieve and use the key during Terraform execution.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use service account impersonation in Cloud Build, run `terraform plan` on pull requests, and require a manual approval step before executing `terraform apply`.

**Correct option:** **B. Use service account impersonation in Cloud Build, run `terraform plan` on pull requests, and require a manual approval step before executing `terraform apply`.**

**Need-to-know foundational concept**

A secure Terraform CI/CD pipeline on Google Cloud should follow two key governance principles:

1. **No long-lived credentials** → use **service account impersonation** instead of keys
2. **Separation of duties** → developers can propose changes, but production apply requires approval

Cloud Build supports both:

- short-lived credentials via impersonation
- built-in **manual approval gates**
- automated execution after approval
- centralized audit trail

**Google explicitly recommends impersonation instead of service account keys for CI/CD pipelines:**
[https://cloud.google.com/iam/docs/service-account-impersonation](https://cloud.google.com/iam/docs/service-account-impersonation)

**Why the correct option fits the scenario**

**Option B provides:**

- zero long-lived keys
- automated plan generation for review
- governance via approval gate
- automated apply after approval
- developers cannot bypass controls
- centralized logging & auditability
- fully automated deployment

This matches enterprise Terraform best practices.

**Why the other options are not the best choice**

**A. Auto apply on merge**
Violates governance. Developers could indirectly push to production without approval.

**C. Manual apply from workstation**
Breaks automation and introduces credential sprawl. It weakens auditability and repeatability.

**D. Store service account key in Secret Manager**
Still uses long-lived credentials. This explicitly violates the security policy.

Exam principle:

Secure Terraform CI/CD = impersonation + approval gate + automated apply.

Final answer: **B**

###### Explanation

**Why the correct option fits the scenario**

**Option B provides:**

- zero long-lived keys
- automated plan generation for review
- governance via approval gate
- automated apply after approval
- developers cannot bypass controls
- centralized logging & auditability
- fully automated deployment

This matches enterprise Terraform best practices.

> [!note]- Why the other options are wrong
> **A. Auto apply on merge**
> Violates governance. Developers could indirectly push to production without approval.
>
> **C. Manual apply from workstation**
> Breaks automation and introduces credential sprawl. It weakens auditability and repeatability.
>
> **D. Store service account key in Secret Manager**
> Still uses long-lived credentials. This explicitly violates the security policy.

</details>

---

### Exam 5 · Q74

**Your organization is cloud-native and relies heavily on Google Kubernetes Engine (GKE) for container workloads. You want to adopt infrastructure-as-code practices to automate provisioning, configuration, and lifecycle management of Google Cloud resources while reducing operational overhead. What should you do?**

- A. Install Config Sync and manage Google Cloud resources using YAML manifests stored in a GitHub repository.
- B. Install Config Connector and use Python scripts to define and manage the desired state of Google Cloud resources.
- C. Deploy Config Controller and define Google Cloud resources with YAML manifests, then apply those manifests to provision and manage infrastructure.
- D. Build a custom Kubernetes operator in your GKE cluster to run your own IaC automation scripts for managing Google Cloud resources.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy Config Controller and define Google Cloud resources with YAML manifests, then apply those manifests to provision and manage infrastructure.

**Correct option: C. Deploy Config Controller and define Google Cloud resources with YAML manifests, then apply those manifests to provision and manage infrastructure.**

**Need-to-know foundational concept**

If you’re already Kubernetes-centric and want infrastructure-as-code with low operational overhead, the cleanest pattern is **Kubernetes-native IaC**: manage Google Cloud resources using Kubernetes-style **YAML manifests** and a controller that reconciles desired state to actual state. **Config Controller** provides a **fully managed** Kubernetes control plane purpose-built to run **Config Connector**, so you can manage Google Cloud resources declaratively without having to operate the management cluster yourself.
[https://cloud.google.com/config-connector/docs/concepts/config-controller-overview](https://cloud.google.com/config-connector/docs/concepts/config-controller-overview)

**Why the chosen option is correct**

- It matches the organization’s cloud-native/GKE operating model: teams use the same Kubernetes workflow (manifests, GitOps, review/merge) for both app and infrastructure.
- It reduces ops overhead: Config Controller is managed and designed specifically for Google Cloud resource management through Config Connector.
- It standardizes provisioning + lifecycle management: resources are reconciled continuously from the YAML desired state.

**Why the other options are not the best choice**

**A. Install Config Sync and manage Google Cloud resources using YAML manifests stored in a GitHub repository.**
Config Sync is primarily for **Kubernetes configuration** (cluster resources and policies). It’s not the core tool for provisioning and managing *Google Cloud resources* themselves; that role is handled by Config Connector / Config Controller.

**B. Install Config Connector and use Python scripts to define and manage the desired state of Google Cloud resources.**
Config Connector is declarative and YAML-driven; “Python scripts” shifts you back toward imperative automation and higher maintenance. Also, this option doesn’t address the “reduce operational overhead” angle as strongly as using the managed Config Controller approach.

**D. Build a custom Kubernetes operator in your GKE cluster to run your own IaC automation scripts for managing Google Cloud resources.**
This increases operational burden and risk (custom code, ongoing maintenance, edge cases, upgrades). It’s the opposite of Google-recommended best practice when a managed, supported controller exists for the exact problem.

Final answer: **C**

###### Explanation

**Correct option: C. Deploy Config Controller and define Google Cloud resources with YAML manifests, then apply those manifests to provision and manage infrastructure.**

**Need-to-know foundational concept**

If you’re already Kubernetes-centric and want infrastructure-as-code with low operational overhead, the cleanest pattern is **Kubernetes-native IaC**: manage Google Cloud resources using Kubernetes-style **YAML manifests** and a controller that reconciles desired state to actual state. **Config Controller** provides a **fully managed** Kubernetes control plane purpose-built to run **Config Connector**, so you can manage Google Cloud resources declaratively without having to operate the management cluster yourself.

**Why the chosen option is correct**

- It matches the organization’s cloud-native/GKE operating model: teams use the same Kubernetes workflow (manifests, GitOps, review/merge) for both app and infrastructure.
- It reduces ops overhead: Config Controller is managed and designed specifically for Google Cloud resource management through Config Connector.
- It standardizes provisioning + lifecycle management: resources are reconciled continuously from the YAML desired state.

> [!note]- Why the other options are wrong
> **A. Install Config Sync and manage Google Cloud resources using YAML manifests stored in a GitHub repository.**
> Config Sync is primarily for **Kubernetes configuration** (cluster resources and policies). It’s not the core tool for provisioning and managing *Google Cloud resources* themselves; that role is handled by Config Connector / Config Controller.
>
> **B. Install Config Connector and use Python scripts to define and manage the desired state of Google Cloud resources.**
> Config Connector is declarative and YAML-driven; “Python scripts” shifts you back toward imperative automation and higher maintenance. Also, this option doesn’t address the “reduce operational overhead” angle as strongly as using the managed Config Controller approach.
>
> **D. Build a custom Kubernetes operator in your GKE cluster to run your own IaC automation scripts for managing Google Cloud resources.**
> This increases operational burden and risk (custom code, ongoing maintenance, edge cases, upgrades). It’s the opposite of Google-recommended best practice when a managed, supported controller exists for the exact problem.

</details>

---

### Exam 5 · Q82

**Your organization runs workloads on both Google Kubernetes Engine (GKE) and Amazon EKS in a multi-cloud Kubernetes environment. You need a solution that simplifies configuration management, enforces security controls, and guarantees consistent deployments across clusters, while aligning with Google-recommended practices. What should you do?**

- A. Use Argo CD for GitOps delivery, enforce policies with Open Policy Agent (OPA), and build a custom controller for multi-cluster configuration management.
- B. Deploy Crossplane to manage cloud resources as Kubernetes objects, use FluxCD for GitOps synchronization, and apply Kyverno for policy enforcement.
- C. Use Kustomize for configuration templating, Config Sync with multiple repositories, and custom scripts to enforce policies.
- D. Use Config Sync to distribute configurations from a central repository and use Policy Controller (OPA Gatekeeper) to enforce policies.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use Config Sync to distribute configurations from a central repository and use Policy Controller (OPA Gatekeeper) to enforce policies.

**Correct option:** **D. Use Config Sync to distribute configurations from a central repository and use Policy Controller (OPA Gatekeeper) to enforce policies.**

**Need-to-know foundational concept**

Google’s recommended multi-cluster configuration model is built around **Anthos Config Management (ACM)**. ACM provides:

- **Config Sync** → GitOps-style configuration distribution across clusters
- **Policy Controller** (based on OPA Gatekeeper) → centralized policy enforcement

This combination ensures:

- consistent cluster state
- declarative Git-based delivery
- security guardrails
- automatic drift correction
- scalable multi-cluster governance

**Anthos Config Management overview:**
[https://cloud.google.com/anthos-config-management/docs/overview](https://cloud.google.com/anthos-config-management/docs/overview)

**Why option D is correct**

Option D matches Google’s official architecture pattern:

- Config Sync = centralized GitOps distribution
- Policy Controller = enforce security/compliance rules
- Works across multiple clusters
- Eliminates custom tooling
- Aligns with Google-supported best practices
- Designed specifically for enterprise multi-cluster Kubernetes

It provides consistency + governance without DIY complexity.

**Why the other options are not the best choice**

**A. Argo + OPA + custom controller**
Functional but introduces custom engineering and operational burden. Google recommends ACM instead of custom frameworks.

**B. Crossplane + Flux + Kyverno**
Powerful but not Google’s recommended enterprise stack. Adds complexity and tool sprawl.

**C. Kustomize + scripts**
Not scalable governance. Scripts are fragile and not policy-enforcing.

Exam principle:

Multi-cluster Kubernetes governance → Anthos Config Management.

Final answer: D

###### Explanation

**Correct option:** **D.**

**Need-to-know foundational concept**

Google’s recommended multi-cluster configuration model is built around **Anthos Config Management (ACM)**. ACM provides:

- **Config Sync** → GitOps-style configuration distribution across clusters
- **Policy Controller** (based on OPA Gatekeeper) → centralized policy enforcement

This combination ensures:

- consistent cluster state
- declarative Git-based delivery
- security guardrails
- automatic drift correction
- scalable multi-cluster governance

**Why option D is correct**

Option D matches Google’s official architecture pattern:

- Config Sync = centralized GitOps distribution
- Policy Controller = enforce security/compliance rules
- Works across multiple clusters
- Eliminates custom tooling
- Aligns with Google-supported best practices
- Designed specifically for enterprise multi-cluster Kubernetes

> [!note]- Why the other options are wrong
> **A. Argo + OPA + custom controller**
> Functional but introduces custom engineering and operational burden. Google recommends ACM instead of custom frameworks.
>
> **B. Crossplane + Flux + Kyverno**
> Powerful but not Google’s recommended enterprise stack. Adds complexity and tool sprawl.
>
> **C. Kustomize + scripts**
> Not scalable governance. Scripts are fragile and not policy-enforcing.

</details>

---
