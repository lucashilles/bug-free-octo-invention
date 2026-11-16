# Domain 3 — Innovating with Google Cloud Artificial Intelligence

56 questions. Answers are collapsed — try each question before expanding it.

## Questions

### Exam 1 · Q2

**BrightCart, a retail mobile app, wants to add features such as product image recognition, customer-support chat, and demand forecasting. The team includes both experienced data scientists and developers who have very limited machine learning experience. How does Google Cloud help BrightCart use artificial intelligence and machine learning effectively?**

- A. By providing scalable on-premises tensor processing units
- B. By providing APIs and tools for users with different levels of expertise
- C. By providing affordable and scalable quantum computing for application development
- D. By providing machine learning models that always require custom training

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. By providing APIs and tools for users with different levels of expertise

**Correct answer: B. By providing APIs and tools for users with different levels of expertise**

Google Cloud offers AI at several skill levels: pre-trained APIs (Vision, Natural Language and others) for developers with little ML knowledge, low-code options like AutoML, and full custom training on Gemini Enterprise Agent Platform (formerly Vertex AI) for data scientists. The clue is the mixed team: experienced data scientists and developers with limited ML experience.

**Why the others are wrong:**
- **A. On-premises tensor processing units**: TPUs are offered as cloud resources, and hardware alone does not help non-experts use ML.
- **C. Quantum computing**: quantum computing is not how Google Cloud delivers AI/ML features to app teams.
- **D. Models that always require custom training**: the opposite is true; pre-trained models and APIs work without any custom training.

**Remember:** Mixed skill levels = a range of AI tools, from pre-trained APIs to custom training.

**References:**
- [cloud.google.com/products/ai](https://cloud.google.com/products/ai)
- [docs.cloud.google.com/docs/ai-ml](https://docs.cloud.google.com/docs/ai-ml)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide)

</details>

---

### Exam 1 · Q36

**Trackly, a logistics analytics company, wants to create custom machine learning models to predict delivery delays. The team needs a managed Google Cloud platform that helps them prepare data, train models, deploy them, and monitor model performance after deployment. Which service should they use?**

- A. Document AI
- B. Natural Language API
- C. Google Kubernetes Engine
- D. Gemini Enterprise Agent Platform

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Gemini Enterprise Agent Platform

**Correct answer: D. Gemini Enterprise Agent Platform**

Gemini Enterprise Agent Platform (formerly Vertex AI) is Google Cloud's unified, managed ML platform. It covers the full ML lifecycle: preparing data, training custom models, deploying them and monitoring them in production. The clues are "custom machine learning models" and the list of lifecycle steps.

**Why the others are wrong:**
- **A. Document AI**: it extracts data from documents; it does not train general custom prediction models.
- **B. Natural Language API**: it is a pre-trained API for text analysis, not a platform for building custom models.
- **C. Google Kubernetes Engine**: GKE can run ML workloads, but it is a container platform, not a managed ML lifecycle service.

**Remember:** Build, train, deploy and monitor custom ML models = Gemini Enterprise Agent Platform.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview)

</details>

---

### Exam 1 · Q37

**PulseHelp, a customer support platform, wants to use machine learning to gain insights from data that does not fit neatly into rows and columns. The company wants to analyze spoken customer conversations and identify whether callers are happy, neutral, or frustrated. Which scenario best shows machine learning unlocking business value from unstructured data?**

- A. Analyzing spreadsheet records of equipment failures to predict upcoming repair schedules.
- B. Suggesting related items based on a customer’s earlier purchases.
- C. Reviewing payment activity to detect possible fraud and financial risk.
- D. Identifying customer sentiment from support center audio recordings.

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Identifying customer sentiment from support center audio recordings.

**Correct answer: D. Identifying customer sentiment from support center audio recordings.**

Audio recordings are unstructured data. They do not fit into rows and columns. ML (speech-to-text plus sentiment analysis) can turn them into insight about how customers feel. The clue is "data that does not fit neatly into rows and columns" and "spoken customer conversations".

**Why the others are wrong:**
- **A. Spreadsheet records of equipment failures**: spreadsheets are structured data.
- **B. Suggesting items from earlier purchases**: purchase history is structured transaction data.
- **C. Reviewing payment activity for fraud**: payment records are structured data.

**Remember:** Audio, images, video and free text = unstructured. ML is what unlocks value from them.

**References:**
- [cloud.google.com/speech-to-text](https://cloud.google.com/speech-to-text)
- [docs.cloud.google.com/natural-language/docs](https://docs.cloud.google.com/natural-language/docs)
- [docs.cloud.google.com/natural-language/docs/basics](https://docs.cloud.google.com/natural-language/docs/basics)

</details>

---

### Exam 1 · Q41

**PhotoTrail, a travel-sharing mobile app, wants to train a machine learning model that can classify uploaded photos into categories such as beaches, mountains, city landmarks, and forests. Which Google Cloud product or service should PhotoTrail use?**

- A. Video Intelligence API
- B. AutoML Vision
- C. BigQuery ML
- D. Looker

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. AutoML Vision

**Correct answer: B. AutoML Vision**

AutoML Vision lets a team train a custom image classification model using its own labeled photos, without writing ML code. The categories here (beaches, mountains, landmarks, forests) are specific to PhotoTrail. That calls for a custom model, not a generic pre-trained one. The clue is "train a machine learning model" to "classify uploaded photos into categories".

**Why the others are wrong:**
- **A. Video Intelligence API**: it analyzes video, not still photos.
- **C. BigQuery ML**: it builds models with SQL on structured data in BigQuery. It is not the direct way to train an image classifier from photos.
- **D. Looker**: Looker is a BI and reporting tool, not an ML training service.

**Remember:** Custom image categories + labeled photos + little ML expertise = AutoML (Vision).

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model)
- [docs.cloud.google.com/video-intelligence/docs](https://docs.cloud.google.com/video-intelligence/docs)
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)

**⚠️ Note:** "AutoML Vision" is the old standalone product name. AutoML now lives inside Gemini Enterprise Agent Platform. The concept (custom image categories with labeled data and no code = AutoML) is still right, so pick B.

</details>

---

### Exam 2 · Q6

**BrightBee, an online tutoring website, wants to train a custom machine learning model that can sort short customer messages from its support form into categories such as billing, course feedback, technical issue, and tutor request. Which Google Cloud product or service should BrightBee use?**

- A. Google Distributed Cloud
- B. Recommendations from Agent Search
- C. AutoML Natural Language
- D. Pub/Sub

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. AutoML Natural Language

**Correct answer: C. AutoML Natural Language**

BrightBee wants a custom model that sorts short text messages into its own categories. AutoML Natural Language trains a custom text classification model from labeled examples without deep ML expertise. The clues are "custom machine learning model", "short customer messages" (text), and "categories".

**Why the others are wrong:**
- **A. Google Distributed Cloud**: This runs Google Cloud infrastructure in your own locations or at the edge; it is not an ML tool.
- **B. Recommendations from Agent Search**: This recommends products or content to users; it does not classify support messages.
- **D. Pub/Sub**: Pub/Sub is a messaging service for moving events, not for training models.

**Remember:** Custom categories + your own labeled text + little ML expertise → AutoML for text.

**References:**
- [docs.cloud.google.com/natural-language/docs](https://docs.cloud.google.com/natural-language/docs)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview)
- [docs.cloud.google.com/pubsub/docs/overview](https://docs.cloud.google.com/pubsub/docs/overview)

**⚠️ Note:** "AutoML Natural Language" is an older standalone product name. Today AutoML is part of the AI platform (Gemini Enterprise Agent Platform, formerly Vertex AI), and Google also steers text classification toward tuning Gemini models. The idea is still right, so pick the keyed answer on this exam.

</details>

---

### Exam 2 · Q13

**CareNest, a healthcare appointment support website, receives thousands of patient questions through chat and phone every week. The support team wants to handle common requests more efficiently while still keeping conversations personalized and helpful for each patient. Which Google Cloud product or service should CareNest use?**

- A. Recommendations AI
- B. Cloud Identity
- C. Contact Center AI Platform
- D. Cloud Text-to-Speech

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Contact Center AI Platform

**Correct answer: C. Contact Center AI Platform**

Contact Center AI Platform is Google's customer-service solution. Virtual agents handle common requests automatically, and AI helps human agents resolve the rest, while keeping conversations personal. The clues are "chat and phone", "common requests more efficiently", and "personalized".

**Why the others are wrong:**
- **A. Recommendations AI**: This suggests products to shoppers; it does not handle support conversations.
- **B. Cloud Identity**: Cloud Identity manages users and sign-in, not customer conversations.
- **D. Cloud Text-to-Speech**: Text-to-Speech only turns text into spoken audio; it is one building block, not a full contact center solution.

**Remember:** High-volume customer chats and calls → Contact Center AI.

**References:**
- [cloud.google.com/solutions/contact-center-ai-platform](https://cloud.google.com/solutions/contact-center-ai-platform)
- [docs.cloud.google.com/contact-center/ccai-platform/docs](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
- [docs.cloud.google.com/text-to-speech/docs](https://docs.cloud.google.com/text-to-speech/docs)

</details>

---

### Exam 2 · Q15

**UrbanPedal, a bike-sharing company, operates smart docking stations across several cities. They store rider activity, station usage, and repair history in BigQuery. They want to maintain their docking stations more efficiently, reduce unnecessary part replacements, and support their sustainability goals. How can Google Cloud services help UrbanPedal?**

- A. Secure data access by using Identity and Access Management.
- B. Provide access to third-party developers by creating an API using Apigee.
- C. Create a model in BigQuery to predict future maintenance schedules.
- D. Move data from BigQuery to Cloud Storage to reduce storage costs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Create a model in BigQuery to predict future maintenance schedules.

**Correct answer: C. Create a model in BigQuery to predict future maintenance schedules.**

UrbanPedal already keeps usage and repair history in BigQuery. With BigQuery ML it can build a predictive maintenance model right where the data lives. Servicing stations only when needed cuts waste and supports sustainability. The clues are "maintain more efficiently" and "reduce unnecessary part replacements".

**Why the others are wrong:**
- **A. Secure data with IAM**: IAM controls access, but it does not make maintenance more efficient.
- **B. Create an API with Apigee**: Sharing data with outside developers does not predict maintenance needs.
- **D. Move data to Cloud Storage**: Moving data may lower storage costs, but it does nothing for maintenance planning.

**Remember:** Historical data + "predict" + data already in BigQuery → build an ML model in BigQuery.

**References:**
- [cloud.google.com/bigquery/docs/bqml-introduction](https://cloud.google.com/bigquery/docs/bqml-introduction)
- [cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create)
- [cloud.google.com/apigee/docs/api-platform/get-started/what-apigee](https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

</details>

---

### Exam 2 · Q17

**FitRoute, a fitness class booking app, wants to create a machine learning model to predict member attendance trends for the next 18 months. The company has four years of attendance records from 220 studios, but each studio exported its data using different column names, date formats, and file structures. FitRoute must prepare the data before training the model. What should they do?**

- A. Use only the most recent 10 months of data so the model has fewer inconsistencies to process.
- B. Transform the data into a consistent format.
- C. Group the records by file format and train a separate model for each group.
- D. Select a machine learning model type that can automatically process all different input formats.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Transform the data into a consistent format.

**Correct answer: B. Transform the data into a consistent format.**

Machine learning needs clean, consistent data. When 220 studios use different column names, date formats, and file structures, the first step is to standardize the data into one format. Then the full four years of history can be used to train one good model. The clue is "must prepare the data before training".

**Why the others are wrong:**
- **A. Use only the last 10 months**: Throwing away most of the history weakens an 18-month forecast and does not fix the format problem.
- **C. Separate model per file format**: This splits the data into weaker models and does not solve inconsistent columns or dates.
- **D. Model that handles any format**: No model type automatically fixes messy, inconsistent input; data preparation is still needed.

**Remember:** Good ML starts with clean, consistent data: prepare and standardize first.

**References:**
- [docs.cloud.google.com/bigquery/docs/preprocess-overview](https://docs.cloud.google.com/bigquery/docs/preprocess-overview)
- [docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data)
- [docs.cloud.google.com/architecture/ml-on-gcp-best-practices](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices)

</details>

---

### Exam 2 · Q29

**RiverBank Plus, a digital banking company, notices that many customers stop using its savings and investment products each year. The company wants to use data and AI to predict which active customers are likely to leave, so the retention team can proactively offer better support, personalized discounts, or improved services. What should RiverBank Plus do?**

- A. Create a dashboard of customers who closed their accounts in the past, and manually look for visible patterns in the charts.
- B. Create a ML model based on the demographics and activities of previous customers who closed their accounts.
- C. Create a survey for all customers to identify their current level of satisfaction.
- D. Create a report based on customer feedback collected during the previous year.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Create a ML model based on the demographics and activities of previous customers who closed their accounts.

**Correct answer: B. Create a ML model based on the demographics and activities of previous customers who closed their accounts.**

Predicting which current customers will leave (churn) is a classic ML use case. A model learns patterns from past customers who left and then scores active customers by risk. The clues are "predict which active customers are likely to leave" and "proactively".

**Why the others are wrong:**
- **A. Dashboard and manual pattern search**: Dashboards look backward and manual review does not scale or predict individual risk.
- **C. Satisfaction survey**: Surveys show current opinions but do not predict who will leave, and many customers won't answer.
- **D. Report on last year's feedback**: A report describes the past; it does not predict future behavior.

**Remember:** "Predict" + historical examples of the outcome → train an ML model.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [docs.cloud.google.com/bigquery/docs/reference-patterns](https://docs.cloud.google.com/bigquery/docs/reference-patterns)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/bqml](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/bqml)

</details>

---

### Exam 2 · Q38

**BrightLens Analytics is building image recognition models on Google Cloud using TensorFlow. The data science team wants to train these advanced machine learning models more quickly by using hardware specifically designed for machine learning workloads. Which solution should BrightLens Analytics use?**

- A. TPUs
- B. CPUs
- C. High-memory VMs
- D. GPUs

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. TPUs

**Correct answer: A. TPUs**

Tensor Processing Units (TPUs) are Google's custom chips designed specifically for machine learning. They speed up training of large models such as image recognition networks, and they work well with TensorFlow. The clue is "hardware specifically designed for machine learning workloads".

**Why the others are wrong:**
- **B. CPUs**: General-purpose processors. They can train models, but slowly compared with accelerators.
- **C. High-memory VMs**: More RAM helps with big datasets in memory, but it doesn't accelerate the math of model training.
- **D. GPUs**: GPUs also accelerate ML training and are a valid choice, but they were designed for graphics first. "Designed specifically for ML" points to TPUs.

**Remember:** Hardware built specifically for ML → TPUs.

**References:**
- [cloud.google.com/tpu](https://cloud.google.com/tpu)
- [docs.cloud.google.com/tpu/docs/intro-to-tpu](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
- [tensorflow.org/guide/tpu](https://tensorflow.org/guide/tpu)

</details>

---

### Exam 2 · Q44

**ShopTrail, a retail analytics website, keeps purchase history and customer behavior data in BigQuery. Its analysts know SQL and want to create machine learning models directly on that data without exporting it or learning Python or Java. Which Google Cloud tool should they use?**

- A. Cloud Vision API
- B. BigQuery ML
- C. Agent Studio
- D. Spanner

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. BigQuery ML

**Correct answer: B. BigQuery ML**

BigQuery ML lets analysts create and run ML models using standard SQL, directly on data already stored in BigQuery. No data export and no Python or Java are needed. The clues are "analysts know SQL" and "without exporting it".

**Why the others are wrong:**
- **A. Cloud Vision API**: Vision API is a pre-trained model for images, not for building models on purchase data.
- **C. Agent Studio**: Agent Studio is a no-code tool for building AI agents, not for training models on BigQuery tables.
- **D. Spanner**: Spanner is a transactional database, not an ML tool.

**Remember:** SQL skills + data in BigQuery + ML → BigQuery ML.

**References:**
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)
- [docs.cloud.google.com/bigquery/docs/create-machine-learning-model](https://docs.cloud.google.com/bigquery/docs/create-machine-learning-model)
- [docs.cloud.google.com/vision/docs](https://docs.cloud.google.com/vision/docs)

</details>

---

### Exam 3 · Q3

**BrightDesk Assist is building a new support automation platform for its banking clients. Instead of only predicting which customers may complain, the company wants an AI system that can understand a customer’s goal, decide the next steps, call different internal tools, update records, and complete the support workflow with little or no human involvement. Which concept best describes this type of AI capability?**

- A. Descriptive analytics
- B. Generative AI
- C. Agentic AI
- D. Business Intelligence

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Agentic AI

**Correct answer: C. Agentic AI**

Agentic AI systems pursue a goal on their own. They reason, plan next steps, call tools and APIs, and take actions to complete a workflow with little human help. The clues are "decide the next steps", "call different internal tools" and "complete the workflow".

**Why the others are wrong:**
- **A. Descriptive analytics**: It explains what happened in past data; it takes no actions.
- **B. Generative AI**: It creates content, but on its own it does not plan and act across tools.
- **D. Business Intelligence**: BI is reporting and dashboards for human decision makers.

**Remember:** Goal + plan + use tools + take action = agentic AI.

**References:**
- [cloud.google.com/discover/what-is-agentic-ai](https://cloud.google.com/discover/what-is-agentic-ai)
- [cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)

</details>

---

### Exam 3 · Q23

**ClearNest Realty runs an internal portal where field agents upload apartment photos after site visits. The compliance team currently reviews every image manually because some photos may accidentally include sensitive documents, such as national ID cards or payment cards. ClearNest wants its developers to add automated image analysis to the portal as quickly as possible, without building and training a custom model. Which solution should ClearNest use?**

- A. Pre-trained APIs
- B. AutoML
- C. Custom training
- D. BigQuery ML

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Pre-trained APIs

**Correct answer: A. Pre-trained APIs**

Pre-trained APIs such as the Cloud Vision API are ready-to-use models that developers call directly. They can detect text and objects in images with no training. The clues are "as quickly as possible" and "without building and training a custom model".

**Why the others are wrong:**
- **B. AutoML**: AutoML still needs labeled data and training a custom model.
- **C. Custom training**: This takes the most time and ML expertise.
- **D. BigQuery ML**: It trains models with SQL on data in BigQuery, not a ready-made image analysis service.

**Remember:** Common task + fastest + no training = pre-trained API.

**References:**
- [cloud.google.com/vision](https://cloud.google.com/vision)
- [docs.cloud.google.com/vision/docs](https://docs.cloud.google.com/vision/docs)
- [docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction)

</details>

---

### Exam 3 · Q24

**StorySpark is a content creation app that wants to explain a basic AI concept to its new product team. The team needs to understand what type of AI can produce new outputs such as text, images, audio, code, or summaries based on user prompts. What is generative AI?**

- A. A machine learning model used only for language translation
- B. A specific field of AI that can be used to create content
- C. A general term that includes every type of machine learning algorithm
- D. An AI model used only for labeling images

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. A specific field of AI that can be used to create content

**Correct answer: B. A specific field of AI that can be used to create content**

Generative AI is a subset of AI that creates new content, such as text, images, audio, code and summaries, from prompts. The stem's clue is "produce new outputs".

**Why the others are wrong:**
- **A. Only for language translation**: Translation is one possible use, not the definition.
- **C. Includes every type of ML algorithm**: Generative AI is a subset of ML, not the umbrella term.
- **D. Only for labeling images**: Labeling images is classification, a different task.

**Remember:** Generative AI = creates new content.

**References:**
- [cloud.google.com/use-cases/generative-ai](https://cloud.google.com/use-cases/generative-ai)
- [cloud.google.com/discover/what-is-generative-ai](https://cloud.google.com/discover/what-is-generative-ai)
- [cloud.google.com/ai/generative-ai](https://cloud.google.com/ai/generative-ai)

</details>

---

### Exam 3 · Q40

**GlowTrail Media is adopting AI for its creative and engineering teams. The company wants a system that can produce new campaign emails, generate product banner images, and create sample application code from user prompts. Which branch of artificial intelligence is focused on creating new content like this?**

- A. Generative AI (gen AI)
- B. Predictive analytics
- C. Data warehousing
- D. Relational databases

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Generative AI (gen AI)

**Correct answer: A. Generative AI (gen AI)**

Generative AI creates new content such as text, images and code from prompts. Emails, banner images and sample code are all newly generated content.

**Why the others are wrong:**
- **B. Predictive analytics**: It forecasts outcomes from data; it doesn't create content.
- **C. Data warehousing**: It stores and analyzes data; it is not a branch of AI.
- **D. Relational databases**: They store structured data; they are not AI.

**Remember:** Create new content = generative AI.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide)
- [cloud.google.com/solutions/generative-ai](https://cloud.google.com/solutions/generative-ai)
- [cloud.google.com/learn/what-is-artificial-intelligence](https://cloud.google.com/learn/what-is-artificial-intelligence)

</details>

---

### Exam 3 · Q45

**HelioWorks Analytics wants its operations analysts to create and test internal AI agents that can answer policy questions, summarize business data, and automate simple approval workflows. The analysts do not have advanced coding or machine learning skills, so the company needs a Google Cloud interface where they can visually design, prototype, and publish agents with a no-code or low-code experience. Which option should they use?**

- A. Agent Studio
- B. Spanner
- C. Security Command Center
- D. Cloud Run

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Agent Studio

**Correct answer: A. Agent Studio**

Agent Studio is the no-code and low-code visual interface for designing, prototyping and publishing AI agents. It suits analysts without coding or ML skills. The clues are "visually design" and "no-code or low-code".

**Why the others are wrong:**
- **B. Spanner**: A globally distributed relational database.
- **C. Security Command Center**: A security and risk management service.
- **D. Cloud Run**: A serverless platform for running containers; it needs developers.

**Remember:** No-code or low-code agent building = Agent Studio.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [docs.cloud.google.com/run/docs](https://docs.cloud.google.com/run/docs)

</details>

---

### Exam 4 · Q1

**FitLens Market is building an AI application for a small group of professional sports coaches who need very specific performance predictions from proprietary athlete training data. Instead of using a ready-made pre-trained API, the company chooses to develop and train its own custom ML model. What is the main tradeoff of this approach?**

- A. It requires less technical expertise but offers faster implementation speed.
- B. It requires more effort and expertise but provides higher business differentiation.
- C. It shifts your cloud expenditure from OpEx to CapEx.
- D. It guarantees that the model will be 100% accurate.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. It requires more effort and expertise but provides higher business differentiation.

**Correct answer: B. It requires more effort and expertise but provides higher business differentiation.**

Building a custom model takes more data work, ML skills, time and money than calling a pre-trained API. In return, the model is tuned to the company's own proprietary data, which competitors can't copy. The clues are "very specific predictions" and "proprietary athlete training data": that is exactly where custom models pay off.

**Why the others are wrong:**
- **A. Less expertise, faster**: It is the opposite: custom models need more expertise and take longer than pre-trained APIs.
- **C. Shifts OpEx to CapEx**: Training a model on Google Cloud is still pay-as-you-go spending, so it stays OpEx.
- **D. 100% accurate**: No ML model is ever guaranteed to be 100% accurate.

**Remember:** Pre-trained API = fast and easy, low differentiation. Custom model = more effort, more differentiation.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview)
- [docs.cloud.google.com/architecture/ml-on-gcp-best-practices](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices)
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)

</details>

---

### Exam 4 · Q14

**CallFlow Analytics, a contact center platform, wants to convert a large archive of recorded customer service conversations into written text. After the calls are transcribed, the text will be used for sentiment analysis and reporting. Which pre-trained Google Cloud service should CallFlow Analytics use?**

- A. Vision API
- B. Speech-to-Text API
- C. Cloud Translation API
- D. Cloud SQL

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Speech-to-Text API

**Correct answer: B. Speech-to-Text API**

Speech-to-Text is a pre-trained API that turns audio into written text. Recorded calls are audio, and the goal is transcripts, so it fits directly. The text can then go to the Natural Language API or other tools for sentiment analysis.

**Why the others are wrong:**
- **A. Vision API**: Vision analyzes images, not audio.
- **C. Cloud Translation API**: Translation converts text from one language to another; it can't transcribe audio.
- **D. Cloud SQL**: Cloud SQL is a managed relational database, not an AI service.

**Remember:** Audio → text = Speech-to-Text. Text → audio = Text-to-Speech.

**References:**
- [cloud.google.com/speech-to-text/docs](https://cloud.google.com/speech-to-text/docs)
- [cloud.google.com/vision/docs](https://cloud.google.com/vision/docs)
- [cloud.google.com/translate/docs](https://cloud.google.com/translate/docs)

</details>

---

### Exam 4 · Q17

**FinBridge Analytics is building internal AI assistants for finance, compliance, and customer support teams. The company wants a managed Google Cloud platform where developers can explore foundation models, adapt them using company data, and deploy production-ready AI agents without managing the full infrastructure themselves. Which Google Cloud solution should FinBridge Analytics choose?**

- A. Gemini Enterprise Agent Platform
- B. Compute Engine
- C. Cloud Load Balancing
- D. Google Kubernetes Engine

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Gemini Enterprise Agent Platform

**Correct answer: A. Gemini Enterprise Agent Platform**

Gemini Enterprise Agent Platform (formerly Vertex AI) is Google Cloud's managed AI platform. Developers can explore foundation models, tune or ground them with company data, and build and deploy AI agents without running the infrastructure. The clues "foundation models", "adapt with company data" and "deploy agents" all point to it.

**Why the others are wrong:**
- **B. Compute Engine**: Compute Engine gives raw VMs, so the team would manage everything themselves.
- **C. Cloud Load Balancing**: Load balancing spreads traffic across servers; it isn't an AI development platform.
- **D. Google Kubernetes Engine**: GKE runs containers but would require the team to build and manage the AI stack.

**Remember:** Foundation models + company data + deploy agents → Gemini Enterprise Agent Platform.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [cloud.google.com/model-garden](https://cloud.google.com/model-garden)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime)

</details>

---

### Exam 4 · Q24

**PixelTrail Media is creating a web platform that can analyze customer support content from many formats, including written messages, source code snippets, voice recordings, screenshots, and short videos. The team wants to use Google Cloud’s multimodal foundation model that can understand and combine information across these different input types. Which model should PixelTrail Media use?**

- A. BigQuery
- B. Gemini
- C. Cloud Storage
- D. Cloud SQL

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Gemini

**Correct answer: B. Gemini**

Gemini is Google's multimodal foundation model family. It can understand and reason across text, code, audio, images and video in one model. The clue is "multimodal foundation model" handling many input types.

**Why the others are wrong:**
- **A. BigQuery**: BigQuery is a data warehouse, not a foundation model.
- **C. Cloud Storage**: Cloud Storage stores files; it doesn't understand their content.
- **D. Cloud SQL**: Cloud SQL is a relational database, not an AI model.

**Remember:** Multimodal foundation model from Google → Gemini.

**References:**
- [cloud.google.com/use-cases/multimodal-ai](https://cloud.google.com/use-cases/multimodal-ai)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models)
- [ai.google.dev/gemini-api/docs/models](https://ai.google.dev/gemini-api/docs/models)

</details>

---

### Exam 4 · Q26

**NovaVerse AI is building a mobile app that generates personalized study videos from text prompts. The team needs to train very large foundation models as quickly as possible and wants Google Cloud hardware that is purpose-built for high-performance machine learning workloads. Which Google Cloud hardware components should NovaVerse AI use?**

- A. Standard hard disk drives (HDDs)
- B. GPUs and TPUs
- C. Archival storage nodes
- D. Virtual Private Cloud routers

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. GPUs and TPUs

**Correct answer: B. GPUs and TPUs**

GPUs and TPUs are accelerators built for the heavy math in machine learning. TPUs are Google's custom chips designed specifically for ML, and GPUs are widely used for training large models. The clue is "purpose-built for high-performance machine learning workloads".

**Why the others are wrong:**
- **A. Standard HDDs**: Hard disks are slow storage, not compute for training.
- **C. Archival storage nodes**: Archival storage is for rarely accessed data, not fast training.
- **D. VPC routers**: Routers move network traffic; they don't run ML computations.

**Remember:** Train large models fast → GPUs and TPUs (TPUs are Google's ML-specific chips).

**References:**
- [docs.cloud.google.com/compute/docs/gpus/overview](https://docs.cloud.google.com/compute/docs/gpus/overview)
- [docs.cloud.google.com/tpu/docs/intro-to-tpu](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
- [docs.cloud.google.com/ai-hypercomputer/docs/overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)

</details>

---

### Exam 4 · Q28

**StyleSnapper, a mobile shopping app, wants to build a custom machine learning model that can sort its private catalog photos into categories such as shoes, bags, watches, and jackets. The team already has accurate labeled image examples, but they do not have enough experience to write advanced machine learning training code. Which Google Cloud solution should they use?**

- A. AutoML on Agent Platform
- B. Cloud Storage Coldline
- C. Dataproc
- D. Cloud Interconnect

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. AutoML on Agent Platform

**Correct answer: A. AutoML on Agent Platform**

AutoML trains a custom model on your own labeled data without you writing training code. StyleSnapper has labeled images and custom categories but lacks ML coding experience, which is exactly AutoML's use case. It runs inside Gemini Enterprise Agent Platform (formerly Vertex AI).

**Why the others are wrong:**
- **B. Cloud Storage Coldline**: Coldline is a storage class for rarely accessed data, not an ML tool.
- **C. Dataproc**: Dataproc runs managed Spark and Hadoop clusters for data processing, not no-code model training.
- **D. Cloud Interconnect**: Interconnect is a private network link to Google Cloud, unrelated to ML.

**Remember:** Custom categories + labeled data + no ML coding → AutoML.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-training-overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-training-overview)
- [cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)

</details>

---

### Exam 4 · Q35

**StormMap Analytics, a climate technology company, is building a machine learning model to predict severe storms, floods, and heat waves across several regions. How should StormMap Analytics collect training data to improve prediction accuracy?**

- A. Collect all weather data evenly across all regions
- B. Collect all weather data primarily from high-risk regions
- C. Collect only severe weather data evenly across all regions
- D. Collect only severe weather data primarily from high-risk regions

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Collect all weather data evenly across all regions

**Correct answer: A. Collect all weather data evenly across all regions**

A model learns patterns from its training data, so the data must represent the conditions it will predict for. StormMap predicts across several regions, so it needs data from all of them. It also needs normal weather as well as severe events, so the model can learn what comes before a storm and tell severe from normal.

**Why the others are wrong:**
- **B. All data, mainly from high-risk regions**: The model would be skewed toward those regions and predict poorly elsewhere.
- **C. Only severe data, evenly**: With no normal weather, the model has nothing to compare severe events against.
- **D. Only severe data, high-risk regions**: Both problems at once: biased regions and no normal cases.

**Remember:** Training data must be representative: every region, normal and extreme cases.

**References:**
- [developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets)
- [developers.google.com/machine-learning/crash-course/classification](https://developers.google.com/machine-learning/crash-course/classification)
- [developers.google.com/machine-learning/crash-course/fairness/types-of-bias](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias)

</details>

---

### Exam 4 · Q43

**HealthHive, a telemedicine app, is creating AI features that help users understand symptoms and book care. To keep users confident in the platform, HealthHive defines strict principles so its AI systems are transparent, fair, safe, privacy-preserving, and designed to reduce harmful bias. What practice is HealthHive applying?**

- A. Responsible AI
- B. Data virtualization
- C. Edge computing
- D. Legacy modernization

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Responsible AI

**Correct answer: A. Responsible AI**

Responsible AI means building AI that is fair, transparent, safe, privacy-preserving and accountable. Google publishes its own AI Principles on the same lines. The stem lists exactly those qualities.

**Why the others are wrong:**
- **B. Data virtualization**: This means querying data where it lives without copying it; it isn't about ethics.
- **C. Edge computing**: Edge computing processes data close to where it is created, unrelated to AI principles.
- **D. Legacy modernization**: This means updating old systems, not governing AI behavior.

**Remember:** Fair, transparent, safe, private, low bias → Responsible AI.

**References:**
- [cloud.google.com/responsible-ai](https://cloud.google.com/responsible-ai)
- [developers.google.com/machine-learning/guides/intro-responsible-ai](https://developers.google.com/machine-learning/guides/intro-responsible-ai)
- [docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly](https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly)

</details>

---

### Exam 4 · Q48

**NovaForge Labs, a software company building generative AI tools, plans to run very large model training and inference workloads. The team needs a Google Cloud architecture that combines AI-optimized hardware, open software, popular ML frameworks, and flexible ways to consume compute capacity. What is this Google Cloud differentiator called?**

- A. Multi-cloud architecture
- B. AI Hypercomputer
- C. Serverless data pipeline
- D. Distributed denial-of-service protection

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. AI Hypercomputer

**Correct answer: B. AI Hypercomputer**

AI Hypercomputer is Google Cloud's integrated architecture for AI. It combines AI-optimized hardware (TPUs, GPUs), open software, popular ML frameworks and flexible consumption models for training and serving at scale. The stem lists exactly these parts.

**Why the others are wrong:**
- **A. Multi-cloud architecture**: Multi-cloud means using several cloud providers, not an AI architecture.
- **C. Serverless data pipeline**: That describes services like Dataflow for data processing.
- **D. DDoS protection**: This is a security capability, such as Cloud Armor.

**Remember:** Hardware + open software + ML frameworks + flexible consumption → AI Hypercomputer.

**References:**
- [docs.cloud.google.com/ai-hypercomputer/docs/overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
- [docs.cloud.google.com/ai-hypercomputer/docs/consumption-models](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models)
- [docs.cloud.google.com/docs/ai-ml](https://docs.cloud.google.com/docs/ai-ml)

</details>

---

### Exam 4 · Q50

**Lendora Bank uses a machine learning model to evaluate mortgage applications and decide whether each request should be accepted or rejected. Because the company operates in a heavily regulated industry, its risk and compliance teams must show auditors why the model made a specific decision for each applicant. Which AI concept helps meet this requirement?**

- A. Generative AI
- B. Explainable AI
- C. Unstructured data processing
- D. Multi-cloud networking

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Explainable AI

**Correct answer: B. Explainable AI**

Explainable AI shows which factors drove a model's prediction for each case. In regulated industries like lending, companies must justify decisions to auditors and customers. The clue is "show auditors why the model made a specific decision".

**Why the others are wrong:**
- **A. Generative AI**: Generative AI creates new content; it doesn't explain decisions.
- **C. Unstructured data processing**: This is about handling text, images or audio, not explaining predictions.
- **D. Multi-cloud networking**: This connects multiple clouds and has nothing to do with model decisions.

**Remember:** "Why did the model decide this?" → Explainable AI.

**References:**
- [cloud.google.com/responsible-ai](https://cloud.google.com/responsible-ai)
- [docs.cloud.google.com/bigquery/docs/xai-overview](https://docs.cloud.google.com/bigquery/docs/xai-overview)
- [ibm.com/think/topics/explainable-ai](https://ibm.com/think/topics/explainable-ai)

</details>

---

### Exam 5 · Q1

**PhotoNest, an online image storage app, has thousands of uploaded pictures that need to be automatically categorized by objects, places, and general labels. The team wants to use a Google Cloud service with pre-trained machine learning instead of building and training its own model. Which Google Cloud product or service should PhotoNest use?**

- A. Vision API
- B. BigQuery ML
- C. AutoML Vision
- D. Looker

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Vision API

**Correct answer: A. Vision API**

Vision API is a pre-trained model that labels images out of the box. It detects objects, places, landmarks and general labels with a simple API call. The clue is "pre-trained machine learning instead of building and training its own model", which rules out anything that needs your own training data.

**Why the others are wrong:**
- **B. BigQuery ML**: it trains models with SQL on tabular data in BigQuery, not ready-made image labeling.
- **C. AutoML Vision**: it trains a custom model on your own labeled images, which the team wants to avoid.
- **D. Looker**: it is a BI and dashboard tool, not an image analysis service.

**Remember:** Common labels, no training = pre-trained API (Vision API). Your own custom categories = AutoML.

**References:**
- [docs.cloud.google.com/vision/docs](https://docs.cloud.google.com/vision/docs)
- [docs.cloud.google.com/vision/docs/detect-labels-image-api](https://docs.cloud.google.com/vision/docs/detect-labels-image-api)
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)

</details>

---

### Exam 5 · Q5

**MedSnap Care, a healthcare mobile app, lets users upload photos of visible symptoms so the app can identify possible condition categories and route the case to the right care team. Which technology is most closely related to this capability?**

- A. Cloud Logging
- B. Cloud Profiler
- C. App Engine
- D. Machine learning

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Machine learning

**Correct answer: D. Machine learning**

Recognizing condition categories in symptom photos is image classification. A machine learning model learns from many labeled example images and then classifies new ones, which lets the app route each case to the right team. On Google Cloud this could be the Vision API, AutoML or a custom model, but the technology behind all of them is ML.

**Why the others are wrong:**
- **A. Cloud Logging**: Stores and searches log entries. It doesn't analyze images.
- **B. Cloud Profiler**: Measures CPU and memory use in application code.
- **C. App Engine**: Hosts web applications. It can run the app, but it doesn't classify images.

**Remember:** Recognize, classify or predict from images, text or data → machine learning.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [docs.cloud.google.com/logging/docs/overview](https://docs.cloud.google.com/logging/docs/overview)
- [docs.cloud.google.com/appengine/docs](https://docs.cloud.google.com/appengine/docs)

</details>

---

### Exam 5 · Q11

**PixelPeak Media, a digital content company, is comparing cloud providers for its next innovation program. The team wants access to ready-to-use AI agents, advanced Google first-party models, and a unified AI development platform for building and managing AI solutions. Under which category of Google Cloud’s top differentiators do these capabilities belong?**

- A. Global network infrastructure
- B. World-leading AI
- C. CapEx reduction
- D. Open standards

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. World-leading AI

**Correct answer: B. World-leading AI**

Ready-to-use AI agents, Google's first-party models (such as Gemini) and a unified AI development platform all describe Google Cloud's AI leadership. These are AI capabilities, so they fall under the AI differentiator.

**Why the others are wrong:**
- **A. Global network infrastructure**: it is about Google's private fiber network and global reach, not AI models.
- **C. CapEx reduction**: it is a financial benefit of cloud in general, not a Google differentiator category.
- **D. Open standards**: it is about avoiding lock-in and interoperability, not AI products.

**Remember:** Agents, Gemini models, AI platform = the AI differentiator.

**References:**
- [cloud.google.com/gemini-enterprise](https://cloud.google.com/gemini-enterprise)
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)

</details>

---

### Exam 5 · Q16

**TrailCart, a small grocery delivery app, wants its developers and analysts to quickly explore reusable machine learning resources on Google Cloud without building everything from scratch. How does Google Cloud AI Hub help Google Cloud customers get started with machine learning?**

- A. It serves artificial intelligence models for real-time predictions
- B. It automatically writes complete machine learning model code for users
- C. It automatically collects, cleans, and prepares users’ machine learning datasets
- D. It provides a repository of ready-to-use artificial intelligence and machine learning resources

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. It provides a repository of ready-to-use artificial intelligence and machine learning resources

**Correct answer: D. It provides a repository of ready-to-use artificial intelligence and machine learning resources**

AI Hub was a catalog of reusable AI and ML assets, such as models, notebooks and pipelines. Teams could find something close to what they needed and start from it. The clue is "explore reusable machine learning resources... without building everything from scratch".

**Why the others are wrong:**
- **A. Serves models for real-time predictions**: that is model serving on the AI platform, not a catalog.
- **B. Writes complete model code**: no catalog writes your whole model for you.
- **C. Collects, cleans and prepares datasets**: data preparation is a separate step and tool set.

**Remember:** Hub = repository of reusable resources.

**References:**
- [cloud.google.com/blog/products/ai-machine-learning/introducing-ai-hub-and-kubeflow-pipelines-making-ai-simpler-faster-and-more-useful-for-businesses](https://cloud.google.com/blog/products/ai-machine-learning/introducing-ai-hub-and-kubeflow-pipelines-making-ai-simpler-faster-and-more-useful-for-businesses)
- [cloud.google.com/model-garden](https://cloud.google.com/model-garden)
- [cloud.google.com/products/ai](https://cloud.google.com/products/ai)

**⚠️ Note:** AI Hub is an older product. Its role is now mostly filled by Model Garden in the AI platform. The definition is still correct, so pick the key.

</details>

---

### Exam 5 · Q21

**BrightWave Media wants to analyze campaign clicks, app installs, website visits, and social media engagement data together so it can predict future customer acquisition. How should the company use cloud technology to gain new insights from this data?**

- A. Import the datasets into a custom data warehouse, and then archive older data
- B. Import and selectively archive the datasets in a custom data lake
- C. Keep the datasets separate and make predictions using machine learning
- D. Combine the datasets and make predictions using machine learning

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Combine the datasets and make predictions using machine learning

**Correct answer: D. Combine the datasets and make predictions using machine learning**

Predictions get better when the model can see how clicks, installs, visits and social engagement relate to each other. Combining the data in one place, then training ML on it, reveals these patterns. The clues are "analyze... together" and "predict".

**Why the others are wrong:**
- **A. Custom warehouse, then archive**: archiving older data removes history the model needs, and there is no prediction step.
- **B. Selectively archive in a data lake**: storing and archiving is not analysis or prediction.
- **C. Keep the datasets separate**: silos hide the cross-channel patterns the company is looking for.

**Remember:** New insights = combine the data, then apply ML.

**References:**
- [cloud.google.com/bigquery/docs/bigqueryml-intro](https://cloud.google.com/bigquery/docs/bigqueryml-intro)
- [cloud.google.com/learn/what-is-a-data-warehouse](https://cloud.google.com/learn/what-is-a-data-warehouse)
- [cloud.google.com/learn/what-is-a-data-lake](https://cloud.google.com/learn/what-is-a-data-lake)

</details>

---

### Exam 5 · Q29

**ShopTrail, an online fashion marketplace, wants to use customer browsing history, previous purchases, and product ratings to improve the shopping experience. Which scenario is a good use case for machine learning?**

- A. Grouping data when there are no useful past examples or patterns to learn from
- B. Completing tasks that mainly depend on human judgment, life experience, and intuition
- C. Creating personalized product recommendations for customers
- D. Making final decisions about complex ethical dilemmas

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Creating personalized product recommendations for customers

**Correct answer: C. Creating personalized product recommendations for customers**

ML learns patterns from lots of past data, such as browsing, purchases and ratings, and uses them to predict what each customer will like. Recommendations are a classic ML use case. The clue is the rich historical customer data.

**Why the others are wrong:**
- **A. No useful past examples or patterns**: ML needs data with patterns to learn from.
- **B. Tasks based on human judgment and intuition**: these depend on experience ML doesn't have.
- **D. Final decisions on ethical dilemmas**: these need human accountability, not a model.

**Remember:** Lots of data + patterns + prediction at scale = good ML fit.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [cloud.google.com/use-cases/recommendations](https://cloud.google.com/use-cases/recommendations)
- [docs.cloud.google.com/bigquery/docs/recommendation-overview](https://docs.cloud.google.com/bigquery/docs/recommendation-overview)

</details>

---

### Exam 5 · Q31

**MediScan Analytics is building image-recognition models to help hospitals detect patterns in medical scan images. The team wants to reduce the time required to train these machine learning models on Google Cloud. Which domain-specific hardware is designed for this purpose?**

- A. Bare Metal Solution
- B. Spot VMs
- C. Cloud TPUs
- D. Containers

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Cloud TPUs

**Correct answer: C. Cloud TPUs**

Tensor Processing Units are chips Google designed specifically to speed up machine learning training and inference. The clues are "reduce the time required to train" and "domain-specific hardware".

**Why the others are wrong:**
- **A. Bare Metal Solution**: dedicated physical servers for special workloads, not ML-specific chips.
- **B. Spot VMs**: lower-cost VMs that can be stopped at any time. They are a pricing option, not special hardware.
- **D. Containers**: a way to package software, not hardware.

**Remember:** Hardware built for ML = TPU.

**References:**
- [docs.cloud.google.com/tpu/docs/intro-to-tpu](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
- [cloud.google.com/tpu](https://cloud.google.com/tpu)
- [docs.cloud.google.com/compute/docs/instances/spot](https://docs.cloud.google.com/compute/docs/instances/spot)

</details>

---

### Exam 5 · Q32

**HelpNest, a customer service web platform, wants to introduce a system that can read support tickets, decide the next best action, trigger approved workflows such as refunds or account updates, and close routine issues without a human agent. Which technology best describes this capability?**

- A. Infrastructure as a Service (IaaS)
- B. Legacy on-premises computing
- C. Agentic AI
- D. Open source software

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Agentic AI

**Correct answer: C. Agentic AI**

Agentic AI systems don't just answer questions. They understand a goal, decide on next steps and take actions through tools and workflows. Here the system reads tickets, picks the next action, triggers refunds or updates, and closes issues on its own. The clue is "decide the next best action" and "trigger approved workflows".

**Why the others are wrong:**
- **A. IaaS**: it is a cloud service model for renting compute, storage and networking.
- **B. Legacy on-premises computing**: it describes where systems run, not an AI capability.
- **D. Open source software**: it describes how software is licensed, not what it does.

**Remember:** AI that plans and takes actions = agentic AI.

**References:**
- [cloud.google.com/discover/what-is-agentic-ai](https://cloud.google.com/discover/what-is-agentic-ai)
- [cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [cloud.google.com/learn/what-is-iaas](https://cloud.google.com/learn/what-is-iaas)

</details>

---

### Exam 5 · Q34

**ModelForge Health, a medical research analytics company, wants to train very large machine learning models for drug discovery. The team needs Google Cloud infrastructure that is purpose-built for AI workloads and combines high-performance hardware, open software, ML frameworks, and flexible ways to consume compute capacity. Which Google Cloud differentiator should the company use?**

- A. Domain Name Service (DNS)
- B. AI Hypercomputer
- C. Software as a Service (SaaS)
- D. Edge locations

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. AI Hypercomputer

**Correct answer: B. AI Hypercomputer**

AI Hypercomputer is Google Cloud's integrated supercomputing architecture for AI. It combines performance-optimized hardware (TPUs and GPUs), open software and ML frameworks, and flexible consumption models. The stem describes exactly these parts for training very large models.

**Why the others are wrong:**
- **A. DNS**: it translates domain names into IP addresses.
- **C. SaaS**: it delivers finished applications, not AI training infrastructure.
- **D. Edge locations**: they cache and deliver content close to users, not train large models.

**Remember:** Hardware + open software + flexible consumption for AI = AI Hypercomputer.

**References:**
- [docs.cloud.google.com/ai-hypercomputer/docs/overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
- [cloud.google.com/ai-infrastructure](https://cloud.google.com/ai-infrastructure)
- [docs.cloud.google.com/ai-hypercomputer/docs/consumption-models](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models)

</details>

---

### Exam 5 · Q36

**BrightCart, an online retail platform, already uses cloud infrastructure to scale its website during seasonal traffic spikes. The leadership team now wants a technology that can independently plan, reason, and carry out multi-step business tasks such as researching customer segments, preparing sales outreach, and coordinating follow-up actions with minimal human direction. What is this concept called?**

- A. Agentic AI
- B. Virtual Machines
- C. Hybrid cloud
- D. Domain Name Service (DNS)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Agentic AI

**Correct answer: A. Agentic AI**

Agentic AI can plan, reason and complete multi-step tasks toward a goal with little human direction. Researching segments, drafting outreach and coordinating follow-ups is a chain of actions an AI agent can carry out. The clue is "independently plan, reason, and carry out multi-step business tasks".

**Why the others are wrong:**
- **B. Virtual Machines**: they are compute resources, not decision-making systems.
- **C. Hybrid cloud**: it combines on-premises and public cloud, an infrastructure model.
- **D. DNS**: it resolves domain names to IP addresses.

**Remember:** Plan + reason + act on multi-step tasks = agentic AI.

**References:**
- [cloud.google.com/discover/what-is-agentic-ai](https://cloud.google.com/discover/what-is-agentic-ai)
- [cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)

</details>

---

### Exam 5 · Q39

**StreamForge, a video creation app, is launching a generative AI feature that will train and serve large models at scale. Its engineering team needs an integrated Google Cloud architecture that combines purpose-built accelerators such as GPUs and TPUs with open software, ML frameworks, and flexible consumption options. Which Google Cloud offering best fits this requirement?**

- A. AI Hypercomputer
- B. Cloud Storage Coldline
- C. Virtual Private Cloud (VPC)
- D. Google Workspace

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. AI Hypercomputer

**Correct answer: A. AI Hypercomputer**

AI Hypercomputer brings together GPUs and TPUs, open software, ML frameworks and flexible consumption options in one architecture for training and serving large AI models. The stem lists these exact components.

**Why the others are wrong:**
- **B. Cloud Storage Coldline**: a low-cost storage class for rarely accessed data.
- **C. VPC**: it provides private networking for cloud resources, not AI compute.
- **D. Google Workspace**: productivity apps such as Gmail and Docs.

**Remember:** GPUs/TPUs + open software + flexible consumption = AI Hypercomputer.

**References:**
- [docs.cloud.google.com/ai-hypercomputer/docs/overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)
- [cloud.google.com/ai-infrastructure](https://cloud.google.com/ai-infrastructure)
- [docs.cloud.google.com/compute/docs/gpus](https://docs.cloud.google.com/compute/docs/gpus)

</details>

---

### Exam 5 · Q41

**BrightCart, an online grocery app, has hired a small group of data scientists and software engineers. The team is building its own advanced machine learning model by writing custom training code in Gemini Enterprise Agent Platform notebooks. Which service should BrightCart use to train this model?**

- A. Custom training
- B. AutoML
- C. Compute Engine
- D. Prebuilt APIs

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Custom training

**Correct answer: A. Custom training**

Custom training lets data scientists write their own training code and run it on the AI platform (formerly Vertex AI). It gives full control over the model. The clues are "data scientists and software engineers", "advanced" model and "writing custom training code".

**Why the others are wrong:**
- **B. AutoML**: it trains models with little or no code, for teams without deep ML skills.
- **C. Compute Engine**: you could run code on VMs, but it isn't the managed ML training service and adds work.
- **D. Prebuilt APIs**: these are pre-trained models; you don't train them yourself.

**Remember:** ML experts + own code = custom training. No code = AutoML. No training = prebuilt APIs.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/training-guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/training-guide)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning)

</details>

---

### Exam 5 · Q46

**BrightCart, a small retail mobile app, wants to add image labeling and text sentiment detection using Google Cloud AI services. The team wants these capabilities without building machine learning models from scratch or hiring a dedicated machine learning team. How do ready-to-use Google Cloud AI and machine learning APIs make AI and ML easier for customers to adopt?**

- A. They don't require data science expertise.
- B. They don't require data input and validation.
- C. They require fewer security permissions.
- D. They all require custom training models.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. They don't require data science expertise.

**Correct answer: A. They don't require data science expertise.**

Pre-trained APIs, such as the Vision API and Natural Language API, use models Google has already built and trained. A developer sends an image or text to the API and gets labels or sentiment back. Nobody has to collect training data, design a model or tune it, so no data scientists or ML engineers are needed. The clue is "without building machine learning models from scratch or hiring a dedicated machine learning team".

**Why the others are wrong:**
- **B. Don't require data input and validation**: You still send the images and text to analyze, and you should validate them.
- **C. Fewer security permissions**: Access is still controlled with IAM. That isn't the adoption benefit.
- **D. All require custom training**: The opposite. They are pre-trained.

**Remember:** Pre-trained API = no model building, no data science team. A developer just calls it.

**References:**
- [cloud.google.com/ai/apis](https://cloud.google.com/ai/apis)
- [cloud.google.com/vision/docs](https://cloud.google.com/vision/docs)
- [cloud.google.com/natural-language](https://cloud.google.com/natural-language)

</details>

---

### Exam 6 · Q2

**RideGrid Logistics wants to quickly add an AI assistant to help warehouse employees check shipment status, summarize delay reasons, and answer common operations questions. Instead of building and training custom AI models from the beginning, the company plans to use pre-built Google Cloud AI agents and templates. What is the main business tradeoff of this approach?**

- A. It provides faster implementation speed but may offer less specialized business differentiation.
- B. It provides maximum business differentiation but takes years to implement.
- C. It requires a massive team of expert data scientists to maintain.
- D. It requires shifting all cloud costs to a capital expenditure (CapEx) model.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. It provides faster implementation speed but may offer less specialized business differentiation.

**Correct answer: A. It provides faster implementation speed but may offer less specialized business differentiation.**

Pre-built agents and templates let a company deliver value quickly, because the hard work of building and training models is already done. The tradeoff is that competitors can use the same building blocks, so the result is less unique to the business. The stem's clue is "quickly" and "instead of building and training custom AI models."

**Why the others are wrong:**
- **B. Maximum differentiation, takes years**: That describes the opposite approach, building custom models from scratch.
- **C. Massive team of data scientists**: Pre-built solutions exist precisely to reduce the need for deep ML expertise.
- **D. Shift to CapEx**: Cloud AI services are usually paid as operating expense (OpEx), not upfront capital spending.

**Remember:** Pre-built = fast, less differentiation. Custom = more effort, more differentiation.

**References:**
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden)

</details>

---

### Exam 6 · Q3

**StreamlyPay is building a customer-support chatbot for its mobile wallet app. The team wants to compare and use different foundation models without being restricted to a single provider. They want access to Google models, open models, and partner models from other companies. Does Gemini Enterprise Agent Platform meet this requirement?**

- A. No, it only permits customers to use Google-owned proprietary models.
- B. Yes, it provides access to a broad selection of foundation models from Google, open-model communities, and third-party partners.
- C. No, it is designed to support only third-party foundation models.
- D. Yes, but it is limited to open models only.

<details><summary>Answer &amp; explanation</summary>

**Correct:** B. Yes, it provides access to a broad selection of foundation models from Google, open-model communities, and third-party partners.

**Correct answer: B. Yes, it provides access to a broad selection of foundation models from Google, open-model communities, and third-party partners.**

Gemini Enterprise Agent Platform (formerly Vertex AI) offers a catalog of models (Model Garden) that includes Google models such as Gemini, open models, and partner models from other companies. This lets teams compare models and pick the best fit without being locked into one provider. The stem asks for exactly that mix: Google, open, and partner models.

**Why the others are wrong:**
- **A. Only Google-owned models**: The platform deliberately includes non-Google models.
- **C. Only third-party models**: Google's own models, such as Gemini, are a core part of the catalog.
- **D. Limited to open models only**: Open models are one part of the choice, not the only one.

**Remember:** Model choice on Google Cloud = Google + open + partner models in one platform.

**References:**
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [cloud.google.com/model-garden](https://cloud.google.com/model-garden)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models)

</details>

---

### Exam 6 · Q5

**ShopEaseNow, an online shopping app, wants to improve its customer support operations by using a purpose-built Google Cloud AI solution. The company wants to help support agents resolve issues faster, automate common customer interactions, and provide more personalized support experiences. Which Google Cloud AI solution should ShopEaseNow use?**

- A. Text-to-Speech API
- B. Cloud Talent Solution
- C. Document AI
- D. Contact Center AI

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Contact Center AI

**Correct answer: D. Contact Center AI**

Contact Center AI is Google Cloud's purpose-built solution for customer service. It uses virtual agents to automate common interactions, assists human agents with suggestions in real time, and gives insights from conversations. The stem's clues are "customer support operations," "help support agents resolve issues faster," and "automate common customer interactions."

**Why the others are wrong:**
- **A. Text-to-Speech API**: It turns text into spoken audio. It is a building block, not a full support solution.
- **B. Cloud Talent Solution**: It improves job search and recruiting, not customer support.
- **C. Document AI**: It extracts data from documents such as forms and invoices.

**Remember:** Customer support at scale → Contact Center AI.

**References:**
- [cloud.google.com/solutions/contact-center-ai-platform](https://cloud.google.com/solutions/contact-center-ai-platform)
- [docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist)
- [docs.cloud.google.com/text-to-speech/docs](https://docs.cloud.google.com/text-to-speech/docs)

</details>

---

### Exam 6 · Q9

**GardenLens, a plant care mobile app, wants its data science team to build and train custom machine learning models that can identify plant diseases from images. The team wants to use an open source machine learning library that provides a flexible ecosystem of tools, libraries, and community resources. Which product or solution should GardenLens use?**

- A. Cloud Run functions
- B. Apache Beam
- C. Dataflow
- D. TensorFlow

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. TensorFlow

**Correct answer: D. TensorFlow**

TensorFlow is an open source machine learning library, originally created by Google, with a large ecosystem of tools, libraries, and community resources. Data scientists use it to build and train custom models, such as image classifiers for plant diseases. The clues are "open source machine learning library" and "build and train custom models."

**Why the others are wrong:**
- **A. Cloud Run functions**: A serverless service for running small pieces of code in response to events, not an ML library.
- **B. Apache Beam**: An open source model for data processing pipelines, not for training ML models.
- **C. Dataflow**: Google's managed service that runs Apache Beam pipelines for batch and streaming data, not an ML library.

**Remember:** Open source ML library → TensorFlow. Data pipelines → Apache Beam / Dataflow.

**References:**
- [tensorflow.org](https://tensorflow.org)
- [tensorflow.org/learn](https://tensorflow.org/learn)
- [docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model)

</details>

---

### Exam 6 · Q14

**CareKart, a healthcare analytics company, is helping its operations managers understand appointment bookings, cancellations, and patient satisfaction scores. The managers want to compare past performance using dashboards, while the data science team wants systems that can learn from data and automatically predict future no-show risk. Which statement best describes the fundamental difference between machine learning and traditional business intelligence?**

- A. Business intelligence predicts future trends using algorithms, while machine learning only visualizes past historical data.
- B. Business intelligence relies on unstructured data like images, while machine learning only works with structured relational tables.
- C. Business intelligence focuses on analyzing historical data to create reports and dashboards, while machine learning learns from data to make automated predictions or decisions.
- D. Business intelligence requires TPUs to operate, while machine learning only runs on standard CPUs.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Business intelligence focuses on analyzing historical data to create reports and dashboards, while machine learning learns from data to make automated predictions or decisions.

**Correct answer: C. Business intelligence focuses on analyzing historical data to create reports and dashboards, while machine learning learns from data to make automated predictions or decisions.**

BI looks backward. It summarizes what already happened in reports and dashboards, like the managers comparing past performance. ML learns patterns from data and applies them to new cases, like predicting no-show risk. The stem describes both uses side by side.

**Why the others are wrong:**
- **A. BI predicts, ML visualizes the past**: This swaps the two roles.
- **B. BI uses unstructured data, ML only structured**: BI usually works on structured data, and ML can handle images, text, and audio.
- **D. BI needs TPUs, ML only CPUs**: TPUs are hardware for accelerating ML, not BI, and ML is not limited to CPUs.

**Remember:** BI = dashboards about the past. ML = learns from data to predict and decide.

**References:**
- [cloud.google.com/learn/what-is-business-intelligence](https://cloud.google.com/learn/what-is-business-intelligence)
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)

</details>

---

### Exam 6 · Q17

**MediLedger Clinics has several hundred scanned patient intake forms and needs to find important details such as appointment dates, patient names, and specific medical keywords. The team wants to use Google Cloud APIs to process these files instead of manually reading every scan. Why should MediLedger Clinics use application programming interfaces APIs?**

- A. To replace the scanned forms with a customer feedback questionnaire
- B. To stream the document data continuously and encrypt words that do not match
- C. To create searchable digital versions of the scanned forms and find important information
- D. To convert the documents into unstructured data

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. To create searchable digital versions of the scanned forms and find important information

**Correct answer: C. To create searchable digital versions of the scanned forms and find important information**

Google Cloud APIs such as the Vision API (text detection) and Document AI can read scanned documents, turn the images into machine-readable text, and extract key fields like names and dates. This removes the need to read every scan by hand. The clues are "scanned patient intake forms" and "find important details."

**Why the others are wrong:**
- **A. Replace forms with a questionnaire**: This changes the business process. It does not process the existing scans.
- **B. Stream data and encrypt non-matching words**: This is not what document-processing APIs do and does not help find information.
- **D. Convert to unstructured data**: Scans are already unstructured. The goal is to turn them into searchable, structured information.

**Remember:** Scanned forms → APIs make them searchable and extract key fields.

**References:**
- [docs.cloud.google.com/document-ai/docs/overview](https://docs.cloud.google.com/document-ai/docs/overview)
- [docs.cloud.google.com/vision/docs/ocr](https://docs.cloud.google.com/vision/docs/ocr)
- [docs.cloud.google.com/document-ai/docs/extracting-overview](https://docs.cloud.google.com/document-ai/docs/extracting-overview)

</details>

---

### Exam 6 · Q18

**FitStyle, a clothing recommendation website, wants to use its full history of browsing behavior, purchases, ratings, and search activity to show personalized product suggestions. The company wants the suggestions to become more accurate as new user data is collected. Which method should FitStyle use?**

- A. Data automation
- B. Trends analysis
- C. Machine learning
- D. Multiple regression

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Machine learning

**Correct answer: C. Machine learning**

Machine learning finds patterns in historical data and keeps improving as new data arrives. A recommendation system that uses browsing, purchases, ratings, and searches, and gets more accurate over time, is a classic ML use case. The key clue is "become more accurate as new user data is collected."

**Why the others are wrong:**
- **A. Data automation**: Automating data tasks moves or processes data but does not learn to predict preferences.
- **B. Trends analysis**: This describes past patterns and does not personalize suggestions for each user.
- **D. Multiple regression**: A single statistical technique for predicting a number. It is not the broad, self-improving approach the stem describes.

**Remember:** Learns and improves as data grows → machine learning.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course)
- [cloud.google.com/discover/what-is-predictive-analytics](https://cloud.google.com/discover/what-is-predictive-analytics)

**⚠️ Note:** Multiple regression is itself a statistical/ML technique, so D is not strictly wrong. "Machine learning" is the broader and best answer because the system must keep improving with new data. Pick the keyed answer on this exam.

</details>

---

### Exam 6 · Q24

**TravelVista, a photo-sharing app, receives 18,000 travel photos every week from its users. The team wants to quickly detect famous places, common items, and readable text in those images without training its own machine learning model. Which Google Cloud service should TravelVista use?**

- A. Vision API
- B. Gemini Enterprise Agent Platform
- C. Cloud Translation API
- D. BigQuery ML

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Vision API

**Correct answer: A. Vision API**

The Vision API is a pre-trained Google Cloud service that analyzes images. It can detect landmarks, label common objects, and read text (OCR) without the customer training any model. The clues are "famous places, common items, and readable text in those images" and "without training its own machine learning model."

**Why the others are wrong:**
- **B. Gemini Enterprise Agent Platform**: This is the full platform for building, training, and deploying models and agents. It is more than needed for a ready-made image task.
- **C. Cloud Translation API**: It translates text between languages. It does not analyze images.
- **D. BigQuery ML**: It builds models with SQL on data in BigQuery, not image recognition out of the box.

**Remember:** Generic photo labels, landmarks, text in images → Vision API.

**References:**
- [cloud.google.com/vision/docs](https://cloud.google.com/vision/docs)
- [cloud.google.com/vision/docs/ocr](https://cloud.google.com/vision/docs/ocr)
- [cloud.google.com/bigquery/docs/bqml-introduction](https://cloud.google.com/bigquery/docs/bqml-introduction)

</details>

---

### Exam 6 · Q26

**FarmSight AI is training a machine learning model to predict crop disease risk from field images and sensor readings. The team wants to improve how accurately the model makes predictions on new farm data. What could help improve the prediction accuracy of the model?**

- A. More storage capacity
- B. Higher network bandwidth
- C. More training data
- D. Faster CPU processors

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. More training data

**Correct answer: C. More training data**

A machine learning model learns patterns from its training data. More relevant, good-quality, representative data usually helps the model generalize better and make more accurate predictions on new data. The clue is "improve how accurately the model makes predictions."

**Why the others are wrong:**
- **A. More storage capacity**: Storage holds data but does not by itself make the model smarter.
- **B. Higher network bandwidth**: Faster data transfer does not change what the model learns.
- **D. Faster CPU processors**: Faster hardware can speed up training, but it does not improve accuracy on its own.

**Remember:** Better accuracy ← more (and better) training data, not more hardware.

**References:**
- [cloud.google.com/learn/what-is-machine-learning](https://cloud.google.com/learn/what-is-machine-learning)
- [developers.google.com/machine-learning/crash-course/overfitting/data-characteristics](https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics)
- [developers.google.com/machine-learning/guides/text-classification/step-1](https://developers.google.com/machine-learning/guides/text-classification/step-1)

</details>

---

### Exam 6 · Q30

**FitBuddy, a wellness app company, has finished building and testing a custom AI agent that can answer member questions about workout plans and nutrition programs. The team now wants to call the agent from its existing Android, iOS, and web applications using code. Which interface should the team use?**

- A. Agent Platform API
- B. Billing Export API
- C. Cloud Storage API
- D. Identity and Access Management (IAM)

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. Agent Platform API

**Correct answer: A. Agent Platform API**

Once an agent is built and tested on Gemini Enterprise Agent Platform, applications call it programmatically through the platform's API. Android, iOS, and web apps send requests to the API and receive the agent's responses. The clues are "call the agent from its existing... applications using code."

**Why the others are wrong:**
- **B. Billing Export API**: Billing export sends cost data to BigQuery for analysis. It has nothing to do with calling an agent.
- **C. Cloud Storage API**: This stores and retrieves objects such as files. It does not run AI agents.
- **D. IAM**: IAM controls who can access resources. It secures the call but is not the interface for calling the agent.

**Remember:** Build agents without code → Agent Studio. Call agents from your apps → Agent Platform API.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/apis](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)
- [cloud.google.com/iam/docs/overview](https://cloud.google.com/iam/docs/overview)

</details>

---

### Exam 6 · Q33

**BrightAxle Components makes small metal brackets for electric scooters. The team has thousands of camera images from the inspection station, and each image is already labeled as acceptable or faulty. They want to create a simple model that can identify faulty brackets on the assembly line, but they do not have employees with machine learning or data science experience. Which Google Cloud solution should they use?**

- A. Pre-trained APIs
- B. Document AI
- C. AutoML
- D. Discovery AI for Retail

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. AutoML

**Correct answer: C. AutoML**

AutoML lets teams train custom models on their own labeled data without writing ML code or needing data science skills. BrightAxle has thousands of images already labeled "acceptable" or "faulty," and its own specific product, so it needs a custom model built the easy way. The clues are "labeled," "simple model," and "no ML or data science experience."

**Why the others are wrong:**
- **A. Pre-trained APIs**: These recognize general objects. They do not know what a faulty bracket from this factory looks like.
- **B. Document AI**: This extracts data from documents like forms and invoices, not product images.
- **D. Discovery AI for Retail**: This improves product search and recommendations for retailers, not defect detection.

**Remember:** Labeled data + your own categories + no ML coders → AutoML.

**References:**
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training)
- [cloud.google.com/document-ai/docs/overview](https://cloud.google.com/document-ai/docs/overview)

</details>

---

### Exam 6 · Q34

**MedRoute Health, a mobile appointment-booking app, is training its product team on cloud technology concepts. The team wants a simple definition of artificial intelligence before deciding whether to add features such as image understanding, language understanding, and automated recommendations. Which definition best describes artificial intelligence?**

- A. Any system that receives data continuously in real time
- B. Any system that automatically organizes data into a structured format
- C. Any system that uses advanced analytics only to create predictions
- D. Any system that can perform tasks that normally require human cognition

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Any system that can perform tasks that normally require human cognition

**Correct answer: D. Any system that can perform tasks that normally require human cognition**

Artificial intelligence is the broad field of making computers do things that normally need human thinking, such as understanding images or language, reasoning, and making recommendations. Machine learning is one way to build AI. The stem's examples (image understanding, language understanding, recommendations) are all cognitive tasks.

**Why the others are wrong:**
- **A. Receives data continuously in real time**: This describes streaming data, not AI.
- **B. Organizes data into a structured format**: This describes data processing or transformation, not intelligence.
- **C. Uses advanced analytics only to create predictions**: Prediction is one AI use, but AI is broader than predictive analytics.

**Remember:** AI = tasks that need human cognition. ML = learning from data to predict and decide.

**References:**
- [cloud.google.com/learn/what-is-artificial-intelligence](https://cloud.google.com/learn/what-is-artificial-intelligence)
- [cloud.google.com/learn/artificial-intelligence-vs-machine-learning](https://cloud.google.com/learn/artificial-intelligence-vs-machine-learning)
- [cloud.google.com/discover/deep-learning-vs-machine-learning](https://cloud.google.com/discover/deep-learning-vs-machine-learning)

</details>

---

### Exam 6 · Q36

**StayNest, a short-term rental website, stores booking history and property details in BigQuery. The company wants to predict which listings will receive the highest demand during the next holiday season. The database administrators are comfortable with SQL, but the company does not have data scientists or machine learning engineers. What should StayNest do?**

- A. Use custom training in Gemini Enterprise Agent Platform with TensorFlow.
- B. Add pre-trained APIs to the rental application.
- C. Use BigQuery ML to build models with SQL.
- D. Create a model with AutoML by using labeled training data.

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Use BigQuery ML to build models with SQL.

**Correct answer: C. Use BigQuery ML to build models with SQL.**

BigQuery ML lets people who know SQL create and run machine learning models directly where the data already lives, in BigQuery. No data movement and no ML coding are needed. The clues are "stores... in BigQuery," "comfortable with SQL," and "no data scientists."

**Why the others are wrong:**
- **A. Custom training with TensorFlow**: This needs ML engineers who write code, which StayNest does not have.
- **B. Pre-trained APIs**: These handle generic tasks such as vision or translation. They cannot forecast demand from StayNest's own booking data.
- **D. AutoML with labeled data**: AutoML is also low-code, but BigQuery ML is the more direct fit when the data is in BigQuery and the team speaks SQL.

**Remember:** SQL analysts + data in BigQuery → BigQuery ML.

**References:**
- [docs.cloud.google.com/bigquery/docs/bqml-introduction](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)
- [docs.cloud.google.com/bigquery/docs/create-machine-learning-model](https://docs.cloud.google.com/bigquery/docs/create-machine-learning-model)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/overview)

</details>

---

### Exam 6 · Q37

**StyleNest Market is preparing to launch its online fashion catalog in many regions. The company needs to automatically translate English product descriptions and help pages into 18 different languages for its international storefronts. Which Google Cloud service provides this pre-trained translation capability?**

- A. Vision API
- B. Speech-to-Text API
- C. Cloud Translation API
- D. BigQuery ML

<details><summary>Answer &amp; explanation</summary>

**Correct:** C. Cloud Translation API

**Correct answer: C. Cloud Translation API**

The Cloud Translation API is a pre-trained service that translates text between many languages. StyleNest can send English product descriptions and help pages to the API and get versions in each target language automatically. The clue is "translate English product descriptions... into 18 different languages."

**Why the others are wrong:**
- **A. Vision API**: It analyzes images, such as objects, landmarks, and text in photos. It does not translate.
- **B. Speech-to-Text API**: It converts spoken audio into text. The content here is already written text.
- **D. BigQuery ML**: It builds custom ML models with SQL. It is not a ready-made translation service.

**Remember:** Audio → Speech-to-Text. Languages → Translation. Text topics and sentiment → Natural Language.

**References:**
- [cloud.google.com/translate](https://cloud.google.com/translate)
- [docs.cloud.google.com/translate/docs](https://docs.cloud.google.com/translate/docs)
- [docs.cloud.google.com/vision/docs](https://docs.cloud.google.com/vision/docs)

</details>

---

### Exam 6 · Q41

**FitPulse Analytics is building an AI feature that can predict user workout progress from historical activity data. The data science team wants a managed Google Cloud platform that supports the complete machine learning lifecycle, including preparing data, training custom models, evaluating them, deploying them, and managing them. Which Google Cloud product or service should FitPulse Analytics use?**

- A. Dataproc
- B. Compute Engine
- C. Recommendations AI
- D. Gemini Enterprise Agent Platform

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Gemini Enterprise Agent Platform

**Correct answer: D. Gemini Enterprise Agent Platform**

Gemini Enterprise Agent Platform (formerly Vertex AI) is Google Cloud's unified, managed platform for the whole ML lifecycle: preparing data, training custom models, evaluating, deploying, and managing them. It also hosts foundation models and agents. The clue is "supports the complete machine learning lifecycle."

**Why the others are wrong:**
- **A. Dataproc**: A managed service for Apache Spark and Hadoop data processing, not a full ML lifecycle platform.
- **B. Compute Engine**: Raw virtual machines. The team would have to build and manage every ML tool itself.
- **C. Recommendations AI**: A specialized product for retail recommendations, not a general platform for custom models.

**Remember:** Full managed ML lifecycle, foundation models, agents → Gemini Enterprise Agent Platform.

**References:**
- [cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview)

</details>

---

### Exam 6 · Q45

**PolicyPilot, an insurance technology company, wants to launch several enterprise AI features, including claim summarization, support response drafting, and document classification. The team wants to avoid building a large model from scratch and instead start from a broadly trained model that can be adapted to its business needs. What is a primary strategic advantage of using foundation models for these AI initiatives?**

- A. They provide a powerful, pre-trained starting point that can be fine-tuned, significantly reducing development time.
- B. They remove the need for organizations to apply governance or security controls to their own data.
- C. They make sure the organization never needs to pay for compute resources.
- D. They guarantee that every generated response will be factually correct without human review.

<details><summary>Answer &amp; explanation</summary>

**Correct:** A. They provide a powerful, pre-trained starting point that can be fine-tuned, significantly reducing development time.

**Correct answer: A. They provide a powerful, pre-trained starting point that can be fine-tuned, significantly reducing development time.**

Foundation models are large models trained on broad data. Companies can adapt them to their own needs through prompting, tuning, or grounding, instead of building a model from scratch. That saves time and cost across many use cases, such as summarizing, drafting, and classifying. The clue is "start from a broadly trained model that can be adapted."

**Why the others are wrong:**
- **B. Remove the need for governance or security**: Organizations must still govern and protect their data when using any AI model.
- **C. Never pay for compute**: Using and tuning models still consumes paid compute.
- **D. Guarantee factually correct responses**: Foundation models can hallucinate. Human review and grounding are still needed.

**Remember:** Foundation models = pre-trained start, fine-tune, save time, still need review.

**References:**
- [cloud.google.com/discover/what-are-foundation-models](https://cloud.google.com/discover/what-are-foundation-models)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)
- [docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning)

</details>

---

### Exam 6 · Q47

**ChatPath Support, a customer service analytics company, stores thousands of written chat transcripts between shoppers and support agents. The business team wants an automated way to analyze the text and discover the main subjects customers mention most often, such as delivery delays, refunds, product quality, or account issues. Which Google Cloud service should they use?**

- A. Vision API
- B. Speech-to-Text API
- C. Cloud Translation API
- D. Natural Language API

<details><summary>Answer &amp; explanation</summary>

**Correct:** D. Natural Language API

**Correct answer: D. Natural Language API**

The Natural Language API is a pre-trained service that analyzes written text. It can identify entities, classify content into topics, and detect sentiment. That lets ChatPath find the main subjects customers mention, such as refunds or delivery delays. The clues are "written chat transcripts" and "discover the main subjects."

**Why the others are wrong:**
- **A. Vision API**: It analyzes images, not written conversations.
- **B. Speech-to-Text API**: It turns audio into text. The transcripts are already written.
- **C. Cloud Translation API**: It translates between languages but does not find topics.

**Remember:** Text topics, entities, sentiment → Natural Language API.

**References:**
- [cloud.google.com/natural-language/docs](https://cloud.google.com/natural-language/docs)
- [cloud.google.com/speech-to-text/docs](https://cloud.google.com/speech-to-text/docs)
- [cloud.google.com/translate/docs](https://cloud.google.com/translate/docs)

</details>

---
