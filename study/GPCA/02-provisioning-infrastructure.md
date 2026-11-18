# Domain 2 — Managing and Provisioning a Solution Infrastructure

68 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q1

**Your organization is planning a significant update to its API to enhance the developer experience. They need to ensure that the previous version of the API remains accessible and deployable while enabling new customers and testers to explore the updated API. Additionally, they want to retain the existing SSL and DNS records to serve both API versions. What is the best approach to achieve this?**

- A. Set up a new load balancer specifically for the updated API.
- B. Modify existing clients to direct traffic to a different endpoint for the new API.
- C. Configure the existing API to route traffic to the new API based on the request path.
- D. Implement separate backend pools behind the load balancer for different API paths.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Implement separate backend pools behind the load balancer for different API paths.

**Correct Answer:**

**D. Implement separate backend pools behind the load balancer for different API paths.**

**Explanation:**

The best approach is to use **separate backend pools** behind a single load balancer that directs traffic based on API paths. This solution ensures that:

- Both the old and new API versions remain **accessible** and **deployable** without disrupting existing customers.
- Existing **SSL certificates** and **DNS records** remain unchanged, as traffic is still routed through the same entry point.
- A seamless transition is provided for **new customers and testers** without modifying existing client applications.
- Traffic can be routed based on specific **path rules** using **Google Cloud HTTP(S) Load Balancer**, allowing selective access to API versions.

Google Cloud HTTP(S) Load Balancer allows defining **backend services with different URL path-based routing**. This lets you configure the load balancer to route requests based on API versions (e.g., `/v1/*` to the old API and `/v2/*` to the new API).

**Supporting Documentation:**

- Google Cloud HTTP(S) Load Balancer - Path-based routing:
  **https://cloud.google.com/load-balancing/docs/https/traffic-management#path_rule_examples**

**Why Other Options Are Incorrect:**

**A. Set up a new load balancer specifically for the updated API.**

❌ **Incorrect** – Setting up a new load balancer means:

- You **need a new DNS record and SSL certificate**, which the requirement explicitly says should be retained.
- It introduces **unnecessary complexity** when the existing load balancer can handle both API versions using **backend pools and URL-based routing**.

✅ **Reference:**

- Google Cloud Load Balancing Best Practices:
  **https://cloud.google.com/load-balancing/docs/best-practices**

**B. Modify existing clients to direct traffic to a different endpoint for the new API.**

❌ **Incorrect** – This approach requires **client-side changes**, which:

- **Breaks backward compatibility** for existing customers.
- Does not allow seamless testing of the new API for new customers while keeping the old API operational.
- The requirement explicitly states that **previous API versions must remain accessible without modification**.

✅ **Reference:**

- API versioning strategies in Google Cloud:
  **https://cloud.google.com/endpoints/docs/openapi/versioning-an-api**

**C. Configure the existing API to route traffic to the new API based on the request path.**

❌ **Incorrect** – This approach suggests modifying the **existing API**, but:

- It **adds complexity and dependencies** within the API code rather than handling it at the infrastructure level.
- API applications should not be responsible for **traffic routing**, as this is best handled by the **load balancer**.
- The requirement is to have **both API versions independently deployable**, which this solution does not fully support.

✅ **Reference:**

- Traffic management with Load Balancers:
  **https://cloud.google.com/load-balancing/docs/https/traffic-management**

**Conclusion:**

The best solution is **Option D**: **Implement separate backend pools behind the load balancer for different API paths**. This approach:

- Retains existing **SSL and DNS settings**.
- Ensures both **API versions remain accessible** without modifying client configurations.
- Allows controlled traffic routing to the **new API version** for new customers and testers.
- Uses Google Cloud **HTTP(S) Load Balancer with URL-based routing**, a recommended best practice.

📌 **Final Reference:**
**https://cloud.google.com/load-balancing/docs/https/traffic-management#path_rule_examples**

</details>

---

### Exam 1 · Q8

**You have set up an autoscaling instance group to handle web traffic for an upcoming launch. After configuring the instance group as a backend service for an HTTP(S) load balancer, you notice that virtual machine (VM) instances are terminating and relaunching every minute. The instances do not have public IP addresses. You have confirmed that each instance returns the expected web response using the curl command. To ensure the backend is configured correctly, what should you do?**

- A. Verify that a firewall rule exists to allow source traffic on HTTP/HTTPS to reach the load balancer.
- B. Assign a public IP to each instance and configure a firewall rule to allow the load balancer to reach the instance’s public IP.
- C. Ensure that a firewall rule is in place to allow load balancer health checks to reach the instances in the instance group.
- D. Tag each instance with the load balancer’s name and create a firewall rule allowing traffic from the load balancer to the instance tag as the destination.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Ensure that a firewall rule is in place to allow load balancer health checks to reach the instances in the instance group.

**Correct Answer:**

**C. Ensure that a firewall rule is in place to allow load balancer health checks to reach the instances in the instance group.**

**Explanation:**

The behavior of VM instances **terminating and relaunching every minute** suggests that the **load balancer’s health checks are failing**, causing the autoscaler to **remove and replace** instances.

- Google Cloud **HTTP(S) Load Balancer** relies on **health checks** to determine whether backend instances are **healthy**.
- If the health check **fails**, the instance is marked as **unhealthy** and is replaced by the autoscaler.
- Since the VMs **do not have public IPs**, the **load balancer’s health checks must reach the private IPs** of the backend instances.
- **A firewall rule must allow ingress traffic from the load balancer's health check IP ranges** to the backend instances on the **configured health check port (e.g., TCP:80 or TCP:443).**

✅ **Fix:** Create a firewall rule to allow **Google Cloud health check probes** to access the backend instances.

✅ **Supporting Documentation:**

- **Firewall Rules for Load Balancer Health Checks:**
  **https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules**
- **Health Check Configuration for Load Balancers:**
  **https://cloud.google.com/load-balancing/docs/health-checks**

**Why Other Options Are Incorrect:**

**A. Verify that a firewall rule exists to allow source traffic on HTTP/HTTPS to reach the load balancer.** ❌

- **Incorrect** because this rule applies to **external users accessing the web service** and **not** to the load balancer's **health checks**.
- The **load balancer itself does not directly use HTTP/HTTPS to determine instance health**; it relies on **dedicated health check probes**.

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/https#firewalls**

**B. Assign a public IP to each instance and configure a firewall rule to allow the load balancer to reach the instance’s public IP.** ❌

- **Incorrect** because:
  - The Google Cloud HTTP(S) Load Balancer uses **internal IPs** for backend instance communication.
  - Backend instances **do not require public IPs** for load balancer health checks or data traffic.
  - Google Cloud best practices **recommend using private IPs** for security and cost efficiency.

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/https#backend_services**

**D. Tag each instance with the load balancer’s name and create a firewall rule allowing traffic from the load balancer to the instance tag as the destination.** ❌

- **Incorrect** because:
  - **Instance tags do not control load balancer traffic routing.**
  - The **correct firewall rule must specifically allow traffic from Google’s health check IP ranges**, not just from the load balancer.
  - **Health checks are conducted by Google’s infrastructure, not the load balancer itself.**

✅ **Reference:**

- **https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules**

**Conclusion:**

The best way to **prevent instances from terminating and relaunching** is to ensure **Google Cloud health check traffic can reach the backend instances** by:

1. **Creating a firewall rule** to allow health check IP ranges to access the instances on the appropriate health check port.
2. **Confirming that the health check settings** (protocol, port, and path) match the actual instance configuration.

📌 **Final Reference:**
**https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules**

</details>

---

### Exam 1 · Q13

**A production database virtual machine on Google Compute Engine uses an ext4-formatted persistent disk for storing data files. The database is approaching its storage limit. What is the best way to resolve this issue while minimizing downtime?**

- A. Increase the size of the persistent disk in the Cloud Platform Console, then use the `resize2fs` command in Linux.
- B. Shut down the virtual machine, increase the persistent disk size in the Cloud Platform Console, and then restart the virtual machine.
- C. Increase the size of the persistent disk in the Cloud Platform Console and verify the newly allocated space using the `fdisk` command in Linux.
- D. Create a new persistent disk in the Cloud Platform Console, attach it to the virtual machine, format and mount it, and update the database configuration to store files on the new disk.
- E. Create a snapshot of the persistent disk in the Cloud Platform Console, restore the snapshot to a new, larger disk, unmount the old disk, mount the new disk, and restart the database service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Increase the size of the persistent disk in the Cloud Platform Console, then use the `resize2fs` command in Linux.

**Correct Answer:**

**A. Increase the size of the persistent disk in the Cloud Platform Console, then use the `resize2fs` command in Linux.**

**Explanation:**

The **best approach** to **increase storage while minimizing downtime** is:

1. **Resize the persistent disk** using the Google Cloud Console or `gcloud compute disks resize`.
2. **Expand the filesystem online using** `resize2fs` (for ext4 filesystems) without needing to unmount the disk or restart the VM.

✅ **Why this works best?**

- Google Cloud Persistent Disks **can be resized dynamically** without VM downtime.
- The **Linux `resize2fs` command** allows resizing an **ext4 filesystem online** without unmounting.
- **No need to restart the VM or database**, ensuring **minimal disruption** to production services.

✅ **Supporting Documentation:**

- **Resizing Persistent Disks on Compute Engine:**
  **https://cloud.google.com/compute/docs/disks/resize-persistent-disk**
- **Resizing ext4 partitions with `resize2fs`:**
  **https://man7.org/linux/man-pages/man8/resize2fs.8.html**

**Why Other Options Are Incorrect:**

**B. Shut down the virtual machine, increase the persistent disk size in the Cloud Platform Console, and then restart the virtual machine.** ❌

- **Incorrect because shutting down the VM is unnecessary.**
- Persistent Disks **can be resized while the VM is running**, and `resize2fs` can be run **without downtime**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/resize-persistent-disk**

**C. Increase the size of the persistent disk in the Cloud Platform Console and verify the newly allocated space using the fdisk command in Linux.** ❌

- **Incorrect because `fdisk` is used for partition management, not filesystem resizing.**
- For **ext4 filesystems,** `resize2fs` is the correct tool to extend the filesystem after resizing the disk.

✅ **Reference:**

- **https://linux.die.net/man/8/fdisk**

**D. Create a new persistent disk in the Cloud Platform Console, attach it to the virtual machine, format and mount it, and update the database configuration to store files on the new disk.** ❌

- **Not the most efficient solution** because:
  - It requires **database reconfiguration**, increasing complexity.
  - Existing data remains on the old disk, **potentially requiring data migration**.
  - A **simpler, non-disruptive** approach is to **resize the existing disk**.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/add-persistent-disk**

**E. Create a snapshot of the persistent disk in the Cloud Platform Console, restore the snapshot to a new, larger disk, unmount the old disk, mount the new disk, and restart the database service.** ❌

- **Not the best approach** because:
  - **Unnecessary downtime** due to snapshot restoration and remounting.
  - **More complex than simply resizing the existing disk**.
  - **Snapshots are primarily for backups** rather than live disk expansion.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/disks/create-snapshots**

**Conclusion:**

The best way to expand storage **without downtime** is:

1. **Increase the size of the persistent disk** in Google Cloud Console (`gcloud compute disks resize`).
2. **Use** `resize2fs` to extend the ext4 filesystem **without unmounting the disk or restarting the VM**.

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/disks/resize-persistent-disk**

</details>

---

### Exam 1 · Q16

**You need to implement a solution to automatically delete backup files older than 90 days from your Cloud Storage bucket while optimizing ongoing storage costs. What should you do?**

- A. Define a **lifecycle management rule** in **XML** and apply it to the bucket using `gsutil`.
- B. Define a **lifecycle management rule** in **JSON** and apply it to the bucket using `gsutil`.
- C. Schedule a **cron job** that runs a script using `gsutil ls -lr gs://backups/**` to find and delete files older than 90 days.
- D. Schedule a **cron job** that runs a script using `gsutil ls -l gs://backups/**` to find and delete files older than 90 days.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Define a **lifecycle management rule** in **JSON** and apply it to the bucket using `gsutil`.

**Correct Answer:**

**B. Define a lifecycle management rule in JSON and apply it to the bucket using gsutil.**

**Explanation:**

Google Cloud Storage **Lifecycle Management** allows you to **automate the deletion of backup files older than 90 days**, ensuring:

- **Automatic cleanup** without manual intervention.
- **Optimized storage costs** by reducing long-term storage usage.
- **Policy-based enforcement** that does not require additional scripts or cron jobs.

**Steps to Implement:**

1. Create a **JSON lifecycle policy**:
  ```
  {  "rule": [    {      "action": {"type": "Delete"},      "condition": {"age": 90}    }  ]}
  ```
2. Apply the policy to the bucket using **gsutil**:
  ```
  gsutil lifecycle set lifecycle.json gs://your-bucket-name
  ```
3. Verify the policy:
  ```
  gsutil lifecycle get gs://your-bucket-name
  ```

✅ **Supporting Documentation:**

- **Google Cloud Storage Lifecycle Management**
  **https://cloud.google.com/storage/docs/lifecycle**
- **Using gsutil for lifecycle policies**
  **https://cloud.google.com/storage/docs/gsutil/commands/lifecycle**

**Why Other Options Are Incorrect:**

**A. Define a lifecycle management rule in XML and apply it to the bucket using gsutil.** ❌

- `gsutil lifecycle set` (and today `gcloud storage buckets update --lifecycle-file`) takes a **JSON** file. XML lifecycle documents exist only for the Cloud Storage XML API, not for these tools.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/lifecycle#configuration**

**C. Schedule a cron job that runs a script using `gsutil ls -lr gs://backups/**` to find and delete files older than 90 days.** ❌

- **Inefficient and unnecessary** when **Cloud Storage lifecycle policies** can handle this automatically.
- Running a script **adds operational overhead** and **increases potential failure points**.
- **Recursive listing (`-lr`) is redundant**, as `gsutil` does not require recursion for finding objects.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/gsutil/commands/ls**

**D. Schedule a cron job that runs a script using `gsutil ls -l gs://backups/**` to find and delete files older than 90 days.** ❌

- Similar to **Option C**, this **manual script approach** is **unnecessary**.
- **Lifecycle rules** are **more reliable** than cron-based deletion scripts.

✅ **Reference:**

- **https://cloud.google.com/storage/docs/lifecycle**

**Conclusion:**

The best approach is **B. Define a lifecycle management rule in JSON and apply it to the bucket using gsutil**, as it:

- **Automates deletion** of files older than 90 days.
- **Optimizes storage costs** without manual intervention.
- **Follows Google Cloud best practices** for object lifecycle management.

📌 **Final Reference:**
**https://cloud.google.com/storage/docs/lifecycle**

**⚠️ Note:** `gsutil` is now legacy; the current command is `gcloud storage buckets update gs://BUCKET --lifecycle-file=FILE.json`. The answer (a JSON lifecycle rule with `age: 90` and a Delete action) is unchanged.

</details>

---

### Exam 1 · Q18

**The database administration team needs your assistance in improving the performance of their new MySQL database server running on Google Compute Engine. The database is used for importing and normalizing performance statistics and is hosted on a Debian Linux virtual machine with an n1-standard-8 configuration and 80 GB of SSD persistent disk. What should they modify to enhance performance?**

- A. Increase the virtual machine’s memory to **64 GB**.
- B. Create a new virtual machine running **PostgreSQL** instead of MySQL.
- C. Dynamically resize the **SSD persistent disk** to **500 GB**.
- D. Migrate the performance metrics warehouse to **BigQuery**.
- E. Optimize batch jobs to use **bulk inserts** into the database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Dynamically resize the **SSD persistent disk** to **500 GB**. **|** E. Optimize batch jobs to use **bulk inserts** into the database.

**Correct Answer:**

**C. Dynamically resize the SSD persistent disk to 500 GB.**
**E. Optimize batch jobs to use bulk inserts into the database.**

**Explanation:**

To improve **MySQL performance on Google Compute Engine**, two key optimizations are required:

1. **Resize the SSD persistent disk to 500 GB (`Option C`)**
  - **Google SSD persistent disks offer higher IOPS with increased disk size.**
  - SSD persistent disk IOPS are a 6,000 baseline plus 30 per GB: an **80 GB disk gets about 8,400 IOPS**, a **500 GB disk about 21,000 IOPS** (both capped by the VM's own limit), significantly improving **read/write performance**.
  - **MySQL benefits from higher disk throughput**, especially for **large-scale data imports and query processing**.
  - Google allows **dynamic disk resizing without downtime**, meaning this change can be applied immediately.
  ✅ **Supporting Documentation:**
  - **Google Cloud SSD Persistent Disk Performance**
    **https://cloud.google.com/compute/docs/disks/performance**
  - **Resizing persistent disks in Google Cloud**
    **https://cloud.google.com/compute/docs/disks/resize-persistent-disk**
2. **Optimize batch jobs to use bulk inserts into the database (`Option E`)**
  - **Bulk inserts reduce the number of disk writes** and **minimize transaction overhead**, leading to **faster import and normalization of performance data**.
  - **MySQL performs better when data is inserted in large batches** instead of multiple individual insert statements.
  - Using `INSERT ... VALUES (...), (...)` or `LOAD DATA INFILE` significantly improves insert speeds.
  ✅ **Supporting Documentation:**
  - **Optimizing MySQL Performance for Batch Inserts**
    [**https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html**](https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html)
  - **MySQL Bulk Insert Best Practices**
    **https://cloud.google.com/sql/docs/mysql/import-export/importing**

**Why Other Options Are Incorrect:**

**A. Increase the virtual machine’s memory to 64 GB.** ❌

- While **more memory can improve query caching**, this is **not the primary bottleneck** in this case.
- The **current n1-standard-8 VM** already provides **30 GB RAM**, which is sufficient for MySQL **unless monitoring indicates high memory usage**.
- **Storage and query optimization are more impactful** for performance improvements in this scenario.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/machine-types**

**B. Create a new virtual machine running PostgreSQL instead of MySQL.** ❌

- **Migrating to PostgreSQL does not inherently improve performance**—both databases have similar capabilities for large-scale data ingestion.
- Migration requires **significant rework**, which is **not a practical solution for immediate performance improvement**.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/postgres**

**D. Migrate the performance metrics warehouse to BigQuery.** ❌

- **BigQuery is optimized for analytical queries, not for transactional workloads like MySQL.**
- If the database is **used for normalizing transactional data**, BigQuery is **not a direct replacement**—instead, **MySQL tuning is required**.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/introduction**

**Conclusion:**

To **improve MySQL performance** on Google Compute Engine:

1. **Increase the SSD persistent disk size to 500 GB (`Option C`)** for better **IOPS and disk performance**.
2. **Optimize batch jobs to use bulk inserts (`Option E`)** to **minimize transaction overhead** and **speed up data imports**.

📌 **Final References:**

- **https://cloud.google.com/compute/docs/disks/performance**
- [**https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html**](https://dev.mysql.com/doc/refman/8.0/en/insert-optimization.html)

</details>

---

### Exam 1 · Q25

**Your company has decided to create a **backup replica** of its **on-premises user authentication PostgreSQL database** on **Google Cloud Platform**. The database is **4 TB in size**, and **large updates occur frequently**. Additionally, **replication must occur over private address space communication**. Which networking approach should you use?**

- A. **Google Cloud Dedicated Interconnect**.
- B. **Google Cloud VPN** connected to the on-premises network.
- C. A **NAT and TLS translation gateway** installed on-premises.
- D. A **Google Compute Engine instance** with a VPN server installed, connected to the on-premises network.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Google Cloud Dedicated Interconnect**.

**Correct Answer:**

**A. Google Cloud Dedicated Interconnect.**

**Explanation:**

To **replicate a 4 TB PostgreSQL database with frequent large updates** over **private address space**, the best approach is **Google Cloud Dedicated Interconnect** because:

✅ **Key Benefits of Dedicated Interconnect:**

- **High-bandwidth, low-latency, and private network connectivity** (up to **100 Gbps**) between on-premises and Google Cloud.
- **Ensures private communication** for secure database replication **without exposing traffic to the public internet**.
- **Minimizes replication lag**, ensuring near real-time synchronization of large updates.
- **More reliable and faster** than VPN-based solutions, which are **limited to 3 Gbps per tunnel**.

✅ **Supporting Documentation:**

- **Google Cloud Dedicated Interconnect Overview:**
  **https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**
- **Best Practices for Database Replication over Cloud Interconnect:**
  **https://cloud.google.com/architecture/database-migration-best-practices**

**Why Other Options Are Incorrect:**

**B. Google Cloud VPN connected to the on-premises network.** ❌

- **Not ideal for a 4 TB database with large frequent updates** due to:
  - **Lower bandwidth limits (3 Gbps per VPN tunnel)** compared to Dedicated Interconnect (up to 100 Gbps).
  - **Higher latency** due to routing over the **public internet** instead of a **private, dedicated network**.
- **Best suited for smaller, less latency-sensitive workloads**, not large-scale database replication.

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn**

**C. A NAT and TLS translation gateway installed on-premises.** ❌

- **Unnecessary complexity** for this use case.
- **NAT (Network Address Translation)** is not required because Dedicated Interconnect or VPN provides **private IP connectivity**.
- **TLS encryption is already built into PostgreSQL replication**, making a separate TLS translation gateway redundant.

✅ **Reference:**

- [**https://www.postgresql.org/docs/current/protocol-overview.html**](https://www.postgresql.org/docs/current/protocol-overview.html)

**D. A Google Compute Engine instance with a VPN server installed, connected to the on-premises network.** ❌

- **Inferior to Google Cloud VPN**, which is a **fully managed service** with better reliability and performance.
- **Manually setting up a VPN server** on Compute Engine adds **operational overhead** without performance benefits.
- **Limited bandwidth (~3 Gbps per VPN tunnel), unsuitable for large database replication.**

✅ **Reference:**

- **https://cloud.google.com/vpn/docs/concepts/overview**

**Conclusion:**

The best approach is **A. Google Cloud Dedicated Interconnect**, as it:

- **Provides high-speed, private connectivity (up to 100 Gbps).**
- **Ensures low-latency, reliable replication of a 4 TB PostgreSQL database.**
- **Avoids the limitations of VPN-based solutions.**

📌 **Final Reference:**
**https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

</details>

---

### Exam 1 · Q30

**You have deployed several preemptible Linux virtual machine instances on Google Compute Engine. To ensure that your application properly shuts down before the virtual machines are preempted, what should you do?**

- A. Create a **shutdown script** named `k99.shutdown` in the `/etc/rc.6.d/` directory.
- B. Register a **shutdown script** as an **xinetd service** in Linux and configure a **Stackdriver endpoint check** to call the service.
- C. Create a **shutdown script** and set it as the value for a **new metadata entry** with the key `shutdown-script` in the **Cloud Console** when creating the instance.
- D. Register a **shutdown script** as an **xinetd service** in Linux and use the `gcloud compute instances add-metadata` command to specify the service URL as the value for a **new metadata entry** with the key `shutdown-script-url`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a **shutdown script** and set it as the value for a **new metadata entry** with the key `shutdown-script` in the **Cloud Console** when creating the instance.

**Correct Answer:**

**C. Create a shutdown script and set it as the value for a new metadata entry with the key `shutdown-script` in the Cloud Console when creating the instance.**

**Explanation:**

Preemptible **Google Compute Engine (GCE) instances** can be **terminated at any time** by Google Cloud. To ensure that an application **properly shuts down** before preemption:

✅ **Best Approach: Use the `shutdown-script` Metadata Key**

- Google Cloud allows configuring **shutdown scripts via instance metadata**.
- These scripts **execute automatically when a VM is preempted**, ensuring **graceful shutdown**.
- The script should be stored as a **custom metadata key** (`shutdown-script`) and **can include commands to flush logs, close database connections, or gracefully terminate services**.

**Example Implementation:**

1. **Create a shutdown script (e.g., `shutdown.sh`)**:
  ```
  #!/bin/bashecho "Shutting down gracefully..." >> /var/log/shutdown.logsystemctl stop my-app.servicesync
  ```
2. **Set the script in the instance metadata (`shutdown-script` key):**
  ```
  gcloud compute instances add-metadata my-instance \    --metadata shutdown-script="$(cat shutdown.sh)"
  ```

✅ **Supporting Documentation:**

- **Shutdown Scripts in Compute Engine:**
  **https://cloud.google.com/compute/docs/shutdownscript**

**Why Other Options Are Incorrect:**

**A. Create a shutdown script named `k99.shutdown` in the `/etc/rc.6.d/` directory.** ❌

- **Incorrect because modern Linux systems use `systemd`, not** `SysVinit`, meaning scripts in `/etc/rc.6.d/` **may not run on all distributions**.
- **Google Cloud metadata-based shutdown scripts are a more reliable approach.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/instances/startup-scripts/linux**

**B. Register a shutdown script as an `xinetd` service in Linux and configure a Stackdriver endpoint check to call the service.** ❌

- **xinetd is a legacy daemon for managing network services**—it is **not needed for handling shutdown events**.
- **Stackdriver Monitoring (now Cloud Monitoring) is used for metrics/logging, not triggering shutdown scripts.**

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs**

**D. Register a shutdown script as an `xinetd` service in Linux and use `gcloud compute instances add-metadata` to specify the service URL as the value for `shutdown-script-url`.** ❌

- **Similar to Option B, xinetd is unrelated to shutdown script execution.**
- **The correct metadata key is `shutdown-script`, not `shutdown-script-url`.**

✅ **Reference:**

- **https://cloud.google.com/compute/docs/shutdownscript**

**Conclusion:**

The best solution is **C. Use the `shutdown-script` metadata key**, as it:

- **Executes automatically before preemption.**
- **Allows clean shutdown of applications and services.**
- **Does not rely on outdated or complex mechanisms.**

📌 **Final Reference:**
**https://cloud.google.com/compute/docs/shutdownscript**

**⚠️ Note:** Preemptible VMs have been superseded by **Spot VMs**. The answer still holds: put the script in the `shutdown-script` metadata key. It gets about 30 seconds, best effort, before the VM stops.

</details>

---

### Exam 1 · Q31

**Your organization has a 3-tier web application deployed within the same network on Google Cloud Platform. Each tier—web, API, and database—scales independently. The network traffic should flow from the web tier to the API tier, and then to the database tier, ensuring that traffic does not flow directly between the web and database tiers.**

**How should you configure the network to enforce this traffic flow?**

- A. Assign each tier to a **different subnetwork**.
- B. Configure **software-based firewalls** on individual virtual machines (VMs).
- C. Use **tags** for each tier and configure **routes** to enforce the desired traffic flow.
- D. Use **tags** for each tier and configure **firewall rules** to enforce the desired traffic flow.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use **tags** for each tier and configure **firewall rules** to enforce the desired traffic flow.

**Correct Answer:**

**D. Use tags for each tier and configure firewall rules to enforce the desired traffic flow.**

**Explanation:**

To **enforce controlled traffic flow** between the **web, API, and database tiers**, **firewall rules** should be used. In Google Cloud, firewall rules can be applied based on **network tags**, ensuring:

✅ **Why Use Firewall Rules with Tags?**

- **Network tags allow easy grouping of instances** based on function (e.g., `web-tier`, `api-tier`, `db-tier`).
- **Firewall rules restrict traffic between tiers**, ensuring that:
  - **Web tier can only communicate with API tier**.
  - **API tier can communicate with both web and database tiers**.
  - **Database tier only accepts connections from the API tier**.
- **More scalable and manageable** than manual instance-based firewall rules.

**Implementation Steps:**

1. **Assign network tags to instances**:
  - Web instances → `web-tier`
  - API instances → `api-tier`
  - Database instances → `db-tier`
2. **Create firewall rules:**
  - **Allow traffic from `web-tier` →** `api-tier`:
    ```
    gcloud compute firewall-rules create allow-web-to-api \    --direction=INGRESS --action=ALLOW --priority=1000 \    --source-tags=web-tier --target-tags=api-tier \    --rules=tcp:443,tcp:80
    ```
  - **Allow traffic from `api-tier` →** `db-tier`:
    ```
    gcloud compute firewall-rules create allow-api-to-db \    --direction=INGRESS --action=ALLOW --priority=1000 \    --source-tags=api-tier --target-tags=db-tier \    --rules=tcp:5432
    ```
  - **Deny direct traffic from `web-tier` →** `db-tier`:
    ```
    gcloud compute firewall-rules create deny-web-to-db \    --direction=INGRESS --action=DENY --priority=900 \    --source-tags=web-tier --target-tags=db-tier \    --rules=tcp:5432
    ```

✅ **Supporting Documentation:**

- **Firewall Rules in Google Cloud:**
  **https://cloud.google.com/vpc/docs/firewalls**
- **Using Tags in Firewall Rules:**
  **https://cloud.google.com/vpc/docs/firewalls#network-tags**

**Why Other Options Are Incorrect:**

**A. Assign each tier to a different subnetwork.** ❌

- **Subnetworks define IP ranges but do not enforce security policies.**
- **Without firewall rules**, instances in separate subnets can still communicate freely.
- **Subnet segmentation alone does not restrict traffic flow.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/subnets**

**B. Configure software-based firewalls on individual virtual machines (VMs).** ❌

- **Managing firewalls on each VM is complex and not scalable** for large deployments.
- **Google Cloud firewall rules apply at the VPC level**, making VM-based firewalls unnecessary.
- **More error-prone and difficult to maintain** than centrally managed firewall rules.

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/firewalls**

**C. Use tags for each tier and configure routes to enforce the desired traffic flow.** ❌

- **Routes control how traffic is forwarded, but they do not enforce security restrictions.**
- **Firewall rules, not routes, define which traffic is allowed or denied.**
- **A route cannot block or enforce directional traffic flows.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/routes**

**Conclusion:**

The best solution is **D. Use tags for each tier and configure firewall rules to enforce the desired traffic flow**, because:

- **Firewall rules enforce traffic control between tiers.**
- **Tags provide a scalable and flexible way to manage security policies.**
- **This ensures that the web tier only communicates with the API tier, and the database remains isolated.**

📌 **Final Reference:**
**https://cloud.google.com/vpc/docs/firewalls#network-tags**

</details>

---

### Exam 1 · Q37

**As part of their disaster recovery plan, your company is replicating a production MySQL database from an on-premises private data center to Google Cloud Platform (GCP) over a Google Cloud VPN connection. However, they are encountering latency issues and packet loss, which are disrupting replication.**

**What should they do?**

- A. Configure the replication to use **UDP**.
- B. Set up a **Google Cloud Dedicated Interconnect**.
- C. Perform a **daily database restore** using **Google Cloud SQL**.
- D. Add **additional VPN connections** and configure **load balancing** between them.
- E. Send the **replicated transactions** to **Google Cloud Pub/Sub**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Set up a **Google Cloud Dedicated Interconnect**.

**Correct Answer:**

✅ **B. Set up a Google Cloud Dedicated Interconnect.**

**Explanation:**

Since the **MySQL database replication is experiencing latency and packet loss over a Google Cloud VPN**, the best solution is to **upgrade to Google Cloud Dedicated Interconnect**.

✅ **Why Google Cloud Dedicated Interconnect?**

- **Provides a high-bandwidth, low-latency connection** between on-premises and Google Cloud.
- **Supports up to 100 Gbps of private connectivity**, reducing replication lag.
- **Bypasses the public internet**, eliminating packet loss and network congestion.
- **Ensures more reliable and predictable performance** compared to VPN.

**Implementation Steps:**

1. **Set up a Dedicated Interconnect connection** in the Google Cloud Console.
2. **Choose a colocation facility** for establishing a direct connection.
3. **Configure a VLAN attachment** to connect on-premises MySQL to Google Cloud SQL or a Compute Engine instance.
4. **Test and optimize MySQL replication performance** over the new connection.

✅ **Supporting Documentation:**

- **Google Cloud Dedicated Interconnect Overview:**
  **https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

**Why Other Options Are Incorrect?**

**A. Configure the replication to use UDP.** ❌

- **MySQL replication relies on TCP for reliable data transmission**, not UDP.
- **UDP does not guarantee delivery**, making it unsuitable for database replication.

✅ **Reference:**

- [**https://dev.mysql.com/doc/refman/8.0/en/replication.html**](https://dev.mysql.com/doc/refman/8.0/en/replication.html)

**C. Perform a daily database restore using Google Cloud SQL.** ❌

- **Not a real-time solution**—daily restores introduce **significant data lag**.
- **Replication ensures near-real-time sync**, whereas restores are periodic snapshots.

✅ **Reference:**

- **https://cloud.google.com/sql/docs/mysql/replication**

**D. Add additional VPN connections and configure load balancing between them.** ❌

- **VPN tunnels have a 3 Gbps per tunnel limit** and rely on **public internet traffic**, leading to potential congestion.
- **Adding multiple VPNs does not eliminate latency and packet loss**—Dedicated Interconnect is a better solution.

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies**

**E. Send the replicated transactions to Google Cloud Pub/Sub.** ❌

- **Pub/Sub is designed for event streaming, not for MySQL database replication.**
- **MySQL replication requires transaction consistency**, which Pub/Sub **does not guarantee**.

✅ **Reference:**

- **https://cloud.google.com/pubsub/docs/overview**

**Conclusion:**

The best solution is **B. Set up a Google Cloud Dedicated Interconnect**, because:

- **It reduces latency and packet loss** by providing a **direct private connection** to Google Cloud.
- **It supports high-speed replication** (up to 100 Gbps), improving database performance.
- **It eliminates dependency on the public internet**, ensuring reliable replication.

📌 **Final Reference:**
**https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

</details>

---

### Exam 1 · Q40

**You need to establish a **private connection** between your **Compute Engine instances** and your **on-premises data center** with a minimum bandwidth requirement of **20 Gbps**, following **Google-recommended best practices**. How should you set up the connection?**

- A. Create a **VPC** and connect it to the on-premises data center using **Dedicated Interconnect**.
- B. Create a **VPC** and connect it to the on-premises data center using a **single Cloud VPN**.
- C. Set up a **Cloud Content Delivery Network (Cloud CDN)** and connect it to the on-premises data center using **Dedicated Interconnect**.
- D. Set up a **Cloud Content Delivery Network (Cloud CDN)** and connect it to the on-premises data center using a **single Cloud VPN**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a **VPC** and connect it to the on-premises data center using **Dedicated Interconnect**.

**Correct Answer:**

✅ **A. Create a VPC and connect it to the on-premises data center using Dedicated Interconnect.**

**Explanation:**

To **establish a private connection between Compute Engine instances and an on-premises data center** with a **minimum bandwidth requirement of 20 Gbps**, the best approach is to use **Google Cloud Dedicated Interconnect**.

✅ **Why Dedicated Interconnect?**

- **Provides high-bandwidth private connectivity** (supports **10 Gbps and 100 Gbps connections**).
- **Bypasses the public internet**, ensuring **low latency and high reliability**.
- **Can be configured to provide an aggregated 20 Gbps link** (e.g., two 10 Gbps connections).
- **Supports hybrid cloud architecture**, ensuring **secure and direct access to on-prem resources**.

**Implementation Steps:**

1. **Provision Dedicated Interconnect** via the Google Cloud Console or `gcloud` CLI.
2. **Choose a colocation facility** where Google Cloud has an interconnect location.
3. **Set up VLAN attachments and BGP peering** to establish the private connection.
4. **Create a VPC in Google Cloud** and configure **routes to on-premises networks**.

✅ **Supporting Documentation:**

- **Dedicated Interconnect Overview:**
  **https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**
- **Choosing Between Cloud VPN and Interconnect:**
  **https://cloud.google.com/hybrid-connectivity/docs/interconnect-overview**

**Why Other Options Are Incorrect?**

**B. Create a VPC and connect it to the on-premises data center using a single Cloud VPN.** ❌

- **Cloud VPN has a maximum bandwidth limit of 3 Gbps per tunnel** (even with multiple tunnels, it’s **not ideal for 20 Gbps**).
- **Cloud VPN relies on the public internet**, which introduces **higher latency and potential packet loss**.
- **Not suitable for large-scale hybrid cloud architectures requiring high bandwidth.**

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies**

**C. Set up a Cloud Content Delivery Network (Cloud CDN) and connect it to the on-premises data center using Dedicated Interconnect.** ❌

- **Cloud CDN is for caching web content globally**, not for hybrid cloud networking.
- **CDN does not establish private connectivity**—it serves cached data from edge locations.
- **Dedicated Interconnect does not integrate with Cloud CDN** for hybrid connectivity.

✅ **Reference:**

- **https://cloud.google.com/cdn/docs/overview**

**D. Set up a Cloud Content Delivery Network (Cloud CDN) and connect it to the on-premises data center using a single Cloud VPN.** ❌

- **Cloud CDN is for optimizing web content delivery**, not for private hybrid networking.
- **Cloud VPN is limited to 3 Gbps per tunnel**, which is insufficient for 20 Gbps bandwidth needs.
- **Cloud VPN uses the public internet**, introducing reliability concerns for high-bandwidth workloads.

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies**

**Conclusion:**

The best solution is **A. Create a VPC and connect it to the on-premises data center using Dedicated Interconnect**, because:

- **It provides private, high-bandwidth (20 Gbps+) connectivity.**
- **It bypasses the public internet, ensuring low latency.**
- **It follows Google Cloud’s best practices for hybrid connectivity.**

📌 **Final Reference:**
**https://cloud.google.com/interconnect/docs/how-to/dedicated/overview**

</details>

---

### Exam 1 · Q47

**You are migrating an on-premises solution to Google Cloud in multiple phases. During the transition, you will use Cloud VPN to maintain connectivity between your on-premises systems and Google Cloud. You need to ensure that all on-premises systems remain reachable throughout the migration.**

**How should you configure networking in Google Cloud?**

- A. Use the **same IP range** on Google Cloud as you use on-premises.
- B. Use the **same IP range** on Google Cloud as on-premises for your **primary range**, and assign a **secondary range** that does **not overlap** with your on-premises range.
- C. Use an **IP range on Google Cloud that does not overlap** with your on-premises range.
- D. Use an **IP range on Google Cloud that does not overlap** with your on-premises range for the **primary range**, and configure a **secondary range that matches** your on-premises IP range.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use an **IP range on Google Cloud that does not overlap** with your on-premises range.

**Correct Answer:**

✅ **C. Use an IP range on Google Cloud that does not overlap with your on-premises range.**

**Explanation:**

When using **Cloud VPN** to maintain connectivity between **on-premises systems and Google Cloud**, **IP address overlap must be avoided** to prevent **routing conflicts** and **connectivity issues**.

✅ **Why Use a Non-Overlapping IP Range in Google Cloud?**

- **Cloud VPN requires distinct, non-overlapping IP ranges** for Google Cloud and on-premises networks to enable proper routing.
- **Overlapping IP ranges cause routing conflicts** because Cloud VPN cannot differentiate traffic between on-prem and Google Cloud.
- **Google-recommended hybrid networking best practice** is to assign **a unique CIDR block** to Google Cloud that does not exist in the on-prem network.

**Implementation Steps:**

1. **Determine your on-premises IP range** (e.g., `192.168.1.0/24`).
2. **Choose a distinct IP range for Google Cloud** (e.g., `10.10.0.0/16`) that does **not** overlap with on-prem.
3. **Configure Cloud VPN** to establish secure connectivity between Google Cloud and the on-prem network.
4. **Set up custom routes in VPC** to enable traffic between the two networks.

✅ **Supporting Documentation:**

- **Google Cloud VPN Overview:**
  **https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**
- **Avoiding Overlapping IP Ranges in Hybrid Cloud:**
  **https://cloud.google.com/network-connectivity/docs/vpn/how-to/topologies**

**Why Other Options Are Incorrect?**

**A. Use the same IP range on Google Cloud as you use on-premises.** ❌

- **This causes IP conflicts and routing failures** because the same subnet would exist in both networks.
- **Cloud VPN would not be able to distinguish between on-prem and Google Cloud traffic.**

✅ **Reference:**

- **https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

**B. Use the same IP range on Google Cloud as on-premises for your primary range, and assign a secondary range that does not overlap with your on-premises range.** ❌

- **The primary range must not overlap with on-prem** to avoid routing conflicts.
- **Even if a secondary range is non-overlapping, the primary range would still create connectivity issues.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/subnets#ip_ranges**

**D. Use an IP range on Google Cloud that does not overlap with your on-premises range for the primary range, and configure a secondary range that matches your on-premises IP range.** ❌

- **A secondary range that overlaps with on-premises would still create conflicts.**
- **Both primary and secondary ranges in Google Cloud should be unique and non-overlapping with on-prem.**

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/subnets**

**Conclusion:**

The best approach is **C. Use an IP range on Google Cloud that does not overlap with your on-premises range**, because:

- **Avoids routing conflicts and ensures proper connectivity**.
- **Follows Google Cloud’s hybrid networking best practices**.
- **Ensures a seamless migration while keeping on-premises systems reachable.**

📌 **Final Reference:**
**https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

</details>

---

### Exam 1 · Q50

**You are deploying an application on App Engine that needs to integrate with an on-premises database. For security reasons, the on-premises database must not be accessible via the public internet.**

**What should you do?**

- A. Deploy the application on **App Engine standard environment** and use **App Engine firewall rules** to restrict access to the open on-premises database.
- B. Deploy the application on **App Engine standard environment** and use **Cloud VPN** to establish a private connection to the on-premises database.
- C. Deploy the application on **App Engine flexible environment** and use **App Engine firewall rules** to restrict access to the on-premises database.
- D. Deploy the application on **App Engine flexible environment** and use **Cloud VPN** to establish a private connection to the on-premises database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy the application on **App Engine flexible environment** and use **Cloud VPN** to establish a private connection to the on-premises database.

**Correct Answer:**

✅ **D. Deploy the application on App Engine flexible environment and use Cloud VPN to establish a private connection to the on-premises database.**

**Explanation:**

Since **the on-premises database must not be accessible via the public internet**, you need to:

1. **Use a private connection** between Google Cloud and the on-premises network.
2. **Deploy the application on App Engine flexible environment**, as App Engine standard **does not support direct network access to Cloud VPN**.
3. **Establish a Cloud VPN connection** to securely connect App Engine to the on-premises database over a private network.

**Why This Works?**

✅ **App Engine Flexible Environment**

- **Supports network configuration** that allows direct communication with a private on-premises network via Cloud VPN.
- **Uses Compute Engine VMs**, which have configurable networking capabilities.
- **Allows private IP connectivity** to non-publicly accessible resources.

✅ **Cloud VPN**

- **Enables a secure, private connection** between Google Cloud and on-premises networks.
- **Traffic never traverses the public internet**, ensuring security compliance.

**Implementation Steps:**

1. **Set up Cloud VPN** to establish a private connection to the on-premises database.
2. **Configure firewall rules** to allow App Engine flexible instances to communicate with the on-prem database.
3. **Ensure the App Engine service account has the necessary IAM roles** to access the database.

✅ **Supporting Documentation:**

- **App Engine Flexible Networking:**
  **https://cloud.google.com/appengine/docs/flexible**
- **Using Cloud VPN for Hybrid Connectivity:**
  **https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

**Why Other Options Are Incorrect?**

**A. Deploy the application on App Engine standard environment and use App Engine firewall rules to restrict access to the open on-premises database.** ❌

- **App Engine standard does not support direct network access to Cloud VPN or private IPs.**
- **Firewall rules do not provide a private connection** to the on-premises database.
- **This option would still expose the database over the public internet.**

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/standard**

**B. Deploy the application on App Engine standard environment and use Cloud VPN to establish a private connection to the on-premises database.** ❌

- **App Engine standard cannot connect directly to Cloud VPN or private networks.**
- **Standard environment apps are sandboxed and do not allow custom networking configurations.**

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/standard**

**C. Deploy the application on App Engine flexible environment and use App Engine firewall rules to restrict access to the on-premises database.** ❌

- **Firewall rules only restrict access but do not establish a private connection.**
- **A VPN is still required** to ensure the on-premises database is accessible privately.

✅ **Reference:**

- **https://cloud.google.com/appengine/docs/flexible**

**Conclusion:**

The best approach is **D. Deploy the application on App Engine flexible environment and use Cloud VPN to establish a private connection to the on-premises database**, because:

- **App Engine flexible supports private networking.**
- **Cloud VPN ensures secure, private connectivity.**
- **It aligns with Google Cloud best practices for hybrid networking.**

📌 **Final Reference:**
**https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview**

**⚠️ Note:** App Engine standard can now reach a VPC (and on-premises over Cloud VPN) through a **Serverless VPC Access connector** (Exam 3 · Q25). Option B mentions only Cloud VPN, with no connector, so flexible + Cloud VPN is still the best of these options.

</details>

---

### Exam 1 · Q51

**You are working in a highly secured environment where public internet access from Compute Engine VMs is not allowed. There is no VPN connection to access an on-premises file server yet. You need to install specific software on a Compute Engine instance.**

**How should you install the software?**

- A. **Upload the installation files to Cloud Storage**, configure the VM on a **subnet with Private Google Access**, assign **only an internal IP** to the VM, and download the files using **gsutil**.
- B. **Upload the installation files to Cloud Storage**, configure **firewall rules to block all traffic** except the **IP address range for Cloud Storage**, and download the files using **gsutil**.
- C. **Upload the installation files to Cloud Source Repositories**, configure the VM on a **subnet with Private Google Access**, assign **only an internal IP** to the VM, and download the files using **gcloud**.
- D. **Upload the installation files to Cloud Source Repositories**, configure **firewall rules to block all traffic** except the **IP address range for Cloud Source Repositories**, and download the files using **gsutil**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Upload the installation files to Cloud Storage**, configure the VM on a **subnet with Private Google Access**, assign **only an internal IP** to the VM, and download the files using **gsutil**.

**Correct Answer:**

✅ **A. Upload the installation files to Cloud Storage, configure the VM on a subnet with Private Google Access, assign only an internal IP to the VM, and download the files using gsutil.**

**Explanation:**

Since the **Compute Engine VM is in a highly secured environment** with **no public internet access**, and there is **no VPN connection to an on-prem file server**, you need a **private and secure way** to download installation files.

**Why This Works?**

1. **Cloud Storage is the best place to store installation files** because it is a **fully managed, secure, and scalable** storage service.
2. **Private Google Access (PGA)** allows VMs with **only internal IPs** to access Google APIs and services (such as Cloud Storage) **without requiring public internet access**.
3. **Using `gsutil` over Private Google Access** ensures **secure and restricted access** to the installation files.

**Implementation Steps:**

1. **Upload the installation files to a Cloud Storage bucket:**
  ```
  bashCopyEditgsutil cp software_package.tar.gz gs://my-secure-bucket/
  ```
2. **Ensure the VM is in a VPC subnet with Private Google Access enabled:**
  - In **Google Cloud Console**, navigate to **VPC network → Subnets → Edit subnet**.
  - Enable **Private Google Access** for the subnet.
3. **Assign only an internal IP to the VM (no public IP).**
4. **Download the files to the VM using `gsutil`:**
  ```
  bashCopyEditgsutil cp gs://my-secure-bucket/software_package.tar.gz .
  ```

✅ **Supporting Documentation:**

- **Private Google Access Overview:**
  **https://cloud.google.com/vpc/docs/configure-private-google-access**
- **Using gsutil with Private Google Access:**
  **https://cloud.google.com/storage/docs/gsutil**

**Why Other Options Are Incorrect?**

**B. Upload the installation files to Cloud Storage, configure firewall rules to block all traffic except the IP address range for Cloud Storage, and download the files using gsutil.** ❌

- **Firewall rules do not control access to Google services like Cloud Storage**—Private Google Access does.
- **Google Cloud services like Cloud Storage do not have fixed IP address ranges** that can be explicitly allowed in firewall rules.
- **PGA is the recommended approach** for accessing Cloud Storage without public internet.

✅ **Reference:**

- **https://cloud.google.com/vpc/docs/configure-private-google-access**

**C. Upload the installation files to Cloud Source Repositories, configure the VM on a subnet with Private Google Access, assign only an internal IP to the VM, and download the files using gcloud.** ❌

- **Cloud Source Repositories is designed for source code, not for large installation files.**
- **Cloud Storage is the recommended service for storing and distributing files.**
- **Downloading binary files using `gcloud source repos` is not the correct approach.**

✅ **Reference:**

- **https://cloud.google.com/source-repositories/docs/**

**D. Upload the installation files to Cloud Source Repositories, configure firewall rules to block all traffic except the IP address range for Cloud Source Repositories, and download the files using gsutil.** ❌

- **Cloud Source Repositories is not meant for binary file distribution.**
- `gsutil` **is used to download from Cloud Storage, not Cloud Source Repositories.**
- **Firewall rules cannot selectively allow Cloud Source Repositories while blocking all other internet access.**

✅ **Reference:**

- **https://cloud.google.com/source-repositories/docs/access-control**

**Conclusion:**

The best approach is **A. Upload the installation files to Cloud Storage, configure the VM on a subnet with Private Google Access, assign only an internal IP to the VM, and download the files using gsutil**, because:

- **Cloud Storage is the recommended service for securely storing installation files.**
- **Private Google Access allows secure access to Cloud Storage without public internet.**
- **The VM remains private and meets the security requirements.**

📌 **Final Reference:**
**https://cloud.google.com/vpc/docs/configure-private-google-access**

**⚠️ Note:** Use `gcloud storage cp` instead of the legacy `gsutil`. Cloud Source Repositories is closed to new customers, which is one more reason the Cloud Storage options win.

</details>

---

### Exam 2 · Q8

**Your company is running a stateless application on a Compute Engine instance. The application experiences heavy usage during business hours and light usage outside of business hours. Users have reported that the application slows down during peak hours. You need to optimize performance dynamically.**

**What should you do?**

- A. **Create a snapshot** of the existing disk, then create an **instance template** from the snapshot. Use this template to create an **autoscaled managed instance group**.
- B. **Create a snapshot** of the existing disk, then create a **custom image** from the snapshot. Use this image to create an **autoscaled managed instance group**.
- C. **Create a custom image** from the existing disk, then create an **instance template** from the custom image. Use this template to create an **autoscaled managed instance group**.
- D. **Create an instance template** from the existing disk, then create a **custom image** from the instance template. Use this image to create an **autoscaled managed instance group**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Create a custom image** from the existing disk, then create an **instance template** from the custom image. Use this template to create an **autoscaled managed instance group**.

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

</details>

---

### Exam 2 · Q9

**Your web application is running on multiple VM instances within a VPC. You need to restrict communication between instances to only the authorized paths and ports while ensuring that your solution does not depend on static IP addresses or subnets, since the application autoscale dynamically.**

**How should you enforce these restrictions?**

- A. Use **separate VPCs** to control traffic flow.
- B. Use **firewall rules based on network tags** attached to the compute instances.
- C. Use **Cloud DNS** and allow connections **only from authorized hostnames**.
- D. Use **service accounts** and configure the web application to **authorize specific service accounts** for access.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **firewall rules based on network tags** attached to the compute instances.

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

</details>

---

### Exam 2 · Q14

**You need to deploy a Compute Engine application in a single VPC that spans two regions. The application must be able to communicate with an on-premises network over VPN.**

**How should you configure the VPN?**

- A. Use **VPC Network Peering** to establish connectivity between the **VPC and the on-premises network**.
- B. Expose the **VPC to the on-premises network** using **IAM and VPC Sharing**.
- C. Create a **global Cloud VPN Gateway** and establish **VPN tunnels from each region** to the **on-premises peer gateway**.
- D. Deploy a **Cloud VPN Gateway** in **each region**, ensuring that each region has **at least one VPN tunnel** to the **on-premises peer gateway**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Deploy a **Cloud VPN Gateway** in **each region**, ensuring that each region has **at least one VPN tunnel** to the **on-premises peer gateway**.

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

</details>

---

### Exam 2 · Q15

**Your applications will be writing logs to BigQuery for analysis, with each application having its own table. You need to automatically remove logs older than 45 days, while optimizing storage and following Google-recommended best practices.**

**What should you do?**

- A. Set the **expiration time** for each table to **45 days**.
- B. Use **time-partitioned tables** and configure the **partition expiration** to **45 days**.
- C. Rely on **BigQuery’s default behavior**, which automatically removes logs older than 45 days.
- D. Create a **script** using the **BigQuery command-line tool (bq)** to delete records older than **45 days**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **time-partitioned tables** and configure the **partition expiration** to **45 days**.

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

</details>

---

### Exam 2 · Q16

**You need your Google Kubernetes Engine (GKE) cluster to automatically scale nodes up or down based on CPU load.**

**What should you do?**

- A. Configure a **HorizontalPodAutoscaler** with a **target CPU usage** and enable **Cluster Autoscaler** from the **Google Cloud Console**.
- B. Configure a **HorizontalPodAutoscaler** with a **target CPU usage** and enable **autoscaling on the managed instance group** for the cluster using the **gcloud** command.
- C. Create a **Deployment** and set the **maxUnavailable** and **maxSurge** properties, then enable **Cluster Autoscaler** using the **gcloud** command.
- D. Create a **Deployment** and set the **maxUnavailable** and **maxSurge** properties, then enable **autoscaling on the cluster's managed instance group** from the **Google Cloud Console**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure a **HorizontalPodAutoscaler** with a **target CPU usage** and enable **Cluster Autoscaler** from the **Google Cloud Console**.

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

</details>

---

### Exam 2 · Q21

**You need to automate the creation of a managed instance group (MIG). The VMs in this group have many OS package dependencies, and you want to minimize startup time when new instances are added.**

**What should you do?**

- A. Use **Terraform** to create the **managed instance group** and a **startup script** to install the OS package dependencies.
- B. Create a **custom VM image** that includes all OS package dependencies, then use **Deployment Manager** to create the **managed instance group** with this VM image.
- C. Use **Puppet** to create the **managed instance group** and install the OS package dependencies.
- D. Use **Deployment Manager** to create the **managed instance group** and **Ansible** to install the OS package dependencies.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a **custom VM image** that includes all OS package dependencies, then use **Deployment Manager** to create the **managed instance group** with this VM image.

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

</details>

---

### Exam 2 · Q24

Your **web application** is deployed on **Google Kubernetes Engine (GKE)** and manages **multiple workloads**. One of the workloads **requires a consistent set of hostnames**, even when **pods scale or relaunch**.

Which **Kubernetes feature** should you use to achieve this?

- A. StatefulSets
- B. Role-Based Access Control (RBAC)
- C. Container Environment Variables
- D. Persistent Volumes

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. StatefulSets

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

</details>

---

### Exam 2 · Q25

**You are using Cloud CDN to serve static HTTP(S) content from a Compute Engine instance group. You need to improve the cache hit ratio to enhance performance and reduce backend load.**

**What should you do?**

- A. **Customize the cache keys** to **omit the protocol** from the key.
- B. **Shorten the expiration time** of cached objects.
- C. Ensure the **HTTP(S) header** `Cache-Region` points to the region **closest to your users**.
- D. **Replicate the static content** in a **Cloud Storage bucket** and point **Cloud CDN** to a **load balancer** on that bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Customize the cache keys** to **omit the protocol** from the key.

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

</details>

---

### Exam 2 · Q28

**You need to ensure that all Compute Engine instances in your VPC can connect to an Active Directory server on specific ports, while blocking all other outbound traffic. You want to enforce this using VPC firewall rules.**

**How should you configure the egress firewall rules?**

- A. **Create an egress rule** with **priority 1000** to **deny all traffic** for all instances. Then, create another **egress rule** with **priority 100** to **allow Active Directory traffic** for all instances.
- B. **Create an egress rule** with **priority 100** to **deny all traffic** for all instances. Then, create another **egress rule** with **priority 1000** to **allow Active Directory traffic** for all instances.
- C. **Create an egress rule** with **priority 1000** to **allow Active Directory traffic**. Rely on the **implied deny egress rule** with **priority 100** to **block all other traffic** for all instances.
- D. **Create an egress rule** with **priority 100** to **allow Active Directory traffic**. Rely on the **implied deny egress rule** with **priority 1000** to **block all other traffic** for all instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Create an egress rule** with **priority 1000** to **deny all traffic** for all instances. Then, create another **egress rule** with **priority 100** to **allow Active Directory traffic** for all instances.

**Correct choice → A**

**A.** Create an egress rule with priority **1000** that **denies all** traffic for all instances, and then add a second egress rule with priority **100** that **allows the required Active Directory ports** for all instances.

Why option A works

1. **Firewall-rule evaluation order**
  - Priorities are integers **0 – 65535**; **lower numbers mean higher priority** and are matched first. [Google Cloud](https://cloud.google.com/firewall/docs/firewalls)
2. **Implied egress behaviour**
  - Every VPC automatically has an ***implied allow-egress* rule** (priority 65535) that lets all outbound traffic through unless a higher-priority rule blocks it. [Google Cloud](https://cloud.google.com/firewall/docs/firewalls)
3. **Result of the two explicit rules in option A**

| Traffic type | Matches rule | Action | Reason |
|---|---|---|---|
| AD ports you list in the allow rule (e.g. TCP 389/636/3268 …, UDP 88/123 …) | **Priority 100** allow | **Allowed** | Highest-priority match permits it |
| Any other outbound traffic | Skips priority 100 (ports don't match) → hits **priority 1000** deny | **Blocked** | Deny overrides the implied allow |
| Anything not caught by the explicit rules | Implied allow-egress rule (priority 65535) | **Ignored** | Lower priority, so never reached |

Thus all VMs can talk only to the specified AD ports, and everything else is dropped.

**Why the other options are incorrect:**

| Option | What happens | Why it fails |
|---|---|---|
| **B**: deny 100, allow 1000 | Traffic hits the **deny (priority 100)** first and is blocked before it reaches the lower-priority allow rule. | Lower number → higher priority. |
| **C**: allow 1000 only, rely on an "implied deny 100" | There is **no implied deny-egress rule**. The implied rule is *allow*, so all other traffic stays open. | The implied egress rule is allow (priority 65535), not deny. |
| **D**: allow 100 only, rely on an "implied deny 1000" | Again, no implied deny-egress rule exists. Traffic that doesn't match the allow rule falls through to the implied **allow-egress**, so nothing is blocked. | Same as C. |

</details>

---

### Exam 2 · Q30

**Your company's development team has built a dockerized HTTPS web application. You need to deploy the application on Google Kubernetes Engine (GKE) while ensuring that it scales automatically.**

**How should you deploy it to GKE?**

- A. Use the **Horizontal Pod Autoscaler (HPA)** and enable **Cluster Autoscaler**. Use an **Ingress resource** to load-balance HTTPS traffic.
- B. Use the **Horizontal Pod Autoscaler (HPA)** and enable **Cluster Autoscaler** on the **Kubernetes cluster**. Use a **Service resource of type LoadBalancer** to distribute HTTPS traffic.
- C. Enable **autoscaling on the Compute Engine instance group**. Use an **Ingress resource** to load-balance HTTPS traffic.
- D. Enable **autoscaling on the Compute Engine instance group**. Use a **Service resource of type LoadBalancer** to distribute HTTPS traffic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use the **Horizontal Pod Autoscaler (HPA)** and enable **Cluster Autoscaler**. Use an **Ingress resource** to load-balance HTTPS traffic.

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

</details>

---

### Exam 2 · Q34

**Your company has acquired a healthcare startup and must retain customer medical information for up to 4 more years, based on when the data was created. Corporate policy requires secure data retention and automatic deletion as soon as regulations permit.**

**Which approach should you take?**

- A. Store the data in **Google Drive** and **manually delete** records as they expire.
- B. **Anonymize the data** using the **Cloud Data Loss Prevention (DLP) API** and **store it indefinitely**.
- C. Store the data in **Cloud Storage** and use **lifecycle management** to **automatically delete files** when they expire.
- D. Store the data in **Cloud Storage** and run a **nightly batch script** to delete **all expired data**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Store the data in **Cloud Storage** and use **lifecycle management** to **automatically delete files** when they expire.

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

</details>

---

### Exam 2 · Q41

Your company has an **application running on multiple Compute Engine instances**. The application must **communicate with an on-premises service** that requires **high throughput** using **internal IP addresses**, while also **minimizing latency**.

What should you do?

- A. **Use OpenVPN** to set up a **VPN tunnel** between the **on-premises environment and Google Cloud**.
- B. **Configure a Direct Peering connection** between the **on-premises network and Google Cloud**.
- C. **Use Cloud VPN** to establish a **VPN tunnel** between the **on-premises environment and Google Cloud**.
- D. **Set up a Cloud Dedicated Interconnect** between the **on-premises environment and Google Cloud**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Set up a Cloud Dedicated Interconnect** between the **on-premises environment and Google Cloud**.

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

</details>

---

### Exam 2 · Q51

Your company has **acquired another company**, and you need to **integrate their existing Google Cloud environment** with your **on-premises data center**.

Upon investigation, you find that some of the **RFC 1918 IP ranges** in the **new company's Virtual Private Cloud (VPC)** **overlap** with the **IP space** in your **data center**.

To enable **connectivity** while ensuring that there are **no routing conflicts**, what should you do?

- A. **Create a Cloud VPN connection** from the new VPC to the data center, then **set up a Cloud Router** and **assign new IP addresses** to avoid overlapping IP space.
- B. Create a Cloud VPN connection between the new VPC and the data center, and configure **Cloud NAT Private NAT / Hybrid NAT** to translate the overlapping IP ranges to non-overlapping address ranges.
- C. **Create a Cloud VPN connection** from the new VPC to the data center, then **set up a Cloud Router** and apply a **custom route advertisement** to **block the overlapping IP space**.
- D. **Create a Cloud VPN connection** from the new VPC to the data center, and configure a **firewall rule** to **block traffic from the overlapping IP space**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a Cloud VPN connection between the new VPC and the data center, and configure **Cloud NAT Private NAT / Hybrid NAT** to translate the overlapping IP ranges to non-overlapping address ranges.

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

</details>

---

### Exam 2 · Q61

**The database administration team seeks assistance in enhancing the performance of their new database server hosted on Compute Engine. This MySQL-based database serves to import and normalize the company's performance statistics and operates on Debian Linux. The current setup consists of an n1-standard-8 virtual machine with an 80 GB SSD zonal persistent disk, which cannot be restarted until the next maintenance event. What change should they implement to promptly and cost-effectively improve system performance?**

- A. Increase the virtual machine's memory to 64 GB.
- B. Deploy a new virtual machine running PostgreSQL.
- C. Dynamically resize the SSD persistent disk to 500 GB.
- D. Migrate their performance metrics warehouse to BigQuery.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Dynamically resize the SSD persistent disk to 500 GB.

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

</details>

---

### Exam 3 · Q3

You are building an application composed of multiple **microservices**, which should remain **internal to the Kubernetes cluster**. Each microservice must be **independently scalable**, allowing you to configure a **specific number of replicas** per service. Additionally, other microservices should be able to **communicate with any microservice** using a **consistent address**, regardless of how many replicas it has.

You are deploying this on **Google Kubernetes Engine (GKE)**.

What is the most appropriate way to implement this?

- A. Deploy each microservice as a **Deployment**, expose it using a **ClusterIP Service**, and reference it via the **Service DNS name** from other microservices.
- B. Deploy each microservice as a **Deployment**, expose it using an **Ingress**, and reference it via the **Ingress IP address** from other microservices.
- C. Deploy each microservice as a **Pod**, expose it using a **Service**, and reference it via the **Service DNS name** from other microservices.
- D. Deploy each microservice as a **Pod**, expose it using an **Ingress**, and reference it via the **Ingress IP address** from other microservices.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy each microservice as a **Deployment**, expose it using a **ClusterIP Service**, and reference it via the **Service DNS name** from other microservices.

✅ **Correct Answer: A. Deploy each microservice as a Deployment, expose it using a ClusterIP Service, and reference it via the Service DNS name from other microservices.**

**Detailed Analysis**

**Given Requirements:**

- Application has **multiple microservices**.
- Microservices should be **internal to the GKE cluster** (not public-facing).
- Each microservice must be **independently scalable**.
- Other microservices should be able to communicate with any microservice via a **consistent address**, regardless of the number of replicas.

✅ **Why Option A is Correct:**

- **Deployment**: Manages replica sets, provides self-healing, and allows you to scale the number of replicas independently for each microservice.
- **ClusterIP Service**: Default type of Kubernetes service; exposes the service **internally within the cluster** only (no external IP). Perfect for internal microservice communication.
- **Service DNS name**: Kubernetes provides a **built-in DNS service** that maps a service name to its virtual IP. Microservices can reach others via `<service-name>.<namespace>.svc.cluster.local`.

This approach ensures:

- Internal-only access (**ClusterIP**).
- Scalable and self-healing microservices (**Deployment**).
- Stable communication endpoint regardless of pod replica count (**Service DNS**).

**Documentation Reference:**

- Kubernetes Services - ClusterIP
- Kubernetes DNS for Service Discovery
- Deployments in Kubernetes

❌ **Why Other Options Are Incorrect:**

**B. Deploy each microservice as a Deployment, expose it using an Ingress, and reference it via the Ingress IP address from other microservices**

- **Ingress** is intended for **external HTTP/S traffic**, not for internal microservice-to-microservice communication.
- Using Ingress for internal communication is unnecessary overhead and **against best practices**.
- Ingress requires **Layer 7 (HTTP) routing configuration**, and it’s more complex and less efficient for internal use cases.

**Docs:**

- Ingress overview

**C. Deploy each microservice as a Pod, expose it using a Service, and reference it via the Service DNS name from other microservices**

- Using **Pods directly** is incorrect because Pods are **ephemeral** (subject to restarts and rescheduling), and **do not scale or self-heal**.
- You should use **Deployments** (not standalone Pods) to manage scaling, availability, and replication.

**Docs:**

- Pods are not meant for direct deployment in production

**D. Deploy each microservice as a Pod, expose it using an Ingress, and reference it via the Ingress IP address from other microservices**

- Combines the two incorrect practices:
  - Exposing standalone **Pods** (no scalability or resilience)
  - Using **Ingress** for internal communication (adds complexity and is not appropriate)
- This would be inefficient and fragile in a microservice architecture.

✅ Final Recommendation:

**Option A** is the most appropriate design:

- Scalable microservices using **Deployments**
- Internal exposure using **ClusterIP Services**
- Stable, internal communication via **Kubernetes DNS**

</details>

---

### Exam 3 · Q14

Your organization has deployed a **Kubernetes application** that **pulls messages from Pub/Sub** and stores them in **Filestore**. Since the application is relatively simple, it was originally deployed as a **single pod**. However, the infrastructure team has reviewed **Pub/Sub metrics** and found that the application is **not keeping up with real-time message processing**—many messages are delayed by several minutes before being handled. The application’s workload is **I/O-intensive**, and you need to **scale the processing layer** to address the performance issue.

What should you do?

- A. Run the command: `kubectl autoscale deployment APP_NAME --max 6 --min 2 --cpu-percent 50` to configure **horizontal pod autoscaling based on CPU usage**.
- B. Set up **Kubernetes autoscaling** using the `subscription/push_request_latencies` metric from Pub/Sub.
- C. Use the `--enable-autoscaling` flag when creating the **GKE cluster** to automatically enable cluster-level autoscaling.
- D. Configure **Kubernetes autoscaling** based on the `subscription/num_undelivered_messages` metric from Pub/Sub

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure **Kubernetes autoscaling** based on the `subscription/num_undelivered_messages` metric from Pub/Sub

✅ **Correct Answer: D. Configure Kubernetes autoscaling based on the `subscription/num_undelivered_messages` metric from Pub/Sub.**

**Scenario Summary:**

- Application running on **Kubernetes** pulls messages from **Pub/Sub** and writes to **Filestore**.
- It's **I/O-intensive**, and **currently underperforms** — Pub/Sub shows **message processing delays**.
- The goal is to **scale the processing layer effectively** based on actual workload (Pub/Sub backlog).
- CPU is **not the bottleneck** — **Pub/Sub backlog is**.

✅ **Why Option D is Correct:**

**Custom Metric-Based Autoscaling with Pub/Sub Backlog:**

- Kubernetes **Horizontal Pod Autoscaler (HPA)** can use **custom metrics** via the **Custom Metrics API**.
- You can configure HPA to **scale pods** based on **Pub/Sub backlog size** (`subscription/num_undelivered_messages`), which is a direct indicator of processing demand.
- This ensures scaling is aligned with **actual message load**, not CPU usage (which might not correlate well with I/O workloads).

**Metric Explanation:**

- `subscription/num_undelivered_messages`:
  *The number of unprocessed messages in the Pub/Sub subscription backlog.*
- When this value increases, it indicates **your app isn’t keeping up**, and **more pods should be added**.

**Official Documentation:**

- Google Cloud – Custom metrics for autoscaling
- GKE – Autoscale based on custom metrics

❌ **Why Other Options Are Incorrect:**

**A. Use `kubectl autoscale` based on CPU usage**

- CPU-based autoscaling is **not appropriate for I/O-bound workloads**.
- Pub/Sub backlog growth is **not necessarily tied to CPU usage**, especially if processing is **disk or network-bound**.

**B. Use autoscaling based on** `subscription/push_request_latencies`

- This metric reflects **Pub/Sub push latency**, not pull subscriber backlog.
- Your app uses **pull**, and the relevant metric is **backlog size**, not delivery latency.
- Also, this metric doesn't directly map to **how many pods you need** to process the load.

**C. Enable cluster-level autoscaling with** `--enable-autoscaling`

- Cluster autoscaler scales **node count**, not **pod count**.
- You still need a correctly configured **HPA** that uses **the right metric**.
- Cluster autoscaler works **with** HPA but does not replace the need for **proper scaling logic** based on message backlog.

✅ **Final Recommendation:**

Configure **HPA to scale your Kubernetes deployment** based on **Pub/Sub** `subscription/num_undelivered_messages` — this gives the **most accurate and workload-specific autoscaling behavior**.

</details>

---

### Exam 3 · Q24

At NetCore Labs, your team is preparing to deploy a newly developed application on **Google Kubernetes Engine (GKE)**. This application needs to interact with external third-party services over the internet. However, your organization's security policy **prohibits assigning public IP addresses** to any **Compute Engine** instances in your environment.

**What deployment strategy should you use to meet these requirements while aligning with best practices?**

- A. Set up a **private GKE cluster**, and configure a **Cloud NAT Gateway** for the subnet used by the cluster.
- B. Set up a **private GKE cluster**, and enable **Private Google Access** on the associated **Virtual Private Cloud (VPC)** network.
- C. Deploy a **route-based GKE cluster**, and enable **Private Google Access** on the associated VPC.
- D. Provision a **Compute Engine instance** to run a custom **NAT proxy**, and configure all GKE workloads to route traffic through this instance to access third-party services.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up a **private GKE cluster**, and configure a **Cloud NAT Gateway** for the subnet used by the cluster.

The correct answer is:
**A. Set up a private GKE cluster, and configure a Cloud NAT Gateway for the subnet used by the cluster.**

✅ Justification for Correct Option (A):

- **Private GKE clusters** do not assign public IP addresses to nodes, aligning perfectly with the security policy that **prohibits public IPs**.
- However, for workloads in the cluster to **access the internet** (e.g., third-party APIs), they need **egress access**.
- The recommended and **secure** approach for enabling internet access **without assigning public IPs** is to use **Cloud NAT**.
- **Cloud NAT (Network Address Translation)** allows resources in a **private subnet** (like GKE nodes) to initiate **outbound connections** to the internet **without needing external IPs**.

**Official Documentation:**

- Using Cloud NAT with GKE
- Cloud NAT overview

❌ Why Other Options Are Incorrect:

B.

Set up a private GKE cluster, and enable Private Google Access on the associated VPC.

- **Private Google Access** allows access to **Google APIs and services**, **not** arbitrary **third-party internet services**.
- Since the requirement involves connecting to **external third-party services**, Private Google Access alone **does not meet the need**.

**Reference:**

- Private Google Access

C.

Deploy a route-based GKE cluster, and enable Private Google Access on the associated VPC.

- This option is also **incorrect** because:
  - **Private Google Access only allows access to Google APIs**.
  - **Route-based GKE** isn’t relevant here and does not solve the egress internet connectivity issue without public IPs.

D.

Provision a Compute Engine instance to run a custom NAT proxy...

- While **technically feasible**, running a **custom NAT proxy** introduces **management complexity**, **scalability challenges**, and **availability risks**.
- **Google Cloud recommends using Cloud NAT** instead of custom-built solutions for **managed, secure, and highly available** NAT functionality.

**Reference:**

- Cloud NAT best practices

✅ Final Answer: **A**

Use a **private GKE cluster with Cloud NAT**, which is a **Google-recommended solution** for enabling **secure outbound internet access** from **private nodes**, ensuring **compliance with the organization's policy**.

Link - [https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private-nodes-outbound](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private-nodes-outbound)

</details>

---

### Exam 3 · Q25

TechAxis Inc. runs a support ticketing system hosted on **App Engine Standard Environment**. The Google Cloud project hosting the App Engine app is already connected to the company's **on-premises network** via a **Cloud VPN tunnel**, and a **Virtual Private Cloud (VPC)** is fully set up.

The App Engine application must now be able to **connect to a database hosted in the on-premises environment**.

**What should you do to enable this connectivity?**

- A. Enable **Private Google Access for on-premises hosts only**.
- B. Enable **Private Google Access**.
- C. Configure **Private Services Access**.
- D. Configure **Serverless VPC Access**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure **Serverless VPC Access**.

The correct answer is:
**D. Configure Serverless VPC Access.**

✅ Justification for Correct Option (D):

- The application is running on **App Engine Standard Environment**, which is a **serverless** platform.
- To allow **serverless apps** (such as App Engine Standard, Cloud Functions, or Cloud Run) to connect to resources in a **VPC network**, including **on-premises resources connected via Cloud VPN**, you must configure **Serverless VPC Access**.
- **Serverless VPC Access connectors** allow serverless environments to **communicate with internal IPs** in the VPC, which includes the **Cloud VPN tunnel** and **on-premises systems**.

**Official Documentation:**

- App Engine Standard → Serverless VPC Access
- Serverless VPC Access Overview

❌ Why the Other Options Are Incorrect:

A.

Enable Private Google Access for on-premises hosts only.

- This setting allows **on-premises systems** to access **Google APIs** using **Private Google Access**, but it **does not allow App Engine** to access on-prem systems.
- This is **not related** to App Engine accessing the on-prem database.

**Reference:**

- Private Google Access for on-premises hosts

B.

Enable Private Google Access.

- This enables **VMs without external IPs** in the VPC to access **Google APIs**, but it **does not allow outbound access** from **App Engine Standard** to **on-prem resources**.
- Again, **not applicable** for serverless-to-on-prem connectivity.

C.

Configure Private Services Access.

- Private Services Access is used to **connect to managed services**, like **Cloud SQL or Filestore**, over internal IP.
- It is **not used** for accessing **on-premises databases** or **establishing serverless access** to VPC networks.

**Reference:**

- Private Services Access overview

✅ Final Answer: **D. Configure Serverless VPC Access.**

It is the **only correct and supported method** for enabling **App Engine Standard Environment** to communicate with **on-premises systems** via **Cloud VPN and VPC**.

</details>

---

### Exam 3 · Q31

You are working at **MediCore Institute**, an organization that processes **sensitive medical data**. As part of your cloud migration strategy, you are moving multiple workloads to **Google Cloud**. Due to strict **compliance requirements**, all workloads must run on **physically isolated hardware**, and **workloads from different clients must be completely separated**.

You have created a **sole-tenant node group** and assigned a **dedicated node for each client**. Now, you need to ensure that each workload is deployed to the appropriate dedicated host.

**What should you do to meet these requirements?**

- A.Attach the **node group name** as a **network tag** when creating **Compute Engine instances** so that each workload is hosted on the correct node group.
- B.Attach the **node name** as a **network tag** when creating Compute Engine instances to ensure each workload is deployed to the correct node.
- C. Use **node affinity labels** referencing the **node group name** when creating Compute Engine instances to schedule workloads on the appropriate node group.
- D. Use **node affinity labels** referencing the **node name** when creating Compute Engine instances to schedule each workload on its designated node.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use **node affinity labels** referencing the **node name** when creating Compute Engine instances to schedule each workload on its designated node.

The correct answer is:
**D. Use node affinity labels referencing the node name when creating Compute Engine instances to schedule each workload on its designated node.**

✅ Justification for Correct Option (D):

- **Sole-tenant nodes** provide **physically isolated hardware** for running sensitive workloads, which is essential for **compliance** in industries like healthcare.
- To schedule workloads on a **specific sole-tenant node**, you must use **node affinity labels**, referencing the **exact node name**.
- This ensures that a specific workload is placed on its **designated, physically isolated node**, guaranteeing **strict client separation**.

**Node affinity** is the mechanism used by Google Cloud to control **VM placement** on sole-tenant nodes.

**Official Documentation:**

- Placing VMs on sole-tenant nodes using node affinity
- Node affinity reference

❌ Why Other Options Are Incorrect:

A.

Attach the node group name as a network tag when creating Compute Engine instances.

- **Network tags** are used for **firewall rules and network configurations**, not for **VM placement on nodes**.
- They **do not influence** how Compute Engine schedules VMs on sole-tenant nodes.

B.

Attach the node name as a network tag when creating Compute Engine instances.

- Again, **network tags do not control VM placement** on nodes.
- They are unrelated to **sole-tenant node scheduling**.

C.

Use node affinity labels referencing the node group name.

- This references a **group of nodes**, not a specific one.
- Since the requirement is **strict client isolation**, placing a workload on **any node in a group** would **not ensure that isolation**.
- Only referencing the **specific node name** ensures a workload is tied to a particular dedicated host.

✅ Final Answer: **D**

Because it uses **node affinity with specific node names**, ensuring **compliance with physical isolation requirements** and **strict workload separation** per client, which is essential in handling **sensitive medical data**.

Ref- [https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_affinity_labels](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_affinity_labels)

</details>

---

### Exam 3 · Q38

**You've set up an autoscaling managed instance group to handle web traffic for an imminent launch. Upon configuring the instance group as a backend service to an HTTP(S) load balancer, you observe that virtual machine (VM) instances are being terminated and restarted every minute. These instances lack public IP addresses, yet you've confirmed that each instance is properly responding to web requests using the curl command. How should you ensure that the backend is configured correctly?**

- A. Verify the presence of a firewall rule permitting source traffic on HTTP/HTTPS to reach the load balancer.
- B. Allocate a public IP to each instance and configure a firewall rule to enable the load balancer to access the instance public IP.
- C. Confirm the existence of a firewall rule enabling load balancer health checks to reach the instances within the instance group.
- D. Attach a tag to each instance matching the load balancer's name. Establish a firewall rule with the load balancer's name as the source and the instance tag as the destination.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Confirm the existence of a firewall rule enabling load balancer health checks to reach the instances within the instance group.

The correct answer is:
**C. Confirm the existence of a firewall rule enabling load balancer health checks to reach the instances within the instance group.**

✅ **Justification for Correct Option (C):**

In Google Cloud, when you configure an **HTTP(S) load balancer** with a **backend service** (such as a **Managed Instance Group**), the load balancer uses **Google Front Ends (GFEs)** to perform **health checks** on the backend instances.

If:

- The health checks **fail** due to blocked traffic,
- Or the instances **don't respond to health check probes** properly,

Then the instances are considered **unhealthy** and are subject to **termination and recreation** by the autoscaler (as part of instance group health management).

Since the instances **do not have public IPs**, the health checks must come from **Google’s health check IP ranges**, and for those to succeed, you must allow them using an **ingress firewall rule**.

**Required Action:**

- Create a **firewall rule** allowing traffic from the health check IP ranges (source IPs) to reach the **health check ports** (e.g., TCP:80 for HTTP, TCP:443 for HTTPS).

**Official Documentation:**

- Health check firewall requirements
- Allowing health check probes

❌ **Why Other Options Are Incorrect:**

**A. Verify the presence of a firewall rule permitting source traffic on HTTP/HTTPS to reach the load balancer.**

- **Incorrect** because traffic from **users to the load balancer** is handled over the public internet via **Google Front Ends** — your backend VMs **do not need to receive traffic directly from clients**, and this firewall rule doesn't affect **health checks**.

**B. Allocate a public IP to each instance and configure a firewall rule...**

- **Not required**. Google Cloud **HTTP(S) Load Balancers use internal IPs** to connect to the backends — you do **not need public IPs** on VM instances for the load balancer to work.
- Adding public IPs introduces unnecessary **security risks and costs**.

**D. Attach a tag to each instance matching the load balancer's name...**

- GCP **does not use instance tags to match load balancers**.
- Also, the **source IP for health checks is not the load balancer name**, but specific **IP address ranges**, which must be allowed via **source IP ranges**, not tags.

✅ **Final Answer: C**

Ensure the backend instance group has a **firewall rule** that explicitly allows **health check probes** from **Google Cloud's health check IP ranges**, so the load balancer can correctly determine backend health.

References:[https://cloud.google.com/load-balancing/docs/https/](https://cloud.google.com/load-balancing/docs/https/)

[https://cloud.google.com/load-balancing/docs/health-check-concepts](https://cloud.google.com/load-balancing/docs/health-check-concepts)

</details>

---

### Exam 3 · Q39

**Your organization hosts a 3-tier web application within the same Google Cloud Virtual Private Cloud (VPC). Each tier (web, API, and database) scales independently. Network traffic is intended to flow from the web tier to the API tier and then to the database tier. However, traffic should not traverse directly between the web and database tiers. How should you configure the network with minimal steps?**

- A. Assign each tier to a distinct subnetwork.
- B. Implement software-based firewalls on individual VMs.
- C. Apply tags to each tier and establish routes to enable the desired traffic flow.
- D. Apply tags to each tier and create firewall rules to permit the intended traffic flow.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Apply tags to each tier and create firewall rules to permit the intended traffic flow.

The correct answer is:
**D. Apply tags to each tier and create firewall rules to permit the intended traffic flow.**

✅ Justification for Correct Option (D):

In Google Cloud's Virtual Private Cloud (VPC), **firewall rules** are essential for controlling traffic flow between Virtual Machine (VM) instances. By default, all incoming traffic is **denied**, and all outgoing traffic is **allowed**. To enforce the desired communication patterns among your web, API, and database tiers, you can:

1. **Assign Network Tags to Each Tier:**
  - **Network tags** are labels that you can attach to VM instances, allowing you to **group instances** and apply firewall rules selectively.
  - For example:
    - Assign the tag `web-tier` to all web server instances.
    - Assign the tag `api-tier` to all API server instances.
    - Assign the tag `db-tier` to all database server instances.
2. **Create Firewall Rules Using These Tags:**
  - **Allow traffic** from the web tier to the API tier:
    - **Source filter:** `web-tier`
    - **Target filter:** `api-tier`
    - **Allowed protocols/ports:** Specify the necessary protocols and ports (e.g., TCP:80, TCP:443).
  - **Allow traffic** from the API tier to the database tier:
    - **Source filter:** `api-tier`
    - **Target filter:** `db-tier`
    - **Allowed protocols/ports:** Specify the necessary protocols and ports (e.g., TCP:3306 for MySQL).
  - **Deny direct traffic** from the web tier to the database tier:
    - **Source filter:** `web-tier`
    - **Target filter:** `db-tier`
    - **Denied protocols/ports:** All or specify as needed.

By implementing these steps, you ensure that:

- **Only authorized communication** occurs between the tiers.
- **Direct access** from the web tier to the database tier is **prevented**, adhering to the principle of least privilege.

**Official Documentation:**

- VPC firewall rules
- Using firewall rules with network tags

❌ Why Other Options Are Incorrect:

A. Assign each tier to a distinct subnetwork.

- **Subnetworks** primarily define **IP address ranges** and **routing domains**. While segmenting tiers into different subnetworks can provide **some level of isolation**, it does **not inherently control traffic flow** between them. You would still need to implement **firewall rules** to enforce the desired communication patterns.

B. Implement software-based firewalls on individual VMs.

- Managing **software-based firewalls** (e.g., `iptables` on Linux) on each VM introduces **operational complexity** and **inconsistencies**. Centralized management through **VPC firewall rules** is more **efficient**, **scalable**, and **aligned with Google Cloud best practices**.

C. Apply tags to each tier and establish routes to enable the desired traffic flow.

- **Routes** in Google Cloud determine how packets are **directed** within the network but do not **filter or control** traffic. To enforce **which traffic is allowed or denied**, you need to use **firewall rules**, not routes.

✅ Final Answer: **D**

Applying network tags to each tier and creating corresponding firewall rules allows you to **precisely control inter-tier communication**, ensuring that traffic flows only as intended while maintaining **security** and **compliance** with best practices.

References:

[https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

[https://cloud.google.com/vpc/docs/routes](https://cloud.google.com/vpc/docs/routes)

[https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)

</details>

---

### Exam 3 · Q43

**You need to create a duplicate of a production Linux VM currently running in the us-central1 region. The goal is to easily manage and update this copy when changes are made to the original VM. You plan to deploy this duplicate VM in a different Google Cloud project located in the us-east1 region. What steps should you take to achieve this?**

- A. Use Linux dd and netcat commands to stream the contents of the root disk directly to a new VM in the us-east1 region
- B. Take a snapshot of the root disk and use it as the boot disk when launching a new VM in the us-east1 region
- C. Use the dd command to create an image file of the root disk, then use this image to create a new VM in the us-east1 region
- D. Take a snapshot of the root disk, export it to a Cloud Storage bucket as an image file, and create a new VM in the us-east1 region using that image as the boot disk

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Take a snapshot of the root disk, export it to a Cloud Storage bucket as an image file, and create a new VM in the us-east1 region using that image as the boot disk

The correct answer is:
**D. Take a snapshot of the root disk, export it to a Cloud Storage bucket as an image file, and create a new VM in the us-east1 region using that image as the boot disk.**

✅ **Justification for Correct Option (D):**

To duplicate a production **Linux VM** from one **region and project** (e.g., `us-central1`) to another **region and project** (`us-east1`), the most reliable and scalable approach is:

1. **Take a snapshot** of the source VM's root disk.
2. **Create a custom image** from the snapshot.
3. **Export** the custom image to a **Cloud Storage bucket** (if transferring to another **project or region**).
4. **Import the image** into the destination project.
5. Use the image to **create a new VM** in `us-east1`.

This method:

- Ensures **cross-region and cross-project portability**
- Provides a **manageable image** that can be reused or updated
- Is **Google Cloud–supported and documented**

**Official Documentation:**

- Exporting a custom image to Cloud Storage
- Importing a custom image from Cloud Storage
- Creating VM from custom image

❌ **Why Other Options Are Incorrect:**

**A. Use Linux `dd` and `netcat` to stream disk content**

- This is a **manual and error-prone** method.
- It is **not scalable or secure** for cloud VM duplication.
- Doesn’t integrate well with Google Cloud’s **managed services** for VM creation or backup.

**B. Take a snapshot of the root disk and use it as the boot disk in** `us-east1`

- Snapshots are global resources and can, with the right IAM permission, boot a disk in another region or project, so B is workable. But a snapshot is a backup of one disk, not a reusable boot artifact. An **image** is the artifact meant for creating and refreshing VM copies.
- You must **export/import** the image for cross-region or cross-project usage.

**Reference:**
Snapshot storage location considerations

**C. Use `dd` to create a disk image and use it to create a new VM**

- Like A, this involves **manual disk imaging** and doesn’t use **GCP-native tools**.
- Using `dd` and image files requires additional conversion steps and doesn’t provide **managed lifecycle capabilities** like custom images do.

✅ **Final Answer: D**

This approach follows **Google Cloud best practices** for **duplicating VMs across regions and projects** using snapshots, images, and Cloud Storage for secure and manageable transfer.

Link - [https://cloud.google.com/compute/docs/instances/copy-vm-between-projects](https://cloud.google.com/compute/docs/instances/copy-vm-between-projects)

**⚠️ Note:** Exporting to a Cloud Storage file isn't strictly required: a custom image is global and can be shared with another project through IAM (`roles/compute.imageUser`), and image families make it easy to roll out a refreshed copy. Keep the key (image-based copy), but know that the export step is optional.

</details>

---

### Exam 3 · Q44

**SkyData Solutions** operates multiple databases on a single MySQL instance hosted on Google Cloud. The team needs to regularly back up one specific database. The backup process must be fast and should not cause any noticeable impact on disk performance.

How should the storage be set up to meet these requirements?

- A. Set up a cron job that uses the `gcloud` CLI to create periodic backups using persistent disk snapshots
- B. Attach a Local SSD volume to the instance for temporary backup storage, then transfer the backup to Cloud Storage using `gsutil`
- C. Mount a Cloud Storage bucket directly on the instance using `gcsfuse`, and use `mysqldump` to write backups to the mounted location
- D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage

**Correct answer: D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage.**

For this scenario, the key requirement is to back up **one specific MySQL database** from a MySQL instance that hosts **multiple databases**, while keeping the backup fast and avoiding noticeable disk-performance impact. Using separate storage volumes managed with LVM allows the database data to be isolated logically, and an LVM snapshot can capture the relevant volume quickly. RAID10 across persistent disks can also improve disk throughput and reduce the performance impact during backup operations.

Google Cloud documentation supports using multiple persistent disks with software RAID to improve throughput and IOPS, and Persistent Disk performance scales based on disk type, size, and configuration. Google also documents disk snapshots as a backup mechanism, but disk snapshots operate at the disk level rather than at the individual MySQL database level.
Reference: [Optimize Persistent Disk performance](https://cloud.google.com/compute/docs/disks/optimizing-pd-performance) and [Persistent Disk snapshots](https://cloud.google.com/compute/docs/disks/snapshots)

**Why the other options are not the best choice**

A. **Incorrect.** Persistent Disk snapshots are fast and useful for backups, but they capture an entire disk, not one specific MySQL database. If multiple databases share the same disk, this does not meet the requirement to back up only one database.

B. **Incorrect.** Local SSD is high-performance temporary storage, but it is ephemeral and not suitable as a reliable backup target. Google Cloud states that Local SSD data is not durable and should be copied to durable storage if it must be preserved.
Reference: [About Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd)

C. **Incorrect.** Mounting Cloud Storage with Cloud Storage FUSE and writing `mysqldump` output directly to it can introduce higher latency than a local file system. It also performs a logical dump, which can significantly affect MySQL read I/O and database performance. Google Cloud notes that Cloud Storage FUSE has higher latency than local file systems and should not be used as a database backend.
Reference: [Cloud Storage FUSE overview](https://cloud.google.com/storage/docs/cloud-storage-fuse/overview)

**Need-to-know foundational concept**

Persistent Disk snapshots are excellent when you need disk-level backups. However, when the requirement is to back up **one specific database** from a MySQL instance hosting multiple databases, the storage layout must isolate that database at the volume level. That is why an LVM-based setup with performance-optimized persistent disks is the best fit among the given options.

###### Explanation

**Correct answer: D. Attach multiple persistent disks to the VM, configure them in a RAID10 array, and use LVM snapshots for backups, which are then uploaded to Cloud Storage.**

For this scenario, the key requirement is to back up **one specific MySQL database** from a MySQL instance that hosts **multiple databases**, while keeping the backup fast and avoiding noticeable disk-performance impact. Using separate storage volumes managed with LVM allows the database data to be isolated logically, and an LVM snapshot can capture the relevant volume quickly. RAID10 across persistent disks can also improve disk throughput and reduce the performance impact during backup operations.

Google Cloud documentation supports using multiple persistent disks with software RAID to improve throughput and IOPS, and Persistent Disk performance scales based on disk type, size, and configuration. Google also documents disk snapshots as a backup mechanism, but disk snapshots operate at the disk level rather than at the individual MySQL database level.
Reference: [Optimize Persistent Disk performance](https://cloud.google.com/compute/docs/disks/optimizing-pd-performance) and [Persistent Disk snapshots](https://cloud.google.com/compute/docs/disks/snapshots)

> [!note]- Why the other options are wrong
> A. **Incorrect.** Persistent Disk snapshots are fast and useful for backups, but they capture an entire disk, not one specific MySQL database. If multiple databases share the same disk, this does not meet the requirement to back up only one database.
>
> B. **Incorrect.** Local SSD is high-performance temporary storage, but it is ephemeral and not suitable as a reliable backup target. Google Cloud states that Local SSD data is not durable and should be copied to durable storage if it must be preserved.
> Reference: [About Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd)
>
> C. **Incorrect.** Mounting Cloud Storage with Cloud Storage FUSE and writing `mysqldump` output directly to it can introduce higher latency than a local file system. It also performs a logical dump, which can significantly affect MySQL read I/O and database performance. Google Cloud notes that Cloud Storage FUSE has higher latency than local file systems and should not be used as a database backend.
> Reference: [Cloud Storage FUSE overview](https://cloud.google.com/storage/docs/cloud-storage-fuse/overview)

**⚠️ Note:** This key is debated. LVM snapshots are copy-on-write, so they add write overhead while they exist, and they capture a whole volume, not one database. Many candidates prefer B (dump the one database to Local SSD, which doesn't share Persistent Disk performance, then copy it to Cloud Storage). Answer D if you see this exact wording.

</details>

---

### Exam 3 · Q48

**You are managing a running Google Kubernetes Engine (GKE) cluster for AppVantage Corp. and want to ensure it automatically scales as application demand fluctuates.**

**What action should you take?**

- A. Manually scale the cluster by running: `gcloud container clusters resize CLUSTER_NAME --size 10`
- B. Add a tag to the cluster instances to enable autoscaling using: `gcloud compute instances add-tags INSTANCE_NAME --tags enable-autoscaling,max-nodes-10`
- C. Enable autoscaling on the existing cluster by executing: `gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`
- D. Create a new cluster with autoscaling enabled and redeploy your app using: `gcloud alpha container clusters create mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Enable autoscaling on the existing cluster by executing: `gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

✅ **Correct Answer:**

**C. Enable autoscaling on the existing cluster by executing:**
`gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

✅ **Justification for Option C:**

- This command uses the `gcloud` CLI to **update an existing cluster** and **enable autoscaling**.
- You can configure **minimum and maximum node counts**, which allow GKE’s **Cluster Autoscaler** to automatically add/remove nodes based on pod resource requests and current usage.

**Note:** Although this command uses `gcloud alpha`, it might also be supported under `gcloud container clusters update` in **GA or beta** depending on your SDK version. Always verify based on the active gcloud release.

**Official GCP Documentation:**

- Cluster autoscaler:
  [https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
- Enabling autoscaling:
  [https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enabling_autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enabling_autoscaling)

❌ **Why the Other Options Are Incorrect:**

**A. Manually scale the cluster by running:

`gcloud container clusters resize CLUSTER_NAME --size 10`**

- This **resizes the cluster manually**, setting a fixed node count.
- It does **not provide automatic scaling** based on demand.
- Does not meet the requirement of **automatic scaling**.

**Reference:**
[https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize)

**B. Add a tag to the cluster instances to enable autoscaling using:

`gcloud compute instances add-tags INSTANCE_NAME --tags enable-autoscaling,max-nodes-10`**

- GKE **autoscaling is not enabled by setting instance tags**.
- Tags are used for **network/firewall rules**, not for controlling autoscaler behavior.
- GKE autoscaler is configured via the `gcloud container clusters` or UI/API, **not via instance tags**.

**Reference:**
[https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags)
(No link between tags and autoscaling behavior.)

**D. Create a new cluster with autoscaling enabled and redeploy your app using:

`gcloud alpha container clusters create mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`**

- While this command **does enable autoscaling**, it **creates a new cluster**, which:
  - **Is not required** since the question says you’re managing a **running cluster**
  - Requires **redeployment of applications**, which is unnecessary and disruptive.

This is a **more destructive approach** than needed.

✅ Final Answer:

**C. Enable autoscaling on the existing cluster by executing:**
`gcloud alpha container clusters update mycluster --enable-autoscaling --min-nodes=1 --max-nodes=10`

**⚠️ Note:** Cluster autoscaling is GA; you no longer need the `alpha` track. Today's form is `gcloud container clusters update CLUSTER --enable-autoscaling --node-pool=POOL --min-nodes=1 --max-nodes=10`. The point still holds: update the existing cluster instead of recreating it.

</details>

---

### Exam 3 · Q64

**CloudLink Inc.** has recently acquired **NetFusion Ltd.**, and both companies operate their infrastructure on **Google Cloud**, each within its **own Google Cloud Organization**. Both organizations use **Shared VPCs** to manage network connectivity for their applications.

Some of the **subnets in both environments overlap**, but the applications that need to communicate **do not reside in the overlapping subnets**. You are tasked with enabling **private network connectivity** between these applications with **minimal re-engineering**.

What should you do?

- A. Set up **VPC Network Peering** between the two Shared VPCs.
- B. **Migrate the acquired company's projects** into your organization's Cloud Organization, and **relaunch the instances** into your Shared VPC.
- C. Set up a **Cloud VPN gateway** in each Shared VPC and **establish a VPN connection** between them.
- D. Use **SSH port forwarding** to connect applications between the two Shared VPCs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Set up a **Cloud VPN gateway** in each Shared VPC and **establish a VPN connection** between them.

✅ Correct Answer:

**C. Set up a Cloud VPN gateway in each Shared VPC and establish a VPN connection between them.**

✅ Why Option C is Correct:

- **Cloud VPN** is supported for **cross-organization connectivity** and **works between Shared VPC networks**.
- It **allows private, secure communication** over the public internet, or via **Cloud Interconnect** if needed.
- **Subnets can overlap** as long as the communicating instances are in **non-overlapping IP ranges**.
- **Minimal re-engineering** is needed:
  - No need to migrate projects
  - No need to redesign or merge networks
- It's a **Google-recommended approach** for inter-org connectivity when peering is not viable due to constraints like overlapping IP ranges.

**Official Documentation:**

- VPN Overview
- Connecting VPC networks across organizations

❌ Why Other Options Are Incorrect:

**A. Set up VPC Network Peering between the two Shared VPCs**

- **Not supported** across different organizations when **IP address ranges overlap**, even partially.
- VPC Peering does **not support transitive routing**, and **Shared VPCs themselves cannot be directly peered across orgs** in overlapping IP scenarios.

**Reference:**
[https://cloud.google.com/vpc/docs/vpc-peering#restrictions](https://cloud.google.com/vpc/docs/vpc-peering#restrictions)

**B. Migrate the acquired company's projects into your organization's Cloud Organization and relaunch the instances**

- This involves **significant re-engineering**:
  - Project migration
  - Instance re-creation
  - Network and IAM reconfiguration
- **High risk**, **time-consuming**, and unnecessary for simple private connectivity.

**D. Use SSH port forwarding to connect applications between the two Shared VPCs**

- **Not a scalable or secure solution**
- Requires:
  - Manual port forwarding setups
  - SSH access and credentials
  - Custom scripts and maintenance
- **Not enterprise-grade** or compliant for production workloads

✅ Final Answer:

**C. Set up a Cloud VPN gateway in each Shared VPC and establish a VPN connection between them.**

</details>

---

### Exam 4 · Q2

TechNova Corp and one of its key collaborators each manage their own Google Cloud projects under different organizations. TechNova's project (project-alpha) uses a Virtual Private Cloud named vpc-alpha, while the collaborator's project (project-beta) operates in vpc-beta. Within vpc-alpha, there are two compute instances running, and vpc-beta contains one compute instance. The IP subnets across both VPCs are non-overlapping.

You’ve been asked to ensure **low-latency, high-throughput internal IP communication** between all compute instances across both VPCs. What should you do?

- A. Establish VPC Network Peering between vpc-alpha and vpc-beta.
- B. Set up a Cloud VPN tunnel to connect vpc-alpha and vpc-beta.
- C. Enable IAP TCP forwarding on the instance in vpc-beta, and from an instance in vpc-alpha, run the following command: gcloud compute start-iap-tunnel INSTANCE_NAME_IN_VPC_B 22 --local-host-port=localhost:22
- D. Launch a new instance in vpc-alpha. Launch a new instance in vpc-beta. Install OpenVPN on both newly created instances. Set up a VPN tunnel between vpc-alpha and vpc-beta using OpenVPN.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Establish VPC Network Peering between vpc-alpha and vpc-beta.

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

</details>

---

### Exam 4 · Q3

Your organization, **DataVerse Solutions**, needs to store sensitive business data in Google Cloud Storage buckets. This data is frequently updated, but past versions must remain accessible for reference. You also need to maintain a complete history of changes made to any object in these buckets. Furthermore, it should be easy to recover from accidental edits or deletions.

Which Cloud Storage feature should you enable to meet these requirements?

- A. **Bucket Lock** – Enforce retention policies to prevent deletion or modification of objects for a set period.
- B. **Object Versioning** – Maintain multiple versions of an object, allowing access to older versions when needed.
- C. **Object Change Notification** – Receive notifications whenever an object in the bucket is modified.
- D. **Object Lifecycle Management** – Automate deletion or transition of objects to different storage classes based on defined rules.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Object Versioning** – Maintain multiple versions of an object, allowing access to older versions when needed.

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

</details>

---

### Exam 4 · Q4

You’re managing a Compute Engine-based application for **CloudNexus Inc.** that needs to automatically scale when memory usage exceeds 80%. You've installed the Cloud Monitoring agent and configured the following autoscaling policy:

- **Metric Identifier**: `agent.googleapis.com/memory/percent_used`
- **Filter**: `metric.label.state = 'used'`
- **Target Utilization Level**: `80`
- **Target Type**: `GAUGE`

However, the application does **not scale up** under heavy memory load. You need to fix the configuration so autoscaling works as expected.

What should you do?

- A. Change the **Target Type** to `DELTA_PER_MINUTE`.
- B. Change the **Metric Identifier** to `agent.googleapis.com/memory/bytes_used`.
- C. Modify the **Filter** to: `metric.label.state = 'used' AND metric.label.state = 'buffered' AND metric.label.state = 'cached' AND metric.label.state = 'slab'`.
- D. Update the **Filter** to: `metric.label.state = 'free'` and change the **Target Utilization Level** to `20`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Update the **Filter** to: `metric.label.state = 'free'` and change the **Target Utilization Level** to `20`.

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

</details>

---

### Exam 4 · Q5

You’re deploying an application to Google Cloud for **NextPhase Systems**. This application is part of a broader system that includes services running outside Google Cloud. The Google Cloud-hosted application must establish private network communication with external (non-GCP) applications. The expected **average network throughput is 200 kbps**.

The business requires:

- **Maximum possible system availability (near 100%)**
- **Cost-effective solution**

You need to design the network connectivity between Google Cloud and the external environment to meet these goals.

What should you implement?

- A. Provision an **HA (High Availability) Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.
- B. Set up **two Classic Cloud VPN gateways**, each with two tunnels, and connect them to separate on-premises VPN gateways.
- C. Deploy **two HA Cloud VPN gateways**, each with two tunnels connected to different on-premises VPN gateways.
- D. Use a **single Cloud VPN gateway** connected to the on-premises VPN gateway.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Provision an **HA (High Availability) Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.

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

</details>

---

### Exam 4 · Q7

You're setting up the network architecture for a newly launched project at **NovaEdge Technologies**, which will host applications on Google Compute Engine. Virtual machine (VM) instances will be deployed in **two different subnets** within a single region:

- Instances in `subnet-alpha` will have public IP addresses.
- Instances in `subnet-beta` will use only private IP addresses.

To keep their software up to date, all instances must be able to **access a public package repository** hosted outside of Google Cloud.

How can you allow instances in `subnet-beta` to reach the external repository?

- A. Enable **Private Google Access** for `subnet-beta`.
- B. Set up **Cloud NAT** and include `subnet-beta` in the NAT subnet configuration.
- C. Deploy a **bastion host** in `subnet-alpha` and use it to proxy traffic for instances in `subnet-beta`.
- D. Enable **Identity-Aware Proxy (IAP)** for TCP forwarding on the instances in `subnet-beta`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Set up **Cloud NAT** and include `subnet-beta` in the NAT subnet configuration.

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

</details>

---

### Exam 4 · Q9

You’re deploying an application to Google Cloud for **EdgeBridge Solutions**. This application is part of a distributed system that includes components running outside of Google Cloud. The application deployed in GCP must communicate over a **private network** with external systems running in an on-premises environment.

The expected **average network throughput is 200 kbps**, and the business has the following requirements:

- **99.99% system availability**
- **Cost-effective connectivity**

You need to design the hybrid connectivity between the two environments to meet these requirements.

**What should you implement?**

- A. Deploy an **HA Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.
- B. Use a **Classic Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.
- C. Deploy **two HA Cloud VPN gateways**, each connected to separate on-premises VPN gateways. Configure each with two tunnels connecting to different on-prem VPNs.
- D. Use a **Classic Cloud VPN gateway** with a single tunnel connected to the on-premises VPN gateway.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy an **HA Cloud VPN gateway** with two tunnels connected to the on-premises VPN gateway.

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

</details>

---

### Exam 4 · Q19

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

- A. Integrate a new Dedicated Interconnect connection.
- B. Enhance the bandwidth on the existing Dedicated Interconnect connection to 100 G.
- C. Implement three new Cloud VPN connections.
- D. Integrate a new Carrier Peering connection.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Integrate a new Dedicated Interconnect connection.

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

</details>

---

### Exam 4 · Q20

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

- A. Configure two Partner Interconnect connections in one metro (City), ensuring placement in different metro zones.
- B. Set up two VPN connections from on-premises to Google Cloud, ensuring that the VPN devices on-premises are in separate racks.
- C. Establish Direct Peering between EHR Healthcare and Google Cloud, ensuring peering at least two Google locations.
- D. Configure two Dedicated Interconnect connections in one metro (City) and two connections in another metro, ensuring placement in different metro zones.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure two Dedicated Interconnect connections in one metro (City) and two connections in another metro, ensuring placement in different metro zones.

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

</details>

---

### Exam 4 · Q40

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

- A. Set up a global load balancer connected to a managed instance group running Compute Engine instances.
- B. Utilize kubemci in conjunction with a global load balancer and Google Kubernetes Engine.
- C. Establish a global load balancer integrated with Google Kubernetes Engine.
- D. Implement Ingress for Anthos alongside a global load balancer and Google Kubernetes Engine.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up a global load balancer connected to a managed instance group running Compute Engine instances.

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

</details>

---

### Exam 4 · Q45

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

- A. Deploy the Cloud Run services across multiple availability zones. Configure Cloud Endpoints to direct traffic to these services. Set up a global HTTP(S) Load Balancer and link the Cloud Endpoints to its backend.
- B. Spread the Cloud Run services across multiple regions. Establish serverless network endpoint groups (NEGs) that point to these services. Integrate the serverless NEGs into a backend service utilized by a global HTTP(S) Load Balancing instance.
- C. Deploy the Cloud Run services across multiple regions. Utilize Cloud DNS to create a latency-based DNS name directing to these services.
- D. Deploy the Cloud Run services across multiple availability zones. Implement a TCP/IP global load balancer and incorporate the Cloud Run Endpoints into its backend service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Spread the Cloud Run services across multiple regions. Establish serverless network endpoint groups (NEGs) that point to these services. Integrate the serverless NEGs into a backend service utilized by a global HTTP(S) Load Balancing instance.

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

</details>

---

### Exam 4 · Q53

**Your company has a project in Google Cloud with three Virtual Private Clouds (VPCs). There is a Compute Engine instance on each VPC. Network subnets do not overlap and must remain separated. The network configuration is shown below. Instance #1 is an exception and must communicate directly with both Instance #2 and Instance #3 via internal IPs. How should you accomplish this?**

![Network diagram: VPC#1, VPC#2 and VPC#3, each with one subnet and one Compute Engine instance (Instance1, Instance2, Instance3)](assets/img/gpca/e4q53-network.jpg)

- A. Create a cloud router to advertise subnet #2 and subnet #3 to subnet #1.
- B. Add two additional NICs to Instance #1 with the following configuration: NIC1: VPC: VPC #2, SUBNETWORK: subnet #2 NIC2: VPC: VPC #3, SUBNETWORK: subnet #3 Update firewall rules to enable traffic between instances.
- C. Create two VPN tunnels via CloudVPN: 1 between VPC #1 and VPC #2. 1 between VPC #2 and VPC #3. Update firewall rules to enable traffic between the instances.
- D. Peer all three VPCs: Peer VPC #1 with VPC #2. Peer VPC #2 with VPC #3. Update firewall rules to enable traffic between the instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Add two additional NICs to Instance #1 with the following configuration: NIC1: VPC: VPC #2, SUBNETWORK: subnet #2 NIC2: VPC: VPC #3, SUBNETWORK: subnet #3 Update firewall rules to enable traffic between instances.

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

</details>

---

### Exam 4 · Q55

For this question, refer to the EHR Healthcare case study. https://services.google.com/fh/files/blogs/master_case_study_ehr_healthcare.pdf

**When connecting an EHR data center situated over 100 kilometers from the closest major city to Google Cloud using a high-bandwidth, low-latency microwave connection, what factors should be considered in designing the network connection?**

- A. Implement Carrier Peering provisioning.
- B. Establish a new Internet connection.
- C. Set up Partner Interconnect provisioning.
- D. Implement Dedicated Interconnect provisioning.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Set up Partner Interconnect provisioning.

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

</details>

---

### Exam 4 · Q64

**You're tasked with designing a future-proof hybrid environment requiring network connectivity between Google Cloud and your on-premises setup. Your aim is to ensure compatibility between the Google Cloud environment and your on-premises networking environment. What steps should you take?**

- A. Opt for the default VPC in your Google Cloud project and establish a Cloud VPN connection between your on-premises environment and Google Cloud.
- B. Create a custom VPC in Google Cloud in auto mode and set up a Cloud VPN connection between your on-premises environment and Google Cloud.
- C. Develop a network plan for your VPC in Google Cloud that utilizes CIDR ranges overlapping with your on-premises environment. Utilize a Cloud Interconnect connection between your on-premises environment and Google Cloud.
- D. Design a network plan for your VPC in Google Cloud with CIDR ranges that do not overlap with your on-premises environment. Deploy a Cloud Interconnect connection between your on-premises environment and Google Cloud.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Design a network plan for your VPC in Google Cloud with CIDR ranges that do not overlap with your on-premises environment. Deploy a Cloud Interconnect connection between your on-premises environment and Google Cloud.

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

</details>

---

### Exam 5 · Q2

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

**Altostrat operates both on-premises ingestion systems and Google Cloud–based media processing services. They need secure, high-performance hybrid connectivity to ingest large media files while minimizing operational overhead and ensuring predictable latency.**

**Which hybrid networking design best meets these requirements?**

- A. Use Cloud VPN with multiple tunnels and rely on application-level retries for throughput optimization.
- B. Implement Partner Interconnect with redundant VLAN attachments and dynamic routing using Cloud Router.
- C. Deploy Dedicated Interconnect with a single 10-Gbps connection and static routing to reduce cost.
- D. Transfer media using Storage Transfer Service scheduled jobs over the public internet.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Implement Partner Interconnect with redundant VLAN attachments and dynamic routing using Cloud Router.

**Correct option: B**

**Why B is best (secure, high-performance, predictable latency, low ops):**

- **Partner Interconnect** provides private connectivity into Google Cloud through a service provider, which is the right fit for **large media ingestion** needing **consistent performance** and **predictable latency** compared to internet-based paths.
- Using **redundant VLAN attachments** addresses availability and stability requirements (designed patterns exist specifically for high availability with Partner Interconnect). [Google Cloud Documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability)
- **Cloud Router** provides **dynamic routing (BGP)** for Partner Interconnect, reducing operational overhead (automatic route exchange/failover) and supporting resilient designs. [Google Cloud Documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)

**Why the others are not the best fit:**

**A. Cloud VPN (multiple tunnels)**

- Cloud VPN is positioned as a **lower-cost option for low-volume** connectivity and runs over the **public internet**, making **predictable latency** and sustained high-throughput ingestion harder to guarantee at scale versus Interconnect. [Google Cloud](https://cloud.google.com/hybrid-connectivity)

**C. Dedicated Interconnect with a single 10-Gbps + static routing**

- “Single connection” is a red flag for reliability: Google’s Interconnect availability designs typically require **at least two connections** for higher availability, and Cloud Router/BGP is the standard approach for dynamic routing. [Google Cloud Documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability)

**D. Storage Transfer Service over public internet**

- Storage Transfer Service is great for scheduled/managed transfers, but it does not meet the requirement for **predictable latency** and **high-performance hybrid connectivity** for ongoing ingestion; the requirement is explicitly “hybrid connectivity,” which points to Interconnect/VPN designs rather than batch transfer tooling. [Google Cloud Documentation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)

**Single authoritative documentation link:**
Google Cloud guidance for selecting hybrid connectivity products (Interconnect vs VPN, etc.): [Google Cloud D](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)

###### Explanation

**Correct option: B**

**Why B is best (secure, high-performance, predictable latency, low ops):**

- **Partner Interconnect** provides private connectivity into Google Cloud through a service provider, which is the right fit for **large media ingestion** needing **consistent performance** and **predictable latency** compared to internet-based paths.
- Using **redundant VLAN attachments** addresses availability and stability requirements (designed patterns exist specifically for high availability with Partner Interconnect). [Google Cloud Documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability)
- **Cloud Router** provides **dynamic routing (BGP)** for Partner Interconnect, reducing operational overhead (automatic route exchange/failover) and supporting resilient designs. [Google Cloud Documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)

> [!note]- Why the other options are wrong
> **A. Cloud VPN (multiple tunnels)**
>
> - Cloud VPN is positioned as a **lower-cost option for low-volume** connectivity and runs over the **public internet**, making **predictable latency** and sustained high-throughput ingestion harder to guarantee at scale versus Interconnect. [Google Cloud](https://cloud.google.com/hybrid-connectivity)
>
> **C. Dedicated Interconnect with a single 10-Gbps + static routing**
>
> - “Single connection” is a red flag for reliability: Google’s Interconnect availability designs typically require **at least two connections** for higher availability, and Cloud Router/BGP is the standard approach for dynamic routing. [Google Cloud Documentation](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability)
>
> **D. Storage Transfer Service over public internet**
>
> - Storage Transfer Service is great for scheduled/managed transfers, but it does not meet the requirement for **predictable latency** and **high-performance hybrid connectivity** for ongoing ingestion; the requirement is explicitly “hybrid connectivity,” which points to Interconnect/VPN designs rather than batch transfer tooling. [Google Cloud Documentation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)

</details>

---

### Exam 5 · Q3

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

**Altostrat wants to reduce cloud storage costs while maintaining high availability and low-latency access for frequently accessed media content. Older content must remain durable but can tolerate higher access latency.**

**Which storage strategy should you recommend?**

- A. Store all content in Standard Cloud Storage with lifecycle rules to delete unused objects.
- B. Use a dual-bucket strategy with Standard Storage for new content and Coldline Storage for archived media, accessed via signed URLs.
- C. Implement lifecycle rules to automatically transition objects from Standard to Nearline and then to Coldline or Archive Storage based on access patterns.
- D. Migrate older content to BigQuery tables to reduce Cloud Storage usage and query media metadata directly.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Implement lifecycle rules to automatically transition objects from Standard to Nearline and then to Coldline or Archive Storage based on access patterns.

**Correct option: C**

**Why C is best**

- Altostrat needs **low-latency access for frequently accessed media** and **lower cost for older content that can tolerate higher latency**. Cloud Storage lifecycle management is built for exactly this: keep objects in **Standard** when hot, then **automatically transition** them to **Nearline → Coldline → Archive** as they age or based on policy, without changing application endpoints. [Google Cloud Documentation](https://docs.cloud.google.com/storage/docs/lifecycle)

**Why the other options are not best**

**A. Standard + delete unused**

- This reduces cost by deleting, but the requirement says **older content must remain durable** (not deleted). It also doesn’t optimize storage cost for retained long-tail media.

**B. Dual-bucket Standard + Coldline + signed URLs**

- Storage class choice is reasonable, but a **manual dual-bucket strategy** adds operational overhead and rigidity. Also, signed URLs are an access-control mechanism, not a cost/availability strategy, and you don’t need separate buckets to manage storage class transitions. [Google Cloud Documentation](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

**D. Move media into BigQuery**

- BigQuery is for analytics/structured data; it’s not a replacement for storing large binary media objects, and this doesn’t meet the “low-latency media access” goal.

**Single authoritative documentation link:**
Cloud Storage Object Lifecycle Management (automatic storage-class transitions and retention actions). [Google Cloud Documentation](https://docs.cloud.google.com/storage/docs/lifecycle)

###### Explanation

**Correct option: C**

**Why C is best**

- Altostrat needs **low-latency access for frequently accessed media** and **lower cost for older content that can tolerate higher latency**. Cloud Storage lifecycle management is built for exactly this: keep objects in **Standard** when hot, then **automatically transition** them to **Nearline → Coldline → Archive** as they age or based on policy, without changing application endpoints. [Google Cloud Documentation](https://docs.cloud.google.com/storage/docs/lifecycle)

> [!note]- Why the other options are wrong
> **A. Standard + delete unused**
>
> - This reduces cost by deleting, but the requirement says **older content must remain durable** (not deleted). It also doesn’t optimize storage cost for retained long-tail media.
>
> **B. Dual-bucket Standard + Coldline + signed URLs**
>
> - Storage class choice is reasonable, but a **manual dual-bucket strategy** adds operational overhead and rigidity. Also, signed URLs are an access-control mechanism, not a cost/availability strategy, and you don’t need separate buckets to manage storage class transitions. [Google Cloud Documentation](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)
>
> **D. Move media into BigQuery**
>
> - BigQuery is for analytics/structured data; it’s not a replacement for storing large binary media objects, and this doesn’t meet the “low-latency media access” goal.

</details>

---

### Exam 5 · Q7

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

**For this question, refer to the Altostrat Media case study. Altostrat is facing variable compute demand for its batch processing workloads. These jobs are not time-sensitive and can withstand occasional interruptions. You want to reduce cloud costs while still meeting the batch processing requirements. What should you do?**

- A. Configure reserved VM instances
- B. Deploy spot VM instances
- C. Use standard VM instances
- D. Use Cloud Run functions

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Deploy spot VM instances

**Correct option: B — Deploy spot VM instances**

Spot VMs are designed exactly for **interruptible, fault-tolerant batch workloads** where cost optimization is more important than guaranteed availability. Altostrat’s jobs are not time-sensitive and can tolerate interruptions, which aligns perfectly with Spot VM behavior. Spot VMs can be preempted, but they provide **deep discounts compared to standard VMs**, making them ideal for batch processing pipelines that can retry or resume work.

**Authoritative documentation:**
[https://cloud.google.com/compute/docs/instances/spot](https://cloud.google.com/compute/docs/instances/spot)

**Why B is correct**

- Spot VMs offer the **lowest-cost compute option** in Compute Engine
- They are intended for **batch, stateless, or retryable workloads**
- They may be terminated at any time, but the workload design already tolerates interruption
- Google explicitly recommends them for **cost-optimized batch processing**

This directly matches the case study’s requirements: variable demand + interruption-tolerant jobs + cost reduction.

**Why the other options are not the best choice**

A. Reserved VM instances
Reservations guarantee capacity but **do not reduce cost** for unpredictable or bursty workloads. They are used when you must guarantee availability, not when you want maximum savings. This conflicts with the goal of minimizing cost for flexible workloads.

C. Standard VM instances
Standard VMs provide stability but are **the most expensive option** for batch jobs that don’t need guaranteed uptime. They don’t leverage the interruption tolerance of the workload.

D. Cloud Run functions
Cloud Run is optimized for **event-driven, request/response serverless workloads**, not large-scale batch compute pipelines. It is not a direct replacement for VM-based batch processing that needs custom runtime environments or long-running compute jobs.

**Need-to-know foundational concept**

Google Cloud compute pricing follows a tradeoff triangle:

- **Standard VMs** → highest stability, highest cost
- **Reserved capacity** → guaranteed availability, predictable workloads
- **Spot VMs** → lowest cost, interruptible, ideal for batch jobs

The architectural principle:
If a workload is **fault-tolerant and restartable**, you should design it to run on **Spot capacity** to dramatically reduce compute spend.

This is a common Professional Cloud Architect exam theme: match workload tolerance to the cheapest appropriate compute model.

###### Explanation

**Correct option: B — Deploy spot VM instances**

Spot VMs are designed exactly for **interruptible, fault-tolerant batch workloads** where cost optimization is more important than guaranteed availability. Altostrat’s jobs are not time-sensitive and can tolerate interruptions, which aligns perfectly with Spot VM behavior. Spot VMs can be preempted, but they provide **deep discounts compared to standard VMs**, making them ideal for batch processing pipelines that can retry or resume work.

> [!note]- Why the other options are wrong
> A. Reserved VM instances
> Reservations guarantee capacity but **do not reduce cost** for unpredictable or bursty workloads. They are used when you must guarantee availability, not when you want maximum savings. This conflicts with the goal of minimizing cost for flexible workloads.
>
> C. Standard VM instances
> Standard VMs provide stability but are **the most expensive option** for batch jobs that don’t need guaranteed uptime. They don’t leverage the interruption tolerance of the workload.
>
> D. Cloud Run functions
> Cloud Run is optimized for **event-driven, request/response serverless workloads**, not large-scale batch compute pipelines. It is not a direct replacement for VM-based batch processing that needs custom runtime environments or long-running compute jobs.

</details>

---

### Exam 5 · Q22

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

**For this question, refer to the KnightMotives Automotive case study. KnightMotives has built a new car configurator application to improve both dealer and customer experience. The application will run on Google Kubernetes Engine (GKE). KnightMotives wants the deployment replicated across multiple geographic locations so the application remains available on the internet even if an entire region fails. What should you do?**

- A. Create GKE clusters in multiple regions, distribute different microservices across the clusters, and configure a multi-cluster Cloud Service Mesh.
- B. Create GKE clusters in multiple regions, deploy the full application to each cluster, and configure a multi-cluster Cloud Service Mesh.
- C. Create a fleet of GKE clusters in multiple regions, distribute different microservices across the clusters, and configure a multi-cluster Gateway.
- D. Create a fleet of GKE clusters in multiple regions, deploy the full application to each cluster, and configure a multi-cluster Gateway.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create a fleet of GKE clusters in multiple regions, deploy the full application to each cluster, and configure a multi-cluster Gateway.

**Correct answer: D**

**Create a fleet of GKE clusters in multiple regions, deploy the full application to each cluster, and configure a multi-cluster Gateway.**

**Why option D is correct**

KnightMotives explicitly wants **regional failure resilience**. That means if an entire Google Cloud region goes down, the car configurator must still work globally. The only safe pattern is **active-active full replication** of the application stack in multiple regions.

Option D does exactly that:

- A **fleet** lets you manage multiple clusters as one logical platform
- Each region runs a **complete copy** of the application
- A **multi-cluster Gateway** provides global load balancing and failover
- Traffic is automatically routed to healthy regions

If a region fails, traffic shifts to another region because every cluster is capable of serving the entire workload. No dependency chain exists between regions.

This aligns perfectly with the case study requirement for high availability and internet-facing reliability.

Authoritative documentation supporting this architecture:
[https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways](https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways)

**Why the other options are not the best choice**

**Option A**
Distributing microservices across regions creates cross-region dependencies. If one region fails, some services disappear and the application becomes partially broken. This violates the requirement that the app remain available even during a regional outage.

Also, Cloud Service Mesh is about service-to-service communication, not global availability routing.

**Option B**
This replicates the full application correctly, but uses **Cloud Service Mesh**, which is not designed for global ingress failover. You still need a multi-cluster ingress/Gateway layer for regional traffic routing. Mesh solves service networking, not global entry traffic resilience.

**Option C**
This correctly uses a fleet and multi-cluster Gateway, but again distributes microservices instead of fully replicating them. That creates a single-region dependency for certain components, which breaks availability guarantees.

Only option D ensures **independent, region-complete deployments** plus **global routing**.

**Need-to-know foundational concept**

For regional disaster resilience in GKE:

- Every region must be able to run the **entire application stack**
- No region should depend on another region to serve requests
- Global availability requires **multi-cluster ingress**, not just service mesh
- Multi-cluster Gateway acts as a globally aware entry point
- GKE fleets provide centralized management of many clusters

This pattern is often called **active-active multi-region architecture**, and it is the gold standard for internet-facing systems that must survive full regional outages.

###### Explanation

**Correct answer: D**

**Create a fleet of GKE clusters in multiple regions, deploy the full application to each cluster, and configure a multi-cluster Gateway.**

**Why option D is correct**

KnightMotives explicitly wants **regional failure resilience**. That means if an entire Google Cloud region goes down, the car configurator must still work globally. The only safe pattern is **active-active full replication** of the application stack in multiple regions.

Option D does exactly that:

- A **fleet** lets you manage multiple clusters as one logical platform
- Each region runs a **complete copy** of the application
- A **multi-cluster Gateway** provides global load balancing and failover
- Traffic is automatically routed to healthy regions

If a region fails, traffic shifts to another region because every cluster is capable of serving the entire workload. No dependency chain exists between regions.

This aligns perfectly with the case study requirement for high availability and internet-facing reliability.

> [!note]- Why the other options are wrong
> **Option A**
> Distributing microservices across regions creates cross-region dependencies. If one region fails, some services disappear and the application becomes partially broken. This violates the requirement that the app remain available even during a regional outage.
>
> Also, Cloud Service Mesh is about service-to-service communication, not global availability routing.
>
> **Option B**
> This replicates the full application correctly, but uses **Cloud Service Mesh**, which is not designed for global ingress failover. You still need a multi-cluster ingress/Gateway layer for regional traffic routing. Mesh solves service networking, not global entry traffic resilience.
>
> **Option C**
> This correctly uses a fleet and multi-cluster Gateway, but again distributes microservices instead of fully replicating them. That creates a single-region dependency for certain components, which breaks availability guarantees.

</details>

---

### Exam 5 · Q24

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

**For this question, refer to the KnightMotives Automotive case study. KnightMotives has deployed its new Dealer Tools on Google Kubernetes Engine (GKE). You are helping optimize performance of the GKE workloads. Some Pods are stateful, and CPU limits are already configured so they cannot consume unlimited resources. Monitoring shows the Pods were overprovisioned and frequently use far less CPU than allocated. You want to improve resource efficiency while still allowing flexibility during traffic spikes. What should you do?**

- A. Configure CPU resource requests per Deployment and set them slightly above the typical observed usage.
- B. Configure CPU resource requests per Deployment and make them equal to the current limits.
- C. Enable Vertical Pod Autoscaling for each Deployment and set the autoscaling mode to Auto.
- D. Enable Horizontal Pod Autoscaling for each Deployment and reduce the minimum replica count below the currently configured number.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure CPU resource requests per Deployment and set them slightly above the typical observed usage.

**Correct answer: A**

**Configure CPU resource requests per Deployment and set them slightly above the typical observed usage.**

**Authoritative documentation link (supports why A is correct):**
[https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits?utm_source=chatgpt.com)

**Why option A is correct**

Your monitoring shows Pods are **overprovisioned** (they request/are allocated far more CPU than they usually use). In Kubernetes:

- **CPU requests** drive **scheduling and bin-packing** (how many Pods fit on a node).
- **CPU limits** cap maximum CPU the container can use (prevent “unlimited” consumption).

So if you reduce **requests** to be slightly above typical observed usage, you:

- improve node utilization (more Pods fit per node),
- reduce wasted capacity,
- still allow short bursts up to the existing **CPU limit** when traffic spikes (the Pod can use more CPU if the node has spare CPU time available).

This is the most direct, low-risk efficiency fix—especially relevant since some Pods are **stateful** (you generally want predictable behavior and minimal disruption).

**Why the other options are not the best choice**

**B. Requests equal to limits**
This makes every Pod reserve its peak CPU all the time. Since the problem is *overprovisioning*, this locks in the waste and usually decreases packing efficiency (nodes look “full” sooner).

**C. Enable VPA in Auto mode**
VPA can right-size requests, but Auto modes typically update requests by **recreating/evicting Pods** to apply new values, which can be disruptive—especially for **stateful** Pods. It’s also not the simplest “optimize now” lever the question is targeting; the stem already tells you you have good monitoring data, so tuning requests is the expected best practice response.

**D. Use HPA and reduce minimum replicas**
HPA changes **replica count**, not per-Pod CPU right-sizing. Lowering min replicas can reduce baseline capacity and harm performance during spikes, while not fixing inflated requests on each Pod.

**Need-to-know foundational concept**

- **Requests** = what the scheduler uses to place Pods; too high requests = wasted capacity, poor bin packing, more nodes.
- **Limits** = maximum allowed usage; keeping limits higher than requests supports bursty workloads.
- For efficiency tuning (especially with stateful workloads), start by correcting **requests** using real observed usage, then consider autoscaling approaches where appropriate.

###### Explanation

**Why option A is correct**

Your monitoring shows Pods are **overprovisioned** (they request/are allocated far more CPU than they usually use). In Kubernetes:

- **CPU requests** drive **scheduling and bin-packing** (how many Pods fit on a node).
- **CPU limits** cap maximum CPU the container can use (prevent “unlimited” consumption).

So if you reduce **requests** to be slightly above typical observed usage, you:

- improve node utilization (more Pods fit per node),
- reduce wasted capacity,
- still allow short bursts up to the existing **CPU limit** when traffic spikes (the Pod can use more CPU if the node has spare CPU time available).

This is the most direct, low-risk efficiency fix—especially relevant since some Pods are **stateful** (you generally want predictable behavior and minimal disruption).

> [!note]- Why the other options are wrong
> **B. Requests equal to limits**
> This makes every Pod reserve its peak CPU all the time. Since the problem is *overprovisioning*, this locks in the waste and usually decreases packing efficiency (nodes look “full” sooner).
>
> **C. Enable VPA in Auto mode**
> VPA can right-size requests, but Auto modes typically update requests by **recreating/evicting Pods** to apply new values, which can be disruptive—especially for **stateful** Pods. It’s also not the simplest “optimize now” lever the question is targeting; the stem already tells you you have good monitoring data, so tuning requests is the expected best practice response.
>
> **D. Use HPA and reduce minimum replicas**
> HPA changes **replica count**, not per-Pod CPU right-sizing. Lowering min replicas can reduce baseline capacity and harm performance during spikes, while not fixing inflated requests on each Pod.

</details>

---

### Exam 5 · Q28

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

**For this question, refer to the KnightMotives Automotive case study. You are designing the VPC network architecture for KnightMotives’ new Google Cloud environment. The company requires guaranteed bandwidth and consistently low latency between its plants and Google Cloud workloads. What should you do?**

- A. Create a Standard Tier VPC and place subnets in the regions closest to each plant. Establish a Cloud Interconnect connection between each subnet and the corresponding plant.
- B. Create a Standard Tier VPC and place subnets in the regions closest to each plant. Establish Direct Peering between the plant network and Google’s edge network.
- C. Create a Premium Tier VPC and place subnets in the regions closest to each plant. Establish a Cloud Interconnect connection between each subnet and the corresponding plant.
- D. Create a Premium Tier VPC and place subnets in the regions closest to each plant. Establish Direct Peering between the plant network and Google’s edge network.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a Premium Tier VPC and place subnets in the regions closest to each plant. Establish a Cloud Interconnect connection between each subnet and the corresponding plant.

**Correct answer: C**

Create a **Premium Tier** VPC and place subnets in the regions closest to each plant. Establish a **Cloud Interconnect** connection between each subnet and the corresponding plant.

**Authoritative documentation link (supports the correct option):**
[https://cloud.google.com/network-connectivity/docs/interconnect/sla](https://cloud.google.com/network-connectivity/docs/interconnect/sla)

**Why option C is correct**

KnightMotives needs **guaranteed bandwidth** and **consistently low latency** between on-prem plants and Google Cloud workloads. That combination points directly to **Cloud Interconnect**, which provides private, high-throughput connectivity and offers an SLA when designed correctly for production.

Choosing **Premium Tier** aligns with the low-latency requirement: Premium Tier delivers traffic on Google’s premium backbone and is the default tier used for performance-optimized networking, whereas Standard Tier relies more heavily on the public internet.

So, **Premium Tier + Cloud Interconnect** best matches “guaranteed bandwidth + consistently low latency.”

**Why the other options are not the best choice**

**A. Standard Tier + Cloud Interconnect**
Interconnect is the right connectivity type for guaranteed bandwidth, but Standard Tier is not the preferred choice when the requirement explicitly emphasizes consistently low latency and performance; Premium Tier is recommended for performance/low latency.

**B. Standard Tier + Direct Peering**
Direct Peering does not provide the same guarantees and does **not** offer a Google SLA; Google explicitly recommends Cloud Interconnect when an SLA is required.

**D. Premium Tier + Direct Peering**
Even with Premium Tier, Direct Peering still lacks a Google SLA and does not provide the same “guaranteed bandwidth” characteristics as Cloud Interconnect.

**Need-to-know foundational concept**

- **Cloud Interconnect** is the go-to option when you need **private connectivity** with **predictable performance** and an SLA (with the recommended redundant design).
- **Network Service Tiers**: **Premium Tier** is used to optimize for **performance and low latency** (traffic on Google’s premium backbone); **Standard Tier** is cost-optimized and uses regular ISP networks more.
- **Direct Peering** is useful for connecting to Google at the edge, but Google does **not** provide an SLA for it—so it’s not the best fit when “guaranteed bandwidth / consistent latency” is a hard requirement.

###### Explanation

**Correct answer: C**

Create a **Premium Tier** VPC and place subnets in the regions closest to each plant. Establish a **Cloud Interconnect** connection between each subnet and the corresponding plant.

**Authoritative documentation link (supports the correct option):**
[https://cloud.google.com/network-connectivity/docs/interconnect/sla](https://cloud.google.com/network-connectivity/docs/interconnect/sla)

**Why option C is correct**

KnightMotives needs **guaranteed bandwidth** and **consistently low latency** between on-prem plants and Google Cloud workloads. That combination points directly to **Cloud Interconnect**, which provides private, high-throughput connectivity and offers an SLA when designed correctly for production.

Choosing **Premium Tier** aligns with the low-latency requirement: Premium Tier delivers traffic on Google’s premium backbone and is the default tier used for performance-optimized networking, whereas Standard Tier relies more heavily on the public internet.

> [!note]- Why the other options are wrong
> **A. Standard Tier + Cloud Interconnect**
> Interconnect is the right connectivity type for guaranteed bandwidth, but Standard Tier is not the preferred choice when the requirement explicitly emphasizes consistently low latency and performance; Premium Tier is recommended for performance/low latency.
>
> **B. Standard Tier + Direct Peering**
> Direct Peering does not provide the same guarantees and does **not** offer a Google SLA; Google explicitly recommends Cloud Interconnect when an SLA is required.
>
> **D. Premium Tier + Direct Peering**
> Even with Premium Tier, Direct Peering still lacks a Google SLA and does not provide the same “guaranteed bandwidth” characteristics as Cloud Interconnect.

</details>

---

### Exam 5 · Q29

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

**For this question, refer to the KnightMotives Automotive case study. As part of its cloud strategy, KnightMotives plans to migrate its virtual machines to Google Cloud. These VMs host applications, databases, and file services. Over time, the company intends to modernize toward cloud-native services. During this transition, they must maintain minimal latency and low operational overhead between legacy VM workloads and newly modernized services. You need to design an architecture that supports the current VM migration and a smooth modernization path. What should you do?**

- A. Create a Shared VPC and migrate the VMs to Compute Engine in a new project. During modernization, deploy each new workload in its own project with a separate VPC, and connect them using an on-premises VPN.
- B. Create a Shared VPC and migrate the VMs to Compute Engine in a new project. During modernization, deploy each new workload in dedicated projects that use the same Shared VPC.
- C. Build a private cloud using Google Cloud VMware Engine and migrate the VMs with VMware HCX. During modernization, deploy all new workloads into a single project with one VPC.
- D. Build a private cloud using Google Cloud VMware Engine and migrate the VMs with VMware HCX. During modernization, deploy each new workload in its own project with a separate VPC.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a Shared VPC and migrate the VMs to Compute Engine in a new project. During modernization, deploy each new workload in dedicated projects that use the same Shared VPC.

**Correct answer: B**

Create a **Shared VPC** and migrate the VMs to Compute Engine in a new project. During modernization, deploy each new workload in dedicated projects that use the **same Shared VPC**.

**Authoritative documentation link (supports the correct option):**
[https://cloud.google.com/vpc/docs/shared-vpc](https://cloud.google.com/vpc/docs/shared-vpc)

**Why option B is correct**

KnightMotives needs two things during the transition:

1. **Minimal latency between legacy VMs and new cloud-native services**
2. **Low operational overhead** while they modernize gradually

Using **one Shared VPC** across multiple projects gives you:

- **Private, intra-VPC connectivity** between VM workloads and new services (no VPN hops, no extra routing overlay)
- **Centralized network governance** (subnets, routes, firewall policies, NAT, PSC patterns) managed once in the host project
- **Clean project separation** for teams/apps (service projects) without fragmenting networking

This is the standard Google Cloud “enterprise landing zone” approach: migrate first, modernize incrementally, and keep east-west traffic fast and simple.

**Why the other options are not the best choice**

**A. Separate VPC per project + on-prem VPN between them**
This adds unnecessary complexity and typically higher latency (tunneling/overhead) for traffic that should stay inside Google Cloud. It also creates operational burden managing many VPNs and routing.

**C. Google Cloud VMware Engine (GCVE) + single project/one VPC for all new workloads**
GCVE can be great when you must keep VMware initially, but the question emphasizes **low operational overhead and modernization path** across many apps/services. Putting *all* new workloads into a single project is usually a governance anti-pattern (IAM, billing, quotas, blast radius). Also, you don’t need GCVE if you’re already comfortable migrating to Compute Engine and modernizing over time.

**D. GCVE + separate VPC per new workload**
This creates the same fragmentation problem as A (multiple VPCs) while also introducing additional platform complexity (GCVE) when the requirement is minimal operational overhead.

**Need-to-know foundational concept**

A common modernization-friendly structure in Google Cloud is:

- **Host project**: owns the Shared VPC network (subnets, firewall policies, NAT, DNS, routes)
- **Service projects**: contain workloads (VMs, GKE, managed services integrations) but attach to the **same Shared VPC**

This provides:

- low-latency private communication (same VPC)
- strong isolation and governance (separate projects)
- simpler operations than stitching many VPCs together with VPN/peering while you modernize.

###### Explanation

**Why option B is correct**

KnightMotives needs two things during the transition:

1. **Minimal latency between legacy VMs and new cloud-native services**
2. **Low operational overhead** while they modernize gradually

Using **one Shared VPC** across multiple projects gives you:

- **Private, intra-VPC connectivity** between VM workloads and new services (no VPN hops, no extra routing overlay)
- **Centralized network governance** (subnets, routes, firewall policies, NAT, PSC patterns) managed once in the host project
- **Clean project separation** for teams/apps (service projects) without fragmenting networking

This is the standard Google Cloud “enterprise landing zone” approach: migrate first, modernize incrementally, and keep east-west traffic fast and simple.

> [!note]- Why the other options are wrong
> **A. Separate VPC per project + on-prem VPN between them**
> This adds unnecessary complexity and typically higher latency (tunneling/overhead) for traffic that should stay inside Google Cloud. It also creates operational burden managing many VPNs and routing.
>
> **C. Google Cloud VMware Engine (GCVE) + single project/one VPC for all new workloads**
> GCVE can be great when you must keep VMware initially, but the question emphasizes **low operational overhead and modernization path** across many apps/services. Putting *all* new workloads into a single project is usually a governance anti-pattern (IAM, billing, quotas, blast radius). Also, you don’t need GCVE if you’re already comfortable migrating to Compute Engine and modernizing over time.
>
> **D. GCVE + separate VPC per new workload**
> This creates the same fragmentation problem as A (multiple VPCs) while also introducing additional platform complexity (GCVE) when the requirement is minimal operational overhead.

</details>

---

### Exam 5 · Q36

**You are designing the network setup for a public, container-based web application running on **Cloud Run**. Every inbound request must be evaluated by a **Cloud Armor WAF** before it reaches the service. You will place an **Application Load Balancer** in front of Cloud Run and attach the Cloud Armor policy to the load balancer. You also need to ensure that users cannot bypass the load balancer by calling the Cloud Run service directly using its default `*.run.app` URL. What should you do?**

- A. Enable **Identity-Aware Proxy (IAP)** on the Cloud Run service so it intercepts and validates all incoming requests.
- B. Create a DNS record to route traffic to Cloud Armor and configure Cloud Armor to deny traffic from unknown IP addresses.
- C. Set **Cloud Run ingress** to **Allow internal traffic and Cloud Load Balancing**, and use a **serverless NEG** backend on the load balancer.
- D. Add a high-priority **VPC firewall rule** that blocks any traffic not originating from the load balancer.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Set **Cloud Run ingress** to **Allow internal traffic and Cloud Load Balancing**, and use a **serverless NEG** backend on the load balancer.

**Correct Answer: C**

**Set Cloud Run ingress to *Allow internal traffic and Cloud Load Balancing*, and use a serverless NEG backend on the load balancer.**

Why C is correct

You want two guarantees:

1. **Every request is evaluated by Cloud Armor (WAF)**
  Cloud Armor attaches to the **external Application Load Balancer**, so traffic must go through that load balancer path.
2. **Users cannot bypass the load balancer using the default `*.run.app` URL**
  The correct control for that is **Cloud Run ingress restrictions**. By setting Cloud Run ingress to **“internal and Cloud Load Balancing”**, Cloud Run will only accept requests coming from:

- internal sources (depending on your setup), and
- **Google Cloud Load Balancing** (the ALB path using a **serverless NEG**)

This blocks direct public access to the `*.run.app` endpoint, forcing all internet traffic through the ALB where Cloud Armor enforces the WAF policy.

**Why the other options are incorrect / not best fit**

**A. Enable IAP on Cloud Run**

IAP is for **identity-based access control** (authentication/authorization). It does not ensure that **all traffic must traverse Cloud Armor**, and it does not inherently prevent bypass of your WAF architecture. Also, your requirement is WAF evaluation before the service, not user identity enforcement.

**B. DNS record to route traffic to Cloud Armor + deny unknown IPs**

Cloud Armor is not a standalone endpoint you route DNS to; it works **with supported load balancers**. Also, IP allow/deny at Cloud Armor does not prevent someone from calling the Cloud Run `*.run.app` URL directly unless you restrict Cloud Run ingress.

**D. VPC firewall rule blocking non-load-balancer traffic**

VPC firewall rules apply to VMs and VPC networks. **Cloud Run is serverless** and is not protected by your project’s VPC firewall rules for inbound internet access to the `*.run.app` URL. This won’t reliably enforce the requirement.

**Need-to-know fundamentals**

- **Cloud Armor WAF** is enforced at the **Application Load Balancer** layer.
- To prevent bypass to serverless backends (Cloud Run), use **Cloud Run ingress controls**.
- For ALB → Cloud Run, you use a **serverless NEG** backend so the LB can route traffic to Cloud Run.
- Setting ingress to **internal and Cloud Load Balancing** ensures the service is not directly reachable via its public URL.

**Official documentation**

**Cloud Run ingress settings (including “internal and Cloud Load Balancing”):**
[https://cloud.google.com/run/docs/securing/ingress](https://cloud.google.com/run/docs/securing/ingress)

###### Explanation

Why C is correct

You want two guarantees:

1. **Every request is evaluated by Cloud Armor (WAF)**
  Cloud Armor attaches to the **external Application Load Balancer**, so traffic must go through that load balancer path.
2. **Users cannot bypass the load balancer using the default `*.run.app` URL**
  The correct control for that is **Cloud Run ingress restrictions**. By setting Cloud Run ingress to **“internal and Cloud Load Balancing”**, Cloud Run will only accept requests coming from:

- internal sources (depending on your setup), and
- **Google Cloud Load Balancing** (the ALB path using a **serverless NEG**)

This blocks direct public access to the `*.run.app` endpoint, forcing all internet traffic through the ALB where Cloud Armor enforces the WAF policy.

> [!note]- Why the other options are wrong
> A. Enable IAP on Cloud Run
>
> IAP is for **identity-based access control** (authentication/authorization). It does not ensure that **all traffic must traverse Cloud Armor**, and it does not inherently prevent bypass of your WAF architecture. Also, your requirement is WAF evaluation before the service, not user identity enforcement.
>
> B. DNS record to route traffic to Cloud Armor + deny unknown IPs
>
> Cloud Armor is not a standalone endpoint you route DNS to; it works **with supported load balancers**. Also, IP allow/deny at Cloud Armor does not prevent someone from calling the Cloud Run `*.run.app` URL directly unless you restrict Cloud Run ingress.
>
> D. VPC firewall rule blocking non-load-balancer traffic
>
> VPC firewall rules apply to VMs and VPC networks. **Cloud Run is serverless** and is not protected by your project’s VPC firewall rules for inbound internet access to the `*.run.app` URL. This won’t reliably enforce the requirement.

</details>

---

### Exam 5 · Q37

Your organization separates workloads into distinct Google Cloud projects: shared services, development, testing, and production.

- The **shared services** project runs private CI/CD runners and hosts a centralized **Artifact Registry**.
- The **development**, **testing**, and **production** projects each run **GKE clusters** for application deployments.

You need an architecture that lets the CI/CD runners reach the GKE clusters and lets the clusters pull images from Artifact Registry, all over **private IP connectivity**. At the same time, you must **prevent any direct network communication** between the development, testing, and production environments. What should you do?

- A. Create one VPC in each of the four projects, and peer each environment VPC only with the shared services VPC using **VPC Network Peering**.
- B. Publish shared services using an **external HTTP(S) load balancer**, and restrict access using firewall rules.
- C. Create a separate VPC per project and use **VPC Network Peering** to build a full mesh so every VPC peers with every other VPC.
- D. Make the shared services project a **Shared VPC host**, create a single VPC in that host project, and attach the environment projects as **service projects**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create one VPC in each of the four projects, and peer each environment VPC only with the shared services VPC using **VPC Network Peering**.

**Correct Answer: A**

**Create one VPC in each of the four projects, and peer each environment VPC only with the shared services VPC using VPC Network Peering.**

**Why A is correct**

This is a hub-and-spoke layout that meets all requirements simultaneously:

- **Private connectivity from shared services CI/CD runners to each environment’s GKE cluster**
  With VPC Network Peering between the shared services VPC and each env VPC, the runners can reach private endpoints (for example, private GKE control plane endpoints or private services exposed inside the env VPC) over RFC1918 routes.
- **GKE clusters can pull images over private connectivity**
  Image pulls from Artifact Registry use Google APIs; you keep that traffic on private connectivity by using private access to Google APIs from each environment VPC (for example, Private Google Access / restricted or private API access patterns). This does not require dev/test/prod to talk to each other.
- **Strict isolation between dev, test, and prod**
  Because you do not peer dev↔test↔prod, there is **no direct network path** between them. Also, VPC Network Peering is **non-transitive**, meaning dev cannot reach prod “through” shared services unless you explicitly create that peering path (which you do not). This is the scalable guardrail you want for current and future projects.

**Official reference for VPC Network Peering behavior (including non-transitive routing):**
[https://cloud.google.com/vpc/docs/vpc-peering](https://cloud.google.com/vpc/docs/vpc-peering)

**Why the other options are incorrect / not best fit**

B. Publish shared services using an external HTTP(S) load balancer and restrict access using firewall rules

This introduces unnecessary public exposure and does not satisfy the “all over private IP connectivity” requirement. Firewall rules also don’t eliminate all bypass paths when services are internet-reachable.

C. Full mesh peering between every VPC

This directly violates the isolation requirement because it enables dev/test/prod to communicate with each other by design. It also becomes harder to manage as environments and projects grow.

D. Shared VPC host with a single VPC and attach all environment projects

This can enable private connectivity, but it does **not inherently prevent** dev/test/prod communication because they are all in the **same VPC**. You would need strict firewall segmentation and enforcement to stop any east-west traffic, which is more complex and easier to misconfigure than simply keeping environments in separate VPCs.

**Need-to-know fundamentals**

- **VPC Network Peering is non-transitive**: peering dev→shared and prod→shared does not automatically allow dev→prod.
- Keeping environments in **separate VPCs** is the cleanest way to guarantee isolation at the network layer.
- Private access to Google APIs is typically handled per-environment VPC/subnet and does not require dev/test/prod to share a network with Artifact Registry.

###### Explanation

Why A is correct

This is a hub-and-spoke layout that meets all requirements simultaneously:

- **Private connectivity from shared services CI/CD runners to each environment’s GKE cluster**
  With VPC Network Peering between the shared services VPC and each env VPC, the runners can reach private endpoints (for example, private GKE control plane endpoints or private services exposed inside the env VPC) over RFC1918 routes.
- **GKE clusters can pull images over private connectivity**
  Image pulls from Artifact Registry use Google APIs; you keep that traffic on private connectivity by using private access to Google APIs from each environment VPC (for example, Private Google Access / restricted or private API access patterns). This does not require dev/test/prod to talk to each other.
- **Strict isolation between dev, test, and prod**
  Because you do not peer dev↔test↔prod, there is **no direct network path** between them. Also, VPC Network Peering is **non-transitive**, meaning dev cannot reach prod “through” shared services unless you explicitly create that peering path (which you do not). This is the scalable guardrail you want for current and future projects.

> [!note]- Why the other options are wrong
> B. Publish shared services using an external HTTP(S) load balancer and restrict access using firewall rules
>
> This introduces unnecessary public exposure and does not satisfy the “all over private IP connectivity” requirement. Firewall rules also don’t eliminate all bypass paths when services are internet-reachable.
>
> C. Full mesh peering between every VPC
>
> This directly violates the isolation requirement because it enables dev/test/prod to communicate with each other by design. It also becomes harder to manage as environments and projects grow.
>
> D. Shared VPC host with a single VPC and attach all environment projects
>
> This can enable private connectivity, but it does **not inherently prevent** dev/test/prod communication because they are all in the **same VPC**. You would need strict firewall segmentation and enforcement to stop any east-west traffic, which is more complex and easier to misconfigure than simply keeping environments in separate VPCs.

</details>

---

### Exam 5 · Q39

**You are designing a new application capability for a healthcare provider in Qatar. The feature must generate summaries of sensitive patient notes submitted by clinicians. A strict requirement is that these notes must **never be processed outside Qatar**. You want to use a strong, pre-trained generative model for summarization while fully meeting the data residency requirement. What should you do?**

- A. Build the application so it sends patient notes directly to the **Gemini API endpoint in Qatar** for summarization, and secure access using **VPC Service Controls**.
- B. Choose a **Gemma** model from **Vertex AI Model Garden** and deploy it to a **Vertex AI Endpoint** in a Google Cloud region located in Qatar.
- C. Use the **Cloud Natural Language API** to process the text and configure it to produce a summary of the patient notes.
- D. Collect a large anonymized medical dataset and use **Vertex AI Training** to train a custom summarization model from scratch, deploying it in a Qatar region.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Choose a **Gemma** model from **Vertex AI Model Garden** and deploy it to a **Vertex AI Endpoint** in a Google Cloud region located in Qatar.

**Correct Answer: B**

**Choose a Gemma model from Vertex AI Model Garden and deploy it to a Vertex AI Endpoint in a Google Cloud region located in Qatar.**

Why B is correct

Your key constraint is **strict data residency**:

- Patient notes **must never be processed outside Qatar**
- You still want a **strong pre-trained generative model** for summarization

The most reliable way to meet this is to use a model that you can **deploy inside a specific Google Cloud region in Qatar** and serve through a **Vertex AI Endpoint** in that same region. That ensures inference happens in-region (Qatar), so sensitive notes are not sent to a global/multi-region endpoint.

Using **Gemma** (a Google open model available in Vertex AI Model Garden) is a strong fit because it supports a **self-hosted deployment pattern on Vertex AI**, giving you location control.

Official reference: [Model Garden and deploying models on Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-and-inference-tutorial)

**Why the other options are incorrect / not best fit**

**A. Send notes directly to Gemini API endpoint in Qatar + VPC Service Controls**

**Not best because:**

- Even if an endpoint exists in Qatar, **VPC Service Controls is not a data residency enforcement tool**. It primarily reduces data exfiltration risk, not guarantee processing locality.
- The requirement is “must never be processed outside Qatar.” The safest approach is **regional model deployment you control**, not relying on a managed API’s routing behavior.

**C. Use Cloud Natural Language API to produce a summary**

**Incorrect because:**

- Cloud Natural Language API is not a generative summarization service for free-form clinical notes.
- It provides NLP features like entity analysis, sentiment, syntax, classification—not high-quality abstractive summarization.

**D. Train a custom summarization model from scratch in Qatar**

**Not best because:**

- Training from scratch is expensive, slow, and risky.
- You explicitly want a **strong pre-trained model** and need a practical solution quickly.
- Custom training is unnecessary unless you have very specialized requirements not met by existing foundation/open models.

**Need-to-know fundamentals (GenAI + residency)**

- **Data residency = where inference happens**, not just where the request originates.
- The safest pattern is **deploying a model to a regional endpoint** you control.
- **VPC Service Controls** helps reduce exfiltration but does not automatically guarantee that processing stays within a country/region.
- For healthcare workloads, prefer solutions that support:
  - regional deployment
  - strong access control (IAM)
  - audit logging (Cloud Audit Logs)

**Official documentation link**

[Vertex AI Model Garden (explore and deploy models like Gemma)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-and-inference-tutorial)

###### Explanation

**Why B is correct**

Your key constraint is **strict data residency**:

- Patient notes **must never be processed outside Qatar**
- You still want a **strong pre-trained generative model** for summarization

The most reliable way to meet this is to use a model that you can **deploy inside a specific Google Cloud region in Qatar** and serve through a **Vertex AI Endpoint** in that same region. That ensures inference happens in-region (Qatar), so sensitive notes are not sent to a global/multi-region endpoint.

Using **Gemma** (a Google open model available in Vertex AI Model Garden) is a strong fit because it supports a **self-hosted deployment pattern on Vertex AI**, giving you location control.

> [!note]- Why the other options are wrong
> A. Send notes directly to Gemini API endpoint in Qatar + VPC Service Controls
>
> Not best because:
>
> - Even if an endpoint exists in Qatar, **VPC Service Controls is not a data residency enforcement tool**. It primarily reduces data exfiltration risk, not guarantee processing locality.
> - The requirement is “must never be processed outside Qatar.” The safest approach is **regional model deployment you control**, not relying on a managed API’s routing behavior.
>
> C. Use Cloud Natural Language API to produce a summary
>
> Incorrect because:
>
> - Cloud Natural Language API is not a generative summarization service for free-form clinical notes.
> - It provides NLP features like entity analysis, sentiment, syntax, classification—not high-quality abstractive summarization.
>
> D. Train a custom summarization model from scratch in Qatar
>
> Not best because:
>
> - Training from scratch is expensive, slow, and risky.
> - You explicitly want a **strong pre-trained model** and need a practical solution quickly.
> - Custom training is unnecessary unless you have very specialized requirements not met by existing foundation/open models.

</details>

---

### Exam 5 · Q40

**You are designing the storage layout for a financial analytics platform. It ingests and stores **terabytes of transaction data each day**, used for both **near-real-time fraud detection** and **long-term historical reporting**. The most recent **30 days of data** must be available with **very low latency** for the fraud detection system. Data older than 30 days is accessed rarely for quarterly reporting, where **a few seconds of retrieval time is acceptable**. Compliance requires keeping all data for **five years**. You want the **most cost-optimized** solution. What should you do?**

- A. Keep all transaction data in a Cloud Storage bucket using the **Standard** storage class for the full five-year retention period.
- B. Load all data into **BigQuery** using time-partitioned tables and use BigQuery’s **automatic long-term storage pricing** for data older than 90 days.
- C. Use a Cloud Storage bucket with **Object Lifecycle Management** to move objects from **Standard** to **Archive** after 30 days.
- D. Use a Cloud Storage bucket with **Object Lifecycle Management** to move objects from **Standard** to **Coldline** after 30 days.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use a Cloud Storage bucket with **Object Lifecycle Management** to move objects from **Standard** to **Coldline** after 30 days.

**Correct Answer: D**

**Use a Cloud Storage bucket with Object Lifecycle Management to move objects from Standard to Coldline after 30 days.**

Why **D (Coldline after 30 days)** is the better cost-optimized choice here

Your access pattern is **not “almost never”**. It’s:

- Hot access for 30 days (fraud detection)
- Then **rare**, but still **predictable and recurring** access for reporting (quarterly)

With quarterly reporting, you can easily end up retrieving **multiple TBs** repeatedly. In that case:

- **Archive** has **much higher retrieval cost** and **365-day minimum storage duration**
- **Coldline** is designed for **infrequent access (~once per quarter)** and has lower retrieval fees than Archive

So even though Archive is cheaper at rest, **the retrieval cost can dominate** when you actually pull TBs every quarter.

This is exactly the scenario where **Coldline beats Archive**.

Why **C (Archive after 30 days)** is not best fit (your reasoning is correct)

1) Minimum storage duration mismatch

Archive has a **365-day minimum storage duration**.
If your reporting workflow sometimes needs to delete/rewrite/reprocess objects (common in analytics pipelines), you can incur early deletion charges.

2) Retrieval cost is significantly higher

For large quarterly reads, Archive retrieval charges can become the largest part of the bill.

So Archive is best when:

- data is retained for years, **and**
- retrieval is extremely rare (disaster recovery / legal hold style)

But quarterly analytics retrieval is **not extremely rare**.

**Why the other options are not best**

**A. Keep everything in Standard**

Too expensive for 5-year retention.

**B. BigQuery long-term storage pricing after 90 days**

This can be good if your main need is **SQL analytics directly**, but it’s not necessarily the cheapest “storage layout” for raw retained data, and it doesn’t match the **30-day hot requirement** as cleanly.

Need-to-know fundamentals (exam + real architecture)

- **Coldline** is usually best for data accessed about **once per quarter**.
- **Archive** is best for data accessed **less than once per year**.
- Cost optimization must consider:
  - storage cost
  - retrieval cost
  - minimum storage duration
  - access frequency and volume

**Official documentation (authoritative)**

**Cloud Storage storage classes (cost + minimum storage duration + retrieval behavior):**
[https://cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)

###### Explanation

Why **D (Coldline after 30 days)** is the better cost-optimized choice here

Your access pattern is **not “almost never”**. It’s:

- Hot access for 30 days (fraud detection)
- Then **rare**, but still **predictable and recurring** access for reporting (quarterly)

With quarterly reporting, you can easily end up retrieving **multiple TBs** repeatedly. In that case:

- **Archive** has **much higher retrieval cost** and **365-day minimum storage duration**
- **Coldline** is designed for **infrequent access (~once per quarter)** and has lower retrieval fees than Archive

So even though Archive is cheaper at rest, **the retrieval cost can dominate** when you actually pull TBs every quarter.

This is exactly the scenario where **Coldline beats Archive**.

> [!note]- Why the other options are wrong
> A. Keep everything in Standard
>
> Too expensive for 5-year retention.
>
> B. BigQuery long-term storage pricing after 90 days
>
> This can be good if your main need is **SQL analytics directly**, but it’s not necessarily the cheapest “storage layout” for raw retained data, and it doesn’t match the **30-day hot requirement** as cleanly.
>
> Need-to-know fundamentals (exam + real architecture)
>
> - **Coldline** is usually best for data accessed about **once per quarter**.
> - **Archive** is best for data accessed **less than once per year**.
> - Cost optimization must consider:
>   - storage cost
>   - retrieval cost
>   - minimum storage duration
>   - access frequency and volume
>
> Why **C (Archive after 30 days)** is not best fit (your reasoning is correct)
>
> 1) Minimum storage duration mismatch
>
> Archive has a **365-day minimum storage duration**.
> If your reporting workflow sometimes needs to delete/rewrite/reprocess objects (common in analytics pipelines), you can incur early deletion charges.
>
> 2) Retrieval cost is significantly higher
>
> For large quarterly reads, Archive retrieval charges can become the largest part of the bill.
>
> So Archive is best when:
>
> - data is retained for years, **and**
> - retrieval is extremely rare (disaster recovery / legal hold style)
>
> But quarterly analytics retrieval is **not extremely rare**.

</details>

---

### Exam 5 · Q45

**A Cloud Run service hosting your serverless application cannot connect to an AlloyDB database that was created using the default settings. You need to quickly identify and fix the connectivity problem. What should you do?**

- A. Confirm that the Cloud Run service and the AlloyDB instance are deployed in the same region.
- B. Enable **Direct VPC egress** for the Cloud Run service so it can send traffic directly into a VPC network.
- C. Turn off the default public IP for the AlloyDB instance and update the connection string to use the private IP address.
- D. Create a **Cloud SQL** instance and migrate the AlloyDB database to Cloud SQL for PostgreSQL.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Enable **Direct VPC egress** for the Cloud Run service so it can send traffic directly into a VPC network.

**Correct Answer: B**

**Enable Direct VPC egress for the Cloud Run service so it can send traffic directly into a VPC network.**

**Why B is correct**

With **default AlloyDB settings**, the database is typically created with **private IP connectivity** inside a VPC (AlloyDB is designed to be accessed privately). A **Cloud Run service**, by default, does **not** have direct access into your VPC network unless you configure VPC connectivity.

So the most common and quickest fix is to enable **Cloud Run Direct VPC egress**, which allows Cloud Run to send outbound traffic directly into a VPC network and reach private resources such as AlloyDB.

This directly resolves the connectivity issue without changing the database design.

**Official documentation:**
[https://cloud.google.com/run/docs/configuring/vpc-direct-vpc](https://cloud.google.com/run/docs/configuring/vpc-direct-vpc)

**Why the other options are incorrect / not best fit**

**A. Same region requirement**

Not required. Cloud Run and AlloyDB do not have to be in the same region to connect (though same-region is best for latency). The core issue is **network path**, not region.

**C. Turn off public IP and use private IP**

AlloyDB does not rely on a default “public IP” model like some databases. The problem is that Cloud Run cannot reach the private endpoint unless VPC connectivity is enabled. Disabling public access won’t fix Cloud Run networking.

**D. Migrate to Cloud SQL**

Unnecessary and not a “quick fix.” This is a major architectural change and doesn’t address the actual connectivity configuration.

**Need-to-know fundamentals**

- **AlloyDB uses private networking** and is meant to be accessed from within a VPC.
- **Cloud Run requires VPC connectivity** to reach private IP resources.
- **Direct VPC egress** is the modern, recommended way to connect Cloud Run to VPC resources.

**Official documentation link**

**Cloud Run Direct VPC egress:**
[https://cloud.google.com/run/docs/configuring/vpc-direct-vpc](https://cloud.google.com/run/docs/configuring/vpc-direct-vpc)

###### Explanation

**Why B is correct**

With **default AlloyDB settings**, the database is typically created with **private IP connectivity** inside a VPC (AlloyDB is designed to be accessed privately). A **Cloud Run service**, by default, does **not** have direct access into your VPC network unless you configure VPC connectivity.

So the most common and quickest fix is to enable **Cloud Run Direct VPC egress**, which allows Cloud Run to send outbound traffic directly into a VPC network and reach private resources such as AlloyDB.

This directly resolves the connectivity issue without changing the database design.

> [!note]- Why the other options are wrong
> A. Same region requirement
>
> Not required. Cloud Run and AlloyDB do not have to be in the same region to connect (though same-region is best for latency). The core issue is **network path**, not region.
>
> C. Turn off public IP and use private IP
>
> AlloyDB does not rely on a default “public IP” model like some databases. The problem is that Cloud Run cannot reach the private endpoint unless VPC connectivity is enabled. Disabling public access won’t fix Cloud Run networking.
>
> D. Migrate to Cloud SQL
>
> Unnecessary and not a “quick fix.” This is a major architectural change and doesn’t address the actual connectivity configuration.

</details>

---

### Exam 5 · Q51

You manage a **Google Compute Engine (GCE)** application running in a **Managed Instance Group (MIG)**. You want the MIG to **autoscale when total memory usage exceeds 80%**.

You have installed the **Cloud Monitoring agent** and configured autoscaling with the following policy:

- **Metric identifier:** `agent.googleapis.com/memory/percent_used`
- **Filter:**

`metric.label.state = 'used' AND`

`metric.label.state = 'buffered' AND`

`metric.label.state = 'cached' AND`

`metric.label.state = 'slab'`

- **Target utilization level:** `80`
- **Target type:** `GAUGE`

You observe that the application **does not scale under high load**. What should you do to fix this?

- A. Change the target type to `DELTA_PER_MINUTE`.
- B. Change the metric identifier to `agent.googleapis.com/memory/bytes_used`.
- C. Change the filter to `metric.label.state = 'used'`.
- D. Change the filter to `metric.label.state = 'free'` and the target utilization to `20`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Change the filter to `metric.label.state = 'used'`.

**Correct Answer: C**

**Change the filter to `metric.label.state = 'used'`.**

Why C is correct

The autoscaler metric `agent.googleapis.com/memory/percent_used` is a **GAUGE** metric that reports memory usage **by state** (for example: `used`, `free`, `buffered`, `cached`, `slab`).

Your current filter is:

```
metric.label.state = 'used' ANDmetric.label.state = 'buffered' ANDmetric.label.state = 'cached' ANDmetric.label.state = 'slab'
```

A single time series **cannot have multiple values for the same label at the same time**.
So this filter matches **zero time series**, meaning the autoscaler receives **no valid data** and therefore **never scales**.

Fix: filter to the specific state you want to scale on, typically:

```
metric.label.state = 'used'
```

That produces a valid time series, allowing autoscaling to trigger when memory usage exceeds 80%.

**Why the other options are incorrect**

**A. Change target type to `DELTA_PER_MINUTE`

Incorrect because memory percent used is a GAUGE, not a delta/counter metric. Autoscaling on memory utilization should remain GAUGE.**

**B. Change metric to** `agent.googleapis.com/memory/bytes_used`

Not required. You can autoscale correctly using percent-based utilization. The real issue is the invalid filter.

**D. Use `state='free'` and target utilization 20**

Not best. It flips the logic and still depends on interpretation of free memory, which can be misleading due to Linux caching behavior. The primary issue remains the filter.

**Need-to-know fundamentals**

- In Cloud Monitoring filters, multiple conditions on the **same label key** must use **OR**, not AND.
- For Linux memory, `cached`/`buffered` can be reclaimed, so scaling on `used` **percent** is usually clearer than scaling on “free”.

**Official documentation**

**Cloud Monitoring filter syntax (how label filters work):**
[https://cloud.google.com/monitoring/api/v3/filters](https://cloud.google.com/monitoring/api/v3/filters)

###### Explanation

Why C is correct

The autoscaler metric `agent.googleapis.com/memory/percent_used` is a **GAUGE** metric that reports memory usage **by state** (for example: `used`, `free`, `buffered`, `cached`, `slab`).

Your current filter is:

```
metric.label.state = 'used' ANDmetric.label.state = 'buffered' ANDmetric.label.state = 'cached' ANDmetric.label.state = 'slab'
```

A single time series **cannot have multiple values for the same label at the same time**.
So this filter matches **zero time series**, meaning the autoscaler receives **no valid data** and therefore **never scales**.

Fix: filter to the specific state you want to scale on, typically:

```
metric.label.state = 'used'
```

That produces a valid time series, allowing autoscaling to trigger when memory usage exceeds 80%.

> [!note]- Why the other options are wrong
> A. Change target type to `DELTA_PER_MINUTE`
>
> Incorrect because memory percent used is a **GAUGE**, not a delta/counter metric. Autoscaling on memory utilization should remain GAUGE.
>
> B. Change metric to `agent.googleapis.com/memory/bytes_used`
>
> Not required. You can autoscale correctly using percent-based utilization. The real issue is the invalid filter.
>
> D. Use `state='free'` and target utilization 20
>
> Not best. It flips the logic and still depends on interpretation of free memory, which can be misleading due to Linux caching behavior. The primary issue remains the filter.

</details>

---

### Exam 5 · Q63

**Your ML engineers currently rely on self-managed Jupyter notebooks for data preparation, model training, and fine-tuning. The operations team is responsible for deploying the trained models into multiple environments. You want to give ML engineers maximum flexibility, standardize collaboration around a shared toolset, and take advantage of Google Cloud’s scalability, while following recommended best practices. What should you do?**

- A. Use AutoML for ML development and Cloud Deploy for model deployment.
- B. Use Colab Enterprise for ML development and DevOps pipelines for model deployment.
- C. Use Vertex AI for ML development and adopt MLOps workflows for model deployment.
- D. Use TensorFlow for ML development and Cloud Deploy for model deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use Vertex AI for ML development and adopt MLOps workflows for model deployment.

**Correct option: C. Use Vertex AI for ML development and adopt MLOps workflows for model deployment.**

**Need-to-know foundational concept**

Google’s recommended best practice for ML teams is to move from ad-hoc notebooks toward a **managed ML platform + MLOps pipeline**. The goal is not just model training — it’s **reproducibility, collaboration, versioning, automated deployment, and lifecycle governance**.

Vertex AI is Google’s unified ML platform that provides:

- Managed notebooks
- Pipelines
- Training infrastructure
- Model registry
- Deployment endpoints
- Experiment tracking
- Feature store
- CI/CD-style MLOps workflows

This lets ML engineers keep notebook flexibility while standardizing tooling and automating deployments across environments.

**Google explicitly recommends Vertex AI as the platform for implementing MLOps practices:**
[https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)

**Why the correct option fits the scenario**

The scenario asks for:

- Maximum flexibility for ML engineers → managed notebooks + pipelines
- Shared standardized tooling → Vertex AI platform
- Scalable infrastructure → managed training + serving
- Best-practice deployment → MLOps workflows

Vertex AI + MLOps directly addresses **collaboration**, **governance**, and **automation**, not just training.

This is exactly how Google recommends modern ML teams operate.

**Why the other options are not the best choice**

**A. AutoML + Cloud Deploy**
AutoML is for low-code model creation. It limits flexibility for engineers who want full control over data prep and custom training.

**B. Colab Enterprise + DevOps pipelines**
Colab helps with notebooks but is not a full ML lifecycle platform. You’d still be stitching together tooling instead of using an integrated MLOps stack.

**D. TensorFlow + Cloud Deploy**
TensorFlow is just a framework, not a platform. It does nothing to standardize collaboration, pipelines, or lifecycle management.

Only Vertex AI provides a **unified ML platform + native MLOps capabilities**, which matches Google’s best-practice architecture for ML organizations.

###### Explanation

**Correct option: C. Use Vertex AI for ML development and adopt MLOps workflows for model deployment.**

**Need-to-know foundational concept**

Google’s recommended best practice for ML teams is to move from ad-hoc notebooks toward a **managed ML platform + MLOps pipeline**. The goal is not just model training — it’s **reproducibility, collaboration, versioning, automated deployment, and lifecycle governance**.

Vertex AI is Google’s unified ML platform that provides:

- Managed notebooks
- Pipelines
- Training infrastructure
- Model registry
- Deployment endpoints
- Experiment tracking
- Feature store
- CI/CD-style MLOps workflows

This lets ML engineers keep notebook flexibility while standardizing tooling and automating deployments across environments.

> [!note]- Why the other options are wrong
> **A. AutoML + Cloud Deploy**
> AutoML is for low-code model creation. It limits flexibility for engineers who want full control over data prep and custom training.
>
> **B. Colab Enterprise + DevOps pipelines**
> Colab helps with notebooks but is not a full ML lifecycle platform. You’d still be stitching together tooling instead of using an integrated MLOps stack.
>
> **D. TensorFlow + Cloud Deploy**
> TensorFlow is just a framework, not a platform. It does nothing to standardize collaboration, pipelines, or lifecycle management.

</details>

---

### Exam 5 · Q65

**You are deploying a three-tier application on Compute Engine within a single VPC. The design uses separate subnets for the web tier, application tier, and database tier.**

**• The web tier should accept traffic only from an external load balancer.

- The application tier should accept traffic only from the web tier.
- The database tier should accept traffic only from the application tier.**

**You must strictly control traffic flow and follow Google-recommended security practices. What should you do?**

- A. Configure Cloud NAT for each subnet and apply Cloud Armor policies to control inter-tier traffic using IP address filtering.
- B. Create one high-priority VPC firewall rule that allows ingress on all ports between the IP ranges of all three subnets.
- C. Assign a unique network tag and dedicated service account to each tier. Create targeted firewall rules that permit ingress traffic only from the upstream tier’s tag or service account.
- D. Configure VPC Network Peering between the web and application subnets, and another peering connection between the application and database subnets.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Assign a unique network tag and dedicated service account to each tier. Create targeted firewall rules that permit ingress traffic only from the upstream tier’s tag or service account.

**Correct option: C. Assign a unique network tag and dedicated service account to each tier. Create targeted firewall rules that permit ingress traffic only from the upstream tier’s tag or service account.**

**Need-to-know foundational concept**

Google-recommended network segmentation in a single VPC is enforced with **VPC firewall rules using least privilege**. Firewall rules can match traffic based on:

- **Source IP ranges** (coarse)
- **Network tags** (instance-level grouping)
- **Service accounts** (identity-based grouping, recommended for stronger control)

Using **service accounts and/or tags per tier** lets you express intent like “only instances running as the app-tier identity can reach the DB tier,” which is more robust than relying on static IP ranges alone.

**Authoritative reference (firewall rules support targets/sources by tags and service accounts):**
[https://cloud.google.com/vpc/docs/firewalls](https://cloud.google.com/vpc/docs/firewalls)

**Why the correct option fits the scenario**

You need strict, tier-to-tier allow-listing:

- Web tier: only accepts from the external load balancer (implemented via allowing from Google load balancer source ranges/health checks + restricting other ingress)
- App tier: only from web tier
- DB tier: only from app tier

By giving each tier a unique **tag and service account**, you can create precise ingress rules:

- App ingress rule: source = web-tier tag/service account, target = app-tier tag/service account, only required ports
- DB ingress rule: source = app-tier tag/service account, target = db-tier tag/service account, only required ports
- Web ingress rule: allow only load balancer/health check sources on required ports, deny everything else by default

This follows least privilege and scales cleanly as instances change.

**Why the other options are not the best choice**

**A. Cloud NAT + Cloud Armor for inter-tier traffic**
Cloud NAT is for outbound internet access, not east-west tier controls. Cloud Armor protects HTTP(S) load balancers and some Google front ends; it is not the primary tool for controlling subnet-to-subnet traffic inside a VPC.

**B. One broad allow rule between all subnet ranges**
This violates least privilege because it allows any-to-any between tiers (and “all ports” is explicitly unsafe). It does not enforce the required traffic flow constraints.

**D. VPC Network Peering between subnets in the same VPC**
Peering is for connecting different VPC networks. It is not used to segment subnets within one VPC, and it does not provide the requested strict inter-tier control.

The correct design is tier identities (tags/service accounts) plus narrowly scoped VPC firewall rules enforcing upstream-only access.

###### Explanation

**Correct option: C. Assign a unique network tag and dedicated service account to each tier. Create targeted firewall rules that permit ingress traffic only from the upstream tier’s tag or service account.**

**Need-to-know foundational concept**

Google-recommended network segmentation in a single VPC is enforced with **VPC firewall rules using least privilege**. Firewall rules can match traffic based on:

- **Source IP ranges** (coarse)
- **Network tags** (instance-level grouping)
- **Service accounts** (identity-based grouping, recommended for stronger control)

Using **service accounts and/or tags per tier** lets you express intent like “only instances running as the app-tier identity can reach the DB tier,” which is more robust than relying on static IP ranges alone.

> [!note]- Why the other options are wrong
> **A. Cloud NAT + Cloud Armor for inter-tier traffic**
> Cloud NAT is for outbound internet access, not east-west tier controls. Cloud Armor protects HTTP(S) load balancers and some Google front ends; it is not the primary tool for controlling subnet-to-subnet traffic inside a VPC.
>
> **B. One broad allow rule between all subnet ranges**
> This violates least privilege because it allows any-to-any between tiers (and “all ports” is explicitly unsafe). It does not enforce the required traffic flow constraints.
>
> **D. VPC Network Peering between subnets in the same VPC**
> Peering is for connecting different VPC networks. It is not used to segment subnets within one VPC, and it does not provide the requested strict inter-tier control.

</details>

---

### Exam 5 · Q76

**You are training a deep learning model that needs fast access to large media datasets stored in Cloud Storage. Training runs on multiple GPU-enabled VMs, and your application must access the data as if it were on a local filesystem. You want the simplest and most cost-effective solution. What should you do?**

- A. Copy the dataset from Cloud Storage into Filestore and mount the Filestore share on each VM as a local filesystem.
- B. Create a shared persistent disk, attach it to the VM instances, and load the data from Cloud Storage onto that disk.
- C. Mount the Cloud Storage bucket locally using **gcsfuse** and access the data through standard filesystem operations.
- D. Use **gsutil** to download the dataset directly onto each VM instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Mount the Cloud Storage bucket locally using **gcsfuse** and access the data through standard filesystem operations.

**Correct option:** **C. Mount the Cloud Storage bucket locally using gcsfuse and access the data through standard filesystem operations.**

**Need-to-know foundational concept**

When an application needs to read objects from Cloud Storage **through POSIX-like file operations**, the simplest approach is to use a user-space filesystem mount. **gcsfuse** lets you mount a Cloud Storage bucket so your code can access objects using standard filesystem paths (open/read/list), without building custom object-storage logic or duplicating datasets on each VM.

**Authoritative reference: gcsfuse mounts Cloud Storage buckets as a file system**
[https://cloud.google.com/storage/docs/gcsfuse](https://cloud.google.com/storage/docs/gcsfuse)

**Why the chosen option is correct**

- Meets the requirement “access the data as if it were on a local filesystem” via a mount point.
- Lowest operational overhead: no need to provision/operate additional storage systems.
- Cost-effective: avoids duplicating a large dataset across multiple VMs and avoids standing up Filestore just to mirror Cloud Storage.

**Why the other options are not the best choice**

**A. Copy into Filestore**
Adds extra storage cost and operational overhead (provisioning Filestore, copying/syncing data, capacity planning). Also duplicates data already in Cloud Storage.

**B. Shared persistent disk**
Persistent Disk is not designed to be attached read-write to many VMs simultaneously in the way a shared dataset needs (and even read-only sharing introduces management overhead and data loading steps). It also requires copying the dataset onto the disk.

**D. gsutil download onto each VM**
This duplicates the dataset on every VM, increasing cost, startup time, and ongoing operational complexity (keeping datasets consistent across VMs).

Final answer: **C**

###### Explanation

**Correct option:** **C.**

**Need-to-know foundational concept**

When an application needs to read objects from Cloud Storage **through POSIX-like file operations**, the simplest approach is to use a user-space filesystem mount. **gcsfuse** lets you mount a Cloud Storage bucket so your code can access objects using standard filesystem paths (open/read/list), without building custom object-storage logic or duplicating datasets on each VM.

**Why the chosen option is correct**

- Meets the requirement “access the data as if it were on a local filesystem” via a mount point.
- Lowest operational overhead: no need to provision/operate additional storage systems.
- Cost-effective: avoids duplicating a large dataset across multiple VMs and avoids standing up Filestore just to mirror Cloud Storage.

> [!note]- Why the other options are wrong
> **A. Copy into Filestore**
> Adds extra storage cost and operational overhead (provisioning Filestore, copying/syncing data, capacity planning). Also duplicates data already in Cloud Storage.
>
> **B. Shared persistent disk**
> Persistent Disk is not designed to be attached read-write to many VMs simultaneously in the way a shared dataset needs (and even read-only sharing introduces management overhead and data loading steps). It also requires copying the dataset onto the disk.
>
> **D. gsutil download onto each VM**
> This duplicates the dataset on every VM, increasing cost, startup time, and ongoing operational complexity (keeping datasets consistent across VMs).

</details>

---

### Exam 5 · Q77

**Your organization is scaling AI operations nationwide and will use accelerator-based compute for AI workloads. The batch image processing jobs are not time-critical and can tolerate interruptions. You need a solution that enables rapid provisioning at low cost, while still supporting data persistence when needed. What should you do?**

- A. Use standard VMs with attached accelerators and Persistent Disk.
- B. Use Spot VMs with Persistent Disk attached, and implement checkpointing to handle interruptions.
- C. Use Spot VMs with local SSD to improve burst performance and shorten runtimes.
- D. Use Cloud Run functions with ephemeral local SSD.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Spot VMs with Persistent Disk attached, and implement checkpointing to handle interruptions.

**Correct option: B. Use Spot VMs with Persistent Disk attached, and implement checkpointing to handle interruptions.**

**Need-to-know foundational concept**

When workloads are **interruptible and non time-critical**, Google recommends using **Spot VMs** to drastically reduce compute cost. Spot VMs can be reclaimed at any time, so resilient workloads must support **checkpointing** and use **durable storage**. Persistent Disk provides durable storage that survives VM termination, allowing jobs to resume from the last checkpoint.

**Spot VMs are designed for fault-tolerant batch workloads and cost optimization:**
[https://cloud.google.com/compute/docs/instances/spot](https://cloud.google.com/compute/docs/instances/spot)

Persistent Disk provides durable block storage independent of VM lifecycle:
[https://cloud.google.com/compute/docs/disks](https://cloud.google.com/compute/docs/disks)

**Why the chosen option is correct**

- Spot VMs = lowest cost accelerator compute
- Batch job tolerates interruption
- Persistent Disk preserves data when VM is reclaimed
- Checkpointing enables restart without losing progress
- Rapid provisioning + cost efficiency
- Aligns with Google best practices for batch AI workloads

This is the standard architecture pattern for resilient, low-cost batch GPU jobs.

**Why the other options are not the best choice**

**A. Standard VMs**
Higher cost with no benefit since the workload tolerates interruption.

**C. Spot VMs + local SSD**
Local SSD is ephemeral and lost when a Spot VM is reclaimed. This violates the requirement for data persistence.

**D. Cloud Run functions**
Cloud Run does not support GPU/accelerator workloads or persistent disk checkpointing for batch AI jobs.

Exam principle:

Interruptible batch + low cost → Spot VMs + durable storage + checkpointing.

Final answer: **B**

###### Explanation

**Correct option: B.**

**Need-to-know foundational concept**

When workloads are **interruptible and non time-critical**, Google recommends using **Spot VMs** to drastically reduce compute cost. Spot VMs can be reclaimed at any time, so resilient workloads must support **checkpointing** and use **durable storage**. Persistent Disk provides durable storage that survives VM termination, allowing jobs to resume from the last checkpoint.

**Why the chosen option is correct**

- Spot VMs = lowest cost accelerator compute
- Batch job tolerates interruption
- Persistent Disk preserves data when VM is reclaimed
- Checkpointing enables restart without losing progress
- Rapid provisioning + cost efficiency
- Aligns with Google best practices for batch AI workloads

> [!note]- Why the other options are wrong
> **A. Standard VMs**
> Higher cost with no benefit since the workload tolerates interruption.
>
> **C. Spot VMs + local SSD**
> Local SSD is ephemeral and lost when a Spot VM is reclaimed. This violates the requirement for data persistence.
>
> **D. Cloud Run functions**
> Cloud Run does not support GPU/accelerator workloads or persistent disk checkpointing for batch AI jobs.

</details>

---
