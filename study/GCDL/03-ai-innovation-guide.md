# Domain 3 Study Guide — Innovating with Google Cloud Artificial Intelligence

> Condensed from the 56-question bank in [`03-ai-innovation.md`](03-ai-innovation.md). Citations look like (Exam N · QM). The reasoning combines our own analysis with the exam-prep author's per-option explanations. Many scenarios repeat with new company names (Vision API for photo labels, BigQuery ML for SQL analysts, AutoML for labeled images with no ML staff, AI Hypercomputer, agentic AI), so look for paired citations. Items marked "see ⚠️" have a shaky key, discussed at the end.

---

## 1. AI and ML fundamentals and where they add business value

### Key facts
- **Artificial intelligence (AI)** is any system that can perform tasks that normally require **human cognition**: seeing, understanding language, reasoning, recommending (Exam 6 · Q34).
- AI is the broad field. **Machine learning** is one part of it, **deep learning** is a part of ML, and **generative AI** is one area inside that. "Uses analytics only to make predictions" is too narrow to define AI (Exam 6 · Q34), (Exam 3 · Q24).
- **Machine learning (ML)** is the subset of AI where a system **learns patterns from data** instead of following hand-written rules. Classifying symptom photos into condition categories is an ML capability, not a logging or hosting product (Exam 5 · Q5, see ⚠️).
- ML **improves as more data arrives**. Personalized suggestions that should get more accurate over time point to ML, not to static trend analysis or one-off regression (Exam 6 · Q18), (Exam 5 · Q29).
- **ML vs business intelligence (BI):** BI looks at **historical data** through reports and dashboards (what happened). ML **learns from data** to make **automated predictions or decisions** (what will happen, what to do) (Exam 6 · Q14).
- **Kinds of analytics:** **descriptive analytics** summarizes what already happened (reports, dashboards, BI) (Exam 3 · Q3). **Predictive analytics** uses historical and current data to forecast outcomes, such as churn (Exam 3 · Q40), (Exam 2 · Q29). Neither one creates content (that's gen AI) or takes actions (that's agentic AI).
- ML unlocks value from **unstructured data** such as audio, images, video and free text. Detecting caller sentiment from support-call recordings is the classic example. Spreadsheet records, purchase histories and payment logs are structured (Exam 1 · Q37).
- **Predicting churn** = train a model on the demographics and behavior of customers who already left, then score current customers. Dashboards, surveys and last year's feedback report only describe the past (Exam 2 · Q29).
- **Combine data sources** before predicting. Clicks, installs, web visits and social data analyzed together give better predictions than separate silos or archived data (Exam 5 · Q21).
- Google Cloud offers **AI tools for every skill level**: ready-made APIs for developers, SQL-based ML for analysts, AutoML for people without ML coding skills, and full custom training for data scientists (Exam 1 · Q2).
- Common ML problem types: **classification** (which category?), **regression/forecasting** (what number?), **clustering** (which items are similar?), **recommendation** and **anomaly detection** (Exam 3 · Q24).
- **Supervised learning** learns from **labeled examples**, such as product photos tagged "shoes" or "bags" (Exam 4 · Q28). **Unsupervised learning** finds groupings in unlabeled data, but even it needs real patterns in the data to find (Exam 5 · Q29).

### Good and bad uses of ML

| Scenario | ML fit? | Source |
|---|---|---|
| Personalized product recommendations from browsing, purchases, ratings | ✅ | (Exam 5 · Q29), (Exam 6 · Q18) |
| Predict which active customers will leave | ✅ | (Exam 2 · Q29) |
| Sentiment from call-center audio | ✅ (unstructured) | (Exam 1 · Q37) |
| Grouping data with no useful past examples or patterns | ❌ Nothing to learn from | (Exam 5 · Q29) |
| Tasks that mainly depend on human judgment, life experience, intuition | ❌ ML can support, humans decide | (Exam 5 · Q29) |
| Final decisions on complex ethical dilemmas | ❌ Keep humans accountable | (Exam 5 · Q29) |

### Decision rules
- "Learns from data", "predicts", "gets better with more data", "automated decisions" → **machine learning** (Exam 6 · Q14), (Exam 6 · Q18).
- "Dashboards", "reports", "compare past performance" → **BI** / descriptive analytics (Exam 6 · Q14), (Exam 3 · Q3).
- "Images, audio, video, free text" → **unstructured data**, a strong ML use case (Exam 1 · Q37).

### Traps
- Swapped definitions: "BI predicts, ML only visualizes" or "ML only works on structured tables" are both reversed. The BI vs ML difference is not about hardware (TPUs vs CPUs) either (Exam 6 · Q14).
- "Any system that receives real-time data" or "organizes data into a structured format" describes pipelines, not AI (Exam 6 · Q34).
- Recommendations and fraud detection are valid ML uses, but they run on **structured** data. Don't pick them when the question asks about **unstructured** data (Exam 1 · Q37).
- **Trends analysis** describes past patterns and **data automation** moves data. Neither learns each user's preferences (Exam 6 · Q18).
- A **survey** can feed a churn model as one input, but on its own it depends on who answers and doesn't predict who will leave (Exam 2 · Q29).

---

## 2. Data for ML: quality, quantity and preparation

### Key facts
- A model is only as good as its data. **More (good) training data** is the main lever for better prediction accuracy, because the model sees more examples and variations and **generalizes** better to new data. More storage, bandwidth or faster CPUs change speed or cost, not accuracy (Exam 6 · Q26).
- The extra data must be **relevant, high quality and correctly labeled**. Adding noisy or irrelevant data may not help (Exam 6 · Q26).
- **Prepare data before training.** When sources use different column names, date formats and file structures, **transform the data into a consistent format** (a common schema). Don't throw data away, split it into one model per format, or hope a model handles every format by itself (Exam 2 · Q17).
  - Typical preparation steps: standardize date formats, rename fields, convert data types, handle missing values, remove duplicates, and normalize category values so each feature means the same thing everywhere (Exam 2 · Q17).
  - Keep the **full history**. Older data shows seasonality, holidays and long-term trends that a forecast needs (Exam 2 · Q17), (Exam 5 · Q21).
- **Breadth matters.** Combine related datasets so the model sees the full picture. BigQuery and BigQuery ML can combine large datasets and predict where the data is stored (Exam 5 · Q21).
- Training data must be **representative**: it should cover every condition the model will meet. A storm model that predicts across several regions needs **all weather data, evenly from all regions**, normal days as well as extreme events (Exam 4 · Q35).
- *(not in the question bank)* Data quality dimensions: **accuracy, completeness, consistency, timeliness, relevance and representativeness**. Biased or unrepresentative data produces biased predictions (see lesson 10).

### Decision rules
- "Improve accuracy" → **more and better training data** (Exam 6 · Q26).
- "Different formats, column names, date styles" → **transform to a consistent format** first (Exam 2 · Q17).
- "Several related sources" → **combine them**, then predict (Exam 5 · Q21).

### Traps
- Infrastructure answers (storage, bandwidth, CPU) to a model-accuracy question. Hardware cuts training time, not prediction quality (Exam 6 · Q26).
- "Use only the most recent 10 months" throws away history that a long-range forecast needs (Exam 2 · Q17).
- "One model per file format" splits the data into smaller, less representative sets and leaves more models to build and maintain. File format isn't the pattern you want to predict (Exam 2 · Q17).
- Storing or archiving data in a warehouse or data lake isn't analysis. Archiving older data also removes history the model needs (Exam 5 · Q21).
- "Only severe weather data" leaves the model no normal cases to compare against (Exam 4 · Q35).

---

## 3. Choosing an approach: buy, adapt or build

### Key facts
- Google Cloud offers a spectrum, from least to most effort: **pre-trained APIs** and pre-built agents → **BigQuery ML** (SQL) → **AutoML** (your labeled data, no code) → **custom training** (your code, full control) (Exam 1 · Q2).
- **Pre-built / pre-trained** (APIs, agents, templates): **fastest to implement**, little ML expertise needed, but **less business differentiation**, because competitors can use the same thing (Exam 6 · Q2), (Exam 3 · Q23). You still need people to configure, integrate, secure, test and govern the solution, just not a large data-science team (Exam 6 · Q2).
- **Custom models**: **more effort and expertise** (collect and prepare data, train, evaluate, tune, deploy, monitor, maintain), but **higher differentiation**, because they encode your proprietary data and needs (Exam 4 · Q1).
- Pre-trained APIs cover **common tasks** (vision, speech, translation, text, documents). Predicting from **your own business data**, such as rental demand from booking history, needs a model trained on that data (Exam 6 · Q36).
- Neither approach changes **CapEx vs OpEx** (both are cloud pay-as-you-go), and nothing guarantees 100% accuracy. Accuracy depends on data quality, model design and monitoring (Exam 4 · Q1), (Exam 6 · Q2).

### Approach comparison

| Approach | Who | Data needed | Speed | Differentiation | Source |
|---|---|---|---|---|---|
| Pre-trained APIs | App developers | None to train | Fastest | Low | (Exam 3 · Q23), (Exam 5 · Q46) |
| Pre-built agents/templates | Business + developers | Your business content | Fast | Lower | (Exam 6 · Q2) |
| BigQuery ML | SQL analysts, DBAs | Tables in BigQuery | Fast | Medium | (Exam 2 · Q44), (Exam 6 · Q36) |
| AutoML | Teams with labeled data, no ML coders | Labeled examples | Medium | Medium | (Exam 6 · Q33), (Exam 4 · Q28) |
| Custom training | Data scientists, ML engineers | Your data + your code | Slowest | Highest | (Exam 5 · Q41), (Exam 4 · Q1) |

### Decision rules
- "As quickly as possible", "without building or training a model" → **pre-trained API** (Exam 3 · Q23).
- "Data in BigQuery" + "knows SQL" + "no data scientists" → **BigQuery ML** (Exam 6 · Q36).
- "Labeled images/text" + "no ML experience / can't write training code" → **AutoML** (Exam 6 · Q33).
- "Data scientists writing their own training code" → **custom training** (Exam 5 · Q41).
- Tradeoff questions: pre-built = **speed vs differentiation**; custom = **effort/expertise vs differentiation** (Exam 6 · Q2), (Exam 4 · Q1).

### Traps
- Answers that put pre-built solutions on the slow, expert-heavy side (or custom models on the easy side) are reversed (Exam 6 · Q2), (Exam 4 · Q1).
- Any option mentioning a shift to **CapEx** is a distractor in this domain (Exam 4 · Q1), (Exam 6 · Q2).
- "Models that always require custom training" contradicts the whole point of Google's tiered offering (Exam 1 · Q2).

---

## 4. Pre-trained APIs: Vision, Speech, Translation, Natural Language

### Key facts
- **Pre-trained APIs** are models Google has already trained. You send data, you get results. No training data, no ML team, and the fastest route to value (Exam 3 · Q23), (Exam 5 · Q46).
- They make AI easy to adopt because they **don't require ML specialists**. Developers call them like any other API (Exam 5 · Q46).
- **Vision API**: **label detection**, **object localization**, **landmark detection**, logos, faces, **text in images (OCR)**, explicit-content detection. Use it to auto-tag photo libraries and read text in photos (Exam 5 · Q1), (Exam 6 · Q24), (Exam 2 · Q44).
- **Sensitive Data Protection** (formerly Cloud DLP) finds and redacts sensitive data such as **payment card numbers** and other personal information. With Vision OCR it can flag ID or payment cards caught in uploaded photos, with no model training (Exam 3 · Q23).
- **Speech-to-Text API**: turns recorded or live audio into text, for example call recordings before sentiment analysis (Exam 4 · Q14). **Text-to-Speech** does the reverse: natural-sounding audio from text (Exam 2 · Q13), (Exam 6 · Q5).
- **Cloud Translation API**: translates text between languages, such as product pages into 18 languages. It can also **detect the language** of a text, and it can translate transcripts after Speech-to-Text (Exam 6 · Q37), (Exam 6 · Q47), (Exam 4 · Q14).
- **Natural Language API**: sentiment, entities, **content classification**, syntax analysis and topic discovery in text such as chat transcripts (Exam 6 · Q47), (Exam 1 · Q36).
- **Scanned forms**: APIs (Vision OCR, or **Document AI** for structured extraction) turn scans into **searchable digital text**. Document AI also pulls out **key-value pairs, entities, tables and fields** such as names and dates from forms, invoices, receipts, contracts and ID documents (Exam 6 · Q17), (Exam 1 · Q36).
- **Video Intelligence API** labels **video** content: objects, shots, explicit content. It is not for still photos (Exam 1 · Q41).

### Which API?

| Input | Need | API | Source |
|---|---|---|---|
| Photos | Labels, objects, places, landmarks, text | Vision API | (Exam 5 · Q1), (Exam 6 · Q24) |
| Photos | Detect ID or payment cards, fast, no model | Pre-trained APIs (Vision OCR + Sensitive Data Protection) | (Exam 3 · Q23) |
| Audio recordings | Transcribe to text | Speech-to-Text API | (Exam 4 · Q14) |
| Text | Spoken audio output | Text-to-Speech | (Exam 6 · Q5) |
| Text | Translate into other languages | Cloud Translation API | (Exam 6 · Q37) |
| Text | Topics, sentiment, entities | Natural Language API | (Exam 6 · Q47) |
| Scanned forms | Searchable text and key fields | Vision OCR / Document AI | (Exam 6 · Q17) |
| Video | Labels, shots, objects | Video Intelligence API | (Exam 1 · Q41) |

### Decision rules
- Generic categories (objects, places, labels, common items) and "without training" → **Vision API**, not AutoML Vision (Exam 5 · Q1), (Exam 6 · Q24).
- **Your own** categories (beaches vs mountains for your app, shoes vs bags in your catalog, faulty vs acceptable parts from your factory) → **AutoML**, see lesson 5. A generic model doesn't know your company-specific patterns (Exam 1 · Q41), (Exam 4 · Q28), (Exam 6 · Q33).
- Audio → Speech-to-Text first, then Natural Language for sentiment (Exam 4 · Q14), (Exam 1 · Q37).

### Traps
- Pre-trained APIs still need **input data** and permissions. They don't skip data validation or need fewer security permissions (Exam 5 · Q46).
- Pre-trained APIs can't forecast from your own tabular data, such as holiday demand for your listings (Exam 6 · Q36).
- "Convert documents into unstructured data" is backwards. Scans are already unstructured, and the API makes them searchable and structured (Exam 6 · Q17).
- Gemini Enterprise Agent Platform and BigQuery ML can do image work, but they are overkill when a simple pre-trained API fits (Exam 6 · Q24).
- Translation and Speech-to-Text don't find topics in text that is already written (Exam 6 · Q47).

---

## 5. BigQuery ML, AutoML and custom training

### Key facts
- **BigQuery ML** lets you **create, train, evaluate and run ML models with SQL** (GoogleSQL statements such as `CREATE MODEL`, or the console) inside BigQuery. The data stays where it is, so there's no export and no Python or Java (Exam 2 · Q44), (Exam 6 · Q36).
  - It works on structured or semi-structured data in BigQuery: classification, regression, **forecasting**, clustering, recommendation and anomaly detection (Exam 5 · Q1), (Exam 3 · Q23).
  - Typical uses: demand forecasting, churn, **predictive maintenance** (a bike-share predicting when docks need repair, cutting needless part swaps, which also helps sustainability) (Exam 2 · Q15), (Exam 6 · Q36).
- **AutoML** (now **AutoML on Agent Platform**; older names **AutoML Vision**, **AutoML Natural Language**) trains a **custom model on your labeled data** without you writing training code (Exam 4 · Q28), (Exam 6 · Q33).
  - Images in **your own categories**: travel photos into beaches, mountains, landmarks, forests (Exam 1 · Q41), catalog photos into shoes, bags, watches (Exam 4 · Q28), faulty vs acceptable parts on an assembly line (Exam 6 · Q33).
  - Text in **your own categories**: support messages into billing, feedback, technical issue (Exam 2 · Q6).
  - It still means preparing and labeling data, training, evaluating and deploying, so it is slower than calling a pre-trained API (Exam 3 · Q23).
- **Custom training** in Gemini Enterprise Agent Platform: data scientists write their **own training code** (for example in Agent Platform notebooks) for full control. It runs as **managed training jobs** with your choice of framework, custom containers, machine types and accelerators (GPUs, TPUs) (Exam 5 · Q41).
- **TensorFlow** is Google's **open-source, end-to-end ML platform** for building, training and deploying models, with a large ecosystem of tools and community resources. It is the answer for "open-source ML framework" (Exam 6 · Q9), (Exam 2 · Q38).

### BigQuery ML vs AutoML vs custom training

| Signal in the question | Answer | Source |
|---|---|---|
| Data in BigQuery, team knows SQL, no exporting, no Python | BigQuery ML | (Exam 2 · Q44), (Exam 6 · Q36), (Exam 2 · Q15) |
| Labeled images/text, custom categories, no ML coding skills | AutoML | (Exam 1 · Q41), (Exam 2 · Q6), (Exam 4 · Q28), (Exam 6 · Q33) |
| Data scientists writing training code | Custom training | (Exam 5 · Q41) |
| Open-source ML library | TensorFlow | (Exam 6 · Q9) |

### Decision rules
- "SQL" + "BigQuery" in the same question → **BigQuery ML**, nearly always. Even when AutoML is offered, a SQL team with data in BigQuery points to BigQuery ML, because AutoML means a separate platform workflow instead of SQL (Exam 6 · Q36).
- "Already labeled" + "no ML experience" → **AutoML** (Exam 6 · Q33).
- "Custom training code" → **custom training**, not AutoML and not raw Compute Engine (Exam 5 · Q41).

### Traps
- **Apache Beam** is an open-source programming model for data pipelines, and **Dataflow** is the managed service that runs Beam pipelines. Both process data. Neither is an ML library. **Cloud Run functions** run small event-driven code, they don't train models (Exam 6 · Q9).
- **Compute Engine** can train a model on VMs, but then you manage provisioning, environments and scaling yourself (Exam 5 · Q41).
- **Dataproc** (now Managed Service for Apache Spark), **Coldline** and **Interconnect** are not ML services (Exam 4 · Q28).
- **Video Intelligence API** is for video, and **Looker** is BI. Neither trains an image classifier (Exam 1 · Q41).
- **Agent Studio** builds agents and **Spanner** is a transactional database. Neither trains models on BigQuery tables with SQL (Exam 2 · Q44).
- Security (IAM), APIs (Apigee) or cheaper storage don't create business insight from data. A model does (Exam 2 · Q15).
- "Recommendations from Agent Search" recommends products, **Pub/Sub** moves messages and **Google Distributed Cloud** runs infrastructure at the edge. None classifies support messages (Exam 2 · Q6).
- **Discovery AI for Retail** improves product search and recommendations. It doesn't detect factory defects (Exam 6 · Q33).

---

## 6. Gemini Enterprise Agent Platform (formerly Vertex AI)

### Key facts
- **Gemini Enterprise Agent Platform** is Google Cloud's **unified, managed AI platform** (the dumps' name for what was Vertex AI). It covers the **whole ML lifecycle**: prepare data, train, evaluate, deploy, **monitor** models after deployment, track experiments and manage models (Exam 1 · Q36), (Exam 6 · Q41).
- It is also the platform for **generative AI**: developers **explore foundation models, adapt them with company data, and build, deploy, govern and optimize production-ready agents** without managing infrastructure (Exam 4 · Q17).
- It offers **model choice**: Google models (Gemini), **open models**, and **third-party partner models**, so you aren't tied to one provider. Teams compare them on cost, capability, performance and governance (Exam 6 · Q3).
- **Model Garden** is the catalog inside the platform where you discover and use Google, open and partner models (Exam 6 · Q3).
- It includes AutoML and custom training (lesson 5) (Exam 4 · Q28), (Exam 5 · Q41).
- **Agent Studio**: the **no-code / low-code** visual designer in the Google Cloud console for designing, configuring, testing and publishing agents, aimed at analysts without coding skills (Exam 3 · Q45), (Exam 2 · Q44).
- **Agent Platform API**: manage and call a finished model or agent **from your own Android, iOS and web apps** in code (Exam 6 · Q30).
- **AI Hub**: a **repository of ready-to-use AI/ML resources** (models, notebooks, pipelines) to help you start without building from scratch. It doesn't serve predictions, write all your code or clean your data (Exam 5 · Q16, see ⚠️).

### Decision rules
- "Managed platform" + "prepare, train, deploy, monitor" → **Gemini Enterprise Agent Platform** (Exam 1 · Q36), (Exam 6 · Q41).
- "Foundation models" + "adapt with company data" + "deploy agents" → **Gemini Enterprise Agent Platform** (Exam 4 · Q17).
- "No-code/low-code agent builder for analysts" → **Agent Studio** (Exam 3 · Q45).
- "Call the agent from our mobile/web app" → **Agent Platform API** (Exam 6 · Q30).

### Traps
- **GKE** and **Compute Engine** can run ML, but they aren't managed ML platforms. You'd build the lifecycle yourself (Exam 1 · Q36), (Exam 4 · Q17), (Exam 6 · Q41).
- **Cloud Load Balancing** spreads traffic. It isn't an AI platform (Exam 4 · Q17). **Dataproc** processes data with Spark and Hadoop, but it isn't a full ML lifecycle platform (Exam 6 · Q41).
- **Document AI** and **Natural Language API** are single-purpose pre-trained services, not a platform for custom models (Exam 1 · Q36).
- **Recommendations AI** is a packaged retail solution, not a general ML platform (Exam 6 · Q41).
- Model choice: "only Google models", "only third-party" and "only open models" are all wrong (Exam 6 · Q3).
- Billing Export API, Cloud Storage API and IAM don't invoke agents. IAM controls who may call the agent, but it isn't the interface (Exam 6 · Q30).

---

## 7. Generative AI, foundation models and Gemini

### Key facts
- **Generative AI** is a **specific field of AI that creates new content**: text, images, audio, video, code, summaries, from prompts (Exam 3 · Q24), (Exam 3 · Q40).
- **Foundation models** are large models **pre-trained on broad data**. They give a **powerful starting point** that you adapt for your business, which **cuts development time** compared with building a model from scratch (Exam 6 · Q45).
- Ways to adapt a foundation model: **prompting** (instructions and examples), **grounding** in trusted sources, often through **retrieval-augmented generation (RAG)** over your own documents, and **fine-tuning** on your data (Exam 6 · Q45).
- Gen AI can produce incomplete, outdated or false output (**hallucinations**), especially when it isn't grounded. Grounding, evaluation and human review reduce the risk (Exam 6 · Q45).
- **Gemini** is Google's **multimodal** foundation model family. It understands and combines **text, code, audio, images and video** in one model (Exam 4 · Q24).
- Through Gemini Enterprise Agent Platform you can choose Gemini, open or partner models (Exam 6 · Q3).
- *(not in the question bank)* Gemini also appears inside products, such as Gemini for Google Workspace and Gemini Code Assist.

### Decision rules
- "Create new content from prompts" → **generative AI** (Exam 3 · Q40).
- "Multimodal" + "text, code, audio, images, video" → **Gemini** (Exam 4 · Q24).
- "Start from a broadly trained model and adapt it" → **foundation model**, valued for **time saved** (Exam 6 · Q45).

### Traps
- Gen AI is not "only translation", "only image labeling", or "every ML algorithm". It is a specific field focused on creation. Image labeling is recognition (classification), not generation (Exam 3 · Q24).
- **Predictive analytics** forecasts, it doesn't create content. Data warehouses and relational databases aren't AI branches (Exam 3 · Q40).
- Foundation models **don't** remove the need for governance and security, **don't** make compute free (inference, tuning and hosting still cost money), and **don't guarantee factual accuracy**. Human review still matters (Exam 6 · Q45).
- BigQuery, Cloud Storage and Cloud SQL are data services, not models (Exam 4 · Q24).

---

## 8. Agentic AI, AI agents and Contact Center AI

### Key facts
- **Agentic AI** = AI that **understands a goal, plans and reasons, decides next steps, calls tools, takes actions** (check account status, update records, trigger refunds, escalate only when needed) and **completes multi-step workflows** with little human involvement (Exam 3 · Q3), (Exam 5 · Q32), (Exam 5 · Q36).
- Generative AI **creates content**. Agentic AI **acts**. An agent usually uses a generative model as its "brain" to understand intent, plus tools to do things (Exam 3 · Q3).
- Building agents on Google Cloud: **Agent Studio** for no-code/low-code (Exam 3 · Q45), **Gemini Enterprise Agent Platform** for developers (Exam 4 · Q17), **Agent Platform API** to call them from apps (Exam 6 · Q30). Pre-built agents and templates are faster but less differentiated (Exam 6 · Q2).
- **Gemini Enterprise** (the app, formerly Google Agentspace) is where employees chat with Gemini models and use ready-made and custom agents over company data. Don't confuse it with Gemini Enterprise Agent Platform, the developer platform (Exam 5 · Q11).
- **Contact Center AI (CCAI)** / **Contact Center AI Platform** is Google's **purpose-built customer-service solution**: virtual agents that automate common requests, **intelligent routing**, agent assist that helps human agents resolve issues faster, and conversation insights across chat and phone, while keeping conversations personalized (Exam 2 · Q13), (Exam 6 · Q5).
- Other packaged AI solutions show up as distractors. Know what each one does:
  - **Document AI**: process and extract data from invoices, forms, receipts, contracts, ID documents (Exam 1 · Q36), (Exam 6 · Q5).
  - **Recommendations AI** and **Recommendations from Agent Search**: personalized product or content recommendations (Exam 2 · Q13), (Exam 2 · Q6), (Exam 6 · Q41).
  - **Discovery AI for Retail**: product search, recommendations and personalization for retailers (Exam 6 · Q33).
  - **Cloud Talent Solution**: job search and candidate matching for recruiting sites (Exam 6 · Q5).

### Which concept or solution?

| Scenario | Answer | Source |
|---|---|---|
| Understand goal, call tools, update records, finish the workflow | Agentic AI | (Exam 3 · Q3), (Exam 5 · Q32) |
| Plan, reason and carry out multi-step tasks with minimal direction | Agentic AI | (Exam 5 · Q36) |
| Produce emails, banners, code from prompts | Generative AI | (Exam 3 · Q40) |
| Dashboards about past results | Business intelligence / descriptive analytics | (Exam 3 · Q3), (Exam 6 · Q14) |
| Handle many chat/phone requests, help support agents, stay personal | Contact Center AI (Platform) | (Exam 2 · Q13), (Exam 6 · Q5) |

### Decision rules
- Verbs like **decide, act, trigger, call tools, complete, plan** → **agentic AI** (Exam 5 · Q32).
- Verbs like **generate, draft, create, summarize** → **generative AI** (Exam 3 · Q24).
- Customer support at scale with phone and chat → **Contact Center AI** (Exam 6 · Q5).

### Traps
- Agentic AI is not IaaS, VMs, hybrid cloud, DNS or open-source software. Those options are filler (Exam 5 · Q32), (Exam 5 · Q36).
- "Generative AI" is the tempting wrong answer for agent scenarios. If the system **takes actions**, choose agentic (Exam 3 · Q3).
- **Descriptive analytics** and BI report on the past. They don't act (Exam 3 · Q3).
- **Text-to-Speech**, **Cloud Talent Solution** and **Document AI** each cover one narrow task, not a full support operation (Exam 6 · Q5). **Recommendations AI**, **Cloud Identity** and **Cloud Text-to-Speech** don't run a contact center (Exam 2 · Q13).

---

## 9. AI infrastructure: TPUs, GPUs and AI Hypercomputer

### Key facts
- **Cloud TPUs (Tensor Processing Units)** are Google's **custom-built ASICs (application-specific chips) designed specifically for ML**. They are fast at the tensor and matrix math in neural networks, **speed up training** of large models such as image recognition, and work well with TensorFlow (Exam 2 · Q38), (Exam 5 · Q31), (Exam 4 · Q26).
- **GPUs** are highly parallel, general-purpose accelerators that are also widely used for deep learning training and inference. For "train very large foundation models quickly", the answer is **GPUs and TPUs** (Exam 4 · Q26).
- **AI Hypercomputer** is Google Cloud's **integrated supercomputing architecture for AI**: performance-optimized hardware (TPUs, GPUs), high-performance networking and storage, **open software and popular ML frameworks**, workload orchestration and **flexible consumption models**, for **training, tuning and serving** at scale (Exam 4 · Q48), (Exam 5 · Q34), (Exam 5 · Q39).
- **World-leading AI** is one of Google Cloud's top differentiators: ready-to-use agents, Google's first-party models (Gemini), the Gemini Enterprise app, a unified AI development platform (Gemini Enterprise Agent Platform) and AI infrastructure (Exam 5 · Q11).

### Decision rules
- "Hardware specifically designed for ML", "domain-specific hardware" → **TPUs** (Exam 2 · Q38), (Exam 5 · Q31).
- "Hardware for very large models" with GPUs and TPUs offered together → **GPUs and TPUs** (Exam 4 · Q26).
- "Hardware + open software + ML frameworks + flexible consumption" → **AI Hypercomputer** (Exam 4 · Q48), (Exam 5 · Q34), (Exam 5 · Q39).
- "Agents + first-party models + unified AI platform" as a differentiator → **world-leading AI** (Exam 5 · Q11).

### Traps
- CPUs are general-purpose, and high-memory VMs add RAM, not ML acceleration. Neither is the ML-specific answer (Exam 2 · Q38).
- **Bare Metal Solution**, **Spot VMs** and **containers** are ways to run or price compute, not ML-specific hardware. Spot VMs are cheaper spare capacity that can be preempted. Containers package code; the speed comes from the hardware underneath (Exam 5 · Q31).
- HDDs, archival storage, VPC routers, DNS, edge locations, SaaS, Coldline, VPC and Workspace are filler (Exam 4 · Q26), (Exam 5 · Q34), (Exam 5 · Q39).
- "Multi-cloud architecture", "serverless data pipeline" and "DDoS protection" don't describe an AI compute stack (Exam 4 · Q48). "Global network", "CapEx reduction" and "open standards" are other categories, not the AI differentiator (Exam 5 · Q11).

---

## 10. Responsible AI and explainable AI

### Key facts
- **Responsible AI** means designing, building, deploying and operating AI that is **transparent, fair, safe, privacy-preserving and accountable**, and **reduces harmful bias** and harm to users. Defining such principles to keep user trust is responsible AI practice. It matters even more with gen AI, whose output can affect users and decisions (Exam 4 · Q43).
- **Explainable AI** shows **why a model made a specific prediction**: which factors or features drove it, for example a mortgage rejection. Regulated industries need it so auditors and compliance teams can review decisions. It also helps **detect bias** and check that the model behaves as intended (Exam 4 · Q50).
- Humans stay accountable: ML shouldn't make final calls on complex ethical dilemmas (Exam 5 · Q29), and gen AI output still needs review because it isn't guaranteed correct. Governance, access control and data protection remain the organization's job (Exam 6 · Q45).
- *(not in the question bank)* **Google's AI Principles** guide its own AI work (be socially beneficial, avoid unfair bias, be safe, be accountable, protect privacy, uphold scientific excellence). Bias usually comes from **unrepresentative training data**, so responsible AI starts with data (lesson 2). Your data used with Google Cloud AI services stays under your control and isn't used to train Google's general models without permission.

### Decision rules
- "Transparent, fair, safe, private, reduce bias" → **responsible AI** (Exam 4 · Q43).
- "Explain why the model decided X for this applicant", "auditors", "regulated" → **explainable AI** (Exam 4 · Q50).

### Traps
- Data virtualization, edge computing and legacy modernization have nothing to do with AI ethics. Edge computing can keep some data local, but it isn't the practice of setting AI principles (Exam 4 · Q43).
- **Generative AI** creates content. It doesn't explain decisions. **Unstructured data processing** and **multi-cloud networking** don't either (Exam 4 · Q50).

---

## ⚠️ Questionable answers

| Item | Issue |
|---|---|
| **(Exam 5 · Q16)** | **AI Hub** is an older Google Cloud product. Its role (a catalog of reusable models and assets) is now mostly filled by **Model Garden** in the AI platform. Know the definition, but it's dated. |
| **(Exam 1 · Q41)**, **(Exam 2 · Q6)** | "AutoML Vision" and "AutoML Natural Language" are the old standalone product names. Today AutoML lives inside the AI platform ("AutoML on Agent Platform" in (Exam 4 · Q28)), and Google steers new text-classification work toward tuning Gemini models. The concept (custom categories + labeled data + no code = AutoML) is still right. |
| **(Exam 6 · Q18)** | Multiple regression is itself a statistical/ML technique, so D isn't strictly wrong. "Machine learning" is keyed because it's the broader approach and the system must keep improving as new data arrives. |

---

## Last-minute cheat sheet

- **AI** = tasks that need human cognition. **ML** = learns from data to predict and decide. **BI** = dashboards about the past (Exam 6 · Q34), (Exam 6 · Q14).
- AI ⊃ ML ⊃ deep learning; gen AI is one area inside. Descriptive = what happened. Predictive = what will happen (Exam 6 · Q34), (Exam 3 · Q3), (Exam 3 · Q40).
- ML shines on **unstructured data** (audio sentiment) and on **recommendations** and **churn** (Exam 1 · Q37), (Exam 5 · Q29), (Exam 2 · Q29).
- Supervised = labeled examples. Unsupervised = groupings in unlabeled data (Exam 4 · Q28), (Exam 5 · Q29).
- Accuracy ← **more good training data**, not hardware. Messy sources → **consistent format**, keep full history. Related sources → **combine** (Exam 6 · Q26), (Exam 2 · Q17), (Exam 5 · Q21).
- Pre-built = **fast, less differentiation**. Custom = **more effort, more differentiation** (Exam 6 · Q2), (Exam 4 · Q1).
- Generic photo labels, landmarks, text → **Vision API**. Card numbers in photos → Vision OCR + **Sensitive Data Protection** (Exam 5 · Q1), (Exam 6 · Q24), (Exam 3 · Q23).
- Audio → **Speech-to-Text**. Text → audio = **Text-to-Speech**. Languages → **Translation**. Text topics/sentiment → **Natural Language**. Video → **Video Intelligence** (Exam 4 · Q14), (Exam 6 · Q37), (Exam 6 · Q47), (Exam 1 · Q41).
- Scanned forms → APIs make them **searchable** and extract fields; Document AI pulls key-value pairs and tables (Exam 6 · Q17).
- SQL analysts + BigQuery → **BigQuery ML** (`CREATE MODEL`), even when AutoML is offered (Exam 2 · Q44), (Exam 6 · Q36), (Exam 2 · Q15).
- Labeled data + your own categories + no ML coders → **AutoML** (Exam 1 · Q41), (Exam 2 · Q6), (Exam 4 · Q28), (Exam 6 · Q33).
- Data scientists' own code → **custom training** (managed jobs, your framework and accelerators). Open-source ML library → **TensorFlow**. Beam/Dataflow = data pipelines (Exam 5 · Q41), (Exam 6 · Q9).
- Full managed ML lifecycle, foundation models, agents → **Gemini Enterprise Agent Platform** (Exam 1 · Q36), (Exam 6 · Q41), (Exam 4 · Q17).
- Model choice = Google + open + partner models in **Model Garden** (Exam 6 · Q3). No-code agents → **Agent Studio**. Call agents from apps → **Agent Platform API** (Exam 3 · Q45), (Exam 6 · Q30).
- **AI Hub** = repository of ready-to-use AI resources (Exam 5 · Q16).
- **Gen AI** creates content. **Gemini** is multimodal. **Foundation models** = pre-trained start; adapt by prompting, grounding/RAG or fine-tuning; save time; still hallucinate and need review (Exam 3 · Q24), (Exam 3 · Q40), (Exam 4 · Q24), (Exam 6 · Q45).
- **Agentic AI** plans, calls tools and completes workflows (Exam 3 · Q3), (Exam 5 · Q32), (Exam 5 · Q36).
- Support at scale → **Contact Center AI**. Talent Solution = jobs. Discovery AI / Recommendations AI = retail search and recs (Exam 2 · Q13), (Exam 6 · Q5), (Exam 6 · Q33).
- ML-specific chips → **TPUs** (ASICs). Big models → **GPUs and TPUs** (Exam 2 · Q38), (Exam 5 · Q31), (Exam 4 · Q26).
- Hardware + open software + frameworks + flexible consumption → **AI Hypercomputer** (Exam 4 · Q48), (Exam 5 · Q34), (Exam 5 · Q39).
- Agents + Gemini + Gemini Enterprise + unified platform → **world-leading AI** differentiator (Exam 5 · Q11).
- Fair, transparent, safe, private → **responsible AI**. "Why this decision?" → **explainable AI** (Exam 4 · Q43), (Exam 4 · Q50).
- Tools for every skill level is Google's AI pitch (Exam 1 · Q2). Image symptom triage = **ML** (Exam 5 · Q5). Learns as data grows = **ML** (Exam 6 · Q18). Representative data from every region, normal and extreme (Exam 4 · Q35).
