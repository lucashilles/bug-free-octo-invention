# Domain 2 Study Guide — Managing and Provisioning a Solution Infrastructure

> Condensed from the 68-question bank in [`02-provisioning-infrastructure.md`](02-provisioning-infrastructure.md). Citations look like (Exam N · QM). Several scenarios repeat across exams, so look for the paired citations.

---

## 1. Hybrid connectivity: Cloud VPN vs Cloud Interconnect

### Key facts
- **Cloud VPN** runs IPsec over the internet. Each tunnel carries up to about 3 Gbps. It is cheap and quick to set up, but latency and packet loss follow the internet path.
- **HA VPN** has two interfaces and gives a **99.99% SLA** when both tunnels are up and BGP is configured. **Classic VPN** has one interface and a 99.9% SLA. One HA VPN gateway with two tunnels to the on-prem gateway is the cheapest way to get "near 100%" availability for a small link (Exam 4 · Q5), (Exam 4 · Q9).
- A Cloud VPN gateway is a **regional** resource. A VPC with workloads in two regions → a gateway in **each region**, each with at least one tunnel to on-prem. There is no "global VPN gateway" (Exam 2 · Q14).
- **Dedicated Interconnect** is a physical link from your router to Google in a **colocation facility**, in 10 Gbps or 100 Gbps circuits. It carries private RFC 1918 traffic, never touches the internet, and gives predictable latency. Pick it for large, frequent replication or any stated bandwidth of 10 Gbps or more (Exam 1 · Q25), (Exam 1 · Q40), (Exam 2 · Q41).
- VPN replication suffering **latency and packet loss** → move to **Dedicated Interconnect**. More VPN tunnels, UDP or Pub/Sub don't fix the path (Exam 1 · Q37).
- **Partner Interconnect** goes through a service provider, from 50 Mbps to 50 Gbps. Pick it when you **can't reach a colocation facility** (e.g. a data center 100 km from the nearest city on a microwave link) (Exam 4 · Q55), or when you want hybrid connectivity with less to operate yourself (Exam 5 · Q2).
- **Interconnect SLAs**: 99.9% needs two connections in one metro, in different edge availability domains. **99.99%** needs **four connections: two in each of two metros**, with Cloud Routers in two regions (Exam 4 · Q20).
- **Cloud Router** runs BGP so routes are exchanged dynamically. Use it with HA VPN and with every Interconnect VLAN attachment (Exam 5 · Q2).
- **Direct Peering** and **Carrier Peering** connect you to Google's **public** edge (Workspace, public Google APIs). They don't give private IP access to your VPC (Exam 2 · Q41), (Exam 4 · Q20).
- **Network Service Tiers**: **Premium** carries traffic on Google's backbone to the edge closest to the user. **Standard** hands it to the public internet in the region. "Guaranteed bandwidth, consistently low latency" → Premium Tier + Interconnect (Exam 5 · Q28).

### Comparison

| Option | Bandwidth | Private IPs to VPC | Picked when | Source |
|---|---|---|---|---|
| HA VPN | ~3 Gbps per tunnel | Yes | Low throughput, cost-effective, 99.99% | (Exam 4 · Q5), (Exam 4 · Q9) |
| Dedicated Interconnect | 10 / 100 Gbps circuits | Yes | Large replication, 20 Gbps+, lowest latency | (Exam 1 · Q25), (Exam 1 · Q40), (Exam 2 · Q41) |
| Partner Interconnect | 50 Mbps – 50 Gbps | Yes | No colocation facility nearby, less to operate | (Exam 4 · Q55), (Exam 5 · Q2) |
| Direct / Carrier Peering | Varies | No (public Google services only) | Workspace / public APIs | (Exam 4 · Q20) |

### Decision rules
- "200 kbps" + "99.99%" + "cost-effective" → **one HA VPN gateway, two tunnels**. Not two HA gateways (more cost, no gain), not Classic VPN (Exam 4 · Q5), (Exam 4 · Q9).
- "Minimum 20 Gbps" + "private" + best practice → **VPC + Dedicated Interconnect**. Cloud CDN has nothing to do with hybrid links (Exam 1 · Q40).
- "4 TB database, frequent large updates, private address space" → **Dedicated Interconnect** (Exam 1 · Q25).
- "High throughput, internal IPs, minimal latency" → **Dedicated Interconnect**, not OpenVPN, Cloud VPN or Direct Peering (Exam 2 · Q41).
- EHR Healthcare needs a "secure and high-performance connection" and production-grade availability → add a **new Dedicated Interconnect** connection rather than enlarging one link (a single link is a single point of failure) (Exam 4 · Q19), and design **2 + 2 connections across two metros** (Exam 4 · Q20).
- Remote site with no colocation reach → **Partner Interconnect** (Exam 4 · Q55).
- Altostrat ingesting large media with "minimal operational overhead" and "predictable latency" → **Partner Interconnect, redundant VLAN attachments, Cloud Router** (Exam 5 · Q2).

### Traps
- Adding VPN tunnels and load-balancing them doesn't cure internet latency or loss (Exam 1 · Q37).
- A single Dedicated Interconnect with **static routing** "to save cost" has no redundancy and no dynamic failover (Exam 5 · Q2).
- **Standard Tier** can't promise consistent latency, and **Direct Peering** isn't a private VPC link (Exam 5 · Q28).
- Two Partner Interconnects in one metro, or two VPNs in separate racks, don't reach the 99.99% production topology (Exam 4 · Q20).
- A self-managed VPN server on a VM or a NAT/TLS gateway on-prem is never the managed answer (Exam 1 · Q25).

---

## 2. IP planning and connecting VPCs

### Key facts
- Plan VPC ranges that **don't overlap** with on-prem, other clouds or other VPCs you'll connect. Overlap breaks routing over VPN, Interconnect and peering (Exam 1 · Q47), (Exam 4 · Q64).
- Use a **custom-mode VPC** for hybrid designs. The default and auto-mode VPCs create a subnet in every region from `10.128.0.0/9`, which may collide with on-prem ranges (Exam 4 · Q64).
- A secondary range doesn't rescue an overlapping primary range, and a secondary range that matches on-prem is just as broken (Exam 1 · Q47).
- **VPC Network Peering** joins two VPCs over Google's network with internal IPs, full bandwidth and no gateways. It works **across projects and organizations**, but subnet ranges must not overlap (Exam 4 · Q2).
- **Peering is not transitive.** If A peers with B and B with C, A can't reach C through B. That makes a **hub-and-spoke** design a deliberate isolation tool: peer each environment VPC only with the shared-services VPC, and dev, test and prod can't reach each other (Exam 5 · Q37).
- When two VPCs have **some overlapping subnets**, peering is refused. **Cloud VPN between the VPCs** (HA VPN to HA VPN) with Cloud Router advertising only the non-overlapping ranges connects the apps that need it with little re-engineering (Exam 3 · Q64).
- Overlap between a VPC and on-prem that you can't renumber → **Cloud NAT Hybrid NAT** (Private NAT). It translates VPC source addresses into a non-overlapping range for traffic going to on-prem over VPN or Interconnect. It needs dynamic routes from Cloud Router (Exam 2 · Q51).
- **Multiple network interfaces**: a VM can have one NIC in each of several VPCs (up to 8 NICs, depending on vCPUs). Only that VM bridges the networks; the VPCs themselves stay separate. NICs are defined when the VM is created (Exam 4 · Q53).
- **Shared VPC**: one host project owns the network; service projects attach to it. Every project's workloads share one network, so latency is low and the network is managed centrally. New modernized workloads can live in their own service projects on the same Shared VPC (Exam 5 · Q29).

### Decision rules
- Phased migration with VPN, "all on-prem systems must stay reachable" → **non-overlapping ranges** in Google Cloud (Exam 1 · Q47).
- "Future-proof hybrid" → **custom VPC with a non-overlapping CIDR plan + Cloud Interconnect** (Exam 4 · Q64).
- Two orgs, non-overlapping VPCs, low latency and high throughput → **VPC Network Peering**, not VPN, IAP tunnels or OpenVPN (Exam 4 · Q2).
- Two orgs' Shared VPCs with partial overlap → **Cloud VPN between them** (Exam 3 · Q64).
- Acquired company's VPC overlaps the data center → **Cloud VPN + Hybrid NAT** (Exam 2 · Q51).
- One VM must talk to two other VPCs that must stay separate → **multi-NIC VM** (Exam 4 · Q53).
- Shared services reachable privately by every environment, environments isolated from each other → **hub-and-spoke peering** (Exam 5 · Q37).
- VM migration now, cloud-native later, low latency between old and new → **Shared VPC, new workloads in service projects** (Exam 5 · Q29).

### Traps
- A full-mesh peering or a single Shared VPC for all environments lets dev talk to prod (Exam 5 · Q37).
- Peering "VPC 1 with 2, and 2 with 3" doesn't let 1 reach 3, and it joins networks that must stay separate (Exam 4 · Q53).
- A Cloud Router route advertisement only controls what is advertised. It doesn't translate overlapping addresses, and neither does a firewall rule (Exam 2 · Q51).
- Moving the acquired company's projects into your org is a big re-engineering job, and SSH port forwarding isn't an architecture (Exam 3 · Q64).
- VMware Engine is for lifting VMware estates as-is; it doesn't help when the goal is Compute Engine plus modernization in shared networking (Exam 5 · Q29).

---

## 3. Firewall rules and private egress

### Key facts
- VPC firewall rules are stateful and apply per VM. **Priority runs from 0 to 65535, and the lower number wins.** Every VPC has two implied rules at 65535: **deny all ingress** and **allow all egress** (Exam 2 · Q28).
- Rules target VMs by **network tag** or **service account**, so they follow instances as they autoscale. Rules on IP ranges break when addresses change (Exam 2 · Q9), (Exam 1 · Q31).
- **Service accounts** are the stronger target: anyone who can edit an instance can change its tags, but changing a service account needs IAM permission. Google's recommended tier isolation uses a tag or a dedicated service account per tier, with rules that allow ingress only from the upstream tier (Exam 5 · Q65).
- Enforce web → API → DB with tag-based **firewall rules**. Routes decide where packets go, not whether they're allowed. Separate subnets alone don't block anything (Exam 1 · Q31), (Exam 3 · Q39).
- **Private Google Access** (a subnet setting) lets VMs with only internal IPs reach Google APIs, such as Cloud Storage. It doesn't reach the internet (Exam 1 · Q51).
- **Cloud NAT** gives VMs and private GKE nodes without external IPs **outbound** internet access, such as package repositories or third-party APIs. It allows no unsolicited inbound connections and is fully managed (Exam 4 · Q7), (Exam 3 · Q24).
- **IAP TCP forwarding** is for inbound admin access (SSH/RDP) without public IPs. It doesn't give VMs outbound access (Exam 4 · Q7).

### Decision rules
- Allow only AD traffic out, block the rest → **egress deny-all at priority 1000 + egress allow-AD at priority 100**. You must create the deny yourself, because the implied egress rule is *allow* (Exam 2 · Q28).
- Autoscaled VMs, restrict paths and ports without static IPs → **firewall rules on network tags** (Exam 2 · Q9).
- No internet, install software from Google Cloud → upload to **Cloud Storage**, use a subnet with **Private Google Access**, internal IP only, then copy with `gcloud storage cp` (formerly `gsutil`) (Exam 1 · Q51).
- Private VMs need an external package repo → **Cloud NAT** on that subnet (Exam 4 · Q7).
- GKE with no public IPs but calls to third-party services → **private cluster + Cloud NAT** (Exam 3 · Q24).

### Traps
- Private Google Access only reaches Google APIs. It never reaches third-party internet hosts (Exam 4 · Q7), (Exam 3 · Q24).
- A DIY NAT VM or a bastion proxy works, but it is a single point of failure that you maintain. Cloud NAT is the managed answer (Exam 3 · Q24), (Exam 4 · Q7).
- "Implied deny egress at priority 100/1000" doesn't exist (Exam 2 · Q28).
- Cloud Armor protects load balancer frontends, not traffic between tiers. Peering subnets in the same VPC makes no sense (Exam 5 · Q65).
- Cloud DNS hostnames and app-level service account checks are not network enforcement (Exam 2 · Q9).

---

## 4. Load balancing, CDN and serverless networking

### Key facts
- The **external Application Load Balancer** (HTTP(S)) has one anycast IP and one certificate, and its **URL map** sends paths to different backend services. `/v1/*` and `/v2/*` on separate backend pools keeps the same DNS name and SSL certificate (Exam 1 · Q1).
- **Health checks** come from Google ranges `130.211.0.0/22` and `35.191.0.0/16`. Without an ingress firewall rule allowing them, every backend looks unhealthy, and MIG autohealing keeps recreating VMs even though `curl` works locally (Exam 1 · Q8), (Exam 3 · Q38).
- **Cloud CDN** caches at Google's edge in front of the load balancer. The **cache key** defaults to protocol + host + path + query string. Removing the protocol (or unneeded query parameters) lets HTTP and HTTPS requests share one cached copy, so the hit ratio rises (Exam 2 · Q25).
- **Serverless NEGs** put Cloud Run, Cloud Run functions or App Engine behind an Application Load Balancer. Deploying the service in several regions with a serverless NEG per region gives global anycast, low latency and regional failover (Exam 4 · Q45).
- **Cloud Run ingress settings**: `all`, `internal`, or **`internal-and-cloud-load-balancing`**. The last one blocks direct calls to the `*.run.app` URL, so every request must pass the load balancer and its **Cloud Armor** policy (Exam 5 · Q36).
- **Serverless → VPC egress**: Cloud Run can use **Direct VPC egress** (no connector, the recommended option) or a **Serverless VPC Access connector**. App Engine standard uses a connector. Either path then reaches private IPs, including on-prem over existing VPN or Interconnect (Exam 3 · Q25), (Exam 5 · Q45).
- **AlloyDB created with default settings has only a private IP** (private services access), so Cloud Run can't reach it until it sends traffic into the VPC (Exam 5 · Q45).
- **App Engine flexible** runs on Compute Engine VMs inside your VPC, so it reaches on-prem over Cloud VPN directly (Exam 1 · Q50).
- Legacy **Mountkirk Games** runs its backend on Compute Engine with a custom Linux distro, so its ingress is a **global load balancer → managed instance group** (Exam 4 · Q40).

### Decision rules
- New API version, keep SSL and DNS → **one load balancer, path rules, separate backend pools** (Exam 1 · Q1).
- VMs recycling every minute behind an HTTP(S) LB → **allow health-check ranges in the firewall** (Exam 1 · Q8), (Exam 3 · Q38).
- Better CDN hit ratio → **customize cache keys** (drop the protocol), not shorter TTLs (Exam 2 · Q25).
- Multi-region Cloud Run, HA and low latency → **serverless NEGs behind a global external Application LB** (Exam 4 · Q45).
- Force all Cloud Run traffic through Cloud Armor → **ingress = internal + Cloud Load Balancing + serverless NEG** (Exam 5 · Q36).
- App Engine standard to an on-prem database over existing VPN → **Serverless VPC Access** (Exam 3 · Q25).
- Cloud Run can't reach default AlloyDB → **Direct VPC egress** (Exam 5 · Q45).

### Traps
- A second load balancer means a new IP, DNS record and certificate (Exam 1 · Q1).
- Giving backends public IPs doesn't help. Load balancers reach backends on internal IPs, and the health-check rule is what's missing (Exam 1 · Q8).
- A `Cache-Region` header doesn't exist. Shorter expiry lowers the hit ratio (Exam 2 · Q25).
- Latency-based Cloud DNS isn't a Google Cloud routing policy for Cloud Run, and Cloud Run is regional, not zonal. Use serverless NEGs (Exam 4 · Q45).
- IAP on Cloud Run authenticates users. It doesn't stop the `run.app` URL from bypassing Cloud Armor, and VPC firewall rules don't apply to Cloud Run ingress (Exam 5 · Q36).
- Private Google Access and Private Services Access don't connect a serverless app to on-prem (Exam 3 · Q25).
- App Engine firewall rules control traffic *into* App Engine, not its path to on-prem (Exam 1 · Q50).
- kubemci and "Ingress for Anthos" (now Multi Cluster Ingress) are GKE answers. The legacy Mountkirk case says Compute Engine (Exam 4 · Q40).

---

## 5. Compute Engine provisioning: images, MIGs, autoscaling and VM types

### Key facts
- **Custom image → instance template → managed instance group (MIG)**. An image is the reusable boot artifact. A template references an image; it can't be built from a disk directly (Exam 2 · Q8).
- **Bake dependencies into the image** to cut boot time. Startup scripts, Puppet or Ansible install packages on every boot, which is slow (Exam 2 · Q21). Deployment Manager in that question has reached end of support; Google now points to **Infrastructure Manager** (managed Terraform).
- Images are global and can be shared across projects through IAM, and **image families** point to the newest image in a series. That's the clean way to keep a copy of a VM in another project and region up to date (Exam 3 · Q43).
- MIG autoscaling signals: CPU, load-balancer serving capacity, Pub/Sub queue or **Cloud Monitoring metrics**. Memory isn't visible without the **Ops Agent**.
- Google's documented memory policy is `agent.googleapis.com/memory/percent_used`, filter **`metric.label.state = 'used'`**, target 80, type **GAUGE**. Without the filter, all states (used, cached, free…) are summed. An `AND` of four `state` values matches no time series, so autoscaling never fires (Exam 5 · Q51). (Exam 4 · Q4) keys a different answer; see the questionable answers.
- **Spot VMs** (the successor to preemptible VMs) cost 60–91% less, can be stopped at any time with about 30 seconds' notice, and have no 24-hour limit. Use them for fault-tolerant batch work that tolerates interruption (Exam 5 · Q7).
- **Graceful shutdown** of Spot or preemptible VMs → a script in the **`shutdown-script` metadata key**. It runs best-effort within the notice period (Exam 1 · Q30).
- **Sole-tenant nodes** give physically dedicated hosts. VMs land on them through **node affinity labels**: `compute.googleapis.com/node-group-name` for a group, **`compute.googleapis.com/node-name`** for one specific node (Exam 3 · Q31).
- Committed use discounts are Google's discount for steady load; "reserved instances" is AWS terminology (Exam 5 · Q7).

### Decision rules
- Stateless app slows at peak hours → **custom image from the disk → template → autoscaled MIG** (Exam 2 · Q8).
- Many OS packages, fast scale-out → **custom image**, not a startup script (Exam 2 · Q21).
- Copy a production VM into another project and region and keep it updatable → **image-based copy** (the key: snapshot → image → new VM from the image) (Exam 3 · Q43).
- Memory autoscaling not firing with the 4-way `AND` filter → change the filter to `state = 'used'` (Exam 5 · Q51).
- Interruptible, non-urgent batch, lower cost → **Spot VMs** (Exam 5 · Q7).
- One dedicated node per client → **node affinity on node name** (Exam 3 · Q31).

### Traps
- An instance template can't be made "from a disk" and then turned into an image. Snapshots aren't templates (Exam 2 · Q8).
- `/etc/rc6.d` scripts and xinetd services aren't how Compute Engine signals preemption (Exam 1 · Q30).
- Network tags don't place VMs on sole-tenant nodes; affinity labels do (Exam 3 · Q31).
- `DELTA_PER_MINUTE` is for counters, not a memory gauge. `bytes_used` is an absolute number that can't be compared to an 80% target (Exam 5 · Q51), (Exam 4 · Q4).
- `dd` + `netcat` copies are manual and fragile (Exam 3 · Q43).
- Cloud Run functions aren't built for long batch jobs, and standard VMs pay full price for interruptible work (Exam 5 · Q7).

---

## 6. Persistent disks: resizing, performance and backups

### Key facts
- A Persistent Disk can be **enlarged while the VM runs** (never shrunk). Then grow the file system online: **`resize2fs`** for ext4 (`xfs_growfs` for XFS), after `growpart` if the disk is partitioned. No restart, no new disk (Exam 1 · Q13).
- **Persistent Disk performance scales with size.** SSD PD gets a 6,000 IOPS baseline plus 30 IOPS per GB, capped by the VM's machine type. An 80 GB SSD PD gets about 8,400 IOPS; at 500 GB, about 21,000. Growing the disk is the quick, online way to get more I/O (Exam 1 · Q18), (Exam 2 · Q61).
- Changing a VM's memory or machine type requires stopping it (Exam 2 · Q61).
- **Hyperdisk**, the newer block storage, lets you provision IOPS and throughput independently of size. Older questions assume PD rules.
- **Local SSD** is physically attached, very fast and **ephemeral**: data is lost when the VM stops or is preempted.
- **PD snapshots** are incremental, crash-consistent copies of a **whole disk**. They can't pick out one database on a shared disk (Exam 3 · Q44).

### Decision rules
- Disk nearly full, minimal downtime → **resize the PD in place + `resize2fs`** (Exam 1 · Q13).
- MySQL import job on a small SSD PD is slow → **resize the SSD PD to 500 GB** and use **bulk inserts** (Exam 1 · Q18).
- Same scenario, the VM "cannot be restarted until the next maintenance event", fast and cheap → **resize the SSD PD** only (Exam 2 · Q61).
- Fast backup of **one** MySQL database without hurting disk performance → the key is **PDs in RAID 10 + LVM snapshots, uploaded to Cloud Storage** (Exam 3 · Q44). This key is disputed; see the questionable answers.

### Traps
- `fdisk` shows the new size but doesn't grow the file system (Exam 1 · Q13).
- Shutting down to resize, or snapshot-and-restore to a larger disk, means needless downtime (Exam 1 · Q13).
- More RAM, switching to PostgreSQL, or moving an OLTP import to BigQuery doesn't fix a disk-IOPS bottleneck (Exam 1 · Q18), (Exam 2 · Q61).
- Writing `mysqldump` straight to a Cloud Storage FUSE mount is slow; FUSE isn't a database or backup file system (Exam 3 · Q44).

---

## 7. Cloud Storage and BigQuery data lifecycle

### Key facts
- **Storage classes**: Standard (hot), **Nearline** (30-day minimum, about once a month), **Coldline** (90-day minimum, about once a quarter), **Archive** (365-day minimum, under once a year). All return data in **milliseconds**; colder classes trade lower storage cost for retrieval fees and minimum storage durations (Exam 5 · Q3), (Exam 5 · Q40).
- **Object Lifecycle Management** rules apply an action (`Delete`, `SetStorageClass`) when conditions match (`age`, `createdBefore`, `numNewerVersions`, `isLive`…). They are written in **JSON** and applied with `gcloud storage buckets update --lifecycle-file` (formerly `gsutil lifecycle set`) (Exam 1 · Q16), (Exam 2 · Q34).
- **Object Versioning** keeps noncurrent versions when objects are overwritten or deleted. Use it for history and recovery from accidental edits. Pair it with a `numNewerVersions` lifecycle rule to control cost (Exam 4 · Q3).
- **Retention policy / Bucket Lock** prevents deletion *before* a date (WORM). Versioning keeps history; lifecycle deletes *after* a date (Exam 4 · Q3), (Exam 2 · Q34).
- **Autoclass** can move objects between classes automatically based on access, as an alternative to hand-written rules.
- **BigQuery partition expiration** drops each partition when it ages out, so a time-partitioned table keeps a rolling window. Table expiration deletes the **whole table**. Partitions not modified for 90 days are billed at the lower long-term storage rate automatically (Exam 2 · Q15), (Exam 5 · Q40).

### Decision rules
- Delete backups older than 90 days → **lifecycle rule (JSON) with `age: 90`, action Delete**, not a cron script (Exam 1 · Q16).
- Keep medical records up to N years from creation, delete as soon as allowed → **Cloud Storage + lifecycle Delete** (Exam 2 · Q34).
- Old versions must stay accessible, with a full change history and easy undo → **Object Versioning** (Exam 4 · Q3).
- Hot media fast, old media cheap but durable → **lifecycle transitions Standard → Nearline → Coldline/Archive** (Exam 5 · Q3).
- Last 30 days hot, then read quarterly, keep 5 years, cheapest → **Standard, then Coldline after 30 days** (Exam 5 · Q40).
- Logs in BigQuery, delete after 45 days → **time-partitioned tables + 45-day partition expiration** (Exam 2 · Q15).

### Traps
- **Archive** for quarterly reads costs more: 365-day minimum and the highest retrieval fees (Exam 5 · Q40).
- Bucket Lock blocks deletion; it doesn't keep history. Change notifications only notify (Exam 4 · Q3).
- BigQuery has no default 45-day deletion, and a 45-day table expiration deletes the entire table (Exam 2 · Q15).
- Google Drive with manual deletes, or a nightly script, isn't policy-driven retention (Exam 2 · Q34).
- Moving media files into BigQuery tables makes no sense; BigQuery is for analytics (Exam 5 · Q3).
- Loading all raw transactions into BigQuery for five years costs more than Coldline objects when they're only read quarterly (Exam 5 · Q40).

---

## 8. GKE: scaling, services and multi-cluster

### Key facts
- **Horizontal Pod Autoscaler (HPA)** adds pods based on CPU, memory or custom/external metrics. **Cluster Autoscaler** adds nodes when pods can't be scheduled. Use both. Never configure autoscaling on the node pool's MIG directly (Exam 2 · Q16), (Exam 2 · Q30).
- Enable node autoscaling on a **running cluster** with `gcloud container clusters update … --enable-autoscaling --min-nodes --max-nodes` (add `--node-pool` for a specific pool). It is GA now, so no `alpha`, and no need to recreate the cluster (Exam 3 · Q48).
- Autoscale a Pub/Sub consumer on **backlog**: an HPA on the external metric **`subscription/num_undelivered_messages`**. CPU is misleading for I/O-bound work (Exam 3 · Q14).
- **Ingress** on GKE creates an external **Application Load Balancer**: HTTPS termination, certificates, path routing. A Service of `type: LoadBalancer` creates a layer-4 passthrough Network Load Balancer (Exam 2 · Q30).
- **Deployment + ClusterIP Service**: the Deployment sets replicas, and the Service gives a stable internal virtual IP and DNS name (`svc.namespace.svc.cluster.local`). Bare Pods aren't managed or scaled (Exam 3 · Q3).
- **StatefulSet** gives each pod a stable, ordered name and hostname (`web-0`, `web-1`) through a headless Service, and stable storage per pod (Exam 2 · Q24).
- **Requests** decide scheduling and the capacity you reserve. **Limits** cap usage. Setting requests just above normal usage, with higher limits, packs nodes efficiently and still allows bursts (Exam 5 · Q24).
- **Multi-cluster Gateway** on a **fleet** puts one global load balancer in front of clusters in several regions. With the full app in each cluster, a whole region can fail and the app stays up (Exam 5 · Q22).

### Decision rules
- Scale nodes with CPU load → **HPA + Cluster Autoscaler** (Exam 2 · Q16).
- Dockerized HTTPS app, autoscaling → **HPA + Cluster Autoscaler + Ingress** (Exam 2 · Q30).
- Make an existing cluster autoscale → **`clusters update --enable-autoscaling`** (Exam 3 · Q48).
- Pub/Sub consumer falling behind → **HPA on `num_undelivered_messages`** (Exam 3 · Q14).
- Internal microservices with independent replicas and stable addresses → **Deployment + ClusterIP + Service DNS** (Exam 3 · Q3).
- Stable hostnames across restarts → **StatefulSet** (Exam 2 · Q24).
- Overprovisioned pods, keep burst headroom → **lower requests to slightly above typical usage** (Exam 5 · Q24).
- Survive a region failure, internet-facing → **fleet + full app per region + multi-cluster Gateway** (Exam 5 · Q22).

### Traps
- `maxSurge`/`maxUnavailable` control rolling updates, not autoscaling (Exam 2 · Q16), (Exam 2 · Q30).
- `push_request_latencies` applies to push subscriptions; a pulling app scales on the backlog (Exam 3 · Q14).
- `--enable-autoscaling` at cluster creation means rebuilding; tags don't enable autoscaling; `resize` is manual (Exam 3 · Q48), (Exam 3 · Q14).
- Persistent Volumes keep data but not names; RBAC and environment variables aren't about identity (Exam 2 · Q24).
- Ingress IPs are for external HTTP traffic, not service-to-service addressing inside a cluster (Exam 3 · Q3).
- Requests equal to limits keeps the waste. VPA in Auto mode evicts pods to resize them, which hurts stateful pods (Exam 5 · Q24).
- Splitting microservices across regions makes every region a single point of failure for part of the app (Exam 5 · Q22).

---

## 9. Vertex AI, Model Garden and AI infrastructure

### Key facts
- **Vertex AI** is Google Cloud's unified ML platform: Workbench and Colab Enterprise notebooks, training jobs, **Vertex AI Pipelines** (Kubeflow/TFX pipelines that automate data prep → train → evaluate → deploy), Model Registry, Endpoints and monitoring. "Shared toolset + scalability + hand-off to operations" → **Vertex AI with MLOps workflows** (Exam 5 · Q63). It replaced AI Platform / Cloud ML Engine.
- **Model Garden** catalogs Google, partner and open models. Open models such as **Gemma** can be deployed to **your own Vertex AI endpoint in the region you pick**, so inference stays in that region (Exam 5 · Q39).
- Google-managed **Gemini API** endpoints decide where processing happens. Data-residency promises depend on the region and model, so a strict "never leave the country" rule favors a self-deployed model in that country's region (Exam 5 · Q39).
- **Pre-built AI APIs** each do one job: Vision (images), Video Intelligence, Speech-to-Text / Text-to-Speech, Translation, **Natural Language** (entities, sentiment, classification — no summaries). Use them when the task fits; use Gemini or Model Garden models for generation and summarization (Exam 5 · Q39).
- **Gemini Enterprise** (formerly Google Agentspace) provides enterprise search, AI agents and NotebookLM for employees. It's an exam-guide topic with no question in this bank yet.
- **AI Hypercomputer** is Google's stack of GPUs, TPUs, storage and networking for AI. For training that **tolerates interruption**, use **Spot VMs with accelerators + Persistent Disk + checkpointing**, so a preempted job resumes instead of restarting (Exam 5 · Q77).
- **Cloud Storage FUSE** (`gcsfuse`) mounts a bucket as a file system on each VM or GKE pod, with optional local caching. It's the simplest, cheapest way to give many GPU VMs file access to a large dataset (Exam 5 · Q76).

### Decision rules
- Self-managed Jupyter → shared, scalable ML platform with deployment hand-off → **Vertex AI + MLOps** (Exam 5 · Q63).
- Strong pretrained summarizer + strict in-country processing → **Gemma from Model Garden on a Vertex AI endpoint in that region** (Exam 5 · Q39).
- Interruptible accelerator batch, low cost, data must persist → **Spot + PD + checkpoints** (Exam 5 · Q77).
- Many GPU VMs need file-style access to a bucket → **gcsfuse** (Exam 5 · Q76).

### Traps
- AutoML limits flexibility, and Cloud Deploy isn't a model-serving pipeline (Exam 5 · Q63).
- VPC Service Controls limit data exfiltration; they don't change where a managed model processes data. Training a summarizer from scratch is slow and costly (Exam 5 · Q39).
- Local SSD on Spot VMs is lost at preemption, so there is no persistence (Exam 5 · Q77).
- Filestore copies and per-VM `gsutil` downloads add cost and duplicated storage. A PD can be shared read-write only in limited multi-writer modes (Exam 5 · Q76).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 4 · Q4)** | Keyed D (filter `state = 'free'`, target 20). Google's docs use exactly the stem's config (`percent_used`, `state = 'used'`, GAUGE). The autoscaler adds VMs when the metric is *above* target, so free memory would scale the wrong way. (Exam 5 · Q51) keys `state = 'used'` as the fix. No option is clearly right; answer D on this exact question, but learn `state = 'used'`. |
| **(Exam 3 · Q44)** | Keyed D (PDs in RAID 10 + LVM snapshots). LVM snapshots are copy-on-write and add write overhead, and they capture a whole volume, not one database. Many candidates prefer B (dump to Local SSD, then copy to Cloud Storage). Answer D if you see this wording. |
| **(Exam 3 · Q43)** | Keyed D (snapshot → image exported to Cloud Storage → VM). The export step isn't needed: images are global and can be shared with another project through IAM, and snapshots can also boot VMs in other regions and projects. The bank's explanation said otherwise and has been corrected. Pick the image-based answer. |
| **(Exam 1 · Q50)** | Keyed D (App Engine flexible + Cloud VPN). Still the best option offered, but App Engine standard can now reach on-prem through a Serverless VPC Access connector (Exam 3 · Q25). |

---

## Last-minute cheat sheet

- Small link, 99.99%, cheap → **one HA VPN gateway, two tunnels** (Exam 4 · Q5), (Exam 4 · Q9). VPN gateways are **regional** (Exam 2 · Q14).
- Big, private, low latency, 10 Gbps+ → **Dedicated Interconnect** (Exam 1 · Q25), (Exam 1 · Q40), (Exam 2 · Q41). VPN losing packets → Interconnect (Exam 1 · Q37).
- No colocation nearby or less to manage → **Partner Interconnect** (Exam 4 · Q55), (Exam 5 · Q2).
- 99.99% Interconnect → **2 + 2 connections in two metros** (Exam 4 · Q20). EHR → add a Dedicated Interconnect (Exam 4 · Q19).
- Guaranteed latency → **Premium Tier + Interconnect** (Exam 5 · Q28).
- **Non-overlapping custom VPC ranges** (Exam 1 · Q47), (Exam 4 · Q64). Overlap with on-prem → **Hybrid NAT** (Exam 2 · Q51). Partial overlap between orgs → **VPN** (Exam 3 · Q64).
- Peering is **non-transitive**: across orgs (Exam 4 · Q2), hub-and-spoke isolation (Exam 5 · Q37). One VM in three VPCs → **multi-NIC** (Exam 4 · Q53). Migration + modernization → **Shared VPC** (Exam 5 · Q29).
- Lower priority number wins; implied **deny ingress / allow egress** (Exam 2 · Q28). Tiers → **tags or service accounts** in firewall rules (Exam 1 · Q31), (Exam 3 · Q39), (Exam 2 · Q9), (Exam 5 · Q65).
- Private VM → Google APIs: **Private Google Access** (Exam 1 · Q51). → Internet: **Cloud NAT** (Exam 4 · Q7), (Exam 3 · Q24).
- Same domain, new API version → **path rules** (Exam 1 · Q1). VMs recycling → **health-check firewall rule** (Exam 1 · Q8), (Exam 3 · Q38). CDN hit ratio → **cache keys** (Exam 2 · Q25).
- Multi-region Cloud Run → **serverless NEGs + global LB** (Exam 4 · Q45); no bypass → **ingress internal + Cloud LB** (Exam 5 · Q36).
- Serverless → private IPs: **Serverless VPC Access** (Exam 3 · Q25), **Direct VPC egress** (Exam 5 · Q45); App Engine flex is already in the VPC (Exam 1 · Q50). Legacy Mountkirk → **global LB + MIG** (Exam 4 · Q40).
- **Image → template → MIG** (Exam 2 · Q8); bake packages into the image (Exam 2 · Q21); copy VMs via images (Exam 3 · Q43).
- Memory autoscaling: **Ops Agent, `percent_used`, `state='used'`, GAUGE** (Exam 5 · Q51), (Exam 4 · Q4).
- Interruptible batch → **Spot VMs** (Exam 5 · Q7); graceful stop → **`shutdown-script` metadata** (Exam 1 · Q30); dedicated host per client → **node-name affinity** (Exam 3 · Q31).
- Disk full → **resize online + `resize2fs`** (Exam 1 · Q13). Slow DB → **bigger SSD PD** (+ bulk inserts) (Exam 1 · Q18), (Exam 2 · Q61). One-database backup → keyed **RAID 10 + LVM** (Exam 3 · Q44).
- Auto-delete → **lifecycle rule (JSON)** (Exam 1 · Q16), (Exam 2 · Q34). History → **versioning** (Exam 4 · Q3). Tiering → **Standard → Nearline → Coldline/Archive** (Exam 5 · Q3); quarterly reads → **Coldline** (Exam 5 · Q40). BigQuery → **partition expiration** (Exam 2 · Q15).
- GKE → **HPA + Cluster Autoscaler + Ingress** (Exam 2 · Q16), (Exam 2 · Q30), `clusters update --enable-autoscaling` (Exam 3 · Q48), Pub/Sub backlog metric (Exam 3 · Q14).
- **ClusterIP + DNS** (Exam 3 · Q3); **StatefulSet** for stable names (Exam 2 · Q24); requests near real usage (Exam 5 · Q24); region-proof → **fleet + multi-cluster Gateway** (Exam 5 · Q22).
- ML platform → **Vertex AI + MLOps** (Exam 5 · Q63); in-country inference → **Gemma on a regional endpoint** (Exam 5 · Q39); **Spot + PD + checkpoints** (Exam 5 · Q77); bucket as file system → **gcsfuse** (Exam 5 · Q76).
