# Domain 3 — Designing for Security and Compliance

79 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q9

**You have written a Python script to connect to Google BigQuery from a Google Compute Engine virtual machine. However, the script is displaying errors indicating that it cannot connect to BigQuery. What should you do to resolve this issue?**

- A. Install the latest BigQuery API client library for Python.
- B. Run the script on a new virtual machine with the BigQuery access scope enabled.
- C. Create a new service account with BigQuery access and execute the script using that account.
- D. Install the BigQuery (`bq`) component for `gcloud` using the command `gcloud components install bq`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a new service account with BigQuery access and execute the script using that account.

**Correct Answer:**

**C. Create a new service account with BigQuery access and execute the script using that account.**

**Explanation:**

If your **Python script cannot connect to BigQuery** from a **Google Compute Engine (GCE) virtual machine**, the most common reason is **insufficient IAM permissions** or **missing authentication credentials**.

✅ **Creating and using a service account with BigQuery access** ensures that the script has the **necessary authentication and authorization** to interact with BigQuery.

**Steps to Fix the Issue:**

1. **Create a Service Account** in Google Cloud IAM:
  - Assign the **BigQuery User** or **BigQuery Data Viewer/Editor** role, depending on required permissions.
2. **Generate a JSON Key File** for the service account and securely store it on the GCE instance.
3. **Set the Authentication Environment Variable** before running the script:
  ```
  texport GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
  ```
4. **Ensure the Python script uses the service account credentials** via `google.auth`:
  ```
  from google.cloud import bigquery client = bigquery.Client()
  ```
  - If the `GOOGLE_APPLICATION_CREDENTIALS` variable is set correctly, BigQuery will authenticate using the service account.

✅ **Supporting Documentation:**

- **Authenticating to BigQuery:**
  **https://cloud.google.com/bigquery/docs/authentication/service-account-file**
- **Service Account IAM Roles:**
  **https://cloud.google.com/iam/docs/understanding-roles**

**Why Other Options Are Incorrect:**

**A. Install the latest BigQuery API client library for Python.** ❌

- Installing the `google-cloud-bigquery` library is **necessary** but **not sufficient** to fix authentication issues.
- The error suggests a **connection issue**, which is usually related to **authentication**, not missing libraries.

✅ **Reference:**

- **https://cloud.google.com/python/docs/reference/bigquery/latest**

**B. Run the script on a new virtual machine with the BigQuery access scope enabled.** ❌

- While enabling **BigQuery API access scopes** on a VM **can help**, the **default Compute Engine service account** may still lack **sufficient IAM permissions**.
- The best practice is to **use a dedicated service account with explicit BigQuery permissions** rather than relying on access scopes alone.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/access/service-accounts**

**D. Install the BigQuery (bq) component for gcloud using the command `gcloud components install bq`.** ❌

- The `bq` command-line tool is **useful for manually running queries**, but it **does not affect a Python script’s ability to authenticate and connect** to BigQuery.
- The Python script requires authentication using the **Google Cloud SDK or a service account** rather than just the `bq` CLI tool.

✅ **Reference:**

- **https://cloud.google.com/sdk/gcloud/reference/components/install**

**Conclusion:**

The best way to resolve the **authentication issue in a Python script connecting to BigQuery** from a GCE instance is:

1. **Create a new service account** with BigQuery access.
2. **Generate a JSON key file** for authentication.
3. **Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable**.

📌 **Final Reference:**
**https://cloud.google.com/bigquery/docs/authentication/service-account-file**

**⚠️ Note:** Two things can block a VM from calling BigQuery: the attached service account lacks a BigQuery IAM role, or the VM's access scopes don't include BigQuery (the default scopes don't). Option B fixes the scope; the key fixes the identity. Current best practice is a dedicated service account with least-privilege BigQuery roles, attached to the VM with the cloud-platform scope, not a downloaded JSON key. Learn the key, but expect the scope option to be argued.

</details>

---

### Exam 1 · Q10

**A customer is migrating an existing corporate application from an on-premises data center to Google Cloud Platform. The business owners want to minimize user disruption during the transition. Additionally, the security team has strict requirements for storing passwords. Which authentication strategy should be implemented?**

- A. Use G Suite Password Sync to replicate passwords into Google.
- B. Federate authentication via SAML 2.0 with the existing Identity Provider.
- C. Provision users in Google using the Google Cloud Directory Sync tool.
- D. Require users to set their Google password to match their corporate password.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Federate authentication via SAML 2.0 with the existing Identity Provider.

**Correct Answer:**

**B. Federate authentication via SAML 2.0 with the existing Identity Provider.**

**Explanation:**

Federating authentication via **SAML 2.0** with the existing **Identity Provider (IdP)** is the best strategy because:

- **Minimizes user disruption**: Users can continue **logging in with their corporate credentials** without changing passwords or adopting new authentication methods.
- **Enhances security**: Passwords **remain stored and managed within the corporate IdP**, meeting the security team’s strict requirements for password storage.
- **Supports Single Sign-On (SSO)**: Users can authenticate once and access Google Cloud resources without re-entering credentials.
- **Google Cloud supports SAML 2.0 integration** with enterprise identity providers like **Microsoft Active Directory, Okta, and Ping Identity**.

✅ **Supporting Documentation:**

- **Setting up SAML for Google Cloud authentication:**
  **https://cloud.google.com/identity/docs/setup/saml**
- **Google Identity Platform Federation Options:**
  **https://cloud.google.com/identity/docs/federation**

**Why Other Options Are Incorrect:**

**A. Use G Suite Password Sync to replicate passwords into Google.** ❌

- **Incorrect** because **Google does not store user passwords** from external directories.
- **G Suite Password Sync** is used to synchronize **Active Directory (AD) passwords to Google Workspace**, but it does not provide **federated authentication**.
- The security team has **strict password storage policies**, and storing passwords in Google **may not meet compliance requirements**.

✅ **Reference:**

- **https://support.google.com/a/answer/2611859?hl=en**

**C. Provision users in Google using the Google Cloud Directory Sync tool.** ❌

- **Incorrect** because **Google Cloud Directory Sync (GCDS)** only synchronizes **user accounts and groups** but **does not synchronize passwords**.
- **GCDS does not provide authentication**—it only **mirrors identities** from Active Directory or LDAP to Google Cloud.
- This approach **does not enable SSO**, meaning users would have **separate login credentials** for Google Cloud, disrupting workflows.

✅ **Reference:**

- **https://cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction**

**D. Require users to set their Google password to match their corporate password.** ❌

- **Incorrect** because:
  - **Users would have to manage two separate passwords**, increasing complexity and risk.
  - **No enforcement mechanism** ensures that users maintain password synchronization between corporate systems and Google.
  - **Less secure** than SAML federation, where authentication happens via a centralized IdP.

✅ **Reference:**

- **https://cloud.google.com/identity/docs/federation**

**Conclusion:**

The best authentication strategy is **B. Federate authentication via SAML 2.0 with the existing Identity Provider**, because it:

- **Ensures seamless authentication** without user disruption.
- **Meets security requirements** by keeping passwords within the corporate system.
- **Supports Single Sign-On (SSO)** for a better user experience.

📌 **Final Reference:**
**https://cloud.google.com/identity/docs/setup/saml**

</details>

---

### Exam 1 · Q14

**Your application is required to process credit card transactions. To minimize the scope of Payment Card Industry (PCI) compliance while still allowing analysis of transactional data and payment trends, how should you design your architecture?**

- A. Implement a **tokenization service** and store only tokenized data.
- B. Use **separate projects** exclusively for processing credit card data.
- C. Configure **separate subnetworks** to isolate components handling credit card data.
- D. Simplify the **audit discovery process** by labeling all virtual machines (VMs) that handle PCI data.
- E. **Export logs to Google BigQuery** and use **ACLs and views** to control data access for auditors.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Implement a **tokenization service** and store only tokenized data.

**Correct Answer:**

**A. Implement a tokenization service and store only tokenized data.**

**Explanation:**

To **minimize the scope of PCI compliance** while still allowing **transactional analysis**, the best practice is to **implement tokenization**.

- **Tokenization replaces sensitive credit card data** (PANs) with **non-sensitive tokens**.
- The **actual credit card data is never stored** in databases or logs, significantly reducing **PCI DSS scope**.
- Transactional data and payment trends can be **analyzed using tokenized values** while maintaining security.
- Google Cloud provides **Cloud Data Loss Prevention (DLP)** and **third-party tokenization solutions** that help achieve this.

✅ **Supporting Documentation:**

- **Google Cloud PCI Compliance Guide:**
  **https://cloud.google.com/security/compliance/pci-dss**
- **Tokenization and Encryption for PCI DSS Compliance:**
  **https://cloud.google.com/security/articles/tokenization-and-encryption**

**Why Other Options Are Incorrect:**

**B. Use separate projects exclusively for processing credit card data.** ❌

- **While separate projects improve isolation**, they do **not reduce PCI compliance scope**.
- If credit card data is **stored or processed**, **all components must comply with PCI DSS**, regardless of project separation.
- **Tokenization is a better approach** because it eliminates the need to store credit card numbers at all.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/pci-dss**

**C. Configure separate subnetworks to isolate components handling credit card data.** ❌

- **Network segmentation helps limit PCI scope**, but it does **not eliminate the storage of sensitive data**.
- **PCI DSS still applies** to all **in-scope** network segments, requiring extensive auditing and security controls.
- Tokenization is **more effective in reducing compliance scope** than just network isolation.

✅ **Reference:**

- **https://cloud.google.com/architecture/framework/security/design-secure-networks**

**D. Simplify the audit discovery process by labeling all virtual machines (VMs) that handle PCI data.** ❌

- **Labeling VMs is helpful for tracking, but it does not minimize PCI scope.**
- If a VM processes **actual credit card data**, it **remains in PCI scope** regardless of labels.
- Tokenization **removes the need to store PCI-sensitive data**, reducing compliance burden.

✅ **Reference:**

- **https://cloud.google.com/compute/docs/labeling-resources**

**E. Export logs to Google BigQuery and use ACLs and views to control data access for auditors.** ❌

- **BigQuery ACLs and views help with access control**, but they do **not reduce PCI compliance scope**.
- If **credit card numbers (PANs) are stored in logs or BigQuery**, **PCI DSS still applies**.
- Tokenization prevents **sensitive data from being stored** in logs or analytics tools.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/standard-sql/security**

**Conclusion:**

The best approach is **A. Implement a tokenization service and store only tokenized data**, because:

- **PCI-sensitive data is never stored**, minimizing compliance scope.
- **Transaction analysis remains possible** using tokenized values.
- **Security and audit complexity are significantly reduced**.

📌 **Final Reference:**
**https://cloud.google.com/security/articles/tokenization-and-encryption**

</details>

---

### Exam 1 · Q24

**Your organization requires that application metrics be retained for 5 years to support potential legal proceedings in the future. Which approach should you take?**

- A. Grant the security team access to logs in each project.
- B. Configure **Stackdriver Monitoring** for all projects and export the data to **BigQuery**.
- C. Configure **Stackdriver Monitoring** for all projects using the **default retention policies**.
- D. Configure **Stackdriver Monitoring** for all projects and export the data to **Google Cloud Storage**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Configure **Stackdriver Monitoring** for all projects and export the data to **Google Cloud Storage**.

**Correct Answer:**

**D. Configure Stackdriver Monitoring for all projects and export the data to Google Cloud Storage.**

**Explanation:**

Google Cloud **operations suite (formerly Stackdriver Monitoring)** retains **metrics data only for a limited period** (e.g., 6 weeks for free-tier users and up to 24 months for premium tiers). Since your organization requires metrics retention for **5 years**, exporting the data is necessary.

✅ **Why Export to Google Cloud Storage?**

- **Cloud Storage is designed for long-term archival storage** and supports **lifecycle policies for cost optimization**.
- **Supports regulatory compliance** and long-term legal retention requirements.
- **More cost-effective for long-term storage** compared to BigQuery, which incurs query costs.
- **Stackdriver Monitoring provides native integration** for exporting metrics to Cloud Storage.

✅ **Supporting Documentation:**

- **Cloud Monitoring Retention Periods:**
  **https://cloud.google.com/monitoring/quotas**
- **Exporting Monitoring Data to Cloud Storage:**
  **https://cloud.google.com/monitoring/docs/export**

**Why Other Options Are Incorrect:**

**A. Grant the security team access to logs in each project.** ❌

- **Incorrect because access control does not extend data retention.**
- **Security team access does not guarantee compliance** with long-term storage policies.
- **Cloud Monitoring metrics expire after their retention period** unless explicitly exported.

✅ **Reference:**

- **https://cloud.google.com/iam/docs/understanding-roles**

**B. Configure Stackdriver Monitoring for all projects and export the data to BigQuery.** ❌

- **BigQuery is a powerful analytics tool, but it incurs storage and query costs.**
- **Not the best option for long-term archival storage**—Google Cloud Storage is more suitable for compliance-driven retention.
- **BigQuery is better suited for querying structured data**, not raw metric storage.

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/introduction**

**C. Configure Stackdriver Monitoring for all projects using the default retention policies.** ❌

- **Cloud Monitoring's default retention policies do not meet the 5-year requirement.**
- **Free-tier users get only 6 weeks of metric retention**, while premium users get up to 24 months.
- **Without exporting data, it will be permanently lost after the retention period expires.**

✅ **Reference:**

- **https://cloud.google.com/monitoring/quotas**

**Conclusion:**

The best approach is **D. Configure Stackdriver Monitoring for all projects and export the data to Google Cloud Storage**, as it:

- **Ensures compliance with the 5-year retention requirement.**
- **Optimizes cost for long-term archival storage.**
- **Provides an efficient way to store and retrieve historical application metrics.**

📌 **Final Reference:**
**https://cloud.google.com/monitoring/docs/export**

**⚠️ Note:** Stackdriver Monitoring is now Cloud Monitoring, which keeps most metric data for 24 months. Anything longer has to be exported.

</details>

---

### Exam 1 · Q26

**Auditors conduct reviews every **12 months** and request an analysis of all **Google Cloud Identity and Access Management (Cloud IAM) policy changes** made during the previous year. You need a solution to **streamline and expedite** the audit process. What should you do?**

- A. Set up **custom Stackdriver alerts** and send the notifications to the auditor.
- B. Enable **Logging export to BigQuery** and use **ACLs and views** to restrict data access for the auditor.
- C. Use **Cloud Functions** to transfer log entries to **Cloud SQL** and apply **ACLs and views** to control auditor access.
- D. Enable **log export to Google Cloud Storage (GCS)**, store audit logs in a GCS bucket, and delegate access to the bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Enable **Logging export to BigQuery** and use **ACLs and views** to restrict data access for the auditor.

**Correct Answer:**

**B. Enable Logging export to BigQuery and use ACLs and views to restrict data access for the auditor.**

**Explanation:**

To **streamline and expedite IAM audit reviews**, the best approach is to **export audit logs to BigQuery**, where auditors can efficiently **query historical IAM policy changes**.

✅ **Why BigQuery is the Best Choice:**

- **Scalable and efficient query engine:** Allows **fast analysis** of **IAM policy changes over the past 12 months**.
- **Native integration with Cloud Audit Logs:** Supports **structured queries** for IAM policy modifications.
- **Access control using ACLs and views:** Restricts **auditor access** to only relevant data.
- **No manual log parsing required:** BigQuery enables **SQL-based queries** rather than manually searching raw logs.

✅ **Implementation Steps:**

1. **Enable Cloud Audit Logging** for **IAM policy changes** (`ADMIN_WRITE` logs).
2. **Set up log export to BigQuery** in a dedicated dataset.
3. **Create a restricted view in BigQuery** to allow **auditors to access only IAM policy change logs**.
4. **Grant auditors read-only access** to the dataset.

✅ **Supporting Documentation:**

- **Exporting Logs to BigQuery:**
  **https://cloud.google.com/logging/docs/export/bigquery**
- **Cloud Audit Logs Overview:**
  **https://cloud.google.com/logging/docs/audit**

**Why Other Options Are Incorrect:**

**A. Set up custom Stackdriver alerts and send the notifications to the auditor.** ❌

- **Not a scalable approach**—auditors require **historical IAM policy change logs**, not real-time alerts.
- **Notifications do not provide a full audit trail** for **past IAM changes over 12 months**.
- **BigQuery is a better tool** for analyzing historical policy changes.

✅ **Reference:**

- **https://cloud.google.com/monitoring/docs/alerts**

**C. Use Cloud Functions to transfer log entries to Cloud SQL and apply ACLs and views to control auditor access.** ❌

- **Unnecessary complexity**—Cloud SQL requires **manual ingestion** and **custom schema design**.
- **BigQuery is a managed analytics solution** designed for large-scale log queries, making it a better fit.
- **Cloud SQL is optimized for transactional data, not large-scale log analysis.**

✅ **Reference:**

- **https://cloud.google.com/sql/docs/introduction**

**D. Enable log export to Google Cloud Storage (GCS), store audit logs in a GCS bucket, and delegate access to the bucket.** ❌

- **GCS is suitable for raw log storage but does not support efficient querying.**
- **Auditors would have to manually parse logs**, making the process time-consuming.
- **BigQuery is the better choice for structured queries and rapid analysis.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/access-control**

**Conclusion:**

The best approach is **B. Enable Logging export to BigQuery and use ACLs and views to restrict data access for the auditor**, because:

- **BigQuery provides fast and scalable querying for IAM audit logs.**
- **IAM access controls allow secure, auditor-specific views.**
- **Fully automates log analysis without manual parsing.**

📌 **Final Reference:**
**https://cloud.google.com/logging/docs/export/bigquery**

</details>

---

### Exam 1 · Q27

**You are designing a large distributed application consisting of 30 microservices. Each microservice requires access to a database backend and must securely store its credentials. Where should you store these credentials?**

- A. Embed them in the **source code**.
- B. Store them in an **environment variable**.
- C. Use a **secret management system**.
- D. Store them in a **configuration file** with **restricted access via ACLs**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use a **secret management system**.

**Correct Answer:**

**C. Use a secret management system.**

**Explanation:**

To **securely store and manage credentials** for a **large distributed application with 30 microservices**, a **secret management system** is the best choice.

✅ **Why Use a Secret Management System?**

- **Secure storage and access control:** Ensures **credentials are encrypted** and **access is restricted** to authorized services.
- **Automated credential rotation:** Reduces security risks by **automatically updating and rotating secrets**.
- **Prevents hardcoding credentials** in application code, environment variables, or configuration files.
- **Google Cloud Secret Manager** provides a **centralized, auditable, and secure way to store and retrieve secrets** for microservices.

**Implementation Steps:**

1. **Use Google Cloud Secret Manager** to securely store database credentials.
2. **Grant least privilege IAM roles** to microservices that require access.
3. **Retrieve secrets programmatically** using the **Secret Manager API** or **client libraries**.

✅ **Supporting Documentation:**

- **Google Cloud Secret Manager Overview:**
  **https://cloud.google.com/secret-manager/docs**
- **Best Practices for Managing Secrets:**
  **https://cloud.google.com/architecture/secrets-management**

**Why Other Options Are Incorrect:**

**A. Embed them in the source code.** ❌

- **Hardcoding credentials in source code is a major security risk.**
- **Source code is often shared or exposed**, making credentials vulnerable to **leaks and unauthorized access**.
- **Difficult to update credentials**, requiring **code changes and redeployment**.

✅ **Reference:**

- **https://cloud.google.com/security/articles/secret-management**

**B. Store them in an environment variable.** ❌

- **Environment variables are not secure**—they can be accessed by **any process running on the system**.
- **Lack of encryption and auditing**, making it difficult to track **who accessed the credentials**.
- **Risk of accidental exposure** (e.g., logs, debugging tools).

✅ **Reference:**

- **https://cloud.google.com/security/articles/secret-management**

**D. Store them in a configuration file with restricted access via ACLs.** ❌

- **Configuration files can be compromised** if misconfigured or **accidentally exposed**.
- **Hard to enforce access control dynamically** across multiple microservices.
- **Manual credential rotation is cumbersome and prone to errors.**

✅ **Reference:**

- **https://cloud.google.com/security/articles/secret-management**

**Conclusion:**

The best approach is **C. Use a secret management system**, as it:

- **Securely stores credentials with encryption**.
- **Enforces IAM-based access controls**.
- **Enables automatic credential rotation**.
- **Prevents credential leaks and enhances security**.

📌 **Final Reference:**
**https://cloud.google.com/secret-manager/docs**

</details>

---

### Exam 1 · Q35

**Your organization wants to **centrally manage IAM policies** while allowing **each department to control its own policies independently**. Which approach should you take?**

- A. Use **multiple Organizations**, each containing multiple **Folders**.
- B. Set up **multiple Organizations**, with **one Organization per department**.
- C. Maintain a **single Organization** and create **Folders for each department**.
- D. Use a **single Organization** with **multiple projects**, each assigned to a central owner.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Maintain a **single Organization** and create **Folders for each department**.

**Correct Answer:**

✅ **C. Maintain a single Organization and create Folders for each department.**

**Explanation:**

In **Google Cloud Identity and Access Management (IAM)**, the **best way to centrally manage IAM policies** while **allowing departments to control their own policies independently** is to use:

- **A single Organization** (root node for centralized governance).
- **Folders for each department**, where each department can **define its own IAM policies**.

✅ **Why This Works:**

- **Folders allow delegation of IAM policies** while maintaining centralized control.
- **Inheritance of IAM policies** enables **organization-wide rules** while allowing **department-specific permissions**.
- **Departments can manage their own resources independently** while still being part of the same Organization.

**Implementation Example:**

1. **Create a Folder for each department** under the Organization.
2. **Assign IAM roles at the Folder level** to grant department admins control over their resources.
3. **Projects are placed within department-specific Folders**, inheriting the appropriate IAM policies.

✅ **Supporting Documentation:**

- **Google Cloud Resource Hierarchy Best Practices:**
  **https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy**

**Why Other Options Are Incorrect?**

**A. Use multiple Organizations, each containing multiple Folders.** ❌

- **Organizations are meant to represent a single company**, not separate departments.
- **Difficult to centrally manage IAM policies across multiple Organizations.**
- **Cross-organization IAM policy management is complex** and not recommended.

✅ **Reference:**

- **https://cloud.google.com/resource-manager/docs/creating-managing-organization**

**B. Set up multiple Organizations, with one Organization per department.** ❌

- **Each Organization would require separate IAM management, billing, and security policies.**
- **Departments would be completely isolated**, making it harder to enforce company-wide policies.
- **A single Organization with department-specific Folders is the recommended structure.**

✅ **Reference:**

- **https://cloud.google.com/resource-manager/docs/organization-policy/overview**

**D. Use a single Organization with multiple projects, each assigned to a central owner.** ❌

- **IAM policies at the project level do not allow independent department-level control.**
- **Centralized ownership limits department autonomy**, increasing operational bottlenecks.
- **Folders provide better separation and policy delegation than managing projects directly.**

✅ **Reference:**

- **https://cloud.google.com/resource-manager/docs/creating-managing-folders**

**Conclusion:**

The best approach is **C. Maintain a single Organization and create Folders for each department**, because:

- **It provides centralized IAM governance while allowing departmental autonomy.**
- **IAM policies can be set at different levels (Organization, Folder, Project).**
- **It simplifies resource and policy management across the organization.**

📌 **Final Reference:**
**https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy**

</details>

---

### Exam 1 · Q36

**In designing a mobile chat application, how can you prevent the spoofing of chat messages to ensure they are attributed to specific users?**

- A. Tag messages client side with the originating user identifier and the destination user.
- B. Encrypt the message client side using block-based encryption with a shared key.
- C. Use public key infrastructure (PKI) to encrypt the message client side using the originating user's private key.
- D. Use a trusted certificate authority to enable SSL connectivity between the client application and the server.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use public key infrastructure (PKI) to encrypt the message client side using the originating user's private key.

**Correct Answer:**

✅ **C. Use public key infrastructure (PKI) to encrypt the message client-side using the originating user's private key.**

**Explanation:**

To **prevent the spoofing of chat messages** and **ensure messages are correctly attributed to specific users**, a **cryptographic approach that verifies message authenticity** is needed.

✅ **Why PKI and Digital Signatures Work?**

- **Public Key Infrastructure (PKI)** provides a **mechanism for authentication and non-repudiation**.
- **Each user has a key pair (public + private key)**, where:
  - The **private key is used to sign messages** before sending.
  - The **public key is used to verify** the signature upon receipt.
- **Prevents attackers from forging messages**, as they cannot generate a valid signature without the sender's private key.

✅ **Implementation Steps:**

1. **User generates a key pair** (Public/Private Key).
2. **Client signs the message using their private key** before sending.
3. **Server verifies the signature using the sender’s public key**.
4. **If the signature is valid, the message is authenticated** as coming from the correct user.

✅ **Supporting Documentation:**

- **Google Cloud PKI and Digital Signatures:**
  **https://cloud.google.com/security/encryption-in-transit**
- **Digital Signature Mechanism Overview:**
  [**https://en.wikipedia.org/wiki/Digital_signature**](https://en.wikipedia.org/wiki/Digital_signature)

**Why Other Options Are Incorrect?**

**A. Tag messages client-side with the originating user identifier and the destination user.** ❌

- **User identifiers can be easily spoofed** if not cryptographically protected.
- **No security mechanism ensures message authenticity**—an attacker could manipulate the sender ID.

✅ **Reference:**

- **https://owasp.org/www-community/controls/Message_Authentication**

**B. Encrypt the message client-side using block-based encryption with a shared key.** ❌

- **Encryption alone does not verify the sender's identity**—anyone with the key can generate messages.
- **Does not prevent spoofing**, as an attacker who obtains the shared key can send messages as someone else.

✅ **Reference:**

- **https://cryptobook.nakov.com/symmetric-key-ciphers/message-authentication-codes**

**D. Use a trusted certificate authority to enable SSL connectivity between the client application and the server.** ❌

- **SSL/TLS ensures secure transport** but **does not authenticate message contents**.
- **An attacker could still modify message payloads before sending them.**

✅ **Reference:**

- **https://cloud.google.com/security/encryption-in-transit**

**Conclusion:**

The best approach is **C. Use public key infrastructure (PKI) to encrypt the message client-side using the originating user's private key**, because it:

- **Ensures message authenticity** (only the rightful user can sign messages).
- **Prevents spoofing** (attackers cannot forge valid messages).
- **Allows secure verification on the server side using public keys**.

📌 **Final Reference:**
[**https://en.wikipedia.org/wiki/Digital_signature**](https://en.wikipedia.org/wiki/Digital_signature)

</details>

---

### Exam 1 · Q38

**Your **customer support tool** logs all **email and chat conversations** to **Cloud Bigtable** for **retention and analysis**. To comply with **privacy and security requirements**, what is the recommended approach for **removing personally identifiable information (PII) and payment card information (PCI)** before storing the data?**

- A. **Hash all data** using **SHA-256**.
- B. **Encrypt all data** using **elliptic curve cryptography (ECC)**.
- C. **De-identify the data** using the **Cloud Data Loss Prevention (DLP) API**.
- D. Use **regular expressions** to identify and redact **phone numbers, email addresses, and credit card numbers**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **De-identify the data** using the **Cloud Data Loss Prevention (DLP) API**.

**Correct Answer:**

✅ **C. De-identify the data using the Cloud Data Loss Prevention (DLP) API.**

**Explanation:**

To comply with **privacy and security requirements** when storing **personally identifiable information (PII) and payment card information (PCI) in Cloud Bigtable**, the best approach is to use **Google Cloud Data Loss Prevention (DLP) API** for **de-identification**.

✅ **Why Cloud DLP API?**

- **Automatically detects and removes PII & PCI** (e.g., names, emails, credit card numbers).
- **Supports tokenization, redaction, and pseudonymization**, ensuring compliance with **GDPR, HIPAA, and PCI DSS**.
- **More reliable than regex-based solutions**, which may miss complex data patterns.
- **Can apply irreversible transformations** to ensure sensitive data is no longer identifiable.

**Implementation Example:**

1. **Use Cloud DLP API to scan incoming data.**
2. **Apply de-identification techniques:**
  - **Redaction**: Remove sensitive data.
  - **Tokenization**: Replace data with a non-reversible token.
  - **Format-preserving encryption (FPE)**: Protect structured data.
3. **Store the de-identified data in Bigtable.**

✅ **Supporting Documentation:**

- **Cloud DLP Overview:**
  **https://cloud.google.com/dlp/docs/deidentify-sensitive-data**
- **DLP Tokenization Guide:**
  **https://cloud.google.com/dlp/docs/pseudonymization**

**Why Other Options Are Incorrect?**

**A. Hash all data using SHA-256.** ❌

- **Hashing is irreversible**, making it **unsuitable for structured data** like emails or credit card numbers that may need retrieval.
- **Does not prevent data exposure** if attackers can use dictionary attacks or brute-force lookup tables.
- **DLP tokenization or redaction is a better approach.**

✅ **Reference:**

- **https://cloud.google.com/security/encryption-in-transit**

**B. Encrypt all data using elliptic curve cryptography (ECC).** ❌

- **Encryption protects data in transit and at rest** but does not remove **PII or PCI** before storage.
- **Decryption keys must be managed**, creating additional security concerns.
- **DLP API offers de-identification, which is more suitable for compliance.**

✅ **Reference:**

- **https://cloud.google.com/security/encryption-at-rest**

**D. Use regular expressions to identify and redact phone numbers, email addresses, and credit card numbers.** ❌

- **Regex-based solutions are error-prone** and can **miss complex patterns** in unstructured text.
- **Cloud DLP API is more reliable** as it uses **machine learning** to detect sensitive data.
- **Regex requires constant updates**, while Cloud DLP **automatically adapts to new data formats.**

✅ **Reference:**

- **https://cloud.google.com/dlp/docs/concepts-infotypes**

**Conclusion:**

The best approach is **C. De-identify the data using the Cloud Data Loss Prevention (DLP) API**, because it:

- **Automatically detects and removes PII/PCI**.
- **Supports compliance with security regulations** (GDPR, HIPAA, PCI DSS).
- **Is more robust and scalable than regex or encryption alone**.

📌 **Final Reference:**
**https://cloud.google.com/dlp/docs/deidentify-sensitive-data**

</details>

---

### Exam 1 · Q44

**Your company is migrating its on-premises data center to the cloud and plans to integrate Google Kubernetes Engine (GKE) for workload orchestration. Certain parts of your architecture must also comply with PCI DSS requirements.**

**Which statement is most accurate?**

- A. **App Engine** is the **only** compute platform on GCP that is **certified** for PCI DSS hosting.
- B. **GKE cannot be used** under PCI DSS because it is considered **shared hosting**.
- C. **GKE and GCP** provide the necessary **tools and configurations** to build a **PCI DSS-compliant** environment.
- D. **All Google Cloud services** can be used because **Google Cloud Platform** is **fully PCI-compliant**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **GKE and GCP** provide the necessary **tools and configurations** to build a **PCI DSS-compliant** environment.

**Correct Answer:**

✅ **C. GKE and GCP provide the necessary tools and configurations to build a PCI DSS-compliant environment.**

**Explanation:**

Google Cloud **does not automatically make workloads PCI DSS compliant**, but it **provides the necessary tools and configurations** to help organizations build a **PCI DSS-compliant environment** on **Google Kubernetes Engine (GKE)**.

✅ **Why GKE Can Be Used for PCI DSS Compliance?**

- **Google Cloud is PCI DSS compliant**, meaning **it provides a compliant infrastructure**.
- **GKE supports network segmentation, encryption, and access controls**, which are essential for PCI DSS compliance.
- **Google Cloud’s PCI DSS Attestation of Compliance (AOC) applies to services including GKE.**
- **Companies must still configure their applications correctly** to meet PCI DSS controls.

**Key PCI DSS Compliance Features in GCP and GKE:**

- **VPC Service Controls**: Restrict access to PCI-sensitive workloads.
- **Cloud Audit Logs**: Monitor user access and API calls for compliance.
- **Shielded VMs**: Protect Kubernetes worker nodes from unauthorized modifications.
- **Private GKE Clusters**: Prevent public exposure of workloads.
- **Encryption (At-Rest and In-Transit)**: Meet PCI DSS encryption requirements.

✅ **Supporting Documentation:**

- **Google Cloud PCI DSS Compliance Overview:**
  **https://cloud.google.com/security/compliance/pci-dss**
- **Best Practices for PCI DSS on GKE:**
  **https://cloud.google.com/blog/products/gcp/building-pci-dss-compliant-solutions-on-gcp**

**Why Other Options Are Incorrect?**

**A. App Engine is the only compute platform on GCP that is certified for PCI DSS hosting.** ❌

- **Incorrect because multiple GCP services, including GKE, Compute Engine, and Cloud SQL, can be used for PCI DSS-compliant workloads.**
- **Google Cloud provides PCI DSS compliance tools across multiple compute platforms.**

✅ **Reference:**

- **https://cloud.google.com/security/compliance/pci-dss**

**B. GKE cannot be used under PCI DSS because it is considered shared hosting.** ❌

- **Incorrect because PCI DSS compliance can be achieved in a shared responsibility model.**
- **Google Cloud provides isolation mechanisms such as private clusters, namespaces, and workload identity.**
- **Google Cloud maintains PCI DSS compliance for the infrastructure, while customers must implement application-level security.**

✅ **Reference:**

- **https://cloud.google.com/kubernetes-engine/docs/concepts/security-overview**

**D. All Google Cloud services can be used because Google Cloud Platform is fully PCI-compliant.** ❌

- **Incorrect because while Google Cloud is PCI DSS compliant, not all services are inherently PCI-compliant.**
- **Customers must implement additional controls** (e.g., encryption, network segmentation, logging).
- **GCP follows a shared responsibility model**—Google secures the infrastructure, but users must secure their applications.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/pci-dss**

**Conclusion:**

The best answer is **C. GKE and GCP provide the necessary tools and configurations to build a PCI DSS-compliant environment**, because:

- **Google Cloud provides PCI DSS compliance at the infrastructure level.**
- **GKE offers features (encryption, network controls, audit logs) to meet compliance requirements.**
- **Companies must implement best practices to achieve full PCI DSS compliance.**

📌 **Final Reference:**
**https://cloud.google.com/security/compliance/pci-dss**

</details>

---

### Exam 1 · Q46

**Google Cloud Platform (GCP) resources are **managed hierarchically** using **organizations, folders, and projects**. When **Cloud Identity and Access Management (IAM) policies** are applied at different levels of the hierarchy, what determines the **effective policy** at a specific node?**

- A. The effective policy is determined **only** by the policy set at that node.
- B. The effective policy is the policy set at the node and is **restricted** by the policies of its ancestors.
- C. The effective policy is the **union** of the policy set at the node and policies **inherited from its ancestors**.
- D. The effective policy is the **intersection** of the policy set at the node and policies inherited from its ancestors.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. The effective policy is the **union** of the policy set at the node and policies **inherited from its ancestors**.

**Correct Answer:**

✅ **C. The effective policy is the union of the policy set at the node and policies inherited from its ancestors.**

**Explanation:**

Google Cloud Platform (GCP) follows a **hierarchical resource model** for managing **Identity and Access Management (IAM) policies** at different levels:

1. **Organization (Root Level) → Folders → Projects → Resources**
2. **IAM policies inherit downward**, meaning:
  - Policies set at **higher levels (Organization, Folder, or Project)** apply to all **child resources**.
  - **Policies are additive**—permissions granted at a higher level **cannot be restricted by lower levels**.

✅ **Key IAM Inheritance Rules:**

- **If a role is granted at a higher level (e.g., Folder or Organization), it automatically applies to all child nodes unless an IAM deny policy blocks it.**
- **If a node (Project or Folder) has additional role bindings, they are combined with inherited policies to form the effective policy.**
- **Allow policies are additive.** Separate IAM deny policies (available since 2022) can block specific permissions, and they are evaluated before allow policies.

✅ **Example Scenario:**

1. **Organization Level:**
  - `user@example.com` is assigned **Viewer** (`roles/viewer`) at the **organization** level.
2. **Folder Level:**
  - The **folder inherits Viewer permissions** from the Organization.
  - Additionally, `user@example.com` is granted **Editor** (`roles/editor`) at the **folder level**.
3. **Project Level:**
  - The **project inherits both Viewer and Editor** from the folder.
  - If no additional roles are assigned at the project level, the user **has both Viewer and Editor permissions** on the project.

Thus, the **effective IAM policy at any node is the union of inherited and explicitly assigned permissions**.

✅ **Supporting Documentation:**

- **IAM Policy Hierarchy:**
  **https://cloud.google.com/iam/docs/policy-hierarchy**
- **Understanding IAM Policy Inheritance:**
  **https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy**

**Why Other Options Are Incorrect?**

**A. The effective policy is determined only by the policy set at that node.** ❌

- **Incorrect because IAM policies are inherited downward from parent nodes.**
- **Higher-level IAM policies (Organization, Folder) apply to all child resources.**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/policy-hierarchy**

**B. The effective policy is the policy set at the node and is restricted by the policies of its ancestors.** ❌

- **Incorrect because IAM policies are additive and cannot restrict permissions granted by ancestors.**
- **Once a permission is granted at a higher level, it applies to all child nodes unless explicitly removed (which GCP IAM does not support).**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/policies**

**D. The effective policy is the intersection of the policy set at the node and policies inherited from its ancestors.** ❌

- **Incorrect because IAM permissions do not get "intersected."**
- **Permissions are combined (union), not filtered (intersection).**

✅ **Reference:**

- **https://cloud.google.com/iam/docs/understanding-policies**

**Conclusion:**

The best answer is **C. The effective policy is the union of the policy set at the node and policies inherited from its ancestors**, because:

- **IAM policies are inherited downward** from Organization → Folder → Project → Resources.
- **Permissions are additive**—roles assigned at higher levels **apply to all child nodes**.
- **The effective policy is a combination of inherited and explicitly assigned roles.**

📌 **Final Reference:**
**https://cloud.google.com/iam/docs/policy-hierarchy**

**⚠️ Note:** IAM deny policies now exist and override allow policies. The answer is still C: the effective *allow* policy is the union of the node's allow policy and its ancestors'.

</details>

---

### Exam 1 · Q54

**Your company is using BigQuery as its enterprise data warehouse, with data distributed across multiple Google Cloud projects. All BigQuery queries must be billed to a single project, and no query costs should be incurred on the projects containing the data. Users should be able to query the datasets but not modify them.**

**How should you configure users' access roles?**

- A. Add all users to a **group**, then grant the group **BigQuery User** on the **billing project** and **BigQuery Data Viewer** on the projects containing the data.
- B. Add all users to a **group**, then grant the group **BigQuery Data Viewer** on the **billing project** and **BigQuery User** on the projects containing the data.
- C. Add all users to a **group**, then grant the group **BigQuery Job User** on the **billing project** and **BigQuery Data Viewer** on the projects containing the data.
- D. Add all users to a **group**, then grant the group **BigQuery Data Viewer** on the **billing project** and **BigQuery Job User** on the projects containing the data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Add all users to a **group**, then grant the group **BigQuery Job User** on the **billing project** and **BigQuery Data Viewer** on the projects containing the data.

**Correct Answer:**

✅ **C. Add all users to a group, then grant the group BigQuery Job User on the billing project and BigQuery Data Viewer on the projects containing the data.**

**Explanation:**

The requirement is that:

1. **All BigQuery queries must be billed to a single project** (the billing project).
2. **No query costs should be incurred on the projects containing the data**.
3. **Users must be able to query datasets but not modify them**.

**Role Breakdown for Proper Access Control:**

✅ **1. BigQuery Job User (`roles/bigquery.jobUser`) on the billing project:**

- **Required for running queries on behalf of the billing project.**
- **Ensures that all query costs are billed to this project.**
- **Users must have this role on the billing project to execute queries.**

✅ **2. BigQuery Data Viewer (`roles/bigquery.dataViewer`) on the projects containing the data:**

- **Allows users to read/query datasets in these projects.**
- **Prevents users from modifying or deleting data.**
- **Ensures that users can access the data without incurring billing in those projects.**

**Implementation Steps:**

1. **Create a Google Cloud IAM group (e.g., `bigquery-users-group`).**
2. **Assign the group the following roles:**
  - `roles/bigquery.jobUser` on the **billing project**.
  - `roles/bigquery.dataViewer` on the **projects containing the data**.
3. **Add users to the group.**
4. **Users now run queries using the billing project but access data from other projects.**

✅ **Supporting Documentation:**

- **BigQuery Job User Role (`roles/bigquery.jobUser`):**
  **https://cloud.google.com/bigquery/docs/access-control**
- **BigQuery Data Viewer Role (`roles/bigquery.dataViewer`):**
  **https://cloud.google.com/bigquery/docs/reference/roles**

**Why Other Options Are Incorrect?**

**A. Add all users to a group, then grant the group BigQuery User on the billing project and BigQuery Data Viewer on the projects containing the data.** ❌

- `BigQuery User` **(`roles/bigquery.user`) allows users to create datasets and tables** in the billing project, which is **not required**.
- **Users only need `BigQuery Job User` to run queries using the billing project.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/roles**

**B. Add all users to a group, then grant the group BigQuery Data Viewer on the billing project and BigQuery User on the projects containing the data.** ❌

- `BigQuery Data Viewer` **on the billing project does not allow users to run queries—it only allows viewing existing datasets.**
- `BigQuery User` **on the data projects allows users to create datasets/tables, which is unnecessary.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/roles**

**D. Add all users to a group, then grant the group BigQuery Data Viewer on the billing project and BigQuery Job User on the projects containing the data.** ❌

- **Incorrect because `BigQuery Job User` must be granted on the billing project, not on the data projects.**
- **Users would not be able to run queries using the billing project, leading to errors.**

✅ **Reference:**

- **https://cloud.google.com/bigquery/docs/reference/roles**

**Conclusion:**

The best approach is **C. Add all users to a group, then grant the group BigQuery Job User on the billing project and BigQuery Data Viewer on the projects containing the data**, because:
✔ **Ensures all queries are billed to the correct project.**
✔ **Allows users to read/query data but not modify it.**
✔ **Follows Google Cloud's recommended best practices for cross-project BigQuery access.**

📌 **Final Reference:**
**https://cloud.google.com/bigquery/docs/access-control**

</details>

---

### Exam 1 · Q55

**You have built an application using Cloud ML Engine that can recognize famous paintings from uploaded images. You need to test the application and allow specific users to upload images for the next 24 hours. Some users do not have a Google Account.**

**How should you enable users to upload images?**

- A. Have users upload images to **Cloud Storage** and **protect the bucket with a password** that expires after **24 hours**.
- B. Have users upload images to **Cloud Storage** using a **signed URL** that expires after **24 hours**.
- C. Create an **App Engine web application** for users to upload images and configure **App Engine to disable the application after 24 hours**. Authenticate users via **Cloud Identity**.
- D. Create an **App Engine web application** where users can upload images for the next **24 hours**. Authenticate users via **Cloud Identity**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Have users upload images to **Cloud Storage** using a **signed URL** that expires after **24 hours**.

**Correct Answer:**

✅ **B. Have users upload images to Cloud Storage using a signed URL that expires after 24 hours.**

**Explanation:**

Since some users **do not have a Google Account**, you need a **temporary, secure, and anonymous method** for them to upload images. The best approach is to use **Cloud Storage signed URLs**, which allow users to **upload files without requiring authentication** while enforcing **time-limited access**.

**Why Signed URLs?**

- **Allows users without a Google Account to upload files.**
- **Supports expiration time (e.g., 24 hours) for controlled access.**
- **Enforces security via cryptographic signing (HMAC-SHA256).**
- **Users do not need IAM roles or Cloud Identity accounts.**

**Implementation Steps:**

1. **Generate a signed URL** for each user using `gsutil` or `gcloud`:
  ```
  bashCopyEditgcloud storage sign-url gs://your-bucket-name --duration=24h
  ```
2. **Share the signed URL** with users.
3. **Users upload images via the signed URL** using `curl` or a simple web form.
4. **After 24 hours, the URL expires**, preventing further uploads.

✅ **Supporting Documentation:**

- **Using Signed URLs in Cloud Storage:**
  **https://cloud.google.com/storage/docs/access-control/signed-urls**

**Why Other Options Are Incorrect?**

**A. Have users upload images to Cloud Storage and protect the bucket with a password that expires after 24 hours.** ❌

- **Cloud Storage does not support password protection**—access is managed via IAM roles or signed URLs.
- **Requires users to have a Google Account, which some do not.**

✅ **Reference:**

- **https://cloud.google.com/storage/docs/access-control**

**C. Create an App Engine web application for users to upload images and configure App Engine to disable the application after 24 hours. Authenticate users via Cloud Identity.** ❌

- **Cloud Identity requires users to have a Google Account**, which **some do not**.
- **Disabling an App Engine app does not automatically revoke access to uploaded files.**

✅ **Reference:**

- **https://cloud.google.com/identity/docs/access-control**

**D. Create an App Engine web application where users can upload images for the next 24 hours. Authenticate users via Cloud Identity.** ❌

- **Requires users to have a Google Account**, which **some do not**.
- **More complex to implement than a signed URL solution.**

✅ **Reference:**

- **https://cloud.google.com/identity/docs**

**Conclusion:**

The best approach is **B. Have users upload images to Cloud Storage using a signed URL that expires after 24 hours**, because:
✔ **Allows access for users without a Google Account.**
✔ **Ensures secure, time-limited file uploads.**
✔ **Simpler and more efficient than setting up an App Engine application.**

📌 **Final Reference:**
**https://cloud.google.com/storage/docs/access-control/signed-urls**

**⚠️ Note:** Cloud ML Engine is now Vertex AI. The answer doesn't depend on it.

</details>

---

### Exam 1 · Q56

**Your web application must comply with the European Union’s General Data Protection Regulation (GDPR). As the technical architect, you are responsible for ensuring that the application meets GDPR requirements.**

**What should you do?**

- A. Ensure that your web application **only uses Google Cloud Platform’s native features and services**, as Google already holds various **certifications** and provides **pass-on compliance** when using native features.
- B. Enable the **relevant GDPR compliance setting** within the **Google Cloud Console** for each service used in your application.
- C. Include **Cloud Security Scanner** in your **test planning strategy** to identify potential **compliance gaps**.
- D. **Design the security architecture** of your web application in a way that aligns with **GDPR requirements**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Design the security architecture** of your web application in a way that aligns with **GDPR requirements**.

**Correct Answer:**

✅ **D. Design the security architecture of your web application in a way that aligns with GDPR requirements.**

**Explanation:**

As the **technical architect**, your responsibility is to **ensure that the application meets GDPR requirements** by **designing a security architecture that aligns with GDPR principles**. GDPR compliance is **not automatic**—organizations must implement specific **security, data protection, and access control measures**.

**Why Security Architecture is Key?**

- **GDPR mandates data security, privacy by design, and access control.**
- **Your architecture must include encryption, data residency controls, and audit logging.**
- **Google Cloud provides GDPR-compliant infrastructure, but organizations must configure security controls correctly.**

✅ **Key Considerations for a GDPR-Compliant Security Architecture:**

1. **Data Encryption:**
  - Use **Cloud KMS** to encrypt sensitive data.
  - Ensure **encryption at rest and in transit** using **TLS and AES-256**.
2. **Data Residency & Processing:**
  - Store **EU customer data in Google Cloud regions within the EU**.
  - Use **Cloud Storage and BigQuery regional locations** to ensure compliance.
3. **Identity & Access Management (IAM):**
  - Implement **least privilege access** using **Google Cloud IAM roles**.
  - Use **Cloud Identity-Aware Proxy (IAP)** for secure access to applications.
4. **Logging & Auditing:**
  - Enable **Cloud Audit Logs** to track data access and processing.
  - Use **Security Command Center** for monitoring security risks.
5. **Data Subject Rights & Deletion Requests:**
  - Implement **data retention policies**.
  - Enable **Cloud DLP API** to detect and remove Personally Identifiable Information (PII).

✅ **Supporting Documentation:**

- **Google Cloud GDPR Compliance Overview:**
  **https://cloud.google.com/security/compliance/gdpr**
- **Security Best Practices for GDPR:**
  **https://cloud.google.com/blog/topics/inside-google-cloud/google-cloud-gdpr-compliance**

**Why Other Options Are Incorrect?**

**A. Ensure that your web application only uses Google Cloud Platform’s native features and services, as Google already holds various certifications and provides pass-on compliance when using native features.** ❌

- **Google Cloud provides GDPR-compliant infrastructure**, but compliance is a **shared responsibility**.
- **Simply using Google Cloud does not automatically make your application GDPR-compliant**—you must **implement proper security controls**.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/gdpr**

**B. Enable the relevant GDPR compliance setting within the Google Cloud Console for each service used in your application.** ❌

- **There is no single "GDPR compliance setting" in Google Cloud Console**.
- **GDPR compliance is achieved through a combination of security measures**, not a toggle setting.

✅ **Reference:**

- **https://cloud.google.com/security/compliance/gdpr**

**C. Include Cloud Security Scanner in your test planning strategy to identify potential compliance gaps.** ❌

- **Cloud Security Scanner helps identify vulnerabilities in web applications** but **does not cover GDPR compliance requirements** such as **data encryption, data subject rights, and retention policies**.
- **It is useful for security best practices, but not a standalone solution for GDPR compliance**.

✅ **Reference:**

- **https://cloud.google.com/security-command-center/docs/concepts-security-scanner**

**Conclusion:**

The best approach is **D. Design the security architecture of your web application in a way that aligns with GDPR requirements**, because:
✔ **GDPR compliance requires a well-architected security design**.
✔ **You must implement encryption, access controls, logging, and data retention policies**.
✔ **Google Cloud provides GDPR-compliant infrastructure, but you must configure and use it correctly**.

📌 **Final Reference:**
**https://cloud.google.com/security/compliance/gdpr**

</details>

---

### Exam 2 · Q2

**You need to upload files from your on-premises environment to Cloud Storage while ensuring that the files are encrypted using customer-supplied encryption keys (CSEK).**

**What should you do?**

- A. Specify the **encryption key** in a **.boto configuration file** and use **gsutil** to upload the files.
- B. Configure the **encryption key** using **gcloud config**, then use **gsutil** to upload the files to the bucket.
- C. Use **gsutil** to upload the files and provide the encryption key using the `--encryption-key` flag.
- D. Use **gsutil** to create a bucket with the `--encryption-key` flag, then upload the files to that bucket using **gsutil**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Specify the **encryption key** in a **.boto configuration file** and use **gsutil** to upload the files.

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

</details>

---

### Exam 2 · Q5

**Your company wants to start using Google Cloud resources while retaining its on-premises Active Directory (AD) domain controller for identity management.**

**What should you do?**

- A. Use the **Admin Directory API** to authenticate against the **Active Directory domain controller**.
- B. Use **Google Cloud Directory Sync** to **synchronize Active Directory usernames** with **Cloud Identities** and configure **SAML SSO**.
- C. Use **Cloud Identity-Aware Proxy (IAP)** and configure it to use the **on-premises Active Directory domain controller** as an **identity provider**.
- D. Use **Compute Engine** to create an **Active Directory (AD) domain controller replica** in Google Cloud, and sync it with the on-premises AD using **Google Cloud Directory Sync**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use **Google Cloud Directory Sync** to **synchronize Active Directory usernames** with **Cloud Identities** and configure **SAML SSO**.

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

</details>

---

### Exam 2 · Q13

**Your company processes batches of sensitive transaction data by pushing them from application server VMs to Cloud Pub/Sub for further processing and storage. You need to ensure that your application authenticates securely to the required Google Cloud services following Google-recommended best practices.**

**What is the best approach?**

- A. Ensure that **VM service accounts** have the appropriate **Cloud Pub/Sub IAM roles** assigned.
- B. Ensure that **VM service accounts do not have direct access** to Cloud Pub/Sub and use **VM access scopes** to assign the appropriate **Cloud Pub/Sub IAM roles**.
- C. Generate an **OAuth2 access token** for Cloud Pub/Sub, **encrypt it**, and store it in **Cloud Storage** for access from each VM.
- D. Create a **gateway to Cloud Pub/Sub** using a **Cloud Function** and grant the **Cloud Function service account** the required **Cloud Pub/Sub IAM roles**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Ensure that **VM service accounts** have the appropriate **Cloud Pub/Sub IAM roles** assigned.

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

</details>

---

### Exam 2 · Q18

**Your company operates nationally and plans to use Google Cloud Platform (GCP) for multiple batch workloads, including some that are not time-sensitive. You also need to ensure that all GCP services used are HIPAA-certified while managing service costs efficiently.**

**How should you design your solution following Google best practices?**

- A. **Use preemptible VMs** to reduce costs and **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.
- B. **Use preemptible VMs** to reduce costs, **disable** and then **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.
- C. **Use standard VMs** in the **same region** to reduce costs and **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.
- D. **Use standard VMs** in the **same region** to reduce costs, **disable** and then **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Use preemptible VMs** to reduce costs and **discontinue all GCP services and APIs** that are **not HIPAA-compliant**.

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

</details>

---

### Exam 2 · Q22

**Your company collects all web traffic data using Google Analytics 360 and stores it in BigQuery. Each country has its own dataset, and each dataset contains multiple tables. You need to ensure that analysts from each country can only view and query the data relevant to their respective countries.**

**How should you configure access rights?**

- A. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery jobUser IAM role**. Share the appropriate **dataset** with **view access** for each respective **analyst country-group**.
- B. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery jobUser IAM role**. Share the appropriate **tables** with **view access** for each respective **analyst country-group**.
- C. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery dataViewer IAM role**. Share the appropriate **dataset** with **view access** for each respective **analyst country-group**.
- D. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery dataViewer IAM role**. Share the appropriate **table** with **view access** for each respective **analyst country-group**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a **group per country** and add analysts to their respective country-groups. Create a single group `all_analysts` and add all **country-groups** as members. Grant the `all_analysts` group the **BigQuery jobUser IAM role**. Share the appropriate **dataset** with **view access** for each respective **analyst country-group**.

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

</details>

---

### Exam 2 · Q44

You are working for a **sports association** with **members aged 8 to 30**. The organization **collects health-related data**, including **sustained injuries**, and stores it in **BigQuery**.

Legislation requires that **personal health data must be deleted upon request** of the individual. You need to **design a solution** that allows for compliance with these requests.

What should you do?

- A. Use a **unique identifier** for each individual. When a **deletion request** is received, **delete all rows** in **BigQuery** that contain this identifier.
- B. Before storing new data in **BigQuery**, process it through the **Data Loss Prevention (DLP) API** to identify personal information. Save the results in **Data Catalog**, and upon a **deletion request**, query **Data Catalog** to identify and remove the relevant personal data.
- C. Create a **BigQuery view** over the original data table. Upon a **deletion request**, modify the view to **exclude rows** related to the subject while keeping the original data intact. Use this view for all analysis tasks.
- D. Use a **unique identifier** for each individual. Upon a **deletion request**, replace the identifier with a **salted SHA256 hash** instead of deleting the data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use a **unique identifier** for each individual. When a **deletion request** is received, **delete all rows** in **BigQuery** that contain this identifier.

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

</details>

---

### Exam 2 · Q47

Your organization has decided to **restrict the use of external IP addresses** on Compute Engine instances, allowing **only approved instances** to have external access. You need to **enforce this policy** across **all Virtual Private Clouds (VPCs)**.

What should you do?

- A. **Remove the default route** on all **VPCs** and move all **approved instances** into a **new subnet** that has a **default route to an internet gateway**.
- B. **Create a new VPC** in **custom mode**, then create a **new subnet** for the **approved instances**, and set a **default route to the internet gateway** for this subnet.
- C. **Implement a Cloud NAT solution** to **eliminate the need for external IP addresses** entirely.
- D. **Set an Organization Policy** with a **constraint on** `constraints/compute.vmExternalIpAccess`, and list the **approved instances** in the **allowedValues list**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. **Set an Organization Policy** with a **constraint on** `constraints/compute.vmExternalIpAccess`, and list the **approved instances** in the **allowedValues list**.

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

</details>

---

### Exam 2 · Q49

Your company stores **sensitive data** in **Cloud Storage buckets**, and **data analysts** have **IAM permissions** to **read** from these buckets. You need to **prevent analysts from accessing the data from outside the office network** while maintaining access from within the office.

What should you do?

- A. **Create a VPC Service Controls perimeter** that includes the **projects containing the Cloud Storage buckets**. **Define an access level** that restricts access based on the **CIDR range of the office network**.
- B. **Create a firewall rule** for all **Compute Engine instances** in the **VPC network**. **Use the office network's CIDR range** as the **source range** in the firewall rule.
- C. **Create a Cloud Function** to **remove IAM permissions** from the buckets, and another **Cloud Function** to **restore IAM permissions**. **Use Cloud Scheduler** to automatically **add permissions at the start of business hours** and **remove them at the end of business hours**.
- D. **Set up a Cloud VPN connection** to the **office network**. **Enable Private Google Access** for **on-premises hosts** to restrict access to **Cloud Storage** through the VPN.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Create a VPC Service Controls perimeter** that includes the **projects containing the Cloud Storage buckets**. **Define an access level** that restricts access based on the **CIDR range of the office network**.

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

</details>

---

### Exam 2 · Q58

You are working at a **financial institution** that stores **mortgage loan approval documents** on **Cloud Storage**.

- **Any changes** to these documents must be **uploaded as separate approval files**.
- You need to ensure that **documents cannot be deleted or overwritten** for the **next 5 years**.

What should you do?

- A. **Set a retention policy** on the **Cloud Storage bucket** for **5 years** and **lock the retention policy** to prevent modifications.
- B. **Create the bucket** with **uniform bucket-level access** and grant a **service account** the **Object Writer role**. Use this service account to **upload new files**.
- C. **Use a customer-managed encryption key (CMEK)** for the **bucket encryption** and **rotate the key** after **5 years**.
- D. **Create the bucket** with **fine-grained access control** and grant a **service account** the **Object Writer role**. Use this service account to **upload new files**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. **Set a retention policy** on the **Cloud Storage bucket** for **5 years** and **lock the retention policy** to prevent modifications.

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

</details>

---

### Exam 3 · Q4

Your organization has **two separate teams**: a **networking team** and an **application development team**. The development team deploys applications on **Compute Engine instances** that contain **confidential data**. They require **admin-level access** to manage Compute Engine resources.

Meanwhile, the company enforces a policy where **all networking components** must be controlled by the **networking team**. The development team wants to **ensure that the networking team cannot access sensitive instance data**.

How should you design the Google Cloud environment to meet these requirements?

- A. Create a project with its own **standalone VPC** and grant the **Network Admin** role to the networking team. Create a second project with another **standalone VPC** and grant the **Compute Admin** role to the development team. Connect both VPCs using **Cloud VPN**.
- B. Create a single project with a **standalone VPC**, and assign the **Network Admin** role to the networking team. In the same project, assign the **Compute Admin** role to the development team.
- C. Create a host project with a **Shared VPC** and grant the **Network Admin** role to the networking team. Create a separate **service project** without its own VPC, attach it to the Shared VPC, and grant the **Compute Admin** role to the development team.
- D. Create a project with a **standalone VPC** and assign the **Network Admin** role to the networking team. Create another project with a separate **standalone VPC** and assign the **Compute Admin** role to the development team. Connect the two VPCs using **VPC Peering**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a host project with a **Shared VPC** and grant the **Network Admin** role to the networking team. Create a separate **service project** without its own VPC, attach it to the Shared VPC, and grant the **Compute Admin** role to the development team.

✅ **Correct Answer: C. Create a host project with a Shared VPC and grant the Network Admin role to the networking team. Create a separate service project without its own VPC, attach it to the Shared VPC, and grant the Compute Admin role to the development team.**

**Scenario Summary:**

- Two teams:
  - **Networking Team**: manages networking resources only.
  - **Application Development Team**: manages **Compute Engine instances** that handle **confidential data**.
- **Development team needs admin access** to Compute Engine but **must not** have control over or visibility into networking configuration.
- **Networking team should not have access to instance data.**

✅ **Why Option C is Correct:**

Key Design Features:

1. **Shared VPC Architecture**:
  - **Host Project**: Owned/managed by the **networking team**, which **creates and controls** the VPC, subnets, firewall rules, etc.
  - **Service Project**: Owned/managed by the **development team**. It contains the **Compute Engine resources (VMs)** that **use the networking resources** from the host project.
2. **IAM Role Separation**:
  - **Networking Team**:
    - Granted **Network Admin** role on the **host project**.
    - Cannot access the VMs or their data in the service project.
  - **Development Team**:
    - Granted **Compute Admin** role on the **service project**.
    - Can manage VMs but **cannot modify network configuration**, which is owned by the host project.
3. **Security Boundary**:
  - This setup enforces **least privilege access** and **clear boundaries** between network and compute responsibilities.
  - Ensures that **networking team has no access** to confidential data stored on instances.

Supporting Documentation:

- Shared VPC Overview
  Shared VPC allows organization administrators to configure and centrally manage VPCs while allowing other projects to provision resources in shared networks.
- IAM Roles and Permissions for Shared VPC
  Projects attached to a Shared VPC host retain administrative independence and resource isolation.

❌ **Why Other Options Are Incorrect:**

**A. Two standalone VPCs with Cloud VPN**

- **Not efficient or secure for internal teams** within the same organization.
- **Cloud VPN** adds **unnecessary cost and complexity** for intra-org connectivity.
- Does not provide **centralized network control**, and VPCs are not centrally managed.
- Lacks **fine-grained IAM controls** across project boundaries like Shared VPC.

**B. Single project with shared roles**

- **Both teams operate in the same project** – no strong boundary between **networking and compute**.
- Even with IAM separation, the development team could potentially access networking components, **violating organizational policy**.

**D. VPC Peering between projects**

- Similar issue as A: introduces **unnecessary peering complexity**.
- VPC peering **does not support transitive routing** and doesn’t centralize control.
- **Network Admin** in one project has **no visibility or control** over another project's VPC.
- Lacks the **centralized governance** offered by Shared VPC.

✅ **Final Recommendation:**

**Use Shared VPC** with:

- **Host project**: managed by the **networking team**.
- **Service project**: used by the **development team**, isolated in terms of data.
- Role-based access ensures **security, scalability, and operational efficiency**.

Hint - [https://cloud.google.com/vpc/docs/shared-vpc](https://cloud.google.com/vpc/docs/shared-vpc)

</details>

---

### Exam 3 · Q6

Your organization routes all Google Cloud logs to **Cloud Logging**. The **security team** needs to **actively monitor these logs** and must be able to **respond quickly to anomalies**, such as **unauthorized firewall modifications** or a **potential server compromise**. You want to implement a solution that aligns with **Google-recommended best practices**.

What should you do?

- A. Use **Cloud Scheduler** to run a **cron job** every minute that queries the logs for specific security-related events.
- B. **Export logs to BigQuery** and run scheduled **queries** to analyze them for anomalies.
- C. **Export logs to a Pub/Sub topic** and trigger a **Cloud Function** to process and respond to relevant log entries.
- D. **Export logs to a Cloud Storage bucket** and trigger a **Cloud Run** service when specific log events occur.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. **Export logs to a Pub/Sub topic** and trigger a **Cloud Function** to process and respond to relevant log entries.

✅ **Correct Answer: C. Export logs to a Pub/Sub topic and trigger a Cloud Function to process and respond to relevant log entries.**

**Scenario Summary:**

- All logs are routed to **Cloud Logging**.
- The **Security team needs to actively monitor logs** for real-time security anomalies (e.g., firewall rule changes, server compromise).
- They must be able to **respond quickly**.
- Solution must follow **Google Cloud recommended best practices**.

✅ **Why Option C is Correct:**

**Real-time Monitoring via Cloud Logging + Pub/Sub + Cloud Functions:**

- **Cloud Logging** can **stream log entries to a Pub/Sub topic** using **log sinks**.
- **Pub/Sub** acts as a real-time delivery channel.
- **Cloud Functions** can be triggered on each relevant log message to:
  - Parse the entry,
  - Detect anomalies (e.g., firewall change event),
  - Take action (e.g., alert security team, revoke access, etc.).

This is a **real-time, serverless, event-driven architecture**, aligned with Google Cloud’s **Security Command Center and logging best practices**.

**Official Documentation:**

- Routing Logs with Sinks
- Real-time log monitoring with Pub/Sub
- Trigger Cloud Functions from Pub/Sub

*"To receive notifications about changes or anomalies in your logs in real time, configure a sink to route logs to Pub/Sub, and set up a Cloud Function that processes and responds to those events."*
— *Google Cloud Logging Best Practices*

❌ **Why Other Options Are Incorrect:**

**A. Use Cloud Scheduler to run a cron job every minute that queries the logs for specific security-related events**

- **Polling-based**, not **event-driven** → introduces latency.
- Doesn’t scale well or respond **immediately** to critical events.
- Not aligned with **real-time monitoring** best practices.

**Docs:** Cloud Scheduler

Not intended for real-time log processing.

**B. Export logs to BigQuery and run scheduled queries to analyze them for anomalies**

- Useful for **historical analysis and dashboards**, but **not real-time detection**.
- Scheduled queries often run **every few hours or once a day**.
- **Too slow** for high-priority alerts (like firewall rule modifications).

**Docs:** Log Export to BigQuery

For analysis, not live incident detection.

**D. Export logs to a Cloud Storage bucket and trigger a Cloud Run service when specific log events occur**

- **Cloud Storage log exports** are batch-based and intended for **archival** or **batch analysis**.
- Cannot **trigger real-time actions** like Cloud Pub/Sub.
- Cloud Run doesn’t have native support for Cloud Storage triggers (would require additional setup via Eventarc).

**Docs:** Log Export to Cloud Storage

✅ **Final Recommendation:**

**Use Pub/Sub log sinks and trigger Cloud Functions** to process and respond to security anomalies in real time.

This approach offers:

- **Real-time detection**
- **Serverless and scalable architecture**
- **Fast response to security events**
- **Google-recommended design**

Hint - [https://cloud.google.com/blog/products/management-tools/automate-your-response-to-a-cloud-logging-event](https://cloud.google.com/blog/products/management-tools/automate-your-response-to-a-cloud-logging-event)

</details>

---

### Exam 3 · Q7

You have launched several **Compute Engine instances** within your Google Cloud environment. Due to **security policies**, these instances **must not have public IP addresses**. There is **no existing VPN connection** between your corporate office and Google Cloud. However, you need to **SSH into one specific instance** without breaching the defined security constraints.

What is the most appropriate approach?

- A. Set up **Cloud NAT** for the subnet containing the instance, and initiate an **SSH connection to the Cloud NAT IP address** to access the instance.
- B. Add all instances to an **unmanaged instance group**, configure **TCP Proxy Load Balancing** with the group as the backend, and connect to the instance using the **TCP proxy IP address**.
- C. Enable **Identity-Aware Proxy (IAP)** for the instance, ensure you have the **IAP-secured Tunnel User** role, and use the **gcloud CLI** to SSH into the instance.
- D. Deploy a **bastion host** in the same VPC network, connect to it via SSH from your office, and then use it to access the **target instance via internal SSH**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Enable **Identity-Aware Proxy (IAP)** for the instance, ensure you have the **IAP-secured Tunnel User** role, and use the **gcloud CLI** to SSH into the instance.

✅ **Correct Answer: C. Enable Identity-Aware Proxy (IAP) for the instance, ensure you have the IAP-secured Tunnel User role, and use the gcloud CLI to SSH into the instance.**

**Scenario Summary:**

- Compute Engine instances **must not have public IP addresses** (security policy).
- **No VPN** or interconnect with on-prem network.
- You need to SSH into one instance **without violating security constraints**.

✅ **Why Option C is Correct:**

**Identity-Aware Proxy (IAP) for TCP forwarding**:

- **IAP** allows SSH access to internal (no public IP) instances **without exposing them to the internet**.
- SSH tunnels are initiated through a **Google-managed proxy**, allowing you to connect to the VM **via the gcloud CLI** using **IAP TCP forwarding**.
- Requires assigning the `roles/iap.tunnelResourceAccessor` (**IAP-secured Tunnel User**) role and setting up proper **OS Login or SSH key access**.

**Advantages:**

- **No public IP** is needed.
- No need for VPN or bastion host.
- Fully compliant with **zero-trust and security-first architectures**.

**Official Documentation:**

- IAP for TCP forwarding (SSH/RDP)
- Connect to VMs that do not have external IP addresses

*"If a VM instance does not have a public IP address, you can still connect to it by using Identity-Aware Proxy (IAP) TCP forwarding."*

❌ **Why Other Options Are Incorrect:**

**A. Set up Cloud NAT and SSH to the Cloud NAT IP**

- **Cloud NAT** is **only for egress** — it allows **VMs without public IPs** to initiate outbound internet traffic.
- It **does not support inbound connections**, including SSH.

**Docs:**

- Cloud NAT overview

*"Cloud NAT does not support incoming connections initiated from outside of your VPC network."*

**B. Configure TCP Proxy Load Balancer with an unmanaged instance group**

- **TCP Proxy Load Balancer** is meant for **TCP-based applications**, not SSH.
- Requires a **backend service** and health checks — not intended for one-off admin access like SSH.
- **Security risks**: exposes a public IP to a group of instances.

**Docs:**

- TCP Proxy Load Balancing

**D. Deploy a bastion host in the same VPC**

- Technically **valid**, but not the most **appropriate** solution here:
  - Requires provisioning a **new public-facing VM**, increasing **attack surface**.
  - Adds **operational overhead** (patching, monitoring the bastion).
  - Violates the policy of **no public IPs**, unless the bastion is specially exempted.

**Docs:**

- Best practices for bastion hosts

✅ **Final Recommendation:**

**Use Identity-Aware Proxy (IAP)** for secure, **zero-public-IP SSH access** to internal VM instances — without a VPN or bastion host.

</details>

---

### Exam 3 · Q8

Your organization uses **Google Cloud** and has set up two folders under its **Organization node**: one for the **Finance** department and another for the **Retail** team. The **development team members** are part of a **Google Group**, and this group has been granted the **Project Owner role at the Organization level**.

You want to ensure that **developers are restricted from creating resources** in any project located under the **Finance folder**.

What is the best way to enforce this restriction?

- A. Grant the development team group the **Project Viewer** role on the Finance folder and the **Project Owner** role on the Retail folder.
- B. Grant the development team group **only the Project Viewer** role on the Finance folder.
- C. Remove the Project Owner role for the development team group from the Organization level, and assign them the **Project Owner** role only on the Retail folder.
- D. Assign the development team group the **Project Owner** role only on the Retail folder.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Remove the Project Owner role for the development team group from the Organization level, and assign them the **Project Owner** role only on the Retail folder.

✅ **Correct Answer: C. Remove the Project Owner role for the development team group from the Organization level, and assign them the Project Owner role only on the Retail folder.**

**Scenario Summary:**

- Organization structure has **two folders** under the Organization node:
  - **Finance folder**
  - **Retail folder**
- A **Google Group (Dev Team)** has the **Project Owner** role **at the Organization level**.
- You need to **restrict developers from creating resources** in any project under the **Finance folder**.

✅ **Why Option C is Correct:**

- **Roles assigned at the Organization level** are inherited by all resources under the org, including **folders and projects**.
- So, if the **Project Owner role is granted at the Organization level**, the development group has **full control** over **all folders/projects**, including **Finance**, which violates the requirement.
- The correct action is to **remove that Organization-level role**, and instead **grant more restrictive access**:
  - Only assign **Project Owner** on the **Retail folder**.
  - No permissions assigned on the **Finance folder**, so developers **cannot create or manage resources** there.

**Google Documentation:**

- Understanding IAM hierarchy and inheritance
  "Permissions granted at higher levels of the resource hierarchy (like the organization) are inherited by lower levels (like folders and projects)."
- Best practices for using folders and resource hierarchies
  "Use folders to group resources that share the same access control policies."

❌ **Why Other Options Are Incorrect:**

**A. Grant the development team group the Project Viewer role on the Finance folder and the Project Owner role on the Retail folder**

- Assigning **Project Viewer** on the Finance folder **does not override** the **Project Owner** permission they already have from the **Organization level**.
- Because of IAM **inheritance**, they would still retain **full access** to the Finance folder unless the higher-level permission is removed.

**B. Grant the development team group only the Project Viewer role on the Finance folder**

- Similar issue as A.
- The group **already has Project Owner at the Organization level**, which **supersedes** the Viewer role.
- They’ll still have **full control** over Finance folder resources unless the higher-level role is revoked.

**D. Assign the development team group the Project Owner role only on the Retail folder**

- This **does not fix the issue** unless the existing **Organization-level Project Owner role is explicitly removed**.
- The key problem is the **broad Organization-level role**, which must be removed to limit access.

✅ **Final Recommendation:**

To ensure developers **cannot manage or create resources** under the **Finance folder**, you must:

- **Remove the Project Owner role from the Organization level**, and
- **Assign the role only at the Retail folder level**.

</details>

---

### Exam 3 · Q18

You are managing your organization's **Google Cloud environment**, where **multiple departments** require access to their own set of projects. Within each department, **team members will share the same responsibilities** across their projects. You want to **minimize administrative overhead** while maintaining a **clear view of IAM permissions**, especially as projects are created and decommissioned over time. You aim to follow **Google-recommended best practices**.

What should you do?

- A. **Individually assign IAM permissions** to all department members for each of their respective projects.
- B. **Create a Google Group** for each department and add relevant members to their group. Then, create a **folder per department**, assign the required IAM roles to the group **at the folder level**, and place department projects under the appropriate folder.
- C. Create a **folder per department** and assign the required IAM permissions **directly to the individual department members** at the folder level. Add each department's projects under its folder.
- D. Create a **Google Group** for each department and add department members. Then, assign IAM permissions **to the group on a per-project basis** for each of their respective projects.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. **Create a Google Group** for each department and add relevant members to their group. Then, create a **folder per department**, assign the required IAM roles to the group **at the folder level**, and place department projects under the appropriate folder.

✅ **Correct Answer: B. Create a Google Group for each department and add relevant members to their group. Then, create a folder per department, assign the required IAM roles to the group at the folder level, and place department projects under the appropriate folder.**

**Scenario Overview:**

- Multiple departments, each managing their own projects in **Google Cloud**.
- **Department members share common roles** across their projects.
- Projects are **created and decommissioned regularly**.
- Goal:
  - **Minimize administrative overhead**
  - **Maintain clear IAM visibility**
  - **Align with Google Cloud best practices**

✅ **Why Option B is Correct:**

**Google Cloud Best Practices Alignment:**

1. **Use Google Groups for IAM:**
  - Groups allow centralized management of access.
  - Adding/removing members doesn’t require changes to IAM policies.
  - Supports **auditability** and **access consistency**.
2. **Use Folders to Structure Resources:**
  - Organize resources by **department, team, or business unit**.
  - **IAM roles inherited** from the folder to all projects under it.
  - When a **new project is created under a folder**, **IAM roles are automatically applied**, minimizing manual IAM configuration.
3. **Assign IAM at the Folder Level:**
  - Reduces redundancy (you avoid repetitive per-project permissions).
  - Easier to **audit and manage** access as a single policy controls multiple projects.

**Documentation Reference:**

- Google Cloud Resource Hierarchy
- Best practices for using folders

"You can assign IAM roles at the folder level to apply to all projects within the folder, simplifying permission management."

- Best Practices for IAM

"Use Google Groups to manage access instead of adding users individually."

❌ **Why Other Options Are Incorrect:**

**A. Individually assign IAM permissions per project**

- **High maintenance** and error-prone.
- Difficult to manage as the number of projects and users grows.
- **Not scalable** and hard to audit.

**C. Assign IAM directly to individuals at folder level**

- Better than project-level roles but still **not scalable**.
- You’d need to **update IAM policies** every time a team member joins or leaves.
- Violates best practice of using **Google Groups** for access management.

**D. Use groups but assign IAM per project**

- Using groups is good, but assigning IAM **per project** increases operational overhead.
- Every new project needs a **manual IAM configuration**, which defeats the goal of **minimal administration**.

✅ **Final Recommendation:**

- Create a **Google Group per department**
- Create a **folder per department**
- Assign IAM roles **at the folder level to the group**
- Add all related projects **under the folder**

This provides a **scalable**, **auditable**, and **low-maintenance** IAM strategy aligned with **Google Cloud best practices**.

</details>

---

### Exam 3 · Q19

Your company has an application deployed as a **Kubernetes Deployment** running in **Google Kubernetes Engine (GKE)**. You maintain **separate clusters for development, staging, and production** environments.

Recently, you discovered that the team is able to **deploy Docker images directly to the production cluster** without first deploying and testing them in the **development** and **staging** environments.

While you want to maintain the team’s **deployment autonomy**, you also want to **enforce proper promotion flow** to prevent this issue from recurring. You are looking for a **Google Cloud-native solution** that can be implemented **quickly with minimal operational overhead**.

What should you do?

- A. Set up a **Kubernetes lifecycle hook** to block the container from starting unless it is approved for use in the specific environment.
- B. Enforce a **company policy** requiring that images must be tested in lower environments before deployment to production.
- C. Use **Binary Authorization policies** for the development, staging, and production clusters, and configure **attestations** in the CI pipeline.
- D. Develop a **Kubernetes admission controller** that blocks containers from starting unless they have been approved for the respective environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use **Binary Authorization policies** for the development, staging, and production clusters, and configure **attestations** in the CI pipeline.

✅ **Correct Answer: C. Use Binary Authorization policies for the development, staging, and production clusters, and configure attestations in the CI pipeline.**

**Scenario Summary:**

- Application runs on **GKE** using **Kubernetes Deployments**.
- You have **separate clusters** for **dev**, **staging**, and **prod**.
- Issue: teams can **bypass dev/staging** and **deploy directly to production**.
- Goal: enforce a **promotion flow** (dev → staging → prod).
- You want a **Google Cloud-native solution** with **minimal operational overhead** and **retained deployment autonomy**.

✅ **Why Option C is Correct:**

**Binary Authorization:**

- **Binary Authorization** is a **Google Cloud-native** security feature that:
  - **Prevents unauthorized container images** from being deployed to GKE.
  - Enforces **deploy-time policies** using **attestations** and **signers**.
- You can define **different policies per environment** (e.g., dev, staging, prod).
- **Attestations** can be generated automatically in the **CI/CD pipeline**, confirming that:
  - The image passed required tests,
  - It was promoted through dev and staging before reaching production.

**How it Works:**

1. CI builds image and runs tests.
2. If tests pass in **dev**, the CI system generates an **attestation** (a cryptographically signed statement).
3. Staging CI pipeline does the same.
4. Production Binary Authorization policy is configured to **require attestations** from both dev and staging environments before allowing deployment.

**Benefits:**

- Enforces **promotion flow** without manual intervention.
- **Prevents unauthorized deployments** to production.
- Fully **integrated with GKE and Cloud Build**.
- Minimal operational overhead once configured.

**Documentation References:**

- Binary Authorization Overview
- Set up Binary Authorization with GKE

❌ **Why Other Options Are Incorrect:**

**A. Kubernetes lifecycle hook to block container start**

- Lifecycle hooks (**e.g., preStart**) are meant for **application-level initialization**, not for **enforcing deployment policies**.
- They **run inside the pod**, which is **too late** — the image is already deployed and running.
- Not intended for security enforcement or environment validation.

**B. Company policy requiring testing in lower environments**

- While governance policies are important, this is a **manual, unenforceable measure**.
- **No technical control** — still allows bypassing the process.
- Not a reliable solution to prevent production misuse.

**D. Custom Kubernetes admission controller**

- Admission controllers can enforce policies, but writing and maintaining a **custom controller** is **complex and high overhead**.
- You'd have to **build, deploy, and manage** the controller yourself.
- Not a **quick or Google Cloud-native** solution.

✅ **Final Recommendation:**

**Use Binary Authorization** to enforce image promotion flow across **dev → staging → prod** by requiring **attestations** before allowing deployments.

This is the **most secure**, **scalable**, and **Google Cloud-aligned** solution with **minimal operational burden.**

Ref - [https://cloud.google.com/binary-authorization/docs/overview#policy_model](https://cloud.google.com/binary-authorization/docs/overview#policy_model)

</details>

---

### Exam 3 · Q22

At CloudLogic Solutions, you're designing a data warehouse solution on Google Cloud. The plan involves storing sensitive information in BigQuery. Your organization enforces a policy requiring that encryption keys must be generated externally and not within Google Cloud.

**Which solution should you implement to meet this requirement?**

- A. Generate a new key in Cloud Key Management Service (Cloud KMS). Store all data in Cloud Storage using the **customer-managed key** option, selecting the newly created key. Then, use a Dataflow pipeline to decrypt the data and load it into a new BigQuery dataset.
- B. Generate a new key in Cloud KMS. Create a new dataset in BigQuery using the **customer-managed key** option and select the generated key.
- C. Import an externally generated key into Cloud KMS. Store all data in Cloud Storage using the **customer-managed key** option and select the imported key. Then, use a Dataflow pipeline to decrypt the data and load it into BigQuery.
- D. Import an externally generated key into Cloud KMS. Create a BigQuery dataset using the **customer-supplied key** option and choose the imported key.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Import an externally generated key into Cloud KMS. Store all data in Cloud Storage using the **customer-managed key** option and select the imported key. Then, use a Dataflow pipeline to decrypt the data and load it into BigQuery.

**The correct option is:**
**C. Import an externally generated key into Cloud KMS. Store all data in Cloud Storage using the customer-managed key option and select the imported key. Then, use a Dataflow pipeline to decrypt the data and load it into BigQuery.**

Justification for Correct Option (C):

- The key requirement is that **encryption keys must be generated externally** — outside of Google Cloud.
- Google Cloud allows importing externally generated keys into **Cloud KMS**, using a process called **External Key Management (EKM)** or **imported keys** for **Cloud KMS**.
- Once the key is imported into **Cloud KMS**, it becomes a **customer-managed key (CMEK)**, which can be used for services like Cloud Storage.
- BigQuery does **not** support customer-supplied keys (CSEK), so option D is impossible. Among the options given, C is the only one that uses an externally generated key:
  - You **store encrypted data in Cloud Storage** using the externally imported key.
  - Then, use **Dataflow to decrypt** the data with the imported key and load it into BigQuery.
  - BigQuery will then use its own encryption (default or CMEK if acceptable), but you’ve ensured the sensitive data **was encrypted with an externally generated key before entering BigQuery**.

**Reference:**

- Importing external keys into Cloud KMS
- BigQuery CMEK limitations
- Dataflow and CMEK

**Why Other Options Are Incorrect:**

A.

Generate a new key in Cloud KMS...

- **Incorrect** because it states the key is **generated in Cloud KMS**, violating the requirement that keys must be **generated externally**.

B.

Generate a new key in Cloud KMS and use it as a CMEK for BigQuery...

- **Incorrect** for the same reason as above — the key is **generated within Google Cloud**, not externally.
- BigQuery has no CSEK option at all.

D.

Import an externally generated key and use it as a customer-supplied key in BigQuery...

- **Incorrect** because **BigQuery does not support Customer-Supplied Encryption Keys (CSEK)**.
- BigQuery only supports Google-managed keys or CMEK.

**Reference:**

- BigQuery does **not support CSEK**: [https://cloud.google.com/bigquery/docs/customer-managed-encryption#limitations](https://cloud.google.com/bigquery/docs/customer-managed-encryption#limitations)

**Final Answer: C**

This is the only solution that:

- Uses **externally generated keys**.
- **Encrypts sensitive data before it enters BigQuery**.
- Leverages **Cloud Storage + Dataflow** to enforce encryption control.

**⚠️ Note:** An imported key is an ordinary Cloud KMS key, and BigQuery CMEK accepts any Cloud KMS key, so in practice you would import the key and set it as the dataset's CMEK directly. That option isn't offered here, so C remains the best of the four.

</details>

---

### Exam 3 · Q23

At DataSecure Corp., sensitive information is stored in a Google Cloud Storage bucket. Due to regulatory compliance requirements, the organization must be able to **rotate the encryption key** used to protect the data stored in that bucket. The data will later be processed using Google Cloud Dataproc. You aim to follow **Google-recommended best practices for security**.

**What should you do to meet these requirements?**

- A. Create a key using **Cloud Key Management Service (Cloud KMS)**. Use the `encrypt` method of Cloud KMS to manually encrypt the data before uploading it.
- B. Create a key using **Cloud Key Management Service (Cloud KMS)**. Assign this key as the **default encryption key** for the Cloud Storage bucket.
- C. Generate a **GPG key pair**. Encrypt the data using this GPG key, then upload the encrypted data to the Cloud Storage bucket.
- D. Generate a **custom AES-256 encryption key**. Encrypt the data in the Cloud Storage bucket using the **customer-supplied encryption key (CSEK)** feature.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a key using **Cloud Key Management Service (Cloud KMS)**. Assign this key as the **default encryption key** for the Cloud Storage bucket.

The correct answer is:
**B. Create a key using Cloud Key Management Service (Cloud KMS). Assign this key as the default encryption key for the Cloud Storage bucket.**

Justification for Correct Option (B):

- **Cloud KMS** allows you to create **Customer-Managed Encryption Keys (CMEK)** that can be used with Google Cloud Storage.
- Assigning a **CMEK as the default encryption key** for a bucket ensures that all newly uploaded objects are automatically encrypted using this key.
- **Key rotation** is supported and **managed via Cloud KMS**, making it easier to meet **regulatory compliance** and **security best practices**.
- This approach is **fully integrated with Google Cloud services like Dataproc**, so when data is accessed or processed, the CMEK-protected data can be decrypted securely.

**Google-recommended best practices** include using **CMEK** over CSEK or manual encryption for production workloads requiring compliance and auditability.

**Official Documentation:**

- Using customer-managed encryption keys (CMEK) with Cloud Storage
- Key rotation with Cloud KMS

**Why Other Options Are Incorrect:**

A.

Create a key using Cloud KMS. Use the encrypt method of Cloud KMS to manually encrypt the data before uploading it.

- This involves **manual encryption**, which is **not scalable** and **not recommended** for production or compliance-heavy environments.
- It complicates integration with other GCP services like Dataproc.
- Also lacks native support for **automatic key rotation and access management**.

**Reference:**

- Manual encryption is possible but not recommended for managing encrypted data at scale:
  [https://cloud.google.com/kms/docs/encrypt-decrypt](https://cloud.google.com/kms/docs/encrypt-decrypt)

C.

Generate a GPG key pair. Encrypt the data using this GPG key, then upload the encrypted data to the Cloud Storage bucket.

- GPG keys are **not natively integrated** with Google Cloud services.
- **Manual encryption** with GPG makes **key rotation, auditability, and access control** more complex and error-prone.
- This approach **doesn’t meet Google’s best practices** for cloud-native data protection.

D.

Generate a custom AES-256 encryption key. Encrypt the data using the CSEK feature.

- **Customer-Supplied Encryption Keys (CSEK)** are supported but **not recommended** for most use cases.
- CSEK does **not support automatic key rotation**, and you are fully responsible for key lifecycle and availability.
- **Google does not retain** a copy of CSEKs, which means that data can be **permanently lost** if the key is lost.

**Reference:**

- [https://cloud.google.com/storage/docs/encryption/customer-supplied-keys](https://cloud.google.com/storage/docs/encryption/customer-supplied-keys)
- [https://cloud.google.com/security/encryption/default-encryption#choose_encryption](https://cloud.google.com/security/encryption/default-encryption#choose_encryption)

Final Answer: **B**

It enables secure, compliant encryption with **key rotation**, **audit logging**, and **tight IAM control**, following **Google Cloud's recommended best practices** for managing sensitive data at scale.

</details>

---

### Exam 3 · Q30

At **DataShield Analytics**, your team manages a **Google Cloud project** that utilizes **BigQuery** as the central data warehouse. A **Cloud VPN tunnel** connects your on-premises infrastructure with Google Cloud. To enhance data security, the **security team** wants to **prevent data exfiltration** caused by **malicious insiders**, **compromised code**, or **accidental oversharing**.

**What should you do to best meet these security requirements?**

- A. Enable **Private Google Access** for on-premises traffic only.
- B. Take the following actions: Create a **service account**. Assign the **BigQuery JobUser** and **Storage Object Viewer** roles to that service account. **Revoke all other IAM access** to the project.
- C. Implement **VPC Service Controls** and enable **Private Google Access**.
- D. Enable **Private Google Access**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Implement **VPC Service Controls** and enable **Private Google Access**.

The correct answer is:
**C. Implement VPC Service Controls and enable Private Google Access.**

✅ Justification for Correct Option (C):

To **prevent data exfiltration** from BigQuery and other Google-managed services, the best and **Google-recommended solution** is to implement:

- **VPC Service Controls**, which create a **security perimeter** around sensitive services like **BigQuery**, **Cloud Storage**, etc., and
- **Private Google Access**, which allows access to Google APIs **without traversing the public internet**, ensuring internal-only traffic routing.

Together, these two controls:

- Restrict **unauthorized or untrusted networks or code** from accessing or leaking data.
- Prevent access to BigQuery from outside the defined **perimeter (such as external networks, compromised VMs, or cloud functions)**.
- Enforce **context-aware access** and restrict services by **source network**, **user identity**, and **device attributes**.

**Official Documentation:**

- VPC Service Controls Overview
- Best practices for securing BigQuery
- Private Google Access

❌ Why Other Options Are Incorrect:

A.

Enable Private Google Access for on-premises traffic only.

- This only allows **on-prem systems to reach Google APIs** using internal IPs but does **not restrict access from other locations** or prevent **exfiltration**.
- It does **not create a security perimeter**, so **malicious insiders or compromised cloud services** can still access/export data.

B.

Create a service account with limited roles and revoke other IAM access.

- Limiting IAM permissions is **necessary** but **not sufficient**.
- IAM alone cannot **prevent data exfiltration** if the authorized identity is **compromised**.
- It lacks **network-level protection**, which is why **VPC Service Controls** are required.

D.

Enable Private Google Access.

- While this ensures Google APIs can be accessed from VMs **without public IPs**, it does **not provide any data exfiltration protection** or security perimeter by itself.

✅ Final Answer: **C**

Because it provides **defense-in-depth** against **data exfiltration**, combining **network-level restrictions (VPC Service Controls)** and **secure access paths (Private Google Access)** — which is aligned with **Google Cloud security best practices**.

**Link-** [https://cloud.google.com/vpc-service-controls/docs/overview#benefits](https://cloud.google.com/vpc-service-controls/docs/overview#benefits)

</details>

---

### Exam 3 · Q40

**You're architecting a sizable distributed application comprising 30 microservices, each requiring connection to a database backend. Your priority is to securely store the credentials. Where should you store these credentials?**

- A. In the source code
- B. Within an environment variable
- C. Within a secret management system
- D. In a configuration file with restricted access via ACLs

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Within a secret management system

The correct answer is:
**C. Within a secret management system**

✅ **Correct Option: C. Within a secret management system**

**Explanation:**
When designing a large-scale distributed application (e.g., with 30 microservices), **secure storage of sensitive information like database credentials** is critical. The **Google-recommended** and **industry-standard** approach is to use a **secret management system** such as:

- **Google Secret Manager**: Enables you to store, manage, and access secrets like API keys, passwords, and certificates with IAM-controlled access and audit logging.

**Benefits:**

- Centralized management of secrets
- Fine-grained IAM permissions
- Integration with GKE, Cloud Functions, Cloud Run, etc.
- Secret versioning and automatic rotation
- Audit logging for access tracking

❌ Incorrect Options:

**A. In the source code**

- **Risky and insecure**: Hardcoding credentials in source code can lead to accidental exposure via version control (e.g., GitHub).
- Violates best practices and fails compliance audits.

**B. Within an environment variable**

- Better than hardcoding, but still **less secure and harder to manage at scale**.
- Environment variables can be exposed through debugging or process dumps.
- Lacks centralized control and rotation features.

**D. In a configuration file with restricted access via ACLs**

- While better than source code, this still **lacks centralized control**, auditing, and built-in rotation.
- ACLs can be difficult to manage at scale and might still be misconfigured.

📚 Google Cloud Documentation:

- Secret Manager Overview – Google Cloud
- Best practices for secrets management

References:

[https://cloud.google.com/kubernetes-engine/docs/concepts/secret](https://cloud.google.com/kubernetes-engine/docs/concepts/secret)

[https://cloud.google.com/secret-manager](https://cloud.google.com/secret-manager)

</details>

---

### Exam 3 · Q41

**Your customer is migrating their corporate applications to Google Cloud. The security team seeks comprehensive visibility of all organization resources. You have established yourself as the Organization Administrator using Resource Manager. Which Identity and Access Management (IAM) roles should you assign to the security team, in accordance with Google's recommended practices?**

- A. Organization viewer, Project owner
- B. Organization viewer, Project viewer
- C. Organization administrator, Project browser
- D. Project owner, Network administrator

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Organization viewer, Project viewer

✅ **Correct Option: B. Organization viewer, Project viewer**

**Explanation:**
To give the **security team visibility across all Google Cloud resources** (without giving them unnecessary permissions to modify resources), you should follow the principle of **least privilege**.

Assigning the following roles ensures **read-only access** at both the organization and project levels:

- `roles/resourcemanager.organizationViewer` **(Organization Viewer)**:
  - Provides **read-only** access to view the organization’s structure, policies, and resources.
  - Allows visibility into folders, projects, and IAM policies.
- `roles/viewer` **(Project Viewer)** or `roles/browser` (for navigating resources):
  - Provides **read-only access** to project-level resources, including Compute Engine, GKE, Cloud Storage, etc.

🔐 These roles are **recommended by Google** to give security teams visibility without write access.

❌ Incorrect Options:

**A. Organization viewer, Project owner**

- **Too much privilege**: The `Project Owner` role (`roles/owner`) includes full administrative rights, which exceeds the visibility requirement and violates least privilege.

**C. Organization administrator, Project browser**

- **Overprivileged**: The `Organization Administrator` (`roles/resourcemanager.organizationAdmin`) role grants broad administrative control over all resources in the organization. This role should be tightly controlled and not assigned for simple visibility needs.

**D. Project owner, Network administrator**

- **Wrong scope & permissions**: These roles grant **administrative access**, not just visibility. Also, they’re limited to specific scopes (project/network), not the entire organization.

📚 Google Cloud Documentation:

- Understanding IAM Roles
- Predefined IAM Roles
- Best practices for enterprise organizations

[https://cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles](https://cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles)

</details>

---

### Exam 3 · Q42

A security review at **CloudNova Corp** uncovered that a new VPC network was recently created in your Google Cloud project. Within this network, a Compute Engine instance has its SSH port exposed to the public internet. You need to determine who created this network and when.

What is the best course of action?

- A. Use the Stackdriver alerting console to look for a "Create VM" entry
- B. Go to the **Activity** section under the **Home** tab, filter by **Data Access**, and search for a "Create VM" entry
- C. Open the **Logs Explorer**, filter by **GCE Network** resource type, and search for a "compute.instances.insert" log entry
- D. Connect to the VM using project-level SSH keys, review system login logs, and compare user activity with the list of project owners

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Open the **Logs Explorer**, filter by **GCE Network** resource type, and search for a "compute.instances.insert" log entry

The correct answer is:
**C. Open the Logs Explorer, filter by GCE Network resource type, and search for a `compute.instances.insert` log entry**

✅ **Justification for Correct Option (C):**

To determine **who created a VPC network or a Compute Engine instance** (such as one exposing SSH to the public), the most reliable and audit-friendly method is to:

1. **Open the Cloud Logging > Logs Explorer**
2. Filter by **resource type**: `gce_network` (or use `gce_instance` for VM creation)
3. Search for the **Admin Activity log** entry for:
  - `compute.networks.insert` → for VPC creation
  - `compute.instances.insert` → for VM creation

These entries include:

- **Actor identity** (email or service account)
- **Timestamp** of the action
- **Resource details** (network name, instance name, etc.)

These logs are **automatically recorded** under **Admin Activity** logs, even if you haven’t enabled Data Access logging.

**Official Documentation:**

- Audit logs for Compute Engine
- Viewing audit logs in Logs Explorer

❌ **Why Other Options Are Incorrect:**

**A. Use the Stackdriver alerting console to look for a "Create VM" entry**

- **Incorrect** because Stackdriver alerts (now Cloud Monitoring) are for **monitoring metrics**, not auditing.
- It **doesn't log admin activity** like resource creation unless custom alerts were set up in advance.

**B. Go to the Activity section under the Home tab, filter by Data Access**

- **Incorrect** because:
  - The **Activity page** only shows **high-level summaries**, not detailed event logs.
  - **Data Access logs** are **not enabled by default**, and this action (VM/VPC creation) would fall under **Admin Activity**, not Data Access.

**D. Connect to the VM using project-level SSH keys and review login logs**

- **Not reliable** or recommended.
- May show **system logins**, but won't show **who created the VM** or the VPC.
- Requires access to the VM, and system logs may be rotated or limited.

✅ **Final Answer: C**

Use **Logs Explorer** with the appropriate **resource type** and **log filter** (e.g., `compute.instances.insert`) to accurately identify **who created the VM/network** and **when** — as per **Google Cloud’s recommended auditing practices**.

**⚠️ Note:** The audit-log method for creating a network is `compute.networks.insert` (resource type `gce_network`); `compute.instances.insert` is VM creation. The approach in C (Admin Activity audit logs in Logs Explorer) is still the right one.

</details>

---

### Exam 3 · Q46

TechNova Inc. is migrating its internal applications to Google Cloud. The cybersecurity team at TechNova requires comprehensive visibility into all projects across the organization. You have already enabled Google Cloud Resource Manager and assigned yourself the Organization Administrator role.

Which **Cloud Identity and Access Management (IAM)** roles should be granted to the cybersecurity team to meet their visibility needs?

- A. Organization Viewer and Project Owner
- B. Organization Viewer and Project Viewer
- C. Organization Administrator and Project Browser
- D. Project Owner and Network Administrator

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Organization Viewer and Project Viewer

✅ Correct Answer:

**B. Organization Viewer and Project Viewer**

✅ Justification for Correct Answer:

To **gain visibility into all projects and their configurations** across the organization, the cybersecurity team needs:

1. **Organization-level visibility**:
  This is provided by the `roles/resourcemanager.organizationViewer` (Organization Viewer).
  - This role allows read-only access to organization-level resources and policies such as:
    - Organization policies
    - Folders
    - Projects
    - IAM policies
  **Official Reference**:
  https://cloud.google.com/iam/docs/understanding-roles#resourcemanager-organizationViewer
2. **Project-level visibility**:
  The `roles/viewer` (Project Viewer) role gives read-only access to all project resources:
  - Compute Engine
  - IAM policies
  - Networking components
  - Logs and monitoring
  **Official Reference**:
  https://cloud.google.com/iam/docs/understanding-roles#viewer

Together, these two roles **satisfy the visibility requirement** without granting excessive permissions.

❌ Justifications for Incorrect Options:

**A. Organization Viewer and Project Owner**

- **Organization Viewer** is good (read-only visibility at org level).
- But **Project Owner** (`roles/owner`) gives **full control**, including the ability to:
  - Modify configurations
  - Delete resources
  - Manage IAM policies

This **violates the principle of least privilege** and is **not suitable for a cybersecurity team** that only needs **visibility**, not modification rights.

**Reference**:
https://cloud.google.com/iam/docs/understanding-roles#owner

**C. Organization Administrator and Project Browser**

- **Organization Administrator** (`roles/resourcemanager.organizationAdmin`) allows **modification and management of the entire organization**, including:
  - Managing IAM roles and policies
  - Creating/deleting folders and projects
    This is **too powerful for visibility needs**.
- **Project Browser** (`roles/browser`) only allows listing of resources, not detailed inspection or viewing configurations, logs, etc.

**References**:

- Organization Admin: https://cloud.google.com/iam/docs/understanding-roles#resourcemanager-organizationAdmin
- Project Browser: https://cloud.google.com/iam/docs/understanding-roles#browser

This combination fails to provide **deep visibility** and **over-privileges** the org level.

**D. Project Owner and Network Administrator**

- **Project Owner** gives full permissions (create, delete, modify) within the project.
- **Network Administrator** (`roles/compute.networkAdmin`) allows managing networking resources (e.g., VPC, firewall rules), but **doesn't provide broad visibility into all project configurations** or security auditability.

This combo is inappropriate:

- **Over-privileges control**
- **Under-delivers visibility across the organization**

**Reference**:
[https://cloud.google.com/iam/docs/understanding-roles#compute-networkAdmin](https://cloud.google.com/iam/docs/understanding-roles#compute-networkAdmin)

✅ Final Answer:

**B. Organization Viewer and Project Viewer**

This is the **least-privilege, visibility-only** approach that gives the **cybersecurity team** full insight without administrative access.

</details>

---

### Exam 3 · Q47

CloudWorks Ltd. emphasizes rapid responsiveness and prioritizes meeting customer demands quickly. Their main business goals are **accelerated release cycles and increased agility**. As part of your DevSecOps initiative, you aim to minimize the risk of unintentionally introducing security issues during development.

Which **two measures** should you implement to achieve this? *(Choose two.)*

- A. Require that every code commit is peer-reviewed by a security subject matter expert (SME)
- B. Integrate static source code security analysis tools into the CI/CD pipeline
- C. Ensure all component interfaces have stubs for unit testing
- D. Enable code signing and use a trusted binary repository integrated with your CI/CD workflow
- E. Include a vulnerability scanning tool as part of your continuous integration and delivery process

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Integrate static source code security analysis tools into the CI/CD pipeline **|** E. Include a vulnerability scanning tool as part of your continuous integration and delivery process

✅ Correct Answers:

**B. Integrate static source code security analysis tools into the CI/CD pipeline**
**E. Include a vulnerability scanning tool as part of your continuous integration and delivery process**

✅ Explanation of Correct Options:

**B. Integrate static source code security analysis tools into the CI/CD pipeline**

**Why it’s correct:**

- Static Application Security Testing (**SAST**) tools analyze source code for vulnerabilities **before the code is compiled**.
- When integrated into the **CI/CD pipeline**, they provide **automated, early detection** of security flaws without manual effort or delay.
- It allows **security to shift left**, aligning perfectly with DevSecOps.

**Official Reference:**
Google Cloud DevSecOps Guide – Security in CI/CD:
https://cloud.google.com/architecture/devsecops-overview#secure-your-code-in-ci/cd-pipelines

**E. Include a vulnerability scanning tool as part of your continuous integration and delivery process**

**Why it’s correct:**

- Integrates tools like **Container Analysis** or **third-party vulnerability scanners** into the build and deployment process.
- Helps identify known vulnerabilities in **libraries, images, or dependencies** before code reaches production.
- Works seamlessly with rapid CI/CD cycles.

**Official Reference:**
Google Cloud DevSecOps – Secure your software supply chain:
https://cloud.google.com/architecture/devsecops-overview#detect-vulnerabilities-in-software-components

❌ Explanation of Incorrect Options:

**A. Require that every code commit is peer-reviewed by a security subject matter expert (SME)**

**Why it’s incorrect:**

- While **peer reviews are important**, requiring a **security SME for every commit** is **not scalable** and will **slow down release cycles**.
- This approach conflicts with the company’s goal of **agility and rapid releases**.

**C. Ensure all component interfaces have stubs for unit testing**

**Why it’s incorrect:**

- Stubbed interfaces are useful for **functional testing**, but they don’t help detect **security vulnerabilities**.
- This measure supports **testability**, not **security validation**.

**D. Enable code signing and use a trusted binary repository integrated with your CI/CD workflow**

**Why it’s not ideal in this context:**

- Code signing and secure artifact storage are important for **software supply chain integrity**, but:
  - They are more about **ensuring authenticity of builds and preventing tampering** post-build.
  - They don’t **actively detect or prevent** vulnerabilities during development.
- Helpful later in the chain, not for minimizing **introduction** of vulnerabilities during early dev.

✅ Final Answers:

**B. Integrate static source code security analysis tools into the CI/CD pipeline**
**E. Include a vulnerability scanning tool as part of your continuous integration and delivery process**

</details>

---

### Exam 3 · Q51

A key objective for **DataSure Systems** is ensuring the **integrity and trustworthiness** of data stored in its application. To support this goal, the team wants to **log every change** made to application data and be able to **verify the authenticity** of those logs.

How should you design the logging system to ensure log authenticity?

- A. Simultaneously write each log entry to both a cloud-based system and an on-premises server
- B. Store the logs in a SQL database with strict access controls on who can modify the log table
- C. Digitally sign each log entry along with its timestamp, and store the signature securely
- D. Export each log entry as a JSON file and save it to **Google Cloud Storage**

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Digitally sign each log entry along with its timestamp, and store the signature securely

✅ Correct Answer:

**C. Digitally sign each log entry along with its timestamp, and store the signature securely**

✅ Justification for Option C:

- **Digital signatures** provide cryptographic assurance that:
  - The log entry hasn’t been tampered with.
  - The source is authentic.
- Signing each log entry ensures **non-repudiation** and **tamper detection**.
- When combined with **timestamps**, it also enables **chronological integrity**.
- This approach is consistent with **best practices in trusted logging systems**, particularly in security-sensitive or regulated environments.

**Google Reference** (while not specific to this use case, the general cryptographic best practice is emphasized):

- Google Cloud Key Management Service documentation – Sign Data
- Cloud Audit Logs Overview — for logging best practices including integrity considerations

❌ Justifications for Incorrect Options:

**A. Simultaneously write each log entry to both a cloud-based system and an on-premises server**

- While this may add redundancy, it does **not ensure authenticity** or tamper detection.
- Logs can still be altered at either location unless cryptographically protected.
- Adds complexity but **no guarantee of integrity**.

**B. Store the logs in a SQL database with strict access controls on who can modify the log table**

- Access control helps **prevent unauthorized modifications**, but:
  - It does **not prove log authenticity**.
  - A rogue administrator or compromised account could still modify logs.
- This lacks cryptographic protection and **cannot verify integrity retrospectively**.

**D. Export each log entry as a JSON file and save it to Google Cloud Storage**

- Storing logs in **Cloud Storage** can provide **immutability** if combined with Object Versioning and IAM.
- However, **JSON files alone are not authenticated** unless you also use **signatures or hashing**.
- Without digital signatures, this approach **fails to meet the authenticity requirement**.

✅ Final Answer:

**C. Digitally sign each log entry along with its timestamp, and store the signature securely**

This is the most robust and **cryptographically verifiable method** to ensure **log integrity and authenticity**.

</details>

---

### Exam 3 · Q52

**CloudOps Inc.** uses both a **Google Workspace account** and a **Google Cloud Organization**. However, some developers have been creating Google Cloud projects **outside the organization structure**.

You want to redesign the **Organization resource hierarchy** to:

- Allow developers to create their own projects
- Prevent them from modifying production projects
- Centralize policy management for all projects
- Apply **stricter policies** to production environments
- Minimize disruptions when business requirements evolve
- Follow **Google-recommended best practices**

How should you structure the organization?

- A.Create a second Google Workspace account and a new Cloud Organization Grant developers the **Project Creator** IAM role on the new Organization Move developer-owned projects into the new Organization Set organization-wide policies for both Organizations Apply production-specific policies on the original Organization
- B.Create a folder named **"Production"** under the Organization resource Grant developers the **Project Creator** role on the Organization Move developer projects into the Organization Set default policies at the Organization level Apply stricter policies at the **"Production"** folder level
- C.Create two folders under the Organization: **"Development"** and **"Production"** Grant developers the **Project Creator** IAM role on the **"Development"** folder only Move developer projects into the **"Development"** folder Set baseline policies at the Organization level Apply more restrictive policies to the **"Production"** folder
- D.Reserve the Organization exclusively for production projects Ensure developers do **not** have the **Project Creator** role at the Organization level Allow developers to create development projects **outside** the Organization using their Workspace accounts Set policies at the Organization level for all production projects Apply specific production policies at the individual project level

<details><summary>Answer &amp; explanation</summary>

**Correct:** C.Create two folders under the Organization: **"Development"** and **"Production"** Grant developers the **Project Creator** IAM role on the **"Development"** folder only Move developer projects into the **"Development"** folder Set baseline policies at the Organization level Apply more restrictive policies to the **"Production"** folder

✅ Correct Answer:

**C.**

Create two folders under the Organization: "Development" and "Production"
Grant developers the Project Creator IAM role on the "Development" folder only
Move developer projects into the "Development" folder
Set baseline policies at the Organization level
Apply more restrictive policies to the "Production" folder

✅ **Justification for Option C:**

This solution follows **Google Cloud’s best practices for resource hierarchy design**:

- **Use folders** to separate **environments** such as **Development** and **Production**.
- Grant **Project Creator** IAM role **only on the “Development” folder**, not the whole org — giving developers autonomy **without compromising production**.
- Apply **organization-wide baseline policies** (e.g., domain restriction, logging).
- Apply **stricter policies (e.g., deny roles, stricter access controls)** to the **Production folder**.
- This design is **centralized**, **scalable**, and **flexible** for future changes.

**Official Documentation References:**

- Google Cloud Resource Hierarchy Best Practices:
  https://cloud.google.com/resource-manager/docs/creating-managing-folders
  https://cloud.google.com/resource-manager/docs/creating-managing-organization
- Designing resource hierarchy for access control and policy management:
  https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-org-structure

❌ Why the Other Options Are Incorrect:

**A. Create a second Google Workspace account and new Cloud Organization**

- **Not recommended** to use **multiple Organizations** to separate dev/prod.
- Splitting Orgs **fragments policy control** and **increases management complexity**.
- **Cross-organization management is not supported** for IAM/policies.

**B. Grant Project Creator at the Organization level**

- This gives **developers access to create projects anywhere**, including in Production, which **violates the goal of isolating prod**.
- While using a “Production” folder is correct, this **exposes prod risk**.

**D. Allow developers to create projects outside the Organization**

- **Defeats the goal of centralized policy management**.
- Projects outside the Organization:
  - **Cannot be governed** by Org policies
  - Are **invisible to Org Admins**
- Google **strongly recommends bringing all projects under a single Organization**.

✅ Final Answer:

**C. Create two folders under the Organization: "Development" and "Production"**
**Grant developers the Project Creator IAM role on the "Development" folder only**
**Move developer projects into the "Development" folder**
**Set baseline policies at the Organization level**
**Apply more restrictive policies to the "Production" folder**

</details>

---

### Exam 3 · Q54

The **IT operations team at NetSecure Corp.** wants to **retain Cloud VPN log events for one year** to support compliance and auditing needs. You need to configure Google Cloud to store these logs appropriately.

What should you do?

- A. Create a **log sink** in Cloud Logging with a filter for Cloud VPN logs, and set a **Cloud Storage bucket** as the destination to store logs long term.
- B. Enable the **Compute Engine API**, and configure logging on firewall rules that match VPN traffic.
- C. Create a **Cloud Logging Dashboard** named “Cloud VPN Logs,” and add a chart that visualizes VPN metrics for the past year.
- D. Set up a **Cloud Logging filter** and create a **Pub/Sub topic** to publish selected log entries.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a **log sink** in Cloud Logging with a filter for Cloud VPN logs, and set a **Cloud Storage bucket** as the destination to store logs long term.

✅ Correct Answer:

**A. Create a log sink in Cloud Logging with a filter for Cloud VPN logs, and set a Cloud Storage bucket as the destination to store logs long term.**

✅ Justification:

- **Cloud Logging** by default retains logs for **30 days (for user logs)** unless you export them.
- To **retain logs for 1 year**, you must **export** them using a **log sink**.
- The most cost-effective and compliance-friendly destination for long-term storage is a **Cloud Storage bucket**, which supports **custom retention policies** (e.g., 1 year).
- You can filter for **Cloud VPN logs** using a **log sink filter** like:
  ```
  resource.type="gce_vpn_gateway"
  ```

**Official Documentation:**

- Log Retention and Export: [https://cloud.google.com/logging/docs/export](https://cloud.google.com/logging/docs/export)
- VPN Logging: [https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging](https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging)
- Exporting logs to Cloud Storage: [https://cloud.google.com/logging/docs/export/storage](https://cloud.google.com/logging/docs/export/storage)

❌ Why Other Options Are Incorrect:

**B. Enable the Compute Engine API and configure logging on firewall rules that match VPN traffic**

- Firewall logging only captures **traffic metadata for firewall rule matches**, not **Cloud VPN tunnel state or events**.
- VPN logs come from **VPN Gateway resources**, not firewall rules.
- This does **not guarantee VPN-specific logs** or long-term storage.

**Reference:**
[https://cloud.google.com/vpc/docs/firewall-rules-logging](https://cloud.google.com/vpc/docs/firewall-rules-logging)
[https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging](https://cloud.google.com/network-connectivity/docs/vpn/how-to/logging)

**C. Create a Cloud Logging Dashboard named “Cloud VPN Logs,” and add a chart that visualizes VPN metrics for the past year**

- Dashboards are for **visualization**, not **log storage**.
- Logging dashboards display up to **30 days** of log-based metrics by default.
- Does **not meet the retention requirement** of **1 year**.

**D. Set up a Cloud Logging filter and create a Pub/Sub topic to publish selected log entries**

- Exporting to **Pub/Sub** is typically used for **real-time streaming or processing** (e.g., with Dataflow), not long-term archival.
- Pub/Sub **does not store messages indefinitely**—it only retains them for up to **7 days**.

**Reference:**
[https://cloud.google.com/logging/docs/export/pubsub](https://cloud.google.com/logging/docs/export/pubsub)
[https://cloud.google.com/pubsub/docs/overview#features](https://cloud.google.com/pubsub/docs/overview#features)

✅ Final Answer:

**A. Create a log sink in Cloud Logging with a filter for Cloud VPN logs, and set a Cloud Storage bucket as the destination to store logs long term.**

</details>

---

### Exam 3 · Q55

You are collaborating with the **data warehousing team at DataWise Analytics**, which conducts analytical processing on incoming data. The team needs to handle data received from **external partners**, but this data includes **personally identifiable information (PII)**. The goal is to **process and store the data without retaining any PII**.

What should you do?

- A. Build a **Dataflow pipeline** to ingest data from external sources. Within the pipeline, use the **Cloud Data Loss Prevention (Cloud DLP) API** to detect and remove PII. Store the cleansed data in **BigQuery**.
- B. Design a **Dataflow pipeline** that stores non-PII data in **BigQuery**, and stores PII data in a **Cloud Storage bucket** with a **retention policy** configured.
- C. Request external partners to upload data to **Cloud Storage**, and apply **Bucket Lock** on the bucket. Use a **Dataflow pipeline** to read from the bucket, apply **Cloud DLP** to strip PII, and then store the results in **BigQuery**.
- D. Ask partners to import their data directly into your **BigQuery dataset**. Then, use a **Dataflow pipeline** to copy the data into a new table, skipping all columns that may contain PII.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Build a **Dataflow pipeline** to ingest data from external sources. Within the pipeline, use the **Cloud Data Loss Prevention (Cloud DLP) API** to detect and remove PII. Store the cleansed data in **BigQuery**.

✅ Correct Answer:

**A. Build a Dataflow pipeline to ingest data from external sources. Within the pipeline, use the Cloud Data Loss Prevention (Cloud DLP) API to detect and remove PII. Store the cleansed data in BigQuery.**

✅ Justification for Option A:

- **Cloud DLP** is specifically designed to:
  - **Inspect**, **de-identify**, **mask**, or **redact** PII (like names, SSNs, emails).
- Integrating **Cloud DLP** within a **Dataflow pipeline** allows you to **automatically detect and remove PII during ingestion**.
- Once the data is cleaned, you can **safely store it in BigQuery** for analytics.
- This ensures full compliance with **privacy** and **data minimization** principles.

**Official Docs:**

- Cloud DLP Overview: [https://cloud.google.com/dlp/docs](https://cloud.google.com/dlp/docs)

❌ Justifications for Incorrect Options:

**B. Dataflow pipeline stores non-PII in BigQuery and PII in Cloud Storage with retention**

- This still involves **storing PII**, even if temporarily.
- The requirement clearly states: **“without retaining any PII”**
- Violates the directive of **not keeping PII at all**

**C. Use Bucket Lock + Cloud DLP after storage**

- Uploading data **with PII directly into Cloud Storage** (even with Bucket Lock) **means PII is retained** during that period.
- **DLP is applied *after* storage**, which conflicts with the goal to **never retain PII**.
- **Bucket Lock** is for **immutability**, not for PII protection.

**D. Partners import into BigQuery, then copy excluding PII columns**

- **Risky and non-compliant approach**: PII is **already in BigQuery**, even temporarily.
- **Violates the "no retention" requirement**
- Also depends on partners to comply with schema expectations—less reliable

✅ Final Answer:

**A. Build a Dataflow pipeline to ingest data from external sources. Within the pipeline, use the Cloud DLP API to detect and remove PII. Store the cleansed data in BigQuery.**

</details>

---

### Exam 3 · Q57

**LogiTrack Inc.** runs an application on multiple **Compute Engine instances**, generating approximately **1 TB of log data per day**. For **compliance**, the logs must be retained for **at least two years**. However, logs only need to be **actively queryable for the first 30 days**—after that, they should simply be **retained for audit purposes**.

You need to implement a **cost-efficient and compliant** logging solution that aligns with **Google Cloud's best practices**.

What should you do?

- A.Install the **Cloud Logging agent** on all Compute Engine instances Create a **log sink** that exports logs to a **regional Cloud Storage bucket** Set an **Object Lifecycle rule** to move logs to **Coldline Storage** after 30 days Apply a **bucket retention policy** using **Bucket Lock** to enforce two-year retention
- B.Write a **cron job** on each instance to upload daily logs to a Cloud Storage bucket Create a **log sink** to export logs to a **regional Cloud Storage bucket** Set an **Object Lifecycle rule** to move logs to **Coldline Storage** after one month
- C.Install the **Cloud Logging agent** on all instances Export logs to a **partitioned BigQuery table** using a log sink Set **time_partitioning_expiration** to **30 days** for automatic pruning
- D.Create a **daily cron job** on each instance to upload logs into a **partitioned BigQuery table** Set **time_partitioning_expiration** to 30 days to delete old partitions

<details><summary>Answer &amp; explanation</summary>

**Correct:** A.Install the **Cloud Logging agent** on all Compute Engine instances Create a **log sink** that exports logs to a **regional Cloud Storage bucket** Set an **Object Lifecycle rule** to move logs to **Coldline Storage** after 30 days Apply a **bucket retention policy** using **Bucket Lock** to enforce two-year retention

✅ Correct Answer:

**A.**

Install the Cloud Logging agent on all Compute Engine instances
Create a log sink that exports logs to a regional Cloud Storage bucket
Set an Object Lifecycle rule to move logs to Coldline Storage after 30 days
Apply a bucket retention policy using Bucket Lock to enforce two-year retention

✅ Why Option A is Correct:

This solution meets all objectives:

1. **High Volume Logging (~1 TB/day)**

- Google Cloud Logging agent collects logs efficiently.
- Exporting to **Cloud Storage** handles large volume logs at **low cost**.

2. **30-Day Queryability**

- You can access logs in **Cloud Logging** for 30 days (default retention).
- After that, logs are **available in Cloud Storage** for compliance—but not actively queried.

3. **Cost-Efficiency**

- Moving logs to **Coldline Storage** (via Lifecycle Rules) reduces long-term storage costs.
- Cloud Storage is **cheaper than BigQuery** for storing logs not being queried.

4. **2-Year Retention (Compliance)**

- Apply a **retention policy using Bucket Lock**, which:
  - Prevents deletion or modification
  - Is **compliant with regulatory requirements** such as audit and legal holds

**Official Documentation:**

- Exporting logs to Cloud Storage
- Bucket Lock & Retention Policies
- Cloud Storage Lifecycle Rules
- Cloud Logging Agent

❌ Why Other Options Are Incorrect:

**B. Cron job to upload logs + export to Storage + lifecycle rules**

- Unnecessarily **duplicates log upload** effort—both **manual upload** and **log sink export**.
- Increases **operational overhead** and **risk of inconsistency**.
- Not scalable for 1 TB/day.

**C. Export logs to BigQuery with 30-day expiration**

- **BigQuery** is powerful for analytics, but:
  - **Expensive** for long-term storage of large log volumes
  - After 30 days, logs are **deleted**, which **violates the 2-year retention requirement**
- **No long-term archival** after logs expire

**D. Cron job to upload logs into BigQuery with 30-day expiration**

- Similar to Option C, but also uses **manual upload**, which is **inefficient** at 1 TB/day.
- Again, logs **expire after 30 days**, violating **compliance** needs.

✅ Final Answer:

**A. Install the Cloud Logging agent on all Compute Engine instances**
**Create a log sink that exports logs to a regional Cloud Storage bucket**
**Set an Object Lifecycle rule to move logs to Coldline Storage after 30 days**
**Apply a bucket retention policy using Bucket Lock to enforce two-year retention**

This is **cost-efficient, compliant, and aligned with Google Cloud’s recommended practices**.

**⚠️ Note:** The legacy Cloud Logging agent is replaced by the Ops Agent; the design (sink to Cloud Storage, lifecycle to Coldline, locked retention) is unchanged.

</details>

---

### Exam 3 · Q58

**SecuGuard Ltd.** has recently enabled **Cloud Identity** to manage its user accounts and has also configured its **Google Cloud Organization**. The **security team** now wants to **secure all projects** within the Organization by **preventing IAM users outside the company’s Cloud Identity domain from being granted permissions** moving forward.

What is the most appropriate action to take?

- A. Configure an **Organization Policy** to **restrict identities by domain** to ensure only users from the company's Cloud Identity domain can be granted IAM roles.
- B. Set an **Organization Policy** to **block the creation of service accounts** across all projects.
- C. Use **Cloud Scheduler** to trigger a **Cloud Function** every hour that scans IAM policies and removes users who are not part of the company domain.
- D. Create a technical service account (e.g., `crawler@yourdomain.com`) and assign it the **Project Owner** role at the Organization level. Then, write a **bash script** that: Lists IAM policies of all projects Deletes users not in the company domain Deploy this script on a **Compute Engine VM** and run it using a **cron job every hour**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure an **Organization Policy** to **restrict identities by domain** to ensure only users from the company's Cloud Identity domain can be granted IAM roles.

✅ **Correct Answer:**

**A. Configure an Organization Policy to restrict identities by domain to ensure only users from the company's Cloud Identity domain can be granted IAM roles.**

✅ **Why Option A is Correct:**

Google Cloud provides an **Organization Policy constraint** named:

```
constraints/iam.allowedPolicyMemberDomains
```

This constraint allows an **Organization Administrator** to **restrict IAM principals** to specific identity domains—e.g., only `@secuguard.com` users.

When enforced:

- IAM policies **cannot be updated** to include **external identities**.
- It **prevents violations proactively**, rather than relying on reactive cleanups.
- Applies at the **Organization level** and can inherit to **all folders/projects**.

This satisfies SecuGuard's goal of **ensuring only internal users** (from their Cloud Identity domain) can be granted IAM roles.

**Official Documentation:**

- Restricting IAM policies by domain
- constraints/iam.allowedPolicyMemberDomains

❌ Why Other Options Are Incorrect:

**B. Set an Organization Policy to block the creation of service accounts**

- This **does not prevent external users from being granted IAM roles**.
- **Service accounts** are internal identities and may still be needed for automation.
- Not aligned with the core requirement (controlling **user** identities by **domain**).

**C. Use Cloud Scheduler + Cloud Function to remove external users**

- This is a **reactive workaround**, not a preventive control.
- May lead to **security gaps** (e.g., external users having temporary access between scans).
- **Complex**, **hard to maintain**, and not Google-recommended.

**D. Use a bash script on a Compute Engine VM to remove external users via cron**

- Similar to option C, but even worse:
  - Requires full **Project Owner** privileges
  - Introduces **operational risk and complexity**
  - Lacks **granular auditing**, and prone to **errors**
- Not a scalable or **policy-driven solution**

✅ Final Answer:

**A. Configure an Organization Policy to restrict identities by domain to ensure only users from the company's Cloud Identity domain can be granted IAM roles.**

</details>

---

### Exam 3 · Q60

**DataSecure Inc.** uses **BigQuery** for its data warehousing needs. Some of the datasets contain **personally identifiable information (PII)** that should be **accessible only to the compliance team**. However, the **data science team** needs access to the **non-PII data** in the same tables.

You want to **minimize both cost and administrative overhead** when granting the appropriate access to each team.

What should you do?

- A.In the source dataset, create **views** of the tables that **exclude PII fields** Grant the data science team an appropriate **project-level IAM role** Set **access controls** on the dataset containing the views
- B.In the source dataset, create **materialized views** of the tables that **exclude PII fields** Grant the data science team an appropriate **project-level IAM role** Set **access controls** on the dataset containing the views
- C.Create a **separate dataset** for the data science team In that dataset, create **views** of the tables that **exclude PII** Assign a **project-level IAM role** to the data science team Set **access controls** on the new dataset **Authorize the view** to access the original dataset
- D.Create a **separate dataset** for the data science team In that dataset, create **materialized views** of the tables that **exclude PII** Assign a **project-level IAM role** to the data science team Set **access controls** on the new dataset **Authorize the view** to access the original dataset

<details><summary>Answer &amp; explanation</summary>

**Correct:** C.Create a **separate dataset** for the data science team In that dataset, create **views** of the tables that **exclude PII** Assign a **project-level IAM role** to the data science team Set **access controls** on the new dataset **Authorize the view** to access the original dataset

✅ Correct Answer:

**C.**

Create a separate dataset for the data science team
In that dataset, create **views** of the tables that exclude PII
Assign a **project-level IAM role** to the data science team
Set access controls on the **new dataset**
Authorize the view to access the original dataset

✅ Why Option C is Correct:

- **Views** in BigQuery are **logical representations** of data and do **not incur additional storage or compute costs** until queried.
- By creating views that **exclude PII columns**, you **safely isolate sensitive data**.
- Placing these views in a **separate dataset** allows you to apply **fine-grained IAM controls** specifically for the data science team.
- The **authorized views mechanism** lets views in one dataset access data in another while enforcing column-level security.

This method:

- **Meets privacy requirements**
- **Minimizes cost** (compared to materialized views)
- **Keeps admin overhead low** (IAM at dataset/view level is simple and scalable)

**Key Google Docs:**

- Authorized views in BigQuery
- Controlling access to datasets
- Views vs. materialized views

❌ Why Other Options Are Incorrect:

**A. Views in the source dataset + project-level IAM role**

- Creating views in the **same source dataset** does **not provide strong separation** of access control.
- IAM permissions at the dataset level can inadvertently expose underlying PII data.
- **Best practice is to put views in a separate dataset** to fully leverage authorized views.

**B. Materialized views in the source dataset**

- **Materialized views incur storage and compute costs** as they precompute and store results.
- Also shares the **same problem as A**: being in the **same dataset** as the source, which complicates access control.

**D. Materialized views in a separate dataset**

- While access control is better than B, **materialized views are unnecessary and more expensive** for the requirement.
- Views suffice when you just need to **hide PII columns** without performance optimization.

✅ Final Answer:

**C. Create a separate dataset for the data science team. In that dataset, create views of the tables that exclude PII. Assign a project-level IAM role to the data science team. Set access controls on the new dataset. Authorize the view to access the original dataset.**

</details>

---

### Exam 4 · Q11

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

- A. Employ Secret Manager to store card data post-query for duplicate identification.
- B. Utilize Firestore in Datastore mode to encrypt card data using a deterministic algorithm.
- C. Employ sharding across multiple Memorystore instances to encrypt card data using a deterministic algorithm.
- D. Use Cloud SQL with column-level encryption to store card data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Utilize Firestore in Datastore mode to encrypt card data using a deterministic algorithm.

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

</details>

---

### Exam 4 · Q12

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

- A. Update Security Policy 'from-fastly' gcloud compute security-policies rules update 1000 \ --security-policy from-fastly \ --src-ip-ranges * \ --action "allow"
- B. Update Firewall Rule 'sourceiplist-fastly' gcloud compute firewall rules update sourceiplist-fastly \ --priority 1000 \ --allow tcp:443
- C. Update Firewall Rule 'hlr-policy' gcloud compute firewall rules update hlr-policy \ --priority 1000 \ --target-tags=sourceiplist-fastly \ --allow tcp:443
- D. Update Security Policy 'hlr-policy' gcloud compute security-policies rules update 1000 \ --security-policy hlr-policy \ --expression "evaluatePreconfiguredExpr('sourceiplist-fastly')" \ --action "allow"

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Update Security Policy 'hlr-policy' gcloud compute security-policies rules update 1000 \ --security-policy hlr-policy \ --expression "evaluatePreconfiguredExpr('sourceiplist-fastly')" \ --action "allow"

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

</details>

---

### Exam 4 · Q17

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

- A. Validate EHR's product usage against the list of compliant products on the Google Cloud compliance page.
- B. Recommend that EHR enters into a Business Associate Agreement (BAA) with Google Cloud.
- C. Employ Firebase Authentication for EHR's user-facing applications.
- D. Deploy Prometheus to detect and prevent security breaches on EHR's web-based applications.
- E. Utilize GKE private clusters for all Kubernetes workloads.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Validate EHR's product usage against the list of compliant products on the Google Cloud compliance page. **|** B. Recommend that EHR enters into a Business Associate Agreement (BAA) with Google Cloud.

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

</details>

---

### Exam 4 · Q18

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

- A. Enable Binary Authorization on GKE, and sign containers as part of a CI/CD pipeline.
- B. Configure Jenkins to leverage Kritis for cryptographic container signing within a CI/CD pipeline.
- C. Configure Container Registry to exclusively permit trusted service accounts to create and deploy containers from the registry.
- D. Configure Container Registry to employ vulnerability scanning to verify the absence of vulnerabilities prior to workload deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Enable Binary Authorization on GKE, and sign containers as part of a CI/CD pipeline. **|** D. Configure Container Registry to employ vulnerability scanning to verify the absence of vulnerabilities prior to workload deployment.

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

</details>

---

### Exam 4 · Q22

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

- A. Implement an Organizational Policy with a constraint allowing external IP addresses solely on the frontend Compute Engine instances.
- B. Remove the compute.networkAdmin role from all users in the project associated with frontend instances.
- C. Set up an Identity and Access Management (IAM) policy assigning the IT staff to the compute.networkAdmin role for the organization.
- D. Create a custom Identity and Access Management (IAM) role named GCE_FRONTEND with the compute.addresses.create permission.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Implement an Organizational Policy with a constraint allowing external IP addresses solely on the frontend Compute Engine instances.

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

</details>

---

### Exam 4 · Q23

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

- A. Deploy a private cluster with a private endpoint, configured with master authorized networks.
- B. Implement a public cluster with firewall rules and Virtual Private Cloud (VPC) routes.
- C. Utilize a private cluster with a public endpoint, configured with master authorized networks.
- D. Opt for a public cluster with enabled master authorized networks and firewall rules.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy a private cluster with a private endpoint, configured with master authorized networks.

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

</details>

---

### Exam 4 · Q28

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

- A. Create a project for development and testing and another for staging and production.
- B. Establish a network for development and testing and another for staging and production.
- C. Set up one subnetwork for development and another for staging and production.
- D. Create one project for development, a second for staging, and a third for production.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create one project for development, a second for staging, and a third for production.

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

</details>

---

### Exam 4 · Q38

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

- A. Create a service account (SA) in the legacy game's Google Cloud project, add this SA in the new game's IAM page, and then assign the Firebase Admin role to the SA in both projects.
- B. Create a service account (SA) in the legacy game's Google Cloud project, assign the SA the Organization Admin role, and then grant it the Firebase Admin role in both projects.
- C. Create a service account (SA) in the legacy game's Google Cloud project, add a second SA in the new game's IAM page, and then assign the Organization Admin role to both SAs.
- D. Create a service account (SA) in the legacy game's Google Cloud project, assign it the Firebase Admin role, and then migrate the new game to the legacy game's project.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a service account (SA) in the legacy game's Google Cloud project, add this SA in the new game's IAM page, and then assign the Firebase Admin role to the SA in both projects.

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

</details>

---

### Exam 4 · Q39

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

- A. Configure an organizational policy that constrains where resources can be deployed.
- B. Configure IAM conditions to limit the configuration of resources.
- C. Adjust the quotas for resources in the regions not being utilized to 0.
- D. Set up a custom alert in Cloud Monitoring to disable resources upon creation in other regions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Configure an organizational policy that constrains where resources can be deployed.

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

</details>

---

### Exam 4 · Q42

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

- A. Implement Workload Identity and service accounts for utilization by the application platform.
- B. Utilize Kubernetes Secrets, which are inherently obscured, and configure these Secrets for use by the application platform.
- C. Set up Kubernetes Secrets for storing the secret, enable Application-Layer Secrets Encryption, and utilize Cloud Key Management Service (Cloud KMS) for managing the encryption keys. Configure these Secrets for use by the application platform.
- D. Deploy HashiCorp Vault on Compute Engine, utilizing customer-managed encryption keys, and integrate Cloud Key Management Service (Cloud KMS) for encryption key management. Configure these Secrets for use by the application platform.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Implement Workload Identity and service accounts for utilization by the application platform.

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

</details>

---

### Exam 4 · Q44

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

- A. Generate a token and set it as an environment variable for func_display. When invoking func_query, include the token in the request. Validate the token in func_query and reject the invocation if the tokens differ.
- B. Enable "Require authentication" for func_query. Create a unique service account and link it to func_display. Assign the service account the invoker role for func_query. Generate an ID token within func_display and include it in the request when invoking func_query.
- C. Enable "Require authentication" for func_query and restrict it to internal traffic only. Deploy both functions within the same Virtual Private Cloud (VPC). Establish an ingress firewall rule for func_query to exclusively permit traffic from func_display.
- D. Deploy both functions in the same project and VPC. Configure func_query to solely accept internal traffic. Implement an ingress firewall for func_query to allow traffic solely from func_display. Additionally, ensure both functions utilize the same service account.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Enable "Require authentication" for func_query. Create a unique service account and link it to func_display. Assign the service account the invoker role for func_query. Generate an ID token within func_display and include it in the request when invoking func_query.

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

</details>

---

### Exam 4 · Q46

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

- A. Open a support case related to the CVE and engage in a discussion with the support engineer.
- B. Review the CVEs through the Google Cloud Status Dashboard to grasp their implications.
- C. Refer to the Google Cloud Platform Security Bulletins to understand the impact of the CVEs.
- D. Seek an explanation about the CVEs by posting a question on Stack Overflow.
- E. Seek an explanation about the CVEs by posting a question in a Google Cloud discussion group.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Open a support case related to the CVE and engage in a discussion with the support engineer. **|** C. Refer to the Google Cloud Platform Security Bulletins to understand the impact of the CVEs.

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

</details>

---

### Exam 4 · Q56

For this question, refer to the EHR Healthcare case study.

https://services.google.com/fh/files/blogs/master_case_study_ehr_healthcare.pdf

**A renowned research and hospital facility, serving many public figures, is an EHR healthcare customer. Given the sensitivity of their patients' health information, both internal and external sources have attempted to access it maliciously. To safeguard patient data stored in Cloud Storage buckets, the hospital mandates that data must not leave the geographic regions where the buckets are hosted. Specifically, information stored in Cloud Storage buckets in the "europe-west2" region must remain within that area. What action should be taken?**

- A. Encrypt the data within the on-premises application before storing it in the "europe-west2" region.
- B. Activate Virtual Private Cloud Service Controls and establish a service perimeter encompassing the Cloud Storage resources.
- C. Restrict the Identity and Access Management (IAM) "storage.objectViewer" role solely to users and service accounts requiring access to the data.
- D. Implement an access control list (ACL) to restrict bucket access to authorized users, applying it to buckets within the "europe-west2" region.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Activate Virtual Private Cloud Service Controls and establish a service perimeter encompassing the Cloud Storage resources.

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

</details>

---

### Exam 4 · Q57

**In the context of the EHR Healthcare case study, where sales employees work remotely and require access to web-based sales tools located in the EHR data center, a transition from a Virtual Private Network (VPN) infrastructure to a BeyondCorp access model is underway. Each sales employee possesses a Google Workspace account for single sign-on (SSO). What steps should be taken?**

- A. Set up an Identity-Aware Proxy (IAP) connector directed towards the sales tool application.
- B. Establish a Google group for the sales tool application and elevate it to a security group status.
- C. Deploy an external HTTP(S) load balancer and craft a customized Cloud Armor policy tailored for the sales tool application.
- D. Grant the predefined AppEngine Viewer role to each Google Workspace user account requiring access to the sales tool application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set up an Identity-Aware Proxy (IAP) connector directed towards the sales tool application.

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

</details>

---

### Exam 4 · Q58

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**As the data compliance officer for Mountkirk Games, you're tasked with safeguarding customers' personally identifiable information (PII). Mountkirk Games aims to produce anonymized usage reports for their new game and implement a mechanism to delete PII data after a designated timeframe, all while keeping costs at a minimum. How can you ensure compliance while fulfilling these business and technical requirements?**

- A. Store audit logs in Cloud Storage and manually compile reports.
- B. Develop a Cloud Logging filter to export specific date ranges to Pub/Sub.
- C. Archive audit logs in BigQuery and utilize Google Data Studio to generate reports.
- D. Archive user logs on a locally attached persistent disk and consolidate them into a text file for auditing.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Archive audit logs in BigQuery and utilize Google Data Studio to generate reports.

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

</details>

---

### Exam 4 · Q59

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**Mountkirk Games seeks assurance that their new gaming platform adheres to Google's best practices. You aim to confirm compliance with Google-recommended security standards while also providing the operations teams with necessary metrics. What steps should you take? (Choose two)**

- A. Confirm the absence of privileged containers in operation.
- B. Implement obfuscated tags on workloads for enhanced security.
- C. Utilize native logging mechanisms for monitoring.
- D. Ensure workloads do not utilize securityContext to operate as a group.
- E. Enable GKE metering on each cluster to facilitate team-specific usage charging.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Confirm the absence of privileged containers in operation. **|** C. Utilize native logging mechanisms for monitoring.

**A is correct because this is High Priority according to Google best practices.**

**C is correct because this is High Priority according to Google best practices.**

**Other options is not correct:**

B is not correct because tags should be readable and useful to the operations teams when they are working on the clusters.

D is not correct because this may be required for some workloads.

E is not correct because although from a business process this may be useful it won’t impact the operations or security of the cluster.

Hints - [https://cloud.google.com/solutions/best-practices-for-operating-containers](https://cloud.google.com/solutions/best-practices-for-operating-containers)

</details>

---

### Exam 4 · Q60

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the Mountkirk Games case study.

https://services.google.com/fh/files/blogs/master_case_study_mountkirk_games.pdf

**To implement Virtual Private Cloud (VPC) Service Controls for Mountkirk Games, you must address the company's need to allow Cloud Shell usage by developers while restricting their access to managed services. How can you reconcile these conflicting objectives with Mountkirk Games' business requirements?**

- A. Implement VPC Service Controls across the entire platform.
- B. Give precedence to implementing VPC Service Controls over Cloud Shell usage for the entire platform.
- C. Enroll all developers in an access level associated with the service perimeter and authorize their use of Cloud Shell.
- D. Establish a service perimeter solely around projects handling sensitive data and withhold access to it from developers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Establish a service perimeter solely around projects handling sensitive data and withhold access to it from developers.

**D is correct because VPC Service Controls protects data, and Cloud Shell facilitates rapid iteration of Google Cloud architecture changes.**

**Other options is not correct:**

A is not correct because VPC Service Controls do not directly affect scaling of Google Cloud architecture.

B is not correct because a security perimeter is not a business requirement, but rapid iteration is.

C is not correct because it works but does not scale, and we do not want to give users this much access.

References:

[https://cloud.google.com/vpc-service-controls/docs/supported-products#shell](https://cloud.google.com/vpc-service-controls/docs/supported-products#shell)

[https://cloud.google.com/vpc-service-controls](https://cloud.google.com/vpc-service-controls)

</details>

---

### Exam 4 · Q63

***"LEGACY AND OPTIONAL"***

Older case-study questions are included as **optional bonus scenarios to strengthen architecture thinking**, while the **main tests are updated to match the current exam expectations**.

---

For this question, refer to the TerramEarth case study.

https://services.google.com/fh/files/blogs/master_case_study_terramearth.pdf

**As the data compliance officer for TerramEarth, your task is to safeguard customers' personally identifiable information (PII), including credit card details. However, TerramEarth aims to offer personalized product recommendations to its extensive industrial clientele. How can you uphold data privacy while delivering a solution?**

- A. Utilize AutoML to supply data to the recommendation service.
- B. Process PII data on-premises to enhance the security of private information.
- C. Leverage the Cloud Data Loss Prevention (DLP) API to provide data to the recommendation service.
- D. Develop, train, and test machine learning models manually to deliver product recommendations anonymously.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Leverage the Cloud Data Loss Prevention (DLP) API to provide data to the recommendation service.

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

</details>

---

### Exam 5 · Q6

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

**For this question, refer to the Altostrat Media case study. Altostrat keeps a large collection of media assets in Cloud Storage, including confidential interviews and documentaries. They are worried about maintaining the confidentiality of this material and want to prevent unauthorized access. You must implement a Google-recommended approach that integrates easily while giving Altostrat ownership, control, and audit visibility over the encryption keys. What should you do?**

- A. Configure Cloud Storage to use server-side encryption with Google-managed keys and create a bucket policy that limits access to only approved Google groups and required service accounts.
- B. Use the default encryption at rest provided by Cloud Storage and apply fine-grained IAM permissions to restrict access to sensitive buckets.
- C. Encrypt the data on the client side before uploading it to Cloud Storage, store the encryption keys in a HashiCorp Vault deployed on GKE, and enforce fine-grained IAM controls on the buckets.
- D. Use customer-managed encryption keys (CMEK) for all Cloud Storage buckets that store sensitive media and apply fine-grained IAM roles and groups to restrict bucket access.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Use customer-managed encryption keys (CMEK) for all Cloud Storage buckets that store sensitive media and apply fine-grained IAM roles and groups to restrict bucket access.

**Correct option: D. Use customer-managed encryption keys (CMEK) for all Cloud Storage buckets that store sensitive media and apply fine-grained IAM roles and groups to restrict bucket access.**

Altostrat should **use Customer-Managed Encryption Keys (CMEK) with Cloud KMS for the Cloud Storage buckets** that store sensitive media, and still **enforce least-privilege IAM** for bucket access. This is the Google-recommended “easy integration” approach when the customer needs **ownership/control of keys plus audit visibility** (key lifecycle controls like rotate/disable/destroy, and logs via Cloud KMS / Cloud Logging).

Authoritative doc link (working):
[https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)

**Why D is correct**

- **Ownership & control of keys:** CMEK uses **your Cloud KMS key** (customer-managed) instead of Google-managed keys, giving you control over key rotation, disablement, and destruction.
- **Audit visibility:** Cloud KMS integrates with audit logging so key usage/administration can be audited (the key is managed in Cloud KMS, where audit logs apply).
- **Easy integration:** With CMEK, Cloud Storage access behavior stays largely the same as default encryption, but with your key protection and controls added.
- **Defense-in-depth:** IAM controls still matter because encryption doesn’t replace access control; you still restrict who can read/write buckets and who can use the KMS key.

**Why the other options are not the best choice**

A. **Google-managed keys + bucket policy**

- Google-managed keys do not give Altostrat **ownership/control** of keys (they cannot manage lifecycle/rotation/disable/destroy in the same way) and provide less customer key governance than CMEK.
- Bucket policies/IAM are important, but they don’t meet the requirement of customer key ownership and auditability.

B. **Default encryption at rest + fine-grained IAM**

- Default encryption (Google-managed) also fails the “customer owns/controls keys” requirement. IAM alone doesn’t provide key-level control/audit visibility over encryption keys.

C. **Client-side encryption + HashiCorp Vault on GKE**

- This can work technically, but it’s **not the Google-recommended, easily integrated** approach here; it adds significant operational complexity (key distribution, rotation, application changes, recoverability, vault HA/DR).
- Also, Cloud Storage CMEK is designed specifically to provide customer key control **without** forcing you to re-architect applications or run your own key infrastructure.

**Need-to-know foundational concept**

- **Encryption-at-rest choices in Google Cloud (key control spectrum):**
  - **Google-managed/default**: encrypted by default, but **Google controls keys**.
  - **CMEK (Cloud KMS)**: encrypted by default *using your KMS key*—you get **control + governance + audit** while keeping service integration straightforward.
  - **Client-side encryption**: you encrypt before upload; maximum control but **highest complexity** and least “drop-in” integration.

In short: if the requirement is “Google-recommended + easy integration + customer key ownership/control + audit visibility,” **CMEK for Cloud Storage (Option D)** is the best fit.

###### Explanation

**Correct option: D**

Altostrat should **use Customer-Managed Encryption Keys (CMEK) with Cloud KMS for the Cloud Storage buckets** that store sensitive media, and still **enforce least-privilege IAM** for bucket access. This is the Google-recommended “easy integration” approach when the customer needs **ownership/control of keys plus audit visibility** (key lifecycle controls like rotate/disable/destroy, and logs via Cloud KMS / Cloud Logging).

> [!note]- Why the other options are wrong
> A. **Google-managed keys + bucket policy**
>
> - Google-managed keys do not give Altostrat **ownership/control** of keys (they cannot manage lifecycle/rotation/disable/destroy in the same way) and provide less customer key governance than CMEK.
> - Bucket policies/IAM are important, but they don’t meet the requirement of customer key ownership and auditability.
>
> B. **Default encryption at rest + fine-grained IAM**
>
> - Default encryption (Google-managed) also fails the “customer owns/controls keys” requirement. IAM alone doesn’t provide key-level control/audit visibility over encryption keys.
>
> C. **Client-side encryption + HashiCorp Vault on GKE**
>
> - This can work technically, but it’s **not the Google-recommended, easily integrated** approach here; it adds significant operational complexity (key distribution, rotation, application changes, recoverability, vault HA/DR).
> - Also, Cloud Storage CMEK is designed specifically to provide customer key control **without** forcing you to re-architect applications or run your own key infrastructure.

</details>

---

### Exam 5 · Q10

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

**For this question, refer to the Altostrat Media case study. Altostrat is worried about advanced, multi-vector Distributed Denial of Service (DDoS) attacks that could impact multiple infrastructure layers. Such attacks might interrupt video streaming services and lead to financial damage. You must choose an appropriate mitigation strategy. What should you do?**

- A. Configure VPC Service Controls to limit access to sensitive services and reduce the risk of data exfiltration.
- B. Use Cloud Next Generation Firewall (NGFW) with custom network rules to block malicious traffic.
- C. Deploy Google Cloud Armor with both preconfigured and custom rules to provide L3/L4 and L7 protection.
- D. Enable Security Command Center to monitor the environment and detect possible threats.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy Google Cloud Armor with both preconfigured and custom rules to provide L3/L4 and L7 protection.

**Correct option: C — Deploy Google Cloud Armor with both preconfigured and custom rules**

Cloud Armor is Google Cloud’s dedicated **DDoS mitigation and web application protection service**. It provides defense against multi-vector attacks at **Layer 3/4 (network)** and **Layer 7 (application)** and is designed to protect internet-facing services such as video streaming platforms. It includes adaptive protection, preconfigured WAF rules, rate limiting, and custom security policies — exactly what Altostrat needs.

**Why C is correct**

- Built specifically for **DDoS mitigation**
- Protects against **multi-layer attacks**
- Provides **L3/L4 + L7 defense**
- Integrates with load balancers
- Includes WAF-style protections
- Supports adaptive threat detection
- Designed for high-scale streaming workloads

This directly matches the scenario: protecting revenue-critical streaming services from advanced attacks.

**Why the other options are not the best choice**

A. VPC Service Controls
Designed to reduce **data exfiltration risk**, not to mitigate DDoS attacks. It protects data boundaries, not traffic floods.

B. Cloud NGFW
A network firewall can block unwanted traffic, but it is not a dedicated **global DDoS mitigation service** and does not provide the same layered protection or adaptive capabilities as Cloud Armor.

D. Security Command Center
SCC is a **monitoring and risk visibility platform**. It detects threats and misconfigurations but does not actively mitigate live DDoS attacks.

**Need-to-know foundational concept**

Google Cloud security tools have distinct roles:

- **Cloud Armor** → active DDoS and WAF protection
- **VPC Service Controls** → data perimeter / exfiltration protection
- **NGFW** → network segmentation and firewall rules
- **Security Command Center** → threat visibility and posture management

Exam principle:
If the question mentions **DDoS**, **multi-layer attack**, or **internet-facing service protection**, the answer is almost always **Cloud Armor**.

###### Explanation

**Correct option: C — Deploy Google Cloud Armor with both preconfigured and custom rules**

Cloud Armor is Google Cloud’s dedicated **DDoS mitigation and web application protection service**. It provides defense against multi-vector attacks at **Layer 3/4 (network)** and **Layer 7 (application)** and is designed to protect internet-facing services such as video streaming platforms. It includes adaptive protection, preconfigured WAF rules, rate limiting, and custom security policies — exactly what Altostrat needs.

> [!note]- Why the other options are wrong
> A. VPC Service Controls
> Designed to reduce **data exfiltration risk**, not to mitigate DDoS attacks. It protects data boundaries, not traffic floods.
>
> B. Cloud NGFW
> A network firewall can block unwanted traffic, but it is not a dedicated **global DDoS mitigation service** and does not provide the same layered protection or adaptive capabilities as Cloud Armor.
>
> D. Security Command Center
> SCC is a **monitoring and risk visibility platform**. It detects threats and misconfigurations but does not actively mitigate live DDoS attacks.

</details>

---

### Exam 5 · Q21

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

**Question:**

**Following previous data breaches, KnightMotives wants to implement a comprehensive security and risk management framework across its hybrid cloud environment. The solution must protect sensitive vehicle and customer data, support EU regulatory requirements, and improve incident response readiness.**

**Which security architecture best aligns with these requirements?**

- A. Rely on network perimeter firewalls and restrict access to internal corporate networks only.
- B. Implement zero-trust principles using IAM, workload identity, centralized logging, and automated security controls across cloud and on-premises systems.
- C. Encrypt data at rest only and focus primarily on intrusion detection systems.
- D. Delegate security responsibilities entirely to third-party vendors to reduce internal overhead.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Implement zero-trust principles using IAM, workload identity, centralized logging, and automated security controls across cloud and on-premises systems.

**Correct option: B**

**Why B best aligns with the requirements**

KnightMotives needs a **comprehensive security and risk management framework** after prior breaches, spanning a **hybrid cloud environment**, protecting **vehicle and customer data**, complying with **EU regulations**, and improving **incident response readiness**.

- **Zero-trust principles** remove implicit trust based on network location, which is essential in hybrid environments where perimeters are porous.
- **IAM and workload identity** enforce least-privilege access for users and services across cloud and on-prem integrations.
- **Centralized logging and monitoring** provide end-to-end visibility and faster detection, investigation, and response to security incidents.
- **Automated security controls** (policy enforcement, continuous monitoring) reduce human error and improve consistency and auditability—key for regulatory compliance.

This architecture directly addresses security, compliance, and incident response as a unified system rather than isolated controls. v6.1_pca_knightmotives_automoti…

**Why the other options are not suitable**

- **A. Perimeter-only firewalls**
  Insufficient for modern hybrid/cloud threats and does not support zero trust or robust incident response.
- **C. Encrypt at rest only + IDS focus**
  Incomplete; ignores identity-centric controls, encryption in transit, and response automation.
- **D. Fully outsourcing security**
  Reduces internal visibility and control, and does not remove KnightMotives’ accountability for compliance and breaches.

**Single authoritative documentation link**
[Google Cloud zero trust and security foundations](https://cloud.google.com/learn/what-is-zero-trust?hl=en)

###### Explanation

**Correct option: B. Implement zero-trust principles using IAM, workload identity, centralized logging, and automated security controls across cloud and on-premises systems.**

**Why B best aligns with the requirements**

KnightMotives needs a **comprehensive security and risk management framework** after prior breaches, spanning a **hybrid cloud environment**, protecting **vehicle and customer data**, complying with **EU regulations**, and improving **incident response readiness**.

- **Zero-trust principles** remove implicit trust based on network location, which is essential in hybrid environments where perimeters are porous.
- **IAM and workload identity** enforce least-privilege access for users and services across cloud and on-prem integrations.
- **Centralized logging and monitoring** provide end-to-end visibility and faster detection, investigation, and response to security incidents.
- **Automated security controls** (policy enforcement, continuous monitoring) reduce human error and improve consistency and auditability—key for regulatory compliance.

> [!note]- Why the other options are wrong
> **A. Perimeter-only firewalls**
> Insufficient for modern hybrid/cloud threats and does not support zero trust or robust incident response.
>
> **C. Encrypt at rest only + IDS focus**
> Incomplete; ignores identity-centric controls, encryption in transit, and response automation.
>
> **D. Fully outsourcing security**
> Reduces internal visibility and control, and does not remove KnightMotives’ accountability for compliance and breaches.

</details>

---

### Exam 5 · Q25

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

**For this question, refer to the KnightMotives Automotive case study. KnightMotives has set up a Dedicated Cloud Interconnect with 99.99% availability between its headquarters and two metro areas that map to the us-central1 and us-east1 Google Cloud regions. To reduce both cost and latency for these workloads, you want to enforce that Google Cloud resources are deployed only in those two Interconnect regions. What should you do?**

- A. Export Cloud Asset Inventory data to BigQuery, then run a daily Cloud Run job that queries the export and alerts when resources are created outside the approved regions.
- B. Standardize all deployments using Infrastructure as Code with Terraform modules, and set the default region variable for resources to one of the approved regions.
- C. Restrict the VPC connected to the Interconnect so it only contains subnets in the approved regions.
- D. Apply an Organization Policy using the Resource Location Restriction constraint at the organization level, allowing only the approved regions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Apply an Organization Policy using the Resource Location Restriction constraint at the organization level, allowing only the approved regions.

**Correct answer: D**

**Apply an Organization Policy using the Resource Location Restriction constraint at the organization level, allowing only the approved regions.**

**Why option D is correct**

KnightMotives wants to **enforce** that resources are created **only** in the two Interconnect regions (us-central1 and us-east1). The only native, preventative control that can centrally block resource creation outside allowed locations is **Organization Policy Service** with the **resource locations** constraint (`constraints/gcp.resourceLocations`).

By applying it at the **organization level**, you create a governance guardrail that applies across projects (unless intentionally overridden where allowed by policy inheritance rules). This is the strongest way to ensure deployments stay within the two regions for cost and latency alignment with the Dedicated Interconnect metros.

Why the other options are not the best choice

**A. Cloud Asset Inventory export + alerts**
This is detective control (alerts after the fact), not enforcement. Resources could still be created in disallowed regions and incur latency/cost before anyone responds.

**B. Terraform modules with a default region variable**
This is a convention, not enforcement. Teams can override variables, deploy manually in the console/CLI, or use different tools. It doesn’t guarantee compliance.

**C. Restrict the VPC to subnets in approved regions**
Many Google Cloud resources are not constrained by VPC subnet region in a way that prevents creation (and some resources are global or don’t require subnets). It also doesn’t enforce location for services that are regional but not tied to that VPC.

Only **D** prevents the creation of supported location-based resources outside approved regions at the policy layer.

**Need-to-know foundational concept**

- **Requests like “enforce allowed regions” = Organization Policy**: use **Resource Location Restriction** to define allowed regions/multi-regions for supported services.
- **Preventative vs detective**: Organization Policies are preventative guardrails; inventory exports/alerts are detective controls.
- This constraint applies only to **services that let you choose a location**; it doesn’t change where global resources live and can have limitations, so you should validate supported services and test in lower environments before broad rollout.

###### Explanation

**Correct answer: D**

**Apply an Organization Policy using the Resource Location Restriction constraint at the organization level, allowing only the approved regions.**

**Why option D is correct**

KnightMotives wants to **enforce** that resources are created **only** in the two Interconnect regions (us-central1 and us-east1). The only native, preventative control that can centrally block resource creation outside allowed locations is **Organization Policy Service** with the **resource locations** constraint (`constraints/gcp.resourceLocations`).

By applying it at the **organization level**, you create a governance guardrail that applies across projects (unless intentionally overridden where allowed by policy inheritance rules). This is the strongest way to ensure deployments stay within the two regions for cost and latency alignment with the Dedicated Interconnect metros.

> [!note]- Why the other options are wrong
> **A. Cloud Asset Inventory export + alerts**
> This is detective control (alerts after the fact), not enforcement. Resources could still be created in disallowed regions and incur latency/cost before anyone responds.
>
> **B. Terraform modules with a default region variable**
> This is a convention, not enforcement. Teams can override variables, deploy manually in the console/CLI, or use different tools. It doesn’t guarantee compliance.
>
> **C. Restrict the VPC to subnets in approved regions**
> Many Google Cloud resources are not constrained by VPC subnet region in a way that prevents creation (and some resources are global or don’t require subnets). It also doesn’t enforce location for services that are regional but not tied to that VPC.

</details>

---

### Exam 5 · Q27

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

**For this question, refer to the KnightMotives Automotive case study. KnightMotives wants to personalize the dealer experience by training its own AI models for customer-specific recommendations. To do this, the company will collect personally identifiable information (PII) as part of the training dataset. KnightMotives must meet strict global security and compliance requirements and wants the data protected both at rest and during model training, without reducing model quality. What should you do?**

- A. Store the training dataset in BigQuery with column-level encryption, and train the model on Confidential GKE Nodes.
- B. Store the training dataset in BigQuery with column-level encryption, and train the model in Vertex AI notebooks using customer-managed encryption keys.
- C. Use Sensitive Data Protection to de-identify all PII by replacing it with random tokens before storage, and train the model on Confidential GKE Nodes.
- D. Use Sensitive Data Protection to de-identify all PII by replacing it with random tokens before storage, and train the model in Vertex AI notebooks using customer-managed encryption keys.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Store the training dataset in BigQuery with column-level encryption, and train the model on Confidential GKE Nodes.

**Correct answer: A**

**Store the training dataset in BigQuery with column-level encryption, and train the model on Confidential GKE Nodes.**

**Why option A is correct**

The question has three non-negotiable constraints:

- PII must be protected
- protection must apply **at rest and during processing**
- model quality must not degrade

This means we **cannot de-identify** the data (that would change the dataset and reduce model fidelity). Instead, we must use **encryption + confidential computing**.

**Option A satisfies both layers of protection:**

**At rest protection**
BigQuery column-level encryption allows sensitive columns containing PII to be encrypted separately and tightly controlled, while still being usable in analytics pipelines.

**In-use protection**
Confidential GKE Nodes use hardware-backed confidential computing. Data remains encrypted even while being processed in memory. This protects training workloads from insider threats and host-level attacks without modifying the dataset.

This preserves full data fidelity while meeting strict global compliance requirements.

That exact combination — encryption at rest + confidential computing during processing — is the intended architecture pattern.

**Why the other options are not the best choice**

**B. BigQuery + Vertex notebooks with CMEK**

Customer-managed encryption keys protect data **at rest**, not during computation. Vertex notebooks run on standard VMs, so data is decrypted in memory during training.

This fails the requirement to protect data during processing.

**C. De-identify PII + Confidential GKE**

Replacing PII with random tokens changes the dataset. The question explicitly says model quality must not be reduced. Tokenization destroys real-world signal needed for personalization models.

Security is achieved, but business value is lost.

**D. De-identify PII + CMEK**

This combines the weaknesses of B and C:

- data fidelity is reduced
- no in-use protection

It satisfies neither requirement well.

**Need-to-know foundational concept**

There are three states of data security:

data at rest → encryption
data in transit → TLS
data in use → confidential computing

Most systems stop at rest + transit. Highly regulated AI workloads require protecting **data in use** as well.

Confidential computing:

- encrypts memory while workloads run
- prevents host/insider access
- satisfies strict compliance frameworks
- preserves full dataset fidelity

For AI systems that must train on raw PII without degradation, confidential computing is the only architecture that meets both security and accuracy requirements.

###### Explanation

**Why option A is correct**

The question has three non-negotiable constraints:

- PII must be protected
- protection must apply **at rest and during processing**
- model quality must not degrade

This means we **cannot de-identify** the data (that would change the dataset and reduce model fidelity). Instead, we must use **encryption + confidential computing**.

**Option A satisfies both layers of protection:**

**At rest protection**
BigQuery column-level encryption allows sensitive columns containing PII to be encrypted separately and tightly controlled, while still being usable in analytics pipelines.

**In-use protection**
Confidential GKE Nodes use hardware-backed confidential computing. Data remains encrypted even while being processed in memory. This protects training workloads from insider threats and host-level attacks without modifying the dataset.

This preserves full data fidelity while meeting strict global compliance requirements.

That exact combination — encryption at rest + confidential computing during processing — is the intended architecture pattern.

> [!note]- Why the other options are wrong
> **B. BigQuery + Vertex notebooks with CMEK**
>
> Customer-managed encryption keys protect data **at rest**, not during computation. Vertex notebooks run on standard VMs, so data is decrypted in memory during training.
>
> This fails the requirement to protect data during processing.
>
> **C. De-identify PII + Confidential GKE**
>
> Replacing PII with random tokens changes the dataset. The question explicitly says model quality must not be reduced. Tokenization destroys real-world signal needed for personalization models.
>
> Security is achieved, but business value is lost.
>
> **D. De-identify PII + CMEK**
>
> This combines the weaknesses of B and C:
>
> - data fidelity is reduced
> - no in-use protection

</details>

---

### Exam 5 · Q34

**You are designing a new insurance claims processing application that will run on **Google Kubernetes Engine (GKE)**. Your compliance team requires a full, tamper-resistant audit trail for **all administrative activities** starting from day one. The solution must record who deploys a new container image, who changes the GKE cluster configuration, and who accesses running pods or Kubernetes secrets using **kubectl**. What should you do?**

- A. Enable **Binary Authorization** on the GKE cluster and enforce a policy that requires all container images to be signed by a trusted attestor before deployment.
- B. Deploy a **DaemonSet** on every GKE node that runs a logging agent to collect and forward all container logs to **Cloud Logging**.
- C. Enable **GKE Audit Logging** to send Kubernetes API server audit logs to **Cloud Logging**, and ensure **Cloud Audit Logs** are enabled for the project.
- D. Enable **Security Command Center Premium** to analyze GKE logs and detect threats, vulnerabilities, and misconfigurations in real time.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Enable **GKE Audit Logging** to send Kubernetes API server audit logs to **Cloud Logging**, and ensure **Cloud Audit Logs** are enabled for the project.

Correct Answer: **C**

**Enable GKE Audit Logging to send Kubernetes API server audit logs to Cloud Logging, and ensure Cloud Audit Logs are enabled for the project.**

Why C is correct

Your requirement is a **tamper-resistant audit trail for administrative actions from day one**, including:

- who deploys a new container image (via Kubernetes API objects like Deployments)
- who changes GKE cluster configuration
- who accesses pods or Kubernetes secrets using `kubectl`

All of these actions go through the **Kubernetes API server** and/or **Google Cloud control plane APIs**, so the correct approach is to enable:

1. **GKE Audit Logging (Kubernetes API server audit logs)**
  Captures `kubectl` activity such as:
  - `get/list/watch` pods
  - `create/update/patch/delete` deployments
  - `get` secrets (very important for compliance)
  - RBAC changes, config changes, etc.
2. **Cloud Audit Logs for Google Cloud administrative actions**
  Captures actions like:
  - enabling/disabling cluster features
  - IAM policy changes
  - cluster create/update/delete events

This combination gives the required “who did what and when” audit trail, stored centrally in **Cloud Logging**.

**Why the other options are incorrect / not best fit**

A. Binary Authorization

Not correct because:

- It enforces **image deployment policy**, but it does **not** provide a complete audit trail of:
  - `kubectl get secrets`
  - pod exec/access
  - cluster config changes
- It’s a control mechanism, not a full audit log solution.

B. DaemonSet logging agent for container logs

Not correct because:

- Container logs capture **application runtime logs**, not **admin/API activity**
- It won’t reliably record:
  - who changed a Deployment
  - who accessed secrets via `kubectl`
  - who modified RBAC or cluster configuration

D. Security Command Center Premium

Not correct because:

- SCC is for **security posture management and threat detection**
- It can help analyze findings, but it is **not the primary system of record** for a tamper-resistant audit trail of admin actions.

Need-to-know fundamentals (GKE audit trail)

- **kubectl actions = Kubernetes API server requests**
- The correct source for “who accessed secrets / who changed config” is **Kubernetes Audit Logs**
- Google Cloud admin actions are captured via **Cloud Audit Logs**
- Centralized storage and retention are managed via **Cloud Logging** (and optionally sinks to BigQuery/GCS for long retention)

**Official documentation link**

GKE audit logging (Kubernetes API server audit logs):
[https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging](https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging)

###### Explanation

**Why C is correct**

Your requirement is a **tamper-resistant audit trail for administrative actions from day one**, including:

- who deploys a new container image (via Kubernetes API objects like Deployments)
- who changes GKE cluster configuration
- who accesses pods or Kubernetes secrets using `kubectl`

All of these actions go through the **Kubernetes API server** and/or **Google Cloud control plane APIs**, so the correct approach is to enable:

1. **GKE Audit Logging (Kubernetes API server audit logs)**
  Captures `kubectl` activity such as:
  - `get/list/watch` pods
  - `create/update/patch/delete` deployments
  - `get` secrets (very important for compliance)
  - RBAC changes, config changes, etc.
2. **Cloud Audit Logs for Google Cloud administrative actions**
  Captures actions like:
  - enabling/disabling cluster features
  - IAM policy changes
  - cluster create/update/delete events

This combination gives the required “who did what and when” audit trail, stored centrally in **Cloud Logging**.

> [!note]- Why the other options are wrong
> A. Binary Authorization
>
> Not correct because:
>
> - It enforces **image deployment policy**, but it does **not** provide a complete audit trail of:
>   - `kubectl get secrets`
>   - pod exec/access
>   - cluster config changes
> - It’s a control mechanism, not a full audit log solution.
>
> B. DaemonSet logging agent for container logs
>
> Not correct because:
>
> - Container logs capture **application runtime logs**, not **admin/API activity**
> - It won’t reliably record:
>   - who changed a Deployment
>   - who accessed secrets via `kubectl`
>   - who modified RBAC or cluster configuration
>
> D. Security Command Center Premium
>
> Not correct because:
>
> - SCC is for **security posture management and threat detection**
> - It can help analyze findings, but it is **not the primary system of record** for a tamper-resistant audit trail of admin actions.

</details>

---

### Exam 5 · Q35

To strengthen governance and security, your organization has organized its Google Cloud resources using folders for different business units. Under each business unit folder, there are subfolders for **development**, **staging**, and **production**, and production environments must meet these internal controls:

- Production workloads must **not allow direct internet ingress by default**, unless explicitly tagged.
- Customer access must be supported over **HTTPS**.

You need a scalable and enforceable approach that **blocks internet ingress** for all production folders, while still allowing **direct HTTPS access only to selected VMs**. You must also ensure that project teams **cannot override** these controls for any current or future production projects. What should you do?

- A. For each production folder, apply a **hierarchical firewall policy** that denies all ingress traffic except HTTPS to tagged VMs.
- B. Require application teams to deploy a **Terraform module** in every project that creates VPC firewall rules to deny ingress and allow HTTPS.
- C. At the organization root, apply a **hierarchical firewall policy** that denies all ingress traffic except HTTPS to tagged VMs.
- D. At each production folder, use an **organization policy** to block all external IPs and require teams to use external HTTPS load balancers.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. For each production folder, apply a **hierarchical firewall policy** that denies all ingress traffic except HTTPS to tagged VMs.

Correct Answer: A

**For each production folder, apply a hierarchical firewall policy that denies all ingress traffic except HTTPS to explicitly selected targets (for example, VMs that have an approved secure tag or run under a specific service account).**

Why A is correct

You need an approach that is:

- **Scalable across many current and future production projects**
- **Enforceable from the resource hierarchy (folders)**
- **Not overridable by project teams**
- **Default-deny for direct internet ingress**
- **Allows direct HTTPS only for explicitly approved workloads**

A **hierarchical firewall policy** attached at each **production folder** is designed for exactly this kind of org-wide governance. Cloud NGFW evaluates hierarchical firewall policy rules **before any VPC firewall rules**, so project-level firewall changes cannot bypass your production guardrail.

Implementation pattern:

- In the **production folder** policy:
  - Rule 1: **Deny ingress from 0.0.0.0/0** to all targets (default deny)
  - Rule 2: **Allow tcp:443** only to explicitly approved targets (for example, by using **secure tags** or a dedicated **service account** for “internet-allowed” VMs)

This satisfies:

- “Must not allow direct internet ingress by default”
- “Allow direct HTTPS only to selected VMs”
- “Teams cannot override controls for any current or future prod projects”

Important detail: hierarchical firewall policy rules don’t use classic VPC network tags; for selective targeting you typically use **secure tags** (IAM-governed tags) or **service accounts**.

**Why the other options are incorrect / not best fit**

B. Terraform module in every project

Not enforceable. Teams can skip it, modify it, or misconfigure it. It also does not automatically protect **future** projects.

C. Apply the hierarchical policy at the organization root

It’s enforceable, but it applies to **dev and staging too**, which violates your requirement to block ingress specifically for **production folders**.

D. Org policy to block all external IPs and require external HTTPS load balancers

Blocking external IPs prevents **direct HTTPS access to selected VMs**, which your requirement explicitly needs. Also, forcing external HTTPS load balancers is a different access model than “direct HTTPS to selected VMs.”

Need-to-know governance fundamentals

- **Hierarchical firewall policies** are the right tool when you need centralized guardrails applied at **folder/org** level.
- They are evaluated **before** VPC firewall rules, which is what makes them hard for project teams to bypass.
- For “allow only if explicitly tagged,” use **secure tags** (or service accounts) to scope the allow rule to just approved instances.

**Official documentation**

**Firewall policies overview (hierarchical firewall policies, evaluation order, and centralized enforcement):**
[https://cloud.google.com/firewall/docs/firewall-policies-overview](https://cloud.google.com/firewall/docs/firewall-policies-overview)

###### Explanation

**Why A is correct**

You need an approach that is:

- **Scalable across many current and future production projects**
- **Enforceable from the resource hierarchy (folders)**
- **Not overridable by project teams**
- **Default-deny for direct internet ingress**
- **Allows direct HTTPS only for explicitly approved workloads**

A **hierarchical firewall policy** attached at each **production folder** is designed for exactly this kind of org-wide governance. Cloud NGFW evaluates hierarchical firewall policy rules **before any VPC firewall rules**, so project-level firewall changes cannot bypass your production guardrail.

Implementation pattern:

- In the **production folder** policy:
  - Rule 1: **Deny ingress from 0.0.0.0/0** to all targets (default deny)
  - Rule 2: **Allow tcp:443** only to explicitly approved targets (for example, by using **secure tags** or a dedicated **service account** for “internet-allowed” VMs)

This satisfies:

- “Must not allow direct internet ingress by default”
- “Allow direct HTTPS only to selected VMs”
- “Teams cannot override controls for any current or future prod projects”

Important detail: hierarchical firewall policy rules don’t use classic VPC network tags; for selective targeting you typically use **secure tags** (IAM-governed tags) or **service accounts**.

> [!note]- Why the other options are wrong
> B. Terraform module in every project
>
> Not enforceable. Teams can skip it, modify it, or misconfigure it. It also does not automatically protect **future** projects.
>
> C. Apply the hierarchical policy at the organization root
>
> It’s enforceable, but it applies to **dev and staging too**, which violates your requirement to block ingress specifically for **production folders**.
>
> D. Org policy to block all external IPs and require external HTTPS load balancers
>
> Blocking external IPs prevents **direct HTTPS access to selected VMs**, which your requirement explicitly needs. Also, forcing external HTTPS load balancers is a different access model than “direct HTTPS to selected VMs.”

</details>

---

### Exam 5 · Q44

**Your company is building containerized applications through a CI/CD pipeline. To improve the security and maintainability of the build workflow, you need to:**

- **Detect potential vulnerabilities in your container images**
- **Produce verifiable build metadata for audit and compliance purposes**
- **Maintain a complete inventory of your application dependencies**

**What should you do?**

- A. Use **Cloud Build** to build container images, then run **Artifact Analysis** on images stored in **Artifact Registry**.
- B. Use **Cloud Build** to build container images, enforce **Binary Authorization**, and use **Cloud Asset Inventory** for tracking and analysis.
- C. Use **Cloud Build** to build container images, push them to **Artifact Registry**, and use **Security Command Center** for tracking and analysis.
- D. Use **Cloud Build** to build container images, enforce **Binary Authorization**, and use **Security Command Center** for tracking and analysis.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Use **Cloud Build** to build container images, then run **Artifact Analysis** on images stored in **Artifact Registry**.

**Correct Answer: A**

**Use Cloud Build to build container images, then run Artifact Analysis on images stored in Artifact Registry.**

Why A is correct

This option best satisfies all three requirements in a secure, maintainable, and Google-recommended way:

1) Detect potential vulnerabilities in container images

When you store images in **Artifact Registry**, you can use **Artifact Analysis (container scanning)** to automatically scan images and surface vulnerabilities.

2) Produce verifiable build metadata (audit/compliance)

Artifact Analysis supports **metadata/attestations** for artifacts, which provides verifiable information about the build and the artifact (useful for compliance and audit trails).

3) Maintain an inventory of application dependencies

Artifact Analysis integrates with **Software Bill of Materials (SBOM)** generation, which provides a structured dependency inventory for container images.

This is a clean CI/CD flow:
Cloud Build → Artifact Registry → Artifact Analysis (scanning + SBOM + metadata)

**Why the other options are incorrect / not best fit**

**B. Cloud Build + Binary Authorization + Cloud Asset Inventory**

**Not best because:**

- **Cloud Asset Inventory** inventories Google Cloud resources, not container dependencies/SBOM.
- Binary Authorization is for **admission control at deploy time**, not vulnerability scanning or dependency inventory.

**C. Cloud Build + Artifact Registry + Security Command Center**

**Not best because:**

- SCC aggregates security findings but is not the primary tool for:
  - image vulnerability scanning workflow
  - SBOM inventory generation
  - build metadata/attestations for artifacts

**D. Cloud Build + Binary Authorization + Security Command Center**

**Not best because:**

- Missing the direct mechanism for scanning + SBOM + artifact-level metadata.
- Binary Authorization helps enforce trusted deployments but does not generate dependency inventory by itself.

**Need-to-know fundamentals**

- **Artifact Registry + Artifact Analysis** is the core Google Cloud-native pattern for:
  - container vulnerability scanning
  - SBOM generation
  - artifact metadata/attestations
- **Binary Authorization** is complementary (policy enforcement during deploy), not a replacement for scanning and SBOM.

**Official documentation link**

[Artifact Analysis overview (vulnerability scanning + metadata/SBOM capabilities)](https://docs.cloud.google.com/artifact-registry/docs/analysis)

###### Explanation

**Why A is correct**

This option best satisfies all three requirements in a secure, maintainable, and Google-recommended way:

1) Detect potential vulnerabilities in container images

When you store images in **Artifact Registry**, you can use **Artifact Analysis (container scanning)** to automatically scan images and surface vulnerabilities.

2) Produce verifiable build metadata (audit/compliance)

Artifact Analysis supports **metadata/attestations** for artifacts, which provides verifiable information about the build and the artifact (useful for compliance and audit trails).

3) Maintain an inventory of application dependencies

Artifact Analysis integrates with **Software Bill of Materials (SBOM)** generation, which provides a structured dependency inventory for container images.

This is a clean CI/CD flow:
Cloud Build → Artifact Registry → Artifact Analysis (scanning + SBOM + metadata)

> [!note]- Why the other options are wrong
> B. Cloud Build + Binary Authorization + Cloud Asset Inventory
>
> Not best because:
>
> - **Cloud Asset Inventory** inventories Google Cloud resources, not container dependencies/SBOM.
> - Binary Authorization is for **admission control at deploy time**, not vulnerability scanning or dependency inventory.
>
> C. Cloud Build + Artifact Registry + Security Command Center
>
> Not best because:
>
> - SCC aggregates security findings but is not the primary tool for:
>   - image vulnerability scanning workflow
>   - SBOM inventory generation
>   - build metadata/attestations for artifacts
>
> D. Cloud Build + Binary Authorization + Security Command Center
>
> Not best because:
>
> - Missing the direct mechanism for scanning + SBOM + artifact-level metadata.
> - Binary Authorization helps enforce trusted deployments but does not generate dependency inventory by itself.

</details>

---

### Exam 5 · Q50

**Your company has a Google Cloud project that uses **BigQuery** as its data warehouse. Connectivity between your on-premises environment and Google Cloud is provided through a **Cloud VPN** tunnel. The security team wants to reduce the risk of **data exfiltration** caused by malicious insiders, compromised application code, or accidental data exposure. What should you do?**

- A. Set up **Private Service Connect**.
- B. Configure **VPC Service Controls**, and enable **Private Google Access** for the on-premises hosts.
- C. Create a service account, grant it **BigQuery JobUser** and **Storage Object Viewer**, and remove all other IAM access from the project.
- D. Enable **Private Google Access**.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure **VPC Service Controls**, and enable **Private Google Access** for the on-premises hosts.

**Correct Answer: B**

**Configure VPC Service Controls, and enable Private Google Access for the on-premises hosts.**

Why B is correct

Your requirement is specifically to **reduce the risk of data exfiltration** from BigQuery due to:

- malicious insiders
- compromised code
- accidental exposure

The Google-recommended control for this is **VPC Service Controls (VPC-SC)**, which creates a **service perimeter** around Google-managed services like **BigQuery** to help prevent data from being accessed or moved outside trusted boundaries.

Since your connectivity is through **Cloud VPN**, you also want your on-prem hosts to reach Google APIs privately (without traversing the public internet). Enabling **Private Google Access** (and the related private access patterns) supports private connectivity to Google APIs.

So this combination delivers:

- **Exfiltration risk reduction** (VPC-SC)
- **Private access to Google APIs** from your network path (Private Google Access)

**Official documentation:**
[https://cloud.google.com/vpc-service-controls/docs/overview](https://cloud.google.com/vpc-service-controls/docs/overview)

**Why the other options are incorrect / not best fit**

**A. Private Service Connect**

PSC provides private connectivity to supported services, but it is not the primary control to stop **data exfiltration** from BigQuery. The key requirement is exfiltration protection, which is VPC-SC’s purpose.

**C. Restrict IAM to a single service account**

IAM hardening helps, but it does not address:

- accidental exposure
- compromised code using valid credentials
- copying data to unauthorized destinations
  Also, it’s not practical for real organizations and doesn’t create an exfiltration perimeter.

**D. Enable Private Google Access only**

Private Google Access reduces internet exposure but does not prevent data exfiltration once access is granted. It does not provide a perimeter control like VPC-SC.

Need-to-know fundamentals

- **VPC Service Controls** is the primary Google Cloud feature to reduce **data exfiltration risk** for Google-managed services like BigQuery.
- **Private Google Access** helps keep API traffic private, but it’s not sufficient alone for insider/exfiltration scenarios.

**Official documentation link**

**VPC Service Controls overview:**
[https://cloud.google.com/vpc-service-controls/docs/overview](https://cloud.google.com/vpc-service-controls/docs/overview)

###### Explanation

**Why B is correct**

Your requirement is specifically to **reduce the risk of data exfiltration** from BigQuery due to:

- malicious insiders
- compromised code
- accidental exposure

The Google-recommended control for this is **VPC Service Controls (VPC-SC)**, which creates a **service perimeter** around Google-managed services like **BigQuery** to help prevent data from being accessed or moved outside trusted boundaries.

Since your connectivity is through **Cloud VPN**, you also want your on-prem hosts to reach Google APIs privately (without traversing the public internet). Enabling **Private Google Access** (and the related private access patterns) supports private connectivity to Google APIs.

So this combination delivers:

- **Exfiltration risk reduction** (VPC-SC)
- **Private access to Google APIs** from your network path (Private Google Access)

> [!note]- Why the other options are wrong
> A. Private Service Connect
>
> PSC provides private connectivity to supported services, but it is not the primary control to stop **data exfiltration** from BigQuery. The key requirement is exfiltration protection, which is VPC-SC’s purpose.
>
> C. Restrict IAM to a single service account
>
> IAM hardening helps, but it does not address:
>
> - accidental exposure
> - compromised code using valid credentials
> - copying data to unauthorized destinations
>   Also, it’s not practical for real organizations and doesn’t create an exfiltration perimeter.
>
> D. Enable Private Google Access only
>
> Private Google Access reduces internet exposure but does not prevent data exfiltration once access is granted. It does not provide a perimeter control like VPC-SC.

</details>

---

### Exam 5 · Q52

**You work at a financial institution that stores mortgage loan approval documents in Cloud Storage. Any modification to an approval document must be uploaded as a new, separate file. You must ensure that these documents cannot be deleted or overwritten for the next 5 years. What should you do?**

- A. Set a **bucket retention policy** for 5 years and **lock** the retention policy.
- B. Apply the organization policy constraint `constraints/storage.retentionPolicySeconds` at the **organization level** and set it to 5 years.
- C. Encrypt the bucket using a **customer-managed encryption key (CMEK)** and rotate the key after 5 years.
- D. Apply the organization policy constraint `constraints/storage.retentionPolicySeconds` at the **project level** and set it to 5 years.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Set a **bucket retention policy** for 5 years and **lock** the retention policy.

**Correct Answer: A**

**Set a bucket retention policy for 5 years and lock the retention policy.**

**Why A is correct**

You need to ensure that mortgage approval documents in **Cloud Storage**:

- **cannot be deleted** for 5 years
- **cannot be overwritten** for 5 years
- and any modification must be stored as a **new object** (new file)

A **Cloud Storage bucket retention policy** enforces a minimum retention period during which objects are **immutable** with respect to deletion or replacement. Once you **lock** the retention policy, it becomes **tamper-resistant**, meaning even project owners/admins cannot remove or reduce the retention period.

This directly satisfies the requirement that documents must not be deleted or overwritten for 5 years.

**Official documentation:**
[https://cloud.google.com/storage/docs/bucket-lock](https://cloud.google.com/storage/docs/bucket-lock)

**Why the other options are incorrect / not best fit**

**B. Org policy at organization level for retentionPolicySeconds**

Organization Policy can enforce that a retention policy must be set, but the question requires ensuring the documents **cannot be deleted or overwritten**, which is guaranteed by the **bucket retention policy + lock** mechanism. Org policy alone does not replace bucket lock enforcement behavior.

**C. CMEK + rotate key after 5 years**

Encryption controls confidentiality, not immutability. Rotating keys does not prevent deletion or overwriting of objects.

**D. Org policy at project level for retentionPolicySeconds**

Same issue as B. It is governance, but the core requirement is **WORM-style protection**, which is achieved by **bucket retention policy + lock**.

**Need-to-know fundamentals**

- **Retention policy** prevents deletion and overwriting for a defined period.
- **Bucket Lock** makes the retention policy irreversible (strong compliance control).
- This is the standard Cloud Storage approach for **WORM compliance**.

**Official documentation link**

**Bucket Lock / retention policy enforcement:**
[https://cloud.google.com/storage/docs/bucket-lock](https://cloud.google.com/storage/docs/bucket-lock)

###### Explanation

**Why A is correct**

**You need to ensure that mortgage approval documents in Cloud Storage:**

- **cannot be deleted** for 5 years
- **cannot be overwritten** for 5 years
- and any modification must be stored as a **new object** (new file)

A **Cloud Storage bucket retention policy** enforces a minimum retention period during which objects are **immutable** with respect to deletion or replacement. Once you **lock** the retention policy, it becomes **tamper-resistant**, meaning even project owners/admins cannot remove or reduce the retention period.

This directly satisfies the requirement that documents must not be deleted or overwritten for 5 years.

> [!note]- Why the other options are wrong
> B. Org policy at organization level for retentionPolicySeconds
>
> Organization Policy can enforce that a retention policy must be set, but the question requires ensuring the documents **cannot be deleted or overwritten**, which is guaranteed by the **bucket retention policy + lock** mechanism. Org policy alone does not replace bucket lock enforcement behavior.
>
> C. CMEK + rotate key after 5 years
>
> Encryption controls confidentiality, not immutability. Rotating keys does not prevent deletion or overwriting of objects.
>
> D. Org policy at project level for retentionPolicySeconds
>
> Same issue as B. It is governance, but the core requirement is **WORM-style protection**, which is achieved by **bucket retention policy + lock**.

</details>

---

### Exam 5 · Q53

**Your team plans to use Vertex AI to build and deploy ML models for fraud detection, recommendations, and churn prediction. You want to harden the Vertex AI and Workbench environment specifically to prevent data exfiltration. What should you do?**

- A. Enable Private Google Access on the VPC so Vertex AI can reach Google services without using the public internet.
- B. Enable VPC Flow Logs to observe traffic to and from Vertex AI services and detect suspicious behavior.
- C. Create a VPC Service Controls perimeter protecting ml.googleapis.com and document.googleapis.com.
- D. Create a VPC Service Controls perimeter protecting aiplatform.googleapis.com and notebooks.googleapis.com.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Create a VPC Service Controls perimeter protecting aiplatform.googleapis.com and notebooks.googleapis.com.

**Correct answer: D. Create a VPC Service Controls perimeter protecting aiplatform.googleapis.com and notebooks.googleapis.com.**

**Why D is correct**
To specifically prevent data exfiltration from Vertex AI training/serving and from Workbench-managed notebooks, you should enforce a VPC Service Controls (VPC SC) service perimeter around the Google APIs those products use. VPC SC is designed to mitigate data exfiltration risk by restricting where protected Google-managed resources can be accessed from, and by blocking API calls that would move data outside the perimeter (unless explicitly allowed via perimeter rules). For Vertex AI and Workbench, that means protecting the Vertex AI API and the Notebooks/Workbench API in the same perimeter so the end-to-end workflow (development in Workbench + training/serving in Vertex AI) stays inside the perimeter.

**Documentation**: [https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls](https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls?utm_source=chatgpt.com)

**Why the other options are not the best choice**
**A.** Private Google Access reduces exposure by allowing access to Google APIs without public IPs, but it does not provide a policy boundary that prevents exfiltration to resources outside your trusted projects/organizations. It’s a networking path choice, not an exfiltration control.

**B.** VPC Flow Logs help you observe and investigate traffic patterns, but they are detective controls, not preventive. They don’t stop data from leaving; they only provide telemetry after (or during) events.

**C.** ml.googleapis.com is associated with legacy ML services (older AI Platform endpoints) rather than the Vertex AI API used for modern Vertex AI workflows, and document.googleapis.com is for Document AI (not the core Vertex AI + Workbench control plane). Even if you protected those, you wouldn’t be placing the primary Vertex AI + Workbench APIs behind the perimeter you actually need for this scenario.

###### Explanation

**Why D is correct**
To specifically prevent data exfiltration from Vertex AI training/serving and from Workbench-managed notebooks, you should enforce a VPC Service Controls (VPC SC) service perimeter around the Google APIs those products use. VPC SC is designed to mitigate data exfiltration risk by restricting where protected Google-managed resources can be accessed from, and by blocking API calls that would move data outside the perimeter (unless explicitly allowed via perimeter rules). For Vertex AI and Workbench, that means protecting the Vertex AI API and the Notebooks/Workbench API in the same perimeter so the end-to-end workflow (development in Workbench + training/serving in Vertex AI) stays inside the perimeter.

> [!note]- Why the other options are wrong
> A. Private Google Access reduces exposure by allowing access to Google APIs without public IPs, but it does not provide a policy boundary that prevents exfiltration to resources outside your trusted projects/organizations. It’s a networking path choice, not an exfiltration control.
>
> B. VPC Flow Logs help you observe and investigate traffic patterns, but they are detective controls, not preventive. They don’t stop data from leaving; they only provide telemetry after (or during) events.
>
> C. ml.googleapis.com is associated with legacy ML services (older AI Platform endpoints) rather than the Vertex AI API used for modern Vertex AI workflows, and document.googleapis.com is for Document AI (not the core Vertex AI + Workbench control plane). Even if you protected those, you wouldn’t be placing the primary Vertex AI + Workbench APIs behind the perimeter you actually need for this scenario.

</details>

---

### Exam 5 · Q67

**You are designing storage settings for a mission-critical Cloud Storage bucket that will hold trade confirmation documents for a financial services company. These records are immutable and must be retained as legal evidence. Your solution must meet these requirements:**

**• Quickly recover any object that is accidentally deleted or maliciously overwritten.

- After an object is written, no one (including admins) can delete or modify it for seven years.**

**What should you do?**

- A. Grant only the `roles/storage.objectCreator` role to the application service account and remove all other admin permissions on the bucket.
- B. Use Storage Transfer Service to run a daily replication job that syncs the bucket to a separate archival bucket in another region.
- C. Configure an Object Lifecycle Management policy to retain all objects for at least seven years before allowing deletion.
- D. Enable Object Versioning on the bucket, and also set a seven-year retention policy and apply Bucket Lock.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Enable Object Versioning on the bucket, and also set a seven-year retention policy and apply Bucket Lock.

**Correct option:** **D. Enable Object Versioning on the bucket, and also set a seven-year retention policy and apply Bucket Lock.**

**Need-to-know foundational concept**

There are two distinct needs here, and they require two different Cloud Storage controls:

1. **Fast recovery from accidental deletion or overwrite** → **Object Versioning** keeps older generations of an object so you can restore a prior version quickly.
2. **WORM-style immutability for seven years (even against admins)** → **Retention policy + Bucket Lock** enforces an unchangeable retention period so objects cannot be deleted (and the retention policy itself cannot be reduced/removed after locking).

**Cloud Storage Bucket Lock is explicitly designed for compliance retention and prevents anyone from shortening or removing the retention policy once locked.**
[https://cloud.google.com/storage/docs/bucket-lock](https://cloud.google.com/storage/docs/bucket-lock)

**Why the chosen option is correct**

- **Object Versioning** directly addresses “recover any object accidentally deleted or maliciously overwritten” by preserving previous versions (generations) that can be restored.
- **Retention policy (7 years)** ensures objects cannot be deleted until the retention duration elapses.
- **Bucket Lock** makes that retention enforcement immutable so even privileged users cannot reduce the retention period or remove the policy, matching the requirement “no one (including admins) can delete or modify it for seven years.”

**Why the other options are not the best choice**

**A. Grant only roles/storage.objectCreator and remove admin permissions**
This is an IAM hardening step, but it is not a compliance-grade immutability guarantee. Privileges can change over time (or be granted in emergencies), and IAM alone does not provide the “even admins cannot delete” enforcement required.

**B. Daily replication to another bucket**
Replication helps with durability and copies, but it does not prevent deletion/modification within the seven-year window, and it does not provide immediate recovery for overwritten objects the way versioning does.

**C. Lifecycle policy to retain objects for seven years**
Lifecycle rules automate deletion/transition actions; they do not create a WORM guarantee that prevents deletion or policy changes by admins. The requirement explicitly demands that nobody can delete or modify objects for seven years, which is what retention policy + Bucket Lock is meant to enforce.

**Final answer: D**

###### Explanation

**Correct option:** **D. Enable Object Versioning on the bucket, and also set a seven-year retention policy and apply Bucket Lock.**

**Need-to-know foundational concept**

There are two distinct needs here, and they require two different Cloud Storage controls:

1. **Fast recovery from accidental deletion or overwrite** → **Object Versioning** keeps older generations of an object so you can restore a prior version quickly.
2. **WORM-style immutability for seven years (even against admins)** → **Retention policy + Bucket Lock** enforces an unchangeable retention period so objects cannot be deleted (and the retention policy itself cannot be reduced/removed after locking).

> [!note]- Why the other options are wrong
> **A. Grant only roles/storage.objectCreator and remove admin permissions**
> This is an IAM hardening step, but it is not a compliance-grade immutability guarantee. Privileges can change over time (or be granted in emergencies), and IAM alone does not provide the “even admins cannot delete” enforcement required.
>
> **B. Daily replication to another bucket**
> Replication helps with durability and copies, but it does not prevent deletion/modification within the seven-year window, and it does not provide immediate recovery for overwritten objects the way versioning does.
>
> **C. Lifecycle policy to retain objects for seven years**
> Lifecycle rules automate deletion/transition actions; they do not create a WORM guarantee that prevents deletion or policy changes by admins. The requirement explicitly demands that nobody can delete or modify objects for seven years, which is what retention policy + Bucket Lock is meant to enforce.

</details>

---

### Exam 5 · Q68

**Your company has engaged an external audit firm for a compliance review. Internal governance requires that all external auditors be managed through a single Google Group, and that this group receive temporary, read-only access to a Cloud Storage bucket named `audit-evidence-bucket`. Access must be attributable to each auditor’s individual identity and should be enabled only for the audit period, which spans the full month of October. You need a secure approach that meets these requirements while minimizing ongoing administrative effort. What should you do?**

- A. Add an IAM binding granting `roles/storage.objectViewer` to the Google Group, and use a time-based IAM Condition so access is automatically allowed from October 1 through November 1.
- B. Create a service account with `roles/storage.objectViewer` on the bucket, then generate and share Signed URLs for the bucket objects with an expiration of November 1.
- C. Use Cloud Scheduler to trigger Cloud Run functions: one to add the `roles/storage.objectViewer` binding for the Google Group on October 1, and another to remove it on November 1.
- D. Use Workforce Identity Federation to map the auditors’ group to the Google Group, grant `roles/storage.objectViewer` to that Google Group, and set the provider session duration to one month.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Add an IAM binding granting `roles/storage.objectViewer` to the Google Group, and use a time-based IAM Condition so access is automatically allowed from October 1 through November 1.

**Correct option: A. Add an IAM binding granting `roles/storage.objectViewer` to the Google Group, and use a time-based IAM Condition so access is automatically allowed from October 1 through November 1.**

**Need-to-know foundational concept**

Use **IAM Conditions** when you need **policy-enforced, automatically expiring access** without building operational automation. A time-based condition evaluates `request.time` so access is only granted during the approved window, while still keeping access **attributable to each auditor’s individual identity** (because the auditors authenticate as themselves and are authorized via group membership).

**Authoritative reference (time-based IAM Conditions using `request.time`):**
[https://cloud.google.com/iam/docs/conditions-overview](https://cloud.google.com/iam/docs/conditions-overview)

**Why the chosen option is correct**

- Meets the “single Google Group” governance rule (group-based access).
- Ensures **read-only** access with `roles/storage.objectViewer`.
- Ensures **individual attribution** (each auditor uses their own identity; audit logs reflect the user principal, not a shared credential).
- Ensures **temporary access for October only** via a **time-based IAM Condition**, with no manual removal needed on November 1.
- Minimizes ongoing admin work (one policy change with an auto-expiry condition).

**Why the other options are not the best choice**

**B. Service account + Signed URLs**
Signed URLs do not provide durable, identity-based access control tied to the auditor’s principal in the same way group-based IAM does, and they create operational overhead (generating/managing URLs, rotating, ensuring coverage for all objects). This also weakens governance because access is effectively delegated via URLs rather than centrally controlled membership + IAM policy.

**C. Cloud Scheduler + Cloud Run to add/remove bindings**
This works, but it introduces extra moving parts (two scheduled jobs, code, permissions, monitoring, failure handling). IAM Conditions achieve the same outcome with materially less operational overhead and fewer failure modes.

**D. Workforce Identity Federation with one-month session duration**
This is for federating external identities into Google Cloud, but your governance requirement already states auditors must be managed through a **single Google Group**. Also, session duration is not the right control for “access allowed only in October” at the bucket policy layer; the correct control is an IAM policy condition with an explicit time window.

**Final answer: A**

###### Explanation

**Correct option: A. Add an IAM binding granting `roles/storage.objectViewer` to the Google Group, and use a time-based IAM Condition so access is automatically allowed from October 1 through November 1.**

**Why the chosen option is correct**

- Meets the “single Google Group” governance rule (group-based access).
- Ensures **read-only** access with `roles/storage.objectViewer`.
- Ensures **individual attribution** (each auditor uses their own identity; audit logs reflect the user principal, not a shared credential).
- Ensures **temporary access for October only** via a **time-based IAM Condition**, with no manual removal needed on November 1.

> [!note]- Why the other options are wrong
> **B. Service account + Signed URLs**
> Signed URLs do not provide durable, identity-based access control tied to the auditor’s principal in the same way group-based IAM does, and they create operational overhead (generating/managing URLs, rotating, ensuring coverage for all objects). This also weakens governance because access is effectively delegated via URLs rather than centrally controlled membership + IAM policy.
>
> **C. Cloud Scheduler + Cloud Run to add/remove bindings**
> This works, but it introduces extra moving parts (two scheduled jobs, code, permissions, monitoring, failure handling). IAM Conditions achieve the same outcome with materially less operational overhead and fewer failure modes.
>
> **D. Workforce Identity Federation with one-month session duration**
> This is for federating external identities into Google Cloud, but your governance requirement already states auditors must be managed through a **single Google Group**. Also, session duration is not the right control for “access allowed only in October” at the bucket policy layer; the correct control is an IAM policy condition with an explicit time window.

</details>

---

### Exam 5 · Q70

**You are deploying a highly sensitive data processing workload on Google Cloud. Company compliance rules require that all encryption keys for data at rest must be generated and stored only inside a certified Hardware Security Module (HSM). You want to rely on a fully managed Google Cloud service to manage the lifecycle and usage of these keys. What should you do?**

- A. Use Customer-Supplied Encryption Keys (CSEK) by sending your on-premises generated key with each API request.
- B. Import key material from your on-premises HSM into a Cloud KMS key that uses SOFTWARE protection.
- C. Create a Cloud KMS key with the HSM protection level and generate the key inside Google’s HSM infrastructure.
- D. Configure Cloud External Key Manager (Cloud EKM) to link Google Cloud to your on-premises HSM.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a Cloud KMS key with the HSM protection level and generate the key inside Google’s HSM infrastructure.

**Correct option: C. Create a Cloud KMS key with the HSM protection level and generate the key inside Google’s HSM infrastructure.**

**Need-to-know foundational concept**

The requirement is:

Keys must be generated and stored *only inside a certified HSM*
Lifecycle must be handled by a *fully managed Google service*

That maps directly to **Cloud KMS with HSM protection level**.

Cloud KMS HSM keys:

- are generated **inside FIPS 140-2 Level 3 validated HSMs**
- never leave the HSM boundary in plaintext
- are lifecycle-managed by Google
- support rotation, IAM control, audit logging
- meet strict compliance requirements

**Authoritative reference:**
[https://cloud.google.com/kms/docs/hsm](https://cloud.google.com/kms/docs/hsm)

**Why the correct option fits the scenario**

**Option C satisfies every constraint:**

- keys generated inside certified HSM
- keys stored inside HSM only
- lifecycle managed by Google
- no customer-managed hardware
- minimal operational burden
- compliance-ready

This is the exact use case Cloud KMS HSM exists for.

**Why the other options are not the best choice**

**A. Customer-Supplied Encryption Keys (CSEK)**
Keys are generated outside Google and sent with API calls. Google does not manage lifecycle. This violates the requirement to rely on a managed key lifecycle.

**B. Import into SOFTWARE protection**
Software keys are not HSM-backed. This fails the compliance rule.

**D. Cloud EKM**
Cloud EKM keeps keys in your external HSM, not inside Google’s managed HSM. The requirement explicitly asks for a fully managed Google Cloud service managing the key lifecycle.

Exam principle:

If compliance requires HSM-backed keys managed by Google → Cloud KMS HSM.

**Final answer: C**

###### Explanation

**Why the correct option fits the scenario**

**Option C satisfies every constraint:**

- keys generated inside certified HSM
- keys stored inside HSM only
- lifecycle managed by Google
- no customer-managed hardware
- minimal operational burden
- compliance-ready

This is the exact use case Cloud KMS HSM exists for.

> [!note]- Why the other options are wrong
> **A. Customer-Supplied Encryption Keys (CSEK)**
> Keys are generated outside Google and sent with API calls. Google does not manage lifecycle. This violates the requirement to rely on a managed key lifecycle.
>
> **B. Import into SOFTWARE protection**
> Software keys are not HSM-backed. This fails the compliance rule.
>
> **D. Cloud EKM**
> Cloud EKM keeps keys in your external HSM, not inside Google’s managed HSM. The requirement explicitly asks for a fully managed Google Cloud service managing the key lifecycle.

</details>

---

### Exam 5 · Q78

**A large multinational enterprise is moving to Google Cloud. It has multiple business units: Finance, Marketing, and Research & Development (R&D). The central security team has defined the following governance requirements:**

**• Finance: Must be limited to deploying resources only in approved regions (us-central1 and europe-west2). Access to Finance projects must be tightly managed through a dedicated finance-admins Google Group.

- Marketing: Requires separate production and development environments, with different teams responsible for each environment.
- R&D: Needs maximum freedom to experiment with new services, but must be fully isolated so it cannot affect any production workloads.
- Global Auditing: A central compliance team needs read-only visibility into all resources across the entire organization for audit purposes.**

**You must design a scalable resource hierarchy that enforces these policies in line with Google Cloud Well-Architected guidance while providing appropriate autonomy to each business unit. What should you do?**

- A. Create a folder per business unit under the Organization root. Apply a Resource Location Restriction organization policy on the Finance folder. Under the Marketing folder, create separate projects for mktg-prod and mktg-dev. Grant the compliance team the roles/viewer role at the Organization level.
- B. Put all projects directly under the Organization node. Use network tags and service accounts to enforce separation between business units. Apply the Resource Location Restriction policy only on the Finance project.
- C. Create a separate Google Cloud Organization for each business unit (Finance, Marketing, and R&D). Grant the compliance team roles/viewer in each organization.
- D. Create one project per business unit. Apply the Resource Location Restriction policy directly on the Finance project. Grant the compliance team roles/browser on each project individually.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Create a folder per business unit under the Organization root. Apply a Resource Location Restriction organization policy on the Finance folder. Under the Marketing folder, create separate projects for mktg-prod and mktg-dev. Grant the compliance team the roles/viewer role at the Organization level.

**Correct option: A**

**Need-to-know foundational concept**

Google Cloud governance at enterprise scale is enforced through the **resource hierarchy**:

Organization → Folders → Projects

Folders are the primary unit for **policy boundaries**, IAM delegation, and organizational autonomy. Organization policies and IAM inheritance flow downward, which lets you enforce guardrails once and scale safely. This is the exact pattern Google recommends for multi-business-unit enterprises.

**Resource hierarchy overview:**
[https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

**Organization Policy constraints (including location restriction):**
[https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)

**Why option A is correct**

Option A builds a clean, scalable hierarchy aligned with governance:

- **Folder per business unit** = policy boundary + autonomy
- Finance folder → apply region restriction once, inherited by all Finance projects
- Marketing folder → separate prod/dev projects under same governance domain
- R&D folder → isolated experimentation space
- Compliance team → org-level read-only visibility across everything

This design:

- scales as new projects are added
- centralizes guardrails
- preserves BU autonomy
- avoids policy duplication
- supports least privilege
- matches Google enterprise architecture guidance

It uses folders exactly as intended: governance domains.

**Why the other options are not the best choice**

**B. All projects under the org root**
No governance boundaries. Policies would need to be applied project-by-project and won’t scale. Network tags do not replace org-level governance.

**C. Separate organizations per BU**
Breaks centralized governance and auditing. The compliance team cannot manage policy uniformly. This adds unnecessary complexity and fragments identity/security.

**D. One project per BU**
Too coarse. Marketing explicitly needs prod/dev separation. Also, granting compliance visibility project-by-project is not scalable.

Exam principle:

Enterprise governance = folders as policy domains, org-level auditing, inherited constraints.

**Final answer: A**

###### Explanation

**Correct option: A**

**Need-to-know foundational concept**

Google Cloud governance at enterprise scale is enforced through the **resource hierarchy**:

Organization → Folders → Projects

Folders are the primary unit for **policy boundaries**, IAM delegation, and organizational autonomy. Organization policies and IAM inheritance flow downward, which lets you enforce guardrails once and scale safely. This is the exact pattern Google recommends for multi-business-unit enterprises.

**Why option A is correct**

Option A builds a clean, scalable hierarchy aligned with governance:

- **Folder per business unit** = policy boundary + autonomy
- Finance folder → apply region restriction once, inherited by all Finance projects
- Marketing folder → separate prod/dev projects under same governance domain
- R&D folder → isolated experimentation space
- Compliance team → org-level read-only visibility across everything

This design:

- scales as new projects are added
- centralizes guardrails
- preserves BU autonomy
- avoids policy duplication
- supports least privilege
- matches Google enterprise architecture guidance

> [!note]- Why the other options are wrong
> **B. All projects under the org root**
> No governance boundaries. Policies would need to be applied project-by-project and won’t scale. Network tags do not replace org-level governance.
>
> **C. Separate organizations per BU**
> Breaks centralized governance and auditing. The compliance team cannot manage policy uniformly. This adds unnecessary complexity and fragments identity/security.
>
> **D. One project per BU**
> Too coarse. Marketing explicitly needs prod/dev separation. Also, granting compliance visibility project-by-project is not scalable.

</details>

---

### Exam 5 · Q83

**Your company is quickly rolling out containerized microservices on Google Kubernetes Engine (GKE) through an automated CI/CD pipeline. Security is critical, and you must prevent vulnerable container images from reaching the production cluster. What should you do? (Choose two.)**

- A. Manually review the Artifact Analysis security reports for each container image before deploying to GKE.
- B. Add vulnerability scanning before image builds and standardize on Google-maintained base images.
- C. Enable Artifact Analysis and block deployments whenever critical vulnerabilities are detected.
- D. Embed a custom security policy inside the container image to limit network ports and resource access.
- E. Enable Shielded GKE Nodes so the cluster automatically prevents execution of vulnerable images.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Add vulnerability scanning before image builds and standardize on Google-maintained base images. **|** C. Enable Artifact Analysis and block deployments whenever critical vulnerabilities are detected.

**Correct options: B and C**

**Need-to-know foundational concept**

This question is about **container supply chain security**, not runtime hardening.

Google’s recommended approach is:

Detect vulnerabilities early and enforce policy automatically in CI/CD.

The pipeline should both **reduce the chance of introducing vulnerabilities** and **block vulnerable artifacts from promotion**. Artifact Analysis (Container Scanning) integrates with CI/CD to scan images and supports policy-based deployment blocking.

**Artifact Analysis vulnerability scanning overview:**
[https://cloud.google.com/artifact-analysis/docs/container-scanning-overview](https://cloud.google.com/artifact-analysis/docs/container-scanning-overview)

**Why the correct options fit the scenario**

**B. Add vulnerability scanning before image builds and standardize on Google-maintained base images.**
This reduces risk at the source. Google-maintained base images are regularly patched and scanned, lowering the attack surface. Scanning early shifts security left into the pipeline.

**C. Enable Artifact Analysis and block deployments whenever critical vulnerabilities are detected.**
This enforces automated policy. Vulnerable images never reach production because the pipeline rejects them. This is the key governance control.

Together they implement:

- prevention (secure base images)
- detection (scanning)
- enforcement (deployment blocking)

That is a full secure supply-chain workflow.

**Why the other options are not the best choice**

**A. Manual review**
Does not scale and introduces human error. The requirement is automated CI/CD protection.

**D. Custom security policy inside images**
Runtime hardening is good, but it does not prevent vulnerable images from being deployed.

**E. Shielded GKE Nodes**
Protects node integrity, not container image vulnerability gating.

Exam principle:

Secure container pipeline = scan + enforce automatically.

Final answer: **B and C**

###### Explanation

**B. Add vulnerability scanning before image builds and standardize on Google-maintained base images.**
This reduces risk at the source. Google-maintained base images are regularly patched and scanned, lowering the attack surface. Scanning early shifts security left into the pipeline.

**C. Enable Artifact Analysis and block deployments whenever critical vulnerabilities are detected.**
This enforces automated policy. Vulnerable images never reach production because the pipeline rejects them. This is the key governance control.

Together they implement:

- prevention (secure base images)
- detection (scanning)
- enforcement (deployment blocking)

> [!note]- Why the other options are wrong
> **A. Manual review**
> Does not scale and introduces human error. The requirement is automated CI/CD protection.
>
> **D. Custom security policy inside images**
> Runtime hardening is good, but it does not prevent vulnerable images from being deployed.
>
> **E. Shielded GKE Nodes**
> Protects node integrity, not container image vulnerability gating.

</details>

---

### Exam 5 · Q84

**Your organization is deploying a new cloud-native application on Google Cloud and must demonstrate alignment with the ISO/IEC 27001 framework. You want to use Google Cloud’s official compliance reports and documentation to support your audit preparation. What should you do?**

- A. Hire an external auditor to perform an ISO/IEC 27001 audit of your Google Cloud deployment.
- B. Search the internet and download an ISO/IEC 27001 report for Google Cloud.
- C. Use Compliance Reports Manager to review ISO/IEC 27001 materials and access the official documentation available through your Google Cloud account.
- D. Use Cloud Audit Logs to obtain ISO/IEC 27001 compliance reports.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use Compliance Reports Manager to review ISO/IEC 27001 materials and access the official documentation available through your Google Cloud account.

**Correct option: C. Use Compliance Reports Manager to review ISO/IEC 27001 materials and access the official documentation available through your Google Cloud account.**

**Need-to-know foundational concept**

Google Cloud provides official third-party audit attestations (like ISO/IEC 27001) through a controlled portal so customers can use them for compliance evidence. The correct way to obtain these documents is **Compliance Reports Manager**, which gives authenticated access to Google’s certified audit reports and supporting compliance materials. This ensures you’re using authoritative, up-to-date documentation directly from Google.

**Authoritative reference:**
[https://cloud.google.com/security/compliance/compliance-reports-manager](https://cloud.google.com/security/compliance/compliance-reports-manager)

**Why the chosen option is correct**

- Provides official ISO/IEC 27001 audit artifacts
- Authenticated and governed access
- Designed specifically for audit preparation
- Maintained by Google
- Recognized compliance evidence

This is the only option that retrieves **official compliance documentation** through a supported channel.

**Why the other options are not the best choice**

**A. Hire an external auditor**
Useful for your own environment assessment, but the question asks for Google’s official compliance reports, not a custom audit.

**B. Download from the internet**
Not authoritative and potentially outdated. Compliance evidence must come from trusted sources.

**D. Cloud Audit Logs**
Audit logs record activity in your environment; they are not ISO compliance certifications or audit reports.

Final answer: **C**

###### Explanation

**Correct option: C. Use Compliance Reports Manager to review ISO/IEC 27001 materials and access the official documentation available through your Google Cloud account.**

**Need-to-know foundational concept**

Google Cloud provides official third-party audit attestations (like ISO/IEC 27001) through a controlled portal so customers can use them for compliance evidence. The correct way to obtain these documents is **Compliance Reports Manager**, which gives authenticated access to Google’s certified audit reports and supporting compliance materials. This ensures you’re using authoritative, up-to-date documentation directly from Google.

**Why the chosen option is correct**

- Provides official ISO/IEC 27001 audit artifacts
- Authenticated and governed access
- Designed specifically for audit preparation
- Maintained by Google
- Recognized compliance evidence

> [!note]- Why the other options are wrong
> **A. Hire an external auditor**
> Useful for your own environment assessment, but the question asks for Google’s official compliance reports, not a custom audit.
>
> **B. Download from the internet**
> Not authoritative and potentially outdated. Compliance evidence must come from trusted sources.
>
> **D. Cloud Audit Logs**
> Audit logs record activity in your environment; they are not ISO compliance certifications or audit reports.

</details>

---
