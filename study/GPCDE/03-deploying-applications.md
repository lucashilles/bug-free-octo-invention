# Domain 3 — Configuring and Deploying Applications

104 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q4

**Upon encountering HTTP request failures between two Pods directed at specific URLs, while other requests between the pods to different URLs are successful in your microservices application on Google Kubernetes Engine (GKE) utilizing Istio, what is the probable cause of the connection issue?**

- IV. If the cluster is configured with mTLS in permissive mode but the Pod's sidecar proxy is transmitting unencrypted traffic in plain text, it could lead to connection failures for specific URLs, particularly if mTLS enforcement is mandated for those URLs.
- II. It's plausible that the Pod initiating the HTTP requests is trying to connect to the target Pod via an incorrect TCP port, resulting in failed communication for specific URLs.
- I. The connection issue might stem from a Kubernetes NetworkPolicy resource, which could be limiting HTTP traffic between the Pods, potentially obstructing communication to specific URLs.
- III. The observed connection failures for certain URLs could be attributable to the AuthorizationPolicy of your cluster being configured to block HTTP requests for specific paths within your application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. The observed connection failures for certain URLs could be attributable to the AuthorizationPolicy of your cluster being configured to block HTTP requests for specific paths within your application.

The probable cause of the connection issue between two Pods directed at specific URLs in your microservices application on Google Kubernetes Engine (GKE) utilizing Istio is:

**III. The observed connection failures for certain URLs could be attributable to the AuthorizationPolicy of your cluster being configured to block HTTP requests for specific paths within your application.**

Explanation:

  * Option I suggests that the connection issue might be caused by a Kubernetes NetworkPolicy resource limiting HTTP traffic between the Pods. While NetworkPolicy could potentially cause connectivity problems, it typically applies to all traffic, not specific URLs, making it less likely to be the cause of failures for certain URLs.

  * Option II implies that the failure might be due to incorrect TCP port configuration. However, if other requests between the pods to different URLs are successful, this is less likely to be the cause, as it would likely affect all requests.

  * Option III points to the AuthorizationPolicy of the cluster being configured to block HTTP requests for specific paths within the application. This is a plausible cause, as an AuthorizationPolicy can indeed restrict access to certain URLs based on specific criteria.

  * Option IV mentions the potential mismatch between mTLS configuration and the Pod's sidecar proxy transmitting unencrypted traffic. While this could lead to connection failures, it's less likely if other requests between the pods are successful, as mTLS enforcement would generally apply to all traffic equally.

Therefore, Option III is the most probable cause of the observed connection failures for specific URLs in this scenario.

**References:**

[https://istio.io/latest/docs/tasks/security/authorization/authz-http/](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://kubernetes.io/docs/concepts/services-networking/network-policies/  https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)

[https://kubernetes.io/docs/concepts/services-networking/network-policies0](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://kubernetes.io/docs/concepts/services-networking/network-policies/  https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)

[https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://kubernetes.io/docs/concepts/services-networking/network-policies/  https://istio.io/latest/docs/tasks/security/authentication/mtls-migration/)

</details>

---

### Exam 1 · Q12

**Your application deployed in Google Kubernetes Engine (GKE) is responsible for reading and processing Pub/Sub messages. The message publication rate to the Pub/Sub topic varies significantly throughout the day and week, occasionally leading to large batches of messages being published simultaneously. To ensure timely message processing, what GKE feature should you employ to automatically adjust your workload?**

- I. Vertical Pod Autoscaler in Auto mode.
- III. Horizontal Pod Autoscaler based on an external metric.
- II. Vertical Pod Autoscaler in Recommendation mode.
- IV. Horizontal Pod Autoscaler based on resource utilization.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Horizontal Pod Autoscaler based on an external metric.

**III. Horizontal Pod Autoscaler based on an external metric.**

Here's why this choice is optimal:

  * **Scaling Based on Demand:** A Horizontal Pod Autoscaler (HPA) combined with an external metric like the Pub/Sub backlog will directly scale your pods in proportion to the number of unprocessed messages. This ensures timely processing even during bursts of activity.

  * **Specific to Pub/Sub:** The HPA can leverage metrics from Cloud Monitoring specific to Pub/Sub, such as `pubsub.googleapis.com/subscription/num_undelivered_messages`.

  * **Efficiency:** Horizontal scaling allows you to add/remove processing capacity as needed, optimizing resource usage and cost.

**Why Other Options Are Less Ideal:**

  * **I. Vertical Pod Autoscaler in Auto mode.**

    * Vertical scaling changes the resources allocated to individual pods (CPU/memory). This may not be the most efficient way to handle bursts if your bottleneck is the number of pods rather than per-pod resources.

  * **II. Vertical Pod Autoscaler in Recommendation mode.**

    * Recommendations might be useful for long-term adjustments, but don't address the need for rapid scaling in response to workload spikes.

  * **IV. Horizontal Pod Autoscaler based on resource utilization.**

    * While useful for many scenarios, resource utilization (CPU/memory) might not directly correlate to message backlog. If Pods are processing messages quickly, they might show low CPU usage even with a backlog due to network latency/other factors.

References:

<https://cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics#pubsub>

</details>

---

### Exam 1 · Q14

**You've set up automatic scaling for your Compute Engine instance group based on overall CPU usage. However, you've noticed a significant uptick in response latency as the cluster scales up. To ensure a smoother user experience, you're considering adjustments to the instance group autoscaler configuration. What are the two recommended changes?**

- II. Shorten the cooldown period for newly added instances in the group.
- IV. Decrease the target CPU usage threshold for the instance group autoscaler.
- III. Increase the target CPU usage threshold for the instance group autoscaler.
- V. Remove the health check for individual VMs in the instance group.
- I. Apply the "AUTOSCALE" label to the instance group template.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Shorten the cooldown period for newly added instances in the group. **|** IV. Decrease the target CPU usage threshold for the instance group autoscaler.

**II. Shorten the cooldown period for newly added instances in the group.**

  * **Faster Readiness:** A shorter cooldown period lets new instances handle traffic sooner after being created, reducing the time where existing instances are overloaded.

  * **Cooldown Considerations:** Choose a cooldown period that allows for your application's initialization time. Too short, and new instances will receive traffic before they're ready.

**IV. Decrease the target CPU usage threshold for the instance group autoscaler.**

  * **Proactive Scaling:** Lowering the threshold triggers scaling earlier. This helps avoid the period where existing instances hit high CPU usage (and therefore higher latency) before new ones are added.

  * **Balance with Cost:** Scaling out earlier might increase costs. Tune the threshold to find the sweet spot between responsiveness and efficient resource usage.

**Why Other Options Are Less Ideal**

  * **I. Apply the "AUTOSCALE" label ...** Autoscaling works without an explicit label, this likely won't help your latency issue.

  * **III. Increase the target CPU usage threshold ...** This would worsen the problem. It would delay scaling until instances are even more heavily loaded, leading to worse latency.

  * **V. Remove the health check ...** Health checks are critical! They prevent unhealthy instances from receiving traffic, which would be disastrous for user experience.

</details>

---

### Exam 1 · Q19

**When configuring a Deployment on Google Kubernetes Engine (GKE), including a check to ensure containers can connect to the database, and initiating a graceful shutdown script if connection fails, what configuration should you employ?**

- IV. Configure the Deployment with an initContainer to check service availability. Set up a Prestop lifecycle handler to execute the shutdown script if the Pod is failing.
- I. Establish two jobs: one to assess container-database connectivity, and another to execute the shutdown script if the Pod is encountering connectivity issues.
- III. Set up the Deployment with a PostStart lifecycle handler to verify service availability. Configure a PreStop lifecycle handler to execute the shutdown script if the container fails.
- II. Construct the Deployment with a livenessProbe for the container, which will fail if database connectivity is not established. Configure a Prestop lifecycle handler to execute the shutdown script if the container fails.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Construct the Deployment with a livenessProbe for the container, which will fail if database connectivity is not established. Configure a Prestop lifecycle handler to execute the shutdown script if the container fails.

The most suitable answer in this case is

**II. Construct the Deployment with a livenessProbe for the container, which will fail if database connectivity is not established. Configure a Prestop lifecycle handler to execute the shutdown script if the container fails.**

Here's why:

  * **LivenessProbe:** A livenessProbe is specifically designed to monitor the health of a container. If it cannot connect to the database, Kubernetes will recognize the container as unhealthy and automatically restart it, potentially re-establishing the connection.

  * **PreStop Lifecycle Handler:** This hook is triggered before the container is terminated. It's the perfect place to execute your graceful shutdown script, ensuring any in-process tasks are completed cleanly.

Here's why the other options aren't as ideal:

  * **I. Separate Jobs:** This approach adds complexity and might introduce delays. Jobs might not run with the frequency needed to detect connectivity issues promptly.

  * **III. PostStart Handler:** PostStart is executed once after container startup. It wouldn't provide continuous monitoring, and a PreStop hook doesn't automatically trigger if a liveness probe fails.

  * **IV. InitContainer:** An initContainer runs to completion before the main container starts. It might not accurately reflect ongoing connectivity issues after startup and delays the main application container.

References:

<https://cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on->

</details>

---

### Exam 1 · Q23

**While developing a JPEG image-resizing API on Google Kubernetes Engine (GKE), the service's callers will reside within the same GKE cluster. You aim to facilitate clients in obtaining the service's IP address. What's the recommended approach?**

- IV. Configure a GKE Endpoint. Clients should obtain the endpoint name from Cloud DNS.
- III. Configure a GKE Endpoint. Clients should retrieve the endpoint name from the appropriate environment variable within the client container.
- I. Establish a GKE Service. Clients should use the A record's name in Cloud DNS to locate the service's cluster IP address.
- II. Set up a GKE Service. Clients should utilize the service name within the URL to access the service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Set up a GKE Service. Clients should utilize the service name within the URL to access the service.

**II. Set up a GKE Service. Clients should utilize the service name within the URL to access the service.**

**Explanation:**

Using a GKE Service with its service name is the most efficient and reliable way to enable service discovery within a Kubernetes cluster:

  * **Internal DNS:** Kubernetes automatically assigns a DNS name to each Service, providing a simple abstraction for clients. The service name becomes the hostname (e.g., `my-image-resizer.default.svc.cluster.local`)

  * **Load Balancing:** Kubernetes Services handle load balancing across the pods that actually run your API.

  * **Simplicity for Clients:** Clients don't need to maintain specific IP addresses, which can change as pods are rescheduled or scaled.

**Why Other Options Are Less Ideal:**

  * **I. Establish a GKE Service ... Cloud DNS to locate ... cluster IP address** While technically possible, manually managing Cloud DNS and cluster IPs adds complexity and potential points of failure.

  * **III & IV. Configure a GKE Endpoint ... Clients should retrieve the endpoint name ...** GKE Endpoints are primarily for exposing services outside the cluster. Since you're working within the cluster, they add unnecessary layers.

**References:**

[https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/  https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery)

[https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/  https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery)

</details>

---

### Exam 1 · Q26

**The latest iteration of your containerized application has undergone rigorous testing and stands poised for deployment to production on Google Kubernetes Engine. Due to limitations, thorough load testing couldn't be conducted in pre-production environments. Ensuring a seamless deployment free from performance glitches is paramount, with automation being a prerequisite. What actions should you take?**

- IV. Execute the deployment using kubectl and configure the spec.updateStrategy.type to RollingUpdate. Utilize Cloud Monitoring to flag any performance issues and initiate a rollback using the kubectl command if necessary.
- I. Employ Cloud Load Balancing to gradually increase traffic between versions, while relying on Cloud Monitoring to detect any performance anomalies.
- II. Implement a continuous delivery pipeline featuring canary deployments, utilizing Cloud Monitoring to pinpoint performance issues and incrementally scaling up traffic based on observed metrics.
- III. Opt for a continuous delivery pipeline with blue/green deployments, leveraging Cloud Monitoring to identify performance bottlenecks and proceeding with full deployment once metrics confirm readiness.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Implement a continuous delivery pipeline featuring canary deployments, utilizing Cloud Monitoring to pinpoint performance issues and incrementally scaling up traffic based on observed metrics.

**II. Implement a continuous delivery pipeline featuring canary deployments, utilizing Cloud Monitoring to pinpoint performance issues and incrementally scaling up traffic based on observed metrics.**

**Explanation:**

  * **Risk Mitigation:** Canary deployments are ideal for this scenario, letting you test the new version with a small subset of real production traffic. This limits potential impact if issues arise.

  * **Gradual Rollout:** With incremental traffic increases, you have greater control while gathering live performance data.

  * **Monitoring-Driven:** Cloud Monitoring plays a key role in observing key metrics (latency, error rates, etc.). This data will inform your decision on whether to continue the rollout or roll back.

  * **Automation:** A continuous delivery pipeline automates the entire process, ensuring consistency and speed.

**Why Other Options Aren't as Suitable**

  * **I. Cloud Load Balancing with Monitoring:** While this can help distribute traffic, it lacks the fine-grained control and automated rollback mechanisms offered by a proper canary deployment strategy.

  * **III. Blue/Green Deployments:** Blue/green is well-suited for rapid rollbacks, but it requires double the resources and can be overkill if the changes aren't drastic.

  * **IV. Manual Rollout with Kubectl:** This option lacks the safeguards and automation of a dedicated continuous delivery pipeline. It's error-prone and less scalable.

**Reference:**

<https://cloud.google.com/deploy/docs/deployment-strategies/canary#types_of_canary>

</details>

---

### Exam 1 · Q27

**Given the urgent need to implement autoscaling for your stateless and distributed service operating in a Google Kubernetes Engine (GKE) cluster without significant alterations, which approach should you pursue?**

- III. Opting for a Horizontal Pod Autoscaler would enable scaling the number of Pods based on CPU load, offering a straightforward solution that aligns with the stateless and distributed nature of the service, with minimal changes required.
- II. Deploying a Vertical Pod Autoscaler to scale based on a custom metric could entail substantial changes and additional configurations, potentially complicating the deployment within the constrained two-week timeframe.
- I. Deploying a Vertical Pod Autoscaler would dynamically adjust the resource requests and limits for individual Pods based on their actual usage, but it doesn't directly cater to autoscaling according to workload demands.
- IV. Implementing a Horizontal Pod Autoscaler to scale based on a custom metric might necessitate more intricate configurations and adjustments, potentially impeding the deployment within the two-week timeframe.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Opting for a Horizontal Pod Autoscaler would enable scaling the number of Pods based on CPU load, offering a straightforward solution that aligns with the stateless and distributed nature of the service, with minimal changes required.

Given the urgent need to implement autoscaling for your stateless and distributed service operating in a Google Kubernetes Engine (GKE) cluster without significant alterations, the most appropriate approach to pursue is:

**III. Opting for a Horizontal Pod Autoscaler would enable scaling the number of Pods based on CPU load, offering a straightforward solution that aligns with the stateless and distributed nature of the service, with minimal changes required.**

Explanation:

  * Option III suggests deploying a Horizontal Pod Autoscaler, which is designed specifically for scaling the number of Pods based on CPU load. This aligns well with the stateless and distributed nature of the service, as it can automatically adjust the number of Pods to handle varying workload demands without significant changes to the deployment.

  * Option I discusses deploying a Vertical Pod Autoscaler, which adjusts resource requests and limits for individual Pods based on their usage but doesn't directly address autoscaling according to workload demands. This approach might not be suitable for rapidly changing workloads.

  * Option II mentions deploying a Vertical Pod Autoscaler to scale based on a custom metric. While this could be possible, it may entail substantial changes and additional configurations, potentially complicating the deployment within the constrained timeframe.

  * Option IV discusses implementing a Horizontal Pod Autoscaler to scale based on a custom metric, which might necessitate more intricate configurations and adjustments, potentially impeding the deployment within the two-week timeframe.

Therefore, Option III provides the most straightforward and suitable solution for implementing autoscaling for the stateless and distributed service in a GKE cluster within the urgent timeframe.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling  https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler  https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling)

[https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling  https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler  https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling)

[https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling  https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler  https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling)

</details>

---

### Exam 1 · Q32

**You manage a microservices application on Google Kubernetes Engine (GKE) using Istio. You secure the communication channels between your microservices by implementing an Istio AuthorizationPolicy, a Kubernetes NetworkPolicy, and mTLS on your GKE cluster. You discover that HTTP requests between two Pods to specific URLs fail, while other requests to other URLs succeed. What is the likely cause of the connection issue?**

- III. The Authorization Policy within your cluster might be blocking HTTP requests for specific paths within your application.
- II. It's possible that the Pod initiating the HTTP requests is trying to connect to the target Pod via an incorrect TCP port.
- IV. The cluster might have mTLS configured in permissive mode, but the Pod's sidecar proxy could be transmitting unencrypted traffic in plain text, causing the failure.
- I. The Kubernetes NetworkPolicy resource is likely blocking HTTP traffic between the Pods for specific URLs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. The Authorization Policy within your cluster might be blocking HTTP requests for specific paths within your application.

**III. The Authorization Policy within your cluster might be blocking HTTP requests for specific paths within your application.**

**Explanation:**

  1. **Istio AuthorizationPolicy: Istio AuthorizationPolicy allows you to define fine-grained access control policies for services within your mesh. If certain HTTP requests between Pods are failing for specific URLs, it's possible that an AuthorizationPolicy is blocking access to those URLs. This could be due to misconfiguration or intentional access restrictions.**

Options I, II, and IV are less likely to be the cause of the connection issue:

I. While Kubernetes NetworkPolicy could potentially block HTTP traffic between Pods for specific URLs, it's less likely to be the cause of the issue if other HTTP requests to different URLs are succeeding. NetworkPolicy usually works at the network level and is not concerned with specific URLs.

II. If the Pod initiating the HTTP requests is trying to connect to the target Pod via an incorrect TCP port, it would likely result in a connection error or timeout rather than only affecting specific URLs.

IV. If mTLS is configured in permissive mode, it allows both encrypted and unencrypted traffic. However, this scenario is less likely to cause the failure of specific HTTP requests to certain URLs unless there's a specific rule or configuration related to those URLs causing the issue.

**References:**

[https://istio.io/latest/docs/tasks/security/authorization/authz-http/](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port  https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging)

[https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port  https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging)

[https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging ](https://istio.io/latest/docs/tasks/security/authorization/authz-http/  https://istio.io/latest/docs/ops/common-problems/network-issues/#sending-https-to-an-http-port  https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#authorization_policy_denial_logging)

</details>

---

### Exam 1 · Q34

**Your website resides on Compute Engine. The marketing team wishes to assess conversion rates across three different website designs. What method should you adopt?**

- IV. Deploy the website on Cloud Functions, dividing it into three distinct functions.
- I. Host the website on App Engine and implement traffic splitting.
- II. Deploy the website on App Engine, dividing it into three separate services.
- III. Utilize Cloud Functions to host the website, employing traffic splitting.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Host the website on App Engine and implement traffic splitting.

**I. Host the website on App Engine and implement traffic splitting.**

**Explanation:**

App Engine is the most suitable choice for this scenario for several reasons:

  * **Traffic Splitting:** App Engine has built-in support for traffic splitting, allowing you to distribute traffic among different versions of your website (each with a different design) based on percentages you define.

  * **Scalability:** App Engine handles scaling automatically, ensuring your website can manage traffic surges during the experiment.

  * **Ease of Use:** App Engine provides a managed environment simplifying deployment and configuration.

**Why Other Options Are Less Suited:**

  * **II. Deploy the website on App Engine, dividing it into three separate services.** While technically possible, this adds unnecessary complexity to your setup and could potentially introduce inconsistencies across the separate services.

  * **III. Utilize Cloud Functions to host the website, employing traffic splitting.** Cloud Functions are better suited for individual, task-based functions rather than hosting entire websites. They lack the built-in traffic routing of App Engine.

  * **IV. Deploy the website on Cloud Functions, dividing it into three distinct functions.** Similar to option III, this approach fractures your website logic and introduces potential overhead in communication between the functions.

**References:**  
<https://cloud.google.com/appengine/docs/standard/python/splitting-traffic>

</details>

---

### Exam 1 · Q37

**Your application is live in production, but certain issues only manifest once the new version starts receiving traffic from users. To mitigate both the impact and the number of users affected, which deployment strategy should you employ?**

- III. Rolling deployment
- IV. Recreate deployment
- I. Blue/green deployment
- II. Canary deployment

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Canary deployment

**II. Canary deployment**

Here's why:

  * **Traffic Control:** Canary deployments allow you to route a small percentage of real user traffic to the new version, while the majority still gets routed to the stable version.

  * **Minimized Impact:** Any issues arising in the new version affect only a limited subset of users, reducing the overall impact on your application.

  * **Live Testing:** You can carefully monitor the new version under real-world conditions, detecting errors or performance issues before they affect your entire userbase.

  * **Gradual Rollout:** If the new version performs well, you can gradually increase the percentage of traffic routed to it, eventually replacing the old version.

**Why Other Options Are Less Ideal:**

  * **Blue/green deployment:** While offering a safe rollback option, blue/green involves switching entirely between versions. This lacks the gradual exposure offered by canary deployments when issues are subtle.

  * **Rolling deployment:** This sequentially updates instances, which can still affect a significant portion of users if an issue arises.

  * **Recreate deployment:** This has downtime involved and lacks the controlled testing that a canary deployment allows.

Ref:

[https://cloud.google.com/architecture/application-deployment-and-testing-strategies#canary_test_pattern](https://cloud.google.com/architecture/application-deployment-and-testing-strategies#canary_test_pattern  https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_a_bluegreen_deployment)

[https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_a_bluegreen_deployment](https://cloud.google.com/architecture/application-deployment-and-testing-strategies#canary_test_pattern  https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_a_bluegreen_deployment)

</details>

---

### Exam 1 · Q39

**Your company's product team has introduced a new requirement, prompted by customer demand, to implement autoscaling for your stateless and distributed service operating within a Google Kubernetes Engine (GKE) cluster. Given the tight timeline of two weeks before this feature needs to be live, what would be the most suitable approach?**

- IV. Implement a Horizontal Pod Autoscaler, with scaling determined by a custom metric.
- II. Implement a Vertical Pod Autoscaler, with scaling determined by a custom metric.
- III. Implement a Horizontal Pod Autoscaler, with scaling determined by the CPU load.
- I. Implement a Vertical Pod Autoscaler, with scaling determined by the CPU load.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Implement a Horizontal Pod Autoscaler, with scaling determined by the CPU load.

**III. Implement a Horizontal Pod Autoscaler, with scaling determined by CPU load.**

**Explanation:**

Here's a breakdown of why this is the best choice, and why the other options are less ideal:

  * **Horizontal vs. Vertical Scaling:** Horizontal scaling (adding/removing replicas of your pods) is inherently better suited for distributed, stateless services than vertical scaling (changing resource allocation of existing pods). This is because horizontal scaling allows you to distribute load and handle more requests in parallel, a key goal of autoscaling.

  * **CPU Load vs. Custom Metrics:** While custom metrics can be valuable, using CPU load as the scaling metric has a significant advantage in this scenario - **speed of implementation**. You can set up a CPU-based Horizontal Pod Autoscaler (HPA) within minutes. Custom metrics usually require defining the metric, ensuring monitoring is in place, and potentially additional code changes.

**Why Other Options Aren't as Suitable**

  * **I. Vertical Pod Autoscaler (CPU Load):** While vertical scaling can handle increased load, it has limits. There comes a point where a single pod can't handle any more load, and horizontal scaling becomes necessary.

  * **II. Vertical Pod Autoscaler (Custom Metric):** VPA with custom metrics could be a good long-term solution, but the two-week deadline makes implementation difficult.

  * **IV. Horizontal Pod Autoscaler (Custom Metric):** This combines the potential complexity of custom metrics with horizontal scaling. While powerful, it's likely too complex for the timeframe.

Reference:

<https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautosc>aler

</details>

---

### Exam 1 · Q41

**To ensure the security of a secret in your application deployed on a Google Kubernetes Engine (GKE) cluster, preventing its exposure via calls to the Kubernetes API server, what is the recommended approach?**

- IV. Place the secret in Secret Manager, then establish a Google service account authorized to access the secret from Secret Manager. Generate a Kubernetes service account for the container, and employ Workload Identity to authenticate as the Google service account, ensuring protected access to the secret without vulnerability to Kubernetes API calls.
- II. Deploy GKE Application-layer Secrets Encryption on the cluster using a Cloud Key Management Service (KMS) key, guaranteeing that secrets are encrypted at the application layer, thereby averting exposure through API calls to the Kubernetes server.
- III. Safeguard the secret in Cloud KMS, then configure a Google service account with authorization to access the secret from Cloud KMS. Export the service account key in JSON format, and attach the JSON file to the container as a ConfigMap volume, enabling secure retrieval of the secret from Cloud KMS.
- I. Create a Kubernetes Secret and transmit the secret as an environment variable to the container, which could potentially risk exposing it through logs or other channels, thus jeopardizing its security.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Place the secret in Secret Manager, then establish a Google service account authorized to access the secret from Secret Manager. Generate a Kubernetes service account for the container, and employ Workload Identity to authenticate as the Google service account, ensuring protected access to the secret without vulnerability to Kubernetes API calls.

The recommended approach to ensure the security of a secret in your application deployed on a Google Kubernetes Engine (GKE) cluster, preventing its exposure via calls to the Kubernetes API server, is:

**IV. Place the secret in Secret Manager, then establish a Google service account authorized to access the secret from Secret Manager. Generate a Kubernetes service account for the container, and employ Workload Identity to authenticate as the Google service account, ensuring protected access to the secret without vulnerability to Kubernetes API calls.**

Explanation:

  * Option IV suggests using Google Cloud's Secret Manager to store the secret, which is designed specifically for securely storing and managing secrets. By establishing a Google service account with appropriate permissions to access the secret from Secret Manager, and then using Workload Identity to authenticate as the Google service account, the application can securely retrieve the secret without directly exposing it to the Kubernetes API server.

  * Option I suggests transmitting the secret as an environment variable to the container, which can risk exposure through logs or other channels, making it less secure.

  * Option II mentions deploying GKE Application-layer Secrets Encryption, which can help encrypt secrets at the application layer, but it doesn't specifically address preventing exposure via calls to the Kubernetes API server.

  * Option III involves safeguarding the secret in Cloud KMS and configuring a service account to access it, but exporting the service account key as a JSON file and attaching it to the container as a ConfigMap volume might introduce additional security risks compared to using Secret Manager and Workload Identity.

Therefore, Option IV provides the most robust and secure approach for protecting secrets in a GKE environment.

**References:**

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

[https://cloud.google.com/kms/docs](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

[https://kubernetes.io/docs/concepts/configuration/secret/](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

[https://cloud.google.com/secret-manager/docs/overview](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity  https://cloud.google.com/kms/docs  https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/secret-manager/docs/overview)

</details>

---

### Exam 1 · Q42

**You've constructed multiple Cloud Functions in Java, accompanied by integration and service tests. Utilizing Cloud Build, you deploy these functions and initiate tests. However, your Cloud Build job flags deployment failures right after validating the code. What steps should you take to address this issue?**

- I. Review the maximum number of Cloud Function instances.
- IV. Confirm that the Cloud Build service account holds the Cloud Functions Developer role.
- III. Attempt the tests again, employing the truncated exponential backoff polling strategy.
- II. Ensure that your Cloud Build trigger is configured with accurate build parameters.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Confirm that the Cloud Build service account holds the Cloud Functions Developer role.

**Correct Option:**

**IV. Confirm that the Cloud Build service account holds the Cloud Functions Developer role.**

**Justification:**

  * **Importance of Service Account Permissions:** Cloud Functions deployment involves resource creation and modification, permissions for which are held by service accounts. The Cloud Functions Developer role is specifically designed to provide the essential set of permissions for Cloud Functions management and deployment. If the Cloud Build service account lacks this role, it won't have adequate authorization, thus impeding the deployment process even if the code itself is valid.

**Why Other Options Are Unsuitable:**

  * **I. Review the maximum number of Cloud Function instances:** While important for scalability and cost management, this wouldn't prevent a deployment failure right after code validation.

  * **II. Ensure that your Cloud Build trigger is configured with accurate build parameters:** Incorrect build parameters might lead to issues in the build process, but the question implies the failure occurs during deployment specifically, pointing towards a permissions problem.

  * **III. Attempt the tests again, employing the truncated exponential backoff polling strategy.:** This approach addresses transient errors but wouldn't resolve a fundamental lack of permissions in the service account.

**References:**

[https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page https://cloud.google.com/build/docs/troubleshooting#build_trigger_fails_due_to_missing_cloudbuildbuildscreate_permission](https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page   https://cloud.google.com/build/docs/troubleshooting#build_trigger_fails_due_to_missing_cloudbuildbuildscreate_permission  https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account)

[https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account](https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page   https://cloud.google.com/build/docs/troubleshooting#build_trigger_fails_due_to_missing_cloudbuildbuildscreate_permission  https://cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account)

</details>

---

### Exam 1 · Q43

**How should you implement a solution on Google Kubernetes Engine to configure each microservice with a specific number of replicas and ensure uniform addressing within the cluster?**

- D. Deploying microservices as Pods without leveraging Deployments can hinder scalability and management. Expose the Pods within the cluster using an Ingress, and depend on the Ingress IP address for addressing, potentially leading to inconsistent access as the number of replicas scales.
- C. Directly deploying each microservice as a Pod limits scalability and management capabilities. Expose the Pods within the cluster through a Service, and utilize the Service DNS name for addressing, ensuring uniform access from other microservices within the cluster.
- A. Deploy each microservice as a Deployment, which facilitates easy scaling and replica management. Expose the Deployment within the cluster via a Service, and utilize the Service DNS name for addressing the microservices from other microservices, ensuring consistent access regardless of the number of replicas.
- B. Use Deployments for each microservice to manage replicas efficiently. Expose the Deployments within the cluster using an Ingress, and use the Ingress IP address to address the microservices from other microservices within the cluster, maintaining a consistent addressing mechanism despite replica scaling.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy each microservice as a Deployment, which facilitates easy scaling and replica management. Expose the Deployment within the cluster via a Service, and utilize the Service DNS name for addressing the microservices from other microservices, ensuring consistent access regardless of the number of replicas.

The correct option is:

**A. Deploy each microservice as a Deployment, which facilitates easy scaling and replica management. Expose the Deployment within the cluster via a Service, and utilize the Service DNS name for addressing the microservices from other microservices, ensuring consistent access regardless of the number of replicas.**

Explanation:

  * Option A suggests using Deployments for each microservice, which allows easy scaling and management of replicas. Services should be used to expose the Deployments within the cluster. This ensures that the microservices can be addressed consistently using the Service DNS name regardless of the number of replicas. This approach provides uniform addressing within the cluster.

  * Option B suggests using Ingress to expose the Deployments within the cluster, but Ingress is typically used for routing external traffic to services within the cluster, not for internal communication between microservices.

  * Option C recommends directly deploying each microservice as a Pod, which limits scalability and management capabilities compared to using Deployments. While it suggests exposing the Pods within the cluster through a Service, it doesn't mention utilizing Service DNS for addressing, which could lead to inconsistent access.

  * Option D also suggests deploying microservices as Pods without leveraging Deployments, which hinders scalability and management. Additionally, using Ingress for addressing internal services is not a recommended practice and can lead to inconsistent access, especially as the number of replicas scales.

Therefore, Option A is the most suitable approach for configuring each microservice with a specific number of replicas and ensuring uniform addressing within the cluster.

References:

<https://cloud.google.com/kubernetes-engine/docs/concepts/service>

</details>

---

### Exam 1 · Q46

**After deploying your application on Google Kubernetes Engine, you now seek the capability to swiftly revert to the prior version if complications arise with the new release. Which deployment model is most suitable for your scenario?**

- III. Opt for a blue/green deployment strategy and test the new application after the deployment process is finalized.
- II. Implement A/B testing and periodically test the application after integrating the new features.
- I. Execute a rolling deployment and conduct testing of the new application post-deployment completion.
- IV. Employ a canary deployment approach and periodically test the new application after deploying the updated version.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Opt for a blue/green deployment strategy and test the new application after the deployment process is finalized.

**III. Opt for a blue/green deployment strategy and test the new application after the deployment process is finalized.**

**Justification:**

  * **Swift Rollback:** Blue/green deployments offer a core advantage – the ability to quickly switch back to the previous version (blue) if the new version (green) exhibits issues. This aligns directly with your need for rapid reversions.

  * **Complete Pre-Release Testing:** Before switching traffic to the new version, the blue/green strategy allows for comprehensive testing of the new application in a production-like environment. This minimizes the risk of surprises.

  * **Clear Separation:** This model maintains two separate environments (blue and green), reducing the risk of interference between old and new versions during testing.

**Why Other Options are Less Ideal:**

  * **I. Execute a rolling deployment and conduct testing of the new application post-deployment completion.** While rolling updates are effective for gradual rollout, if issues are found after the deployment is complete, rollback can be more complex and disruptive.

  * **II. Implement A/B testing and periodically test the application after integrating the new features.** A/B testing focuses primarily on comparing versions for user experience or conversion purposes. It doesn't inherently provide the quick, full rollback mechanism of blue/green.

  * **IV. Employ a canary deployment approach and periodically test the new application after deploying the updated version.** Canary deployments help with gradual rollout and testing but introduce an additional layer of complexity if you need a swift, complete rollback.

**Reference:**

<https://cloud.google.com/architecture/application-deployment-and-testing-strategies#choosing_the_right_strategy>

</details>

---

### Exam 1 · Q52

**In your role as a developer collaborating with the CI/CD team, you're tasked with troubleshooting a new feature recently introduced by your team. Utilizing HashiCorp Packer, the CI/CD team created a new Compute Engine image from your development branch. Despite a successful build, the image fails to boot up. What's the appropriate step to investigate the issue with the CI/CD team?**

- I. Initiate a new feature branch and request the build team to recompile the image.
- III. Install Packer on your local environment, build the Compute Engine image locally, and then test it within your personal Google Cloud project.
- IV. Analyze the Compute Engine OS logs via the serial port and verify access to the serial port by examining the Cloud Logging logs.
- II. Halt the deployed virtual machine, export the disk, and subsequently mount the disk locally to access the boot logs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Analyze the Compute Engine OS logs via the serial port and verify access to the serial port by examining the Cloud Logging logs.

**IV. Analyze the Compute Engine OS logs via the serial port and verify access to the serial port by examining the Cloud Logging logs.**

Here's why this is the best approach:

  * **Direct Problem Diagnosis:** The serial port provides access to boot logs generated by the operating system installed on the image. These logs frequently reveal the root cause of boot failures.

  * **Cloud Logging Integration:** Cloud Logging captures serial port output, making it easy to access and analyze the logs even if the VM doesn't fully boot.

  * **Troubleshooting Focus:** This approach focuses on identifying the source of the issue, allowing for a targeted fix.

**Why Other Options Are Less Ideal:**

  * **I. New Feature Branch:** This might be necessary later but is premature without identifying the root cause of the issue.

  * **II. Mounting the Disk:** While potentially useful, this is more complex than accessing serial port logs and might not reveal the issue if it's related to early boot processes.

  * **III. Replicating Locally:** This could be helpful but may not fully reproduce the CI/CD team's environment and can be time-consuming.

**References:**  
[https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console  https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting)

[https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console  https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting)

</details>

---

### Exam 1 · Q53

**You're managing an analytics application that executes numerous queries on BigQuery via the BigQuery API at regular intervals. How can you determine the execution time of these queries?**

- IV. Utilize Stackdriver Monitoring to monitor query execution times.
- I. Utilize Stackdriver Monitoring to visualize slot usage.
- III. Utilize Stackdriver Trace to monitor query execution time.
- II. Employ Stackdriver Trace to track API execution time.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Stackdriver Monitoring to monitor query execution times.

**IV. Utilize Stackdriver Monitoring to monitor query execution times.**

Here's why:

  * **Query-Centric Metrics:** Stackdriver Monitoring (now called Cloud Monitoring) provides metrics specifically tailored to BigQuery, including query execution time. Using it allows you to track and visualize this information as time-series data.

  * **Alerts and Analysis:** You can set alerts based on query execution time thresholds and analyze trends over time to identify performance bottlenecks.

  * **BigQuery Integration:** These metrics are collected directly from BigQuery by Stackdriver Monitoring.

**Why Other Options Are Not Ideal**

  * **I. Utilize Stackdriver Monitoring to visualize slot usage.** Slot usage shows your BigQuery query resource utilization, which can _indirectly_ relate to performance, but isn't a direct measure of execution time.

  * **II & III. Utilize Stackdriver Trace...** Stackdriver Trace is primarily used for distributed tracing and performance profiling within applications. While you might instrument your application code to include parts that interact with BigQuery, it's unnecessary overhead for simply measuring query execution time.

**Reference** :

<https://cloud.google.com/bigquery/docs/monitoring>

</details>

---

### Exam 1 · Q56

**Your application deployed on Compute Engine is encountering persistent failures with a limited number of requests. Upon investigation, you've identified the problem to a particular Compute Engine instance. However, SSH access to the instance is unresponsive. What should be your next course of action?**

- IV. Capture a disk snapshot and link it to a new instance.
- I. Restart the machine.
- II. Activate and inspect the serial port output.
- III. Terminate the instance and create a replacement.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Activate and inspect the serial port output.

The best course of action in this scenario would be to:

**II. Activate and inspect the serial port output.**

Here's why:

  * **Unresponsive SSH:** This indicates a potential issue at the operating system level or deeper. Inspecting the serial port output can provide valuable insights into the underlying problem, such as kernel panics, boot failures, or other critical errors that might not be visible through other means.

  * **Limited Impact:** The problem is isolated to a single instance, so actions like restarting the machine or terminating it might disrupt the service unnecessarily.

  * **Diagnosis First:** Before taking any drastic action, it's crucial to understand the root cause of the failure. The serial port output can help diagnose the problem accurately, allowing you to take targeted corrective measures.

**Other options and why they might not be the best first step:**

  * **I. Restart the machine:** This might temporarily resolve the issue if it's a minor glitch, but it won't help diagnose the underlying problem, and the issue could recur.

  * **III. Terminate the instance and create a replacement:** This is a more drastic step that should be considered only after exhausting other troubleshooting options. It might lead to data loss if not handled carefully.

  * **IV. Capture a disk snapshot and link it to a new instance:** This is a good practice for preserving data, but it doesn't address the root cause of the failure. The new instance might encounter the same problem if the underlying issue is not resolved.

**In summary, activating and inspecting the serial port output is the most logical first step to diagnose the problem on the unresponsive Compute Engine instance.**

</details>

---

### Exam 2 · Q1

**You're strategizing the deployment of your application on Google Kubernetes Engine (GKE). Your application demands horizontal scalability, with each instance necessitating both a stable network identity and its persistent disk. Which GKE component aligns best with this requirement?**

- I. Deployment
- III. ReplicaSet
- IV. ReplicaController
- II. StatefulSet

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. StatefulSet

**II. StatefulSet**

Explanation:

  * **Stable Network Identities:** Each pod in a StatefulSet is assigned a unique and persistent hostname/DNS entry, allowing reliable communication within and outside the cluster.

  * **Persistent Disks:** StatefulSets are designed to work with persistent storage. Pods can be associated with individual PersistentVolumeClaims, ensuring data persists even if pods are rescheduled.

  * **Ordered Scaling:** StatefulSets scale pods in a sequential order (0, 1, 2...), which can be important for certain applications that rely on pod identity during initialization or coordination.

Why Other Options Are Less Ideal:

  * **I. Deployment:** Deployments manage stateless pods designed for horizontal scaling. They don't guarantee stable network identities or have built-in mechanisms for persistent storage association.

  * **III. ReplicaSet:** Similar to Deployments, ReplicaSets primarily manage stateless replicas and don't directly handle persistent storage or stable identifiers.

  * **IV. ReplicaController:** ReplicaControllers are an older version of ReplicaSets with less functionality and shouldn't be used in new deployments.

Ref:

<https://cloud.google.com/kubernetes-engine/docs/concepts/statefulset>

</details>

---

### Exam 2 · Q4

**You've containerized a legacy application that relies on configuration stored on an NFS share. How can you ensure the application doesn't serve traffic until its configuration is retrieved when deploying it to Google Kubernetes Engine (GKE)?**

- IV. Introduce a startup script to the GKE instance group to mount the NFS share during node startup, transferring the configuration files into the container, and activate the service via an ENTRYPOINT script.
- II. Establish a PersistentVolumeClaim (PVC) on the GKE cluster, accessing configuration files from the volume, and commence the service via an ENTRYPOINT script.
- I. Utilize the gsutil utility within the Docker container at startup, copying files, and initiate the service via an ENTRYPOINT script.
- III. Incorporate the COPY statement in the Dockerfile to inject the configuration into the container image, validating its availability, and launch the service using an ENTRYPOINT script.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Establish a PersistentVolumeClaim (PVC) on the GKE cluster, accessing configuration files from the volume, and commence the service via an ENTRYPOINT script.

**II. Establish a PersistentVolumeClaim (PVC) on the GKE cluster, accessing configuration files from the volume, and commence the service via an ENTRYPOINT script.**

Here's why this stands out as the ideal choice:

  * **Kubernetes Native:** Using PersistentVolumeClaims (PVCs) integrates seamlessly with Kubernetes, providing a standard way to manage persistent storage for Pods.

  * **Configuration Decoupling:** Separating the configuration from the container image enhances flexibility and maintainability, avoiding re-building images for configuration changes.

  * **Availability Check:** Your ENTRYPOINT script can include logic to verify the configuration is accessible from the mounted volume before starting the application, ensuring it doesn't serve traffic prematurely.

**Why Other Options Are Less Ideal:**

  * **I. gsutil within the container:** While possible, it adds complexity and potential security risks due to embedding credentials within the container.

  * **III. Embedding config in the image:** This makes image management less flexible, requiring rebuilds for configuration changes.

  * **IV. Instance Group Startup Script:** This approach tightly couples configuration management to the underlying infrastructure, making it less portable and harder to manage within Kubernetes.

**References** :

[https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes  https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

[https://cloud.google.com/filestore/docs/accessing-fileshares](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes  https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

[https://cloud.google.com/storage/docs/gcs-fuse](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes  https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

</details>

---

### Exam 2 · Q5

**Upon installing the Stackdriver Logging Agent to transmit an application's log file to Stackdriver from a Compute Engine virtual machine instance, what is the initial step you should take?**

- IV. Establish a Stackdriver Logs Export Sink with a filter aligning with the application's log entries.
- III. Define the application log file as a custom source.
- II. Provide the instance with complete access to all Cloud APIs.
- I. Activate the Error Reporting API for the project.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Define the application log file as a custom source.

**The initial step you should take upon installing the Stackdriver Logging Agent to transmit an application's log file to Stackdriver from a Compute Engine virtual machine instance is:**

**III. Define the application log file as a custom source.**

**Explanation:**

I. Activating the Error Reporting API for the project:

  * While activating the Error Reporting API may be necessary for capturing and reporting errors, it is not the initial step for configuring log forwarding with the Stackdriver Logging Agent.

II. Providing the instance with complete access to all Cloud APIs:

  * Providing the instance with complete access to all Cloud APIs is not necessary for configuring log forwarding with the Stackdriver Logging Agent. It is a security best practice to provide only the necessary permissions to instances.

**III. Defining the application log file as a custom source:**

  * **This is the initial step in configuring log forwarding with the Stackdriver Logging Agent. By defining the application log file as a custom source, you specify which log files should be collected and forwarded to Stackdriver Logging.**

IV. Establishing a Stackdriver Logs Export Sink with a filter aligning with the application's log entries:

  * Establishing a Stackdriver Logs Export Sink with a filter aligning with the application's log entries is a subsequent step after defining the custom log source. It involves configuring the destination for the logs and specifying any filters to ensure only relevant log entries are exported.

**Therefore, the initial step you should take is to define the application log file as a custom source (Option III).**

Ref:  
<https://cloud.google.com/logging/docs/agent/configuration>

</details>

---

### Exam 2 · Q7

**Your application comprises a series of loosely interconnected services managed by code executed on Compute Engine. To facilitate the seamless deployment of new Compute Engine instances accessing a specific service version, how should you configure the setup?**

- IV. Configure your service to utilize a fixed hostname and port for connecting to the desired service, and update the service at the endpoint with the new version.
- I. Specify your service endpoint details as metadata fetched at runtime, enabling connection to the desired service.
- II. Specify your service endpoint details as label data fetched at runtime, facilitating connection to the desired service.
- III. Define your service endpoint details to be fetched from an environment variable at runtime, facilitating connection to the desired service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Specify your service endpoint details as metadata fetched at runtime, enabling connection to the desired service.

**I. Specify your service endpoint details as metadata fetched at runtime, enabling connection to the desired service.**

**Explanation:**

  * **Dynamic Configuration:** Metadata is a key strength in Compute Engine. It allows you to provide instance-specific information that code running on the instance can access. This is ideal for discovering the correct endpoint to connect to.

  * **Deployment Flexibility:** With metadata, you don't need to modify code or environment variables with each service version change. Updating the metadata is enough for your new instances to point to the correct location.

**Why Other Options Aren't as Suitable**

  * **II. Labels:** Labels are primarily for organizing resources, not dynamically providing runtime configuration details.

  * **III. Environment Variables:** Environment variables can work but they introduce another element to manage during your deployment process. Metadata is more streamlined in this case.

  * **IV. Fixed Hostname/Port:** This approach is inflexible, especially if you use load balancing or service discovery, where endpoints may change dynamically.

**References:**  
[https://cloud.google.com/apis/design/glossary#api_service_endpoint https://cloud.google.com/compute/docs/metadata/overview](https://cloud.google.com/apis/design/glossary#api_service_endpoint   https://cloud.google.com/compute/docs/metadata/overview  https://cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest#service-endpoint)

[https://cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest#service-endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint   https://cloud.google.com/compute/docs/metadata/overview  https://cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest#service-endpoint)

</details>

---

### Exam 2 · Q8

**You're utilizing Cloud Build to create a new Docker image for each source code commit to a Cloud Source Repositories repository. Commits to the master branch trigger builds for your application. How can you automate the release process for specific commits to the master branch?**

- III. Configure a build trigger based on a Git branch name pattern, adhering to a Git branch naming convention for releases.
- I. Trigger the build manually for new releases.
- II. Set up a build trigger based on a Git tag pattern, following a Git tag convention for releases.
- IV. Store your source code in a secondary Cloud Source Repositories repository with a distinct Cloud Build trigger solely for new releases.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Set up a build trigger based on a Git tag pattern, following a Git tag convention for releases.

**II. Set up a build trigger based on a Git tag pattern, following a Git tag convention for releases.**

Explanation:

  * **Versioning:** Git tags provide a clear and structured way to mark specific commits as releasable versions (e.g., v1.0.0, v1.1.2).

  * **Automation:** A Cloud Build trigger tied to your tag pattern (e.g., `v*.**`) automatically initiates builds when you create a release tag.

  * **Consistency:** A well-defined tagging convention streamlines the release process and maintains historical tracking of releases.

Why Other Options Are Less Ideal:

  * **I. Trigger the build manually...** This lacks automation and introduces potential for errors due to manual intervention.

  * **III. Configure a build trigger based on a Git branch name pattern ...** Branch naming conventions might change or be less reliable than an explicit tagging strategy.

  * **IV. Store your source code in a secondary Cloud Source Repositories repository ...** This adds unnecessary complexity, fragmenting your codebase and its history.

**Reference:**

<https://cloud.google.com/source-repositories/docs/integrating-with-cloud-build#create_a_build_trigger>

</details>

---

### Exam 2 · Q10

**Which approach should you take to install a third-party logging solution on each node in your Google Kubernetes Engine (GKE) cluster to troubleshoot intermittent performance issues?**

- IV. Utilize Terraform to deploy the third-party solution and deploy the logging Pod as a Kubernetes Deployment
- III. Manually install the software on GKE nodes via SSH
- I. Implement the third-party solution as a DaemonSet
- II. Embed the monitoring software into your container image

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement the third-party solution as a DaemonSet

**Correct option- I. Implement the third-party solution as a DaemonSet**

**I. Implement the third-party solution as a DaemonSet**

  * **Correct Option:** DaemonSets offer the most suitable approach for this scenario.

  * **Justification:** DaemonSets ensure that a pod (in this case, the logging agent) runs on each node within the Kubernetes cluster. This guarantees consistent logging across all nodes, crucial for investigating intermittent performance problems that could occur anywhere within the cluster.

**II. Embed the monitoring software into your container image**

  * **Incorrect Option:** While possible, it's not ideal for this use case.

  * **Justification:**

    * **Tight Coupling:** Embedding the logging agent directly in your application containers creates unnecessary dependencies and complicates future updates to either the application or the logging solution.

    * **Node-Level Issues:** This method only logs issues within your application container, missing potential problems at the node or infrastructure level that might be causing the performance problems.

**III. Manually install the software on GKE nodes via SSH**

  * **Incorrect Option:** This approach should be avoided.

  * **Justification:**

    * **Scalability:** Manual installation is time-consuming and prone to human error, especially in large clusters.

    * **Maintenance:** Updating the logging agent across nodes becomes tedious and harder to track.

    * **Kubernetes Philosophy:** It goes against the declarative nature of Kubernetes, where infrastructure state should be managed through configuration, not manual intervention.

**IV. Utilize Terraform to deploy the third-party solution and deploy the logging Pod as a Kubernetes Deployment**

  * **Potentially Correct, but less ideal than DaemonSets:** Terraform can automate the deployment, but...

  * **Justification:**

    * **Node-Level Granularity:** Regular Deployments don't guarantee a pod on each node. You might get multiple logging pods on the same node or miss some nodes entirely, leading to inconsistent logging coverage.

</details>

---

### Exam 2 · Q13

**Your data resides in Cloud Storage buckets. Colleagues have reported that retrieving data from Cloud Storage is causing sluggish performance in API responses. To investigate the issue thoroughly and provide pertinent details to the GCP support team, which command should you execute?**

- III. `**gcloud compute scp example-instance:~/test-data -o output.json gs://my-bucket**`
- IV. `**gcloud services test -o output.json gs://my-bucket**`
- I. `**gsutil test -o output.json gs://my-bucket**`
- II. `**gsutil perfdiag -o output.json gs://my-bucket**`

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. `**gsutil perfdiag -o output.json gs://my-bucket**`

**II. gsutil perfdiag -o output.json gs://my-bucket**

Explanation:

  * **gsutil perfdiag:** This command specifically diagnoses Cloud Storage performance issues, capturing detailed metrics and trace information.

  * **output.json:** The output is stored in a structured JSON file for easy analysis and inclusion in your communication with GCP support.

  * **Targeted Diagnostics:** `perfdiag` measures factors like network latency, object sizes, throughput, and error rates – all directly influencing data retrieval speed.

Why Other Options Are Less Ideal:

  * **I. gsutil test ...** This performs basic connectivity tests but doesn't provide the in-depth performance profiling relevant to your scenario.

  * **III. gcloud compute scp ...** This command is for copying files between a Compute Engine instance and Cloud Storage. It might be useful in some performance investigations, but not for the initial diagnosis.

  * **IV. gcloud services test ...** This tests the health status of Google Cloud services in general, not the granular performance of Cloud Storage.

**Reference:**  
<https://cloud.google.com/storage/docs/gsutil/commands/perfdiag#providing-diagnostic-output-to-cloud-storage-team>

</details>

---

### Exam 2 · Q15

**In setting up a build pipeline for an application intended to operate in Google Kubernetes Engine (GKE), your team prioritizes security to permit only images generated by the pipeline to be deployed to the GKE cluster. Which combination of Google Cloud services should be employed?**

- I. Cloud Build, Cloud Storage, and Binary Authorization
- III. Google Cloud Deploy, Artifact Registry, and Google Cloud Armor
- II. Google Cloud Deploy, Cloud Storage, and Google Cloud Armor
- IV. Cloud Build, Artifact Registry, and Binary Authorization

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Cloud Build, Artifact Registry, and Binary Authorization

**Correct Answer:**

  * **IV. Cloud Build, Artifact Registry, and Binary Authorization**

**Justification:**

  * **Image Pipeline:** Cloud Build is ideal for creating the container images in a secure and controlled build process.

  * **Trusted Repository:** Artifact Registry serves as a secure, managed image repository, providing fine-grained access controls.

  * **Deployment Authorization:** Binary Authorization acts as a gatekeeper, ensuring that only images that have passed specific checks (build provenance, vulnerability scans, etc.) are allowed for deployment to GKE.

**Why Other Options Are Less Ideal:**

  * **I. Cloud Build, Cloud Storage, and Binary Authorization**

    * **Artifact Registry Advantage:** While Cloud Storage can store images, Artifact Registry offers features tailored for container management, such as versioning and vulnerability scanning integration.

  * **II. Google Cloud Deploy, Cloud Storage, and Google Cloud Armor**

    * **Focus Mismatch:** Google Cloud Deploy is for managing application deployments, not enforcing image security policy. Google Cloud Armor is a web application firewall (WAF), not directly related to secure build pipelines.

  * **III. Google Cloud Deploy, Artifact Registry, and Google Cloud Armor**

    * **Missing Authorization:** While Artifact Registry provides a secure repository, it needs Binary Authorization to enforce the "only approved images" policy.

**References:**

[https://cloud.google.com/binary-authorization/docs/cloud-build](https://cloud.google.com/binary-authorization/docs/cloud-build  https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke#objectives)

[https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke#objectives](https://cloud.google.com/binary-authorization/docs/cloud-build  https://cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke#objectives)

</details>

---

### Exam 2 · Q18

**To deploy a new European version of a website on Google Kubernetes Engine, ensuring both the current and new websites can be accessed via the same HTTP(S) load balancer's external IP address but with different domain names, what action should you take?**

- I. Define a new Ingress resource with a host rule matching the new domain.
- III. Create a new Service of type LoadBalancer specifying the existing IP address as the loadBalancerIP.
- IV. Generate a new Ingress resource and specify the existing IP address as the kubernetes.io/ingress.global-static-ip-name annotation value.c
- II. Modify the existing Ingress resource with a host rule matching the new domain.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Modify the existing Ingress resource with a host rule matching the new domain.

**II. Modify the existing Ingress resource with a host rule matching the new domain.**

Here's why:

  * **Ingress for Routing:** Ingress is the preferred way to expose Kubernetes services outside the cluster, and it's designed for routing traffic based on domain names.

  * **Shared Load Balancer:** Since you want to reuse the existing HTTP(S) load balancer, modifying the existing Ingress is the most straightforward approach.

  * **Host-based Routing:** Ingress resources use host rules to determine which backend service to route traffic to based on the incoming domain name. By adding a new host rule for the European domain, you can direct traffic to the appropriate service within your GKE cluster.

**Why other options are not as suitable:**

  * **I. New Ingress Resource:** While technically possible, creating a separate Ingress would likely result in the provisioning of a new external IP address, which isn't the goal.

  * **III. New LoadBalancer Service:** Creating a new LoadBalancer service would also provision a new IP address. Moreover, using raw Kubernetes services for this type of routing is less manageable than using an Ingress.

  * **IV. Static IP Annotation:** This annotation is used to associate a specific static IP address with an Ingress resource. While relevant for preserving an IP, it's not the primary mechanism for adding a new domain route.

**References:**

[https://kubernetes.io/docs/concepts/services-networking/ingress/#name-based-virtual-hosting https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip](https://kubernetes.io/docs/concepts/services-networking/ingress/#name-based-virtual-hosting   https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip)

</details>

---

### Exam 2 · Q21

**You're preparing to deploy a new Go application to Cloud Run, with its source code stored in Cloud Source Repositories. You aim to establish a fully managed, automated, continuous deployment pipeline triggered by each source code commit. Seeking the simplest deployment solution,**

**what should you do?**

- II. Configure a Jenkins trigger to initiate the container build and deployment process for each source code commit made to Cloud Source Repositories.
- III. Enable continuous deployment of new revisions from the source repository to Cloud Run using buildpacks.
- I. Set up a cron job on your workstations to periodically execute 'gcloud run deploy --source' within the working directory.
- IV. Utilize Cloud Build with a trigger configured to execute the container build and deploy process for each source code commit to Cloud Source Repositories.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Cloud Build with a trigger configured to execute the container build and deploy process for each source code commit to Cloud Source Repositories.

**Correct Option:**

**IV. Utilize Cloud Build with a trigger configured to execute the container build and deploy process for each source code commit to Cloud Source Repositories.**

**Explanation:**

  * **Fully Managed:** Cloud Build is a serverless CI/CD platform within Google Cloud, eliminating the need to manage your own build infrastructure.

  * **Easy Integration:** Cloud Build integrates seamlessly with Cloud Source Repositories, allowing you to set up triggers that automatically initiate builds on commits.

  * **Cloud Run Deployment:** Cloud Build can directly build and deploy container images to Cloud Run, simplifying the entire pipeline.

  * **Simplicity:** This approach offers a streamlined workflow with minimal setup on your side.

**Why other options are less ideal:**

  * **I. Cron Job:** This solution is manual, not automated, and requires you to manage the cron schedule and deployment script.

  * **II. Jenkins:** While powerful, Jenkins introduces the overhead of maintaining your own Jenkins server and its configuration.

  * **III. Buildpacks:** Buildpacks can be a great option, but they might require additional configuration if you have specific build requirements beyond what buildpacks provide.

**Reference:**  
<https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build>

</details>

---

### Exam 2 · Q27

**You are designing a deployment strategy for your new applications on Google Cloud. As part of your deployment planning, you aim to leverage live traffic to collect performance metrics for both new and existing applications. You need to test against the full production load before launch. What should you do?**

- II. Implement blue/green deployment.
- IV. Employ A/B testing with traffic mirroring during deployment.
- I. Opt for canary deployment.
- III. Choose rolling updates deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Employ A/B testing with traffic mirroring during deployment.

**IV. Employ A/B testing with traffic mirroring during deployment.**

Let's break down why this is the most effective choice:

  * **Live Production Traffic:** Traffic mirroring allows you to test new code with real production traffic without impacting user experience. This gives you the most realistic performance assessment.

  * **Full Load Testing:** Mirroring the entire production load ensures you're testing against the true scale of your traffic.

  * **A/B Comparison:** Comparing the performance of your new application code against the existing version under identical load provides valuable insights for optimization.

  * **Controlled Rollout:** Based on the results of your A/B tests, you can gradually and safely increase traffic to the new version.

**Why Other Options are Less Ideal:**

  * **I. Canary Deployment:** While it offers gradual rollout and risk mitigation, its focus is not on pre-launch load testing. You'd get only partial traffic exposure.

  * **II. Blue/Green Deployment:** This is for rapid cutovers, not gradual testing with full production load. You'd also need to maintain duplicate production environments.

  * **III. Rolling Updates:** This focuses on gradual rollout, but doesn't inherently provide side-by-side comparisons or full production load testing.

**Reference:**

<https://cloud.google.com/architecture/application-deployment-and-testing-strategies#shadow_test_pattern>

</details>

---

### Exam 2 · Q32

**How should you design a study to determine whether a new color scheme for a global ecommerce web application hosted on Cloud Run will increase sales, utilizing live production traffic?**

- III. Utilize an external HTTP(S) load balancer to mirror traffic to the new version of the application with the updated color scheme. Analyze the results to determine whether there is a statistically significant difference in sales.
- II. Utilize an external HTTP(S) load balancer to direct traffic to the original color scheme while creating and testing the new deployment. Upon completion of testing, switch all traffic to the new color scheme. Analyze the results to evaluate any statistically significant difference in sales.
- I. Utilize an external HTTP(S) load balancer to split a predetermined percentage of traffic between two different color schemes of the application. Analyze the results to assess any statistically significant difference in sales.
- IV. Implement a feature flag to display the new color scheme to half of all users. Monitor sales for this group to assess whether there is an increase.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Utilize an external HTTP(S) load balancer to split a predetermined percentage of traffic between two different color schemes of the application. Analyze the results to assess any statistically significant difference in sales.

**I. Option I: Utilize an external HTTP(S) load balancer to split a predetermined percentage of traffic between two different color schemes of the application. Analyze the results to assess any statistically significant difference in sales.**

  * **Feedback: This option effectively implements A/B testing, allowing for a controlled comparison between the original and new color schemes. By splitting traffic, it enables the assessment of any impact on sales without disrupting the user experience for all users.**

  * **Justification for selection: A/B testing is a widely used method for evaluating changes in web applications, as it provides clear insights into the effectiveness of variations. By directing a portion of the traffic to the new color scheme, it allows for a direct comparison with the original scheme, facilitating analysis of any differences in sales.**

II. Utilize an external HTTP(S) load balancer to direct traffic to the original color scheme while creating and testing the new deployment. Upon completion of testing, switch all traffic to the new color scheme. Analyze the results to evaluate any statistically significant difference in sales.

  * Feedback: This option involves a phased rollout approach, which may not provide immediate insights into the impact on sales. While it minimizes risk by initially testing the new color scheme on a subset of traffic, it delays the assessment of its effectiveness until after full deployment.

  * Justification for not selecting: This approach might not be suitable for immediate evaluation of the new color scheme's impact on sales, as it delays the comparison between the original and new schemes until after full deployment. It's generally preferable to conduct A/B testing to directly compare performance variations.

III. Utilize an external HTTP(S) load balancer to mirror traffic to the new version of the application with the updated color scheme. Analyze the results to determine whether there is a statistically significant difference in sales.

  * Feedback: While mirroring traffic allows for observation of user behavior without affecting their experience, it doesn't directly compare the performance of the two versions. This approach might not provide clear insights into the impact of the new color scheme on sales.

  * Justification for not selecting: Without a direct comparison between the original and new color schemes, it may be challenging to determine whether any observed differences in sales are attributable to the color scheme change or other factors.

IV. Implement a feature flag to display the new color scheme to half of all users. Monitor sales for this group to assess whether there is an increase.

  * Feedback: Implementing a feature flag allows for random assignment of users to different groups, enabling evaluation of the new color scheme's impact on sales. However, this approach doesn't split traffic evenly and may not provide a clear comparison between the two versions.

  * Justification for not selecting: While feature flags can be useful for experimentation, they may not provide as controlled an environment for comparison as A/B testing. Randomly assigning users to different groups might not result in an even distribution of traffic between the original and new color schemes, potentially biasing the results.

**In summary, while all options present different approaches for evaluating the impact of the new color scheme on sales, Option I (utilizing A/B testing with an external HTTP(S) load balancer) provides the most direct and controlled comparison between the original and new schemes, making it the preferred choice for determining the effectiveness of the color scheme change.**

**References:**

[https://cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_actions_weight-based_traffic_splitting](https://cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_actions_weight-based_traffic_splitting  https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)

[https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless](https://cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic_actions_weight-based_traffic_splitting  https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)

</details>

---

### Exam 2 · Q35

**You need to transfer the directory "local-scripts" and all its contents from your local workstation to a Compute Engine virtual machine instance. Which command should you use?**

- IV. `**gcloud compute mv --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`
- III. `**gcloud compute scp --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`
- II. `**gsutil cp --project my-gcp-project -R ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`
- I. `**gsutil cp --project my-gcp-project -r ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. `**gcloud compute scp --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**`

**III. gcloud compute scp --project my-gcp-project --recurse ~/local-scripts/ gcp-instance-name:~/server-scripts/ --zone us-east1-b**

**Explanation:**

  * **gcloud compute scp:** This is the appropriate tool for secure file transfers between local machines and Compute Engine instances.

  * **\--project my-gcp-project:** Specifies your Google Cloud Project for authentication.

  * **\--recurse:** This flag is essential since you want to copy the entire directory, including its contents.

  * **~/local-scripts/** : The source path on your local machine.

  * **gcp-instance-name:~/server-scripts/** : The destination path on the Compute Engine instance (make sure to replace 'gcp-instance-name' with your actual instance's name).

  * **\--zone us-east1-b:** Specifies the zone of your Compute Engine instance.

**Why Other Options Are Incorrect:**

  * **I & II. gsutil cp...** The `gsutil` command is primarily for interacting with Google Cloud Storage buckets, not direct file transfers to Compute Engine instances. While there are ways to make it work, it's less straightforward than using `gcloud compute scp`.

  * **IV. gcloud compute mv ...** The `mv` command is for moving or renaming files, not copying them across machines.

</details>

---

### Exam 2 · Q39

**You've transitioned an on-premises monolithic application to a microservices setup on Google Kubernetes Engine (GKE), with backend dependencies such as a CRM system and a MySQL database containing PII residing on-premises for regulatory compliance. Despite establishing a Cloud VPN connection between your on-premises data center and Google Cloud, you're encountering latency-related crashes due to fluctuating bandwidth. How should you tackle these latency issues?**

- I. Implement Memorystore to cache frequently accessed PII data from the on-premises MySQL database
- III. Scale up the number of Cloud VPN tunnels for the connection between Google Cloud and the on-premises services
- IV. Reduce network layer packet size by adjusting the Maximum Transmission Unit (MTU) value from its default setting on Cloud VPN
- II. Utilize Istio to establish a service mesh encompassing the microservices on GKE and the on-premises services

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Scale up the number of Cloud VPN tunnels for the connection between Google Cloud and the on-premises services

**III. Scale up the number of Cloud VPN tunnels for the connection between Google Cloud and the on-premises services.**

**Explanation:**

  1. **Scaling Cloud VPN Tunnels: Increasing the number of Cloud VPN tunnels can help distribute the network traffic between your on-premises data center and Google Cloud, thus potentially mitigating the impact of fluctuating bandwidth and reducing latency-related crashes. This approach can provide additional bandwidth and redundancy, improving the stability and reliability of the connection.**

Options I, II, and IV are less likely to directly address the latency issues caused by fluctuating bandwidth:

I. Implementing Memorystore to cache frequently accessed PII data from the on-premises MySQL database might improve performance by reducing the need to access the database frequently, but it may not directly address the latency issues caused by fluctuating bandwidth between the on-premises data center and Google Cloud.

II. Utilizing Istio to establish a service mesh can help manage and secure communication between microservices, but it may not directly alleviate the latency issues arising from the fluctuating bandwidth between on-premises services and microservices on GKE.

IV. Adjusting the Maximum Transmission Unit (MTU) value on Cloud VPN could potentially optimize network performance, but it may not be as effective in addressing latency issues caused by fluctuating bandwidth compared to scaling up the number of VPN tunnels. Additionally, adjusting MTU values requires careful consideration and testing to avoid introducing compatibility or performance issues.

**Hint:**

[https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#more-bandwidth](https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#more-bandwidth  https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment)

[https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment](https://cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#more-bandwidth  https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#route-alignment)

</details>

---

### Exam 2 · Q43

**As you deploy your applications on Compute Engine, you face a failure to launch one of your Compute Engine instances. What steps should you take? (Select two.)**

- III. Investigate firewall rules or routes on the instance.
- V. Review whether network traffic to or from your instance is being dropped.
- IV. Check if your instance's boot disk is completely full.
- II. Try accessing Compute Engine using an alternative SSH user.
- I. Evaluate whether your file system is corrupted.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Check if your instance's boot disk is completely full. **|** I. Evaluate whether your file system is corrupted.

* **IV. Check if your instance's boot disk is completely full.** A full boot disk can prevent the operating system from loading, hindering the startup process.

  * **I. Evaluate whether your file system is corrupted.** File system corruption on the boot disk can also cause startup issues.

Here's why the other options are less important initially:

  * **II. Try accessing Compute Engine using an alternative SSH user.** This assumes the instance has at least booted, allowing for SSH access. It's helpful for later-stage troubleshooting, not when the instance won't launch at all.

  * **III. Investigate firewall rules or routes on the instance.** Similar to the previous point, this assumes the instance has some level of functionality, whereas firewall issues are unlikely to prevent initial startup entirely.

  * **V. Review whether network traffic to or from your instance is being dropped.** Network connectivity issues, while possible, are less likely to be the sole cause of a complete launch failure.

**References:**

<https://cloud.google.com/compute/docs/troubleshooting/vm-startup#identify_the_reason_why_the_boot_disk_isnt_booting>

</details>

---

### Exam 2 · Q44

**As a developer at a large organization deploying a web application to Google Kubernetes Engine (GKE), you're tasked with configuring a CI/CD pipeline using Cloud Deploy. The pipeline should deploy the application to Dev, Test, and Prod clusters in GKE. Following Google-recommended best practices, how should you configure the process to automatically promote the application from the Dev to the Test cluster after a successful deployment?**

- IV. Establish a Cloud Build pipeline utilizing the gke-deploy builder. Create a Cloud Build trigger to monitor SUCCEEDED Pub/Sub messages from the cloud-builds topic. Configure this pipeline to execute a deployment step to the Test cluster.
- II. Develop a Cloud Function to call the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the cloud-builds topic.
- III. Create a Cloud Function to invoke the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic.
- I. Set up a Cloud Build trigger to monitor SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic. Configure Cloud Build to include a step for promoting the application to the Test cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Create a Cloud Function to invoke the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic.

**Correct Answer:**

  * **III. Create a Cloud Function to invoke the Google Cloud Deploy API for promoting the application to the Test cluster. Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the clouddeploy-operations topic.**

**Justification:**

  * **Automation & Integration:** Cloud Deploy emits events to a Pub/Sub topic (`clouddeploy-operations`) when deployment operations succeed or fail. A Cloud Function directly subscribing to this topic provides a clean, event-driven promotion mechanism.

  * **API Directness:** Utilizing the Google Cloud Deploy API within the Cloud Function ensures you're directly controlling the promotion step and adhering to Google's prescribed practices.

  * **Flexibility:** Cloud Functions provide flexibility if you need additional logic or customization around the promotion process.

**Why Other Options Are Less Ideal:**

  * **I. Set up a Cloud Build trigger to monitor SUCCEEDED Pub/Sub messages...**

    * **Scope:** While Cloud Build is excellent for CI/CD pipelines, it's not the primary tool for managing promotions within Cloud Deploy. Using a Cloud Function aligns better with Cloud Deploy's native mechanisms.

  * **II. ... Configure this function to be triggered by SUCCEEDED Pub/Sub messages from the cloud-builds topic.**

    * **Topic Mismatch:** The `cloud-builds` topic is related to build events, not Cloud Deploy's deployment lifecycle events.

  * **IV. Establish a Cloud Build pipeline utilizing the gke-deploy builder ...**

    * **Separation of Concerns:** While Cloud Build is suitable for the initial deployment steps, it's cleaner to use Cloud Deploy's native eventing and API for managing promotions between environments.

**References:**  
[https://cloud.google.com/functions/docs/calling/pubsub https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing](https://cloud.google.com/functions/docs/calling/pubsub   https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing  https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2  https://cloud.google.com/deploy/docs/integrating#before_you_begin)

[https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2](https://cloud.google.com/functions/docs/calling/pubsub   https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing  https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2  https://cloud.google.com/deploy/docs/integrating#before_you_begin)

[https://cloud.google.com/deploy/docs/integrating#before_you_begin](https://cloud.google.com/functions/docs/calling/pubsub   https://cloud.google.com/deploy/docs/integrating#integrating_with_automated_testing  https://cloud.google.com/build/docs/automate-builds-pubsub-events#console_2  https://cloud.google.com/deploy/docs/integrating#before_you_begin)

</details>

---

### Exam 2 · Q45

**As the manager responsible for your company's ecommerce platform payment system on Google Cloud, you're mandated to retain user logs for specific durations. Logs must be kept for 1 year for internal audits and for 3 years to meet compliance standards. To reduce on-premises storage usage and ensure efficient searchability, what's the optimal method for storing new user logs on Google Cloud with minimal effort while ensuring correct storage?**

- I. Store logs in a Cloud Storage bucket with bucket locking enabled.
- II. Store logs in a Cloud Storage bucket with a 3-year retention period.
- III. Employ Cloud Logging to store logs as customized logs with a tailored retention duration.
- IV. Initially store logs in a Cloud Storage bucket with a 1-year retention period. After 1 year, transfer logs to another bucket with a 2-year retention period.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Employ Cloud Logging to store logs as customized logs with a tailored retention duration.

**The optimal method for storing new user logs on Google Cloud with minimal effort while ensuring correct storage is option III:**

**III. Employ Cloud Logging to store logs as customized logs with a tailored retention duration.**

**Explanation:**

  1. **Cloud Logging (formerly Stackdriver Logging)** : Cloud Logging is a fully managed service by Google Cloud Platform for collecting, viewing, and analyzing logs from applications and services. It offers customizable retention periods, making it an ideal solution for meeting specific compliance requirements.

  2. **Customized retention duration** : With Cloud Logging, you can set retention periods tailored to your specific needs. In this scenario, you can set a retention period of 1 year for internal audits and 3 years to meet compliance standards.

Options I, II, and IV do not fully address the requirements and may introduce unnecessary complexity:

I. Storing logs in a Cloud Storage bucket with bucket locking enabled can prevent deletion of objects but doesn't address the need for different retention periods for internal audits and compliance standards.

II. Storing logs in a Cloud Storage bucket with a fixed 3-year retention period doesn't meet the requirement of retaining logs for 1 year for internal audits.

IV. Initially storing logs in a Cloud Storage bucket with a 1-year retention period and then transferring logs to another bucket with a 2-year retention period after 1 year adds unnecessary complexity and management overhead. Using Cloud Logging with customized retention durations is a more straightforward solution.

**References:**  
[https://cloud.google.com/logging/docs/buckets#custom-retention](https://cloud.google.com/logging/docs/buckets#custom-retention  https://cloud.google.com/logging/docs/central-log-storage)

[https://cloud.google.com/logging/docs/central-log-storage](https://cloud.google.com/logging/docs/buckets#custom-retention  https://cloud.google.com/logging/docs/central-log-storage)

</details>

---

### Exam 2 · Q47

**In developing an application comprising various internal microservices on Google Kubernetes Engine (GKE), you seek the ability to configure each microservice with a distinct number of replicas. Additionally, you aim for a uniform approach to address any microservice from another, irrespective of the microservice's scaling. How should you implement this solution?**

- III. Deploy each microservice as a Pod, exposing it within the cluster via a Service. Employ the Service DNS name for microservice-to-microservice interaction.
- I. Deploy each microservice as a Deployment, exposing it within the cluster via a Service. Utilize the Service DNS name for inter-microservice communication.
- IV. Deploy each microservice as a Pod, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.
- II. Deploy each microservice as a Deployment, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Deploy each microservice as a Deployment, exposing it within the cluster via a Service. Utilize the Service DNS name for inter-microservice communication.

**I. Deploy each microservice as a Deployment, exposing it within the cluster via a Service. Utilize the Service DNS name for inter-microservice communication.**

Here's why this approach excels:

  * **Scaling Flexibility:** Deployments allow you to easily control the number of replicas for each microservice, providing granular scaling to match workload demands.

  * **Reliability:** Services provide stable, internal DNS names that remain consistent even if the underlying Pods are rescheduled or replaced.

  * **Abstraction:** Using Service DNS names abstracts away the details of individual Pods, making it simpler to reason about inter-microservice communication within the cluster.

  * **Kubernetes-Native:** This approach aligns with standard Kubernetes practices for deploying and exposing microservices.

**Why Other Options Are Less Ideal:**

  * **II. Deploy each microservice as a Deployment, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.**

    * Ingresses are primarily designed for external traffic entering the cluster. While technically possible, it's less efficient for internal service-to-service communication.

  * **III. Deploy each microservice as a Pod, exposing it within the cluster via a Service. Employ the Service DNS name for microservice-to-microservice interaction.**

    * Pods are ephemeral; they can be created and destroyed frequently. Deployments provide a higher-level abstraction and management capabilities that are better suited for microservices.

  * **IV. Deploy each microservice as a Pod, exposing it within the cluster via an Ingress. Utilize the Ingress IP address for communication between microservices.**

    * This combines the drawbacks of both Pods and using Ingress for internal communication, making it the least desirable option.

</details>

---

### Exam 2 · Q50

**After mistakenly typing a configuration error in a low-level Linux file, preventing your Compute Engine instance from booting normally, what corrective action should you take?**

- IV. Rectify the mistake by configuring and logging into the Compute Engine instance using a remote desktop client.
- I. Download the file via scp, modify it locally, and then upload the corrected version to the Compute Engine instance.
- III. Correct the error by configuring and accessing the Compute Engine instance through the serial port connection.
- II. Access and modify the file directly by configuring and logging into the Compute Engine instance via SSH.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Correct the error by configuring and accessing the Compute Engine instance through the serial port connection.

Here's the most effective way to resolve this issue:

**III. Correct the error by configuring and accessing the Compute Engine instance through the serial port connection.**

Here's why this is the best approach:

  * **System Can't Fully Boot:** The configuration error prevents your instance from booting normally, making traditional remote access options like SSH unavailable.

  * **Serial Port Access:** The serial port provides access even when regular boot processes fail. This lets you directly interact with the early boot stages and file system.

  * **Corrects the Root Cause:** You can diagnose and fix the configuration error in the file, addressing the issue preventing a successful boot.

**Why other options are less ideal:**

  * **I. Downloading and Uploading:** This assumes that you can still access the file system somehow, which might not be the case if the system can't boot completely.

  * **II. SSH Access:** SSH requires that the instance is booted with a functional network stack – a scenario the configuration error likely prevents.

  * **IV. Remote Desktop:** Remote desktop relies on the instance being fully booted and running a graphical interface, which is unlikely with this error.

**References:**

<https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console>

</details>

---

### Exam 2 · Q53

**You have a variety of packaged and internally developed applications hosted on a Linux Compute Engine instance. These applications log data as text in local files. You want these logs to be stored in Cloud Logging. What's the recommended approach?**

- III. Implement a Google-provided version of collectd on the Compute Engine instance.
- IV. Set up a cron job to transfer the log files to Cloud Storage once a day.
- II. Deploy a Google-provided version of fluentd on the Compute Engine instance.
- I. Configure the files' content to be directed to the Linux Syslog daemon.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Deploy a Google-provided version of fluentd on the Compute Engine instance.

**II. Deploy a Google-provided version of Fluentd on the Compute Engine instance.**

Here's why this is the best option:

  * **Log Collection & Parsing:** Fluentd is a powerful open-source log collector designed specifically for this purpose. It can parse various log formats, structure data, and send it to Cloud Logging efficiently.

  * **Google Integration:** Google provides a pre-configured Fluentd agent tailored for integration with Cloud Logging. This simplifies setup and ensures compatibility.

  * **Flexibility:** Fluentd can handle not only standard text log files but also diverse log sources, providing you with room for expansion.

**Why Other Options Are Less Ideal:**

  * **I. Linux Syslog:** While Syslog could be a step, it doesn't directly forward logs to Cloud Logging. You'd need an additional tool to bridge this gap.

  * **III. Collectd:** Collectd is primarily focused on system and performance metrics, not general-purpose log collection.

  * **IV. Cron job to Cloud Storage:** This approach lacks real-time insights, adds complexity by requiring further processing for Cloud Logging, and isn't ideal for large volumes of logs.

Ref:

<https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent>

</details>

---

### Exam 2 · Q57

**You are tasked with deploying an internet-facing microservices application to Google Kubernetes Engine (GKE) and implementing A/B testing for new features. Your deployment must adhere to the following requirements:**

  * **Zero downtime during the deployment of new container images.**

  * **Testing and verification of new production releases using a subset of production users.**

**Which approach should you take?**

- III. Install Anthos Service Mesh on the GKE cluster. Create two Deployments labeled with different version names. Implement an Istio routing rule to direct a small percentage of traffic to the Deployment with the new application version.
- IV. Implement a rolling update pattern by gradually replacing Pods with the new release version. Validate application performance for the subset of users during the rollout and rollback if necessary.
- II. Create a second namespace on GKE for the new release version. Set up a Deployment configuration in the new namespace with the required number of Pods. Deploy new container versions in this namespace and update the Ingress configuration to direct traffic to it.
- I. Configure your CI/CD pipeline to update the Deployment manifest file with the latest container version. Recreate Pods in the cluster by applying the updated Deployment manifest file. Validate application performance by comparing functionality with the previous release and rollback if necessary.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Install Anthos Service Mesh on the GKE cluster. Create two Deployments labeled with different version names. Implement an Istio routing rule to direct a small percentage of traffic to the Deployment with the new application version.

**Correct Option:**

**III. Install Anthos Service Mesh on the GKE cluster. Create two Deployments labeled with different version names. Implement an Istio routing rule to direct a small percentage of traffic to the Deployment with the new application version.**

**Explanation:**

  * **Zero downtime:** Service meshes like Istio facilitate traffic management without disrupting running Pods. This ensures no downtime during deployments.

  * **A/B Testing:** Istio's routing capabilities allow fine-grained control over traffic splitting, ideal for directing a small percentage of users to the new version for testing.

  * **Canary Releases:** This approach aligns with the concept of canary releases where you gradually expose new versions to increasing subsets of users.

**Why other options are less ideal:**

  * **I. Replacing Pods:** This will incur downtime as existing pods are terminated before new ones are launched. Not suitable for zero downtime requirements.

  * **II. Separate Namespaces:** While possible, managing traffic redirection through namespaces is less sophisticated than using a service mesh. It can add operational complexity.

  * **IV. Rolling Update:** Standard rolling updates achieve zero downtime, but lack the granular traffic control needed for true A/B testing on a subset of production users.

**References:**  
<https://cloud.google.com/architecture/implementing-deployment-and-testing-strategies-on-gke#perform_an_ab_test>

</details>

---

### Exam 2 · Q59

**You encountered a situation where your application abruptly terminated during a Deployment update in Google Kubernetes Engine due to not closing the database connection properly. Now, you aim to enhance your application to ensure it undergoes a graceful shutdown. What is the recommended action to take?**

- I. Revise your code to handle a received SIGTERM signal appropriately to gracefully disconnect from the database.
- III. Extend the terminationGracePeriodSeconds for your application.
- II. Implement a PodDisruptionBudget to safeguard the Pod from being forcibly terminated.
- IV. Set up a PreStop hook to manage the shutdown process of your application.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Revise your code to handle a received SIGTERM signal appropriately to gracefully disconnect from the database.

**Correct Option:**

**I. Update your code to process a received SIGTERM signal to gracefully disconnect from the database.**

**Explanation:**

  * This directly targets the root cause of the forceful shutdown. Kubernetes sends a SIGTERM signal before terminating a Pod. Your code needs to intercept this signal and initiate a graceful shutdown, including closing database connections.

**Why other options are less suitable:**

  * **II. Configure a PodDisruptionBudget:** While helpful for minimizing disruptions, this won't prevent shutdowns during node failures or manual deletions. It doesn't address the lack of graceful database connection handling.

  * **III. Increase the terminationGracePeriodSeconds:** This gives your application more time to shut down but doesn't ensure it will actually use that time to properly close connections if the SIGTERM signal isn't handled.

  * **IV. Configure a PreStop hook:** This can be useful for additional shutdown logic but is ineffective if your code still doesn't handle SIGTERM and close the database connection within the hook.

**References:**

[https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks  https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-graceful-shutdown-for-your-application)

[https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-graceful-shutdown-for-your-application](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks  https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-graceful-shutdown-for-your-application)

</details>

---

### Exam 3 · Q3

**Before deploying your new application code to production, you aim to conduct testing across various user profiles. Despite the inherent risks, you intend to assess the new version with production users, controlling access based on their operating systems. If issues arise, you seek a swift rollback process. What's the recommended approach?**

- III. Opt for App Engine deployment, employing traffic splitting to direct specific user segments to the new version based on IP addresses.
- IV. Consider Compute Engine deployment, leveraging Traffic Director to guide specific user segments to the new version based on predefined weights.
- II. Choose Google Kubernetes Engine with Anthos Service Mesh deployment, employing traffic splitting to route certain user segments to the new version based on the user-agent header.
- I. Opt for Cloud Run deployment, utilizing traffic splitting to direct specific user segments to the new version based on the revision tag.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Choose Google Kubernetes Engine with Anthos Service Mesh deployment, employing traffic splitting to route certain user segments to the new version based on the user-agent header.

**Correct Answer:**

  * **II. Choose Google Kubernetes Engine with Anthos Service Mesh deployment, employing traffic splitting to route certain user segments to the new version based on the user-agent header.**

**Justification:**

  * **Accurate User Targeting:** The user-agent header within HTTP requests reliably conveys the operating system of the user's device. Anthos Service Mesh (and other service meshes) can finely control traffic routing using these headers.

  * **Rollbacks and Granular Control:** Service meshes excel at swift rollbacks and granular adjustments to traffic distribution percentages. These attributes are well-suited for mitigating potential risks.

  * **Kubernetes as a Foundation:** GKE provides the ideal platform for managing service mesh deployments like Anthos.

**Why Other Options Are Less Optimal:**

  * **I. Opt for Cloud Run deployment, utilizing traffic splitting to direct specific user segments to the new version based on the revision tag.**

    * **Limitation:** While Cloud Run's traffic splitting is robust, it usually targets revisions rather than user-agent headers. This makes OS-based segmentation difficult.

  * **III. Opt for App Engine deployment, employing traffic splitting to direct specific user segments to the new version based on IP addresses.**

    * **Imprecise Targeting:** Relying on IP addresses for identifying operating systems is unreliable, as users on different OSes can share IP ranges.

  * **IV. Consider Compute Engine deployment, leveraging Traffic Director to guide specific user segments to the new version based on predefined weights**

    * **Added Complexity:** Though Traffic Director offers fine-grained control, it increases setup and management complexity compared to the Anthos Service Mesh solution built for this use case.

**References:**

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent>

</details>

---

### Exam 3 · Q4

**As you develop an HTTP API on a Compute Engine virtual machine instance, it's crucial for multiple clients within the same Virtual Private Cloud (VPC) to access it. How can clients retrieve the service's IP address?**

- I. Reserve a static external IP address and assign it to an HTTP(S) load balancing service's forwarding rule. Clients should use this IP address for connection.
- IV. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[API_NAME]/[API_VERSION]/.
- III. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal/.
- II. Reserve a static external IP address and assign it to an HTTP(S) load balancing service's forwarding rule. Then, set up an A record in Cloud DNS. Clients should use the A record's name to connect.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal/.

**III. Ensure clients leverage Compute Engine internal DNS by accessing the instance name through the URL https://[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal/.**

Here's why this is the most efficient and reliable approach for clients within the same VPC:

  * **Internal communication:** Compute Engine's internal DNS allows for direct communication between instances within a VPC, bypassing the need for external IP addresses.

  * **Simplicity:** This approach doesn't involve reserving external IP addresses, setting up load balancers, or managing extra DNS records.

  * **Cost-effectiveness:** Utilizing internal DNS typically incurs no additional charges, making it efficient and cost-effective.

  * **Dynamic Updates:** Even if the instance's internal IP address changes, the internal DNS record will automatically update, minimizing client-side changes.

**Why Other Options Are Less Ideal**

  * **I & II. Reserve a static external IP address ...** While functional, these options are overly complex for internal VPC communication. They introduce unnecessary components and potential additional costs.

  * **IV. ... using the URL https://[API_NAME]/[API_VERSION]/.** This URL structure doesn't directly provide the IP address. Without internal DNS, client-side configuration would be required to map `[API_NAME]` to the correct address.

Ref:

[https://cloud.google.com/compute/docs/internal-dns#access_by_internal_DNS](https://cloud.google.com/compute/docs/internal-dns#access_by_internal_DNS  https://cloud.google.com/compute/docs/internal-dns)

[https://cloud.google.com/compute/docs/internal-dns](https://cloud.google.com/compute/docs/internal-dns#access_by_internal_DNS  https://cloud.google.com/compute/docs/internal-dns)

</details>

---

### Exam 3 · Q5

**You've deployed a Java application on Cloud Run, requiring access to a Cloud SQL-hosted database. To comply with regulations, the connection must use the Cloud SQL instance's internal IP address. How should you configure connectivity, following Google's best practices?**

- III. Adapt your application to use the Cloud SQL Java connector for connectivity.
- I. Set up your Cloud Run service with a Cloud SQL connection.
- II. Configure your Cloud Run service to utilize a Serverless VPC Access connector.
- IV. Adjust your application to connect to a Cloud SQL Auth proxy instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Configure your Cloud Run service to utilize a Serverless VPC Access connector.

**Correct Option: II. Configure your Cloud Run service to utilize a Serverless VPC Access connector.**

**Explanation:**

  * **Serverless VPC Access:** This is the recommended way to connect Cloud Run to Cloud SQL using private IP addresses. It establishes a secure tunnel within your VPC network.

  * **Security:** Private IP connectivity enhances security by preventing database exposure to the public internet.

  * **No code changes:** This method generally doesn't require any changes to your Java application code.

**Why other options are less ideal:**

  * **I. Cloud SQL connection:** While Cloud Run can connect to Cloud SQL, this usually uses public IP by default, not complying with the internal IP requirement.

  * **III. Cloud SQL Java connector:** The connector is necessary, but on its own, it won't solve the private IP access issue.

  * **IV. Cloud SQL Auth proxy:** The proxy is useful but adds an extra component. Serverless VPC Access is a more streamlined solution for private IP connections from Cloud Run.

**References:**

[https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object](https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object  https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response we)

[https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response we](https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#rest-csek-download-object  https://cloud.google.com/storage/docs/encryption/customer-supplied-keys#response we)

</details>

---

### Exam 3 · Q6

**As you support a business-critical application deployed on Cloud Run in production, the application reports HTTP 500 errors, impacting its usability. You aim to receive alerts when the error rate exceeds 15% of the requests within a specific time frame. What should be your approach?**

- I. Develop a Cloud Function utilizing the Cloud Monitoring API. Schedule this function with Cloud Scheduler to trigger daily, notifying you if errors surpass the defined threshold.
- IV. Implement a Cloud Function consuming the Cloud Monitoring API and schedule it with Cloud Composer to trigger daily, alerting you if errors surpass the set threshold.
- II. Access the Cloud Run page in the Google Cloud console, select the service from the services list, and utilize the Metrics tab to visualize error rates for the revision. Perform this check daily.
- III. Establish an alerting policy within Cloud Monitoring to notify you if errors exceed the specified threshold.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Establish an alerting policy within Cloud Monitoring to notify you if errors exceed the specified threshold.

**Correct Answer:**

  * **III. Establish an alerting policy within Cloud Monitoring to notify you if errors exceed the specified threshold.**

**Justification:**

  * **Purpose-Built:** Cloud Monitoring's alerting functionality is designed specifically for this type of scenario. You can define thresholds, conditions, and notification channels directly within the service.

  * **Real-Time:** Alerting policies continuously monitor your metrics and trigger notifications as soon as the error rate exceeds your defined threshold.

  * **Efficiency:** This eliminates the need to develop custom Cloud Functions, schedule jobs, or manually check metrics.

**Why Other Options Are Less Ideal:**

  * **I. Develop a Cloud Function utilizing the Cloud Monitoring API.**

    * **Unnecessary Complexity:** While feasible, developing a custom Cloud Function introduces more overhead compared to Cloud Monitoring's native alerting features.

    * **Delayed Alerts:** Utilizing Cloud Scheduler for daily checks means you won't receive timely notifications when issues arise.

  * **II. Access the Cloud Run page in the Google Cloud console ...**

    * **Manual Intervention:** This approach relies on manual checks, which isn't proactive or suitable for a production application where timely error detection is critical.

  * **IV. Implement a Cloud Function ...schedule it with Cloud Composer...**

    * **Overkill:** Cloud Composer is designed for complex workflows and data pipelines. Its use for simple error monitoring is over-engineered and adds unnecessary complexity.

**References:**

[https://cloud.google.com/run/docs/monitoring#custom-metrics https://cloud.google.com/run/docs/monitoring#add_alerts](https://cloud.google.com/run/docs/monitoring#custom-metrics   https://cloud.google.com/run/docs/monitoring#add_alerts  https://cloud.google.com/monitoring/alerts)

[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/run/docs/monitoring#custom-metrics   https://cloud.google.com/run/docs/monitoring#add_alerts  https://cloud.google.com/monitoring/alerts)

</details>

---

### Exam 3 · Q12

**You are deploying a single website on App Engine, which must be accessible via the URL http://www.altostrat.com/. What steps should you take to achieve this?**

- I. Verify domain ownership through Webmaster Central. Set up a DNS CNAME record directing to the App Engine canonical name ghs.googlehosted.com.
- III. Configure a mapping in dispatch.yaml to link the domain www.altostrat.com to your App Engine service. Set up a DNS CNAME record pointing to the App Engine canonical name ghs.googlehosted.com.
- II. Verify domain ownership via Webmaster Central. Configure an A record pointing to the singular global App Engine IP address.
- IV. Set up a mapping in dispatch.yaml to direct the domain www.altostrat.com to your App Engine service. Establish an A record pointing to the singular global App Engine IP address.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Verify domain ownership through Webmaster Central. Set up a DNS CNAME record directing to the App Engine canonical name ghs.googlehosted.com.

**I. Verify domain ownership through Webmaster Central. Set up a DNS CNAME record directing to the App Engine canonical name ghs.googlehosted.com.**

Explanation:

  * **Domain Verification:** Webmaster Central allows you to prove ownership of your domain, a prerequisite for configuring custom domains with App Engine.

  * **CNAME Record:** CNAME records create an alias. In this case, `www.altostrat.com` becomes an alias for your App Engine's `ghs.googlehosted.com` address.

  * **App Engine Configuration:** You also need to configure your App Engine project to recognize and serve `www.altostrat.com` (this is done within the Google Cloud Console, not `dispatch.yaml`).

**Why Other Options Are Incorrect:**

  * **II. ... Configure an A record pointing to the singular global App Engine IP address.** App Engine IP addresses can change, making A records unreliable for the long term. CNAMEs are more flexible.

  * **III & IV. Set up a mapping in dispatch.yaml ...** `dispatch.yaml` is primarily for routing requests _within_ your App Engine app, not for setting up the initial custom domain mapping. This step is done in the Cloud Console.

**Reference:**

<https://support.google.com/domains/answer/6009957?hl=en app.mydomain.com CNAME 1H ghs.googlehosted.com.>

</details>

---

### Exam 3 · Q14

**Your team develops stateless services running on Google Kubernetes Engine (GKE). You need to deploy a new service accessible only by other services within the GKE cluster. This service must scale rapidly to meet fluctuating loads. What's the best approach?**

- I. Utilize a Vertical Pod Autoscaler to adjust container sizes and expose them through a ClusterIP Service.
- III. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a ClusterIP Service.
- IV. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a NodePort Service.
- II. Implement a Vertical Pod Autoscaler to adjust container sizes and expose them through a NodePort Service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a ClusterIP Service.

**III. Deploy a Horizontal Pod Autoscaler to scale the containers and expose them through a ClusterIP Service.**

Let's break down why this is the ideal choice:

  * **Internal Access:** ClusterIP Services are designed for communication within the Kubernetes cluster, meeting your requirement of internal-only access.

  * **Scaling:** The Horizontal Pod Autoscaler (HPA) automatically adjusts the number of replicas of your pods based on metrics like CPU or memory usage, ensuring your service can handle varying loads.

  * **Statelessness:** HPAs are well-suited for stateless services, allowing you to scale replicas up and down without affecting data consistency or state.

**Why Other Options Are Less Ideal:**

  * **I & II. Vertical Pod Autoscaling:** VPAs adjust resource requests/limits for _individual pods_ , not their count. This is less suitable for rapidly scaling to meet fluctuating demand.

  * **II & IV. NodePort:** NodePort Services expose your service to external traffic, whereas your requirement is internal-only access.

References:  
<https://cloud.google.com/kubernetes-engine/docs/concepts/service>

</details>

---

### Exam 3 · Q19

**You're preparing to transition a MySQL database to Google Cloud's managed Cloud SQL service. Your Compute Engine VM instances must connect to this Cloud SQL instance without requiring IP whitelisting. Which approach should you take?**

- III. Define a role within Cloud SQL granting external instance access to the database, then assign this role to the Compute Engine instances.
- IV. Deploy a CloudSQL instance in one project, create Compute Engine instances in another project, and establish a VPN connection between them for internal CloudSQL access.
- II. Include Compute Engine instances in a whitelisted project for Cloud SQL access.
- I. Activate private IP for the Cloud SQL instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Activate private IP for the Cloud SQL instance.

**I. Activate private IP for the Cloud SQL instance.**

**Explanation:**

  * **Efficiency and Security:** Private IP provides direct, internal connectivity between your Compute Engine instances and the Cloud SQL instance. This avoids the need for IP whitelisting, simplifies management, and enhances security.

**Why Other Options Are Less Ideal:**

  * **II. Include Compute Engine instances in a whitelisted project for Cloud SQL access.** While feasible, it relies on managing IP addresses and potential updates if your Compute Engine configuration changes. It's less streamlined than the private IP approach.

  * **III. Define a role within Cloud SQL granting external instance access to the database, then assign this role to the Compute Engine instances.** This works but exposes your Cloud SQL instance to the public internet via its public IP, increasing security risks.

  * **IV. Deploy a CloudSQL instance in one project, create Compute Engine instances in another project, and establish a VPN connection between them for internal CloudSQL access.** Establishing a VPN adds complexity, overhead, and potential performance bottlenecks compared to direct private IP connectivity.

**Reference:**

[https://shorturl.at/ryMUW](https://shorturl.at/ryMUW  https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions)

[https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions](https://shorturl.at/ryMUW  https://cloud.google.com/sql/docs/mysql/roles-and-permissions#proxy-roles-permissions)

</details>

---

### Exam 3 · Q23

**You seek to alert on-call engineers promptly about a service degradation in production, minimizing development time. Which option is the most efficient?**

- IV. Employ Stackdriver Monitoring to monitor resources and generate alerts.
- II. Implement Cloud Pub/Sub to monitor resources and generate alerts.
- III. Utilize Stackdriver Error Reporting to capture errors and generate alerts.
- I. Utilize Cloud Function to monitor resources and generate alerts.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Employ Stackdriver Monitoring to monitor resources and generate alerts.

**IV. Employ Stackdriver Monitoring to monitor resources and generate alerts.**

Here's why:

  * **Purpose-Built:** Stackdriver Monitoring (now called Cloud Monitoring) is specifically designed for monitoring resources, metrics, and setting up alerting policies based on various conditions.

  * **Wide Range of Metrics:** It offers comprehensive coverage of infrastructure and application-level metrics, allowing you to pinpoint relevant indicators of service degradation (e.g., error rates, latency, resource utilization).

  * **Alerting Integration:** Stackdriver Monitoring seamlessly integrates with alerting mechanisms, allowing you to define thresholds and quickly notify on-call engineers.

  * **Minimizes Development Effort:** Using Stackdriver Monitoring requires minimal development time compared to building a custom solution.

**Why Other Options are Less Ideal:**

  * **I. Utilize Cloud Function to monitor resources...** While Cloud Functions can be used for this purpose, it involves more development overhead in fetching metrics, defining logic, and handling alerts.

  * **II. Implement Cloud Pub/Sub to monitor resources...** Cloud Pub/Sub is a messaging service. It would need to be integrated with other monitoring and alerting components, adding complexity.

  * **III. Utilize Stackdriver Error Reporting...** Error Reporting is primarily focused on error analysis rather than general resource monitoring and alerting.

**References:**

[https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions](https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions  https://cloud.google.com/error-reporting/docs/notifications  https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring)

[https://cloud.google.com/error-reporting/docs/notifications](https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions  https://cloud.google.com/error-reporting/docs/notifications  https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring)

[https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring](https://cloud.google.com/solutions/serverless-web-performance-monitoring-using-cloud-functions  https://cloud.google.com/error-reporting/docs/notifications  https://cloud.google.com/blog/products/gcp/drilling-down-into-stackdriver-service-monitoring)

</details>

---

### Exam 3 · Q24

**You've recently joined a new team managing a Cloud Spanner database instance in production. The manager tasks you with optimizing the Spanner instance to cut costs while maintaining top-notch reliability and availability. What's the recommended strategy?**

- I. Review error logs using Cloud Logging, gradually reducing Spanner processing units until reaching the minimum required capacity.
- II. Utilize Cloud Trace to monitor incoming requests' requests per second to Spanner, gradually decreasing Spanner processing units until identifying the minimum necessary capacity.
- IV. Utilize Snapshot Debugger to identify application errors, gradually decreasing Spanner processing units until finding the minimum required capacity.
- III. Monitor CPU utilization with Cloud Monitoring, gradually reducing Spanner processing units until reaching the minimum required capacity.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Monitor CPU utilization with Cloud Monitoring, gradually reducing Spanner processing units until reaching the minimum required capacity.

**The recommended strategy for optimizing a Cloud Spanner database instance to cut costs while maintaining reliability and availability would be:**

**III. Monitor CPU utilization with Cloud Monitoring, gradually reducing Spanner processing units until reaching the minimum required capacity.**

**Explanation:**

  * **Cloud Monitoring provides comprehensive metrics for monitoring various aspects of Cloud Spanner, including CPU utilization.**

  * **By monitoring CPU utilization, you can determine the actual resource usage of the Spanner instance and make informed decisions about scaling down processing units.**

  * **Gradually reducing processing units based on CPU utilization allows for fine-tuning the capacity while ensuring that the database can handle the workload without compromising performance or availability.**

  * **This approach provides a data-driven method for optimizing costs while maintaining reliability and availability, as it directly correlates resource usage with the actual workload requirements.**

Options I, II, and IV are less suitable for optimizing Cloud Spanner in terms of cost reduction while maintaining reliability and availability:

  * Option I focuses on error logs, which may not directly reflect the resource usage and workload demands of the Spanner instance.

  * Option II suggests monitoring incoming requests per second, which may not accurately represent the resource utilization or workload patterns of the database.

  * Option IV involves using Snapshot Debugger to identify application errors, which is not directly related to optimizing the resource allocation of the Spanner instance.

</details>

---

### Exam 3 · Q25

**Your application is deployed as a container within a Google Kubernetes Engine (GKE) cluster. You need to securely integrate a secret into your application. What should be your approach?**

- III. Safely store the credential in Cloud KMS. Create a Google service account (GSA) to access the credential from Cloud KMS. Export the GSA as a .json file and mount it into the container as a volume, enabling access to the credential from Cloud KMS.
- I. Create a Kubernetes Secret and inject it as an environment variable into the container.
- IV. Securely store the credential in Secret Manager. Create a Google service account (GSA) to access the credential from Secret Manager. Establish a Kubernetes service account (KSA) to run the container. Utilize Workload Identity to configure your KSA to act as a GSA.
- II. Implement Application-layer Secret Encryption on the cluster using a Cloud Key Management Service (KMS) key.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Securely store the credential in Secret Manager. Create a Google service account (GSA) to access the credential from Secret Manager. Establish a Kubernetes service account (KSA) to run the container. Utilize Workload Identity to configure your KSA to act as a GSA.

**Correct Answer:**

  * **IV. Securely store the credential in Secret Manager. Create a Google service account (GSA) to access the credential from Secret Manager. Establish a Kubernetes service account (KSA) to run the container. Utilize Workload Identity to configure your KSA to act as a GSA.**

**Justification:**

  * **Secret Manager:** Secret Manager is designed specifically to store and manage sensitive data like credentials, offering stronger security than Kubernetes Secrets alone.

  * **Workload Identity:** This method avoids direct handling of service account keys, significantly reducing the risk of key exposure. Kubernetes pods authenticate to Cloud services like Secret Manager using their identity bound to the Kubernetes service account (KSA).

  * **Best Practice:** Google strongly advocates this approach due to its enhanced security posture.

**Why Other Options Are Less Ideal:**

  * **I. Create a Kubernetes Secret and inject it as an environment variable...**

    * **Security Concerns:** While convenient, Kubernetes Secrets are generally base64 encoded, not fully encrypted. They are more vulnerable if the cluster security is compromised.

  * **II. Implement Application-layer Secret Encryption...**

    * **Overhead:** This involves additional complexity, as you'd need to manage encryption/decryption within your application, potentially adding performance impact.

  * **III. Safely store the credential in Cloud KMS...**

    * **Key Handling:** Exporting service account keys as JSON files introduces potential exposure risks. Workload Identity offers a more secure authentication flow.

**References:**

[https://kubernetes.io/docs/concepts/configuration/secret/](https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity   https://cloud.google.com/secret-manager/docs/overview)

[https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity https://cloud.google.com/secret-manager/docs/overview](https://kubernetes.io/docs/concepts/configuration/secret/  https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity   https://cloud.google.com/secret-manager/docs/overview)

</details>

---

### Exam 3 · Q26

**You aim to create**`**fully baked**`**or**`**golden**`**Compute Engine images for your application. Your objective is to configure your application to connect to the correct database depending on the environment (test, staging, production). What's the best approach?**

- III. During Compute Engine instance creation, set up a metadata item with a key named `**DATABASE**` and specify a value for the appropriate database connection string. In your application, read the `**DATABASE**` environment variable and use its value to connect to the suitable database.
- II. During Compute Engine instance creation, assign a tag with the database name to be connected. In your application, retrieve the tags for the current instance via the Compute Engine API, and utilize the tag to construct the appropriate database connection string.
- I. Embed the relevant database connection string in the image and generate a distinct image for each environment.
- IV. During Compute Engine instance creation, configure a metadata item with a key named `**DATABASE**` and specify a value for the appropriate database connection string. In your application, query the metadata server for the `**DATABASE**` value and use it to connect to the suitable database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. During Compute Engine instance creation, configure a metadata item with a key named `**DATABASE**` and specify a value for the appropriate database connection string. In your application, query the metadata server for the `**DATABASE**` value and use it to connect to the suitable database.

**IV. During Compute Engine instance creation, configure a metadata item with a key named DATABASE and specify a value for the appropriate database connection string. In your application, query the metadata server for the DATABASE value and use it to connect to the suitable database.**

Here's why this approach excels:

  * **Flexibility:** Metadata provides a dynamic way to pass environment-specific configuration to your application during instance creation. This avoids building separate images for each environment.

  * **Maintainability:** A single image can be used across all environments, simplifying image management and updates.

  * **Security:** Sensitive database connection strings are not embedded directly within the image, improving security posture.

  * **Standard Practice:** Utilizing metadata is a common and recommended way to configure Compute Engine instances.

**Why Other Options Are Less Ideal:**

  * **I. Embedding Connection Strings:** Hardcoding database connection strings into images creates multiple images, hindering maintainability and security.

  * **II. Using Instance Tags:** While tags can be useful for classification, they are less optimal for storing sensitive information like database connection strings.

  * **III. Environment Variables:** Compute Engine doesn't have a built-in mechanism to set environment variables during instance creation like metadata does.

**References:**

[https://cloud.google.com/compute/docs/metadata/querying-metadata](https://cloud.google.com/compute/docs/metadata/querying-metadata  https://cloud.google.com/compute/docs/metadata/overview)

[https://cloud.google.com/compute/docs/metadata/overview](https://cloud.google.com/compute/docs/metadata/querying-metadata  https://cloud.google.com/compute/docs/metadata/overview)

</details>

---

### Exam 3 · Q30

**While running a containerized application on Google Kubernetes Engine with container images stored in Container Registry and employing CI/CD practices, how can you prevent the deployment of containers containing known critical vulnerabilities?**

- III. Enable the Container Scanning API for vulnerability scanning, review vulnerability reporting in Container Registry within the Cloud Console, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.
- I. Utilize Web Security Scanner to automatically crawl the application, review scan results in application logs, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.
- IV. Enable the Container Scanning API for vulnerability scanning, programmatically review vulnerability reporting through the Container Scanning API, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.
- II. Utilize Web Security Scanner to automatically crawl the application, review scan results in the Cloud Console's scan details page, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Enable the Container Scanning API for vulnerability scanning, programmatically review vulnerability reporting through the Container Scanning API, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.

**IV. Enable the Container Scanning API for vulnerability scanning, programmatically review vulnerability reporting through the Container Scanning API, and provide an attestation of the container's freedom from critical vulnerabilities, enforced by Binary Authorization policy before deployment.**

Here's why this stands out:

  * **Automation & Integration:** Programmatic interaction with the Container Scanning API enables you to integrate vulnerability checks directly into your CI/CD pipeline for a seamless workflow.

  * **Customizable Severity Assessment:** Programmatically parsing the vulnerability scan results gives you fine-grained control to define what constitutes a "critical" vulnerability based on your organization's risk tolerance.

  * **Enforcement:** Binary Authorization provides a robust mechanism to enforce policies based on the scan results, preventing vulnerable images from being deployed into your GKE clusters.

  * **Scalability:** This solution scales well, enabling you to automate vulnerability checks across a large number of container images.

**Why Other Options Are Less Ideal:**

  * **I & II. Web Security Scanner:** While useful for web application security, Web Security Scanner doesn't focus on container image vulnerability scanning.

  * **III. Manual Review in Console:** Relying on manual review in the Cloud Console slows down your CI/CD pipelines and is less scalable for larger deployments.

</details>

---

### Exam 3 · Q34

**You're planning to publish a straightforward HTML application online, which serves as an FAQ resource for your application. This static site comprises images, HTML, CSS, and JavaScript. Your aim is to make it accessible on the internet with minimal effort. What's the recommended action?**

- II. Deploy your application to an App Engine environment.
- III. Set up a Compute Engine instance with Apache web server installed. Configure Apache to host the application.
- IV. Containerize your application first. Then, deploy this container to Google Kubernetes Engine (GKE) and assign an external IP address to the GKE pod hosting the application.
- I. Upload your application to Cloud Storage.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Upload your application to Cloud Storage.

**I. Upload your application to Cloud Storage.**

**Explanation:**

For a simple, static website, Cloud Storage is the easiest way to make it publicly accessible:

  * **Simplicity:** Directly upload your files (HTML, CSS, JavaScript, Images) to a Cloud Storage bucket and configure the bucket for website hosting.

  * **Cost-effective:** Cloud Storage is a cost-effective option for simple website hosting.

  * **No Server Management:** You don't have to manage virtual machines or webserver software.

  * **Global Distribution:** Cloud Storage leverages Google's global infrastructure for low-latency content delivery.

**Why Other Options Are Less Ideal:**

  * **II. Deploy your application to an App Engine environment.** App Engine is overkill for a static site, adding unnecessary complexity and potential overhead.

  * **III. Set up a Compute Engine instance ...** This involves managing a virtual machine, installing, and configuring a web server – much more work than necessary for a static site.

  * **IV. Containerize your application ...** Containerizing and using Kubernetes adds complexity (and cost) without offering significant benefits for a purely static site.

**Reference:**  
<https://examlab.co/google/google-cloud-professional-cloud-developer>

</details>

---

### Exam 3 · Q35

**Upon migrating certain applications to Google Cloud, you observe that your on-premises legacy monitoring platform, used for both on-premises and cloud applications, is responding sluggishly to urgent issues in the cloud deployments. What's the recommended course of action?**

- III. Revert some traffic to your previous platform and conduct A/B testing between the two platforms simultaneously.
- II. Install the Cloud Monitoring agent on your Compute Engine instances.
- IV. Utilize Cloud Logging and Cloud Monitoring for log capture, monitoring, and alerting, directing alerts to your existing platform.
- I. Transition to Cloud Monitoring as a replacement for your current monitoring platform.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Utilize Cloud Logging and Cloud Monitoring for log capture, monitoring, and alerting, directing alerts to your existing platform.

**IV. Utilize Cloud Logging and Cloud Monitoring for log capture, monitoring, and alerting, directing alerts to your existing platform.**

**Justification:**

  * **Integration Focus:** This approach focuses on integrating the strengths of Google Cloud's native monitoring tools with your existing platform. This minimizes disruption and leverages both tools effectively.

  * **Cloud-Native Advantages:** Cloud Logging and Cloud Monitoring are optimized for Google Cloud environments. They provide in-depth visibility into your cloud resources and offer features tailored to GCP.

  * **Minimize Disruption:** Integrating alerts with your existing platform avoids a complete overhaul of your monitoring setup and associated processes. This ensures a smoother transition and lessens the risk of overlooking issues.

  * **Flexibility:** This approach offers flexibility as you gradually evaluate the capabilities of Cloud Monitoring. If needed, you can further expand your use of Cloud Monitoring over time.

**Why Other Options are Less Suitable:**

  * **I. Transition to Cloud Monitoring as a replacement for your current monitoring platform.** A complete replacement introduces a significant change which could be disruptive to existing workflows. Integration may be a better starting point.

  * **II. Install the Cloud Monitoring agent on your Compute Engine instances.** This improves resource monitoring on Compute Engine, but it may not fully address the broader cloud application monitoring requirements and the integration needs with your existing system.

  * **III. Revert some traffic to your previous platform and conduct A/B testing between the two platforms simultaneously.** While helpful for evaluation, splitting traffic and A/B testing setups can be complex, and might not be the most efficient approach to improve monitoring responsiveness for urgent issues.

</details>

---

### Exam 3 · Q36

**Your application is deployed using a custom machine image, with multiple unique deployments organized into separate managed instance groups, each with its own template. Each deployment requires distinct configuration values. How can you provide these unique values to each deployment while using the same custom machine image across all deployments, leveraging Compute Engine's built-in functionalities?**

- II. Store the unique configuration values in a Cloud Bigtable table, accessible by each deployment.
- III. Include the unique configuration values in the instance template's startup script.
- I. Store the unique configuration values in a persistent disk accessible to each deployment.
- IV. Embed the unique configuration values in the instance template's instance metadata.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Embed the unique configuration values in the instance template's instance metadata.

**IV. Embed the unique configuration values in the instance template's instance metadata.**

Here's why this stands out as the most suitable solution:

  * **Built-in Mechanism:** Instance metadata is designed specifically for providing configuration data to Compute Engine instances.

  * **Flexibility:** Metadata can be defined at the instance template level, allowing customization for each deployment.

  * **Security:** Metadata is accessible only from within the VM instance, enhancing security compared to external storage solutions.

  * **Ease of Management:** You can manage metadata through the Cloud Console, gcloud commands, or API calls, making updates straightforward.

**Why Other Options Have Drawbacks:**

  * **I. Store the unique configuration values in a persistent disk ...** This introduces dependencies on additional infrastructure (the disk) and potential complications around disk mounting and access permissions.

  * **II. Store the unique configuration values in a Cloud Bigtable table ...** Using Bigtable adds complexity. It's more suitable for large-scale, structured data rather than simple deployment-specific configuration values.

  * **III. Include the unique configuration values in the instance template's startup script.** Hardcoding values in the startup script makes it inflexible. Updates would require modifying the script and potentially rebuilding the machine image.

**References:**

[https://cloud.google.com/compute/docs/instances/startup-scripts](https://cloud.google.com/compute/docs/instances/startup-scripts  https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom)

[https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom](https://cloud.google.com/compute/docs/instances/startup-scripts  https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom)

</details>

---

### Exam 3 · Q39

**In ensuring private traffic on Google Cloud for an application utilizing PostgreSQL and Cloud Run, which approach, aligning with Google's best practices and leveraging managed services, should be pursued?**

- III. Utilize Cloud SQL and Cloud Run in separate projects. Configure a private IP address for Cloud SQL, enable private services access, and establish a Serverless VPC Access connector. Set up a VPN connection between the projects and configure Cloud Run to use the connector for connecting to Cloud SQL.
- II. Deploy PostgreSQL on a Compute Engine virtual machine (VM) and enable Cloud Run in the same project. Allocate a private IP address to the VM, enable private services access, and create a Serverless VPC Access connector. Configure Cloud Run to utilize this connector for connecting to the VM hosting PostgreSQL.
- I. Enable Cloud SQL and Cloud Run within the same project. Configure a private IP address for Cloud SQL and activate private services access. Set up a Serverless VPC Access connector, then configure Cloud Run to utilize it for connecting to Cloud SQL.
- IV. Deploy PostgreSQL on a Compute Engine VM and enable Cloud Run in different projects. Assign a private IP address to the VM, enable private services access, and create a Serverless VPC Access connector. Set up a VPN connection between the projects and configure Cloud Run to utilize the connector for accessing the VM hosting PostgreSQL.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Enable Cloud SQL and Cloud Run within the same project. Configure a private IP address for Cloud SQL and activate private services access. Set up a Serverless VPC Access connector, then configure Cloud Run to utilize it for connecting to Cloud SQL.

**I. Enable Cloud SQL and Cloud Run within the same project. Configure a private IP address for Cloud SQL and activate private services access. Set up a Serverless VPC Access connector, then configure Cloud Run to utilize it for connecting to Cloud SQL.**

Here's why this is the most streamlined, secure, and Google-recommended approach:

  * **Simplified Networking:** Keeping Cloud SQL and Cloud Run in the same project and using a Serverless VPC Access connector eliminates complex VPN configuration.

  * **Managed Services:** This leverages fully managed Google Cloud services, minimizing operational overhead.

  * **Secure by Default:** Private services access and private IPs enhance security by isolating traffic within Google's internal network.

  * **Google Best Practice:** This is the approach explicitly recommended by Google for this scenario.

**Why Other Options are Less Ideal:**

  * **II. Self-managed PostgreSQL:** Deploying PostgreSQL on a Compute Engine VM adds the burden of managing the database instance and its security.

  * **III & IV. Cross-project VPN:** Setting up VPN tunnels introduces complexity, potential performance overhead, and the need to manage additional networking infrastructure.

**References:**  
[https://cloud.google.com/sql/docs/postgres/connect-run#configure https://cloud.google.com/sql/docs/postgres/connect-run#private-ip](https://cloud.google.com/sql/docs/postgres/connect-run#configure   https://cloud.google.com/sql/docs/postgres/connect-run#private-ip)

</details>

---

### Exam 3 · Q40

**You are designing an application to receive messages from a single Pub/Sub topic and insert corresponding rows into a database. The application runs on Linux and utilizes preemptible virtual machines to reduce costs. To ensure a graceful shutdown, what should you do?**

- III. Implement a shutdown script that writes a file in a specified location, which the application polls every five minutes. Upon reading the file, the application disconnects from the database.
- I. Develop a shutdown script utilizing inter-process signals to notify the application process to disconnect from the database.
- II. Create a shutdown script that broadcasts a message to all logged-in users, informing them of the Compute Engine instance shutdown, and advises them to save their work and log out.
- IV. Write a shutdown script that publishes a message to the Pub/Sub topic indicating a shutdown is in progress. After the application reads the message, it disconnects from the database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Develop a shutdown script utilizing inter-process signals to notify the application process to disconnect from the database.

**I. Develop a shutdown script utilizing inter-process signals to notify the application process to disconnect from the database.**

Here's why this is the most suitable approach:

  * **Reliability:** Signals are a standard and reliable mechanism for inter-process communication in Linux, ensuring the message is likely to be received by the application.

  * **Efficiency:** Signals are efficient, ensuring a prompt response to the shutdown event.

  * **Preemptible VM Specific:** Shutdown scripts are the recommended way to handle graceful termination of preemptible VMs.

  * **Focus:** This solution specifically addresses graceful shutdown of the application and database connection, without unnecessary steps.

**Why other options are not as good:**

  * **II. User Notification:** While user notification _might_ be helpful in a different context, it's not relevant to graceful shutdown of the automated process.

  * **III. File Polling:** Polling adds overhead, introduces delays (especially with a 5-minute interval), and is generally less reliable than signals.

  * **IV. Pub/Sub Overkill:** While sending a shutdown message to Pub/Sub could be used as an additional notification, it overcomplicates graceful shutdown for a single subscriber application.

**Reference:**

<https://cloud.google.com/compute/docs/instances/preemptible#preemption>

</details>

---

### Exam 3 · Q42

**As you deploy your application to a Compute Engine virtual machine instance, it logs its files to disk. You want to view these logs in Stackdriver Logging without modifying the application code. What's the recommended approach?**

- I. Install the Stackdriver Logging Agent and set it up to transmit the application logs.
- IV. Modify the application to log to /var/log so that its logs are automatically sent to Stackdriver Logging.
- III. Specify the log file folder path in the instance's metadata to configure it for sending the application logs.
- II. Utilize a Stackdriver Logging Library to directly log from the application to Stackdriver Logging.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Install the Stackdriver Logging Agent and set it up to transmit the application logs.

**I. Install the Stackdriver Logging Agent and set it up to transmit the application logs.**

**Explanation:**

The Stackdriver Logging Agent (now called the Cloud Logging Agent) is the most flexible and least invasive way to achieve this:

  * **No Code Changes:** You don't have to modify your existing logging mechanisms, preserving your application logic.

  * **Customization:** The agent can monitor custom log files and even parse them to extract structured data, making it adaptable to your application's log format.

  * **Centralization:** The agent reliably sends logs to Stackdriver Logging, giving you a unified view in the Google Cloud Console.

**Why Other Options Are Less Ideal:**

  * **II. Utilize a Stackdriver Logging Library...** This requires changes to your code, adding the library and potentially modifying your logging statements.

  * **III. Specify the log file folder path...** This method relies on specific agent configurations and log formats, making it less flexible than actively configuring the agent.

  * **IV. Modify the application to log to /var/log...** This assumes your application can easily be reconfigured to write to `/var/log`. It also assumes standard log paths, which might not always be true.

**Reference:**

<https://cloud.google.com/logging/docs/agent/logging/installation>

</details>

---

### Exam 3 · Q46

**During the development of an application with multiple microservices on Google Kubernetes Engine (GKE), one microservice requires connectivity to a third-party on-premises database. It's crucial to securely store database credentials and ensure regular rotation, following security best practices. What's the recommended approach?**

- IV. Securely store credentials as a Kubernetes Secret, employing the Cloud Key Management Service plugin for encryption and decryption.
- III. Store credentials in an encrypted volume mount, linking a Persistent Volume Claim to the client Pod.
- I. Save credentials in a sidecar container proxy, using it for database connections.
- II. Set up a service mesh to control traffic between microservice Pods and the database.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Securely store credentials as a Kubernetes Secret, employing the Cloud Key Management Service plugin for encryption and decryption.

**The recommended approach for securely storing and managing database credentials for a microservice running on Google Kubernetes Engine (GKE) would be option IV:**

**IV. Securely store credentials as a Kubernetes Secret, employing the Cloud Key Management Service plugin for encryption and decryption.**

**Explanation:**

  1. **Kubernetes Secrets** : Kubernetes provides a built-in resource called Secrets, designed specifically for storing sensitive information such as passwords, OAuth tokens, and SSH keys. Kubernetes Secrets are a natural fit for storing database credentials securely within the cluster.

  2. **Cloud Key Management Service (KMS)** : Google Cloud Platform offers a Key Management Service (KMS) that allows you to manage cryptographic keys for your cloud services. By using KMS, you can encrypt the Secrets stored in Kubernetes, adding an extra layer of security to the sensitive data.

  3. **Plugin Integration** : Kubernetes allows for plugins to integrate with external key management services like Google Cloud KMS. By using the Cloud KMS plugin, you can ensure that the Secrets stored in Kubernetes are encrypted using keys managed by Cloud KMS, adding another layer of security.

Options I, II, and III are not the best fit for securely managing database credentials in this scenario:

I. Saving credentials in a sidecar container proxy might introduce unnecessary complexity and potential security vulnerabilities. Additionally, sidecar containers are typically used for tasks such as logging, monitoring, or additional functionality, rather than securely storing sensitive data.

II. Setting up a service mesh could help control traffic between microservices within the cluster, but it's not directly related to securely storing database credentials.

III. Storing credentials in an encrypted volume mount is better than plain text storage, but it lacks the fine-grained control and integration with key management services provided by Kubernetes Secrets with Cloud KMS integration. Additionally, managing encryption keys and rotation might be more complex compared to using Kubernetes Secrets with a KMS plugin.

**Reference:**

<https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#reencrypt-secrets>

</details>

---

### Exam 3 · Q49

**You're preparing to deploy a new application revision to Google Kubernetes Engine (GKE) in a production environment. Considering potential container issues, you aim to minimize risks while following Google's recommended practices. Which approach should you take?**

- III. Convert the Deployment to a StatefulSet and conduct a rolling update with a PodDisruptionBudget set at 80%.
- IV. Convert the Deployment to a StatefulSet and execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.
- II. Execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.
- I. Conduct a rolling update with a PodDisruptionBudget set at 80%.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Conduct a rolling update with a PodDisruptionBudget set at 80%.

**Correct Answer:**

  * **I. Conduct a rolling update with a PodDisruptionBudget set to 80%.**

**Justification:**

  * **Minimizing Downtime:** Rolling updates replace pods gradually, ensuring service availability during the update process.

  * **Safety Net:** A PodDisruptionBudget (PDB) limits the number of pods that can be unavailable simultaneously. Setting it to 80% guarantees that at least 80% of your pods remain active, mitigating the risk of full service disruption.

  * **Google-Recommended:** This strategy aligns with Google's best practices for production deployments on GKE.

**Why Other Options Are Less Suitable:**

  * **II. Execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.**

    * **HPA's Purpose:** A HorizontalPodAutoscaler (HPA) is meant to adjust the number of replicas based on load, not primarily for deployment strategies. Disabling scaling down during the upgrade might help but doesn't provide the same level of control as a PDB.

  * **III. Convert the Deployment to a StatefulSet and conduct a rolling update with a PodDisruptionBudget set at 80%.**

  * **IV. Convert the Deployment to a StatefulSet and execute a rolling update with a HorizontalPodAutoscaler scale-down policy value of 0.**

    * **Unnecessary for Stateless Apps:** StatefulSets are designed for stateful applications that require stable identifiers and persistent storage. If your application is stateless, converting to a StatefulSet adds unnecessary complexity.

**References:**

[https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect  https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/   https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster  https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/)

[https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/ https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect  https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/   https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster  https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/)

[https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#identify-an-application-to-protect  https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/   https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster  https://blog.knoldus.com/how-to-avoid-outages-in-your-kubernetes-cluster-using-pdb/)

</details>

---

### Exam 3 · Q52

**You aim to monitor the memory usage of your application deployed on Compute Engine. What's the appropriate action?**

- I. Implement the Stackdriver Client Library.
- III. Utilize the Stackdriver Metrics Explorer.
- II. Deploy the Stackdriver Monitoring Agent.
- IV. Access the Google Cloud Platform Console.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Deploy the Stackdriver Monitoring Agent.

**II. Deploy the Stackdriver Monitoring Agent.**

Here's why this is the best option:

  * **Comprehensive Metrics:** The Stackdriver Monitoring Agent automatically collects a wide range of system-level metrics, including memory usage, and sends them to Stackdriver Monitoring.

  * **Minimal Configuration:** Agent installation and basic configuration are relatively straightforward.

  * **Visualization & Alerting:** Stackdriver Monitoring provides tools for visualizing memory usage data over time and creating alerts based on thresholds you define.

**Why Other Options Are Less Ideal:**

  * **I. Implement the Stackdriver Client Library.** While this library _can_ be used for custom metrics, it's overkill for basic memory usage. The agent handles this automatically.

  * **III. Utilize the Stackdriver Metrics Explorer.** Metrics Explorer is for viewing and querying data collected by Stackdriver Monitoring – this relies on the agent collecting those metrics first.

  * **IV. Access the Google Cloud Platform Console.** The GCP console offers a high-level overview of resources, but lacks the granular historical views and alerting capabilities you'd need for detailed memory monitoring.

References:

[https://cloud.google.com/monitoring/api/metrics_agent#agent-memory](https://cloud.google.com/monitoring/api/metrics_agent#agent-memory  https://cloud.google.com/monitoring/agent)

[https://cloud.google.com/monitoring/agent](https://cloud.google.com/monitoring/api/metrics_agent#agent-memory  https://cloud.google.com/monitoring/agent)

</details>

---

### Exam 3 · Q55

**You've deployed a new application to Google Kubernetes Engine and are facing performance degradation. Logs are directed to Cloud Logging, and Prometheus metrics are captured using a sidecar model. How do you effectively correlate metrics and log data to troubleshoot and set up real-time alerts, all while minimizing costs?**

- II. Export both Cloud Logging logs and Prometheus metrics to Cloud Bigtable. Conduct a query to combine the data for analysis within Google Data Studio.
- IV. Export Prometheus metrics and utilize Cloud Monitoring to visualize them as external metrics. Configure Cloud Monitoring to establish log-based metrics from the logs and correlate them with the Prometheus data.
- III. Export Cloud Logging logs and stream Prometheus metrics to BigQuery. Set up periodic queries to merge the data and trigger notifications using Cloud Tasks.
- I. Derive custom metrics from Cloud Logging logs, then leverage Prometheus to import them via the Cloud Monitoring REST API.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Export Prometheus metrics and utilize Cloud Monitoring to visualize them as external metrics. Configure Cloud Monitoring to establish log-based metrics from the logs and correlate them with the Prometheus data.

**IV. Export Prometheus metrics and utilize Cloud Monitoring to visualize them as external metrics. Configure Cloud Monitoring to establish log-based metrics from the logs and correlate them with the Prometheus data.**

Here's why this stands out as the best choice:

  * **Unified Insights:** Cloud Monitoring provides a centralized platform for both Prometheus metrics and log-based metrics, enabling easier correlation and visualization.

  * **Real-time Alerting:** Cloud Monitoring's built-in alerting mechanisms allow you to create alerts directly based on both metrics and log-based metrics.

  * **Cost Optimization:** Cloud Monitoring is generally a more cost-effective solution compared to exporting all data to BigQuery or Bigtable.

  * **Minimized Complexity:** This approach avoids the overhead of setting up streaming pipelines and additional data transformations.

**Why Other Options Are Less Ideal:**

  * **I. Deriving Custom Metrics:** While possible, it adds complexity and potential latency to your troubleshooting workflow.

  * **II. Cloud Bigtable & Data Studio:** Bigtable is geared towards large-scale data management. Data Studio adds cost and complexity when Cloud Monitoring can cover visualization and alerting needs.

  * **III. BigQuery & Cloud Tasks:** While queries in BigQuery are powerful, setting up this pipeline increases operational overhead and might introduce latency for real-time troubleshooting.

**References:**

<https://cloud.google.com/stackdriver/docs/solutions/gke/prometheus#viewing_metrics>

</details>

---

### Exam 3 · Q58

**As you develop a new web application using Cloud Run and commit code to Cloud Source Repositories, you aim to deploy new code efficiently. You've already crafted a Cloud Build YAML file that builds a container and executes the command: gcloud run deploy. What's the next step?**

- IV. Schedule a Cron job to run the command gcloud builds submit every 24 hours.
- I. Establish a Pub/Sub topic to receive notifications when code is pushed to the repository. Set up a Pub/Sub trigger to execute the build file upon receiving an event on the topic.
- II. Configure a build trigger to activate the build file when code is pushed to the development branch of the repository.
- III. Implement a webhook build trigger to execute the build file upon receiving HTTP POST calls at the webhook URL.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Configure a build trigger to activate the build file when code is pushed to the development branch of the repository.

**Correct Answer:**

  * **II. Configure a build trigger to activate the build file when code is pushed to the development branch of the repository.**

**Justification:**

  * **Direct Integration:** Cloud Build triggers offer the most seamless integration with Cloud Source Repositories. They directly monitor your repo for changes.

  * **Branch Specificity:** You can configure the trigger to activate only on pushes to the designated branch (development in this case), ensuring builds happen when you expect them.

  * **Efficiency:** This automated process eliminates the need for manual intervention or external systems for triggering builds.

**Why Other Options Are Less Ideal:**

  * **I. Establish a Pub/Sub topic ...**

    * **Added Complexity:** While Pub/Sub could be used to trigger Cloud Build, it introduces an additional layer to manage compared to a direct build trigger.

  * **III. Implement a webhook build trigger...**

    * **External Dependency:** Webhooks require an external system to send the HTTP POST request, adding a dependency outside of Cloud Build.

  * **IV. Schedule a Cron job...**

    * **Inflexible:** Cron jobs are good for scheduled tasks but less responsive to dynamic events like code pushes. Also, daily builds could be too infrequent for active development.

**References:**  
[https://cloud.google.com/build/docs/automating-builds/create-manage-triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers  https://cloud.google.com/build/docs/triggers  https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo)

[https://cloud.google.com/build/docs/triggers](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers  https://cloud.google.com/build/docs/triggers  https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo)

[https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers  https://cloud.google.com/build/docs/triggers  https://cloud.google.com/build/docs/automating-builds/create-manage-triggers#connect_repo)

</details>

---

### Exam 4 · Q5

**How can you test conversion rates between three different website designs without altering the application code deployed on Compute Engine?**

- III. Deploy the website on Cloud Functions as three separate functions.
- I. Deploy the website on Cloud Run and utilize traffic splitting to test different designs.
- II. Deploy the website on Cloud Run as three separate revisions to test different designs.
- IV. Deploy the website on Cloud Functions and implement custom code to display different designs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Deploy the website on Cloud Run and utilize traffic splitting to test different designs.

To test conversion rates between three different website designs without altering the application code deployed on Compute Engine, the most appropriate approach is:

**I. Deploy the website on Cloud Run and utilize traffic splitting to test different designs.**

Explanation:

Option I involves deploying the website on Cloud Run and utilizing traffic splitting to direct users to different versions of the website with different designs. Cloud Run allows for easy deployment of containerized applications, and traffic splitting enables directing a portion of the traffic to different revisions of the same service. This approach allows for testing different designs in a real-world scenario without modifying the application code.

Option II suggests deploying the website on Cloud Run as three separate revisions to test different designs. While this approach is feasible, it may require more manual management and monitoring of the different revisions compared to traffic splitting.

Option III proposes deploying the website on Cloud Functions as three separate functions. However, Cloud Functions are designed for event-driven serverless execution, and deploying a website as separate functions may not be the most suitable approach for testing different designs.

Option IV suggests deploying the website on Cloud Functions and implementing custom code to display different designs. While technically possible, this approach would require significant custom development and may introduce complexity and maintenance overhead.

Therefore, option I is the most appropriate approach for testing conversion rates between three different website designs without altering the application code deployed on Compute Engine.

**Documentation:**

  * Traffic splitting in Cloud Run: <https://cloud.google.com/run/docs/rollouts-deployments#traffic_splitting>

</details>

---

### Exam 4 · Q10

**In your production environment, your application runs on Compute Engine virtual machine instances managed by a managed instance group and accessed through an HTTP(s) load balancer. Users are reporting inability to access the application. How can you set up monitoring to receive alerts when the application becomes unavailable?**

- IV. Enable managed instance group health checks to monitor the health of your instances.
- I. Implement smoke tests to detect application unavailability.
- II. Set up Stackdriver uptime checks to monitor the availability of your application.
- III. Configure Cloud Load Balancing health checks to monitor the health of your instances.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Set up Stackdriver uptime checks to monitor the availability of your application.

**Option II, "Set up Stackdriver uptime checks to monitor the availability of your application," is the most suitable choice for setting up monitoring to receive alerts when the application becomes unavailable.**

Justification:

  * Stackdriver uptime checks provide a straightforward method to monitor the availability of your application by periodically pinging its endpoints. This directly addresses the need to monitor application unavailability.

  * Stackdriver integrates seamlessly with Google Cloud Platform's monitoring and alerting capabilities, allowing you to configure alerts based on the results of uptime checks.

  * By setting up Stackdriver uptime checks, you can quickly detect when your application becomes unavailable and receive timely alerts to take necessary actions.

  * This option focuses specifically on monitoring application availability, which is crucial for ensuring a good user experience.

While the other options (I, III, and IV) also contribute to monitoring and maintaining the health of your infrastructure and application, they do not directly address the requirement of setting up monitoring to receive alerts when the application becomes unavailable.

For further details, you can refer to the documentation on [Monitoring uptime](https://cloud.google.com/monitoring/uptime-checks).

</details>

---

### Exam 4 · Q18

You manage an application deployed on **GKE clusters** across multiple environments, using **Cloud Build** for user acceptance testing (UAT). **Artifact Analysis** is integrated with **Cloud Build** , and the **Binary Authorization API** is enabled in all Google Cloud projects for your environments. To ensure that only container images passing specific UAT tests are deployed to production, and with an attestor already created, what should you do next?

- D. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.
- A. After the UAT phase, sign the attestation with a key stored as a Kubernetes secret and add a GKE cluster-specific rule in Binary Authorization for the UAT Google Cloud project.
- C. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a default rule in Binary Authorization for the UAT Google Cloud project.
- B. After the UAT phase, sign the attestation with a key stored as a Kubernetes secret and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.

The correct answer is 

**D. After the UAT phase, sign the attestation with a key stored in Cloud Key Management Service (KMS) and add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project policy.**

Explanation:

To ensure that only container images passing UAT are deployed to production, you need to follow these steps:

  1. **Sign the attestation** after the UAT phase, indicating that the image has passed the necessary UAT tests. Using **Cloud Key Management Service (KMS)** to store the signing key is a best practice for security and management, as it allows centralized control over cryptographic keys.

  2. **Add a GKE cluster-specific rule in Binary Authorization for the production Google Cloud project**. This rule ensures that only container images with the required attestation can be deployed to production. By applying this rule to the production project, you restrict deployments to images that have passed UAT.

**Justifications for Incorrect Options:**

  * **Option A: Sign with a key stored as a Kubernetes secret and add a rule in Binary Authorization for the UAT Google Cloud project**  
Storing the signing key as a Kubernetes secret is less secure than using Cloud KMS. Additionally, the Binary Authorization rule should be set in the **production** project, as UAT is not the target deployment environment.

  * **Option B: Sign with a key stored as a Kubernetes secret and add a rule in Binary Authorization for the production project**  
Although this option uses the correct environment for Binary Authorization (production), storing the signing key as a Kubernetes secret is not recommended for security. Using Cloud KMS for key management is more secure.

  * **Option C: Sign with a key stored in Cloud KMS and add a default rule in Binary Authorization for the UAT project**  
Adding a Binary Authorization rule in the UAT project does not control deployments to the production environment. You need the rule in the production project to ensure only tested images are deployed there.

**Relevant Documentation:**

For more information on setting up Binary Authorization and best practices with Cloud KMS, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

  * [Using Binary Authorization with GKE](https://cloud.google.com/binary-authorization/docs)

</details>

---

### Exam 4 · Q22

**While testing your ecommerce web application, which employs Cloud Run and Memorystore for Redis, you encounter a 502 Bad Gateway error in the browser. Upon investigation, you discover that the application is failing to connect to Memorystore. What is the probable cause of this error?**

- III. The firewall rule permitting a connection between Cloud Run and Memorystore was inadvertently removed during an infrastructure update by the DevOps team.
- IV. You configured your application to utilize a Serverless VPC Access connector on a different subnet in a distinct region than your Cloud Run service.
- I. Your Memorystore for Redis instance was deployed without a public IP address.
- II. You configured your Serverless VPC Access connector in a different region than your Cloud Run service.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. You configured your Serverless VPC Access connector in a different region than your Cloud Run service.

Correct answer

**II. You configured your Serverless VPC Access connector in a different region than your Cloud Run service.**

I is not correct because Cloud Run connects to Memorystore via the Serverless VPC Connector. Connections are over private networks. Public addresses are not required.  
II is correct. All of the components must be in the same region.  
III is not correct because for connectivity between Cloud Run and Memorystore all that is required is a Serverless VPN Connector.  
IV is not correct. The Serverless VPC Connector is configured with a non-overlapping subnet that is not associated with the VPC.  
  
**References:**

[https://cloud.google.com/memorystore/docs/redis/redis-overview#connecting](%0d https:/cloud.google.com/memorystore/docs/redis/redis-overview#connecting)

[https://cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run](%0d https:/cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run%0d)

[https://cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector](%0d https:/cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector)

</details>

---

### Exam 4 · Q23

**You're deploying an application to a Compute Engine virtual machine instance equipped with the Stackdriver Monitoring Agent. The application, a Unix process, needs monitoring to alert if it hasn't run for at least 5 minutes. However, you can't modify the application to generate metrics or logs. Which alert condition is most appropriate for this scenario?**

- II. Configure process health monitoring to detect any issues with the Unix process.
- III. Utilize metric absence detection to alert when the Unix process hasn't been active for the specified duration.
- I. Set up an uptime check to monitor the availability of the virtual machine instance.
- IV. Establish a metric threshold to trigger an alert when the Unix process activity falls below the defined threshold.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Utilize metric absence detection to alert when the Unix process hasn't been active for the specified duration.

**Correct Option:**

  * **III. Utilize metric absence detection to alert when the Unix process hasn't been active for the specified duration.**

**Justification:**

Metric absence detection perfectly aligns with the scenario where the application doesn't generate custom metrics or logs. Since most Unix processes utilize system resources, their activity often reflects in system-level metrics like CPU or memory usage. Metric absence allows you to configure an alert that triggers if these metrics haven't been reported for a certain timeframe (5 minutes in this case). This signifies that the process is likely inactive.

  * Supporting Documentation: <https://stackoverflow.com/questions/53095774/stackdriver-monitoring-metric-absent>

**Incorrect Options:**

  * **I. Set up an uptime check to monitor the availability of the virtual machine instance.**

  * Justification: Uptime checks are effective for ensuring the entire VM is operational, but they don't provide insight into the status of individual processes running within the VM. A VM can be online while a specific process within it might be inactive.

  * **II. Configure process health monitoring to detect any issues with the Unix process.**

  * Justification: While this might seem like a suitable solution, Stackdriver Monitoring Agent has limitations when monitoring arbitrary Unix processes. It requires the application to send custom metrics for effective process health monitoring. In this scenario, the application doesn't emit such metrics.

  * Supporting Documentation: <https://cloud.google.com/monitoring/custom-metrics>

  * **IV. Establish a metric threshold to trigger an alert when the Unix process activity falls below the defined threshold.**

  * Justification: This approach could be viable if the Unix process has a metric explicitly indicating its activity level. However, if the only available metrics are system-level ones (CPU, memory), a complete drop to zero is a more reliable indicator of process inactivity compared to a specific low threshold.

Setting a threshold on these system metrics might trigger alerts due to normal process behavior (e.g., the process might sleep occasionally, causing a temporary dip in CPU usage).

</details>

---

### Exam 4 · Q25

**How can you streamline the management effort required to transition from decomposing a monolithic application into microservices, especially when dealing with multiple instances that require read and write access to a configuration file stored on a shared file system, without necessitating the rewriting of the application code?**

- II. Opt for a new persistent disk, configuring it as a shared PersistentVolume to fulfill the shared file system requirement.
- IV. Introduce a new ConfigMap along with volumeMount to efficiently store and access the contents of the configuration file.
- III. Deploy a new Filestore instance and link the volume as an NFS PersistentVolume for seamless access to the configuration file.
- I. Utilize a Cloud Storage bucket, establishing it as a mounted resource within the container using FUSE.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Deploy a new Filestore instance and link the volume as an NFS PersistentVolume for seamless access to the configuration file.

**The recommended approach is:**

**III. Deploy a new Filestore instance and link the volume as an NFS PersistentVolume for seamless access to the configuration file.**

**Justification:**

  * **Shared File System:** Filestore offers a managed NFS service, creating a shared file system accessible by multiple container instances, perfectly suited for your scenario. (<https://cloud.google.com/filestore/docs/overview>)

  * **Performance and Scalability:** NFS offers better performance and can scale efficiently for multiple concurrent file accesses compared to FUSE-based workarounds on Cloud Storage. (<https://www.linuxtechi.com/configure-nfs-persistent-volume-kubernetes/>)

  * **No Code Changes:** This approach avoids the need to rewrite application code, minimizing the transition effort.

**Considerations:**

  * **Cost:** While convenient, Filestore can be more expensive than object storage solutions. Evaluate your budget and expected usage patterns.

  * **Management Overhead:** Introducing a new service like Filestore adds a small layer of additional management complexity.

**Why Other Options Are Less Ideal:**

  * **I. Utilize a Cloud Storage bucket, establishing it as a mounted resource within the container using FUSE.**

    * **Performance Limitations:** FUSE-based mounts on Cloud Storage can introduce performance overhead and latency, especially with frequent reads and writes compared to native file systems like NFS. (<https://cloud.google.com/storage/docs/gcs-fuse>)

  * **II. Opt for a new persistent disk, configuring it as a shared PersistentVolume to fulfill the shared file system requirement.**

    * **Complexity and Single Point of Failure:** Shared PersistentVolumes often involve complex setups like ReadWriteMany volumes in Kubernetes. Additionally, a single disk failure would impact all instances accessing the configuration file. (<https://www.shebanglabs.io/how-to-set-up-read-write-many-rwx-persistent-volumes-with-nfs-on-kubernetes/>)

  * **IV. Introduce a new ConfigMap along with volumeMount to efficiently store and access the contents of the configuration file.**

    * **Limited Use Case:** ConfigMaps are well-suited for storing configuration data within a Kubernetes cluster, but they are not designed for concurrent modification by multiple containers, which is a key requirement for your shared configuration file. (<https://kubernetes.io/docs/concepts/configuration/configmap/>)

</details>

---

### Exam 4 · Q29

**How can you ensure that your Google Kubernetes Engine (GKE) cluster optimizes performance and minimizes cost by automatically adjusting the number of pods and nodes based on CPU load fluctuations?**

- IV. Modify the MIG to enable Autoscaling to configure max and min amount of nodes based on CPU load, and configure the Vertical Pod Autoscaler (VPA) to scale workloads based on CPU load.
- I. Modify the managed instance group (MIG) to enable Autoscaling to configure max and min amount of nodes based on CPU load.
- II. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.
- III. Enable Cluster Autoscaler on the GKE cluster, and configure the HPA to autoscale the workloads based on a custom metric.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.

The best solution is

**II. Enable Cluster Autoscaler on the GKE cluster, and configure the Horizontal Pod Autoscaler (HPA) to autoscale the workload based on CPU load.**

**Explanation:**

  * **Cluster Autoscaler:** This is the essential component for scaling the number of nodes in a GKE cluster based on resource demands (<https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler>).

  * **Horizontal Pod Autoscaler (HPA):** The HPA works in tandem with Cluster Autoscaler. It scales the number of pods in your deployments based on CPU utilization metrics (<https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/>).

**Why other options are less ideal:**

  * **I. Modify the managed instance group (MIG) to enable Autoscaling to configure max and min amount of nodes based on CPU load.** While MIG autoscaling helps, it does not directly manage the scaling of pods within your Kubernetes deployments.

  * **III. Enable Cluster Autoscaler on the GKE cluster, and configure the HPA to autoscale the workloads based on a custom metric.** In most cases, CPU utilization is the ideal metric for horizontal pod scaling to match demand. Custom metrics might be needed in specific scenarios, but they introduce potential additional complexity.

  * **IV. Modify the MIG to enable Autoscaling to configure max and min amount of nodes based on CPU load, and configure the Vertical Pod Autoscaler (VPA) to scale workloads based on CPU load.** The VPA adjusts resource requests and limits for individual pods but doesn't directly increase or decrease the number of pods like the HPA.

</details>

---

### Exam 4 · Q30

**In order to deploy new features quickly while minimizing the risk of negatively impacting all users in a Cloud Run application with significant traffic volume, which approach should you choose?**

- I. Schedule weekly load tests against the production application.
- IV. Implement traffic splitting to have a smaller portion of users test out new features, gradually adjusting traffic splitting until all users receive the new features.
- II. Utilize the local development environment to perform load testing outside Google Cloud.
- III. Deploy new features as a new version, conduct smoke tests before allowing all users access, and then enable all users to access the new features.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Implement traffic splitting to have a smaller portion of users test out new features, gradually adjusting traffic splitting until all users receive the new features.

The best approach for your scenario is

**IV. Implement traffic splitting to have a smaller portion of users test out new features, gradually adjusting traffic splitting until all users receive the new features.**

Here's a breakdown of why this is superior and the limitations of the other choices:

**IV. Traffic Splitting:**

  * **Controlled Rollout:** Allows you to expose new features to a subset of users, minimizing the blast radius of potential issues.

  * **Monitoring and Feedback:** You can monitor real-world performance and gather feedback from the initial rollout before exposing all users.

  * **Gradual Increase:** Traffic splitting allows you to carefully increase the exposure of new features, making it easier to identify and address problems before they become widespread.

**Limitations of Other Approaches:**

  * **I. Schedule weekly load tests against the production application.** Load testing is important but doesn't fully simulate real-world user behavior and edge cases that might arise with new features.

  * **II. Utilize the local development environment to perform load testing outside of Google Cloud.** Local environments rarely match the production environment's scale and complexity, making testing less reliable.

  * **III. Deploy new features as a new version, conduct smoke tests before allowing all users access, and then enable all users to access the new features.** While smoke testing is valuable, it lacks the phased rollout and user feedback that traffic splitting provides.

**Traffic Splitting on Cloud Run**

Cloud Run natively supports traffic splitting, allowing you to precisely control the percentage of traffic directed to different revisions of your service (<https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration>).

</details>

---

### Exam 4 · Q37

**As a cluster administrator overseeing Google Kubernetes Engine (GKE), your organization's clusters are enrolled in a release channel. You require timely updates on pertinent events impacting your GKE clusters, including available upgrades and security bulletins. What is the recommended approach?**

- IV. Establish an RSS subscription to receive a daily summary of the GKE release notes.
- II. Schedule a query against the google_cloud_release_notes BigQuery dataset to retrieve relevant information.
- I. Set up cluster notifications to be dispatched to a Pub/Sub topic.
- III. Query the GKE API to ascertain available versions.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Set up cluster notifications to be dispatched to a Pub/Sub topic.

**Correct Option:**

**I. Set up cluster notifications to be dispatched to a Pub/Sub topic.**

**Justification:**

  * **Proactive Updates:** GKE cluster notifications pushed to a Pub/Sub topic provide real-time alerts for important events, including upgrade availability and security notices.

  * **Flexibility:** You can integrate Pub/Sub with various tools (e.g., email, Slack, webhooks) to tailor how you receive the critical notifications.

  * **Minimizes Manual Effort:** Avoids the need for manual queries or polling.

**Why Other Options Are Less Ideal:**

  * **II. Schedule a query against the google_cloud_release_notes BigQuery dataset...**

    * **Reactive:** Regularly querying BigQuery is still a manual approach. While you'll get release information, it's less timely than Pub/Sub notifications.

  * **III. Query the GKE API to ascertain available versions.**

    * **Focused Scope:** Only provides information on available versions, missing out on other important security notices.

  * **IV. Establish an RSS subscription to receive a daily summary...**

    * **Delayed:** Daily summaries may not be timely enough for critical security bulletins or essential upgrades.

**References:**

<https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications>

<https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels>

<https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications>

</details>

---

### Exam 4 · Q40

**Your application logs to Stackdriver, and you need to obtain the count of all requests made to endpoints starting with /api/alpha/. How can you achieve this?**

- IV. Export the logs to Cloud Pub/Sub and count the lines matching the pattern /api/alpha.
- I. Create a Stackdriver counter metric for the path /api/alpha/.
- II. Create a Stackdriver counter metric for the endpoint /api/alpha/*.
- III. Export the logs to Cloud Storage and count the lines matching the pattern /api/alpha.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Create a Stackdriver counter metric for the endpoint /api/alpha/*.

**The most suitable approaches:**

  * **II. Create a Stackdriver counter metric for the endpoint /api/alpha/*.** This is the most direct and efficient way. Steps involved:

    1. Go to Stackdriver Monitoring.

    2. Create a custom counter metric.

    3. Filter this metric with the HTTP request path `/api/alpha/*`

**Why the other options aren't the best fit:**

  * **I. Create a Stackdriver counter metric for the path /api/alpha/.** This is too specific. It won't count requests to sub-endpoints like `/api/alpha/resource1`.

  * **III. Export the logs to Cloud Storage and count the lines matching the pattern /api/alpha.** This method works, but it's less efficient for real-time monitoring:

Set up a logs export to Cloud Storage.

Filter logs for lines containing `/api/alpha/*`.

Use tools (like command-line tools or a script) to count the matching lines.

* **IV. Export the logs to Cloud Pub/Sub and count the lines matching the pattern /api/alpha.** This adds unnecessary complexity. Pub/Sub is good for real-time message distribution, but not optimized for log analysis and counting.

</details>

---

### Exam 4 · Q49

**In your Google Cloud project, you're defining system tests for an application hosted in Cloud Run. You need to establish a testing environment that's separate from the production environment. Your goal is to fully automate the creation of this testing environment with minimal effort and execute automated tests. What is the recommended approach?**

- I. Utilize Cloud Build to execute Terraform scripts, thereby creating a new Google Cloud project and deploying a Cloud Run instance of your application within it.
- III. Utilize Cloud Build to execute gcloud commands, facilitating the creation of a new Google Cloud project and deploying a Cloud Run instance of your application within it.
- II. Employ Cloud Build to execute a Terraform script, deploying a new Cloud Run revision within the existing Google Cloud project. Implement traffic splitting to direct traffic to your test environment.
- IV. Employ Cloud Build to execute gcloud commands, deploying a new Cloud Run revision within the existing Google Cloud project. Implement traffic splitting to direct traffic to your test environment.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Utilize Cloud Build to execute Terraform scripts, thereby creating a new Google Cloud project and deploying a Cloud Run instance of your application within it.

**Correct Option:**

  * **I. Utilize Cloud Build to execute Terraform scripts, thereby creating a new Google Cloud project and deploying a Cloud Run instance of your application within it.**

**Justification:**

  * **Isolation:** Creating a separate Google Cloud project establishes the strongest level of isolation, guaranteeing that production resources remain unaffected by your system tests.

  * **Automation:** Terraform enables infrastructure-as-code, allowing you to fully define your test environment's resources in a declarative way, ensuring consistency and easy replication.

  * **Cloud Build Integration:** Cloud Build seamlessly integrates with Terraform for executing your scripts, automating environment setup.

  * **Minimizing Production Impact:** Deploying your application in a separate project ensures your system tests won't affect your production environment's stability.

**Why Other Options Are Less Ideal:**

  * **II. Employ Cloud Build to execute a Terraform script, deploying a new Cloud Run revision...**

    * **Lack of Isolation:** Deploying a new revision within your production project still carries the risk of affecting the production environment if tests have unintended side effects.

  * **III. Utilize Cloud Build to execute gcloud commands...**

    * **Less Structured:** `gcloud` commands offer less declarative resource definition than Terraform, potentially making the test environment more difficult to replicate and prone to manual configuration errors.

  * **IV. Employ Cloud Build to execute gcloud commands, deploying a new Cloud Run revision...**

    * **Shares the challenges of options II and III, with less structured configuration and lesser isolation.**

**References:**

<https://cloud.google.com/docs/terraform/best-practices-for-terraform>

<https://cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code>

</details>

---

### Exam 4 · Q51

**What is the recommended method for deploying a microservice developed in C++ with custom software libraries for a Google Cloud-hosted application, ensuring minimal infrastructure management?**

- I. Utilize Cloud Functions for deploying the microservice.
- II. Employ Cloud Build for container creation and deployment on Cloud Run.
- III. Utilize Cloud Shell for containerizing the microservice and deploy it on a Container-Optimized OS Compute Engine instance.
- IV. Leverage Cloud Shell for containerization and deployment on standard Google Kubernetes Engine.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Employ Cloud Build for container creation and deployment on Cloud Run.

**II. Employ Cloud Build for container creation and deployment on Cloud Run.**

**Explanation:**

  * **Cloud Run** is a fully managed serverless platform perfect for deploying stateless containerized applications. It handles scaling and infrastructure management for you.

  * **Cloud Build** is a service to streamline building and deploying containers. This aligns well for creating the container image of your C++ microservice.

**Why Other Options are Less Suitable:**

  * **I. Utilize Cloud Functions for deploying the microservice.** Cloud Functions are best for short-lived, event-driven tasks rather than continuously running microservices.

  * **III. Utilize Cloud Shell for containerizing the microservice and deploy it on a Container-Optimized OS Compute Engine instance.** While viable, it introduces more manual infrastructure management than Cloud Run, which defeats the purpose of minimizing overhead.

  * **IV. Leverage Cloud Shell for containerization and deployment on standard Google Kubernetes Engine.** Kubernetes is powerful but brings complexity. For a single microservice with minimal management preference, Cloud Run is simpler.

</details>

---

### Exam 4 · Q57

**For an application deployed on Google Kubernetes Engine (GKE), how should you set up alerts to be notified when the average memory consumption of containers dips below 20% or exceeds 80%?**

- III. Create a scheduled Cloud Function to execute 'kubectl top' on all cluster workloads and send an email alert if the average memory consumption falls outside the specified bounds.
- IV. Design a script to gather memory consumption at the OS level and send an email alert if the average memory usage crosses the defined threshold.
- I. Develop a Cloud Function leveraging the Monitoring API. Schedule it to run hourly and alert you if the average memory consumption strays from the specified range.
- II. Within Cloud Monitoring, establish an alerting policy to notify you of any deviations in average memory consumption from the designated range.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Within Cloud Monitoring, establish an alerting policy to notify you of any deviations in average memory consumption from the designated range.

**The most suitable option:**

**II. Within Cloud Monitoring, establish an alerting policy to notify you of any deviations in average memory consumption from the designated range.**

**Explanation:**

  * **Native Integration:** Cloud Monitoring is tightly integrated with GKE, and designed specifically for metric-based alerting.

  * **Efficiency:** You avoid the overhead of custom code and don't need to reinvent the wheel. Cloud Monitoring does the tracking and alerting for you.

  * **Customization:** Alerting policies offer flexibility in notification channels and escalation configurations.

**Why Other Options Are Less Ideal:**

  * **I. Develop a Cloud Function leveraging the Monitoring API. Schedule it to run hourly and alert you if the average memory consumption strays from the specified range.** This is workable, but more complex than necessary. It introduces custom code and scheduling that Cloud Monitoring already handles.

  * **III. Create a scheduled Cloud Function to execute 'kubectl top' on all cluster workloads and send an email alert if the average memory consumption falls outside the specified bounds.** `kubectl top` is useful for spot checks, but not ideal for continuous monitoring. It's also less scalable than Cloud Monitoring's metrics collection.

  * **IV. Design a script to gather memory consumption at the OS level and send an email alert if the average memory usage crosses the defined threshold.** This approach focuses on OS-level metrics rather than container-level metrics, which are more relevant for GKE. It also adds the overhead of script development and management.

Reference:

<https://cloud.google.com/monitoring>

</details>

---

### Exam 4 · Q58

You’ve deployed an application to Google Kubernetes Engine (GKE) where the Pods write data to a Compute Engine persistent disk. You’ve already created the PersistentVolume (PV) and PersistentVolumeClaim (PVC) objects and referenced the PVC in your Deployment manifest.

After expanding the persistent disk due to nearing full capacity, you log into one of the running Pods and notice that the increased disk space isn’t reflected inside the container’s file system.  
**What should you do to make the additional space available to the Pods?**

- C. Modify the `spec.resources.requests.storage` field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using `kubectl`.
- D. Use a tool like `fdisk` or `parted` inside the Pod to manually resize the partition to utilize the full disk.
- B. Restart the application by deleting and reapplying the Deployment using the commands:  
  `kubectl delete deployment DEPLOYMENT_NAME && kubectl apply -f deployment.yaml`.
- A. Update the `spec.capacity.storage` field in the PersistentVolume (PV) configuration to reflect the new disk size, then apply the changes using `kubectl`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Modify the `spec.resources.requests.storage` field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using `kubectl`.

The correct answer is:  
**C. Modify the spec.resources.requests.storage field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using kubectl.**

✅ **Explanation of the Correct Option:**

✅ Option C:

**"Modify the spec.resources.requests.storage field in the PersistentVolumeClaim (PVC) to match the new disk size and apply the change using kubectl."**

When you **resize a Compute Engine persistent disk** , GKE does **not automatically expand the file system inside the Pods**. To propagate the change, you must also update the associated **PersistentVolumeClaim (PVC)** with the new desired size.

  * Kubernetes supports **expanding PVCs** if the underlying StorageClass allows volume expansion (`allowVolumeExpansion: true`).

  * After expanding the PVC, **GKE will automatically resize the file system** when the Pod is restarted or rescheduled.

**Official Documentation:**

  * <https://cloud.google.com/kubernetes-engine/docs/concepts/storage-overview>

  * <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes>

❌ **Why Other Options Are Incorrect:**

❌ Option A:

**"Update the spec.capacity.storage field in the PersistentVolume (PV) configuration to reflect the new disk size."**

  * You **should never manually edit the PV object** to reflect storage changes.

  * PVs are usually **bound to PVCs** , and their capacity is **automatically managed** by Kubernetes based on the associated PVC.

  * Editing the PV directly can cause inconsistencies and is **not the supported method** for resizing volumes.

**Reference:**  
<https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolume>

❌ Option B:

**"Restart the application by deleting and reapplying the Deployment."**

  * Restarting the Deployment **does not trigger PVC resizing**.

  * If the PVC’s `requests.storage` field hasn't been updated, **the file system inside the Pod remains at the original size**.

❌ Option D:

**"Use a tool like fdisk or parted inside the Pod to manually resize the partition."**

  * This is **not recommended or supported** in GKE.

  * Kubernetes abstracts storage management, and manual partition changes **can lead to data corruption or unsupported states**.

✅ Summary:

To reflect the increased disk size in the Pod’s file system, update the **PVC’s storage request**.

📌 **Correct Action:**  
Edit the PVC and run: kubectl edit pvc YOUR_PVC_NAME

Then update:

spec:

resources:

requests:

storage: 100Gi # Update to new size

Kubernetes will handle the rest, especially if the StorageClass has `allowVolumeExpansion: true`.

</details>

---

### Exam 5 · Q5

**Your team is utilizing Cloud Build to facilitate the promotion of a Node.js application deployed on App Engine from the staging environment to production. The application relies on several directories of photos stored in a Cloud Storage bucket named `webphotos-staging` in the staging environment. Post-promotion, these photos need to be accessible in a Cloud Storage bucket named `webphotos-prod` in the production environment. You aim to automate this process where feasible. What action should you take?**

- A. Perform a manual copy of the photos to `webphotos-prod`.
- C. Insert a build step in the `cloudbuild.yaml` file before the promotion step with the arguments:
    name: gcr.io/cloud-builders/gsutil
    args: ['cp', '-r', 'gs://webphotos-staging', 'gs://webphotos-prod']
    waitFor: ['-']
- B. Introduce a startup script in the application's `app.yaml` file to transfer the photos from `webphotos-staging` to `webphotos-prod`.
- D. Include a build step in the `cloudbuild.yaml` file before the promotion step with the arguments:
    name: 'gcr.io/cloud-builders/gsutil'
    args: ['cp', '-a', 'gs://webphotos-staging', 'gs://webphotos-prod']
    waitFor: ['-']

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Insert a build step in the `cloudbuild.yaml` file before the promotion step with the arguments:

**Correct Answer:**

  * **C. Insert a build step in the**`**cloudbuild.yaml**`**file before the promotion step with the arguments:...**

1.  name: gcr.io/cloud-builders/gsutil
      2. args: ['cp', '-r', 'gs://webphotos-staging', 'gs://webphotos-prod']
      3. waitFor: ['-']

**Justification:**

  * **Automation within the Build Pipeline:** Integrating the photo transfer into your Cloud Build pipeline ensures it happens automatically during the promotion process. This aligns with the goal of automating where feasible.

  * **The 'gsutil' Cloud Builder:** The `gcr.io/cloud-builders/gsutil` image provides tools for efficient Cloud Storage operations.

  * **Recursive Copy (**`**-r**`**):** Ensures all photos and subdirectories within `webphotos-staging` are copied.

  * `**waitFor: ['-']**`**:** Prevents subsequent build steps from running until the copy operation successfully completes.

**Incorrect Answers:**

  * **A. Perform a manual copy of the photos to**`**webphotos-prod**`**.**

    * **Reasoning:** This breaks the desired automation and introduces the potential for errors or missed steps in the promotion process.

  * **B. Introduce a startup script in the application's**`**app.yaml**`**file...**

    * **Reasoning:** While possible, this mixes concerns. Deployment and data transfer are better separated; keeping the transfer in Cloud Build makes the process more independent and reusable.

  * **D. Include a build step... `args: ['cp', '-a', 'gs://webphotos-staging', 'gs://webphotos-prod']...**

    * **Reasoning:** The `-a` flag (archive mode) is usually for preserving file attributes. While it would work, the simpler `-r` (recursive) flag is more direct for this use case.

</details>

---

### Exam 5 · Q8

**You're attempting to utilize kubectl from Cloud Shell to connect to your Google Kubernetes Engine (GKE) cluster. After deploying the GKE cluster with a public endpoint, you execute the following command from Cloud Shell:**

**```**

**gcloud container clusters get-credentials <cluster-name> \**

**\--zone <zone> \--project <project-name>**

**```**

**However, you observe that the kubectl commands are timing out without providing any error message. What is the most probable cause of this issue?**

- A. Your user account lacks the necessary privileges to interact with the cluster using kubectl.
- D. A VPC firewall is obstructing access to the cluster's endpoint.
- C. Cloud Shell is not part of the same VPC as the GKE cluster.
- B. The Cloud Shell's external IP address is not included in the authorized networks of the cluster.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. The Cloud Shell's external IP address is not included in the authorized networks of the cluster.

**Correct Answer:**

  * **B. The Cloud Shell's external IP address is not included in the authorized networks of the cluster.**

**Justification:**

  * **Authorized Networks for Public Clusters:** Even though your GKE cluster has a public endpoint, by default, access is restricted to a set of authorized IP addresses. Cloud Shell has a dynamic, ephemeral IP address that changes, making it likely it's not included in the allowed list. (GCP Documentation: [invalid URL removed])

  * **Timeout Behavior:** The lack of an explicit error message and a timeout is consistent with traffic simply being blocked without rejection at the network level.

**Incorrect Answers:**

  * **A. Your user account lacks the necessary privileges...**

    * **Reasoning:** If this were the case, the `gcloud container clusters get-credentials` command itself would have likely failed with a permission-related error.

  * **C. Cloud Shell is not part of the same VPC as the GKE cluster.**

    * **Reasoning:** While VPC network boundaries _can_ affect connectivity, a public endpoint with proper authorization should be accessible even if Cloud Shell is in a different VPC.

  * **D. A VPC firewall is obstructing access to the cluster's endpoint**

    * **Reasoning:** While possible, VPC firewalls would usually result in a more explicit connection failure rather than a silent timeout.

</details>

---

### Exam 5 · Q10

**You oversee an application governed by a managed instance group. In the event of deploying a new version of the application, your objective is to minimize costs and maintain a consistent number of instances. It's imperative that each new instance created during deployment is deemed healthy before the deployment proceeds.**

**Which approach should you employ to achieve this?**

- III. Implement a rolling-action with a limit on the maximum number of healthy instances set to 1, and the maximum number of unhealthy instances set to 0.
- I. Execute a rolling-action with a maximum surge set to 1 and maximum unavailable instances set to 0.
- II. Conduct a rolling-action with a maximum surge set to 0 and a maximum number of instances deemed unavailable set to 1.
- IV. Engage in a rolling-action with a restriction on the maximum number of healthy instances set to 0, and the maximum number of unhealthy instances set to 1.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Conduct a rolling-action with a maximum surge set to 0 and a maximum number of instances deemed unavailable set to 1.

**The correct option for this scenario is:**

**II. Conduct a rolling-action with a maximum surge set to 0 and a maximum number of instances deemed unavailable set to 1.**

**Justification:** In this scenario, the objective is to minimize costs and maintain a consistent number of instances while ensuring that each new instance created during deployment is considered healthy before the deployment proceeds. Using a rolling update strategy with a maximum surge set to 0 ensures that no additional instances are created beyond the current capacity, thereby helping to minimize costs. Setting the maximum number of instances deemed unavailable to 1 ensures that only one instance can be considered unhealthy at any given time during the deployment process, maintaining consistency and reducing the risk of service disruption.

**Why the other options are not suitable:**

I. Executing a rolling-action with a maximum surge set to 1 and maximum unavailable instances set to 0: This option allows for one additional instance (surge) to be created during the deployment process, which may not align with the objective of minimizing costs and maintaining a consistent number of instances. Additionally, setting the maximum unavailable instances to 0 does not provide flexibility in handling instances that may temporarily become unhealthy during the deployment.

III. Implementing a rolling-action with a limit on the maximum number of healthy instances set to 1, and the maximum number of unhealthy instances set to 0: This option restricts the number of healthy instances to 1, which may not be desirable as it limits the deployment process and may lead to service disruption if the existing healthy instance experiences issues during deployment. It's also not optimal for maintaining consistency in the number of instances.

IV. Engaging in a rolling-action with a restriction on the maximum number of healthy instances set to 0, and the maximum number of unhealthy instances set to 1: Similarly to option III, this approach imposes unnecessary constraints on the deployment process and may increase the risk of service disruption by disallowing any healthy instances during deployment.

**Documentation Link:** You can find more information about managing instance groups and rolling updates in the official documentation here: [Rolling out updates](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)

</details>

---

### Exam 5 · Q11

**You are creating a public-facing web application on Cloud Run, making it accessible through its public IP address. To test its ability to handle high traffic, you conduct a load test. While the app works fine under light traffic, you observe slower responses and error messages when the load is high. What is the best way to investigate and resolve this performance issue?**

- D. Verify if your Cloud Run service has reached the set maximum instances. If so, increase the maximum instance count to allow for more scaling during high demand.
- A. Review the network traffic to your Cloud Run service using Cloud Monitoring to confirm if there's a spike in demand. If needed, use traffic splitting on the Cloud Run service to redirect some requests to a previous revision.
- B. Check the minimum instances setting for your Cloud Run service. If required, increase the minimum number of instances to align with the maximum virtual users in your load test.
- C. Investigate if Cloud Armor is detecting and blocking potential DDoS attacks before traffic reaches your Cloud Run service. Disable any Cloud Armor policies if they are restricting legitimate traffic.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Verify if your Cloud Run service has reached the set maximum instances. If so, increase the maximum instance count to allow for more scaling during high demand.

The correct answer is 

**D. Verify if your Cloud Run service has reached the set maximum instances. If so, increase the maximum instance count to allow for more scaling during high demand.**

Explanation:

In **Cloud Run** , the maximum instances setting controls the upper limit for concurrent instances that can be started in response to incoming traffic. If your application is experiencing slower responses and errors under high load, it is likely that the maximum instance limit has been reached, preventing Cloud Run from scaling further to handle the increased demand. By increasing the **maximum instance count** , you allow Cloud Run to start more instances, which can handle additional traffic and improve performance during peak loads.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Monitoring and traffic splitting**  
While Cloud Monitoring can help monitor traffic spikes, **traffic splitting** is not relevant for handling high demand. Splitting traffic to a previous revision would not improve scalability or performance under load.

  * **Option B: Check the minimum instances setting**  
The **minimum instances setting** determines the baseline number of instances to keep warm, which helps reduce cold start latency but does not impact the ability to scale up. Increasing this setting would result in unnecessary costs without improving the maximum scaling capacity.

  * **Option C: Investigate Cloud Armor for DDoS blocking**  
Cloud Armor provides protection against DDoS attacks, but it is unlikely that it is blocking legitimate traffic without specific configurations. Disabling Cloud Armor would not address performance issues caused by scaling limits in Cloud Run.

</details>

---

### Exam 5 · Q13

**Your team oversees a Google Kubernetes Engine (GKE) cluster hosting an application. Another team intends to integrate with this application. Before commencing the integration, you must ensure that the other team cannot modify your application but can deploy their integration on GKE. What is the appropriate action to take?**

- I. Grant the Viewer IAM role on the cluster project to the other team using Identity and Access Management (IAM).
- II. Create a new GKE cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).
- IV. Create a new namespace within the existing cluster and grant the Admin role on the new namespace to the other team using Kubernetes role-based access control (RBAC).
- III. Establish a new namespace within the existing cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Create a new namespace within the existing cluster and grant the Admin role on the new namespace to the other team using Kubernetes role-based access control (RBAC).

**IV. Create a new namespace within the existing cluster and grant the Admin role on the new namespace to the other team using Kubernetes role-based access control (RBAC).**

Here's why this is the best approach:

  * **Resource Isolation:** Namespaces provide logical separation within a GKE cluster, ensuring the other team's work doesn't interfere with your application's resources.

  * **Principle of Least Privilege:** Granting the Admin role within the namespace gives the other team the necessary permissions to deploy and manage their integration, but limits their access to only that namespace.

  * **Separation of Concerns:** This approach maintains clear ownership boundaries between your application and the other team's integration.

**Why other options are less suitable:**

  * **I. Grant the Viewer IAM role on the cluster project to the other team using Identity and Access Management (IAM).** The Viewer role is too restrictive, preventing the other team from deploying their integration components.

  * **II. Create a new GKE cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).** A separate cluster adds unnecessary management overhead and may increase costs.

  * **III. Establish a new namespace within the existing cluster and grant the Editor role on the cluster project to the other team using Identity and Access Management (IAM).** Cluster-wide Editor permissions are too broad and could allow the other team to interfere with resources outside their designated namespace.

**References:**  
[https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control  https://cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac   https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)

[https://cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control  https://cloud.google.com/kubernetes-engine/docs/concepts/access-control#rbac   https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)

</details>

---

### Exam 5 · Q18

**As part of your workflow utilizing Cloud Build, you're tasked with promoting a Docker image across Development, Test, and Production environments. It's imperative to ensure consistency by deploying the same Docker image to each environment.**

**How should you designate the Docker image within your build?**

- III. Utilize the digest of the Docker image for precise identification.
- II. Employ a unique Docker image name for differentiation.
- IV. Utilize a semantic version Docker image tag for version control.
- I. Employ the latest Docker image tag for identification.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Utilize the digest of the Docker image for precise identification.

**Correct Choice:**

  * **III. Utilize the digest of the Docker image for precise identification.**

**Explanation:**

  * **Immutability:** A Docker image digest is a unique, content-based hash (e.g., sha256:abcd1234...). This guarantees that if you reference a specific digest, you are always referring to the exact, unchanging image contents. This is crucial for ensuring the same image gets deployed across environments.

**Why Other Options Can Be Problematic:**

  * **I. Employ the latest Docker image tag for identification.**

    * **Ambiguity:** The "latest" tag is mutable, meaning it could be reassigned to a different image over time. This introduces uncertainty and undermines reliable promotion across environments.

  * **II. Employ a unique Docker image name for differentiation.**

    * **Insufficent Specificity:** While unique names can help, they don't ensure content hasn't changed. Developers could rebuild an image with the same name but with different contents.

  * **IV. Utilize a semantic version Docker image tag for version control.**

    * **Potential for Human Error:** Semantic versioning (e.g., 1.0.2) is useful for tracking changes. However, a developer could accidentally increment a minor version without intending major changes, leading to unexpected inconsistencies.

**Reference:**  
<https://cloud.google.com/architecture/using-container-images>

</details>

---

### Exam 5 · Q20

**You're preparing to deploy your application in a Google Kubernetes Engine (GKE) cluster. The application offers an HTTP-based health check accessible at /healthz. You aim to utilize this health check endpoint for determining whether traffic should be directed to the pod by the load balancer. Which code snippet should you include in your Pod configuration?**

- D.
      
            1. healthCheck:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80
- A.
      
            1. livenessProbe:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80
- C.
      
            1. loadbalancerHealthCheck:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80
- B.
      
            1. readinessProbe:
        2.   httpGet:
        3.     path: /healthz
        4.     port: 80

<details><summary>Answer &amp; explanation</summary>

**Correct:** B.

**Correct Answer**

  * **B. readinessProbe: httpGet: path: /healthz port: 80**

**Justification:**

  * **Readiness Probes:** In Kubernetes, readiness probes tell the system when a container is ready to start receiving traffic from a service. A pod only becomes part of a service's endpoints when its readiness probe succeeds. (Kubernetes Documentation: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>)

  * **HTTP Health Checks:** The `httpGet` probe type is used to perform HTTP GET requests on a configured path and port. A successful response indicates the container is healthy. (Kubernetes Documentation: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>)

**Incorrect Answers**

  * **A. livenessProbe: httpGet: path: /healthz port: 80**

    * **Reasoning:** Liveness probes determine if a container is still running and should be restarted if not. While important, liveness probes don't directly handle traffic routing.

  * **C. loadbalancerHealthCheck: httpGet: path: /healthz port: 80**

    * **Reasoning:** There's no concept of a `loadBalancerHealthCheck` in Kubernetes pod specifications. Health checks are defined using readiness and liveness probes.

  * **D. healthCheck: httpGet: path: /healthz port: 80**

    * **Reasoning:** The `healthCheck` field is too generic; Kubernetes needs a specific probe type (`readinessProbe` or `livenessProbe`) to function correctly.

</details>

---

### Exam 5 · Q25

**You are employed by a company managing an ecommerce platform. Your task involves testing a new product recommendation algorithm through A/B testing to assess its impact on sales in a randomized manner. What is the recommended approach for testing this feature?**

- IV. Utilize HTTP header-based routing.
- I. Distribute traffic between versions using weights.
- III. Mirror traffic to the new version of your application.
- II. Activate the new recommendation feature flag on a single instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Distribute traffic between versions using weights.

**The recommended approach for testing a new product recommendation algorithm through A/B testing to assess its impact on sales in a randomized manner is:**

**I. Distribute traffic between versions using weights.**

**Explanation:**

  * **A/B testing involves splitting traffic between different versions of the application to compare their performance.**

  * **By distributing traffic between versions using weights, you can control the proportion of users exposed to each version. For example, you might allocate 50% of the traffic to the current version and 50% to the version with the new recommendation algorithm.**

  * **This approach allows for a randomized and controlled comparison between the two versions, enabling you to measure the impact of the new recommendation algorithm on sales in a statistically valid manner.**

The other options can be explained as follows:

II. Activating the new recommendation feature flag on a single instance (Option II) would not provide a randomized comparison between different versions. It also does not allow for statistical analysis of the impact on sales across a diverse user base.

III. Mirroring traffic to the new version of your application (Option III) involves sending a copy of traffic to the new version without impacting the primary traffic flow. While this approach can be useful for testing in a non-disruptive manner, it does not inherently provide a randomized comparison between different versions.

IV. Utilizing HTTP header-based routing (Option IV) can be a part of the implementation for directing traffic to different versions of the application, but it alone does not ensure randomized distribution or controlled comparison between versions. It's more about routing traffic based on specific conditions rather than conducting A/B testing.

**References:**  
[https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments](https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments  https://cloud.google.com/load-balancing/docs/https/traffic-management-global)

[https://cloud.google.com/load-balancing/docs/](https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments  https://cloud.google.com/load-balancing/docs/https/traffic-management-global)

[https/traffic-management-global](https://cloud.google.com/traffic-director/docs/advanced-traffic-management#weight-based_traffic_splitting_for_safer_deployments  https://cloud.google.com/load-balancing/docs/https/traffic-management-global)

</details>

---

### Exam 5 · Q27

**While creating a Google Kubernetes Engine (GKE) cluster using the command `gcloud container clusters create large-cluster --num-nodes 200`, you encounter an error:**

**insufficient regional quota to satisfy request: resource "CPUS": request requires '200.0' and is short '176.0'. project has a quota of '24.0' with '24.0' available**

**To resolve this issue, what should you do?**

- D. Modify services in the cluster to function with fewer cores, and rewrite new clusters accordingly.
- C. Raise a support case to request additional GKE quota.
- B. Increase the Compute Engine quota in the GCP Console.
- A. Increase the GKE quota in the GCP Console.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Increase the Compute Engine quota in the GCP Console.

**Correct Answer:**

  * **B. Increase the Compute Engine quota in the GCP Console.**

**Justification:**

  * **Quota Limits:** Google Kubernetes Engine (GKE) clusters fundamentally consist of Compute Engine virtual machines (nodes). The "CPUs" quota directly corresponds to the number of virtual CPUs available to your project in the region you're attempting to create the cluster (GCP Documentation: <https://cloud.google.com/compute/quotas>).

**Incorrect Answers:**

  * **A. Increase the GKE quota in the GCP Console.**

    * **Reasoning:** While some regions have specific GKE quotas, the error message indicates a CPU limitation. Often, increasing the underlying Compute Engine quota automatically adjusts the connected GKE quota (if one exists).

  * **C. Raise a support case to request additional GKE quota.**

    * **Reasoning:** While support could eventually help, it's usually faster to directly increase the Compute Engine CPU quota yourself (if your project permissions allow it).

  * **D. Modify services in the cluster to function with fewer cores...**

    * **Reasoning:** Resource optimization is good practice, but it doesn't address the core problem - the project-level limitation on the number of CPUs you can use in the region.

</details>

---

### Exam 5 · Q28

**Your application is deployed across multiple Google Kubernetes Engine clusters, each managed by a Deployment. Within each cluster, the Deployment has spawned multiple replicas of your Pod. Your aim is to inspect the logs transmitted to stdout for all replicas within your Deployment across all clusters. Which command should you employ?**

- III. Run `**kubectl exec -it [PARAM] journalctl**`.
- I. Execute `**kubectl logs [PARAM]**`.
- IV. Access logs via `**gcloud compute ssh [PARAM] --command="sudo journalctl"**`.
- II. Utilize `**gcloud logging read [PARAM]**`.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Utilize `**gcloud logging read [PARAM]**`.

**Best Approach (assuming centralized logging):**

  * **II. Utilize gcloud logging read [PARAM]**

    * **Explanation:** Centralized logging offers the ability to aggregate logs from all your clusters and pods, and `gcloud logging read` lets you access and filter these logs effectively.

    * **Documentation:** <https://cloud.google.com/logging/docs/reference/tools/gcloud-logging>

**If centralized logging is NOT set up:**

In the absence of a centralized logging solution, the task becomes more cumbersome. You _could_ technically achieve the goal with a combination of the following, but it's less than ideal:

  * **I. Execute kubectl logs [PARAM].**

    * **Explanation:** You'd need to iterate through each cluster, retrieve a list of Pods within your Deployment, and then run `kubectl logs` against each Pod individually.

    * **Documentation:** <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/>

**Why the other options are NEVER suitable**

  * **III. Run kubectl exec -it [PARAM] journalctl.**

    * **Incorrect:** `journalctl` provides system-level logs, not necessarily the application logs sent to stdout.

  * **IV. Access logs via gcloud compute ssh [PARAM] --command="sudo journalctl".**

    * **Incorrect and Inefficient:** Same limitations as option III, and it introduces the unnecessary overhead of SSH-ing into each node of your clusters.

</details>

---

### Exam 5 · Q29

**Your production application runs on Compute Engine virtual machine instances managed by a managed instance group, with traffic directed through an HTTP(s) load balancer. Despite this setup, users are currently unable to access the application. Your goal is to establish a monitoring mechanism to alert you when the application becomes inaccessible.**

**Which method should you select?**

- I. Functional tests
- III. Cloud Load Balancing - health probes
- IV. Managed instance group - health evaluations
- II. Stackdriver availability checks

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Stackdriver availability checks

The correct option for this scenario is:

**II. Stackdriver availability checks**

**Justification:** Stackdriver availability checks allow you to monitor the availability of your application from various locations globally. By configuring Stackdriver availability checks, you can receive alerts when your application becomes inaccessible, ensuring you're promptly notified of any issues affecting user access. This method directly addresses the goal of establishing a monitoring mechanism to detect when the application becomes inaccessible.

**Why the other options are not suitable:**

I. Functional tests: Functional tests typically involve testing specific functionalities or workflows within your application. While functional tests are valuable for ensuring the correctness of your application's behavior, they may not directly address the need to monitor the overall accessibility of your application from an external perspective.

III. Cloud Load Balancing - health probes: Cloud Load Balancing health probes monitor the health of backend instances within a load balancer's target pool. While health probes are essential for load balancer management and ensuring traffic is directed only to healthy instances, they may not directly alert you when the application as a whole becomes inaccessible from an external perspective.

IV. Managed instance group - health evaluations: Managed instance group health evaluations assess the health of individual instances within the group. While it's crucial to monitor the health of your instances, especially in a managed instance group scenario, this method may not provide direct alerts about the overall accessibility of your application from an external perspective.

</details>

---

### Exam 5 · Q31

**In maintaining a .NET legacy application, your aim is to ensure consistent results during the CI/CD pipeline while minimizing deployment costs and mitigating external factors and dependencies between hosting environments, as containers are not yet sanctioned in your organization. What should be your approach?**

- III. Deploy the application utilizing MS Web Deploy, ensuring utilization of the latest, patched MS Windows Server base image in Compute Engine.
- I. Rewrite the application utilizing .NET Core and deploy it to Cloud Run, employing revisions for environment separation.
- IV. Utilize Cloud Build to package the application and deploy it to a Google Kubernetes Engine cluster, utilizing namespaces for environment separation.
- II. Utilize Cloud Build to deploy the application as a new Compute Engine image for each build, utilizing the same image across all environments.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Utilize Cloud Build to deploy the application as a new Compute Engine image for each build, utilizing the same image across all environments.

**Best Choice:**

  * **II. Utilize Cloud Build to deploy the application as a new Compute Engine image for each build, utilizing the same image across all environments.**

**Explanation:**

  * **Consistency:** Creating a golden image with the application pre-installed and baking it into each environment ensures maximal consistency and minimizes external dependencies.

  * **CI/CD Integration:** Cloud Build simplifies image creation and management with automation.

  * **Cost Considerations:** While not as cost-efficient as containers, Compute Engine instances allow better control over costs compared to always-on Kubernetes nodes.

**Why Other Options Are Unsuitableable:**

  * **I. Rewrite the application utilizing .NET Core and deploy it to Cloud Run...**

    * **Major Rewrite:** Rewriting a legacy .NET application for .NET Core could be a significant undertaking that violates your current constraints.

  * **III. Deploy the application utilizing MS Web Deploy...**

    * **Image Management:** Web Deploy is good for quick updates, but doesn't address the image consistency issue for full deployments across environments.

  * **IV. Utilize Cloud Build to package the application and deploy it to a Google Kubernetes Engine cluster...**

    * **Container Requirement:** You explicitly stated that containers are not currently an option in your organization.

**References:**  
[https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine](https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud)

[https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud](https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud)

[https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud](https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#take_advantage_of_compute_engine  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud#phase_1_rehost_in_the_cloud  https://cloud.google.com/architecture/modernization-path-dotnet-applications-google-cloud)

</details>

---

### Exam 5 · Q32

**You're developing a new application with specific design requirements:**

**Ensure versioning and auditability of the application infrastructure changes.**

**Optimize the use of Google-managed services for both the application and deployment infrastructure.**

**Utilize a serverless compute platform for the application.**

**Which architecture design should you choose?**

- I.
    I. Maintain the application and infrastructure source code in a Git repository.
    II. Utilize Cloud Build to deploy the application infrastructure using Terraform.
    III. Deploy the application to Cloud Functions within a pipeline step.
- IV.
    I. Deploy the application infrastructure using gcloud commands.
    II. Define a continuous integration pipeline for application source code changes using Cloud Build.
    III. Implement a pipeline step to fetch the application source code from a Git repository, containerize it.
    IV. Deploy the new container on Cloud Run within the pipeline.
- II.
    I. Deploy Jenkins from the Google Cloud Marketplace and establish a continuous integration pipeline.
    II. Configure a pipeline step in Jenkins to fetch the application source code from a Git repository.
    III. Deploy the application source code to App Engine within the pipeline.
- III.
    I. Set up a continuous integration pipeline on Cloud Build and deploy the application infrastructure using Deployment Manager templates.
    II. Implement a pipeline step to create a container with the latest application source code.
    III. Deploy the container to a Compute Engine instance within the pipeline.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I.

**Best Choice:**

  * **I. Maintain the application and infrastructure source code in a Git repository. Utilize Cloud Build to deploy the application infrastructure using Terraform. Deploy the application to Cloud Functions within a pipeline step.**

**Explanation:**

  * **Versioning & Auditability:** Git provides inherent versioning and change tracking for both application code and Infrastructure as Code (IaC) defined in Terraform.

  * **Google-Managed Services:** Cloud Build and Cloud Functions are fully-managed, easing operational burden. Terraform has excellent integration with GCP.

  * **Serverless Alignment:** Cloud Functions is the ideal serverless compute choice for the application tier.

**Why Other Options Are Less Ideal:**

  * **II. Deploy Jenkins ... Deploy the application to App Engine ...**

    * **Operational Overhead:** Jenkins introduces self-management of a VM compared to Cloud Build. App Engine is also less serverless than Cloud Functions.

  * **III. Set up a continuous integration pipeline on Cloud Build ... Deploy the container to a Compute Engine instance ...**

    * **Serverless Mismatch:** While valid for some use cases, deploying a container to a Compute Engine instance misses out on the benefits of serverless compute.

  * **IV. Deploy the application infrastructure using gcloud commands ... Deploy the new container on Cloud Run ...**

    * **Manual Infrastructure:** `gcloud` commands lack the versioning and automation features of IaC tools like Terraform.

**Reference:**

<https://cloud.google.com/docs/ci-cd/products#featured-products-for-cicd>

</details>

---

### Exam 5 · Q33

**You’re setting up a container build pipeline for an application hosted on GKE. The requirements are:**

  * **Only images created by your build pipeline should be deployed on the GKE cluster.**

  * **All code and build artifacts must stay within your environment and be protected from data exfiltration.**

**How should you design the pipeline?**

- D. Use Cloud Build with the default worker pool to create the build pipeline.
    Configure the pipeline to build container images and store them in Artifact Registry.
    Configure the GKE cluster to accept only container images signed by Binary Authorization.
- A. Use Cloud Build with the default worker pool to create the build pipeline.
    Deploy container images to a private container registry in your VPC.
    Create a VPC firewall policy that denies all egress and ingress traffic to public networks.
- B. Use Cloud Build with a private worker pool to create the build pipeline.
    Use VPC Service Controls to include all CI/CD components and services within a security perimeter.
    Configure the GKE cluster to accept only container images signed by Binary Authorization.
- C. Use Cloud Build with a private worker pool to create the build pipeline.
    Configure the pipeline to build container images and store them in Artifact Registry.
    Set up Artifact Registry to use customer-managed encryption keys (CMEK) to encrypt container images.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Use Cloud Build with a private worker pool to create the build pipeline.

The correct answer is **B**.

Explanation:

To meet the requirements of ensuring that only images created by the build pipeline are deployed on the GKE cluster and to protect code and artifacts from data exfiltration, you should:

  1. **Use Cloud Build with a private worker pool** : This ensures that the build process remains within your private network, isolating it from the public internet and providing additional security for code and build artifacts.

  2. **Use VPC Service Controls** : By configuring a security perimeter around your CI/CD components and services, including Cloud Build, GKE, and Artifact Registry, VPC Service Controls help prevent data exfiltration and enforce strict boundary protection for sensitive data.

  3. **Configure Binary Authorization on GKE** : Binary Authorization allows you to enforce policies that only permit images with the required attestations (e.g., signed images from your build pipeline) to be deployed to the GKE cluster, ensuring that only verified images are used.

Justifications for Incorrect Options:

  * **Option A** : Using the default worker pool in Cloud Build does not provide isolation from the public internet. VPC firewall policies alone do not offer the same level of data exfiltration protection as VPC Service Controls.

  * **Option C** : Although using a private worker pool and customer-managed encryption keys (CMEK) provides some security, it does not fully address the need to prevent data exfiltration without VPC Service Controls. CMEK encrypts stored data but does not provide the comprehensive perimeter protection that VPC Service Controls offer.

  * **Option D** : Using the default worker pool exposes the build pipeline to the public internet, and while Binary Authorization helps secure deployments, it does not address data exfiltration concerns without a private worker pool and VPC Service Controls.

**Relevant Documentation:**

For more information, refer to:

  * [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/overview)

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

</details>

---

### Exam 5 · Q36

**You are pushing container images to Artifact Registry and deploying a containerized microservices application on GKE. After deployment, you notice unexpected behavior in the services. Upon inspecting the Pods with kubectl get pods, you see that one Pod is in a CrashLoopBackoff state. How should you troubleshoot this Pod?**

- C. Use kubectl logs POD_NAME, where POD_NAME is the problematic Pod’s name, to review logs from previous runs and identify the cause of failed start attempts.
- A. Connect to the Pod with kubectl exec -it POD_NAME -- /bin/bash, where POD_NAME is the problematic Pod’s name. Check logs in the /var/log/messages folder to identify the issue.
- B. Run gcloud projects get-iam-policy PROJECT_ID, where PROJECT_ID is the project’s ID for the Artifact Registry. Check IAM bindings of the node pool’s service account to ensure it has roles/artifactregistry.reader permissions.
- D. In the Google Cloud Console, go to Cloud Logging for the cluster’s VPC project. Filter for denied egress traffic to the Private Google Access CIDR range and verify if egress from the GKE cluster to this range is blocked.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use kubectl logs POD_NAME, where POD_NAME is the problematic Pod’s name, to review logs from previous runs and identify the cause of failed start attempts.

**The correct answer is**

**C. Use kubectl logs POD_NAME, where POD_NAME is the problematic Pod’s name, to review logs from previous runs and identify the cause of failed start attempts.**

Explanation:

When a Pod is in a **CrashLoopBackoff** state, it means the container inside the Pod repeatedly fails to start, causing Kubernetes to restart it. The first step in troubleshooting is to inspect the **Pod’s logs** to understand why the container is crashing. Using `kubectl logs POD_NAME` allows you to view logs for the most recent attempt and any previous failures (`kubectl logs POD_NAME --previous`). These logs often provide direct clues as to why the container is failing to start, such as missing environment variables, incorrect configurations, or application errors.

Justifications for Incorrect Options:

  * **Option A: Connect to the Pod with kubectl exec**  
Since the Pod is in a CrashLoopBackoff state, the container is likely not running long enough to establish a shell connection. Additionally, Kubernetes Pods don’t typically log to `/var/log/messages`, as application logs are usually written to stdout and stderr, which `kubectl logs` retrieves.

  * **Option B: Check IAM permissions for Artifact Registry access**  
While incorrect IAM permissions could prevent access to Artifact Registry, this would cause an `ImagePullBackOff` error, not a CrashLoopBackoff. If the container was deployed successfully, the issue is likely related to the application or its configuration within the container.

  * **Option D: Check Cloud Logging for denied egress traffic to the Private Google Access CIDR range**  
This option is relevant if there are network issues affecting access to external resources; however, a CrashLoopBackoff is typically caused by container-specific errors rather than network configurations. Network issues would more likely prevent the application from functioning properly after starting, rather than causing repeated crashes at startup.

</details>

---

### Exam 5 · Q38

**You’re using Cloud Build to build and test container images before deploying them to Cloud Run. The images are stored in Artifact Registry, and you need to ensure that only images that have passed testing are deployed, with minimal operational overhead. What should you do?**

- **A.** Deploy a new revision to a **Cloud Run** service and assign it a tag that provides access at a specific URL without serving traffic. Test this revision, and once confirmed, migrate traffic to the new revision.
- **D.** Configure **build provenance** on your **Cloud Build** pipeline, confirm all tests have passed, and deploy the image to a **Cloud Run** service.
- **C.** Set up a **GKE cluster** , verify that all tests have passed, and deploy the image to the **GKE cluster**.
- **B.** Enable **Binary Authorization** on your **Cloud Run** service. Create an attestation for images that pass all tests, and configure **Binary Authorization** to allow only images with valid attestations to be deployed.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **B.** Enable **Binary Authorization** on your **Cloud Run** service. Create an attestation for images that pass all tests, and configure **Binary Authorization** to allow only images with valid attestations to be deployed.

**The correct answer is**

**B. Enable Binary Authorization on your Cloud Run service. Create an attestation for images that pass all tests, and configure Binary Authorization to allow only images with valid attestations to be deployed.**

Explanation:

**Binary Authorization** provides a security layer that ensures only container images meeting specific criteria, such as passing all tests, are deployed to production environments like **Cloud Run**. By configuring Binary Authorization with attestations, you can require that only images that pass testing (and have corresponding attestations) are allowed to be deployed. This approach automates enforcement of deployment policies with minimal operational overhead, as Binary Authorization will automatically block any unapproved images.

Justifications for Incorrect Options:

  * **Option A: Deploy a new revision and assign it a tag**  
This option requires manual steps to test and shift traffic to the new revision. Although it provides a mechanism for testing, it does not enforce strict control over which images can be deployed, nor does it prevent untested images from being deployed.

  * **Option C: Set up a GKE cluster and deploy the image**  
Deploying to GKE introduces additional complexity, as Cloud Run is the intended deployment environment in this scenario. This option does not address the requirement for controlled deployment based on testing results, nor does it leverage Binary Authorization.

  * **Option D: Configure build provenance on your Cloud Build pipeline**  
Build provenance tracks the source and build process of an artifact but does not enforce deployment rules based on test results. Provenance alone does not restrict deployments to tested images, nor does it automatically prevent untested images from being deployed.

**Relevant Documentation:**

For more on Binary Authorization and using attestations to control deployments, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

  * [Binary Authorization with Cloud Run](https://cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run)

</details>

---

### Exam 5 · Q42

**You are migrating a containerized application to Cloud Run and plan to use Cloud Build to build and push your container image to Artifact Registry. For deployment, you’ll use Cloud Deploy to move the image to production. To ensure that only secure images are deployed, what should you do?**

- **C.** Store the encrypted image in **Secret Manager** and deploy it to production.
- **B.** Enable **Artifact Analysis** to scan the image for vulnerabilities, and use **Cloud Key Management Service** (KMS) to encrypt the image before deployment to production.
- **A.** Use **Cloud Armor** in front of **Cloud Run** to protect the container image from threats.
- **D.** Use **Binary Authorization** to enforce a policy allowing only images signed with a trusted key to be deployed to production.

<details><summary>Answer &amp; explanation</summary>

**Correct:** **D.** Use **Binary Authorization** to enforce a policy allowing only images signed with a trusted key to be deployed to production.

The correct answer is 

**D. Use Binary Authorization to enforce a policy allowing only images signed with a trusted key to be deployed to production.**

Explanation:

**Binary Authorization** is a security feature that allows you to define and enforce policies to ensure that only trusted and verified container images are deployed to production. By configuring Binary Authorization to require a signed attestation, you can enforce that only images that have passed security checks (such as vulnerability scans) and are signed with a trusted key are deployed. This approach is directly aligned with best practices for securing container deployments on Google Cloud.

Justifications for Incorrect Options:

  * **Option A: Use Cloud Armor in front of Cloud Run to protect the container image from threats**  
Cloud Armor provides network-level protection by filtering incoming requests based on rules but does not control or verify container images. It does not enforce security on the images themselves.

  * **Option B: Enable Artifact Analysis and use Cloud Key Management Service (KMS) to encrypt the image**  
While Artifact Analysis is useful for vulnerability scanning, encrypting the image with KMS is unnecessary for deployment. The critical step is using Binary Authorization to enforce deployment policies based on the security of the image.

  * **Option C: Store the encrypted image in Secret Manager and deploy it to production**  
Secret Manager is designed to store sensitive configuration data, not container images. Artifact Registry is the appropriate place for storing container images, with Binary Authorization used to enforce deployment security.

**Relevant Documentation:**

For more information on Binary Authorization and Artifact Analysis, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

</details>

---

### Exam 5 · Q44

**Which approach should you take to efficiently configure an application deployed on Compute Engine instances across multiple projects, each representing a different environment in your software development process (development, QA, staging, and production)?**

- III. Deploy your chosen deployment tool on an instance within each project. Utilize a deployment job to fetch the relevant configuration file from your version control system and apply it during application deployment on each instance.
- II. Configure a metadata key within each project named "environment" and set its value to reflect the environment served by the instance. Use a deployment tool to access instance metadata and configure the application based on the "environment" value.
- IV. Configure an instance custom-metadata key named "environment" with the appropriate environment value during each instance launch. Use your deployment tool to access instance metadata and configure the application based on the "environment" value.
- I. Utilize a startup script with the gcloud command when creating instances, which determines the project name indicating the environment, to configure the application accordingly.

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Configure a metadata key within each project named "environment" and set its value to reflect the environment served by the instance. Use a deployment tool to access instance metadata and configure the application based on the "environment" value.

**The most efficient approach to configure an application deployed on Compute Engine instances across multiple projects, each representing a different environment, would be:**

**II. Configure a metadata key within each project named "environment" and set its value to reflect the environment served by the instance. Use a deployment tool to access instance metadata and configure the application based on the "environment" value.**

**Justification:**

Option II allows for centralizing the configuration management by utilizing project metadata. By setting a metadata key named "environment" within each project and assigning values corresponding to the environment (e.g., development, QA, staging, production), you can easily identify and manage the environment of each instance.

Using a deployment tool to access instance metadata simplifies the configuration process. The deployment tool can retrieve the "environment" metadata value and configure the application accordingly during deployment. This approach promotes consistency and reduces the complexity of managing configurations across multiple environments.

**Why the other options are not as efficient:**

I. Utilizing a startup script with the gcloud command when creating instances may introduce complexity and potential inconsistencies, especially when dealing with multiple projects and environments. Managing configuration directly within the startup script could lead to maintenance challenges and difficulties in ensuring uniformity across environments.

III. Deploying a deployment tool on an instance within each project and fetching configuration files from a version control system adds unnecessary overhead. It requires additional resources and introduces dependencies on the instance running the deployment tool. This approach may also complicate the configuration management process, especially in large-scale deployments.

IV. Configuring instance custom-metadata keys named "environment" during instance launch introduces manual steps and potential errors. It requires ensuring that the correct metadata keys and values are set for each instance, which could lead to inconsistencies or misconfigurations across environments. Additionally, relying solely on instance metadata for configuration may not be as robust or scalable as leveraging a dedicated deployment tool.

**References:**

[https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata  https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom)

[https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata  https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom)

</details>

---

### Exam 5 · Q45

**You aim to restrict your App Engine standard configuration to a maximum of 5 instances while using the following setup:**

**Which code snippet should be integrated into your configuration to achieve this?**

- I. Utilize manual scaling with a set number of instances and a minimum pending latency of 30ms.
- III. Opt for basic scaling with a designated number of instances set at 5 and a minimum pending latency of 30ms.
- II. Employ manual scaling with a maximum instance limit of 5 and an idle timeout of 10 minutes.
- IV. Choose basic scaling with a cap on the maximum instances set to 5 and an idle timeout of 10 minutes.

<details><summary>Answer &amp; explanation</summary>

**Correct:** IV. Choose basic scaling with a cap on the maximum instances set to 5 and an idle timeout of 10 minutes.

**Correct Choice:**

  * **IV. Choose basic scaling with a cap on the maximum instances set to 5 and an idle timeout of 10 minutes.**

**Explanation:**

  * **Basic Scaling:** App Engine standard environment offers two scaling types: basic and automatic. Basic scaling allows you to directly control the maximum number of instances.

  * **Maximum Instances:** The `max_instances` setting within your configuration file enables you to explicitly limit the number of instances to 5.

  * **Idle Timeout:** The `idle_timeout` setting is relevant for basic scaling, ensuring that instances that remain inactive for 10 minutes are shutdown, thus conserving resources.

**Incorrect Options:**

  * **I. Utilize manual scaling with a set number of instances and a minimum pending latency of 30ms.**

    * **Manual Scaling Limitation:** Manual scaling is used to set a fixed number of instances, not a maximum. It doesn't allow you to cap the instances dynamically based on traffic.

  * **II. Employ manual scaling with a maximum instance limit of 5 and an idle timeout of 10 minutes.**

    * **No Such Setting:** Manual scaling in App Engine doesn't have a `max_instances` setting.

  * **III. Opt for basic scaling with a designated number of instances set at 5 and a minimum pending latency of 30ms.**

    * **Basic Scaling Limitation:** With basic scaling, you control the maximum, not a fixed number of instances. Your app could still run fewer instances.

**References:**  
[https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed#scaling_types](https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed#scaling_types  https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#manual_scaling)

[https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#manual_scaling](https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed#scaling_types  https://cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#manual_scaling)

</details>

---

### Exam 5 · Q47

**You are setting up monitoring for your application deployed on a Compute Engine virtual machine instance equipped with the Stackdriver Monitoring Agent. The application functions as a Unix process on the instance. Your objective is to receive alerts if the Unix process remains inactive for at least 5 minutes. Given the limitation that you cannot modify the application to produce metrics or logs, what alert condition should you establish?**

- II. Process status evaluation
- IV. Metric level benchmark
- III. Metric nonexistence detection
- I. System availability assessment

<details><summary>Answer &amp; explanation</summary>

**Correct:** II. Process status evaluation

**Correct Option: II. Process status evaluation**

**Justification:**

  * **Process Status Evaluation Focus:** Process status checks directly monitor whether a particular process is running or not, aligning precisely with the goal of detecting inactivity.

  * **Monitoring Agent Capability:** The Stackdriver Monitoring Agent can track system-level metrics, including the existence and state of Unix processes. This makes process status evaluation a readily achievable monitoring method with the existing setup.

**Reasons Why Other Options Are Incorrect:**

  * **I. System Availability Assessment:** While useful for overall system health, this is too broad. A system could be available, but the specific application process might be inactive.

  * **III. Metric Nonexistence Detection:** This is relevant when a process _should_ produce metrics. This approach would fail to signal if the process is expected to be inactive for periods and thus naturally produce no metrics.

  * **IV. Metric Level Benchmark:** This involves comparing metrics to thresholds, which is not suitable when the goal is to detect the very absence of activity and the implied lack of any metrics.

**References:**  
[https://cloud.google.com/monitoring/alerts/policies-in-json#json-process-health](https://cloud.google.com/monitoring/alerts/policies-in-json#json-process-health  https://cloud.google.com/monitoring/alerts/types-of-conditions#metric-threshold)

[https://cloud.google.com/monitoring/alerts/types-of-conditions#metric-threshold](https://cloud.google.com/monitoring/alerts/policies-in-json#json-process-health  https://cloud.google.com/monitoring/alerts/types-of-conditions#metric-threshold)

</details>

---

### Exam 5 · Q49

**You have a container deployed on Google Kubernetes Engine. Occasionally, the container experiences delays in launching, leading to failures in the liveness probe. What is the recommended action to address this issue?**

- I. Implement a startup probe.
- III. Raise the CPU limit for the container.
- II. Extend the initial delay for the liveness probe.
- IV. Introduce a readiness probe.

<details><summary>Answer &amp; explanation</summary>

**Correct:** I. Implement a startup probe.

**The recommended action to address the issue of occasional delays in container launching, leading to failures in the liveness probe, is:**

**I. Implement a startup probe.**

**Explanation:**

  * **A startup probe is specifically designed to determine if a container has started successfully before the liveness probe is activated.**

  * **By implementing a startup probe, you can delay the execution of the liveness probe until the container has had sufficient time to start up and initialize properly.**

  * **This helps prevent false-positive liveness probe failures caused by temporary delays during container startup, allowing the container to become ready and available for handling traffic only after it has fully initialized and is able to respond to requests properly.**

The other options can be explained as follows:

II. Extending the initial delay for the liveness probe may provide some temporary relief by giving the container more time to start up before the probe starts checking its health. However, this approach does not address the root cause of the issue and may result in longer detection times for actual liveness failures.

III. Raising the CPU limit for the container might improve its performance but is unlikely to directly resolve delays in container startup. CPU limits are more relevant for managing resource allocation and preventing resource contention, rather than addressing startup delays.

IV. Introducing a readiness probe is also a good practice, but it specifically checks if the container is ready to handle traffic. While it helps ensure that only healthy containers receive traffic, it does not directly address delays in container startup, which is the primary concern in this scenario.

**Reference:**

<https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-startup-probes>

</details>

---

### Exam 5 · Q57

**Your application is deployed within a Google Kubernetes Engine (GKE) cluster. Whenever a new version of your application is released, your CI/CD tool updates the `spec.template.spec.containers[0].image` value to point to the Docker image of the new application version. Upon applying the change, you aim to deploy a minimum of 1 replica of the new version while ensuring that the previous replicas are retained until the new replica is deemed healthy.**

**Which modification should you apply to the GKE Deployment object shown below?**

**apiVersion: apps/v1**

**kind: Deployment**

**metadata:**

**name: ecommerce-frontend-deployment**

**spec:**

**replicas: 3**

**selector:**

**matchLabels:**

**app: ecommerce-frontend**

**template:**

**metadata:**

**labels:**

**app: ecommerce-frontend**

**spec:**

**containers:**

**\- name: ecommerce-frontend-webapp**

**image: ecommerce-frontend-webapp:1.7.9**

**ports:**

**\- containerPort: 80**

- A. Configure the Deployment strategy as RollingUpdate with `maxSurge` set to 0 and `maxUnavailable` set to 1.
- C. Configure the Deployment strategy as Recreate with `maxSurge` set to 0 and `maxUnavailable` set to 1.
- D. Configure the Deployment strategy as Recreate with `maxSurge` set to 1 and `maxUnavailable` set to 0.
- B. Configure the Deployment strategy as RollingUpdate with `maxSurge` set to 1 and `maxUnavailable` set to 0.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Configure the Deployment strategy as RollingUpdate with `maxSurge` set to 1 and `maxUnavailable` set to 0.

**Correct Answer:**

  * **B. Configure the Deployment strategy as RollingUpdate with**`**maxSurge**`**set to 1 and**`**maxUnavailable**`**set to 0.**

**Justification:**

  * **RollingUpdate:** This strategy gracefully replaces existing pods with new ones, ensuring service availability throughout the update. (Kubernetes Documentation: <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>)

  * **maxSurge: 1** This allows the creation of one additional pod beyond the desired replica count (`replicas: 3`). This ensures the new replica starts and becomes healthy before proceeding.

  * **maxUnavailable: 0** Ensures at least 3 pods (the original `replicas` count) remain available, maintaining service uptime.

**Incorrect Answers**

  * **A. ...maxSurge**`**set to 0 and**`**maxUnavailable` set to 1.**

    * **Reasoning:** This setup would prevent a new pod from being created until an old one is terminated, hindering the requirement for a temporary overlap of a new and old versions.

  * **C. Configure the Deployment strategy as Recreate...**

    * **Reasoning:** The Recreate strategy terminates all existing pods before starting new ones. This would introduce downtime which conflicts with the goal of maintaining service availability.

  * **D. Configure the Deployment strategy as Recreate...**

    * **Reasoning:** Same as C – the Recreate strategy would lead to service unavailability.

</details>

---

### Exam 5 · Q58

**As the lead developer responsible for a financial risk calculation API hosted on Cloud Run with a gRPC interface, you continuously work on enhancing the risk analysis features. You want to make these optimizations available first to a select group of customers who signed up to test the improvements before releasing them more broadly. Your CI/CD pipeline has created a new version of the API as a container image, which is now stored in the Artifact Registry.**

**Which rollout strategy should you use to manage this controlled release?**

- A. Use Cloud Run’s traffic splitting to direct a specific percentage of traffic from registered test users to the updated service.
- C. Control access to the new service using a feature flag for customers registered to test the updates.
- B. Implement a blue/green deployment to transition traffic to the new version of the service.
- D. Migrate traffic to the updated service and activate session affinity for Cloud Run.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Control access to the new service using a feature flag for customers registered to test the updates.

The correct answer is 

**C. Control access to the new service using a feature flag for customers registered to test the updates.**

Explanation:

Using a **feature flag** is the most effective strategy for selectively enabling new optimizations for a specific group of customers who have opted to test them. Feature flags allow you to control access to the updated features based on specific user criteria, such as registration for testing. This approach enables you to:

  * **Precisely target** only the selected group of customers without affecting others.

  * **Gradually roll out and monitor** the new features for feedback before a full release.

Feature flags offer flexibility and reduce the risk of potential issues affecting all users by isolating changes to only a controlled group.

Justifications for Incorrect Options:

  * **Option A: Traffic splitting based on a percentage**  
Traffic splitting in Cloud Run distributes traffic based on percentage rather than user-specific criteria, making it unsuitable for selectively targeting specific registered customers.

  * **Option B: Blue/green deployment**  
Blue/green deployments are designed for swapping all traffic between two service versions and do not allow selective feature access for a specific user group. This approach is better suited for general rollouts or quick rollbacks, not for limited testing.

  * **Option D: Session affinity for Cloud Run**  
Session affinity ensures that a user’s requests are directed to the same instance, but it does not allow you to control which users see the new features. Session affinity is not relevant for user-specific feature testing.

</details>

---

### Exam 5 · Q59

**In the process of replatforming legacy applications onto Google Kubernetes Engine, your organization aims to decompose a monolithic application into microservices without rewriting the application code. There are multiple instances with read and write access to a configuration file stored on a shared file system. How can you minimize the effort required to manage this transition?**

- IV. Implement a new ConfigMap and volumeMount to store the contents of the configuration file.
- I. Utilize a new Cloud Storage bucket and mount it within the container using FUSE.
- II. Establish a new persistent disk and mount the volume as a shared PersistentVolume.
- III. Deploy a new Filestore instance and mount the volume as an NFS PersistentVolume.

<details><summary>Answer &amp; explanation</summary>

**Correct:** III. Deploy a new Filestore instance and mount the volume as an NFS PersistentVolume.

**III. Deploy a new Filestore instance and mount the volume as an NFS PersistentVolume.**

Here's why:

  * **Supports Shared Access:** Filestore provides a network file system (NFS) solution that natively supports multiple instances reading and writing to the same shared storage. This aligns well with the legacy application's requirements.

  * **Manageability:** Filestore is a fully managed service, significantly reducing the administrative overhead compared to manually managing a persistent disk or self-hosting an NFS solution.

**Why other options are less suitable:**

  * **I. Utilize a new Cloud Storage bucket and mount it within the container using FUSE.** Cloud Storage is object storage, not a file system. While FUSE could be used, it adds complexity and might introduce performance or consistency issues.

  * **II. Establish a new persistent disk and mount the volume as a shared PersistentVolume.** Most persistent disk types in Kubernetes don't support simultaneous mounting from multiple pods, making this unsuitable for the shared file system requirement.

  * **IV. Implement a new ConfigMap and volumeMount to store the contents of the configuration file.** ConfigMaps are designed for storing configuration data, not large shared files, and they might have size limitations.

**References:**

[https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes https://cloud.google.com/filestore/docs/accessing-fileshares](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes   https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

[https://cloud.google.com/storage/docs/gcs-fuse](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes   https://cloud.google.com/filestore/docs/accessing-fileshares  https://cloud.google.com/storage/docs/gcs-fuse)

</details>

---

### Exam 6 · Q2

**You are tasked with deploying a new feature to production on Cloud Run. Your company’s SRE team requires that all deployments be gradual to minimize the risk of downtime due to potential code issues. You want to set up this deployment with minimal configuration effort.**

**What should you do?**

- A. Set up the application’s frontend load balancer to alternate traffic between the new and previous revisions.
- B. Modify the application code to route a small portion of users to the new revision.
- C. Deploy the feature with the “Serve this revision immediately” option turned off, configure the new revision to handle a small percentage of traffic, monitor for issues, and gradually increase traffic if no errors are found.
- D. Deploy the feature with “Serve this revision immediately” enabled. Check for any issues, roll back to the prior revision if errors occur, and repeat until the deployment is confirmed to be error-free.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Deploy the feature with the “Serve this revision immediately” option turned off, configure the new revision to handle a small percentage of traffic, monitor for issues, and gradually increase traffic if no errors are found.

The correct answer is 

**C. Deploy the feature with the “Serve this revision immediately” option turned off, configure the new revision to handle a small percentage of traffic, monitor for issues, and gradually increase traffic if no errors are found.**

Explanation:

Cloud Run supports **traffic splitting** between revisions, allowing you to roll out a new version gradually. By deploying the new feature with the **“Serve this revision immediately”** option turned off, you can initially direct a small percentage of traffic to the new revision. This strategy minimizes the risk of downtime because you can monitor for issues with a limited user base. If no issues are detected, you can gradually increase the traffic until 100% is routed to the new revision. This approach aligns with the SRE team’s requirement for a gradual rollout and minimizes configuration effort.

Justifications for Incorrect Options:

  * **Option A: Set up the load balancer to alternate traffic between revisions**  
Configuring a load balancer to alternate traffic is complex and unnecessary. Cloud Run’s built-in traffic splitting feature provides a simpler, more effective solution for gradual rollouts.

  * **Option B: Modify application code to route users to the new revision**  
Code-based traffic routing adds unnecessary complexity and maintenance overhead. Cloud Run’s traffic splitting can handle this without code changes, providing a more efficient deployment strategy.

  * **Option D: Enable “Serve this revision immediately” and roll back if issues arise**  
Serving the revision immediately directs 100% of traffic to the new version, which doesn’t allow for a gradual rollout. This approach increases the risk of downtime if issues are detected only after deployment.

**Relevant Documentation:**

For more information, refer to:

  * [Traffic Splitting in Cloud Run](https://cloud.google.com/functions/docs/configuring/traffic-splitting)

</details>

---

### Exam 6 · Q12

**You work for an ecommerce company migrating several applications to Google Cloud, and you're involved in migrating one of these applications. The application currently runs on a VM without specific OS dependencies. You’ve created a Dockerfile and uploaded the resulting image to Artifact Registry. To reduce infrastructure management and operational complexity, you need an appropriate deployment option.**

**What should you do?**

- A. Deploy the image to Cloud Run.
- B. Deploy the image to a GKE Autopilot cluster.
- C. Deploy the image to a GKE Standard cluster.
- D. Deploy the image on a Compute Engine instance.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Deploy the image to Cloud Run.

The correct answer is

**A. Deploy the image to Cloud Run**.

Explanation:

**Cloud Run** is a fully managed, serverless platform designed for deploying containerized applications. It automatically scales based on traffic, significantly reduces infrastructure management, and requires minimal operational overhead. Since your application has no specific OS dependencies and you’re aiming to reduce infrastructure management and complexity, Cloud Run is the best choice.

Key benefits of Cloud Run:

  * **Serverless** : Cloud Run handles all infrastructure management, including scaling, load balancing, and updates.

  * **Cost-effective** : You only pay when the application is serving requests, making it ideal for unpredictable or bursty traffic.

  * **Low complexity** : Cloud Run requires minimal configuration compared to setting up and maintaining a Kubernetes cluster or virtual machine.

Justifications for Incorrect Options:

  * **Option B: Deploy the image to a GKE Autopilot cluster**  
Although GKE Autopilot reduces some Kubernetes management overhead, it still requires more configuration and ongoing Kubernetes management than Cloud Run. Cloud Run is a simpler and more cost-effective choice for an application without OS dependencies.

  * **Option C: Deploy the image to a GKE Standard cluster**  
A GKE Standard cluster provides more control over configuration but requires significant Kubernetes management, which increases complexity and operational overhead.

  * **Option D: Deploy the image on a Compute Engine instance**  
Using Compute Engine would involve managing VM instances, including scaling, health checks, and OS updates, adding unnecessary complexity compared to a serverless option like Cloud Run.

**Relevant Documentation:**

For more information on Cloud Run, refer to:

  * [Getting started with Cloud Run](https://cloud.google.com/run/docs/quickstarts)

</details>

---

### Exam 6 · Q14

**You work at a financial services company that prioritizes containerized applications, and your team develops microservices. A Cloud Build pipeline is set up to create container images, run regression tests, and publish the images to Artifact Registry. To ensure only containers that pass regression tests are deployed to GKE clusters, you have already enabled Binary Authorization on the clusters.**

**What should you do next?**

- A. Deploy both Voucher Server and Voucher Client components. After a container image passes the regression tests, run Voucher Client as a step in the Cloud Build pipeline.
- B. Set up an attestor and a policy, then perform a vulnerability scan and create an attestation for the container image as part of the Cloud Build pipeline.
- C. Set up an attestor and a policy. Create an attestation for container images that pass regression tests as a step in the Cloud Build pipeline.
- D. Apply the Restricted level of Pod Security Standard to the relevant namespaces. Digitally sign the container images that pass regression tests as a step in the Cloud Build pipeline.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Set up an attestor and a policy. Create an attestation for container images that pass regression tests as a step in the Cloud Build pipeline.

The correct answer is 

**C. Set up an attestor and a policy. Create an attestation for container images that pass regression tests as a step in the Cloud Build pipeline.**

Explanation:

With **Binary Authorization** enabled, deploying only trusted container images requires creating **attestations** that certify an image has met specific criteria. By setting up an **attestor** and defining a **policy** in Binary Authorization, you can restrict deployments to images that have a valid attestation. Adding an attestation step in the **Cloud Build pipeline** ensures that only images passing regression tests are signed, thus allowing only those images to be deployed to the GKE clusters.

This approach leverages Binary Authorization to enforce security policies, ensuring that only verified and tested images are deployed to production environments.

Justifications for Incorrect Options:

  * **Option A: Deploy Voucher Server and Client**  
Voucher is a third-party tool for creating attestations, but Google Cloud provides native support for attestations with Binary Authorization. Using Voucher introduces additional complexity and is unnecessary if Binary Authorization and Cloud Build are already integrated.

  * **Option B: Perform a vulnerability scan and create an attestation**  
A vulnerability scan is useful, but the question specifies ensuring that images passing regression tests are deployed. While scanning for vulnerabilities is beneficial, the attestation step should focus on confirming that regression tests have passed.

  * **Option D: Apply the Restricted Pod Security Standard and sign images**  
The Restricted Pod Security Standard governs security settings for pod configurations but does not verify or enforce container image provenance. Binary Authorization attestations are necessary to enforce that only approved images (those that passed tests) are deployed.

**Relevant Documentation:**

For more information, refer to:

  * [Binary Authorization Overview](https://cloud.google.com/binary-authorization/docs/overview)

  * [Creating Attestations in Binary Authorization](https://cloud.google.com/binary-authorization/docs/making-attestations)

</details>

---
