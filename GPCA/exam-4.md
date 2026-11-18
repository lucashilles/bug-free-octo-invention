# Professional Cloud Architect — Practice Exam 4

66 questions.

## Question 1

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

**DataNova Corp.** uses **BigQuery** as its data warehouse in a **pay-per-query pricing model**. You want to monitor **query activity in real time**, identify the **most expensive queries**, and determine **which users are generating the highest costs**.

What should you do?

- [ ] A. Add **labels** for each user to the BigQuery dataset containing the queried tables Go to the **Billing page** of the project Select **Reports** Filter the product by **BigQuery** and select the **user** you want to analyze
- [x] B. Create a **Cloud Logging sink** to export **BigQuery Data Access logs** to **BigQuery** Use **SQL queries** on the exported logs to extract cost and usage details per user
- [ ] C. Create a **Cloud Logging sink** to export **BigQuery Data Access logs** to **Cloud Storage** Use a **Dataflow pipeline** to analyze the exported logs and compute costs per user
- [ ] D. Enable **Billing Export to BigQuery** Query the exported **billing dataset** to extract usage and cost data per user

### Explanation

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

---

## Question 2

*Domain 2: Managing and Provisioning a Solution Infrastructure*

TechNova Corp and one of its key collaborators each manage their own Google Cloud projects under different organizations. TechNova's project (project-alpha) uses a Virtual Private Cloud named vpc-alpha, while the collaborator's project (project-beta) operates in vpc-beta. Within vpc-alpha, there are two compute instances running, and vpc-beta contains one compute instance. The IP subnets across both VPCs are non-overlapping.

You’ve been asked to ensure **low-latency, high-throughput internal IP communication** between all compute instances across both VPCs. What should you do?

- [x] A. Establish VPC Network Peering between vpc-alpha and vpc-beta.
- [ ] B. Set up a Cloud VPN tunnel to connect vpc-alpha and vpc-beta.
- [ ] C. Enable IAP TCP forwarding on the instance in vpc-beta, and from an instance in vpc-alpha, run the following command: gcloud compute start-iap-tunnel INSTANCE_NAME_IN_VPC_B 22 --local-host-port=localhost:22
- [ ] D. Launch a new instance in vpc-alpha. Launch a new instance in vpc-beta. Install OpenVPN on both newly created instances. Set up a VPN tunnel between vpc-alpha and vpc-beta using OpenVPN.

### Explanation

**Correct Answer: A. Establish VPC Network Peering between vpc-alpha and vpc-beta.**

✅ **Explanation for Correct Option:**

**VPC Network Peering** is the best solution for **low-latency**, **high-throughput**, and **internal IP** communication across **Google Cloud VPC networks**, even if they are in **different projects or different organizations**, **as long as the IP ranges do not overlap**, which is the case here.

- It allows private RFC 1918 IP address communication between VM instances across peered networks.
- Peering uses Google’s internal network, ensuring low-latency and high-bandwidth connections.
- It is **not transitive**, but since the goal is **bidirectional communication between two specific VPCs**, it’s ideal.

**Documentation Reference:**

- Official Google Cloud documentation on VPC Network Peering:
  [https://cloud.google.com/vpc/docs/vpc-peering](https://cloud.google.com/vpc/docs/vpc-peering)

*“VPC Network Peering enables you to connect VPC networks so that workloads in different VPC networks can communicate internally. Traffic stays on Google's high-speed backbone and doesn't traverse the public internet.”*

❌ **Why Other Options Are Incorrect:**

**B. Set up a Cloud VPN tunnel to connect vpc-alpha and vpc-beta.**

- **Incorrect**, though Cloud VPN supports connecting different VPCs, it introduces **more latency** and **lower throughput** compared to VPC peering.
- Cloud VPN encrypts traffic and uses **IPsec over the public internet**, which can be **less performant** and **more complex** for just internal communication.

**Documentation Reference:** [https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview)

*“For high-throughput, low-latency connections between Google Cloud VPCs, consider using VPC Network Peering instead of Cloud VPN.”*

**C. Enable IAP TCP forwarding on the instance in vpc-beta, and from an instance in vpc-alpha, run...**

- **Incorrect**. This is a **manual and temporary method**, suitable only for administrative access (like SSH or RDP) over **port forwarding**, not general-purpose internal IP communication.
- It is not scalable or meant for continuous or high-throughput application-level communication between VMs.

*“IAP TCP forwarding is primarily intended for administrative access, such as using SSH or RDP over the internet in a secure way.”*

**D. Set up a VPN tunnel between vpc-alpha and vpc-beta using OpenVPN.**

- **Incorrect**. While technically feasible, setting up OpenVPN is **manual**, **requires maintaining and securing servers**, and **adds latency**.
- It is not recommended for internal VM communication when more performant and native options like **VPC Peering** exist.

*“OpenVPN solutions require more operational overhead and are not preferred for internal communication between Google Cloud VPCs.”*

✅ Final Answer: **A. Establish VPC Network Peering between vpc-alpha and vpc-beta.**

Because it is **simple to configure**, supports **private internal IPs**, ensures **low-latency**, **high-throughput**, and works **across different organizations** as long as the networks are non-overlapping.

---

## Question 3

*Domain 2: Managing and Provisioning a Solution Infrastructure*

Your organization, **DataVerse Solutions**, needs to store sensitive business data in Google Cloud Storage buckets. This data is frequently updated, but past versions must remain accessible for reference. You also need to maintain a complete history of changes made to any object in these buckets. Furthermore, it should be easy to recover from accidental edits or deletions.

Which Cloud Storage feature should you enable to meet these requirements?

- [ ] A. **Bucket Lock** – Enforce retention policies to prevent deletion or modification of objects for a set period.
- [x] B. **Object Versioning** – Maintain multiple versions of an object, allowing access to older versions when needed.
- [ ] C. **Object Change Notification** – Receive notifications whenever an object in the bucket is modified.
- [ ] D. **Object Lifecycle Management** – Automate deletion or transition of objects to different storage classes based on defined rules.

### Explanation

**Correct Answer: B. Object Versioning – Maintain multiple versions of an object, allowing access to older versions when needed.**

✅ **Justification for the Correct Option (B):**

**Object Versioning** is the most suitable Google Cloud Storage feature for the given scenario because it directly addresses all the key requirements:

- **Frequent updates** to objects → Supported.
- **Past versions must remain accessible** → Maintains archived (noncurrent) versions.
- **Maintain a complete history of changes** → Enables access to all generations of the object.
- **Easy recovery from accidental edits or deletions** → You can restore a previous version or retrieve a deleted object.

When Object Versioning is enabled:

- Deleting or overwriting an object **does not permanently remove it**; a **new version is created**, and older versions are retained.
- You can access older versions by referencing their generation number.

**Official Google Cloud Documentation:**

“When you enable Object Versioning on a bucket, Cloud Storage automatically keeps a history of modifications to objects. This feature lets you retrieve versions of objects that are overwritten or deleted.”

❌ **Why Other Options Are Incorrect:**

**A. Bucket Lock – Enforce retention policies to prevent deletion or modification of objects for a set period.**

- **Incorrect**, because it is designed to **lock objects** against deletion or modification for compliance (WORM - Write Once Read Many).
- It does **not support version history** or recovery of older versions on updates.
- Once locked, the retention policy **cannot be shortened**, which can be restrictive.

**Source:** [https://cloud.google.com/storage/docs/](https://cloud.google.com/storage/docs/)bucket-lock

“Bucket Lock allows you to configure a data retention policy for a Cloud Storage bucket that governs how long objects in the bucket must be retained.”

**C. Object Change Notification – Receive notifications whenever an object in the bucket is modified.**

- **Incorrect**, because it only **notifies** about object changes.
- It does **not store previous versions** or enable rollback/recovery.
- Deprecated in favor of **Pub/Sub notifications**.

**Source:** [https://cloud.google.com/storage/docs/object-change-notification](https://cloud.google.com/storage/docs/object-change-notification)

“This feature is deprecated and replaced by Pub/Sub notifications. Notifications do not retain object versions or changes.”

**D. Object Lifecycle Management – Automate deletion or transition of objects to different storage classes based on defined rules.**

- **Incorrect**, because it helps in **cost optimization** by automating object transitions or deletions.
- It does not preserve older versions unless versioning is enabled.
- Not useful for **maintaining a history of changes** or **recovery from deletions** unless paired with versioning.

**Source:** [https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)

“Object Lifecycle Management lets you automatically manage objects, for example by deleting or transitioning them to cheaper storage classes.”

✅ Final Answer: **B. Object Versioning**

---

## Question 4

*Domain 2: Managing and Provisioning a Solution Infrastructure*

You’re managing a Compute Engine-based application for **CloudNexus Inc.** that needs to automatically scale when memory usage exceeds 80%. You've installed the Cloud Monitoring agent and configured the following autoscaling policy:

- **Metric Identifier**: `agent.googleapis.com/memory/percent_used`
- **Filter**: `metric.label.state = 'used'`
- **Target Utilization Level**: `80`
- **Target Type**: `GAUGE`

However, the application does **not scale up** under heavy memory load. You need to fix the configuration so autoscaling works as expected.

What should you do?

- [ ] A. Change the **Target Type** to `DELTA_PER_MINUTE`.
- [ ] B. Change the **Metric Identifier** to `agent.googleapis.com/memory/bytes_used`.
- [ ] C. Modify the **Filter** to: `metric.label.state = 'used' AND metric.label.state = 'buffered' AND metric.label.state = 'cached' AND metric.label.state = 'slab'`.
- [x] D. Update the **Filter** to: `metric.label.state = 'free'` and change the **Target Utilization Level** to `20`.

### Explanation

**Correct option: D**

D. Change the filter to `metric.label.state = 'free'` and the Target utilization to `20`.

This is correct because **Compute Engine autoscaling based on Cloud Monitoring metrics works best with metrics where “higher value = more available capacity”** (for example, CPU utilization, free resources, etc.).

For memory, using `percent_used` with `state='used'` often does **not** behave as expected for autoscaling because Linux memory accounting includes cache/buffers and “used” memory may not reflect real pressure accurately.
A more reliable approach is to scale based on **low free memory**, which is directly actionable:

- If **free memory drops below 20%**, that implies **~80% memory is consumed**
- Autoscaler can then scale out properly

**Why the other options are incorrect**

A. Change the Target type to `DELTA_PER_MINUTE`.

Incorrect because memory usage is a **GAUGE** metric (instantaneous value), not a rate/counter. `DELTA_PER_MINUTE` is used for metrics that represent change over time.

B. Change the Metric identifier to `agent.googleapis.com/memory/bytes_used`.

Incorrect because the problem is not the unit (percent vs bytes). Even bytes-used memory can still be misleading due to Linux cache/buffer behavior. The core issue is **choosing the wrong memory signal to scale on**.

Documentation:
[https://cloud.google.com/monitoring/api/metrics_agent](https://cloud.google.com/monitoring/api/metrics_agent)

C. Change the filter to include `used AND buffered AND cached AND slab`.

Incorrect because this filter is logically impossible as written:
A single time series cannot have `state='used'` AND `state='cached'` at the same time. These are **different label values**, so you would need aggregation logic, not an AND filter.

Documentation (metric labels and filtering):
[https://cloud.google.com/monitoring/api/v3/filters](https://cloud.google.com/monitoring/api/v3/filters)

**Final Answer: D**

###### Explanation

D. Change the filter to `metric.label.state = 'free'` and the Target utilization to `20`.

This is correct because **Compute Engine autoscaling based on Cloud Monitoring metrics works best with metrics where “higher value = more available capacity”** (for example, CPU utilization, free resources, etc.).

For memory, using `percent_used` with `state='used'` often does **not** behave as expected for autoscaling because Linux memory accounting includes cache/buffers and “used” memory may not reflect real pressure accurately.
A more reliable approach is to scale based on **low free memory**, which is directly actionable:

- If **free memory drops below 20%**, that implies **~80% memory is consumed**
- Autoscaler can then scale out properly

> [!note]- Why the other options are wrong
> A. Change the Target type to `DELTA_PER_MINUTE`.
>
> Incorrect because memory usage is a **GAUGE** metric (instantaneous value), not a rate/counter. `DELTA_PER_MINUTE` is used for metrics that represent change over time.
>
> B. Change the Metric identifier to `agent.googleapis.com/memory/bytes_used`.
>
> Incorrect because the problem is not the unit (percent vs bytes). Even bytes-used memory can still be misleading due to Linux cache/buffer behavior. The core issue is **choosing the wrong memory signal to scale on**.
>
> Documentation:
> [https://cloud.google.com/monitoring/api/metrics_agent](https://cloud.google.com/monitoring/api/metrics_agent)
>
> C. Change the filter to include `used AND buffered AND cached AND slab`.
>
> Incorrect because this filter is logically impossible as written:
> A single time series cannot have `state='used'` AND `state='cached'` at the same time. These are **different label values**, so you would need aggregation logic, not an AND filter.
>
> Documentation (metric labels and filtering):
> [https://cloud.google.com/monitoring/api/v3/filters](https://cloud.google.com/monitoring/api/v3/filters)

**⚠️ Note:** Doubtful key. Google's documented setup for memory-based MIG autoscaling is exactly the one in the stem: `agent.googleapis.com/memory/percent_used`, filter `metric.label.state = 'used'`, GAUGE. The autoscaler adds VMs when the metric is **above** the target, and free memory falls as load rises, so option D would scale the wrong way. None of the other options fixes it either (C's AND filter matches nothing). (Exam 5 · Q51) keys the 'used' filter as the fix. Learn: memory autoscaling = Ops Agent + percent_used + state='used'.

---

## Question 5

*Domain 2: Managing and Provisioning a Solution Infrastructure*

You’re deploying an application to Google Cloud for **NextPhase Systems**. This application is part of a broader system that includes services running outside Google Cloud. The Google Cloud-hosted application must establish private network communication with external (non-GCP) applications. The expected **average network throughput is 200 kbps**.

The business requires:

- **Maximum possible system availability (near 100%)**
- **Cost-effective solution**

You need to design the network connectivity between Google Cloud and the external environment to meet these goals.

What should you implement?

- [x] A. Provision an **HA (High Availability) Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.
- [ ] B. Set up **two Classic Cloud VPN gateways**, each with two tunnels, and connect them to separate on-premises VPN gateways.
- [ ] C. Deploy **two HA Cloud VPN gateways**, each with two tunnels connected to different on-premises VPN gateways.
- [ ] D. Use a **single Cloud VPN gateway** connected to the on-premises VPN gateway.

### Explanation

**Correct Answer: A. Provision an HA (High Availability) Cloud VPN gateway with two tunnels connected to the on-premises VPN gateway.**

✅ **Justification for Correct Option (A):**

This option **meets both the high availability and cost-effectiveness requirements** for low-throughput (200 kbps) private communication between Google Cloud and non-GCP (on-prem or external) systems.

**Why it's the best fit:**

- **HA (High Availability) Cloud VPN** provides **built-in redundancy and failover** using two interfaces (each with one tunnel), and it operates in **active/active mode**.
- Supports **uptime near 99.99%**, which aligns well with the “**maximum possible system availability**” requirement.
- Since the **throughput is only 200 kbps**, HA Cloud VPN is **more cost-effective** than Dedicated Interconnect or Partner Interconnect.
- You only need **one HA VPN gateway**, not multiple, as it already offers high availability.

**Official Documentation Reference:**

- HA VPN overview

"HA VPN provides an SLA of 99.99% service availability. Each HA VPN gateway interface supports one tunnel, and you can create up to two interfaces, achieving redundancy and fault tolerance."

❌ **Why Other Options Are Incorrect:**

**B. Set up two Classic Cloud VPN gateways, each with two tunnels, and connect them to separate on-premises VPN gateways.**

- **Incorrect**, because **Classic Cloud VPN** does **not provide an SLA**, and managing two Classic gateways with two tunnels each increases **operational overhead**.
- Less cost-effective than HA VPN and doesn’t match the goal of **maximizing availability with minimal complexity**.

**Reference:**
[https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview#vpn_classic](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview#vpn_classic)

**C. Deploy two HA Cloud VPN gateways, each with two tunnels connected to different on-premises VPN gateways.**

- **Incorrect**, because one **HA VPN gateway already provides high availability**.
- Deploying two HA VPN gateways is **over-engineering** the solution for 200 kbps throughput.
- It increases **cost unnecessarily**, violating the “**cost-effective**” requirement.

**D. Use a single Cloud VPN gateway connected to the on-premises VPN gateway.**

- **Incorrect**, because a **single tunnel** setup (classic or HA) creates a **single point of failure**.
- This option **fails the high availability requirement** ("maximum possible system availability").

✅ Final Answer: **A. Provision an HA (High Availability) Cloud VPN gateway with two tunnels connected to the on-premises VPN gateway.**

---

## Question 6

*Domain 5: Managing Implementation*

**Your company's application, hosted on App Engine, facilitates user uploads of music files directly into Cloud Storage from their browser session, bypassing the backend. What steps should you take to accomplish this?**

- [x] A. Configure CORS in the target Cloud Storage bucket, allowing the base URL of the App Engine application as an allowed origin. Utilize the Cloud Storage Signed URL feature to generate a POST URL for uploads.
- [ ] B. Configure CORS in the target Cloud Storage bucket, permitting the base URL of the App Engine application as an allowed origin. Grant users who upload files the Cloud Storage WRITER role.
- [ ] C. Utilize the Cloud Storage Signed URL feature to generate a POST URL for uploads. Employ App Engine default credentials to sign requests for Cloud Storage operations.
- [ ] D. Grant users who upload files the Cloud Storage WRITER role. Utilize App Engine default credentials to sign requests for Cloud Storage operations.

### Explanation

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

---

## Question 7

*Domain 2: Managing and Provisioning a Solution Infrastructure*

You're setting up the network architecture for a newly launched project at **NovaEdge Technologies**, which will host applications on Google Compute Engine. Virtual machine (VM) instances will be deployed in **two different subnets** within a single region:

- Instances in `subnet-alpha` will have public IP addresses.
- Instances in `subnet-beta` will use only private IP addresses.

To keep their software up to date, all instances must be able to **access a public package repository** hosted outside of Google Cloud.

How can you allow instances in `subnet-beta` to reach the external repository?

- [ ] A. Enable **Private Google Access** for `subnet-beta`.
- [x] B. Set up **Cloud NAT** and include `subnet-beta` in the NAT subnet configuration.
- [ ] C. Deploy a **bastion host** in `subnet-alpha` and use it to proxy traffic for instances in `subnet-beta`.
- [ ] D. Enable **Identity-Aware Proxy (IAP)** for TCP forwarding on the instances in `subnet-beta`.

### Explanation

**Correct Answer: B. Set up Cloud NAT and include subnet-beta in the NAT subnet configuration.**

✅ **Justification for Correct Option (B):**

**Cloud NAT (Network Address Translation)** is the correct and recommended solution when:

- Instances **do not have external (public) IPs**, like those in **subnet-beta**.
- You want them to **access the internet securely**, such as **downloading packages from public repositories**.
- You do **not want to expose** these VMs directly to the internet.

**Cloud NAT** allows private VM instances to initiate **outbound connections** to the internet **without a public IP**, while still **blocking inbound connections** for security.

**Why this meets the scenario:**

- Subnet-beta instances need to **reach external public repositories**.
- These instances **lack external IPs**, so **Cloud NAT** is required for outbound access.

**Official Documentation:**

- Cloud NAT Overview

*"Cloud NAT (Network Address Translation) allows resources without external IP addresses to access the internet in a controlled and secure manner."*

❌ **Why Other Options Are Incorrect:**

**A. Enable Private Google Access for subnet-beta.**

- **Incorrect**, because **Private Google Access** only allows access to **Google APIs and services** (like `*.googleapis.com`) **from VMs without public IPs**.
- It **does not provide access to the public internet**, including **third-party package repositories** (e.g., Debian, Ubuntu, or Python mirrors).

**Documentation:**
[https://cloud.google.com/vpc/docs/private-google-access](https://cloud.google.com/vpc/docs/private-google-access)

*"Private Google Access does not provide access to the public internet."*

**C. Deploy a bastion host in subnet-alpha and use it to proxy traffic for instances in subnet-beta.**

- **Incorrect**, because this setup:
  - Adds **manual configuration and maintenance overhead**.
  - Is **not scalable** for outbound traffic.
  - Is typically used for **SSH or admin access**, not package download traffic.

**D. Enable Identity-Aware Proxy (IAP) for TCP forwarding on the instances in subnet-beta.**

- **Incorrect**, because IAP is meant for **secure remote access to internal applications** over HTTPS or SSH — **not for allowing outbound internet access**.

*"IAP enables access to your application from outside without exposing your VMs to the internet, but it does not enable internet-bound access from those VMs."*

✅ **Final Answer: B. Set up Cloud NAT and include subnet-beta in the NAT subnet configuration.**

---

## Question 8

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**ZenCore Enterprises** is preparing to migrate their **Windows Server 2022** workloads from their on-premises data center to Google Cloud. They want to **bring their existing Windows Server licenses** into the cloud environment as part of the migration process.

What steps should they take to meet this requirement?

- [ ] A. Create an image of the on-premises virtual machines and upload it to Cloud Storage. Import the image as a virtual disk into Compute Engine.
- [ ] B. Create standard virtual machine instances in Compute Engine. Choose the same Microsoft Windows version (Windows Server 2022) that is currently used on-premises.
- [ ] C.Create an image of the on-premises virtual machine. Import the image as a virtual disk in Compute Engine. Launch a standard Compute Engine instance with the same Windows version selected. Attach a data disk containing content that matches the imported image.
- [x] D. Create an image of the on-premises virtual machine. Import the image into Compute Engine using the flag `--os=windows-2022-byol`. Launch a **sole-tenant VM** in Compute Engine using the imported disk as the boot disk.

### Explanation

**Correct Answer: D.**

**Create an image of the on-premises virtual machine. Import the image into Compute Engine using the flag --os=windows-2022-byol. Launch a sole-tenant VM in Compute Engine using the imported disk as the boot disk.**

✅ **Justification for Correct Option (D):**

To **bring your own Windows Server licenses (BYOL)** to Google Cloud, organizations must follow Google’s **License Mobility** and **sole-tenant node** requirements.

**Key requirements for BYOL with Windows Server on Google Cloud:**

1. **Use Sole-Tenant Nodes**:
  - Microsoft licensing requires that BYOL of Windows Server licenses can only be done on **dedicated hardware**.
  - In Google Cloud, this means using **Sole-Tenant VMs**.
2. **Import the Windows Image Properly**:
  - You must **import the on-prem VM image** using `gcloud compute images import` with the correct `--os` flag (e.g., `--os=windows-2022-byol`).
  - This ensures that the system is recognized as Windows Server 2022 with Data Center edition (for license compliance).
3. **Use the imported image as the boot disk** for your sole-tenant VM instance.

**Documentation Reference:**

- Bringing existing Windows licenses

*"You can bring your own Windows Server licenses to Compute Engine by using sole-tenant nodes and importing your existing Windows Server images."*

- Creating sole-tenant VMs

❌ **Why Other Options Are Incorrect:**

**A. Create an image and import it, then use it as a virtual disk.**

- **Incorrect**, because this does **not specify** launching the VM on **sole-tenant nodes**, which is **mandatory for BYOL** under Microsoft licensing for Windows Server.
- Without sole-tenant VMs, this violates licensing terms.

**B. Create standard Compute Engine VM using the same Windows version.**

- **Incorrect**, because selecting a standard GCP Windows image uses **Google's SPLA-licensed images**, **not your own licenses**.
- This defeats the purpose of **BYOL**.

**C. Create image, import virtual disk, launch standard VM and attach data disk.**

- **Incorrect**, again because it uses **standard Compute Engine instances**, not **sole-tenant nodes**, which is **non-compliant** with BYOL rules.
- Also, attaching a data disk doesn’t help for **boot licensing** concerns.

✅ **Final Answer: D.**

Because **BYOL for Windows Server on Google Cloud** requires:

- Using **sole-tenant nodes** (for Microsoft licensing compliance),
- **Importing your own Windows Server image** properly,
- And **booting** your instance using that image.

**⚠️ Note:** `gcloud compute images import` is deprecated; Google now points to image imports in Migrate to Virtual Machines. The BYOL rule is unchanged: import as a BYOL image and run it on sole-tenant nodes.

---

## Question 9

*Domain 2: Managing and Provisioning a Solution Infrastructure*

You’re deploying an application to Google Cloud for **EdgeBridge Solutions**. This application is part of a distributed system that includes components running outside of Google Cloud. The application deployed in GCP must communicate over a **private network** with external systems running in an on-premises environment.

The expected **average network throughput is 200 kbps**, and the business has the following requirements:

- **99.99% system availability**
- **Cost-effective connectivity**

You need to design the hybrid connectivity between the two environments to meet these requirements.

**What should you implement?**

- [x] A. Deploy an **HA Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.
- [ ] B. Use a **Classic Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.
- [ ] C. Deploy **two HA Cloud VPN gateways**, each connected to separate on-premises VPN gateways. Configure each with two tunnels connecting to different on-prem VPNs.
- [ ] D. Use a **Classic Cloud VPN gateway** with a single tunnel connected to the on-premises VPN gateway.

### Explanation

**Correct Answer: A. Deploy an HA Cloud VPN gateway with two tunnels connected to the on-premises VPN gateway.**

✅ **Justification for Correct Option (A):**

This option best aligns with **EdgeBridge Solutions'** requirements:

- **Target Availability: 99.99%**
- **Low throughput: 200 kbps**
- **Cost-effective hybrid connectivity**
- **Private network communication**

**HA Cloud VPN** is designed to provide:

- **99.99% availability SLA**
- Built-in **redundancy** with **two interfaces and tunnels**
- **Active-active routing** using **Google Cloud Router**
- **Cost-effective pricing**, especially when compared to Dedicated Interconnect

**Why this option is optimal:**

- **Low throughput (200 kbps)** makes **Cloud Interconnect unnecessary** and **too costly**.
- **HA VPN** provides **high availability (99.99%)** and is the officially recommended solution for **VPN-based hybrid connectivity**.
- **Two tunnels on a single HA VPN gateway** give sufficient redundancy and meet **SLA** without unnecessary overengineering.

**Documentation Reference:**

- HA VPN Overview – Google Cloud

*“HA VPN provides an SLA of 99.99% service availability. HA VPN uses two interfaces (each with its own IP address), and each interface supports one tunnel.”*

❌ **Why Other Options Are Incorrect:**

**B. Use a Classic Cloud VPN gateway with two tunnels connected to the on-premises VPN gateway.**

- **Incorrect** because Classic VPN:
  - **Does not offer any SLA**.
  - Is being phased out in favor of HA VPN.
  - Does not integrate as seamlessly with Cloud Router for dynamic routing.

**Reference:**
[https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview#vpn_classic](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview#vpn_classic)

**C. Deploy two HA Cloud VPN gateways, each connected to separate on-premises VPN gateways, with two tunnels each.**

- **Incorrect** because:
  - While this setup can increase redundancy, it is **overkill** for the **low 200 kbps throughput**.
  - It also **increases cost and operational complexity**, going beyond what's needed to meet the **99.99% availability SLA**.

**D. Use a Classic Cloud VPN gateway with a single tunnel connected to the on-premises VPN gateway.**

- **Incorrect**, because:
  - A **single tunnel** is a **single point of failure**, which violates the **99.99% availability** requirement.
  - Classic VPN **does not offer any availability SLA**.

✅ **Final Answer: A. Deploy an HA Cloud VPN gateway with two tunnels connected to the on-premises VPN gateway.**

It meets all the key requirements:

- **High availability (99.99%)**
- **Private connectivity**
- **Low cost**
- **Simple and scalable configuration**

---

## Question 10

*Domain 5: Managing Implementation*

**InfoPulse Corp** is planning to migrate a **10 TB on-premises database export** to **Google Cloud Storage**. The objective is to **minimize both the total transfer time and the overall cost**. The available bandwidth between their on-premises data center and Google Cloud is **1 Gbps**.

You are tasked with selecting a migration approach that aligns with **Google-recommended best practices**.

**What should you do?**

- [ ] A. Create a **Cloud Dataflow** pipeline that directly reads data from the on-premises database and writes it to Cloud Storage.
- [ ] B. Use the **Transfer Appliance** to move the data via an **offline** transfer method.
- [ ] C. Use a third-party **commercial ETL partner** solution to extract and load the data into Cloud Storage.
- [x] D. Transfer the data using the command: `gcloud storage cp [SOURCE] [DESTINATION]`

### Explanation

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

---

## Question 11

*Domain 3: Designing for Security and Compliance*

***"LEGACY AND OPTIONAL"***

**Older case-study questions are included as optional bonus scenarios to strengthen architecture thinking, while the main tests are updated to match the current exam expectations.**

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

Which storage approach is most fitting for implementing a custom card tokenization service for the Helicopter Racing League (HRL) case study, given the demands of low latency, cost-effectiveness, identification of duplicate credit cards, and support for annual key rotation?

- [ ] A. Employ Secret Manager to store card data post-query for duplicate identification.
- [x] B. Utilize Firestore in Datastore mode to encrypt card data using a deterministic algorithm.
- [ ] C. Employ sharding across multiple Memorystore instances to encrypt card data using a deterministic algorithm.
- [ ] D. Use Cloud SQL with column-level encryption to store card data.

### Explanation

**Why B is the Best Choice:**

- **Low Latency:** Firestore/Datastore are NoSQL databases optimized for extremely fast reads and writes, especially for lookups by key, which would be ideal in a tokenization service.
- **Duplicate Identification:** A deterministic algorithm ensures the same card generates the same token, ideal for quick duplication detection.
- **Annual Key Rotation:** While not directly built in, custom logic can be implemented to facilitate key rotation with a deterministic algorithm. You'd essentially:
  1. Generate a new encryption key
  2. Use both old and new keys in parallel for a transition period to decrypt existing tokens
  3. Gradually re-encrypt all tokens with the new key
  4. Retire the old key

**Why Other Options Are Less Suitable:**

- **A. Secret Manager:** Designed for storing secrets, not optimized for the scale of transaction data and its query patterns. Can be expensive for this use case.
- **C. Memorystore (Redis):** Great for speed but primarily an in-memory cache. Its lack of persistence poses a risk to sensitive financial data. Sharding adds complexity.
- **D. Cloud SQL:** While secure, traditional relational databases (like Cloud SQL) often introduce a slight latency overhead compared to NoSQL options specifically tuned for key-value lookups. Column-level encryption adds computational overhead.

**Key Takeaway:** It's important to critically analyze the nuanced requirements of highly sensitive scenarios like credit card tokenization. While Cloud SQL is a robust choice, the specific needs for speed and duplicate detection make Firestore/Datastore better suited in this case.

Reference:

[https://cloud.google.com/community/tutorials/pci-tokenizerhttps://cloud.google.com/architecture/tokenizing-sensitive-cardholder-data-for-pci-dss](https://cloud.google.com/community/tutorials/pci-tokenizer  https://cloud.google.com/architecture/tokenizing-sensitive-cardholder-data-for-pci-dss)

**⚠️ Note:** This is a legacy case-study item. Deterministic encryption is what lets duplicate cards be detected (same card, same token); the storage choice is less clear-cut than the explanation suggests. Google's reference tokenizer design uses Sensitive Data Protection with Cloud KMS-wrapped keys.

---

## Question 12

*Domain 3: Designing for Security and Compliance*

***"LEGACY AND OPTIONAL"***

**Older case-study questions are included as optional bonus scenarios to strengthen architecture thinking, while the main tests are updated to match the current exam expectations.**

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

In the Helicopter Racing League (HRL) case study, with the recent establishment of a new regional racing league in Cape Town, South Africa, HRL has partnered with Fastly, a Content Delivery Network provider, to enhance the user experience. To permit traffic exclusively from all Fastly IP address ranges into their Virtual Private Cloud network (VPC network) through the External HTTP(S) load balancer, which command should you use?

- [ ] A. Update Security Policy 'from-fastly' gcloud compute security-policies rules update 1000 \ --security-policy from-fastly \ --src-ip-ranges * \ --action "allow"
- [ ] B. Update Firewall Rule 'sourceiplist-fastly' gcloud compute firewall rules update sourceiplist-fastly \ --priority 1000 \ --allow tcp:443
- [ ] C. Update Firewall Rule 'hlr-policy' gcloud compute firewall rules update hlr-policy \ --priority 1000 \ --target-tags=sourceiplist-fastly \ --allow tcp:443
- [x] D. Update Security Policy 'hlr-policy' gcloud compute security-policies rules update 1000 \ --security-policy hlr-policy \ --expression "evaluatePreconfiguredExpr('sourceiplist-fastly')" \ --action "allow"

### Explanation

The most suitable command for this scenario is indeed

**D. gcloud compute security-policies rules update 1000 --security-policy hlr-policy --expression "evaluatePreconfiguredExpr('sourceiplist-fastly')" --action "allow"**. Here's a breakdown of why D is the best choice and why the others are not ideal:

**Why D is the Best Choice:**

- **Security Policy Integration:** This command utilizes Cloud Armor security policies, which are designed specifically for managing security at the network layer. This aligns well with the requirement of controlling traffic entering the VPC network.
- **Preconfigured Expression:** The `evaluatePreconfiguredExpr('sourceiplist-fastly')` part leverages a pre-configured list of Fastly's IP addresses, offering a secure and efficient way to reference the allowed source.
- **Granular Control:** Security policies provide granular control over traffic flow, allowing you to define specific conditions (like source IP list) for allowing or denying traffic.

**Why Other Options Are Less Suitable:**

- **A. gcloud compute security-policies rules update... (with src-ip-ranges)** While this command uses security policies, it relies on specifying individual IP ranges. This can become cumbersome and error-prone for a large dynamic list like Fastly's.
- **B. gcloud compute firewall rules update...** Firewall rules offer a lower-level approach compared to security policies. While they can achieve traffic control, security policies provide a more centralized and policy-driven way to manage complex access rules.
- **C. gcloud compute firewall rules update hlr-policy... (with target-tags)** This command seems related to a policy named "hlr-policy" and uses target tags, which might not be directly tied to the Fastly IP list requirement.

Here are some additional points to consider:

- **Security Policy Creation:** This command assumes a security policy named "hlr-policy" already exists. If not, you'd need to create it first using a separate command.
- **Preconfigured List Management:** Ensure the `sourceiplist-fastly` expression refers to an actual, up-to-date list of Fastly's IP addresses. This list might be maintained in a separate service or file.

By leveraging Cloud Armor security policies with pre-configured expressions, option D offers a secure, scalable, and efficient approach to controlling traffic from Fastly's IP addresses into the HRL's VPC network.

Reference:

[https://cloud.google.com/armor/docs/configure-security-policies#create-ruleshttps://cloud.google.com/armor/docs/configure-security-policies#use-console-gcloudhttps://cloud.google.com/armor/docs/integrating-cloud-armor#https-vpc-firewall-rules](https://cloud.google.com/armor/docs/configure-security-policies#create-rules  https://cloud.google.com/armor/docs/configure-security-policies#use-console-gcloud  https://cloud.google.com/armor/docs/integrating-cloud-armor#https-vpc-firewall-rules)

---

## Question 13

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [ ] A. Establish Cloud Tasks and a Cloud Storage bucket that activates a Cloud Function.
- [ ] B. Establish a Cloud Logging sink and a Cloud Storage bucket that activates a Cloud Function.
- [x] C. Configure the deployment job to inform a Pub/Sub queue that activates a Cloud Function.
- [ ] D. Establish Identity and Access Management (IAM) and Confidential Computing to activate a Cloud Function.

### Explanation

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

---

## Question 14

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

In reference to the Helicopter Racing League (HRL) case study, HRL aims to enhance prediction accuracy from their ML prediction models. They request the utilization of Google's AI Platform to facilitate comprehension and interpretation of predictions. What course of action should be taken?

- [x] A. Employ Explainable AI.
- [ ] B. Employ Vision AI.
- [ ] C. Utilize Google Cloud's Operations Suite.
- [ ] D. Utilize Jupyter Notebooks.

### Explanation

The best course of action in this scenario is

**A. Employ Explainable AI.** Here's why:

- **Core Requirement Alignment:** The primary need is to understand *why* ML models make specific predictions. Explainable AI techniques are explicitly designed to address this by providing insights into the features that contribute most to a prediction.
- **Improved Model Trust and Debugging:** Explainable AI can help build trust in the ML models, identify potential biases or problems, and provide avenues for further refinement.

**Why Others Are Less Optimal:**

- **B. Vision AI:** Vision AI focuses on analyzing images and videos. While it could be a tangential component if predictions are based on visual data, it doesn't directly address the need to explain model decisions.
- **C. Google Cloud's Operations Suite:** Operations Suite (formerly Stackdriver) focuses on monitoring, logging, and troubleshooting production systems. While helpful for overall system health, it doesn't provide the model-level explainability needed here.
- **D. Jupyter Notebooks:** These are valuable tools for data scientists and ML model development but, by themselves, don't offer the explainability features required.

**How Explainable AI Could Be Used In the HRL Context:**

- **Feature Importance:** Identify the key data points (e.g., race track conditions, weather, pilot history, etc.) that have the most significant influence on race outcome predictions.
- **Local Explanations:** Understand why a model made a specific prediction for a particular race.
- **Counterfactual Explanations:** Explore "what if" scenarios to see how changes in input data might affect the prediction outcome.

**Note:** Explainable AI is an active area of research. Google's AI Platform provides tools and libraries to help with its implementation: [https://cloud.google.com/explainable-ai](https://cloud.google.com/explainable-ai)

Further Details:

[https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/overview)

---

## Question 15

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

In reference to the Helicopter Racing League (HRL) case study, HRL seeks a cost-effective approach for storing their race data, including telemetry. They aim to retain all historical records, train models solely using the previous season's data, and anticipate data growth in terms of volume and collected information. Given HRL's business requirements and the objectives articulated by CEO S. Hawke, what data solution should be proposed?

- [ ] A. Implement Firestore for its scalable and flexible document-based database. Utilize collections to aggregate race data by season and event.
- [ ] B. Employ Cloud Spanner for its scalability and capability to version schemas seamlessly with zero downtime. Distribute race data using season as a primary key.
- [x] C. Utilize BigQuery for its scalability and ability to incorporate columns into a schema. Partition race data based on season.
- [ ] D. Opt for Cloud SQL for its automatic management of storage expansions and compatibility with MySQL. Utilize separate database instances for each season.

### Explanation

Here's the breakdown of why the best choice for this scenario is

**C. Utilize BigQuery for its scalability and ability to incorporate columns into a schema. Partition race data based on season.**

**Reasons for Choosing BigQuery:**

- **Cost-Effective for Historical Storage:** BigQuery's pricing model is based on the amount of data stored and queried. It's ideal for large datasets (historical records) that are infrequently updated but analyzed in bulk (training on previous season's data).
- **Scalability for Growth:** BigQuery is designed to handle massive datasets, scaling seamlessly to accommodate anticipated growth in the volume and complexity of race data.
- **Schema Evolution:** As new types of telemetry data are collected, BigQuery's flexible schema allows for adding new columns without disrupting existing data, supporting future changes.
- **Season-Based Partitioning:** Partitioning race data by season optimizes query performance, making it efficient to train models only on the relevant past season's data.

**Why Other Options Are Less Optimal:**

- **A. Firestore:** While Firestore is scalable and flexible, its pricing model is usually better suited for high read/write frequency use cases. HRL's data is likely write-once, read-infrequently for training purposes.
- **B. Cloud Spanner:** Cloud Spanner is optimized for transactional workloads and strong consistency. The cost model and complexity make it less suitable for the volume of primarily analytical data in the HRL scenario.
- **D. Cloud SQL:** Cloud SQL is a great option for traditional relational database needs, but BigQuery's columnar storage, pricing model, and scaling advantages make it better for this specific data scenario.

**Key Points for HRL:**

- **Query Optimization:** Using partitioning and appropriate querying techniques will be critical for efficiently analyzing large amounts of data in BigQuery.
- **Storage Classes:** Explore BigQuery's long-term storage options to reduce costs for older data not immediately needed for model training.

References:

[https://cloud.google.com/blog/products/gcp/architecting-live-ncaa-predictions-from-archives-to-insights](https://cloud.google.com/blog/products/gcp/architecting-live-ncaa-predictions-from-archives-to-insights)

---

## Question 16

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [ ] A. Access each Compute Engine instance individually and gather disk, CPU, memory, and network usage statistics for analysis.
- [ ] B. Utilize the gcloud compute instances list command to identify the virtual machine instances labeled with idle: true.
- [x] C. Employ the gcloud recommender command to generate a list of idle virtual machine instances.
- [ ] D. Through the Google Console, pinpoint which Compute Engine instances within the managed instance groups are no longer responsive to health check probes.

### Explanation

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

---

## Question 17

*Domain 3: Designing for Security and Compliance*

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

In reference to the EHR Healthcare case study, you are tasked with ensuring that EHR's utilization of Google Cloud will satisfy an upcoming privacy compliance audit. What actions should be taken? (Select two.)

- [x] A. Validate EHR's product usage against the list of compliant products on the Google Cloud compliance page.
- [x] B. Recommend that EHR enters into a Business Associate Agreement (BAA) with Google Cloud.
- [ ] C. Employ Firebase Authentication for EHR's user-facing applications.
- [ ] D. Deploy Prometheus to detect and prevent security breaches on EHR's web-based applications.
- [ ] E. Utilize GKE private clusters for all Kubernetes workloads.

### Explanation

The two best actions to ensure EHR's compliance with an upcoming privacy audit are:

- **A. Validate EHR's product usage against the list of compliant products on the Google Cloud compliance page.**
  - It's essential to make sure the Google Cloud services being used by EHR are specifically covered under compliance frameworks relevant to the healthcare industry (likely HIPAA in the US).
- **B. Recommend that EHR enters into a Business Associate Agreement (BAA) with Google Cloud.**
  - A BAA clarifies the responsibilities of both Google Cloud and EHR regarding the handling of protected health information (PHI) and establishes safeguards for PHI in compliance with regulations.

**Let's analyze why the other options aren't the top priorities for compliance:**

- **C. Employ Firebase Authentication for EHR's user-facing applications.**
  - Authentication is a security component, but it doesn't directly address privacy compliance. It's indirectly important though, as strong authentication is part of HIPAA requirements.
- **D. Deploy Prometheus to detect and prevent security breaches on EHR's web-based applications.**
  - This is focused on security monitoring and proactive threat detection, which is a valuable piece of the security puzzle but not the primary focus for a privacy compliance audit.
- **E. Utilize GKE private clusters for all Kubernetes workloads.**
  - GKE private clusters enhance security, but they are not sufficient in themselves to fulfill all the requirements of a privacy compliance audit.

**Important Notes:**

- **Regulations:** The specific compliance requirements will depend on EHR's location and the regulatory framework they adhere to (HIPAA, HITECH, GDPR, etc.).
- **Comprehensive Approach:** A successful compliance audit involves a wide range of factors, including:
  - Encryption of data at rest and in transit
  - Access controls and identity management
  - Logging and audit trails
  - Incident response procedures
  - Employee training on privacy regulations.

References:

[https://cloud.google.com/security/compliance/offerings?skip_cache=true#/regions=USA&industries=Healthcare_and_life_sciences&focusArea=Privacy)https://cloud.google.com/security/compliance/hipaahttps://cloud.google.com/security/compliance/hipaa#customer_responsibilities](https://cloud.google.com/security/compliance/offerings?skip_cache=true#/regions=USA&industries=Healthcare_and_life_sciences&focusArea=Privacy)  https://cloud.google.com/security/compliance/hipaa  https://cloud.google.com/security/compliance/hipaa#customer_responsibilities)

---

## Question 18

*Domain 3: Designing for Security and Compliance*

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

**What steps should you take to establish a secure technical architecture for deploying workloads to Google Cloud in accordance with the EHR Healthcare case study? Select two options.**

- [x] A. Enable Binary Authorization on GKE, and sign containers as part of a CI/CD pipeline.
- [ ] B. Configure Jenkins to leverage Kritis for cryptographic container signing within a CI/CD pipeline.
- [ ] C. Configure Container Registry to exclusively permit trusted service accounts to create and deploy containers from the registry.
- [x] D. Configure Container Registry to employ vulnerability scanning to verify the absence of vulnerabilities prior to workload deployment.

### Explanation

The two best steps to establish a secure architecture in the EHR Healthcare case study are:

- **A. Enable Binary Authorization on GKE, and sign containers as part of a CI/CD pipeline.**
  - Binary Authorization ensures that only trusted and verified containers can be deployed into your Kubernetes environment.
  - Integrating container signing into the CI/CD pipeline creates a chain of trust that guarantees the integrity and origin of the images being deployed.
- **D. Configure Container Registry to employ vulnerability scanning to verify the absence of vulnerabilities prior to workload deployment.**
  - Vulnerability scanning adds a crucial layer of security by proactively identifying known vulnerabilities in container images.
  - Preventing the deployment of images containing high-severity vulnerabilities significantly reduces the attack surface of your applications.

**Why the other options are less ideal for this specific focus:**

- **B. Configure Jenkins to leverage Kritis for cryptographic container signing...** While Kritis is a valid tool for container signing, this option is more tool-specific. The core principles of container signing and integrating it into the CI/CD pipeline are the key security measures, regardless of the specific tooling.
- **C. Configure Container Registry to exclusively permit trusted service accounts...** This is a good security practice. However, it primarily addresses authorization, while the focus here is more on image integrity and vulnerability prevention.

**Important Considerations:**

- **Defense in Depth:** Remember, security is a multi-layered approach. These steps are crucial but need to be combined with:
  - Strong network security (firewalls, VPC configurations)
  - Identity and Access Management (IAM) best practices
  - Monitoring and logging

References:

[https://cloud.google.com/binary-authorization/docs/overviewhttps://cloud.google.com/docs/ci-cd/overview?hl=en&skip_cache=true](https://cloud.google.com/binary-authorization/docs/overview  https://cloud.google.com/docs/ci-cd/overview?hl=en&skip_cache=true)

**⚠️ Note:** Container Registry has been shut down; its replacement is Artifact Registry with Artifact Analysis for vulnerability scanning.

---

## Question 19

*Domain 2: Managing and Provisioning a Solution Infrastructure*

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

**To upgrade the EHR connection in compliance with their requirements, ensuring support for business-critical needs and adherence to existing network and security policies, what action should you take?**

- [x] A. Integrate a new Dedicated Interconnect connection.
- [ ] B. Enhance the bandwidth on the existing Dedicated Interconnect connection to 100 G.
- [ ] C. Implement three new Cloud VPN connections.
- [ ] D. Integrate a new Carrier Peering connection.

### Explanation

**Dedicated Interconnect (Option A) is the Best Choice:**

- **Security and Reliability:** EHR data is highly sensitive and often subject to strict compliance regulations (such as HIPAA). Dedicated Interconnect offers a direct, private connection to Google Cloud, bypassing the public internet. This greatly reduces vulnerability to interception or disruption, making it highly suitable for healthcare data.
- **Performance:** Dedicated Interconnect provides low-latency, high-bandwidth connections, essential for transferring potentially large EHR data sets (patient records, imaging studies, etc.). This ensures smooth access to critical information for healthcare providers.
- **Scalability:** Dedicated Interconnect offers capacities up to 100 Gbps and can be easily scaled up as data volumes grow, aligning with the anticipated increase in EHR usage.

**Feedback on Other Options:**

- **B. Enhance the bandwidth on the existing Dedicated Interconnect connection to 100 G:** This is also a strong contender, *if* the existing interconnect meets security policies and the primary limitation is bandwidth. It's simpler and likely quicker to implement than establishing a new connection.
- **C. Implement three new Cloud VPN connections:** Cloud VPNs can be viable for less stringent security requirements or as a temporary/backup solution. However, they introduce potential latency, performance bottlenecks, and are generally less reliable than a dedicated line due to reliance on the public internet.
- **D. Integrate a new Carrier Peering connection:** Carrier Peering is often geared towards improving general internet traffic performance and reducing costs. While it can benefit some cloud services, it's less tailored to the specific security and reliability needs of EHR data.

References:

[https://cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-interconnectshttps://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overviewhttps://cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-interconnects](https://cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-interconnects  https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview  https://cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-interconnects)

---

## Question 20

*Domain 2: Managing and Provisioning a Solution Infrastructure*

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

**Considering the EHR Healthcare business and technical requirements, how should you define the technical architecture for hybrid connectivity between EHR's on-premises systems and Google Cloud, following Google's recommended practices for production-level applications?**

- [ ] A. Configure two Partner Interconnect connections in one metro (City), ensuring placement in different metro zones.
- [ ] B. Set up two VPN connections from on-premises to Google Cloud, ensuring that the VPN devices on-premises are in separate racks.
- [ ] C. Establish Direct Peering between EHR Healthcare and Google Cloud, ensuring peering at least two Google locations.
- [x] D. Configure two Dedicated Interconnect connections in one metro (City) and two connections in another metro, ensuring placement in different metro zones.

### Explanation

The best option of the four is

**D. Configure two Dedicated Interconnect connections in one metro (City) and two connections in another metro, ensuring placement in different metro zones.**

Here's why this solution stands out, and how it aligns with Google's best practices for hybrid connectivity in the context of EHR systems:

**Why Option D is Ideal**

- **High Availability and Redundancy:** Two Dedicated Interconnects in each metro provide redundancy at the connection level. Placing them in different metro zones offers additional protection from potential infrastructure failures within a specific zone. This is critical for EHR systems, where downtime can directly impact patient care.
- **Security:** Dedicated Interconnect provides the highest level of security compared to VPNs or peering, thanks to its private, physical connection to Google Cloud. This is essential for protecting sensitive EHR data.
- **Performance:** Dedicated Interconnect offers low latency and high bandwidth, ideal for the demands of transferring potentially large EHR datasets.
- **Scalability:** Dedicated Interconnect is easily scalable for future growth as EHR data volumes increase.
- **Google Best Practices:** This architecture aligns with Google's focus on redundancy and reliability for production-level hybrid cloud environments.

**Considerations Regarding Other Options**

- **A. Configure two Partner Interconnect connections in one metro (City), ensuring placement in different metro zones:** Partner Interconnect offers similar benefits to Dedicated Interconnect but relies on a third-party service provider. This adds a potential point of complexity.
- **B. Set up two VPN connections from on-premises to Google Cloud, ensuring that the VPN devices on-premises are in separate racks:** VPNs are more cost-effective than dedicated connections but may introduce significant latency, performance issues, and less inherent security for the sensitive nature of EHR data.
- **C. Establish Direct Peering between EHR Healthcare and Google Cloud, ensuring peering at least two Google locations:** Direct Peering is primarily for optimizing public internet performance and reducing costs. It's suitable for general web services but might not be the ideal choice for the mission-critical security and reliability needs of EHR data.

**Important Additions to a Complete Architecture:**

A truly robust hybrid architecture for EHR systems should also include:

- **Security:** Firewalls, intrusion detection/prevention, data encryption (both at rest and in transit), and strong access controls are essential.
- **Monitoring and Logging:** Implement systems to monitor the health and performance of the connections, along with rigorous logging for auditing and troubleshooting.
- **Disaster Recovery:** Establish clear procedures and mechanisms for handling outages and recovering EHR data swiftly to minimize disruption.

References:

[https://cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#scenarioshttps://cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#scenarios  https://cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview)

---

## Question 21

*Domain 5: Managing Implementation*

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

- [ ] A. Adjust the Pub/Sub Total Timeout retry value.
- [ ] B. Transition from a Pub/Sub subscriber pull model to a push model.
- [x] C. Disable Pub/Sub message batching.
- [ ] D. Establish a backup Pub/Sub message queue.

### Explanation

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

---

## Question 22

*Domain 3: Designing for Security and Compliance*

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

**In the context of the EHR Healthcare case study, to prevent the recurrence of configuration errors where public IP addresses were mistakenly assigned to backend servers, and to ensure that external IP addresses are only configured on frontend Compute Engine instances, what action should you take?**

- [x] A. Implement an Organizational Policy with a constraint allowing external IP addresses solely on the frontend Compute Engine instances.
- [ ] B. Remove the compute.networkAdmin role from all users in the project associated with frontend instances.
- [ ] C. Set up an Identity and Access Management (IAM) policy assigning the IT staff to the compute.networkAdmin role for the organization.
- [ ] D. Create a custom Identity and Access Management (IAM) role named GCE_FRONTEND with the compute.addresses.create permission.

### Explanation

Here's why Option A (Implement an Organizational Policy with a constraint allowing external IP addresses solely on the frontend Compute Engine instances) is the best approach for the EHR Healthcare use case:

**Why Organizational Policy is Ideal**

- **Targeted Solution:** Organizational Policies are designed specifically for enforcing configuration rules across your Google Cloud environment. This aligns perfectly with the goal of preventing public IP assignment on backend servers.
- **Granularity:** You can customize the policy to explicitly deny external IP addresses for Compute Engine instances that are labeled as "backend" or with any other identifier you choose.
- **Centralized Control:** The policy applies at the organization (or sub-folder) level, providing a single point of enforcement. This makes it easier to manage and ensures consistency.
- **Automation and Scalability:** Once the policy is in place, it automatically prevents misconfigurations as your infrastructure grows. You won't need to make manual permission changes for each new backend instance.

**Considerations about the Other Options**

- **B. Remove the compute.networkAdmin role from all users in the project associated with frontend instances.** This is too broad. It might prevent the unwanted configuration but would also hinder legitimate tasks related to frontend instances.
- **C. Set up an Identity and Access Management (IAM) policy assigning the IT staff to the compute.networkAdmin role for the organization.** This lacks the specificity needed. It grants organization-wide network permissions, increasing the risk of misconfigurations in other areas.
- **D. Create a custom Identity and Access Management (IAM) role named GCE_FRONTEND with the compute.addresses.create permission.** Custom IAM roles are great but better suited for fine-grained permissions beyond what Organizational Policies offer. They are harder to manage at scale for broad configuration rules.

**Best Practice**

A robust approach combines Organizational Policies and custom IAM roles:

1. **Organizational Policy:** Enforce the broad "no external IPs on backend servers" rule.
2. **Custom IAM Role:** Create a role with restricted permissions for managing frontend instances, including the ability to create external IP addresses.

**Additional Notes:**

- **Documentation:** Refer to Google's documentation on creating Organizational Policies for specific instructions and examples.
- **Labels and Tagging:** Use meaningful labels or tags to identify backend servers and streamline policy application.

References:

[https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternaliphttps://cloud.google.com/blog/ja/products/identity-security/limiting-public-ips-google-cloud](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternalip  https://cloud.google.com/blog/ja/products/identity-security/limiting-public-ips-google-cloud)

---

## Question 23

*Domain 3: Designing for Security and Compliance*

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

**In designing the Google Cloud network architecture for Google Kubernetes Engine within the EHR Healthcare context and adhering to Google best practices, what action should you take to minimize the attack surface?**

- [x] A. Deploy a private cluster with a private endpoint, configured with master authorized networks.
- [ ] B. Implement a public cluster with firewall rules and Virtual Private Cloud (VPC) routes.
- [ ] C. Utilize a private cluster with a public endpoint, configured with master authorized networks.
- [ ] D. Opt for a public cluster with enabled master authorized networks and firewall rules.

### Explanation

The best option for minimizing the attack surface in the EHR Healthcare context is

**A. Deploy a private cluster with a private endpoint, configured with master authorized networks.**

Let's break down why this is the most secure approach and how it adheres to Google's best practices:

**Why Choose a Private Cluster**

- **Reduced Exposure:** Private GKE clusters don't have public IP addresses assigned to their control plane nodes. This significantly limits external access, reducing the attack surface.
- **Controlled Access:** You can fine-tune access to the control plane from specific, trusted IP ranges using master authorized networks. This is vital in a healthcare environment where sensitive data is involved.
- **Private Endpoint:** Enables you to connect to the cluster's control plane from your on-premises network via Google Cloud's private network infrastructure, further enhancing security.

**Why Other Options Are Less Secure**

- **B. Implement a public cluster with firewall rules and Virtual Private Cloud (VPC) routes.** While firewall rules and VPC routes add security, they don't fundamentally isolate the cluster control plane like a private cluster does.
- **C. Utilize a private cluster with a public endpoint, configured with master authorized networks.** Even with master authorized networks, this option still leaves the control plane partially exposed on the public internet, increasing the risk of targeted attacks.
- **D. Opt for a public cluster with enabled master authorized networks and firewall rules.** This has the highest level of exposure and presents the most significant risk from a security standpoint.

**Google Best Practices Alignment:**

Google strongly recommends deploying private GKE clusters for maximum security, especially when handling sensitive data like EHR Healthcare.

**Important Considerations:**

- **Network Connectivity:** If you choose a private cluster, ensure your on-premises network has a secure connection to Google Cloud, such as Cloud VPN or Cloud Interconnect.
- **Management:** Manage access to the private cluster rigorously. Use strong authentication and authorization mechanisms.

References:

[https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept](https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept)

---

## Question 24

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [x] A. Tests should scale well beyond the prior approaches.
- [ ] B. Unit tests are no longer necessary; only end-to-end tests.
- [ ] C. Tests should be implemented after the release is deployed in the production environment.
- [ ] D. Tests should involve directly assessing the Google Cloud Platform (GCP) infrastructure.

### Explanation

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

---

## Question 25

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [x] A. Develop a scalable environment within GCP to emulate production load.
- [ ] B. Utilize the existing infrastructure to test the GCP-based backend at scale.
- [ ] C. Incorporate stress tests into each component of the application, utilizing internal GCP resources to simulate load.
- [ ] D. Establish a set of static environments within GCP to test various load levels, such as high, medium, and low.

### Explanation

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

---

## Question 26

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**Mountkirk Games intends to establish a continuous delivery pipeline for their architecture, which comprises numerous small services requiring quick updates and rollbacks. The company has specific requirements:**

- Services must be redundantly deployed across multiple regions in the US and Europe.
- Only frontend services are publicly accessible on the internet.
- A single frontend IP address should be provided for their service fleet.
- Deployment artifacts must be immutable.

**Which set of products should they use to meet these requirements?**

- [ ] A. Google Cloud Storage, Google Cloud Dataflow, Google Compute Engine
- [ ] B. Google Cloud Storage, Google App Engine, Google Network Load Balancer
- [x] C. Google Kubernetes Registry, Google Kubernetes Engine, Google HTTP(S) Load Balancer
- [ ] D. Google Cloud Functions, Google Cloud Pub/Sub, Google Cloud Deployment Manager

### Explanation

The best choice for Mountkirk Games is

**C. Google Kubernetes Registry, Google Kubernetes Engine, Google HTTP(S) Load Balancer**. Here's a breakdown of why this combination aligns with their requirements and why other options are less suitable:

**Why Option C is Ideal**

- **Containerization and Microservices:** Google Kubernetes Engine (GKE) is designed for managing containerized applications, making it perfect for Mountkirk Games' architecture of small services. Google Kubernetes Registry provides secure, private storage for their container images.
- **Multi-Region Redundancy:** GKE supports multi-regional clusters for high availability. This fulfills the requirement for redundant deployment across the US and Europe.
- **Single Frontend IP:** Google HTTP(S) Load Balancer offers a single, global IP address for their frontend services while intelligently distributing traffic across multiple regions.
- **Immutable Artifacts:** Container images are inherently immutable, ensuring consistent deployment artifacts and easy rollbacks if needed.

**Why Other Options Don't Fit As Well**

- **A. Google Cloud Storage, Google Cloud Dataflow, Google Compute Engine**
  - Cloud Storage is purely for object storage.
  - Dataflow is focused on data processing pipelines.
  - While Compute Engine can run containers, the management overhead for small, frequently updated services would be higher than GKE's purpose-built solution.
- **B. Google Cloud Storage, Google App Engine, Google Network Load Balancer**
  - App Engine is better suited to monolithic or less-scalable applications, not as ideal for many small services.
  - Network Load Balancer lacks the advanced traffic management features of HTTP(S) Load Balancer for multi-region distribution.
- **D. Google Cloud Functions, Google Cloud Pub/Sub, Google Cloud Deployment Manager**
  - Cloud Functions is great for event-driven or serverless workloads, but not for consistently running frontend services.
  - Pub/Sub is a messaging service not focused on service deployment.
  - Deployment Manager is for infrastructure automation, but lacks GKE's container-specific deployment and traffic management capabilities.

**⚠️ Note:** "Google Kubernetes Registry" means Container Registry, which has been replaced by **Artifact Registry**.

---

## Question 27

*Domain 6: Ensuring Solution and Operations Excellence*

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

- [ ] A. Confirm the availability of the database.
- [x] B. Ensure that the project quota hasn't been surpassed.
- [ ] C. Validate that the new feature code hasn't introduced any performance bugs.
- [ ] D. Verify that the load-testing team isn't running their tool against production.

### Explanation

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

---

## Question 28

*Domain 3: Designing for Security and Compliance*

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

**Mountkirk Games aims to establish a repeatable and configurable method for deploying isolated application environments, where developers and testers can access each other's environments and resources, but cannot access staging or production resources. The staging environment requires access to certain services from production. How should you isolate development environments from staging and production?**

- [ ] A. Create a project for development and testing and another for staging and production.
- [ ] B. Establish a network for development and testing and another for staging and production.
- [ ] C. Set up one subnetwork for development and another for staging and production.
- [x] D. Create one project for development, a second for staging, and a third for production.

### Explanation

**D. Create one project for development, a second for staging, and a third for production.**

**Why Project-Level Separation is Ideal**

- **Strongest Isolation:** Projects are the top-level isolation boundary in Google Cloud. Separating development, staging, and production into distinct projects provides the most robust separation of resources, permissions, and configurations – a key security principle.
- **Resource Scope:** Each project has its own quotas, IAM policies, and networks. This prevents misconfigurations in development or testing from accidentally impacting staging or production.
- **Ease of Access Control:** IAM (Identity and Access Management) permissions can be applied separately to each project, allowing controlled developer and tester access in dev/testing projects while strictly limiting access to the production project.

**Considerations for Network Connectivity (for Staging)**

Since staging needs access to select production services, consider either:

- **VPC Peering:** Connect the staging project's VPC network to specific networks in the production project, allowing controlled traffic flow with granular firewall rules.
- **Shared VPC:** Place specific production services in a Shared VPC network that both the staging and production project can connect to.

**Why Other Options Are Less Effective:**

- **A. Create a project for development and testing and another for staging and production.** While this offers some separation, it's not as strong as isolating each environment with a separate project.
- **B. Establish a network for development and testing and another for staging and production.** Networks provide isolation but primarily focus on network communication, not permissions and resource ownership like projects do.
- **C. Set up one subnetwork for development and another for staging and production.** Subnetworks are a network-level segmentation, weaker than the full isolation offered by separate projects.

References:

[https://cloud.google.com/appengine/docs/standard/php/creating-separate-dev-environmentshttps://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy](https://cloud.google.com/appengine/docs/standard/php/creating-separate-dev-environments  https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

---

## Question 29

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**Mountkirk Games intends to establish a real-time analytics platform for their latest game, ensuring it meets their technical requirements. Which combination of Google technologies will satisfy all of their requirements?**

- [ ] A. Kubernetes Engine, Cloud Pub/Sub, and Cloud SQL
- [x] B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery
- [ ] C. Cloud SQL, Cloud Storage, Cloud Pub/Sub, and Cloud Dataflow
- [ ] D. Cloud Dataproc, Cloud Pub/Sub, Cloud SQL, and Cloud Dataflow
- [ ] E. Cloud Pub/Sub, Compute Engine, Cloud Storage, and Cloud Dataproc

### Explanation

The best combination of Google technologies for Mountkirk Games' real-time analytics platform is

**B. Cloud Dataflow, Cloud Storage, Cloud Pub/Sub, and BigQuery.**

Here's why this combination closely aligns with their requirements:

- **Real-time Event Ingestion:** Cloud Pub/Sub is a scalable, globally-distributed messaging service ideal for receiving high volumes of game event data in real-time.
- **Stream Processing:** Cloud Dataflow provides a fully-managed service for building, executing, and monitoring complex streaming data pipelines, enabling real-time analysis and transformation of in-flight data.
- **Storage:** Cloud Storage offers durable, highly available storage for raw event data (for replay or historical analysis) and potentially intermediate results from data processing.
- **Analytics:** BigQuery is a serverless, petabyte-scale data warehouse designed for lightning-fast analytics, empowering interactive exploration of real-time data and historical trends.

**Why Other Options Are Less Suitable:**

- **A. Kubernetes Engine, Cloud Pub/Sub, and Cloud SQL:**
  - Kubernetes Engine is primarily for container orchestration. While it could be part of the architecture, it doesn't directly address the need for stream processing or analytics.
  - Cloud SQL is for relational databases, not as well-suited for high-volume, real-time analytics.
- **C. Cloud SQL, Cloud Storage, Cloud Pub/Sub, and Cloud Dataflow:** Same limitations as option A with Cloud SQL.
- **D. Cloud Dataproc, Cloud Pub/Sub, Cloud SQL, and Cloud Dataflow:**
  - Cloud Dataproc is focused on Hadoop and Spark clusters, which might be overkill if the primary need is real-time analytics, rather than large-scale batch processing.
- **E. Cloud Pub/Sub, Compute Engine, Cloud Storage, and Cloud Dataproc:**
  - Using Compute Engine requires more management overhead than using Cloud Dataflow for stream processing.

---

## Question 30

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**In the context of the Mountkirk Games case study, which two steps should be included in their migration plan to transition to a model on Google Cloud Platform that aligns with their technical requirements? (Choose two.)**

- [x] A. Evaluate the impact of migrating their current batch ETL code to Cloud Dataflow.
- [x] B. Develop a schema migration plan to denormalize data for improved performance in BigQuery.
- [ ] C. Design an architecture diagram illustrating the transition from a single MySQL database to a MySQL cluster.
- [ ] D. Transfer 10 TB of analytics data from a previous game into a Cloud SQL instance and execute test queries against the full dataset to ensure successful completion.
- [ ] E. Implement Cloud Armor to safeguard against potential SQL injection attacks in analytics files uploaded to Cloud Storage.

### Explanation

Here's the breakdown of why options A and B are the best steps to include in Mountkirk Games' migration plan and why the others aren't as crucial:

**A. Evaluate the impact of migrating their current batch ETL code to Cloud Dataflow.**

- **Focus on Real-Time:** A key requirement is moving to real-time analytics. Cloud Dataflow's strength is stream processing, making it vital to assess the feasibility and impact of adapting existing batch ETL processes to a real-time model.

**B. Develop a schema migration plan to denormalize data for improved performance in BigQuery.**

- **BigQuery Optimization:** BigQuery excels with denormalized data structures. Proactively planning this migration ensures they leverage BigQuery's performance advantages from the start.

**Why Other Options Are Less Critical**

- **C. Design an architecture diagram illustrating the transition from a single MySQL database to a MySQL cluster.** While clustering might be beneficial, it's not directly tied to their core requirement of real-time analytics. Real-time capabilities likely involve new components, not just MySQL optimization.
- **D. Transfer 10 TB of analytics data from a previous game into a Cloud SQL instance and execute test queries against the full dataset to ensure successful completion.** This focuses on legacy data in Cloud SQL, less relevant for the new real-time platform. It could be a later phase of migration, but not a priority for the initial transition.
- **E. Implement Cloud Armor to safeguard against potential SQL injection attacks in analytics files uploaded to Cloud Storage.** Security is vital, but this protects less relevant static files. Immediate focus should be on securing the real-time data ingestion and processing pipeline.

**Important Note:** The best answers depend on the specific technical requirements mentioned in the full Mountkirk Games case study. If the requirements include aspects like data retention, security of historical data, or MySQL cluster integration, then options C, D, and E might become more important.

References:

[https://cloud.google.com/bigquery/docs/loading-data#loading_denormalized_nested_and_repeated_datahttps://cloud.google.com/solutions/bigquery-data-warehouse#managing_data](https://cloud.google.com/bigquery/docs/loading-data#loading_denormalized_nested_and_repeated_data  https://cloud.google.com/solutions/bigquery-data-warehouse#managing_data)

---

## Question 31

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**Considering the business and technical requirements of Mountkirk Games, what approach should you take to analyze and define the technical architecture for the compute workloads?**

- [ ] A. Implement network load balancers and utilize preemptible Compute Engine instances.
- [ ] B. Implement network load balancers and utilize non-preemptible Compute Engine instances.
- [ ] C. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing preemptible Compute Engine instances.
- [x] D. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing non-preemptible Compute Engine instances.

### Explanation

**Option D (Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing non-preemptible Compute Engine instances)**

as the best approach. Here's a deeper explanation of why:

**Why Option D Excels**

- **Global Availability and Low Latency:** Mountkirk Games likely has a global user base. A global load balancer ensures users are routed to the closest available region, minimizing latency and improving their experience.
- **Reliability and Uptime:** Non-preemptible Compute Engine instances guarantee availability, crucial for core game-related workloads where any disruption directly impacts players.
- **Scalability for Peak Demand:** Managed instance groups with autoscaling dynamically adjust the number of instances based on traffic, ensuring the system can handle sudden spikes in player activity.
- **High-Performance Architecture:** This combination of technologies is geared towards delivering a robust, reliable, and performant platform essential for supporting a popular online game.

**Why Other Options Fall Short:**

- **A. Implement network load balancers and utilize preemptible Compute Engine instances.** While cost-effective, preemptible instances are susceptible to interruption. This isn't ideal for core game workloads requiring high availability.
- **B. Implement network load balancers and utilize non-preemptible Compute Engine instances.** This lacks the global reach of a global load balancer, potentially affecting user experience in geographically distant regions.
- **C. Deploy a global load balancer with managed instance groups and autoscaling policies, utilizing preemptible Compute Engine instances.** The risk of preemption for core workloads outweighs the cost savings for this specific case.

**Important Considerations:**

- **Cost vs. Reliability Balance:** While Option D is the most reliable, it's also potentially the most expensive. A hybrid approach using a mix of non-preemptible and preemptible instances could be explored for specific background or less critical workloads.
- **Workload Analysis:** Carefully analyze which aspects of Mountkirk Games' compute workloads are truly disruption-sensitive and require non-preemptible instances.

**Key Takeaway:** Prioritizing reliability and global performance for mission-critical, user-facing game services makes Option D the best choice as a foundation. Strategic use of preemptible instances could still be incorporated for cost optimization where possible.

References:

[https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2](https://cloud.google.com/certification/guides/cloud-architect/casestudy-mountkirkgames-rev2)

---

## Question 32

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**Considering the Mountkirk Games case study, which two steps should they take to design their solution for the future and leverage cloud and technology improvements as they become available? (Choose two.)**

- [x] A. Store as much analytics and game activity data as financially feasible today to utilize for training machine learning models to predict user behavior in the future.
- [x] B. Begin packaging their game backend artifacts in container images and deploying them on Google Kubernetes Engine to enhance scalability based on game activity.
- [ ] C. Establish a CI/CD pipeline using Jenkins and Spinnaker to automate canary deployments and enhance development velocity.
- [ ] D. Implement a schema versioning tool to minimize downtime when introducing new game features that require storing additional player data in the database.
- [ ] E. Implement a weekly rolling maintenance process for the Linux virtual machines to apply critical kernel patches and package updates, mitigating the risk of 0-day vulnerabilities.

### Explanation

The best two steps Mountkirk Games should take to future-proof their solution are:

- **A. Store as much analytics and game activity data as financially feasible today to utilize for training machine learning models to predict user behavior in the future.** Gathering large amounts of data lays the foundation for future machine learning initiatives, which could drive significant improvements in player engagement and personalization.
- **B. Begin packaging their game backend artifacts in container images and deploying them on Google Kubernetes Engine to enhance scalability based on game activity.** Adopting containers and Kubernetes positions them to embrace modern, scalable architectures. This allows them to respond to dynamic player demand more effectively.

Let's analyze why these options take priority and where others fall slightly short:

**Why the Other Options Are Less Ideal**

- **C. Establish a CI/CD pipeline using Jenkins and Spinnaker to automate canary deployments and enhance development velocity.** While CI/CD is essential, it addresses a different kind of "future-proofing" related to development practices. Options A and B relate more to positioning them to leverage future advancements in data analytics and scalable architecture.
- **D. Implement a schema versioning tool to minimize downtime when introducing new game features that require storing additional player data in the database.** This is good practice but focuses on a narrower aspect of future development flexibility, not as broadly impactful as data collection for ML or scalable architecture foundations.
- **E. Implement a weekly rolling maintenance process for the Linux virtual machines to apply critical kernel patches and package updates, mitigating the risk of 0-day vulnerabilities.** Security is vital, but this is more about ongoing operational maintenance, not directly positioning them to better leverage future cloud technologies or capabilities.

**Important Considerations:**

- **Cost-Benefit of Data Storage:** Balance data collection's value with the storage costs on Google Cloud. Define clear use cases for that data to justify the investment.
- **Learning Curve:** Adopting containers and Kubernetes often has a learning curve. Plan for skill development and potentially external assistance with the transition.

---

## Question 33

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [x] A. Implement failure injection software within the game analytics platform to introduce additional latency to mobile client analytics traffic.
- [ ] B. Develop a test client capable of running from a mobile phone emulator on a Compute Engine virtual machine, running multiple instances across various Google Cloud Platform regions globally to simulate realistic traffic.
- [ ] C. Incorporate the capability to introduce a random delay before processing analytics files uploaded from mobile devices.
- [ ] D. Launch an opt-in beta version of the game on players' mobile devices, gathering response times from analytics endpoints hosted in Google Cloud Platform regions worldwide.

### Explanation

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

---

## Question 34

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**Considering the business and technical requirements of Mountkirk Games, how should you analyze and define the technical architecture for the database workloads?**

- [ ] A. Utilize Cloud SQL for time series data and employ Cloud Bigtable for historical data queries.
- [ ] B. Transition to Cloud SQL to replace MySQL and implement Cloud Spanner for historical data queries.
- [ ] C. Replace MySQL with Cloud Bigtable and utilize BigQuery for historical data queries.
- [x] D. Implement Cloud Bigtable for time series data, utilize Cloud Spanner for transactional data, and employ BigQuery for historical data queries.

### Explanation

The best option here is likely

**D. Implement Cloud Bigtable for time series data, utilize Cloud Spanner for transactional data, and employ BigQuery for historical data queries.** Let's break down why this combination aligns with Mountkirk Games' requirements and potential use cases:

**Why Option D Excels:**

- **Specialized Databases:** This architecture leverages the strengths of each Google Cloud database service to match specific workload types:
  - **Cloud Bigtable:** Ideal for high-volume time-series data typical of game analytics (player actions, metrics, etc.). It offers low latency and high throughput for real-time ingestion and analysis.
  - **Cloud Spanner:** A strongly consistent, distributed relational database well-suited for transactional data that requires ACID properties (like in-game purchases, player profiles, etc.).
  - **BigQuery:** A powerful data warehouse designed for fast analytical queries on massive datasets. It can aggregate and analyze historical data for insights, trends, and reporting.
- **Scalability:** Google Cloud databases are designed to seamlessly scale to meet the demands of a popular game.
- **Future-Proofing:** This architecture aligns with modern, cloud-native architecture patterns and allows Mountkirk Games to leverage the latest database technologies.

**Why Other Options Are Less Ideal:**

- **A. Utilize Cloud SQL for time series data and employ Cloud Bigtable for historical data queries.** Cloud SQL (MySQL-compatible) is less performant for high-volume, fast writes typical of time series data. Cloud Bigtable is a better fit for that workload.
- **B. Transition to Cloud SQL to replace MySQL and implement Cloud Spanner for historical data queries.** While this improves scalability and consistency compared to standalone MySQL, it misses the opportunity to leverage the power of BigQuery for historical analytics workloads.
- **C. Replace MySQL with Cloud Bigtable and utilize BigQuery for historical data queries.** This could work for some scenarios, but Cloud Bigtable is less suited for transactional data that requires strong consistency. Cloud Spanner is a better choice for that use case.

**Important Considerations**

- **Migration Complexity:** Transitioning to multiple databases will require careful planning and execution. Consider a phased approach if possible.
- **Database Compatibility:** If existing MySQL schemas are complex, refactoring them for Cloud Bigtable or Cloud Spanner could be significant.
- **Workload Specifics:** The best architecture depends on the exact nature of their transactional data vs. time series data.

References:

[https://cloud.google.com/architecture/best-practices-cloud-spanner-gaming-database](https://cloud.google.com/architecture/best-practices-cloud-spanner-gaming-database)

---

## Question 35

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**In the context of the Mountkirk Games case study, which managed storage option aligns with Mountkirk's technical requirement for storing game activity in a time series database service?**

- [x] A. Cloud Bigtable
- [ ] B. Cloud Spanner
- [ ] C. BigQuery
- [ ] D. Cloud Datastore

### Explanation

The correct answer is **A. Cloud Bigtable**.

Here's why it's the perfect fit for Mountkirk Games' requirement:

**Why Cloud Bigtable is Ideal for Time Series Data**

- **Data Structure:** Cloud Bigtable is designed specifically for storing and managing massive amounts of time-series data. Its columnar structure and row key indexing make it efficient for querying based on time ranges.
- **High Throughput:** Cloud Bigtable excels at handling high-volume data writes with low latency, essential for capturing real-time game activity.
- **Scalability:** It easily scales to handle the potentially vast amounts of game activity data generated by a popular game.
- **Integration with Analytics Tools:** Cloud Bigtable often integrates seamlessly with BigQuery and other analytics tools, enabling Mountkirk Games to perform historical analysis or build visualizations on their game activity data.

**Why Other Options Are Less Suitable**

- **B. Cloud Spanner:** Cloud Spanner is a globally distributed, strongly consistent relational database. While powerful, its primary focus isn't the high-volume, fast write patterns of time-series data.
- **C. BigQuery:** BigQuery is a serverless data warehouse optimized for analytical queries over large datasets. It's great for analysis but isn't the best choice for storing the raw, continuously generated game activity data.
- **D. Cloud Datastore:** Cloud Datastore is a NoSQL document database suited for storing semi-structured data. It's less optimized for the specific structure and access patterns of time-series data compared to Cloud Bigtable.

**References:**

[https://cloud.google.com/bigtable/docs/schema-design-time-series](https://cloud.google.com/bigtable/docs/schema-design-time-series)

---

## Question 36

*Domain 1: Designing and Planning a Cloud Solution Architecture*

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

**Referring to the Mountkirk Games case study, you are responsible for designing the new Game Backend Platform architecture, which communicates with the game via a REST API. How should you design the backend to adhere to Google-recommended practices?**

- [ ] A. Create an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L4 load balancer.
- [ ] B. Develop an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L4 load balancer.
- [x] C. Establish an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L7 load balancer.
- [ ] D. Design an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L7 load balancer.

### Explanation

Here's the breakdown of why option **C (Establish an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L7 load balancer)**

is the best design adhering to Google-recommended practices:

**Why Option C Excels**

- **Resiliency:** Multi-zone managed instance groups ensure instances are distributed across multiple zones within a region. This protects against localized failures and enhances availability.
- **Scalability:** Managed instance groups enable automatic scaling based on demand, handling traffic spikes without manual intervention.
- **HTTP(S) Traffic:** An L7 (HTTP/HTTPS) load balancer provides intelligent traffic distribution, content-based routing, and features like SSL termination, crucial for a REST API.
- **Google Best Practices:** This architecture aligns with Google's emphasis on reliability, scalability, and using the right load balancing type for the given traffic nature.

**Why Other Options Are Less Optimal**

- **A. Create an instance template for the backend and deploy it on a multi-zone managed instance group for each region. Utilize an L4 load balancer.** An L4 (TCP/UDP) load balancer lacks the content-aware features of an L7 load balancer, which are often useful for REST APIs (path-based routing, header inspection, etc.).
- **B. Develop an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L4 load balancer.** This is less resilient than a multi-zone setup, as it's vulnerable to a zone-level outage.
- **D. Design an instance template for the backend and deploy it on a single-zone managed instance group for each region. Utilize an L7 load balancer.** Similar to option B, the lack of multi-zone deployment increases the risk of downtime due to zone-level failures.

**Important Considerations:**

- **Global Deployment:** If the game has a global player base, consider a global HTTP(S) load balancer for cross-region distribution and lower latency.
- **API Design:** Ensure the REST API is stateless and well-structured to leverage load balancing effectively.

References:

[https://cloud.google.com/solutions/gaming/cloud-game-infrastructure#dedicated_game_server](https://cloud.google.com/solutions/gaming/cloud-game-infrastructure#dedicated_game_server)

---

## Question 37

*Domain 5: Managing Implementation*

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

- [ ] A. Utilize gsutil to batch move files in sequence.
- [x] B. Utilize gsutil to batch copy the files in parallel.
- [ ] C. Utilize gsutil to extract the files as the initial step of ETL.
- [ ] D. Utilize gsutil to load the files as the final step of ETL.

### Explanation

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

---

## Question 38

*Domain 3: Designing for Security and Compliance*

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

**As you implement Firestore for Mountkirk Games, the company aims to grant a new game programmatic access to a legacy game's Firestore database with the highest possible level of restriction. What action should you take?**

- [x] A. Create a service account (SA) in the legacy game's Google Cloud project, add this SA in the new game's IAM page, and then assign the Firebase Admin role to the SA in both projects.
- [ ] B. Create a service account (SA) in the legacy game's Google Cloud project, assign the SA the Organization Admin role, and then grant it the Firebase Admin role in both projects.
- [ ] C. Create a service account (SA) in the legacy game's Google Cloud project, add a second SA in the new game's IAM page, and then assign the Organization Admin role to both SAs.
- [ ] D. Create a service account (SA) in the legacy game's Google Cloud project, assign it the Firebase Admin role, and then migrate the new game to the legacy game's project.

### Explanation

**Correct Answer: A.**
**Create a service account (SA) in the legacy game's Google Cloud project, add this SA in the new game's IAM page, and then assign the Firebase Admin role to the SA in both projects.**

✅ **Justification for Correct Option (A):**

- **Principle of Least Privilege**: This option **limits access to only what's needed** by assigning the **Firebase Admin role** specifically to a **service account**, without granting excessive permissions (like Organization Admin).
- **Service Account Placement**: The service account is created in the **legacy game’s project**—where the **Firestore database resides**, which is the correct scope for managing access.
- **Cross-Project Access**: By **adding the service account to the new game’s IAM**, the new game can **impersonate or use this account** (as appropriate) to access Firestore securely.

📌 Refer to:

- [Granting roles to service accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)
- [Firebase Admin SDK access permissions](https://firebase.google.com/docs/auth/admin/manage-users)

❌ **Incorrect Options:**

**B. Assign the SA the Organization Admin role**

- **Overly permissive**: The **Organization Admin role** is extremely powerful and unnecessary for accessing Firestore. This **violates least privilege principles** and could be a serious security concern.
- 🔗 Organization Admin role reference

**C. Assign Organization Admin role to both SAs**

- Same problem as Option B, but even worse by **duplicating powerful access** to two service accounts across projects.
- Again, **not required for accessing Firestore**.

**D. Migrate the new game to the legacy game's project**

- **Unnecessary project consolidation**: This undermines the **isolation and resource boundary** established for different games. It also introduces **operational complexity** and **tight coupling** of unrelated workloads.

🔐 **Summary:**

To ensure **programmatic access with the highest restriction**, **Option A** correctly:

- Uses a **dedicated service account** with the **Firebase Admin role**
- Avoids excessive permissions
- Maintains **cross-project isolation** and follows best practices

**⚠️ Note:** Firebase Admin is broader than this need strictly requires (a Firestore/Datastore user role on the legacy project would be narrower), but it is the most restrictive option offered.

---

## Question 39

*Domain 3: Designing for Security and Compliance*

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

**To restrict the physical location of resources to Mountkirk Games' operating Google Cloud regions, what should you do?**

- [x] A. Configure an organizational policy that constrains where resources can be deployed.
- [ ] B. Configure IAM conditions to limit the configuration of resources.
- [ ] C. Adjust the quotas for resources in the regions not being utilized to 0.
- [ ] D. Set up a custom alert in Cloud Monitoring to disable resources upon creation in other regions.

### Explanation

The most direct and effective way to restrict the physical location of resources in Mountkirk Games' Google Cloud environment is:

**A. Configure an organizational policy that constrains where resources can be deployed.**

Here's why this is the best choice:

- **Enforceable Restriction:** Organizational policies provide a powerful way to enforce rules across an entire Google Cloud organization. This ensures that all projects within the organization must adhere to the location constraints, preventing accidental or unauthorized resource creation in disallowed regions.
- **Centralized Management:** Organizational policies allow you to manage restrictions from a single point of control, simplifying administration and ensuring consistency.
- **Flexibility:** These policies allow you to specify allowed regions at various levels of granularity (specific zones, regions, or multi-region areas), giving you the control you need.

**Why other options are less optimal:**

- **B. Configure IAM conditions to limit the configuration of resources.** IAM conditions are useful for fine-grained access control but wouldn't directly stop the provisioning of resources in the wrong location. Admins with sufficient permissions could still create resources in undesired regions.
- **C. Adjust the quotas for resources in the regions not being utilized to 0.** Quotas are helpful for managing resource usage but don't completely prevent resource creation. A user with enough permissions could adjust quotas to create resources even in restricted regions.
- **D. Set up a custom alert in Cloud Monitoring to disable resources upon creation in other regions.** This approach is reactive, not preventative. It could lead to resource creation in disallowed regions followed by deletion, causing disruptions.

**How to implement Organization Policies**

Here are the general steps to restrict resource locations using Organizational Policies:

1. **Access the Resource Manager in the Google Cloud Console:** Search for "Resource Manager" or find it under the IAM & Admin section.
2. **Navigate to the Organization Policies:** Locate the "Organization Policies" section.
3. **Create a new policy** Click on "Add Policy" and select the "locations constraint".
4. **Specify allowed regions** Choose "Allow" and then carefully select the specific zones, regions, or multi-region locations permitted for resource deployment.
5. **Save and Apply:** Save the policy, and it will propagate across your organization.

References:

[https://cloud.google.com/resource-manager/docs/organization-policy/defining-locationshttps://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraintshttps://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations  https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints  https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy)

---

## Question 40

*Domain 2: Managing and Provisioning a Solution Infrastructure*

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

**What is the recommended approach for implementing a network ingress for a new game that adheres to Mountkirk Games' specified business and technical requirements?**

- [x] A. Set up a global load balancer connected to a managed instance group running Compute Engine instances.
- [ ] B. Utilize kubemci in conjunction with a global load balancer and Google Kubernetes Engine.
- [ ] C. Establish a global load balancer integrated with Google Kubernetes Engine.
- [ ] D. Implement Ingress for Anthos alongside a global load balancer and Google Kubernetes Engine.

### Explanation

**Correct Answer: A. Set up a global load balancer connected to a managed instance group running Compute Engine instances.**

**Why A is correct**

Mountkirk Games explicitly plans to deploy the backend on **Google Compute Engine** and needs:

- **Global footprint + low latency** for players worldwide
- **High uptime** (downtime = lost players)
- **Autoscaling** based on game activity
- **Efficient resource usage** (scale out/in automatically)
- **Hardened Linux distro** (custom OS control on VMs)

A **Global External Application Load Balancer** gives **global anycast IP**, routes users to the closest healthy backend, and supports high availability. Pairing it with a **Managed Instance Group (MIG)** gives **autoscaling + autohealing**, which directly matches the backend scaling and uptime requirements.

Official docs:

- Global external Application Load Balancer (global ingress, low latency routing):
  [https://cloud.google.com/load-balancing/docs/https](https://cloud.google.com/load-balancing/docs/https)
- Managed Instance Groups (autoscaling and autohealing):
  [https://cloud.google.com/compute/docs/instance-groups](https://cloud.google.com/compute/docs/instance-groups)

Why the other options are not the best fit

**B. Utilize kubemci in conjunction with a global load balancer and Google Kubernetes Engine.**
Not recommended because **kubemci is an older / legacy-style approach** for multi-cluster ingress and adds operational complexity. It’s not the clean “recommended” ingress approach today for this requirement set.

Reference (kubemci is legacy / replaced by newer solutions):
[https://cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress)

**C. Establish a global load balancer integrated with Google Kubernetes Engine.**
This is valid *if* the backend was planned on **GKE**, but the scenario clearly says the backend will be on **Compute Engine**. This option also doesn’t directly address the requirement for a hardened Linux distro at the VM level (which is naturally aligned with GCE VM control).

Reference (GKE Ingress uses Cloud Load Balancing):
[https://cloud.google.com/kubernetes-engine/docs/concepts/ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress)

**D. Implement Ingress for Anthos alongside a global load balancer and Google Kubernetes Engine.**
Ingress for Anthos is mainly used for **advanced multi-cluster / hybrid** Kubernetes ingress patterns. That’s unnecessary complexity here, and the requirement is best met with a simpler, highly scalable **GCE + MIG + Global LB** architecture.

**Final Answer**

**A. Set up a global load balancer connected to a managed instance group running Compute Engine instances.**

###### Explanation

Mountkirk Games explicitly plans to deploy the backend on **Google Compute Engine** and needs:

- **Global footprint + low latency** for players worldwide
- **High uptime** (downtime = lost players)
- **Autoscaling** based on game activity
- **Efficient resource usage** (scale out/in automatically)
- **Hardened Linux distro** (custom OS control on VMs)

A **Global External Application Load Balancer** gives **global anycast IP**, routes users to the closest healthy backend, and supports high availability. Pairing it with a **Managed Instance Group (MIG)** gives **autoscaling + autohealing**, which directly matches the backend scaling and uptime requirements.

> [!note]- Why the other options are wrong
> **B. Utilize kubemci in conjunction with a global load balancer and Google Kubernetes Engine.**
> Not recommended because **kubemci is an older / legacy-style approach** for multi-cluster ingress and adds operational complexity. It’s not the clean “recommended” ingress approach today for this requirement set.
>
> Reference (kubemci is legacy / replaced by newer solutions):
> [https://cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress)
>
> **C. Establish a global load balancer integrated with Google Kubernetes Engine.**
> This is valid *if* the backend was planned on **GKE**, but the scenario clearly says the backend will be on **Compute Engine**. This option also doesn’t directly address the requirement for a hardened Linux distro at the VM level (which is naturally aligned with GCE VM control).
>
> Reference (GKE Ingress uses Cloud Load Balancing):
> [https://cloud.google.com/kubernetes-engine/docs/concepts/ingress](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress)
>
> **D. Implement Ingress for Anthos alongside a global load balancer and Google Kubernetes Engine.**
> Ingress for Anthos is mainly used for **advanced multi-cluster / hybrid** Kubernetes ingress patterns. That’s unnecessary complexity here, and the requirement is best met with a simpler, highly scalable **GCE + MIG + Global LB** architecture.

---

## Question 41

*Domain 6: Ensuring Solution and Operations Excellence*

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

- [ ] A. Establish CPU Utilization and Request Latency as service level indicators.
- [ ] B. Establish GKE CPU Utilization and Memory Utilization as service level indicators.
- [x] C. Establish Request Latency and Error Rate as service level indicators.
- [ ] D. Establish Server Uptime and Error Rate as service level indicators.

### Explanation

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

---

## Question 42

*Domain 3: Designing for Security and Compliance*

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

**To secure the connectivity from the new gaming application platform to Google Cloud in alignment with Google-recommended practices, what action should you take?**

- [x] A. Implement Workload Identity and service accounts for utilization by the application platform.
- [ ] B. Utilize Kubernetes Secrets, which are inherently obscured, and configure these Secrets for use by the application platform.
- [ ] C. Set up Kubernetes Secrets for storing the secret, enable Application-Layer Secrets Encryption, and utilize Cloud Key Management Service (Cloud KMS) for managing the encryption keys. Configure these Secrets for use by the application platform.
- [ ] D. Deploy HashiCorp Vault on Compute Engine, utilizing customer-managed encryption keys, and integrate Cloud Key Management Service (Cloud KMS) for encryption key management. Configure these Secrets for use by the application platform.

### Explanation

Here's a breakdown of why the best option is **A**, and the considerations for the other options:

**A. Implement Workload Identity and service accounts for utilization by the application platform.**

- **Google-Recommended:** Workload Identity is the preferred method for accessing Google Cloud services from applications running on Google Kubernetes Engine (GKE), aligning perfectly with Google-recommended practices.
- **Security:** Workload Identity eliminates the need to manage long-lived credentials or secrets within Kubernetes. Identity tokens are short-lived, reducing the risk of exposure.
- **Ease of Management:** Workload Identity simplifies access management by integrating with Kubernetes service accounts and IAM, allowing for centralized and granular authorization policies.

**Why Other Options Are Less Ideal:**

- **B. Utilize Kubernetes Secrets, which are inherently obscured, and configure these Secrets for use by the application platform.** While Kubernetes Secrets offer basic encoding, storing sensitive information like API keys or database passwords within them poses potential security risks. Secrets can be exposed if the Kubernetes cluster is compromised.
- **C. Set up Kubernetes Secrets for storing the secret, enable Application-Layer Secrets Encryption, and utilize Cloud Key Management Service (Cloud KMS) for managing the encryption keys. Configure these Secrets for use by the application platform.** This option introduces more complexity than Workload Identity, although it does provide a higher level of security than unencrypted Kubernetes Secrets.
- **D. Deploy HashiCorp Vault on Compute Engine, utilizing customer-managed encryption keys, and integrate Cloud Key Management Service (Cloud KMS) for encryption key management. Configure these Secrets for use by the application platform.** HashiCorp Vault offers excellent secret management capabilities but introduces additional complexity and operational overhead in terms of deployment and management. It might be overkill for Mountkirk Games' initial setup if their focus is on a streamlined cloud-native approach.

**Key Points to Consider:**

- **Workload Identity is the most streamlined and secure solution for the scenario described, assuming your application is running in GKE.**
- **If you cannot use Workload Identity, then option C (Kubernetes Secrets with appropriate encryption) is the next best choice.**

**How to Implement Workload Identity**

1. **Create a Google Cloud Service Account:** Provide necessary IAM permissions for the Google Cloud services the application needs to access.
2. **Create a Kubernetes Service Account:** Annotate this Kubernetes service account with the Google Cloud service account's email address to establish a connection.
3. **IAM Binding:** Create an IAM policy binding that grants the Kubernetes service account the ability to impersonate the Google Cloud service account.

References:

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

---

## Question 43

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [x] A. Utilize Firebase Test Lab by uploading the mobile app and conducting testing on both Android and iOS devices.
- [ ] B. Set up Android and iOS virtual machines (VMs) on Google Cloud, install the mobile app on the VMs, and conduct testing.
- [ ] C. Deploy Android and iOS containers on Google Kubernetes Engine (GKE), install the mobile app on the containers, and conduct testing.
- [ ] D. Upload the mobile app with different configurations to Firebase Hosting and conduct testing for each configuration.

### Explanation

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

---

## Question 44

*Domain 3: Designing for Security and Compliance*

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

**In accordance with Google's recommended best practices and considering the TerramEarth case study, how should you configure Cloud Functions to ensure that func_query can only be invoked by func_display?**

- [ ] A. Generate a token and set it as an environment variable for func_display. When invoking func_query, include the token in the request. Validate the token in func_query and reject the invocation if the tokens differ.
- [x] B. Enable "Require authentication" for func_query. Create a unique service account and link it to func_display. Assign the service account the invoker role for func_query. Generate an ID token within func_display and include it in the request when invoking func_query.
- [ ] C. Enable "Require authentication" for func_query and restrict it to internal traffic only. Deploy both functions within the same Virtual Private Cloud (VPC). Establish an ingress firewall rule for func_query to exclusively permit traffic from func_display.
- [ ] D. Deploy both functions in the same project and VPC. Configure func_query to solely accept internal traffic. Implement an ingress firewall for func_query to allow traffic solely from func_display. Additionally, ensure both functions utilize the same service account.

### Explanation

**B. Enable "Require authentication" for func_query. Create a unique service account and link it to func_display. Assign the service account the invoker role for func_query. Generate an ID token within func_display and include it in the request when invoking func_query.**

Here's a breakdown of why option B is ideal and why the others fall short:

**Why B is the Best Choice:**

- **Enhanced Security:** Enabling authentication for func_query enforces a layer of control. By linking a dedicated service account to func_display, access is restricted to that specific function.
- **Granular Control:** Assigning the "invoker" role to the service account grants the minimum required permission – the ability to invoke func_query. This adheres to the principle of least privilege.
- **Secure Communication:** Including an ID token generated within func_display in the request to func_query verifies the caller's identity. Only func_display with the linked service account can generate a valid ID token.

**Explanation of Why Other Options Are Less Optimal:**

- **D. Deploy both functions in the same project and VPC...** While this option offers basic network-level security, it lacks the explicit authentication provided by service accounts and ID tokens. If another function within the same VPC gained unauthorized access to the service account, it could potentially invoke func_query.
- **A. Generate a token and set it as an environment variable...** Custom tokens introduce additional complexity. Managing token generation, rotation, and ensuring their security adds extra overhead compared to using Google Cloud's built-in service accounts and ID tokens.
- **C. Enable "Require authentication"...** Similar to D, this approach provides basic network security but lacks the granularity of service account permissions. Additionally, restricting access solely to internal traffic might not be ideal for TerramEarth's future goals if they plan to expose func_display externally for specific integrations.

**Security Considerations:**

- **Service Account Permissions:** While the "invoker" role is a good starting point, review and adjust permissions as needed based on the specific actions func_display needs to perform within func_query.
- **ID Token Lifetime:** Configure ID tokens generated by func_display to have a short expiration time to minimize the window of vulnerability if compromised.
- **Monitoring and Logging:** Implement Cloud Monitoring and Logging to track API calls and identify any suspicious activity.

References:

[https://cloud.google.com/functions/docs/securing/authenticating](https://cloud.google.com/functions/docs/securing/authenticating)

---

## Question 45

*Domain 2: Managing and Provisioning a Solution Infrastructure*

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

**In the context of the TerramEarth case study, where a legacy monolithic application has been broken down into containerized RESTful microservices, how can you ensure high availability and low latency for these microservices when deploying them on Cloud Run?**

- [ ] A. Deploy the Cloud Run services across multiple availability zones. Configure Cloud Endpoints to direct traffic to these services. Set up a global HTTP(S) Load Balancer and link the Cloud Endpoints to its backend.
- [x] B. Spread the Cloud Run services across multiple regions. Establish serverless network endpoint groups (NEGs) that point to these services. Integrate the serverless NEGs into a backend service utilized by a global HTTP(S) Load Balancing instance.
- [ ] C. Deploy the Cloud Run services across multiple regions. Utilize Cloud DNS to create a latency-based DNS name directing to these services.
- [ ] D. Deploy the Cloud Run services across multiple availability zones. Implement a TCP/IP global load balancer and incorporate the Cloud Run Endpoints into its backend service.

### Explanation

The best option to ensure high availability and low latency for TerramEarth's microservices on Cloud Run is:

**B. Spread the Cloud Run services across multiple regions. Establish serverless network endpoint groups (NEGs) that point to these services. Integrate the serverless NEGs into a backend service utilized by a global HTTP(S) Load Balancing instance.**

Here's why this solution stands out:

- **Global Reach and Redundancy:** Distributing Cloud Run services across multiple regions and using serverless NEGs provides global load balancing and failover. If a service in one region fails, traffic is routed to healthy instances in other regions.
- **Latency Reduction:** Google's global load balancing infrastructure intelligently routes traffic to the closest healthy service instance, minimizing latency for users worldwide.
- **Managed Services:** Cloud Run and serverless NEGs remove operational overhead compared to manually managing load balancers and virtual machines.
- **Scalability:** Cloud Run's automatic scaling capabilities seamlessly support TerramEarth's expected growth, accommodating demand spikes while reducing unnecessary costs.

**Why Other Options are Less Ideal:**

- **A. Deploy the Cloud Run services across multiple availability zones...** While deploying across availability zones within a single region helps with localized failures, it doesn't address TerramEarth's need for low-latency across a global user base.
- **C. Deploy the Cloud Run services across multiple regions. Utilize Cloud DNS...** Cloud DNS with latency-based routing offers some load distribution, but it might not be as fine-grained or responsive as using dedicated global HTTP(S) load balancing. Additionally, load balancers provide more robust health checks and traffic management features.
- **D. Deploy the Cloud Run services across multiple availability zones...** This option offers the same limitation as A – focus on localized availability within a region instead of global distribution and latency optimization.

**Key Points to Consider:**

- **Availability Zones vs. Regions:** Availability zones are isolated locations *within* a region, while regions are geographically distinct areas. TerramEarth needs deployment across multiple regions for true global high availability.
- **Cloud Run with Global HTTP(S) Load Balancer:** This combination provides a powerful and managed solution to achieve TerramEarth's business requirements.

**Additional Considerations:**

- **Traffic Patterns:** Carefully analyze expected traffic patterns to determine the optimal number of instances to deploy in each region.
- **Monitoring:** Utilize Cloud Monitoring and Logging to track service availability, latency, and troubleshoot issues.

References:

[https://cloud.google.com/load-balancing/docs/negs/serverless-neg-conceptshttps://cloud.google.com/run/docs/multiple-regions](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts  https://cloud.google.com/run/docs/multiple-regions)

---

## Question 46

*Domain 3: Designing for Security and Compliance*

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

**In the context of the TerramEarth case study, during the migration of a Linux-based application from a private data center to Google Cloud, the TerramEarth security team has provided several recent Linux vulnerabilities identified by Common Vulnerabilities and Exposures (CVE). What steps should you take to comprehend the potential impact of these vulnerabilities? (Select two.)**

- [x] A. Open a support case related to the CVE and engage in a discussion with the support engineer.
- [ ] B. Review the CVEs through the Google Cloud Status Dashboard to grasp their implications.
- [x] C. Refer to the Google Cloud Platform Security Bulletins to understand the impact of the CVEs.
- [ ] D. Seek an explanation about the CVEs by posting a question on Stack Overflow.
- [ ] E. Seek an explanation about the CVEs by posting a question in a Google Cloud discussion group.

### Explanation

Let me clarify why options **A** and **C** stand out as the most suitable choices, and where the other options might be less effective for TerramEarth's scenario:

**A. Open a support case related to the CVE and engage in a discussion with the support engineer.**

- **Direct Assistance:** Google Cloud support engineers have in-depth knowledge of GCP services and can provide specific guidance on how the CVEs might impact TerramEarth's migration.
- **Tailored Advice:** They can consider the specific Linux distribution, application components, and configurations TerramEarth is using to offer targeted recommendations.
- **Access to Internal Information:** Support engineers might have insights into unreleased patches or upcoming security updates that are not yet publicly available.

**C. Refer to the Google Cloud Platform Security Bulletins to understand the impact of the CVEs.**

- **Focused Information:** Security Bulletins are specifically designed to explain the implications of security vulnerabilities related to GCP, making them a highly relevant resource for TerramEarth.
- **Actionable Guidance:** Bulletins often outline mitigation steps, patches, or configuration changes needed to address the CVEs within the context of Google Cloud.
- **Official and Reliable Source:** Google directly publishes the Security Bulletins, ensuring the information is accurate and up-to-date.

**Why Other Options Are Less Optimal:**

- **B. Review the CVEs through the Google Cloud Status Dashboard...** While the Status Dashboard is valuable, it primarily focuses on service disruptions or known issues. It might not offer the same level of detail on specific CVEs and their mitigation strategies as the Security Bulletins.
- **D. Seek an explanation about the CVEs by posting a question on Stack Overflow.** Stack Overflow is a great general-purpose resource, but responses might lack the specificity needed for TerramEarth's assessment within the context of their Google Cloud migration.
- **E. Seek an explanation about the CVEs by posting a question in a Google Cloud discussion group.** Discussion groups can be helpful, but the quality of responses can vary, and there might be delays in getting specific answers about the CVEs' impact on TerramEarth's migration.

**Key Takeaway:** Prioritize official and reliable channels from Google (Support and Security Bulletins) for the most accurate and actionable guidance during a security-sensitive migration.

References:

[https://cloud.google.com/support/bulletins](https://cloud.google.com/support/bulletins)

---

## Question 47

*Domain 6: Ensuring Solution and Operations Excellence*

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

- [ ] A. Develop a scheduled job in Cloud Run to trigger a container every minute. The container will inspect the application URL; if the application is inaccessible, it will switch the URL to the "Site is unavailable" page and notify the Ops team.
- [ ] B. Set up a cron job on a Compute Engine VM scheduled to run every minute. The cron job will execute a Python script to check the application URL status. Upon detecting downtime, it will switch the URL to the "Site is unavailable" page and notify the Ops team.
- [x] C. Configure a Cloud Monitoring uptime check to monitor the application URL. Upon failure, publish a message to a Pub/Sub queue, triggering a Cloud Function to switch the URL to the "Site is unavailable" page and notify the Ops team.
- [ ] D. Utilize Cloud Error Reporting to monitor the application URL. In case of downtime, automatically switch the URL to the "Site is unavailable" page and notify the Ops team.

### Explanation

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

---

## Question 48

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [x] A. Set up a trigger in Cloud Build to respond to new source changes. Utilize Cloud Build to build container images for each microservice, tagging them with the code commit hash, and then push the images to the Container Registry.
- [ ] B. Configure a trigger in Cloud Build to handle new source changes. This trigger should initiate build jobs to construct container images for the microservices, tagging these images with a version number before pushing them to Cloud Storage.
- [ ] C. Establish a Scheduler job to monitor the repository every minute. Upon detecting new changes, trigger Cloud Build to build container images for the microservices. Tag the images using the current timestamp and then push them to the Container Registry.
- [ ] D. Implement a trigger in Cloud Build to handle new source changes. Utilize Cloud Build to construct a single container image, tagging it with the label 'latest,' and then push this image to the Container Registry.

### Explanation

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

---

## Question 49

*Domain 5: Managing Implementation*

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

- [x] A. Request Transfer Appliances from Google Cloud, transfer the data to the appliances, and then return the appliances to Google Cloud for ingestion into Cloud Storage.
- [ ] B. Set up the Storage Transfer service provided by Google Cloud to facilitate the transfer of data from your data center to Cloud Storage.
- [ ] C. Ensure exclusive access to the 1-Gbps link and employ multi-threaded transfer techniques to upload the data to Cloud Storage.
- [ ] D. Export the data to an encrypted USB device, dispatch the device to Google Cloud, and request a data import to Cloud Storage.

### Explanation

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

---

## Question 50

*Domain 4: Analyzing and Optimizing Technical and Business Processes*

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

- [x] A. The session variable is local to just a single instance.
- [ ] B. The session variable is being overwritten in Cloud Datastore.
- [ ] C. The URL of the API needs modification to prevent caching.
- [ ] D. The HTTP Expires header needs to be set to -1 to prevent caching.

### Explanation

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

---

## Question 51

*Domain 5: Managing Implementation*

**A developer in your team deployed his application in Google Container Engine using the Dockerfile provided below. They have noticed that the application deployments are taking longer than desired.**

*FROM ubuntu:16.03*

*COPY . /src*

*RUN apt-get update && apt-get install -y python python-pip*

*RUN pip installl -r requirements.txt*

**Which two actions should you take to optimize this Dockerfile for faster deployment times without adversely affecting the app's functionality? (Choose two.)**

- [ ] A. Eliminate Python after pip installation.
- [ ] B. Minimize dependencies in requirements.txt.
- [x] C. Opt for a lightweight base image like Alpine Linux.
- [ ] D. Upgrade to larger machine types for Google Container Engine node pools.
- [x] E. Rearrange the source code copying step after installing package dependencies (Python and pip).

### Explanation

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

---

## Question 52

*Domain 5: Managing Implementation*

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

- [ ] A. Ensure all necessary JAR files are uploaded and redeploy your application.
- [x] B. Apply digital signatures to all JAR files and redeploy your application.
- [ ] C. Rebuild the CloakedServlet class using MD5 hashing instead of SHA1.
- [ ] D. Only Clean and Rebuild Your Project

### Explanation

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

---

## Question 53

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**Your company has a project in Google Cloud with three Virtual Private Clouds (VPCs). There is a Compute Engine instance on each VPC. Network subnets do not overlap and must remain separated. The network configuration is shown below. Instance #1 is an exception and must communicate directly with both Instance #2 and Instance #3 via internal IPs. How should you accomplish this?**

![](https://img-c.udemycdn.com/redactor/raw/practice_test_question/2024-03-12_09-16-28-70e965d00dc270a8a9c983257f8d4cea.jpg)

- [ ] A. Create a cloud router to advertise subnet #2 and subnet #3 to subnet #1.
- [x] B. Add two additional NICs to Instance #1 with the following configuration: NIC1: VPC: VPC #2, SUBNETWORK: subnet #2 NIC2: VPC: VPC #3, SUBNETWORK: subnet #3 Update firewall rules to enable traffic between instances.
- [ ] C. Create two VPN tunnels via CloudVPN: 1 between VPC #1 and VPC #2. 1 between VPC #2 and VPC #3. Update firewall rules to enable traffic between the instances.
- [ ] D. Peer all three VPCs: Peer VPC #1 with VPC #2. Peer VPC #2 with VPC #3. Update firewall rules to enable traffic between the instances.

### Explanation

Here's a breakdown of the options and why the best solution is

**B. Add two additional NICs to Instance #1**:

**Explanation:**

- **Direct Communication:** Option B allows Instance #1 to communicate directly with Instance #2 and Instance #3 using their internal IPs within their respective VPCs. This is the most efficient approach for the specified scenario.
- **Network Isolation:** Since the subnets must remain separated, having Instance #1 be part of those networks is the most practical way to ensure connectivity with the other instances while maintaining the separation required.

**Why the Others Are Less Ideal:**

- **A. Cloud Router:** While a cloud router could advertise routes, it adds complexity and potential overhead, particularly when direct communication is possible.
- **C. VPN Tunnels:** CloudVPN is a good option for cross-VPC communication, but it would be overkill in this case. VPNs introduce additional overhead and management complexity.
- **D. VPC Peering:** Peering VPCs would allow communication, but it's not the most efficient solution. Peered networks can still have firewall restrictions, and it would unnecessarily connect VPC #2 and #3 when direct communication between them isn't needed.

**Steps for Option B:**

1. **Add NICs:**
  - Go to the Compute Engine instance details for Instance #1.
  - Edit the instance and add two additional network interfaces (NICs).
  - Configure each NIC with its respective VPC and subnet.
2. **Firewall Rules:**
  - Create firewall rules within each VPC's network settings to allow traffic between the internal IP addresses of the three instances.

**Important Considerations:**

- **Security:** Ensure your firewall rules are as specific as possible to only allow necessary traffic between the instances.
- **Instance IP Assignments:** You'll likely need to manually assign static internal IP addresses to the relevant NICs on Instance #1 for reliable communication.

References:

[https://cloud.google.com/vpc/docs/create-use-multiple-interfaceshttps://cloud.google.com/vpc/docs/multiple-interfaces-concepts#firewall_rules_and_multiple_network_interfaces](https://cloud.google.com/vpc/docs/create-use-multiple-interfaces  https://cloud.google.com/vpc/docs/multiple-interfaces-concepts#firewall_rules_and_multiple_network_interfaces)

---

## Question 54

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**A public health information website hosted in an on-premises EHR data center is experiencing slow response times, coupled with distributed denial-of-service attacks from specific IP address ranges. EHR management deems the website suitable for migration to Google Cloud due to its low risk. To address latency issues and prevent denial-of-service traffic, what steps should be taken?**

- [ ] A. Deploy an external HTTP(S) load balancer, set up VPC firewall rules, and migrate the applications to Compute Engine virtual machines.
- [x] B. Deploy an external HTTP(S) load balancer, configure Google Cloud Armor, and migrate the application to Compute Engine virtual machines.
- [ ] C. Containerize the application and migrate it to Google Kubernetes Engine (GKE). Implement a GKE service for pod exposure within the cluster, and establish a GKE network policy.
- [ ] D. Containerize the application and migrate it to Google Kubernetes Engine (GKE). Employ an internal load balancer for pod exposure outside the cluster, and enable Identity-Aware Proxy (IAP) for access control.

### Explanation

The best choice amongst these options is **B**:

- **External HTTP(S) Load Balancer:** Distributes traffic across multiple VM instances, improving performance and resilience against traffic surges.
- **Google Cloud Armor:** Provides built-in DDoS protection and web application firewall (WAF) capabilities to filter out malicious traffic based on IP ranges and other attack signatures.
- **Compute Engine Virtual Machines:** A flexible and scalable infrastructure-as-a-service (IaaS) option suitable for migrating the existing web application.

**Here's why the other options are less optimal:**

- **A:** While this solution addresses some of the issues, it lacks specific defenses against the mentioned DDoS attacks.
- **C:** While GKE is great for containerized workloads, it might introduce unnecessary complexity for a simple web application migration focused on latency and DDoS protection.
- **D:** GKE's internal load balancer is for traffic within a cluster. IAP focuses on user authentication rather than DDoS mitigation.

**Important Considerations:**

- **Cloud Armor Configuration:** Careful configuration of Cloud Armor's WAF rules is needed to block specific DDoS attack patterns and mitigate the identified IP address ranges.
- **Monitoring:** Implement robust monitoring for both performance metrics and Cloud Armor logs to detect and respond to potential attacks.

[https://cloud.google.com/vpc/docs/firewalls](https://cloud.google.com/vpc/docs/firewalls)

[https://cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency](https://cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency)

[https://cloud.google.com/armor/docs/security-policy-concepts](https://cloud.google.com/armor/docs/security-policy-concepts)

[https://cloud.google.com/kubernetes-engine/docs/concepts/service](https://cloud.google.com/kubernetes-engine/docs/concepts/service)

[https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy](https://cloud.google.com/kubernetes-engine/docs/how-to/network-policy)

[https://cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress-ilb)

[https://cloud.google.com/iap/docs/concepts-overview#when_to_use_iap](https://cloud.google.com/iap/docs/concepts-overview#when_to_use_iap)

---

## Question 55

*Domain 2: Managing and Provisioning a Solution Infrastructure*

For this question, refer to the EHR Healthcare case study. https://services.google.com/fh/files/blogs/master_case_study_ehr_healthcare.pdf

**When connecting an EHR data center situated over 100 kilometers from the closest major city to Google Cloud using a high-bandwidth, low-latency microwave connection, what factors should be considered in designing the network connection?**

- [ ] A. Implement Carrier Peering provisioning.
- [ ] B. Establish a new Internet connection.
- [x] C. Set up Partner Interconnect provisioning.
- [ ] D. Implement Dedicated Interconnect provisioning.

### Explanation

**C is correct because it allows the customer to lower latency by connecting directly to a partner network that is directly connected to Google. This option will also allow the customer to use the lower bandwidth interfaces that they have on their current firewall.**

Other options is not correct:

A is not correct because it does not give private IP addressing across the connection.

B is not correct because an additional Internet connection will not provide RFC1918 communications by itself.

D is not correct because Dedicated Interconnect would require the customer to buy new hardware to get a 10 gig interface for their firewall.

References:

[https://cloud.google.com/blog/products/networking/google-cloud-network-connectivity-options-explained](https://cloud.google.com/blog/products/networking/google-cloud-network-connectivity-options-explained)

[https://cloud.google.com/interconnect/docs/how-to/carrier-peering#considerations](https://cloud.google.com/interconnect/docs/how-to/carrier-peering#considerations)

[https://cloud.google.com/interconnect/docs/concepts/partner-overview](https://cloud.google.com/interconnect/docs/concepts/partner-overview)

[https://cloud.google.com/interconnect/docs/concepts/dedicated-overview#before_you_use](https://cloud.google.com/interconnect/docs/concepts/dedicated-overview#before_you_use)

---

## Question 56

*Domain 3: Designing for Security and Compliance*

For this question, refer to the EHR Healthcare case study.

https://services.google.com/fh/files/blogs/master_case_study_ehr_healthcare.pdf

**A renowned research and hospital facility, serving many public figures, is an EHR healthcare customer. Given the sensitivity of their patients' health information, both internal and external sources have attempted to access it maliciously. To safeguard patient data stored in Cloud Storage buckets, the hospital mandates that data must not leave the geographic regions where the buckets are hosted. Specifically, information stored in Cloud Storage buckets in the "europe-west2" region must remain within that area. What action should be taken?**

- [ ] A. Encrypt the data within the on-premises application before storing it in the "europe-west2" region.
- [x] B. Activate Virtual Private Cloud Service Controls and establish a service perimeter encompassing the Cloud Storage resources.
- [ ] C. Restrict the Identity and Access Management (IAM) "storage.objectViewer" role solely to users and service accounts requiring access to the data.
- [ ] D. Implement an access control list (ACL) to restrict bucket access to authorized users, applying it to buckets within the "europe-west2" region.

### Explanation

The most effective solution in this scenario is

**B: Activate Virtual Private Cloud Service Controls and establish a service perimeter encompassing the Cloud Storage resources.** Here's why:

- **Data Residency Enforcement:** VPC Service Controls directly address the core requirement of preventing data from leaving the specified region ("europe-west2"). It creates a security perimeter around Google Cloud resources, including Cloud Storage, to enforce data residency requirements.
- **Access Restriction:** VPC Service Controls restrict data egress even if permissions are misconfigured, providing a strong layer of protection.

**Why other options are less optimal:**

- **A. Encryption:** Encryption is essential but doesn't prevent data from leaving the region. If an attacker gets access to the bucket, data could still be exfiltrated.
- **C. IAM Permissions:** Restricting IAM roles is a good security practice but doesn't guarantee data residency. Misconfigurations could still allow data transfer outside the region.
- **D. ACLs:** ACLs provide granular control but offer less robust enforcement of data residency compared to VPC Service Controls.

**Important Considerations:**

- **Thorough Configuration:** Carefully configure VPC Service Controls to enforce the perimeter around the specific Cloud Storage buckets located in the "europe-west2" region.
- **Layered Security:** Use a combination of encryption, IAM, and ACLs for a defense-in-depth approach alongside VPC Service Controls.

References:

[https://cloud.google.com/vpc-service-controls/docs/overview](https://cloud.google.com/vpc-service-controls/docs/overview)

[https://cloud.google.com/storage/docs/access-control/lists](https://cloud.google.com/storage/docs/access-control/lists)

---

## Question 57

*Domain 3: Designing for Security and Compliance*

**In the context of the EHR Healthcare case study, where sales employees work remotely and require access to web-based sales tools located in the EHR data center, a transition from a Virtual Private Network (VPN) infrastructure to a BeyondCorp access model is underway. Each sales employee possesses a Google Workspace account for single sign-on (SSO). What steps should be taken?**

- [x] A. Set up an Identity-Aware Proxy (IAP) connector directed towards the sales tool application.
- [ ] B. Establish a Google group for the sales tool application and elevate it to a security group status.
- [ ] C. Deploy an external HTTP(S) load balancer and craft a customized Cloud Armor policy tailored for the sales tool application.
- [ ] D. Grant the predefined AppEngine Viewer role to each Google Workspace user account requiring access to the sales tool application.

### Explanation

Here's the breakdown of why the best answer is

**A: Set up an Identity-Aware Proxy (IAP) connector directed towards the sales tool application.**

- **Core of BeyondCorp:** IAP is the cornerstone of Google's BeyondCorp implementation, enabling context-aware authorization for applications beyond the traditional VPN boundary.
- **Authentication and Authorization:** IAP tightly integrates with Google Workspace SSO, ensuring seamless user authentication. It allows the creation of granular access policies based on user identity, device, context, etc.
- **On-premises Application Access:** Deploying an IAP connector enables IAP to secure access to on-premises workloads like the web-based sales tool located in the data center.

**Why other options aren't the best fit:**

- **B. Group and Security Group:** While creating a Google group is a necessary step, simply elevating it to a security group status won't implement the BeyondCorp model.
- **C. Load Balancer and Cloud Armor:** They are valuable for scaling and security but focus on Layer 4 (network) traffic control instead of the granular application-level access central to BeyondCorp.
- **D. Predefined AppEngine Role:** This role is specific to App Engine applications and not directly applicable to securing an on-premises sales tool.

**Important Notes:**

- **Transition Planning:** Switching to a BeyondCorp model may involve adjustments to the existing sales tool application for integration with IAP.
- **BeyondCorp Benefits:** This shift brings improved security, access controls, and aligns with the zero-trust philosophy.

References:

[https://cloud.google.com/iap/docs/cloud-iap-for-on-prem-apps-overview](https://cloud.google.com/iap/docs/cloud-iap-for-on-prem-apps-overview)

---

## Question 58

*Domain 3: Designing for Security and Compliance*

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**As the data compliance officer for Mountkirk Games, you're tasked with safeguarding customers' personally identifiable information (PII). Mountkirk Games aims to produce anonymized usage reports for their new game and implement a mechanism to delete PII data after a designated timeframe, all while keeping costs at a minimum. How can you ensure compliance while fulfilling these business and technical requirements?**

- [ ] A. Store audit logs in Cloud Storage and manually compile reports.
- [ ] B. Develop a Cloud Logging filter to export specific date ranges to Pub/Sub.
- [x] C. Archive audit logs in BigQuery and utilize Google Data Studio to generate reports.
- [ ] D. Archive user logs on a locally attached persistent disk and consolidate them into a text file for auditing.

### Explanation

**C: Archive audit logs in BigQuery and utilize Google Data Studio to generate reports.**

**Reasons for its superiority:**

- **Cost-Effectiveness and Scalability:** BigQuery's long-term storage is cost-effective for archiving large volumes of audit logs. Its serverless architecture scales effortlessly as data grows.
- **Advanced Analytics and Reporting:** BigQuery's SQL-like querying enables sophisticated analysis of audit logs to extract PII and generate anonymized usage reports tailored to the game's needs. Google Data Studio provides a user-friendly interface for visualizing these reports.
- **PII Deletion:** BigQuery supports time-based partitioning. You can schedule automated jobs within BigQuery to delete partitions containing PII data older than the specified timeframe, ensuring compliance.

**Why other options are less optimal:**

- **A. Cloud Storage and Manual Work:** This approach lacks the query power of BigQuery for targeted PII identification and would involve significantly more manual effort in report creation.
- **B. Cloud Logging to Pub/Sub:** While useful for real-time processing, Pub/Sub doesn't offer the cost-effective, long-term retention and flexible analytics essential for PII management.
- **D. Locally Attached Disk:** Lacks scalability, introduces additional management overhead, and doesn't integrate well with cloud-based tools for analytics and reporting.

**Additional Considerations:**

- **Logging Configuration:** Ensure Cloud Audit Logs (specifically, Data Access logs) are enabled at the relevant project or organization level to capture user activity and PII interactions.
- **PII Identification:** Carefully define what constitutes PII in the context of game data. Implement regular expressions or other techniques within BigQuery queries to reliably locate PII.

References:

[https://cloud.google.com/security/compliance/soc-2](https://cloud.google.com/security/compliance/soc-2)

[https://cloud.google.com/logging/docs/audit](https://cloud.google.com/logging/docs/audit)

[https://cloud.google.com/bigquery/docs/cached-results](https://cloud.google.com/bigquery/docs/cached-results)

[https://cloud.google.com/logging/docs/view/available-logs](https://cloud.google.com/logging/docs/view/available-logs)

**⚠️ Note:** The options don't really address PII deletion. C works because BigQuery can hold the logs cheaply, drop old partitions on a schedule (partition expiration) and feed Data Studio (called Looker Studio from 2022 to 2026) reports.

---

## Question 59

*Domain 3: Designing for Security and Compliance*

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**Mountkirk Games seeks assurance that their new gaming platform adheres to Google's best practices. You aim to confirm compliance with Google-recommended security standards while also providing the operations teams with necessary metrics. What steps should you take? (Choose two)**

- [x] A. Confirm the absence of privileged containers in operation.
- [ ] B. Implement obfuscated tags on workloads for enhanced security.
- [x] C. Utilize native logging mechanisms for monitoring.
- [ ] D. Ensure workloads do not utilize securityContext to operate as a group.
- [ ] E. Enable GKE metering on each cluster to facilitate team-specific usage charging.

### Explanation

**A is correct because this is High Priority according to Google best practices.**

**C is correct because this is High Priority according to Google best practices.**

**Other options is not correct:**

B is not correct because tags should be readable and useful to the operations teams when they are working on the clusters.

D is not correct because this may be required for some workloads.

E is not correct because although from a business process this may be useful it won’t impact the operations or security of the cluster.

Hints - [https://cloud.google.com/solutions/best-practices-for-operating-containers](https://cloud.google.com/solutions/best-practices-for-operating-containers)

---

## Question 60

*Domain 3: Designing for Security and Compliance*

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**To implement Virtual Private Cloud (VPC) Service Controls for Mountkirk Games, you must address the company's need to allow Cloud Shell usage by developers while restricting their access to managed services. How can you reconcile these conflicting objectives with Mountkirk Games' business requirements?**

- [ ] A. Implement VPC Service Controls across the entire platform.
- [ ] B. Give precedence to implementing VPC Service Controls over Cloud Shell usage for the entire platform.
- [ ] C. Enroll all developers in an access level associated with the service perimeter and authorize their use of Cloud Shell.
- [x] D. Establish a service perimeter solely around projects handling sensitive data and withhold access to it from developers.

### Explanation

**D is correct because VPC Service Controls protects data, and Cloud Shell facilitates rapid iteration of Google Cloud architecture changes.**

**Other options is not correct:**

A is not correct because VPC Service Controls do not directly affect scaling of Google Cloud architecture.

B is not correct because a security perimeter is not a business requirement, but rapid iteration is.

C is not correct because it works but does not scale, and we do not want to give users this much access.

References:

[https://cloud.google.com/vpc-service-controls/docs/supported-products#shell](https://cloud.google.com/vpc-service-controls/docs/supported-products#shell)

[https://cloud.google.com/vpc-service-controls](https://cloud.google.com/vpc-service-controls)

---

## Question 61

*Domain 6: Ensuring Solution and Operations Excellence*

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**As your new game on Google Cloud enters public beta, you aim to establish meaningful service level objectives (SLOs) before its general availability. What approach should you take?**

- [ ] A. Set one SLO for 99.9% game server availability and another for less than 100-ms latency.
- [ ] B. Establish one SLO aligning with Google Cloud's availability and another targeting 100-ms latency.
- [x] C. Define one SLO ensuring 99% of HTTP requests return the 2xx status code, and another for 99% of requests to complete within 100 ms.
- [ ] D. Define one SLO for the total uptime of the game server within a week and another for the mean response time of all HTTP requests under 100 ms.

### Explanation

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

---

## Question 62

*Domain 1: Designing and Planning a Cloud Solution Architecture*

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Helicopter Racing League (HRL) case study.

https://services.google.com/fh/files/blogs/master_case_study_helicopter_racing_league.pdf

**HRL seeks assistance in introducing existing recorded video content to new audiences in emerging regions. How should you proceed, considering HRL's business and technical needs?**

- [ ] A. Deliver the video content directly from a multi-region Cloud Storage bucket.
- [x] B. Employ Cloud CDN to cache the video content from HRL's current public cloud provider.
- [ ] C. Utilize Apigee Edge to cache the video content from HRL's existing public cloud provider.
- [ ] D. Replicate the video content in Google Kubernetes Engine clusters located near the target audience.

### Explanation

**B is correct because Cloud CDN can be used to cache data hosted on other cloud providers and supports large objects such as video.**

**Other options is Not correct:**

A is not correct because a multi-region bucket does not serve all global areas with similar latency.

C is not correct because Apigee Edge is not designed to cache data larger than 512 KB.

D is not correct because replicating the video content introduces unnecessary complexity.

References:

[https://cloud.google.com/storage/docs/locations#considerations](https://cloud.google.com/storage/docs/locations#considerations)

[https://cloud.google.com/cdn/docs/caching#maximum-size](https://cloud.google.com/cdn/docs/caching#maximum-size)

[https://cloud.google.com/cdn/docs/custom-origins-overview#hybrid_and_multi-cloud_architectures](https://cloud.google.com/cdn/docs/custom-origins-overview#hybrid_and_multi-cloud_architectures)

[https://docs.apigee.com/api-platform/antipatterns/caching-large](https://docs.apigee.com/api-platform/antipatterns/caching-large)

[https://cloud.google.com/solutions/building-a-multi-cluster-service-mesh-on-gke-using-replicated-control-plane-architecture](https://cloud.google.com/solutions/building-a-multi-cluster-service-mesh-on-gke-using-replicated-control-plane-architecture)

---

## Question 63

*Domain 3: Designing for Security and Compliance*

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the TerramEarth case study.

https://services.google.com/fh/files/blogs/master_case_study_terramearth.pdf

**As the data compliance officer for TerramEarth, your task is to safeguard customers' personally identifiable information (PII), including credit card details. However, TerramEarth aims to offer personalized product recommendations to its extensive industrial clientele. How can you uphold data privacy while delivering a solution?**

- [ ] A. Utilize AutoML to supply data to the recommendation service.
- [ ] B. Process PII data on-premises to enhance the security of private information.
- [x] C. Leverage the Cloud Data Loss Prevention (DLP) API to provide data to the recommendation service.
- [ ] D. Develop, train, and test machine learning models manually to deliver product recommendations anonymously.

### Explanation

The best approach in this scenario is

**C: Leverage the Cloud Data Loss Prevention (DLP) API to provide data to the recommendation service.** Here's why:

- **Balancing Personalization and Privacy:** The DLP API enables the de-identification of sensitive data like credit card details before sending it to the recommendation service. This allows TerramEarth to create useful recommendations without compromising PII.
- **Built-in De-identification:** The DLP API offers various techniques like masking, redaction, tokenization, etc., to sanitize sensitive data, ensuring compliance with data privacy regulations.
- **Cloud-Native and Scalable:** The DLP API integrates seamlessly with other GCP services and can handle the large-scale data processing that TerramEarth likely requires.

**Why Other Options Are Less Ideal:**

- **A. AutoML:** While powerful for building ML models, AutoML itself doesn't address PII concerns. Feeding it raw customer data would create privacy risks.
- **B. On-premises Processing:** Increases complexity and potentially weakens security posture by introducing a hybrid environment. Doesn't solve the core problem of needing to use the data while protecting PII
- **D. Manual ML Model Development:** Extremely resource-intensive and error-prone, especially at scale. Unlikely to keep pace with TerramEarth's large customer base.

**Essential Considerations:**

- **DLP Configuration:** Carefully select the appropriate de-identification methods based on PII sensitivity and requirements.
- **Regular Audit:** Implement ongoing monitoring and auditing procedures to ensure DLP rules are effective and updated as compliance needs evolve.

References:

[https://cloud.google.com/dlp/docs/deidentify-sensitive-data](https://cloud.google.com/dlp/docs/deidentify-sensitive-data)

[https://cloud.google.com/automl](https://cloud.google.com/automl)

---

## Question 64

*Domain 2: Managing and Provisioning a Solution Infrastructure*

**You're tasked with designing a future-proof hybrid environment requiring network connectivity between Google Cloud and your on-premises setup. Your aim is to ensure compatibility between the Google Cloud environment and your on-premises networking environment. What steps should you take?**

- [ ] A. Opt for the default VPC in your Google Cloud project and establish a Cloud VPN connection between your on-premises environment and Google Cloud.
- [ ] B. Create a custom VPC in Google Cloud in auto mode and set up a Cloud VPN connection between your on-premises environment and Google Cloud.
- [ ] C. Develop a network plan for your VPC in Google Cloud that utilizes CIDR ranges overlapping with your on-premises environment. Utilize a Cloud Interconnect connection between your on-premises environment and Google Cloud.
- [x] D. Design a network plan for your VPC in Google Cloud with CIDR ranges that do not overlap with your on-premises environment. Deploy a Cloud Interconnect connection between your on-premises environment and Google Cloud.

### Explanation

**D. Design a network plan for your VPC in Google Cloud with CIDR ranges that do not overlap with your on-premises environment. Deploy a Cloud Interconnect connection between your on-premises environment and Google Cloud.**

Let's break down the reasons for this:

- **Non-Overlapping CIDR Ranges:** Prevents IP address conflicts, which are critical for seamless communication in a hybrid environment. This ensures unambiguous routing and reduces the risk of downtime.
- **Cloud Interconnect:** Provides high-bandwidth, low-latency, and private connectivity between your on-premises data center and Google Cloud. This is ideal for heavy data transfer and mission-critical workloads.
- **Scalability and Future-Proofing:** This approach provides a solid foundation for future expansion and integration of additional services without the complexities introduced by overlapping IP addresses.

**Why Other Options Are Less Optimal**

- **A. Default VPC and Cloud VPN:** While Cloud VPN is viable, the default VPC has limited subnet customization flexibility. You would likely need a custom VPC for better control. Choosing Cloud VPN also limits your bandwidth compared to Cloud Interconnect.
- **B. Custom Auto-Mode VPC and Cloud VPN:** Auto-mode VPCs assign subnets automatically, potentially increasing the risk of IP address conflicts with your on-premises setup.
- **C. Overlapping CIDRs and Cloud Interconnect:** Creates IP routing ambiguities and management headaches. While technically possible to overcome, it's prone to configuration errors and less maintainable in the long run.

**Important Considerations:**

- **Careful IP Planning:** Design your VPC subnet ranges with enough space for future growth, keeping your on-premises network(s) in mind.
- **Redundancy:** For high-availability, consider multiple Cloud Interconnect links for failover scenarios.

Hint - [https://cloud.google.com/vpc/docs/vpc#ip-ranges](https://cloud.google.com/vpc/docs/vpc#ip-ranges)

---

## Question 65

*Domain 1: Designing and Planning a Cloud Solution Architecture*

**Your company aims to monitor the presence of individuals in meeting rooms reserved for scheduled meetings. There are 1000 meeting rooms spread across 5 offices on 3 continents, each equipped with a motion sensor reporting its status every second. How should you design a solution to meet the data ingestion requirements of this sensor network, considering the possibility of inconsistent device connectivity?**

- [ ] A. Establish a persistent connection from each device to a Compute Engine instance and transmit messages to a custom application.
- [ ] B. Enable devices to check connectivity to Cloud SQL and periodically insert the latest messages into a device-specific table.
- [x] C. Configure devices to verify connectivity to Pub/Sub and regularly publish the latest messages to a shared topic for all devices.
- [ ] D. Implement a persistent connection from devices to an App Engine application with Cloud Endpoints, which processes and stores messages in Datastore.

### Explanation

**C. Configure devices to verify connectivity to Pub/Sub and regularly publish the latest messages to a shared topic for all devices.**

Here's why this approach is superior:

- **Scalability:** Pub/Sub is a managed messaging service designed to handle large volumes of data with high throughput. It can easily accommodate the 1000 rooms and their frequent sensor updates.
- **Decoupled Architecture:** Pub/Sub decouples data producers (sensors) from downstream processing, improving the system's resilience to connectivity issues and uneven data rates from different rooms.
- **Handling Connectivity Issues:** Pub/Sub's buffering and asynchronous nature tolerate inconsistent connectivity. Sensors can publish messages when connectivity is available, ensuring data isn't lost.
- **Global Reach:** Pub/Sub seamlessly operates across multiple continents, simplifying data ingestion from geographically distributed meeting rooms.

**Why Other Options are Less Optimal:**

- **A. Compute Engine Persistence:** Managing persistent connections from 1000 devices to a Compute Engine instance introduces scaling challenges and a higher risk of downtime if the instance fails.
- **B. Cloud SQL:** Cloud SQL is a database, not ideal for real-time message ingestion. Periodic inserts might cause delays in data analysis.
- **D. App Engine and Datastore:** While feasible, this approach requires more custom application logic for message handling and might not scale as gracefully as Pub/Sub.

**Additional Considerations:**

- **Downstream Processing:** Choose a suitable technology (e.g., Dataflow, Cloud Functions) to subscribe to the Pub/Sub topic for real-time or batch processing of the motion sensor data.
- **Data Retention:** Define clear data retention policies within Pub/Sub based on how long you need to store the sensor data.

References:

[https://cloud.google.com/sql/](https://cloud.google.com/sql/)

[https://cloud.google.com/pubsub/](https://cloud.google.com/pubsub/)

---

## Question 66

*Domain 1: Designing and Planning a Cloud Solution Architecture*

Your company runs a large-scale e-commerce application on Google Cloud, serving millions of global customers. The application consists of multiple microservices running on **Google Kubernetes Engine (GKE)** with an **Istio service mesh** for traffic management. The backend is powered by **Cloud Spanner** for transactional consistency, and **BigQuery** for analytics.

Recently, users in different regions have reported **inconsistent and stale data** when querying order details immediately after placing an order. You suspect this is due to eventual consistency issues.

**What is the MOST effective way to ensure strong consistency while maintaining high availability across multiple regions?**

- [ ] A) Configure **Cloud CDN** to cache database responses and reduce load on Cloud Spanner.
- [x] B) Use **Cloud Spanner’s strong read** with **leader placement strategy** in the region closest to the majority of users.
- [ ] C) Replace **Cloud Spanner with Bigtable**, as Bigtable offers low-latency reads and writes across regions.
- [ ] D) Deploy **Memorystore (Redis) for caching**, ensuring all read operations hit the cache before going to Cloud Spanner.

### Explanation

**Answer – Option B: Configure Cloud Spanner clients to issue *strong reads* and set the database’s *default-leader region* to the region that serves most of your traffic.**

Why B solves the problem

• **Strong reads guarantee freshness.** A strong read in Cloud Spanner “is guaranteed to see all data that has been committed up until the start of the read,” eliminating the stale results your users are seeing. [Google Cloud](https://cloud.google.com/spanner/docs/reads?utm_source=chatgpt.com)

• **Leader placement keeps the latency low while preserving external consistency.** By moving the Paxos leader replicas to the primary-traffic region, both writes and strong reads avoid a cross-continent round-trip, yet Spanner continues to synchronously replicate across the other regions for 5-nines availability. [Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/reduce-latency-with-cloud-spanner-multi-region-leader-placement/?utm_source=chatgpt.com) | [Google Cloud](https://cloud.google.com/spanner/docs/replication?utm_source=chatgpt.com)

Why the other choices are not appropriate

**A – Cloud CDN**
Cloud CDN is designed for caching *static* or publicly cacheable HTTP content. Caching per-order database responses would either violate cacheability rules or require aggressive invalidations, adding the very staleness you are trying to remove. [Google Cloud](https://cloud.google.com/cdn/docs/caching?utm_source=chatgpt.com)

**C – Bigtable**
Cloud Bigtable replication trades strong consistency for very low latency; reads from clusters that did not process the write can be seconds (or longer) behind. Switching would re-introduce eventual consistency rather than fix it. [Google Cloud](https://cloud.google.com/bigtable/docs/replication-overview?utm_source=chatgpt.com)

**D – Memorystore (Redis)**
Memorystore is a single-region cache; any replicas you build yourself are asynchronous and provide no transactional guarantees. Reads served from Redis in one region could easily be stale relative to writes that were just committed in another. [Google Cloud](https://cloud.google.com/memorystore/docs/redis/regions?utm_source=chatgpt.com)

By continuing to use Cloud Spanner but enforcing strong reads and thoughtful leader placement, you keep global high availability while ensuring every customer sees their newly placed order immediately.

---
