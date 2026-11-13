# Domain 2 — Building and Testing Applications

49 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q1

**What approach should you take to implement a custom step in Cloud Build that ensures a copyright comment is present at the beginning of all source files, triggered by each source commit, and adds one if it's missing?**

- II. Develop a new Docker container to inspect files in /workspace, validating and appending a copyright comment to each source file. There's no requirement to commit the modified files back to the source repository.
- IV. Develop a new Docker container to inspect files in a Cloud Storage bucket, validating and appending a copyright comment to each source file. Modified files are explicitly committed back to the source repository.
- I. Develop a new Docker container to analyze files in /workspace, verifying and adding a copyright comment to each source file. Any modified files are directly committed back to the source repository.
- III. Develop a new Docker container to inspect files in a Cloud Storage bucket, verifying and appending a copyright comment to each source file. Any changed files are written back to the Cloud Storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Develop a new Docker container to analyze files in /workspace, verifying and adding a copyright comment to each source file. Any modified files are directly committed back to the source repository.

**I. Develop a new Docker container to analyze files in /workspace, verifying and adding a copyright comment to each source file. Any modified files are directly committed back to the source repository.**

Here's why this stands out:

  * **Integration with Source Control:** Directly committing changes back to the repository ensures the copyright comment exists in the canonical source code, simplifying collaboration and preventing future inconsistencies.

  * **/workspace Context:** Cloud Build provides the `/workspace` directory, which contains the current state of your source repository. This aligns seamlessly with your Docker container's file analysis.

  * **Trigger Efficiency:** Triggering the build step on each source commit guarantees that the copyright comment is always present.

**Why other options are less ideal:**

  * **II. No Commit:** Without committing changes, your source code wouldn't reflect the updated copyright comments, leading to potential inaccuracies.

  * **III & IV. Cloud Storage Bucket:** While you could temporarily use a Cloud Storage bucket, it introduces unnecessary overhead compared to the direct `/workspace` approach and potential syncing complications if multiple builds run concurrently.

References:

<https://cloud.google.com/build/docs/configuring-builds/pass-data-between-steps#passing_data_using_workspaces>

</details>

---

### Exam 1 · Q3

**How should you set up the unit testing process for Cloud Function code stored in a Cloud Source Repositories repository, ensuring deployment only occurs after passing the tests?**

- IV. Utilize Cloud Build to perform unit tests, employing the specific service account for building; upon test success, Cloud Build automatically deploys the Cloud Function.
- I. Set up Cloud Build to handle Cloud Function deployment, with deployment approval triggered after passing tests.
- III. Implement Cloud Build to execute unit tests; upon successful testing, developers can proceed with Cloud Function deployment.
- II. Employ Cloud Build for deploying the Cloud Function, utilizing the specific service account for the build process, and executing unit tests post-deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Cloud Build to perform unit tests, employing the specific service account for building; upon test success, Cloud Build automatically deploys the Cloud Function.

**The correct option is**

**IV: Utilize Cloud Build to perform unit tests, employing the specific service account for building; upon test success, Cloud Build automatically deploys the Cloud Function.**

**Here's why:**

  * **Automation & Efficiency:** This option streamlines testing and deployment into a single integrated process, saving time and effort.

  * **Enforced Testing:** Guarantees code quality because deployment happens _only_ after tests pass. This is critical for preventing broken code from reaching production.

  * **Cloud Build:** This Google Cloud service is ideal for building, testing, and deploying cloud-native applications, including Cloud Functions.

  * **Service Account:** Using a specific service account with deployment permissions ensures controlled access and security.

**Here's why the other options aren't as suitable:**

  * **I. Set up Cloud Build to handle Cloud Function deployment, with deployment approval triggered after passing tests.** While correct in ensuring that tests run, this option introduces a manual approval step. This can slow down deployment and might be unnecessary in many scenarios.

  * **II. Employ Cloud Build for deploying the Cloud Function, utilizing the specific service account for the build process, and executing unit tests post-deployment.** This approach is problematic because it deploys potentially untested code. Executing tests after deployment could reveal issues, necessitating rollbacks and adding complexity.

  * **III. Implement Cloud Build to execute unit tests; upon successful testing, developers can proceed with Cloud Function deployment.** This option places the deployment burden on developers and is less efficient than automated deployment through Cloud Build. It risks inconsistent deployment procedures as different developers handle this step.

</details>

---

### Exam 1 · Q6

**You are preparing to deploy a microservices application on Google Kubernetes Engine (GKE) that will undergo daily updates. With a large number of distinct containers running on the Linux operating system (OS), you aim to stay informed about any known OS vulnerabilities in the new containers. Prioritizing Google's recommended best practices, what is the most suitable approach for achieving this?**

- III. Enable Container Analysis, store new container images in Artifact Registry, and specifically review critical vulnerability results before each deployment.
- IV. Utilize the Container Analysis REST API to invoke Container Analysis for scanning new container images, then review the vulnerability results before each deployment.
- II. Enable Container Analysis and store new container images in Artifact Registry, subsequently reviewing the vulnerability results before each deployment.
- I. Utilize the gcloud CLI to invoke Container Analysis for scanning new container images and review the vulnerability results before each deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Enable Container Analysis and store new container images in Artifact Registry, subsequently reviewing the vulnerability results before each deployment.

**II. Enable Container Analysis and store new container images in Artifact Registry, subsequently reviewing the vulnerability results before each deployment.**

Explanation:

Option II is the most suitable approach for achieving the goal of staying informed about any known OS vulnerabilities in the new containers while prioritizing Google's recommended best practices. Here's why:

  * **Enable Container Analysis** : By enabling Container Analysis, you ensure that each container image pushed to Artifact Registry is automatically scanned for vulnerabilities. This allows you to proactively identify any potential security issues.

  * **Store new container images in Artifact Registry** : Storing container images in Artifact Registry provides a centralized location for managing and storing your images securely. It integrates seamlessly with Container Analysis, allowing vulnerability scanning to be performed automatically on each image upload.

  * **Review the vulnerability results before each deployment** : Before deploying a new container image, it's crucial to review the vulnerability results generated by Container Analysis. This ensures that you are aware of any known vulnerabilities present in the image and can take appropriate actions, such as patching or updating dependencies, before deployment.

**Options I, III, and IV also involve utilizing Container Analysis for scanning container images, but they either lack the integration with Artifact Registry (option I) or do not emphasize the importance of reviewing vulnerability results before each deployment (options III and IV).**

**Therefore, option II aligns with Google's recommended best practices and provides a comprehensive approach to staying informed about OS vulnerabilities in container images before deployment on Google Kubernetes Engine (GKE).**

**Reference:**

[https://cloud.google.com/artifact-registry/docs/analysis ](https://cloud.google.com/artifact-registry/docs/analysis)

</details>

---

### Exam 1 · Q7

**Considering the scenario of configuring a continuous integration pipeline using Cloud Build to automate container image builds, which optimization can be implemented based on the provided code segment? Choose two options.**

FROM python:3.7-alpine 

COPY . /app WORKDIR /app 

RUN pip install -r requirements.txt 

CMD ["gunicorn", "-w 4", "main:app"]

- E. Store the application's source code on Cloud Storage and configure the pipeline to download it using gsutil.
- A. Opt for a larger virtual machine (VM) size with increased CPU capacity for Cloud Build operations.
- B. Establish a Container Registry on a Compute Engine VM within a Virtual Private Cloud (VPC) to store final images.
- C. Employ caching for container images in subsequent builds using the --cache-from argument in the build configuration file.
- D. Adjust the base image in the build file to ubuntu:latest and install Python 3.7 using a package manager.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Opt for a larger virtual machine (VM) size with increased CPU capacity for Cloud Build operations. **|** C. Employ caching for container images in subsequent builds using the --cache-from argument in the build configuration file.

Correct answer

**A. Opt for a larger virtual machine (VM) size with increased CPU capacity for Cloud Build operations.**

**C. Employ caching for container images in subsequent builds using the --cache-from argument in the build configuration file.**

_A is correct because a high-CPU virtual machine type can increase the speed of your build.  
B is not correct because a Container Registry on a VM will not speed up the build.  
C is correct because the same container is used in subsequent steps for testing and to be pushed to the registry.  
D is not correct because an ubuntu container image will be significantly larger than the python:3.7-alpine image.  
E is not correct because storing the application source code on Cloud Storage does not decrease the time to build the application._

**References:**

[https://cloud.google.com/cloud-build/docs/speeding-up-builds](%0d https:/cloud.google.com/cloud-build/docs/speeding-up-builds%0d)

[https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds](%0d https:/cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds%0d)

</details>

---

### Exam 1 · Q9

**You've recently launched a new service on Cloud Run, which authenticates via a custom service and records transactional data in a Cloud Spanner database. Your aim is to validate the application's capability to handle up to 5,000 read and 1,000 write transactions per second while pinpointing any bottlenecks. Additionally, your testing setup should be able to autoscale. What's the optimal approach?**

- I. Develop a testing framework to generate requests and deploy it on Cloud Run. Analyze VPC Flow Logs using Cloud Logging.
- II. Set up a Google Kubernetes Engine cluster with Locust or JMeter images to dynamically generate load tests. Analyze outcomes with Cloud Trace.
- IV. Deploy a Compute Engine instance with a LAMP stack image from the Marketplace. Utilize Apache Bench for load testing against the service. Analyze findings with Cloud Trace.
- III. Use Cloud Tasks to generate a test load. Schedule 60,000 Cloud Task transactions per minute for 10 minutes using Cloud Scheduler. Review results via Cloud Monitoring.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Set up a Google Kubernetes Engine cluster with Locust or JMeter images to dynamically generate load tests. Analyze outcomes with Cloud Trace.

**II. Set up a Google Kubernetes Engine cluster with Locust or JMeter images to dynamically generate load tests. Analyze outcomes with Cloud Trace.**

**Justification:**

  * **Suitable Load Testing Tools:** Locust and JMeter are industry-standard load testing tools designed specifically to simulate heavy user traffic and stress test systems. They offer flexibility for defining custom request patterns and simulating realistic user behavior.

  * **Scalability with Kubernetes:** GKE provides scalable and self-healing infrastructure for running load testing tools. You can spin up multiple instances of JMeter or Locust pods as needed to achieve the desired load of 5,000 read/1,000 write requests per second.

  * **In-depth Tracing with Cloud Trace:** Cloud Trace integrates seamlessly with Cloud Run and Cloud Spanner. It provides detailed visibility into request latencies, error rates, and spans, allowing you to pinpoint bottlenecks at different layers of your system.

**Why Other Options Are Less Ideal:**

  * **I. Develop a testing framework to generate requests and deploy it on Cloud Run. Analyze VPC Flow Logs using Cloud Logging.** Cloud Run can scale during the tests, but building your own framework would be time-consuming. VPC Flow Logs don't provide the granular telemetry needed to identify bottlenecks.

  * **III. Use Cloud Tasks to generate a test load. Schedule 60,000 Cloud Task transactions per minute for 10 minutes using Cloud Scheduler. Review results via Cloud Monitoring.** While Cloud Tasks can generate load, they are not specialized load testing tools and lack the flexibility to customize request patterns. Cloud Monitoring on its own may not uncover performance bottlenecks.

  * **IV. Deploy a Compute Engine instance with a LAMP stack image from the Marketplace. Utilize Apache Bench for load testing against the service. Analyze findings with Cloud Trace.** Deploying and managing a Compute Engine instance for load testing adds overhead. Apache Bench is not as advanced as Locust or JMeter in terms of customizability.

References:

<https://cloud.google.com/architecture/distributed-load-testing-using-gke>

</details>

---

### Exam 1 · Q20

**You want to assess the security vulnerabilities of an application running on App Engine. Which service should you use for this purpose?**

- I. Cloud Armor
- IV. Stackdriver Error Reporting
- II. Stackdriver Debugger
- III. Cloud Security Scanner

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Cloud Security Scanner

**III. Cloud Security Scanner**

Here's why it's the right choice:

  * **Vulnerability Scanning:** Cloud Security Scanner is designed specifically to scan web applications for common vulnerabilities like cross-site scripting (XSS), SQL injection, and outdated libraries.

  * **App Engine Integration:** It seamlessly integrates with App Engine, making it easy to scan your deployed application.

  * **Actionable Reports:** Cloud Security Scanner provides detailed reports on discovered vulnerabilities, along with recommendations for remediation.

**Why Other Options Are Less Ideal:**

  * **I. Cloud Armor** Cloud Armor is a web application firewall (WAF) primarily focused on mitigating DDoS attacks and enforcing IP-based allow/deny lists. While it enhances security, it doesn't directly scan for application-level vulnerabilities.

  * **II. Stackdriver Debugger** Debugger helps inspect an application's state in production for troubleshooting errors, but doesn't have a security focus.

  * **IV. Stackdriver Error Reporting** Error Reporting aids in error analysis, but may indirectly reveal consequences of an exploit rather than identifying the vulnerability itself.

**References:**

[https://cloud.google.com/appengine/docs/standard/python/application-security:](https://cloud.google.com/appengine/docs/standard/python/application-security:  https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)

[https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview](https://cloud.google.com/appengine/docs/standard/python/application-security:  https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)

</details>

---

### Exam 1 · Q28

**You've recently launched a Go application on Google Kubernetes Engine (GKE). The operations team has observed high CPU usage even during periods of low production traffic. They've requested you to optimize the application's CPU resource consumption. To identify which Go functions are consuming the most CPU, what action should you take?**

- III. Access your GKE nodes via SSH. Execute the top command in the shell to extract the CPU utilization of your application.
- II. Develop a customized dashboard in Cloud Monitoring to assess the CPU performance metrics of your application.
- IV. Adjust your Go application to gather profiling data. Evaluate the CPU metrics of your application using flame graphs in Profiler.
- I. Implement a Fluent Bit daemonset on the GKE cluster for logging data in Cloud Logging. Analyze the logs to gain insights into your application code's performance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Adjust your Go application to gather profiling data. Evaluate the CPU metrics of your application using flame graphs in Profiler.

The most suitable option is 

**IV. Adjust your Go application to gather profiling data. Evaluate the CPU metrics of your application using flame graphs in Profiler.**

**Here's why:**

  * **Profiling provides function-level granularity:** Profiling tools in Go allow pinpointing the exact functions within your application that consume the most CPU resources. This level of detail is crucial for focused optimization efforts.

**Here's why the other options aren't as suitable:**

  * **I. Logs** Logs might indicate performance issues, but they won't directly reveal which functions are consuming the most CPU time. Analyzing logs for this purpose can be cumbersome and indirect.

  * **II. Cloud Monitoring dashboards** Dashboards provide a high-level overview of CPU usage but don't offer the function-level detail needed to pinpoint the root cause of high CPU usage.

  * **III. SSH and top** The `top` command provides real-time process-level CPU usage but lacks the fine-grained analysis that profiling provides for pinpointing the most CPU-intensive functions within your Go application's code.

Ref:

<https://cloud.google.com/profiler/docs>

</details>

---

### Exam 1 · Q33

**Your application exhibits significantly slower performance after deployment to a Compute Engine instance, despite performing well during local testing. What is the recommended course of action to diagnose the issue?**

- II. Utilize Cloud Debugger snapshots to examine a specific moment in the application's execution.
- III. Employ Cloud Profiler to identify the functions within the application consuming the most time.
- IV. Integrate logging commands within the application code and leverage Cloud Logging to pinpoint the source of latency issues.
- I. Submit a ticket to Cloud Support, highlighting the contrast in performance between local testing and deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Employ Cloud Profiler to identify the functions within the application consuming the most time.

**III. Employ Cloud Profiler to identify the functions within the application consuming the most time.**

Why Profiling is the First Line of Defense:

  * **Pinpointing Bottlenecks:** Cloud Profiler excels at identifying performance-intensive areas within your code. This quickly focuses your investigation on the root cause, rather than just symptoms.

  * **Low Overhead:** It often works with minimal code changes. Profiling production environments gives the most realistic performance picture.

  * **Targeted Troubleshooting:** Knowing which functions are slow helps you determine _why_ they're slow (e.g., network calls, suboptimal algorithms, resource constraints on the VM).

When Other Options Become Relevant:

  * **II. Utilize Cloud Debugger snapshots ...** Debugger is great if you suspect the issue is related to incorrect application state or logic at specific points, but less likely to be the first step for _general_ slowness.

  * **IV. Integrate logging ... Cloud Logging ...** Logging is always useful, but if the core issue is a slow function, logs might show you the consequence of that (long requests), not the cause within the code itself.

  * **I. Submit a ticket to Cloud Support ...** Support can be helpful if the issue seems related to the underlying infrastructure (VM, network, etc.), but it's a good idea to gather performance data from your application first.

</details>

---

### Exam 1 · Q40

**Your company's development teams wish to employ Cloud Build in their projects to build and push Docker images to Container Registry. However, the operations team mandates that all Docker images must be published to a centralized and securely managed Docker registry they oversee. What's the best approach to address this requirement?**

- II. Create a dedicated project for the operations team, equipped with Container Registry. Grant appropriate permissions to the Cloud Build service account in each developer team's project to enable access to the operations team's registry.
- III. Set up a separate project for the operations team, integrating Container Registry. Generate a Service Account for each development team and allocate necessary permissions to access the operations team's registry. Store the service account key file in the source code repository for authentication against the registry.
- I. Establish Container Registry within each development team's project. Configure Cloud Build builds to push Docker images to the respective project's registry. Provide the operations team access to each team's registry.
- IV. Deploy an open-source Docker Registry on a Compute Engine virtual machine instance within a distinct project for the operations team. Assign each development team a unique username and password, storing these credentials in the source code repository for authentication against the operations team's Docker registry.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Create a dedicated project for the operations team, equipped with Container Registry. Grant appropriate permissions to the Cloud Build service account in each developer team's project to enable access to the operations team's registry.

**II. Create a dedicated project for the operations team, equipped with Container Registry. Grant appropriate permissions to the Cloud Build service account in each developer team's project to enable access to the operations team's registry.**

Here's why this approach excels:

  * **Centralization:** A single registry under the operations team's control provides a unified location for managing and governing Docker images.

  * **Security:** IAM permissions ensure fine-grained access control to the centralized registry, aligning with operational security requirements.

  * **Service Accounts:** Using the Cloud Build service account for authentication is streamlined and avoids the security risks of storing credentials in source code repositories.

  * **Maintainability:** Simplifies the setup and reduces complexity for development teams.

**Why Other Options Are Less Ideal:**

  * **I. Establish Container Registry within each development team's project ...** This creates management overhead for the operations team, who would have to maintain access to numerous registries.

  * **III. ... Generate a Service Account for each development team ...** Storing the key file in the repository is a significant security risk and creates more management complexity.

  * **IV. Deploy an open-source Docker Registry on a Compute Engine virtual machine instance ...** This increases operational overhead compared to using a managed service like Container Registry and introduces additional security considerations in self-managing a registry.

</details>

---

### Exam 1 · Q45

**As the sole developer available over the weekend, your manager tasks you with making an emergency update to a website for your startup's web development team. Your development environment relies on Google Cloud services like Cloud Storage and Cloud Build, with version control managed through Git. Without your work laptop, you cannot store source code locally on a non-corporate computer. How should you configure your developer environment?**

- IV. Store the necessary source code in a Cloud Storage bucket. Mount the bucket as a drive on a public computer and use a code editor to make the required updates. Enable versioning for the bucket and link it to the team's Git repository.
- I. Utilize a text editor and Git command line to submit source code updates as pull requests from a public computer.
- II. Employ a text editor and Git command line to submit source code updates as pull requests from a virtual machine running on a public computer.
- III. Utilize Cloud Shell and its built-in code editor for development tasks, sending source code updates as pull requests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Utilize Cloud Shell and its built-in code editor for development tasks, sending source code updates as pull requests.

**III. Utilize Cloud Shell and its built-in code editor for development tasks, sending source code updates as pull requests.**

Here's why this is the best choice:

  * **Accessibility:** Cloud Shell is readily available from any modern web browser, eliminating the need to install software locally.

  * **Cloud Integration:** Cloud Shell provides integrated access to your GCP project's resources, including Cloud Storage, Cloud Build, and your Git repository.

  * **Security:** Your code stays within the secure Google Cloud environment. You don't risk storing sensitive source code on a public computer.

  * **Familiar Tools:** Cloud Shell's code editor and command-line tools provide a familiar development experience.

**Why other options have issues:**

  * **I. Public Computer (Basic Text Editor + Git):**

    * **Security Risk:** Storing or cloning the project on a public computer compromises the security of your source code.

    * **Limited Tools:** Basic text editors may lack the features you need for effective development.

  * **II. Public Computer (VM + Text Editor + Git):**

    * **Complexity:** Requires setting up a VM, which adds overhead and time pressure to your task.

    * **Security Risk:** Still introduces the security concerns of storing code on a public machine.

  * **IV. Cloud Storage Mount with Versioning:**

    * **Not ideal for Git:** While versioning helps, managing a Git project this way is cumbersome and prone to errors.

    * **Local Editing:** Still requires a capable code editor on the public computer.

**Reference:**

<https://cloud.google.com/shell/docs>

</details>

---

### Exam 1 · Q49

**To efficiently scan container images for Common Vulnerabilities and Exposures (CVEs) without impeding software development agility using managed services, which approach should you take?**

- A. Activate the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry, enabling seamless integration of vulnerability scanning into the container image management workflow.
- D. Utilize Cloud Monitoring to evaluate the outcomes of Cloud Build and identify if a vulnerable version has been utilized, which may provide insights into potential vulnerabilities but does not offer direct vulnerability scanning of container images.
- C. Restrict the usage of non-commercially supported base images within your development environment, which is a proactive measure but does not address the need for automated vulnerability scanning.
- B. Establish a Cloud Run service triggered by code check-ins to scan the code for CVEs, which may offer continuous monitoring but might not directly address vulnerabilities within container images.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Activate the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry, enabling seamless integration of vulnerability scanning into the container image management workflow.

The most efficient approach to scan container images for Common Vulnerabilities and Exposures (CVEs) without impeding software development agility using managed services is:

**A. Activate the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry, enabling seamless integration of vulnerability scanning into the container image management workflow.**

Explanation:

  * Option A suggests activating the Container Analysis API to conduct vulnerability scans on images stored in Artifact Registry. This approach directly addresses the need for automated vulnerability scanning of container images within the container image management workflow. It seamlessly integrates vulnerability scanning without impeding software development agility.

  * Option B involves establishing a Cloud Run service triggered by code check-ins to scan the code for CVEs. While continuous monitoring is valuable, this approach does not directly address vulnerabilities within container images, which are a crucial aspect of container security.

  * Option C proposes restricting the usage of non-commercially supported base images within the development environment as a proactive measure. While this is important for security, it does not automate vulnerability scanning of container images, which is necessary for efficient and timely detection of vulnerabilities.

  * Option D suggests utilizing Cloud Monitoring to evaluate the outcomes of Cloud Build and identify if a vulnerable version has been utilized. While this provides insights into potential vulnerabilities, it does not offer direct vulnerability scanning of container images as requested.

Therefore, Option A provides the most efficient approach by seamlessly integrating vulnerability scanning into the container image management workflow using managed services.

**References:**

[https://cloud.google.com/container-registry/docs/get-image-vulnerabilities#viewing_vulnerabilities_and_other_occurrences](https://cloud.google.com/container-registry/docs/get-image-vulnerabilities#viewing_vulnerabilities_and_other_occurrences  https://cloud.google.com/container-registry/docs/container-analysis)

[https://cloud.google.com/container-registry/docs/container-analysis](https://cloud.google.com/container-registry/docs/get-image-vulnerabilities#viewing_vulnerabilities_and_other_occurrences  https://cloud.google.com/container-registry/docs/container-analysis)

</details>

---

### Exam 1 · Q58

**In order to assess whether the web application running on Google Kubernetes Engine is susceptible to cross-site scripting (XSS) attacks or if it utilizes libraries with known vulnerabilities, which service should you employ?**

- I. Google Cloud Armor
- IV. Error Reporting
- II. Debugger
- III. Web Security Scanner

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Web Security Scanner

**The most suitable option in this case is:**

  * **III. Web Security Scanner**

**Explanation:**

  * **Designed for Vulnerability Detection:** Web Security Scanner is specifically designed to find web application vulnerabilities, including XSS and those caused by outdated libraries with known flaws.

  * **Active Assessment:** It thoroughly examines your application, simulating attacks and analyzing the results to uncover potential attack vectors.

  * **Comprehensive Reports:** It provides detailed reports outlining vulnerabilities, making it easier to focus your remediation efforts.

**Why Other Options Are Less Ideal:**

  * **I. Google Cloud Armor:** Google Cloud Armor is a Web Application Firewall (WAF). While important for defense, it mainly protects against already-known attack patterns. It doesn't actively scan for new vulnerabilities like a dedicated security scanner.

  * **II. Debugger:** A debugger is a development tool used to troubleshoot code problems. It's not designed for proactive vulnerability detection.

  * **IV. Error Reporting:** Error logs can sometimes reveal issues caused by XSS attempts, but this is more of an indirect and reactive approach. Monitoring errors is helpful, but doesn't replace a proactive vulnerability scanner.

Ref:

<https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview>

</details>

---

### Exam 1 · Q59

**You have developed a new application and aim to deploy it on Cloud Run without utilizing a Dockerfile. Your organization mandates that all container images are stored in a centrally managed container repository. Which approach should you take to construct your container using Google Cloud services? (Select two.)**

- I. Upload your source code to Artifact Registry.
- III. Utilize the pack build command through pack CLI.
- IV. Incorporate the --source flag within the gcloud run deploy CLI command.
- V. Add the --platform=kubernetes flag within the gcloud run deploy CLI command.
- II. Initiate a Cloud Build job for image pushing.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Utilize the pack build command through pack CLI. **|** IV. Incorporate the --source flag within the gcloud run deploy CLI command.

The two correct answers are:

  * **III. Utilize the pack build command through the pack CLI.**

  * **IV. Incorporate the --source flag within the gcloud run deploy CLI command.**

Here's why these choices work together, and why the others aren't suitable:

**III. Using the pack build command:**

  * **Buildpacks:** This command leverages Cloud Native Buildpacks, which automatically examine your source code and detect the appropriate language/framework. Buildpacks then handle the construction of the container image for you, eliminating the need for a Dockerfile.

  * **Pushing to Repository:** The `pack build` command can directly push the built container image to a supported registry, like Artifact Registry, satisfying your organization's central repository requirement.

**IV. Using the gcloud run deploy --source flag:**

  * **Direct Source Deployment:** This flag allows you to deploy your application code directly to Cloud Run. Cloud Build will be triggered under the hood, utilizing Buildpacks to create a container image from your source code.

  * **Automated Repository Storage:** Cloud Build automatically stores the resulting image in a compatible container repository (such as Artifact Registry).

**Why other options aren't correct:**

  * **I. Upload your source code to Artifact Registry.** While Artifact Registry is the right place to store images, simply uploading source code does not create a container image.

  * **II. Initiate a Cloud Build job for image pushing.** You'd need a container image to begin with for Cloud Build to push; this option doesn't address image creation.

  * **V. Add the --platform=kubernetes flag within the gcloud run deploy CLI command.** This flag is used to manage Cloud Run deployments for Kubernetes environments and isn't relevant to building a container image without a Dockerfile.

References:

<https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-now-supports-buildpacks>

</details>

---

### Exam 2 · Q2

**How should you configure the load testing for a set of REST API endpoints deployed to Cloud Run, meeting Google-recommended best practices?**

- II. Employ an unmanaged instance group to deploy an image with cURL installed. Configure cURL within the image to execute a test plan, running one instance per VM to initiate load from multiple parallel threads and source IP addresses.
- IV. Download a container image of a distributed load testing framework on Cloud Shell. Sequentially launch multiple instances of the container on Cloud Shell to augment the load on the API.
- I. Utilize a managed instance group to deploy an image with cURL installed. Configure cURL within the image to execute a test plan, running one instance per VM to initiate load from multiple parallel threads and source IP addresses.
- III. Implement a distributed load testing framework on a private Google Kubernetes Engine (GKE) cluster. Scale by deploying additional Pods as necessary to generate more traffic and support concurrent users.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Implement a distributed load testing framework on a private Google Kubernetes Engine (GKE) cluster. Scale by deploying additional Pods as necessary to generate more traffic and support concurrent users.

Here's a breakdown of the options and why the best choice aligns with Google's recommended practices:

**Correct Option:**

  * **III. Implement a distributed load testing framework on a private Google Kubernetes Engine (GKE) cluster. Scale by deploying additional Pods as necessary to generate more traffic and support concurrent users.**

**Justification:**

  * **Scalability:** GKE is inherently designed for scalability, especially for load testing purposes. Adding pods dynamically allows you to simulate realistic user loads, including spikes.

  * **Distributed Testing:** Load testing frameworks are best leveraged in a distributed manner, ensuring that the load generated mimics real-world scenarios with traffic originating from diverse sources. GKE's flexibility facilitates this.

  * **Manageability:** GKE provides managed infrastructure, simplifying cluster configuration and maintenance, allowing you to focus on your test plans.

  * **Google Best Practices:** Aligns with Google's advice to use tools like JMeter in a distributed setup for thorough Cloud Run load testing.

**Why Other Options Are Not Ideal:**

  * **I. Utilizing a managed instance group to deploy an image with cURL installed...**

    * **Inefficient Scaling:** Managed instance groups are not as easily scalable as GKE for quick load ramp-up and ramp-down.

    * **Limited Distribution:** Load generated will originate from similar IP addresses, unlike real user scenarios.

  * **II. Employ an unmanaged instance group to deploy an image with cURL installed...**

    * **Even less scalable than option I** and has the same distribution issue.

    * **Management Overhead:** Unmanaged instance groups require more effort for configuration and maintenance.

  * **IV. Download a container image of a distributed load testing framework on Cloud Shell...**

    * **Resource Constraints:** Cloud Shell instances have limited resources for extensive load testing.

    * **Sequential Launch:** Launching containers sequentially doesn't reflect realistic traffic patterns.

**References:**

[https://cloud.google.com/architecture/distributed-load-testing-using-gke#build_the_](https://cloud.google.com/architecture/distributed-load-testing-using-gke#build_the_c)[container_image](https://cloud.google.com/architecture/distributed-load-testing-using-gke#build_the_ccontainer_image)

</details>

---

### Exam 2 · Q3

**In the process of parsing a log file containing timestamp, account number (string), and transaction amount (number) columns, you aim to efficiently compute the sum of transaction amounts for each unique account number. Which data structure is best suited for this task?**

- IV. A comma-delimited string
- III. A two-dimensional array
- I. A linked list
- II. A hash table

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. A hash table

**II. A hash table**

  * **Efficient Lookups:** Hash tables offer near-constant time lookups based on keys (in this case, the account number). This is critical for quickly finding existing entries or adding new ones as you parse the log file.

  * **Natural Key-Value Fit:** The 'account number' (key) and its corresponding 'total transaction amount' (value) map perfectly to the key-value structure of a hash table.

**Why Other Options Are Less Ideal:**

  * **I. A linked list** Searching for the right account number in a linked list would be linear (O(n)), meaning it gets slower as the number of accounts grows.

  * **III. A two-dimensional array** While an array could work, it's less efficient than a hash table for lookups if the account numbers are not known beforehand or aren't sequential.

  * **IV. A comma-delimited string** Storing data this way would make calculations and lookups extremely inefficient. Strings are not ideal for structured data.

Reference:  
<https://open4tech.com/array-vs-linked-list-vs-hash-table/>

</details>

---

### Exam 2 · Q6

**Your company's development teams wish to incorporate various open-source operating systems into their Docker builds. As images are generated and published in containers within your company's environment, you need to conduct scans for Common Vulnerabilities and Exposures (CVEs) without hindering software development agility. Additionally, you prefer employing managed services whenever possible. What's the best course of action?**

- II. Develop a Cloud Function triggered by code check-ins to perform CVE scans on the code.
- III. Restrict the usage of non-commercially supported base images within your development environment.
- I. Activate the Vulnerability scanning feature within the Container Registry.
- IV. Utilize Cloud Monitoring to scrutinize Cloud Build's output and detect if a vulnerable version has been utilized.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Activate the Vulnerability scanning feature within the Container Registry.

**I. Activate the Vulnerability scanning feature within the Container Registry.**

Here's why this stands out as the most suitable option:

  * **Purpose-Built:** Container Registry's vulnerability scanning feature is specifically designed to scan container images for known CVEs. It aligns directly with your core requirement.

  * **Seamless Integration:** It works seamlessly with container images stored in the Container Registry, fitting naturally into your existing workflow.

  * **Minimal Disruption:** Activating this scanning feature does not require significant changes to the development process, maintaining agility.

  * **Managed Service:** Utilizing this feature within the Container Registry aligns with your stated preference for managed services.

**Why Other Options are Less Ideal:**

  * **II. Develop a Cloud Function triggered by code check-ins to perform CVE scans on the code.** Code-level CVE scans are important, but they won't identify vulnerabilities introduced by dependencies in the container image.

  * **III. Restrict the usage of non-commercially supported base images within your development environment.** This improves security posture but might be overly restrictive and could hinder development flexibility. Not all vulnerabilities stem from lack of commercial support.

  * **IV. Utilize Cloud Monitoring to scrutinize Cloud Build's output and detect if a vulnerable version has been utilized.** Cloud Monitoring is useful for general logging and alerting but lacks the specialized CVE scanning capabilities.

**References:**  
[https://docs.docker.com/engine/scan/](https://docs.docker.com/engine/scan/  https://cloud.google.com/container-analysis/docs/os-overview)

[https://cloud.google.com/container-analysis/docs/os-overview](https://docs.docker.com/engine/scan/  https://cloud.google.com/container-analysis/docs/os-overview)

</details>

---

### Exam 2 · Q11

**As part of updating Cloud Build steps to align with best practices, you're tasked with integrating a vulnerability scan for the built container image. The scan results should seamlessly integrate into your Google Cloud deployment pipeline without causing disruptions to other teams' processes. What's the recommended approach?**

- III. Enable the Container Scanning API in Artifact Registry to scan the built container images for vulnerabilities.
- IV. Integrate Artifact Registry with your Aqua Security instance to perform vulnerability scans on the built container images.
- II. Upload the built container images to your Docker Hub instance and conduct vulnerability scans.
- I. Enable Binary Authorization and configure it to attest that no vulnerabilities exist in the container image.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Enable the Container Scanning API in Artifact Registry to scan the built container images for vulnerabilities.

**Correct Option:**

**III. Enable the Container Scanning API in Artifact Registry to scan the built container images for vulnerabilities.**

**Explanation:**

  * **Native Integration:** The Container Scanning API is a built-in feature of Artifact Registry, providing a seamless and integrated vulnerability scanning experience within Google Cloud.

  * **Minimal Disruption:** Adding a vulnerability scan in Artifact Registry is unlikely to disrupt other teams' workflows, as it's a natural extension of storing images.

  * **Actionable Results:** Container Scanning can be configured to generate findings viewable in Security Command Center, providing insights and the ability to potentially block deployments based on vulnerability severity.

**Why other options are less ideal:**

  * **I. Binary Authorization:** While critical, Binary Authorization relies on attestations. Vulnerability scanning would be the mechanism to generate such attestations but isn't a vulnerability scanner itself.

  * **II. Docker Hub Scanning:** This involves pushing images to an external repository and adds another dependency outside of GCP.

  * **IV. Aqua Security Integration:** While Aqua Security is a robust tool, it introduces another external system to manage and adds complexity to your pipeline.

**References:**  
<https://cloud.google.com/container-analysis/docs/automated-scanning-howto#view_the_image_vulnerabilities>

</details>

---

### Exam 2 · Q17

**You are monitoring a web application deployed on Google Kubernetes Engine, developed in Go. An increase in CPU and memory usage has been observed. How can you determine which sections of the source code are consuming the most CPU and memory resources?**

- III. Integrate OpenTelemetry and Trace export packages into your application to create the trace provider. Examine the latency data for your application on the Trace overview page to identify bottleneck areas.
- IV. Develop a Cloud Logging query to collect the web application's logs. Create a Python script to compute the difference between the timestamps from the beginning and end of the application's longest functions to identify time-intensive functions.
- I. Install the Snapshot Debugger agent in your VM. Capture debug snapshots of the functions with the longest execution time. Analyze the call stack frame to identify the local variables at that level in the stack.
- II. Incorporate the Cloud Profiler package into your application and initialize the Profiler agent. Review the generated flame graph in the Google Cloud console to pinpoint time-intensive functions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Incorporate the Cloud Profiler package into your application and initialize the Profiler agent. Review the generated flame graph in the Google Cloud console to pinpoint time-intensive functions.

**Correct Answer:**

  * **II. Incorporate the Cloud Profiler package into your application and initialize the Profiler agent. Review the generated flame graph in the Google Cloud console to pinpoint time-intensive functions.**

**Justification:**

  * **Specific to Application Profiling:** Cloud Profiler is a continuous profiling tool designed explicitly to identify performance bottlenecks in applications running on production environments like Google Kubernetes Engine.

  * **Optimized for GKE:** It has seamless integration with GKE, minimizing setup complexity.

  * **Flame Graphs:** Flame graphs are an effective visual representation for pinpointing resource-heavy code sections, making analysis efficient.

**Why Other Options Are Less Suitable:**

  * **I. Install the Snapshot Debugger agent in your VM...**

    * **Debugging vs. Profiling:** Snapshot Debugger is primarily a debugging tool. While it can provide insights into code execution, it's less tailored for continuous resource usage monitoring.

    * **Overhead:** Introducing a debugger can add overhead to a production environment.

  * **III. Integrate OpenTelemetry and Trace export packages...**

    * **Focus on Tracing:** OpenTelemetry is excellent for distributed tracing, which primarily tracks request flows across systems. It's less direct for pinpointing CPU or memory-heavy code sections within the application itself.

  * **IV. Develop a Cloud Logging query to collect the web application's logs...**

    * **Manual and Time-Consuming:** Analyzing logs manually can be effective but is often tedious for pinpointing performance issues. Profilers are more efficient for this specific task.

**References:**

[https://cloud.google.com/profiler/docs](https://cloud.google.com/profiler/docs  https://cloud.google.com/profiler/docs/about-profiler#profiling_agent  https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages)

[https://cloud.google.com/profiler/docs/about-profiler#profiling_agent](https://cloud.google.com/profiler/docs  https://cloud.google.com/profiler/docs/about-profiler#profiling_agent  https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages)

[https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages](https://cloud.google.com/profiler/docs  https://cloud.google.com/profiler/docs/about-profiler#profiling_agent  https://cloud.google.com/profiler/docs/about-profiler#environment_and_languages)

</details>

---

### Exam 2 · Q20

**While employing Cloud Build to build and test application source code stored in Cloud Source Repositories, you encounter a requirement for a build tool that isn't available in the Cloud Build environment. What's the recommended course of action?**

- III. Embed the binary in your Cloud Source Repositories repository and reference it in your build scripts.
- IV. Request the addition of the binary to the Cloud Build environment by submitting a feature request via the Cloud Build public Issue Tracker.
- II. Develop a custom cloud builder image and specify it in your build steps.
- I. Fetch the binary from the internet during the build process.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Develop a custom cloud builder image and specify it in your build steps.

**II. Develop a custom cloud builder image and specify it in your build steps.**

**Explanation:**

  * **Customization:** Creating a custom cloud builder image gives you complete control over the tools and libraries available in the build environment.

  * **Reproducibility:** The image ensures that builds are consistent and independent of changes in default Cloud Build environments.

  * **Maintainability:** You manage the build tool's installation and version within the image.

**Why Other Options Are Less Ideal:**

  * **I. Fetch the binary from the internet during the build process.** This introduces potential security risks, network dependency, and could make builds less reproducible if the external source changes.

  * **III. Embed the binary in your Cloud Source Repositories repository and reference it in your build scripts.** Bundling a large binary with your source code can increase repository size and potentially complicate build scripts.

  * **IV. Request the addition of the binary...** This is a viable long-term option, but it doesn't give you immediate control and might not be possible if the tool isn't widely used.

**Reference:**

<https://cloud.google.com/cloud-build/docs/configuring-builds/use-community-and-custom-builders#creating_a_custom_builder>

</details>

---

### Exam 2 · Q26

**In response to a surge in errors within an application operating on Cloud Run within your production environment, configured to handle messages from Pub/Sub topic A, process them, and then forward them to topic B, what steps should you take to identify the error's cause, utilizing mock messages for testing?**

- IV. Utilize the Google Cloud console to generate mock messages for topic A. Adjust the application's logging level to DEBUG or INFO, then analyze the logs for diagnostic information.
- III. Set up the Pub/Sub emulator locally. Redirect the production application to interact with local Pub/Sub topics. Generate mock messages for topic A and analyze the resulting logs.
- II. Utilize the gcloud CLI to generate mock messages for topic A. Adjust the application's logging level to DEBUG or INFO, then analyze the logs for insights.
- I. Install the Pub/Sub and Cloud Run emulators on your local system. Deploy the application locally, adjusting the logging level to DEBUG or INFO. Generate mock messages for topic A and analyze the application logs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Install the Pub/Sub and Cloud Run emulators on your local system. Deploy the application locally, adjusting the logging level to DEBUG or INFO. Generate mock messages for topic A and analyze the application logs.

The most effective approach to identify the error's cause in your Cloud Run application using mock messages is:

**I. Install the Pub/Sub and Cloud Run emulators on your local system. Deploy the application locally, adjusting the logging level to DEBUG or INFO. Generate mock messages for topic A and analyze the application logs.**

Here's why this approach is the best:

  * **Isolated testing environment:** The emulators allow you to replicate the production environment locally, isolating the issue and eliminating potential interference from other production components.

  * **Controlled testing:** You have complete control over the mock messages generated, enabling you to reproduce specific scenarios that trigger the errors.

  * **Detailed logging:** Adjusting the logging level provides granular insights into the application's behavior during message processing, helping pinpoint the root cause of the errors.

  * **Efficient debugging:** Debugging locally is generally faster and more convenient than troubleshooting in a production environment.

Let's analyze why the other options aren't as suitable:

  * **II. Utilize the gcloud CLI to generate mock messages for topic A.** While this allows you to generate mock messages, it doesn't provide an isolated testing environment, potentially making it difficult to isolate the issue.

  * **III. Set up the Pub/Sub emulator locally. Redirect the production application to interact with local Pub/Sub topics.** This approach involves modifying the production application's configuration, which could introduce risks and disruptions to the live environment.

  * **IV. Utilize the Google Cloud console to generate mock messages for topic A.** Similar to option II, this lacks an isolated testing environment and might not be the most efficient way to reproduce and diagnose the errors.

**By installing the emulators and testing locally, you create a safe and controlled environment to thoroughly investigate the errors and identify their root cause without impacting the production system.**

</details>

---

### Exam 2 · Q28

**After integrating a new application with OpenTelemetry, you aim to monitor the latency of your application requests within Trace. Your goal is to guarantee that a particular request is consistently traced. What is the recommended course of action?**

- III. Employ the Trace API to assign custom attributes to the trace.
- II. Develop a custom script to continuously send requests of this type from your development project.
- I. Allow a 10-minute interval to confirm that Trace automatically captures these specific requests.
- IV. Append the X-Cloud-Trace-Context header to the request with the correct parameters.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Append the X-Cloud-Trace-Context header to the request with the correct parameters.

**IV. Append the X-Cloud-Trace-Context header to the request with the correct parameters.**

Here's why:

  * **Forced Tracing:** The `X-Cloud-Trace-Context` header directly instructs Cloud Trace to include the specific request in its traces. This ensures the desired request is traced regardless of other factors or sampling configurations.

Here's why the other options are less ideal:

  * **I. Waiting:** Traces might not automatically capture the request, especially if sampling is in place or the request volume is low.

  * **II. Scripting:** While a script could help, it's not the most efficient way to force tracing for a specific request type.

  * **III. Custom Attributes:** Adding attributes helps provide context but doesn't guarantee the request is traced.

References:

<https://cloud.google.com/trace/docs/setup#force-trace>

</details>

---

### Exam 2 · Q48

**Your API backend operates across multiple cloud providers, and you need to analyze the network latency of your API. Which two actions should you take? (Select two.)**

- I. Utilize Zipkin collector to gather data efficiently.
- V. Employ Stackdriver Profiler to identify performance bottlenecks and generate reports.
- IV. Leverage Stackdriver Debugger to analyze network latency issues.
- II. Implement Fluentd agent to collect data seamlessly.
- III. Use Stackdriver Trace for generating comprehensive latency reports.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Utilize Zipkin collector to gather data efficiently. **|** III. Use Stackdriver Trace for generating comprehensive latency reports.

* **I. Utilize Zipkin collector to gather data efficiently.**

    * **Distributed Tracing:** Zipkin is designed explicitly for tracing requests across distributed systems, including those spanning multiple cloud providers. It's compatible with various frameworks and protocols.

    * **Latency Analysis:** Zipkin captures detailed timing data about each "span" within a request, crucial for network latency analysis.

  * **III. Use Stackdriver Trace for generating comprehensive latency reports.**

    * **Trace Analysis:** Stackdriver Trace ingests trace data (including from Zipkin) and provides powerful visualization and analysis tools specifically tailored to investigating latency issues.

    * **Cross-Cloud Visibility:** If parts of your backend are on GCP, Stackdriver Trace will integrate with them natively.

**Why Other Options Are Less Ideal**

  * **II. Implement Fluentd agent ...** While Fluentd is a versatile log aggregator, it's not focused on distributed tracing. It would require custom processing to extract the latency data you need.

  * **IV. Leverage Stackdriver Debugger ...** Debugger is primarily for debugging running code, not for tracing distributed request paths and measuring network time specifically.

  * **V. Employ Stackdriver Profiler ...** Profiler focuses on code-level performance issues, not end-to-end network latency.

**Reference:**

[https://cloud.google.com/trace/docs/zipkin](https://cloud.google.com/trace/docs/zipkin  https://cloud.google.com/trace/docs/zipkin#frequently_asked_questions)

[https://cloud.google.com/trace/docs/zipkin#frequently_asked_questions](https://cloud.google.com/trace/docs/zipkin  https://cloud.google.com/trace/docs/zipkin#frequently_asked_questions)

</details>

---

### Exam 2 · Q51

**Your team is responsible for crafting services operating on Google Kubernetes Engine. Storing your team's code in Cloud Source Repositories, you're aiming to swiftly pinpoint bugs in the code prior to deployment to production. Your objective is to streamline developer feedback and optimize the process through automation. What's the recommended course of action?**

- III. Leverage Spinnaker to automate the deployment of container images to the production environment.
- IV. Employ Cloud Build to automate the creation of container images from code, initiated by forked versions.
- I. Employ Spinnaker to automate the creation of container images from code, triggered by Git tags.
- II. Utilize Cloud Build to automate the creation of container images from code, activated by Git tags.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Utilize Cloud Build to automate the creation of container images from code, activated by Git tags.

**II. Utilize Cloud Build to automate the creation of container images from code, activated by Git tags.**

Here's why:

  * **Focus on Pre-Deployment Testing:** The goal here is to catch bugs **before** code reaches production. Cloud Build excels at automating image creation, a key part of a pre-deployment testing and validation pipeline.

  * **Git Tag Integration:** Tagging in source control often signifies a release candidate. Using Git tags to trigger Cloud Build ensures the image built reflects a potentially releasable state of your code, ideal for testing.

  * **Streamlined Workflow:** Cloud Build offers a well-integrated workflow for building container images directly from Cloud Source Repositories, promoting efficiency for developers.

Let's analyze why other options are less optimal:

  * **I. Employ Spinnaker...** Spinnaker is primarily a continuous delivery (CD) platform focused on deployment automation. While it can integrate image building tasks, its strength lies in managing deployments, not pre-deployment testing feedback.

  * **III. Leverage Spinnaker...** Again, Spinnaker's core competency is deployment, making it less ideal for the bug-identification stage that happens earlier in the pipeline.

  * **IV. Employ Cloud Build...forked versions.** Building images from forked versions could introduce inconsistencies and make it harder to track the connection between code and image for testing purposes. Using Git tags provides a more controlled and predictable workflow.

</details>

---

### Exam 2 · Q54

**In the process of adding unit tests to your application, you aim to assert that published Pub/Sub messages are processed by your subscriber in the correct order. Your priority is to ensure the unit tests are cost-effective and reliable. What approach should you take?**

- IV. Utilize the Pub/Sub emulator for testing purposes.
- II. Establish a topic and subscription for each tester.
- I. Implement a mocking framework for testing.
- III. Introduce a filter by tester to the subscription.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize the Pub/Sub emulator for testing purposes.

Here's the breakdown of why the best option is:

**IV. Utilize the Pub/Sub emulator for testing purposes.**

Here's why this approach is the most suitable:

  * **Cost-Effectiveness:** The Pub/Sub emulator runs locally, eliminating costs associated with using the actual Google Cloud Pub/Sub service during testing.

  * **Isolation:** The emulator provides a controlled testing environment, allowing you to focus on message order verification without external interference.

  * **Control:** You can easily manipulate message order and timing in the emulator, enabling thorough testing of your subscriber's logic.

  * **Reliability:** The emulator offers a consistent and predictable environment for unit testing, enhancing test reliability.

**Why Other Options Are Less Ideal:**

  * **I. Implement a mocking framework for testing.**

    * Mocking can be useful for certain aspects of subscriber testing but may struggle to fully replicate Pub/Sub behavior and message ordering in a complex system.

  * **II. Establish a topic and subscription for each tester.**

    * This approach introduces provisioning and management overhead within the production Pub/Sub service and can become costly with a large number of testers.

  * **III. Introduce a filter by tester to the subscription.**

    * Filtering adds complexity and may not be a sca

</details>

---

### Exam 2 · Q58

**You are preparing to test the Pub/Sub integration of your application, which reads credit card data from a Pub/Sub subscription. After completing code and unit testing, what is the recommended approach for testing the Pub/Sub integration before deploying to Google Cloud?**

- IV. Establish a service for message publication and deploy the Pub/Sub emulator. Publish a predefined set of testing messages from the publishing service to the emulator for testing
- III. Implement a service for message publication and deploy the Pub/Sub emulator. Capture the messages from Pub/Sub in the production environment and publish them to the emulator for testing.
- II. Set up a service to publish messages to your application. Capture the messages from Pub/Sub in the production environment and replay them through the publishing service for testing.
- I. Develop a service for message publication and deploy the Pub/Sub emulator. Generate random content in the publishing service and publish it to the emulator for testing.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Establish a service for message publication and deploy the Pub/Sub emulator. Publish a predefined set of testing messages from the publishing service to the emulator for testing

**IV. Establish a service for message publication and deploy the Pub/Sub emulator. Publish a predefined set of testing messages from the publishing service to the emulator for testing**

Here's the reasoning:

  * **Isolation:** Using the Pub/Sub emulator within a local or isolated testing environment protects your production environment from unintended consequences and experimental data.

  * **Control:** Predefined test messages allow you to test specific scenarios, edge cases, and potential error conditions relevant to your credit card processing logic.

  * **Reproducibility:** Having a controlled set of test messages makes the testing process more reproducible, aiding in debugging and ensuring consistent results.

**Why other options are less ideal:**

  * **I. Random Content:** While testing with random data can be useful, it might not cover all the important scenarios for your credit card data processing.

  * **II & III. Using Production Messages:** Relying on messages from production introduces these risks:

    * **Data Exposure:** Sensitive credit card data may be exposed in test environments.

    * **Inconsistency:** Production message patterns might not be suitable for your test cases.

    * **Potential Impact:** Replaying messages could interfere with real production operations.

**Reference:**

<https://cloud.google.com/pubsub/docs/emulator>

</details>

---

### Exam 3 · Q8

**While leveraging Cloud Build for Docker image creation, you're tasked with integrating unit and integration tests into the build process. In the event of a failure, you aim for clear identification of the failing stage in the build history. What's the optimal strategy to achieve this?**

- IV. Construct a Cloud Build build configuration file featuring distinct cloud builder steps for compiling and executing unit and integration tests.
- III. Develop a Cloud Build build configuration file to trigger a separate cloud build pipeline dedicated to unit and integration tests.
- I. Embed RUN commands within the Dockerfile to execute unit and integration tests.
- II. Craft a Cloud Build build configuration file with a unified build step for compiling unit and integration tests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Construct a Cloud Build build configuration file featuring distinct cloud builder steps for compiling and executing unit and integration tests.

**IV. Construct a Cloud Build build configuration file featuring distinct cloud builder steps for compiling and executing unit and integration tests.**

Let's break down why it's the best choice:

  * **Granular Test Stages:** Separate build steps provide a clear demarcation between the unit and integration test stages, making it easier to pinpoint the specific source of a failure.

  * **Targeted Actions:** Each step can have its own dependencies, configuration, and commands tailored to the type of test being executed.

  * **Readable Build History:** The Cloud Build history will clearly display the success or failure status of each individual test stage.

  * **Flexibility:** You can easily add more test stages or modify the order without affecting the overall build.

**Why Other Options Are Less Ideal:**

  * **I. Embed RUN commands within the Dockerfile** Cluttering the Dockerfile compromises readability and can create maintenance challenges. Unit and integration tests should ideally be decoupled from the core image build process.

  * **II. Craft a Cloud Build build configuration file ... unified build step** This approach lumps the tests together, hindering your ability to pinpoint the root cause of a failure.

  * **III. Develop a Cloud Build build configuration file to trigger a separate cloud build pipeline ...** This adds unnecessary complexity and potential build time overhead due to managing separate pipelines.

Ref:

<https://cloud.google.com/build/docs/build-config-file-schema:>

</details>

---

### Exam 3 · Q11

**In the context of developing an online gaming platform on Google Kubernetes Engine (GKE), where users are experiencing extended loading times for specific URL requests, what is the recommended approach to identify performance bottlenecks and pinpoint HTTP requests with significant latency?**

- III. Integrate your microservices with the OpenTelemetry tracing package. Update application code to dispatch traces to Trace for thorough inspection and analysis. Generate an analysis report within Trace to evaluate user requests comprehensively.
- II. Enhance your microservices to log HTTP request methods and URL paths to STDOUT. Utilize the logs router to forward container logs to Cloud Logging. Implement filters within Cloud Logging to assess the latency of user requests across various methods and URL paths.
- IV. Deploy tcpdump on your GKE nodes and initiate it to capture network traffic over an extended duration for data collection. Subsequently, analyze the captured data files employing Wireshark to uncover the root cause of high latency.
- I. Configure GKE workload metrics through kubectl, directing all Pods to transmit metrics to Cloud Monitoring. Utilize Cloud Monitoring to craft a custom dashboard showcasing application metrics, facilitating the identification of performance bottlenecks within the GKE cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Integrate your microservices with the OpenTelemetry tracing package. Update application code to dispatch traces to Trace for thorough inspection and analysis. Generate an analysis report within Trace to evaluate user requests comprehensively.

**Correct Option: III. Integrate your microservices with the OpenTelemetry tracing package. Update application code to dispatch traces to Trace for thorough inspection and analysis. Generate an analysis report within Trace to evaluate user requests comprehensively.**

**Explanation:**

  * **Distributed Tracing:** OpenTelemetry is specifically designed for distributed tracing in microservices environments. It provides fine-grained visibility into request paths, timings, and potential bottlenecks across services.

  * **Cloud Trace Integration:** Trace is natively integrated with Google Cloud, offering a powerful visualization and analysis platform tailored for tracing data.

  * **Targeted Analysis:** Traces allow you to pinpoint slow parts of your system specifically related to user-facing HTTP requests, giving you the most relevant data.

**Why other options are less ideal:**

  * **I. GKE Workload Metrics:** While useful for general cluster health, these metrics are less granular for pinpointing latency at the individual HTTP request level.

  * **II. Log Analysis:** While logs can help, analyzing raw HTTP logs for latency is less efficient and provides less granular insights than distributed traces.

  * **IV. tcpdump:** Network packet analysis can be helpful but is very low-level. It is less efficient for quickly understanding bottlenecks within a complex microservices application.#

**Reference:**

<https://cloud.google.com/trace/docs/setup#when-to-instrument>

</details>

---

### Exam 3 · Q16

**In a distributed microservices architecture, you aim to assess the performance and system resource utilization of a Java-based microservice. What steps should you take?**

- IV. Utilize OpenCensus to instrument the service for measuring service latency, and subsequently, generate custom metrics in Cloud Monitoring.
- I. Employ Cloud Profiler to instrument the service, enabling measurement of CPU utilization and method-level execution times.
- II. Utilize Debugger to instrument the service for error investigation purposes.
- III. Employ Cloud Trace to instrument the service, facilitating the measurement of request latency.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Employ Cloud Profiler to instrument the service, enabling measurement of CPU utilization and method-level execution times.

The correct answer for assessing the **performance** and **system resource utilization** of a Java-based microservice in a distributed architecture is

**Option I: Employ Cloud Profiler to instrument the service, enabling measurement of CPU utilization and method-level execution times**.

Why Option I is correct:

  * **Cloud Profiler** is specifically designed to assess **CPU utilization** , memory allocation, and method-level execution times. It continuously samples the application to identify performance bottlenecks and inefficient code paths, making it highly suitable for monitoring system resource utilization in your Java microservice.

Why other options are incorrect:

  * **Option II: Utilize Debugger for error investigation** :

    * Cloud Debugger is used to track down issues in the code without stopping the service. However, it focuses on debugging and inspecting code rather than performance assessment or system resource utilization. It doesn't provide insights into CPU or memory usage.

  * **Option III: Employ Cloud Trace to measure request latency** :

    * Cloud Trace is useful for tracking request latency across services, but it does not give detailed insights into resource utilization (e.g., CPU or memory). Its primary focus is on tracing the flow of requests and measuring how long it takes for services to respond, not on performance profiling.

  * **Option IV: Utilize OpenCensus to measure service latency and generate custom metrics** :

    * OpenCensus (now part of OpenTelemetry) is used for **distributed tracing** and **latency** monitoring, not directly for CPU or method-level performance analysis. While useful for tracking the flow of requests and generating metrics, it doesn’t provide deep insights into resource utilization like Cloud Profiler does.

In conclusion, **Cloud Profiler (Option I)** is the correct choice for your performance assessment and resource utilization needs.

**Reference:**

<https://cloud.google.com/profiler/docs>

</details>

---

### Exam 3 · Q18

**You're assessing developer tools to facilitate Google Kubernetes Engine adoption and integration within your development ecosystem, which encompasses VS Code and IntelliJ. What's the recommended approach?**

- IV. Utilize Cloud Shell for managing infrastructure and applications via the command line.
- III. Implement a Cloud Notebook instance for data ingestion, processing, and model deployment.
- II. Utilize the Cloud Shell integrated Code Editor for editing code and configuration files.
- I. Employ Cloud Code for application development.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Employ Cloud Code for application development.

**I. Employ Cloud Code for application development.** Here's why this is the best choice, followed by explanations of why the other options aren't as suitable:

  * **Cloud Code: The Ideal Fit** Cloud Code is purpose-built to enhance the developer experience within Google Kubernetes Engine (GKE) environments. It offers extensions for popular IDEs like VS Code and IntelliJ, providing:

    * Kubernetes-aware coding assistance (e.g., code completion, snippets)

    * Easy debugging for applications running within the cluster

    * Deployment workflows from within the IDE

    * Integrated management of cluster resources

  * **Other Options: Their Limitations**

    * **II. Cloud Shell Integrated Code Editor:** The Cloud Shell code editor is better suited for quick edits and configuration file changes but lacks the depth and Kubernetes-specific features of Cloud Code for full-fledged application development.

    * **III. Cloud Notebook Instance:** Cloud Notebooks are designed primarily for data analysis and machine learning tasks. While they can be used in conjunction with GKE, they are not the primary tool for building and deploying applications onto Kubernetes.

    * **IV. Cloud Shell:** Cloud Shell is powerful for command-line interaction with GKE (using kubectl, etc.). However, it doesn't provide the rich IDE experience, extensions, and code assistance of Cloud Code.

**Reference:**

<https://cloud.google.com/code/docs>

</details>

---

### Exam 3 · Q37

**As a developer managing three Google Kubernetes Engine clusters on Google Cloud, you need to enable your team to switch between clusters seamlessly while adhering to Google-recommended best practices. What is the best approach to configure access to multiple clusters?**

- IV. Advise the developers to open three terminals on their workstation and utilize `**kubectl config**` to set up access to each cluster.
- I. Request the developers to utilize Cloud Shell and execute `**gcloud container clusters get-credential**` to switch to another cluster.
- II. Define the clusters, users, and contexts in a configuration file, and distribute the file to developers, instructing them to employ `**kubectl config**` to incorporate cluster, user, and context details.
- III. Instruct the developers to install the gcloud CLI on their workstations and execute `**gcloud container clusters get-credentials**` to switch to another cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Define the clusters, users, and contexts in a configuration file, and distribute the file to developers, instructing them to employ `**kubectl config**` to incorporate cluster, user, and context details.

**Correct Option:**

  * **II. Define the clusters, users, and contexts in a configuration file, and distribute the file to developers, instructing them to employ kubectl config to incorporate cluster, user, and context details.**

**Justification:**

  * **Centralized Management:** Maintaining a single configuration file (often named `kubeconfig`) streamlines cluster access for your entire team and keeps configurations consistent.

  * **kubectl Standard:** This approach leverages the standard `kubectl` tool designed for managing Kubernetes resources across clusters.

  * **Best Practice:** Aligns with Google's recommendations and Kubernetes documentation for configuring access to multiple clusters.

**Why Other Options Are Less Ideal:**

  * **I. Request the developers to utilize Cloud Shell...**

    * **Impractical:** Cloud Shell sessions are transient, requiring repeated configuration and are less suitable for ongoing development work.

    * **Local Tooling:** Developers often need to interact with clusters from their local development environments.

  * **III. Instruct the developers to install the gcloud CLI...**

    * **Additional Overhead:** While the `gcloud` CLI is useful, it introduces an extra tool dependency. `kubectl` is the primary interface for Kubernetes interaction.

  * **IV. Advise the developers to open three terminals...**

    * **Inefficient:** Manually switching context in separate terminals is cumbersome and less manageable than a centralized configuration file.

**Reference:**  
<https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/>

</details>

---

### Exam 3 · Q38

**In the development process of a Cloud Function triggered by Cloud Storage events, your team seeks to streamline testing and development while adhering to Google-recommended best practices. Which method should you employ?**

- III. Set up the Functions Framework library and configure the Cloud Function on a local environment. Duplicate the function and modify the new version. Use curl to test the updated version locally.
- II. Duplicate the Cloud Function and refactor the code to trigger on HTTP requests. Test the updated version by invoking the HTTP endpoint and assess functionality using mock requests.
- IV. Duplicate the Cloud Function in the Google Cloud console and edit the source code of the new function using the in-line editor. Adapt your web application to call the new function and test the updated version in production.
- I. Develop a new Cloud Function triggered by Cloud Audit Logs detecting the cloudfunctions.functions.sourceCodeSet operation in the original Cloud Function. Evaluate functionality using mock requests.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Set up the Functions Framework library and configure the Cloud Function on a local environment. Duplicate the function and modify the new version. Use curl to test the updated version locally.

**Correct Answer:**

  * **III. Set up the Functions Framework library and configure the Cloud Function on a local environment. Duplicate the function and modify the new version. Use curl to test the updated version locally.**

**Justification:**

  * **Local Development:** The Functions Framework allows you to emulate Cloud Function behavior directly on your local machine, accelerating development and testing cycles.

  * **Isolation:** Testing changes locally before deploying them to the cloud environment minimizes the risk of introducing errors in production.

  * **Ease of Testing:** Using `curl` or other HTTP tools lets you easily send mock requests and verify your function's behavior.

**Why Other Options Are Less Ideal:**

  * **I. Develop a new Cloud Function triggered by Cloud Audit Logs...**

    * **Complexity:** While feasible, setting up another Cloud Function just for testing introduces unnecessary complexity and overhead.

  * **II. Duplicate the Cloud Function and refactor the code to trigger on HTTP requests...**

    * **Limited Testing:** This approach can be useful for basic HTTP testing, but it doesn't fully simulate the Cloud Storage event trigger behavior.

  * **IV. Duplicate the Cloud Function in the Google Cloud console ...**

    * **Production Risk:** Testing directly in a production environment is risky and strongly discouraged. It could lead to unexpected behavior for users.

**References:**

[https://cloud.google.com/functions/docs/running/function-frameworks](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/running/calling#cloudevent_functions](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/writing/write-event-driven-functions ](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

[https://cloud.google.com/functions/docs/calling/storage](https://cloud.google.com/functions/docs/running/function-frameworks  https://cloud.google.com/functions/docs/running/calling#cloudevent_functions  https://cloud.google.com/functions/docs/running/overview#choosing_an_abstraction_layer  https://cloud.google.com/functions/docs/writing/write-event-driven-functions   https://cloud.google.com/functions/docs/calling/storage)

</details>

---

### Exam 3 · Q48

**Your company stores its source code in a Cloud Source Repositories repository. The company aims to build and test the code with each source code commit to the repository, seeking a managed solution with minimal operational overhead. Which method should they use?**

- IV. Implement a source code commit trigger to send a message to a Cloud Pub/Sub topic, subsequently activating an App Engine service to build the source code.
- II. Deploy Jenkins via the Google Cloud Platform Marketplace, set up to monitor source code commits.
- I. Utilize Cloud Build with a trigger configured for each source code commit.
- III. Employ a Compute Engine virtual machine instance with an open-source continuous integration tool, configured to monitor source code commits.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Utilize Cloud Build with a trigger configured for each source code commit.

**I. Utilize Cloud Build with a trigger configured for each source code commit.**

Here's why this is the best choice:

  * **Managed Service:** Cloud Build is a serverless CI/CD solution from Google Cloud, minimizing operational burden compared to self-managing CI tools.

  * **Integration:** Cloud Build has direct integration with Cloud Source Repositories, simplifying setup.

  * **Flexibility:** Cloud Build can be customized for various build and test scenarios.

**Why Other Options Are Less Ideal:**

  * **II. Deploy Jenkins via the Google Cloud Platform Marketplace ...** Jenkins is a versatile CI tool, but deploying it through the Marketplace still involves managing a VM, updates, etc., increasing operational overhead.

  * **III. Employ a Compute Engine virtual machine instance ...** This approach has the most operational overhead, requiring provisioning, OS maintenance, and CI tool configuration.

  * **IV. Implement a source code commit trigger to send a message ...** While feasible, this introduces more moving parts (Pub/Sub, App Engine), adding complexity compared to the direct Cloud Build integration.

</details>

---

### Exam 3 · Q50

**You are setting up a continuous integration pipeline with Cloud Build to automate the deployment of new container images to Google Kubernetes Engine (GKE). The pipeline includes building the application from its source code, running unit and integration tests separately, and pushing the container to Container Registry. The application operates on a Python web server.**

**The Dockerfile provided is as follows:**

- I. Select a virtual machine (VM) size with higher CPU for Cloud Build runs.
- V. Store application source code on Cloud Storage, and configure the pipeline to use gsutil to download the source code.
- II. Deploy a Container Registry on a Compute Engine VM in a VPC, and utilize it to store the final images.
- IV. Change the base image in the Dockerfile to ubuntu:latest, and install Python 3.7 using a package manager utility.
- III. Cache the Docker image for subsequent builds using the --cache-from argument in your build config file.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Select a virtual machine (VM) size with higher CPU for Cloud Build runs. **|** III. Cache the Docker image for subsequent builds using the --cache-from argument in your build config file.

I. **Select a virtual machine (VM) size with higher CPU for Cloud Build runs:**

  * **Cloud Build allows you to specify machine type and size for your builds.**

  * **Choosing a VM size with higher CPU can speed up build times, especially for CPU-intensive tasks like building Docker images.**

  * **This option can improve build performance and reduce overall pipeline execution time.**

II. **Deploy a Container Registry on a Compute Engine VM in a VPC, and utilize it to store the final images:**

  * Google Container Registry (GCR) is a managed Docker container registry that integrates well with Google Cloud Platform services like Cloud Build and GKE.

  * GCR provides secure, reliable, and scalable storage for Docker images without the need to manage infrastructure.

  * Deploying a separate Container Registry on Compute Engine adds unnecessary complexity and maintenance overhead compared to using GCR directly.

III. **Cache the Docker image for subsequent builds using the --cache-from argument in your build config file:**

  * **Cloud Build supports caching Docker images to improve build performance.**

  * **By caching Docker images, subsequent builds can reuse layers from previous builds, reducing build times.**

  * **This option helps optimize build times and improve pipeline efficiency.**

IV. **Change the base image in the Dockerfile to ubuntu:latest, and install Python 3.7 using a package manager utility:**

  * Changing the base image to Ubuntu and installing Python 3.7 using a package manager utility like apt can introduce compatibility issues.

  * The Docker image might not match the runtime environment of Google Kubernetes Engine, which typically uses container-optimized OS images.

  * It's generally recommended to use base images specifically designed for container environments to ensure compatibility and security.

V. **Store application source code on Cloud Storage, and configure the pipeline to use gsutil to download the source code:**

  * Storing application source code on Cloud Storage and using gsutil to download it adds unnecessary complexity to the pipeline.

  * Cloud Build provides native integration with source code repositories like Cloud Source Repositories or GitHub.

  * Leveraging native integrations simplifies pipeline configuration and management.

Considering the requirements and best practices, the most suitable options would be:

  * **I. Select a virtual machine (VM) size with higher CPU for Cloud Build runs.**

  * **III. Cache the Docker image for subsequent builds using the --cache-from argument in your build config file.**

These options optimize build performance and efficiency without introducing unnecessary complexity or potential compatibility issues.

References:  
[https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds https://cloud.google.com/build/docs/optimize-builds/building-leaner-containers#building_leaner_containers](https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds   https://cloud.google.com/build/docs/optimize-builds/building-leaner-containers#building_leaner_containers  https://cloud.google.com/build/docs/optimize-builds/speeding-up-builds#using_a_cached_docker_image)

[https://cloud.google.com/build/docs/optimize-builds/speeding-up-builds#using_a_cached_docker_image](https://cloud.google.com/build/docs/optimize-builds/increase-vcpu-for-builds   https://cloud.google.com/build/docs/optimize-builds/building-leaner-containers#building_leaner_containers  https://cloud.google.com/build/docs/optimize-builds/speeding-up-builds#using_a_cached_docker_image)

</details>

---

### Exam 3 · Q51

**To migrate an independent Java application operating on an on-premises Linux virtual machine (VM) to Google Cloud cost-effectively without employing the lift-and-shift method, the plan is to modernize the application by converting it to a container. How should this task be accomplished?**

- I. Employ Migrate for Anthos to transition the VM to your Google Kubernetes Engine (GKE) cluster as a container.
- IV. Utilize Jib to construct a Docker image from your source code, subsequently uploading it to Artifact Registry. Then, deploy the application within a GKE cluster and perform testing.
- III. Use Migrate for Compute Engine to transfer the VM to a Compute Engine instance, and leverage Cloud Build for container conversion.
- II. Export the VM as a raw disk and import it as an image. Then, instantiate a Compute Engine instance from the imported image.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Jib to construct a Docker image from your source code, subsequently uploading it to Artifact Registry. Then, deploy the application within a GKE cluster and perform testing.

**The most appropriate approach for modernizing the Java application by converting it into a container on Google Cloud would be option IV:**

**IV. Utilize Jib to construct a Docker image from your source code, subsequently uploading it to Artifact Registry. Then, deploy the application within a GKE cluster and perform testing.**

**Explanation:**

  1. Jib: Jib is a tool provided by Google for building Docker and OCI images for Java applications without needing to write a Dockerfile or manage Docker daemon. Jib integrates seamlessly with Maven or Gradle, making it easy to build container images directly from your Java source code.

  2. **Artifact Registry** : Artifact Registry is a managed service provided by Google Cloud for storing and managing container images. Once the Docker image is built using Jib, you can upload it to Artifact Registry for secure storage and distribution.

  3. **Deploy to GKE** : Google Kubernetes Engine (GKE) is a managed Kubernetes service provided by Google Cloud. Once the Docker image is stored in Artifact Registry, you can deploy it to GKE for container orchestration. GKE offers scalability, reliability, and ease of management for running containerized applications.

Options I, II, and III are not the best fit for modernizing the application as described:

I. Migrate for Anthos is a tool for modernizing and migrating workloads to containers and Kubernetes, but it's typically used for more complex applications that may require additional refactoring or integration with Kubernetes features. For a simple Java application, using Jib and deploying to GKE directly would be more straightforward and cost-effective.

II. Exporting the VM as a raw disk and importing it as an image to instantiate a Compute Engine instance doesn't involve containerization. While it can migrate the application to Google Cloud, it doesn't achieve the modernization goal of running the application in a containerized environment.

III. Migrate for Compute Engine is a tool for migrating VMs to Compute Engine instances, but it doesn't inherently involve containerization. Leveraging Cloud Build for container conversion might add unnecessary complexity compared to using Jib directly for building Docker images.

**Reference:**

<https://cloud.google.com/blog/products/application-development/introducing-jib-build-java-docker-images-better>

</details>

---

### Exam 3 · Q60

**You manage an application hosted on a production Google Kubernetes Engine (GKE) cluster, deploying updates through Cloud Deploy. As you anticipate frequent code modifications, you need tools to test these changes locally. These tools should:**

  * **Automate testing of local changes.**

  * **Ensure local deployment mirrors production deployment.**

**Which tools should you select to test container building and execution on your local machine with minimal resource usage?**

- I. Docker Compose and dockerd
- III. Minikube and Skaffold
- II. Terraform and kubeadm
- IV. kaniko and Tekton

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Minikube and Skaffold

**Correct Option:** **III. Minikube and Skaffold**

**Explanation:**

  * **Minikube:** This provides a lightweight, single-node Kubernetes cluster on your local machine, replicating a production-like environment for testing.

  * **Skaffold:** Skaffold handles local container builds, pushes them to a registry, and deploys them to the Minikube cluster. It also automates rebuilds/redeploys whenever you make local code changes. This combination is optimized for developer experience and resource efficiency during local testing.

**Why other options are less suitable:**

  * **I. Docker Compose and dockerd:** Docker Compose helps with container orchestration but doesn't fully emulate a Kubernetes environment, making it less ideal for ensuring your local deployment mirrors production. `dockerd` focuses on image management rather than the full deployment process.

  * **II. Terraform and kubeadm:** This combination focuses on infrastructure provisioning (GKE cluster creation) rather than streamlined local development and testing workflows.

  * **IV. kaniko and Tekton:** Kaniko is useful for building container images within a Kubernetes cluster, and Tekton provides a CI/CD framework. While powerful, they are heavier solutions than necessary for optimized local development and testing.

</details>

---

### Exam 4 · Q3

**You've developed an application intended for Cloud Run, where log records are currently being stored as text in local files. To optimize maintenance and ensure logs are directed to Cloud Logging, what approach is recommended?**

- I. Integrate the Cloud Logging library into your codebase and utilize it for logging purposes.
- II. Direct logs to Standard Output (stdout) and Standard Error (stderr) streams using your programming language's logger.
- IV. Set up a cron job to transfer the log files to Cloud Storage once per day for archival purposes.
- III. Make the log files accessible via a public URL like www.mycompany.com/logs, manually download them, and then upload to Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Direct logs to Standard Output (stdout) and Standard Error (stderr) streams using your programming language's logger.

Correct answer

**II. Use your programming language logger to write logs to Standard output (stdout) and Standard error (stderr) streams.**

Justifications:

I. This is incorrect. While it's technically possible to use the library, that would result in a lot of code to maintain.  
II. This is correct. Cloud Run has direct integration to Cloud Logging via stdout and stderr.  
III. This is incorrect. This task would have to be performed manually. Also this approach isn’t the most secure.  
IV. This is incorrect. While data can be copied to Cloud Storage buckets, this doesn't help us with our goal of storing log data within Cloud Logging.

**References:**

[https://cloud.google.com/run/docs/logging#container-logs](%0d https:/cloud.google.com/run/docs/logging#container-logs)

[https://cloud.google.com/logging/docs/reference/libraries](%0d https:/cloud.google.com/logging/docs/reference/libraries%0d)

</details>

---

### Exam 4 · Q6

**What action should you take to ensure that the Cloud Function is deleted even if the test fails during the automated testing process?**

- I. Change the order of the steps to delete the Cloud Function before performing the test.
- IV. Have the Cloud Build test step set its outcome in an environment variable called result and return 0. Add a final step after the Cloud Function deletion that checks whether the environment variable contains the expected results.
- II. Include a waitFor option in the Cloud Build step that deletes the Cloud Function test step as a required preceding step.
- III. Have the Cloud Build step write the Cloud Function results to a file and return 0. Add a step after the Cloud Function deletion that checks whether the file contains the expected results and fails if it doesn't.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Have the Cloud Build step write the Cloud Function results to a file and return 0. Add a step after the Cloud Function deletion that checks whether the file contains the expected results and fails if it doesn't.

The most suitable action to ensure that the Cloud Function is deleted even if the test fails during the automated testing process is:

**III. Have the Cloud Build step write the Cloud Function results to a file and return 0. Add a step after the Cloud Function deletion that checks whether the file contains the expected results and fails if it doesn't.**

Explanation:

Option I suggests changing the order of the steps to delete the Cloud Function before performing the test. While this might ensure that the Cloud Function is deleted regardless of the test outcome, it doesn't address the issue of handling a failed test effectively.

Option II proposes including a waitFor option in the Cloud Build step that deletes the Cloud Function test step as a required preceding step. This approach might ensure that the Cloud Function is deleted only if the test step succeeds, but it doesn't provide a mechanism to handle a failed test and still delete the Cloud Function.

Option IV suggests having the Cloud Build test step set its outcome in an environment variable and adding a final step to check whether the variable contains the expected results. While this approach allows for capturing the test outcome, it doesn't ensure that the Cloud Function is deleted if the test fails.

Option III is the recommended approach because it involves writing the Cloud Function results to a file during the Cloud Build step and then adding a subsequent step to check whether the file contains the expected results. If the test fails, the subsequent step can still execute and verify whether the Cloud Function was deleted as expected, ensuring cleanup regardless of the test outcome.

Therefore, option III is the most suitable action to ensure that the Cloud Function is deleted even if the test fails during the automated testing process.

**Documentation** :

  * Cloud Build: <https://cloud.google.com/build/docs/automating-builds/create-manage-triggers>

</details>

---

### Exam 4 · Q8

**You are developing an application with a microservices architecture that includes Cloud Run, Bigtable, and Pub/Sub. To create a minimally viable product, you want to complete the testing and debugging process quickly and at minimal cost. What is the best approach?**

- D. Use Cloud Code for developing, deploying, and testing microservices, and review logs with Cloud Logging.
- C. Use Cloud Build to set up a pipeline, adding stages for unit testing and manual approval, then deploy the code to your Google Cloud project.
- B. Use emulators to locally test cloud resources, then deploy the code to your Google Cloud project.
- A. Use Cloud Shell Editor and Cloud Shell for deployment, and test the application using the Google Cloud Console in the project.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use emulators to locally test cloud resources, then deploy the code to your Google Cloud project.

The correct answer is

**B. Use emulators to locally test cloud resources, then deploy the code to your Google Cloud project.**

Explanation:

Using **emulators** is the best approach for quick and cost-effective testing of cloud services in a development environment. Google Cloud provides emulators for services like **Bigtable** and **Pub/Sub** that allow you to simulate the behavior of these resources on your local machine without incurring cloud costs. By testing your application locally with emulators, you can debug and validate its functionality before deploying to Google Cloud, saving both time and expenses in the early stages of development.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Shell Editor and Cloud Shell for deployment, and test the application using the Google Cloud Console in the project**  
While Cloud Shell provides a development environment, testing entirely in the cloud could incur higher costs due to resource usage. This option is less suitable for minimizing costs during the MVP phase compared to using local emulators.

  * **Option C: Use Cloud Build to set up a pipeline, adding stages for unit testing and manual approval, then deploy the code to your Google Cloud project**  
While CI/CD pipelines are valuable, setting up a full Cloud Build pipeline for an MVP may be unnecessary overhead. Emulators offer a simpler and more cost-effective solution for early-stage testing.

  * **Option D: Use Cloud Code for developing, deploying, and testing microservices, and review logs with Cloud Logging**  
Cloud Code is helpful for microservices development but involves deploying to Google Cloud for testing, which can incur additional costs. Emulators provide a more cost-efficient local testing option.

**Relevant Documentation:**

For more information on using emulators in Google Cloud, refer to:

  * [Google Cloud Bigtable Emulator](https://cloud.google.com/bigtable/docs/emulator)

  * [Google Cloud Pub/Sub Emulator](https://cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/EMULATOR)

</details>

---

### Exam 4 · Q9

**Your company recently deployed a new API to the App Engine Standard environment. However, during testing, the API isn't functioning as anticipated. You aim to continuously monitor the application to diagnose potential issues within the application code without necessitating redeployment. Which tool is most suitable for this purpose?**

- IV. Implement Stackdriver Debug Logpoints to dynamically insert log statements into the running application code for real-time debugging.
- III. Make use of Stackdriver Debug Snapshots to capture and analyze application state and variables at specific points in time.
- II. Employ Stackdriver Monitoring to track and monitor the health and performance metrics of the deployed API.
- I. Utilize Stackdriver Trace to trace and analyze request latency and performance across the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Implement Stackdriver Debug Logpoints to dynamically insert log statements into the running application code for real-time debugging.

**Correct Option:**

  * **IV. Implement Stackdriver Debug Logpoints to dynamically insert log statements into the running application code for real-time debugging.**

**Reasoning:**

  * **Dynamic Logging:** Stackdriver Debug Logpoints provide the most appropriate approach in this scenario because they allow you to add detailed log statements directly into your running code without the need for code changes or redeployment. This enables you to gather real-time insights into the application's behavior and pinpoint the root cause of the unexpected issues.

**Incorrect Options and Why:**

  * **I. Utilize Stackdriver Trace to trace and analyze request latency and performance across the application.**

    * While Stackdriver Trace is valuable, it focuses on tracing requests and uncovering latency bottlenecks within a distributed system. It's less suited for diagnosing issues within the code itself without changes.

  * **II. Employ Stackdriver Monitoring to track and monitor the health and performance metrics of the deployed API.**

    * Stackdriver Monitoring provides insights into the API's overall health and resource usage. It's helpful for general health checks but doesn't offer the granular code-level debugging needed in this case.

  * **III. Make use of Stackdriver Debug Snapshots to capture and analyze application state and variables at specific points in time.**

    * Although Stackdriver Debug Snapshots are useful for debugging, they provide a static view of the application's state at a given moment. Logpoints offer a more dynamic and real-time perspective, which is better suited to finding issues in a continuously running application.

**Supporting Documentation:**

  * **Stackdriver Debugger (Logpoints):** <https://cloud.google.com/blog/products/gcp/add-log-statements-to-your-application-on-the-fly-with-stackdriver-debugger-logpoints/>

  * **Stackdriver Trace:** <https://cloud.google.com/trace>

  * **Stackdriver Monitoring:** <https://cloud.google.com/monitoring>

</details>

---

### Exam 4 · Q21

**To swiftly assess Pub/Sub integration for each new build of a web application that publishes messages to Pub/Sub, how should local testing be configured?**

- II. Use gcloud to install the Pub/Sub emulator, initiating it with a valid Google Project ID. Configure the local application to use the emulator by exporting the PUBSUB_EMULATOR_HOST variable.
- I. Enable the Pub/Sub API in the Google Cloud console and configure the local application to call pubsub.googleapis.com.
- IV. Install Cloud Code in the integrated development environment (IDE), enable Pub/Sub in the Cloud APIs against a valid Google Project ID, and configure the local application to call pubsub.googleapis.com.
- III. Set the Pub/Sub endpoint to the emulator by executing 'gcloud config set api_endpoint_overrides/pubsub https://pubsubemulator.googleapis.com.com/' before starting the application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Use gcloud to install the Pub/Sub emulator, initiating it with a valid Google Project ID. Configure the local application to use the emulator by exporting the PUBSUB_EMULATOR_HOST variable.

**II. Use gcloud to install the Pub/Sub emulator, initiating it with a valid Google Project ID. Configure the local application to use the emulator by exporting the PUBSUB_EMULATOR_HOST variable.**

**Explanation:**

  * **Emulator for Local Testing:** The Pub/Sub emulator provides a local environment that mimics the production Pub/Sub service, allowing you to test your integration without interacting with the actual cloud service.

  * **gcloud for Setup:** gcloud offers a convenient way to manage the installation and initiation of the emulator.

  * **PUBSUB_EMULATOR_HOST:** This environment variable ensures your local application correctly targets the emulator instead of the production service during development.

**Why Other Options Are Less Ideal:**

  * **I. Enable the Pub/Sub API in the Google Cloud console and configure the local application to call pubsub.googleapis.com.** This would connect your local application to the production Pub/Sub service, not ideal for isolated development and testing.

  * **III. Set the Pub/Sub endpoint to the emulator by executing 'gcloud config set api_endpoint_overrides/pubsub**[**https://pubsubemulator.googleapis.com.com/**](https://pubsubemulator.googleapis.com.com/)**' before starting the application.** This endpoint is not valid. The emulator runs locally, and you'd use the `PUBSUB_EMULATOR_HOST` to point to it.

  * **IV. Install Cloud Code in the integrated development environment (IDE), enable Pub/Sub in the Cloud APIs against a valid Google Project ID, and configure the local application to call pubsub.googleapis.com.** Cloud Code might provide some tools, but it unnecessarily adds IDE dependencies and, by default, would still connect to the production service.

**Reference:**

<https://cloud.google.com/pubsub/docs/emulator>

</details>

---

### Exam 4 · Q28

**To align with your company's IAM tracking procedures and support rapid release cycles with minimal merge conflicts, how should you design a version control system?**

- III. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and implement trunk-based development.
- IV. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and employ feature-based development.
- I. Establish a Cloud Source Repositories repository and implement trunk-based development.
- II. Set up a Cloud Source Repositories repository and employ feature-based development.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Establish a Cloud Source Repositories repository and implement trunk-based development.

**Likely Best Solution:**

**I. Establish a Cloud Source Repositories repository and implement trunk-based development.**

  * **IAM Tracking:** Cloud Source Repositories integrates well with Google Cloud's IAM auditing and logging, providing a clear audit trail for changes.

  * **Reduced Merge Conflicts:** Trunk-based development encourages small, frequent commits to the main branch, minimizing the likelihood of large, complex merge conflicts.

**Consideration if GitHub is Mandated:**

**III. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and implement trunk-based development.**

  * **Workflow Familiarity:** Allows developers to leverage GitHub if it's their preferred tool.

  * **IAM Tracking:** Mirroring to Cloud Source Repositories ensures IAM auditability within Google Cloud.

  * **Potential Complexity:** Maintaining synchronization between repositories introduces a slight overhead.

**Why the Feature Branch Options Are Less Ideal:**

  * **II. Set up a Cloud Source Repositories repository and employ feature-based development.** Feature branches, while common, increase the potential for larger merge conflicts, especially in rapid release environments.

  * **IV. Create a GitHub repository, mirror it to a Cloud Source Repositories repository, and employ feature-based development.** Adds the complexity of mirroring on top of the merge conflict concerns with feature branches.

</details>

---

### Exam 4 · Q38

**As a lead developer, you need to recommend a development environment for an organization that recently integrated multiple Google Cloud services within VPC environments secured by VPC Service Controls and Private Service Connect endpoints. Developers use various operating systems, frameworks, and IDEs. Your recommendation should:**

  * **Enforce consistent security controls.**

  * **Access Google Cloud resources and applications within the VPC.**

  * **Allow installation of custom tools and utilities in the development environments.**

**What solution should you recommend?**

- D. Use the Cloud Code extension with the organization’s IDEs and enable access to VPC services using Identity-Aware Proxy.
- B. Use Cloud Workstations with preconfigured base images, and for custom tools and utilities, use custom images that are rebuilt weekly.
- C. Use the Cloud Code extension with the organization’s IDEs and configure Cloud VPN for VPC access.
- A. Use Cloud Workstations and allow developers to create custom images as needed.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Cloud Workstations with preconfigured base images, and for custom tools and utilities, use custom images that are rebuilt weekly.

**B. Use Cloud Workstations with preconfigured base images, and for custom tools and utilities, use custom images that are rebuilt weekly.**

**Explanation:**

**Why B is the best choice:**

  * **Enforces Consistent Security Controls:**

    * Preconfigured base images ensure that all development environments start with a standardized security baseline.

    * Weekly rebuilds guarantee that the latest security patches and configurations are applied.

  * **Access to Google Cloud Resources and Applications within the VPC:**

    * Cloud Workstations provide a secure and isolated development environment that can access VPC resources and applications.

    * VPC Service Controls and Private Service Connect ensure that only authorized resources can access the VPC.

  * **Allows Installation of Custom Tools and Utilities:**

    * Custom images enable developers to install specific tools and utilities tailored to their needs, while maintaining security standards.

    * Weekly rebuilds of custom images keep them up-to-date and secure.

**Why other options are not as suitable:**

  * **A. Cloud Workstations with Custom Images:** While this option provides flexibility, it can lead to inconsistencies in security configurations if not managed carefully.

  * **C. Cloud Code Extension with Cloud VPN:** This option can be complex to set up and manage, and it may not provide the same level of security and isolation as Cloud Workstations.

  * **D. Cloud Code Extension with Identity-Aware Proxy:** This option can be more complex to configure and manage than Cloud Workstations, and it may not provide the same level of security and isolation.

By choosing Option B, the organization can balance security, flexibility, and developer productivity.

**For more information, refer to the following documentation:**

  * Cloud Workstations: <https://cloud.google.com/workstations/docs>

  * VPC Service Controls: <https://cloud.google.com/vpc-service-controls/docs>

  * Private Service Connect: <https://cloud.google.com/vpc/docs/private-service-connect>

</details>

---

### Exam 4 · Q46

**To troubleshoot the performance difference between your locally tested application and its deployed version on a Compute Engine instance with minimal adjustments, what approach is recommended?**

- II. Utilize Cloud Debugger snapshots to examine a specific moment in the application's execution.
- IV. Integrate logging commands into the application and use Cloud Logging to identify areas of latency.
- III. Leverage Cloud Profiler to identify the functions within the application that consume the most time.
- I. File a ticket with Cloud Support to report the performance gap between local and deployed environments.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Leverage Cloud Profiler to identify the functions within the application that consume the most time.

The recommended approach for troubleshooting the performance difference between a locally tested application and its deployed version on a Compute Engine instance with minimal adjustments is:

**III. Leverage Cloud Profiler to identify the functions within the application that consume the most time.**

Explanation:

  1. **Identifying Performance Bottlenecks** : Cloud Profiler is a powerful tool designed specifically for analyzing the performance of applications running on Google Cloud Platform. It provides detailed insights into which functions or methods within your application are consuming the most time, helping you identify performance bottlenecks.

  2. **Minimal Adjustments** : Cloud Profiler requires minimal adjustments to your application code or deployment configuration. Once enabled, it automatically profiles your application's performance without requiring significant modifications.

Options I, II, and IV are not the most suitable for this scenario:

I. Filing a ticket with Cloud Support may not be the most efficient or effective approach for troubleshooting performance differences, especially when there are dedicated tools available for performance analysis like Cloud Profiler. Support tickets are typically reserved for addressing technical issues or inquiries that cannot be resolved through self-service methods.

II. While Cloud Debugger can be useful for examining specific moments in the application's execution, it may not provide comprehensive insights into overall performance differences between the local and deployed environments. Cloud Debugger is more focused on debugging specific issues or errors rather than performance analysis.

IV. Integrating logging commands into the application and using Cloud Logging can help identify areas of latency, but it may not provide the detailed insights into performance bottlenecks that Cloud Profiler offers. Logging can be useful for capturing information about application behavior, but it may not be as effective for pinpointing specific performance issues within the codebase.

Therefore, leveraging Cloud Profiler to identify the functions within the application that consume the most time is the recommended approach for troubleshooting performance differences between a locally tested application and its deployed version on a Compute Engine instance with minimal 

**Reference:**

<https://cloud.google.com/profiler/docs/>

</details>

---

### Exam 4 · Q47

**As a developer within a large organization utilizing Git for source code management (SCM), you aim to align your team with Google-recommended best practices to enhance software delivery efficiency. Which SCM process should your team adopt?**

- III. Each developer creates a branch for their individual work, commits their changes to their branch, and merges their code into the main branch on a daily basis.
- IV. Groups of developers create a feature branch from the main branch for their work, commit their changes to their branch, and merge their code into the main branch following approval from the change advisory board.
- II. Groups of developers copy the repository, commit their changes to their respective repositories, and merge their code into the main repository before each product release.
- I. Developers commit their code to the main branch before each product release, conduct testing, and initiate rollbacks if integration issues arise.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Groups of developers create a feature branch from the main branch for their work, commit their changes to their branch, and merge their code into the main branch following approval from the change advisory board.

**Correct Option:**

  * **IV. Groups of developers create a feature branch from the main branch for their work, commit their changes to their branch, and merge their code into the main branch following approval from the change advisory board.**

**Justification:**

  * **Feature Branch Workflow:** This approach is the core of GitFlow (and similar branching strategies), a widely-adopted model that aligns with Google's best SCM practices. Feature branches promote collaboration while isolating changes, reducing the risk of conflicts and errors in the main branch.

  * **Change Approval:** Having a change advisory board ensures code quality and adherence to standards before integrating features into the main branch.

  * **Collaboration and Isolation:** This process fosters teamwork while keeping unreviewed code safely out of the main branch, aiding quality control.

**Why Other Options Are Not Ideal:**

  * **I. Developers commit their code to the main branch...**

    * **High Risk:** Directly committing to the main branch increases the likelihood of introducing errors and breaking the build.

  * **II. Groups of developers copy the repository...**

    * **Inefficient Merging:** Merging changes from separate repositories adds complexity and increases the risk of conflicts.

    * **Coordination Overhead:** Maintaining multiple repositories for a single project demands extra coordination.

  * **III. Each developer creates a branch...**

    * **Code Review:** Lacks a formal code review process, which could lead to quality issues slipping into the main branch.

</details>

---

### Exam 4 · Q48

**You’re preparing to load test a Cloud Run service using JMeter and need to orchestrate the process and tools for effective testing and analysis. You aim to follow Google’s recommended practices. What steps should you take?**

- **D.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to **BigQuery** , and use **Looker Studio** for analysis.
- **A.** Install **JMeter** on your local machine, set up a log sink to **BigQuery** , and use **Looker** to analyze the test results.
- **C.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to a **Cloud Storage** bucket, and use **Looker** for analysis.
- **B.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to a **Cloud Storage** bucket, and use **Looker Studio** for analysis.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **D.** Set up a **Compute Engine** instance, install **JMeter** on the instance, create a log sink to **BigQuery** , and use **Looker Studio** for analysis.

The correct answer is 

**D. Set up a Compute Engine instance, install JMeter on the instance, create a log sink to BigQuery, and use Looker Studio for analysis.**

Explanation:

Following Google’s recommended practices for load testing a **Cloud Run** service involves the following key steps:

  1. **Use a dedicated Compute Engine instance for JMeter** : Running JMeter on a Compute Engine instance allows you to scale your load tests independently of your local resources, ensuring consistent and high-performance load testing without impacting your local network or machine.

  2. **Create a log sink to BigQuery** : BigQuery is designed to handle large volumes of log data efficiently, making it ideal for storing and querying log data generated during load testing. Using BigQuery allows for detailed analysis, flexible querying, and seamless integration with other Google Cloud tools.

  3. **Use Looker Studio for analysis** : Looker Studio (formerly known as Data Studio) provides a powerful and user-friendly platform for visualizing BigQuery data. By connecting Looker Studio to BigQuery, you can create interactive reports and dashboards to analyze test results and gain insights into performance trends and bottlenecks.

**Justifications for Incorrect Options:**

  * **Option A: Install JMeter on your local machine, set up a log sink to BigQuery, and use Looker to analyze the test results**  
Running JMeter on a local machine is not recommended for load testing at scale. Using a Compute Engine instance provides more consistent resources and scalability. Additionally, Google recommends using **Looker Studio** rather than Looker for direct integration with BigQuery for reporting.

  * **Option B: Set up a Compute Engine instance, install JMeter, create a log sink to a Cloud Storage bucket, and use Looker Studio for analysis**  
Storing logs in **BigQuery** is preferred over Cloud Storage because BigQuery offers efficient querying and analysis capabilities, which are essential for analyzing large volumes of load test data.

  * **Option C: Set up a Compute Engine instance, install JMeter, create a log sink to Cloud Storage, and use Looker for analysis**  
This approach is incorrect due to both the use of **Cloud Storage** (instead of BigQuery) for logs and **Looker** (instead of Looker Studio) for analysis. BigQuery and Looker Studio are better suited for handling and visualizing large-scale load testing data.

</details>

---

### Exam 4 · Q52

**In an application utilizing Cloud Spanner as its primary datastore, how can you prevent performance regressions by running automated performance tests for each commit made via Cloud Build, ensuring concurrent test execution for multiple commits?**

- IV. Initiate the Cloud Spanner emulator locally, load necessary data, and shut down the emulator after test execution.
- I. Generate a new project with a random name for every build, load necessary data, and delete the project post-test execution.
- II. Establish a new Cloud Spanner instance for each build, load the requisite data, and delete the Cloud Spanner instance after testing.
- III. Set up a project with a Cloud Spanner instance containing the required data, and modify the Cloud Build build file to restore data to its initial state automatically post-test.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Establish a new Cloud Spanner instance for each build, load the requisite data, and delete the Cloud Spanner instance after testing.

The **correct answer is:**

✅ **II. Establish a new Cloud Spanner instance for each build, load the requisite data, and delete the Cloud Spanner instance after testing.**

✅ **Explanation for Correct Option:**

**II. Create a new Cloud Spanner instance per build**

  * This approach ensures **isolation** between test runs from different commits.

  * It **avoids shared-state conflicts** , enables **parallel execution** , and provides a **realistic performance environment** , since you’re testing against **actual Cloud Spanner infrastructure**.

  * You can use **Cloud Build** to script instance creation, schema/data loading, testing, and teardown.

  * Although it incurs cost, it’s optimal for **realistic, scalable, and concurrent performance testing**.

**Official Documentation:**

  * Cloud Spanner performance testing guide: https://cloud.google.com/spanner/docs/performance

  * Cloud Build integration: https://cloud.google.com/build/docs/configuring-builds/run-bash-scripts

  * Instance creation via gcloud: https://cloud.google.com/spanner/docs/instances

❌ **Explanation for Incorrect Options:**

**I. Generate a new project per build**

  * **Creating a new GCP project for each build** is **time-consuming** , involves **org-level permissions** , and **slow resource provisioning**.

  * It is **not recommended** for fast, automated CI pipelines.

  * Project creation can also hit **quota limits** and requires IAM & billing setup.

**III. Reuse a single Spanner instance**

  * **Sharing a single Spanner instance** across builds may lead to **race conditions** and **non-deterministic test results**.

  * Resetting data between tests introduces complexity and increases chances of **state leakage or contention** , particularly with concurrent builds.

**IV. Use the Cloud Spanner emulator locally**

  * The **Spanner emulator does not simulate performance characteristics of the real service** (e.g., latency, transactions).

  * Good for functional unit tests, **but not suitable for performance benchmarking** or scalability tests.

**Reference:**  
https://cloud.google.com/spanner/docs/emulator

📌 **Best Practice:**  
Use **Cloud Build** to:

  1. **Create a new Cloud Spanner instance.**

  2. **Load schema and test data.**

  3. **Run performance tests.**

  4. **Delete the instance post-test.**

This ensures **concurrency, test isolation, and reliable performance metrics**.

</details>

---

### Exam 4 · Q53

**As you monitor a Go-based web application deployed on Google Kubernetes Engine, you notice an uptick in CPU and memory usage. How can you pinpoint the functions consuming the most CPU and memory resources?**

- III. Implement OpenTelemetry and Trace export packages within the application and set up the trace provider. Analyze latency data for the application on the Trace overview page to identify functions causing the most latency.
- IV. Incorporate the Cloud Profiler package into the application and initialize the Profiler agent. Examine the generated flame graph in the Google Cloud console to identify functions with significant time consumption.
- I. Integrate print commands into the application's source code to log function calls, then redeploy the application.
- II. Develop a Cloud Logging query to collect the application's logs. Utilize a Python script to compute the duration between timestamps of the longest functions, aiding in identifying time-intensive functions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Incorporate the Cloud Profiler package into the application and initialize the Profiler agent. Examine the generated flame graph in the Google Cloud console to identify functions with significant time consumption.

**To pinpoint the functions consuming the most CPU and memory resources in a Go-based web application deployed on Google Kubernetes Engine, the most effective approach would be:**

**IV. Incorporate the Cloud Profiler package into the application and initialize the Profiler agent. Examine the generated flame graph in the Google Cloud console to identify functions with significant time consumption.**

**Here's why:**

  1. **Cloud Profiler** : Google Cloud Profiler is specifically designed for profiling applications running on Google Cloud Platform, including applications deployed on Google Kubernetes Engine. It collects CPU and memory allocation data with minimal overhead and provides detailed insights into the performance of the application.

  2. **Flame Graphs** : Cloud Profiler generates flame graphs, which are visual representations of stack traces showing where CPU time is being spent. This allows you to easily identify the functions and code paths that are consuming the most CPU and memory resources.

Option I is less suitable because manually adding print commands to the source code and redeploying the application can be time-consuming and may not provide detailed insights into CPU and memory usage.

Option II involves developing custom scripts to analyze application logs, which may not provide accurate or comprehensive data about CPU and memory usage compared to specialized profiling tools like Cloud Profiler.

Option III suggests using OpenTelemetry and Trace export packages, which are primarily focused on distributed tracing for monitoring application latency and performance. While tracing can provide valuable insights into the performance of distributed systems, it may not provide the detailed CPU and memory profiling needed to identify specific functions causing resource consumption.

**Therefore, option IV, incorporating the Cloud Profiler package into the application and examining the generated flame graph, is the most effective approach for pinpointing the functions consuming the most CPU and memory resources in the Go-based web application deployed on Google Kubernetes Engine.**

**References:**

[https://dev.to/billcchung/profiling-go-grpc-service-with-google-cloud-profiler-1k8l and https://www.cncf.io/blog/2020/03/27/continuous-profiling-go-application-running-in-kubernetes/](https://dev.to/billcchung/profiling-go-grpc-service-with-google-cloud-profiler-1k8l and   https://www.cncf.io/blog/2020/03/27/continuous-profiling-go-application-running-in-kubernetes/)

</details>

---

### Exam 4 · Q55

**How can you ensure that error messages from your Java application appear in the Error Reporting console on Cloud Run?**

- A. Confirm that the Java application includes the necessary Cloud Monitoring client libraries.
- D. Implement logging of exceptions using appropriate logging mechanisms rather than System.out.println.
- C. Validate that application errors are being written to the standard error (stderr) stream.
- B. Ensure that the application logs are correctly directed to the appropriate regional storage bucket.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Validate that application errors are being written to the standard error (stderr) stream.

To ensure that error messages from your Java application appear in the Error Reporting console on Cloud Run, you should:

**C. Validate that application errors are being written to the standard error (stderr) stream.**

Explanation:

Cloud Run automatically captures logs from the standard output (stdout) and standard error (stderr) streams of your containerized application. When an application encounters an error, writing the error message to the stderr stream ensures that Cloud Run captures it and sends it to Cloud Logging. From there, errors can be analyzed and viewed in the Error Reporting console.

Option A, confirming that the Java application includes the necessary Cloud Monitoring client libraries, is not directly related to ensuring error messages appear in the Error Reporting console. While Cloud Monitoring can provide additional monitoring and alerting capabilities, Error Reporting primarily relies on logs captured in Cloud Logging.

Option B, ensuring that the application logs are correctly directed to the appropriate regional storage bucket, is not the recommended approach for Cloud Run. Cloud Run automatically manages logs and directs them to Cloud Logging, where they can be viewed and analyzed, including error messages.

Option D, implementing logging of exceptions using appropriate logging mechanisms rather than System.out.println, is good practice for improving logging clarity and maintainability. However, it does not guarantee that errors will appear in the Error Reporting console unless they are written to stderr.

Therefore, option C is the correct approach to ensure that error messages from your Java application appear in the Error Reporting console on Cloud Run.

**Documentation:**

  * **Error Reporting for Cloud Run** : <https://cloud.google.com/run/docs/error-reporting>

  * <https://cloud.google.com/error-reporting/docs/troubleshooting>

</details>

---

### Exam 6 · Q10

**You are developing a discussion portal hosted on Cloud Run, where incoming requests pass through multiple microservices before a response is returned. Some of these microservices connect to databases. To optimize performance, you want to conduct a load test to identify any potential bottlenecks when the application is under heavy traffic. You plan to follow Google’s recommended practices.**

**What should you do?**

- A. Modify responses to include a time series showing the elapsed time for each service. Then, use Log Analytics in Cloud Logging to create a heatmap highlighting any bottleneck services.
- B**.** Enable Cloud Trace to track requests from load testing clients and review request timings in Cloud Trace.
- C. Expose latency metrics for each service with every request. Set up Google Cloud Managed Service for Prometheus to collect and analyze these metrics.
- D. Add log statements that capture elapsed time for each service. Use BigQuery to analyze the logs and metrics.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B**.** Enable Cloud Trace to track requests from load testing clients and review request timings in Cloud Trace.

**The correct answer is**

**B. Enable Cloud Trace to track requests from load testing clients and review request timings in Cloud Trace.**

Explanation:

**Cloud Trace** is a distributed tracing service designed for tracking request latencies across microservices, which is ideal for identifying bottlenecks in a complex application architecture like the discussion portal. By enabling Cloud Trace, you can capture latency data for each service in the request path, allowing you to pinpoint performance issues and evaluate how each microservice impacts overall response times. Cloud Trace is part of Google’s recommended practices for identifying latency bottlenecks in distributed systems.

Justifications for Incorrect Options:

  * **Option A: Modify responses to include a time series**  
Adding time series data to responses would require substantial changes to response formatting and is not a scalable or efficient way to monitor service latency. Log Analytics is useful but would not offer as comprehensive a view as Cloud Trace for end-to-end request tracking.

  * **Option C: Use Google Cloud Managed Service for Prometheus with latency metrics**  
Exposing latency metrics for each request can be helpful for ongoing monitoring, but Prometheus is less suited for detailed, end-to-end request tracing compared to Cloud Trace, especially in scenarios involving multiple microservices.

  * **Option D: Capture elapsed time with log statements and analyze in BigQuery**  
Logging elapsed times for each service can provide useful data, but it’s less efficient for real-time performance analysis across multiple services. Cloud Trace is specifically optimized for distributed tracing and offers more granular insights into request latency.

**Relevant Documentation:**

For more information, refer to:

  * [Google Cloud Trace Overview](https://cloud.google.com/trace/docs/overview)

</details>

---
