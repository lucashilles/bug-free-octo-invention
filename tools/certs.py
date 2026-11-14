"""Certification definitions shared by all tools.

Each certification lives in <CODE>/ (questions.json, domain-map.json, exam-N.md),
study/<CODE>/ (guides + question banks) and content/<id>/ (lesson metadata + glossary).
"""
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CERTS = {
    'gpcdoe': {
        'code': 'GPCDOE',
        'name': 'Professional Cloud DevOps Engineer',
        'domains': {
            1: {'slug': '01-bootstrapping-gcp-organization', 'title': 'Bootstrapping and Maintaining a Google Cloud Organization',
                'short': 'Organization & IaC', 'weight': '~17%',
                'desc': 'Resource hierarchy, org policies, IAM and service accounts, Terraform and Kubernetes-native config management, environments.'},
            2: {'slug': '02-cicd-pipelines', 'title': 'Building and Implementing CI/CD Pipelines',
                'short': 'CI/CD Pipelines', 'weight': '~23%',
                'desc': 'Cloud Build, Cloud Deploy, Artifact Registry, deployment strategies, secrets and software supply-chain security.'},
            3: {'slug': '03-sre-practices', 'title': 'Applying Site Reliability Engineering Practices',
                'short': 'SRE Practices', 'weight': '~18%',
                'desc': 'SLIs, SLOs and error budgets, incident management, blameless postmortems, toil and capacity planning.'},
            4: {'slug': '04-observability-troubleshooting', 'title': 'Implementing Observability Practices and Troubleshooting Issues',
                'short': 'Observability & Troubleshooting', 'weight': '~23%',
                'desc': 'Cloud Logging and Monitoring, log-based metrics, alerting, Trace/Profiler/Error Reporting and troubleshooting.'},
            5: {'slug': '05-performance-and-cost', 'title': 'Optimizing Performance and Cost',
                'short': 'Performance & Cost', 'weight': '~19%',
                'desc': 'Compute pricing models, network tiers, billing export and labels, rightsizing and logging cost control.'},
        },
        # Udemy "Domain" labels (prefix match) -> domain number; untagged questions go in domain-map.json.
        'prefix_rules': [('Bootstrapping', 1), ('Set up and manage', 1), ('Building and implementing CI/CD', 2),
                         ('Applying site reliability', 3), ('Implementing observability', 4), ('Optimiz', 5)],
    },
    'gpcde': {
        'code': 'GPCDE',
        'name': 'Professional Cloud Developer',
        'domains': {
            1: {'slug': '01-designing-cloud-native-apps', 'title': 'Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications',
                'short': 'Design & Architecture', 'weight': '',
                'desc': 'Choosing compute and storage, microservices and API design, security and IAM for apps, scalability, caching and reliability patterns.'},
            2: {'slug': '02-building-and-testing', 'title': 'Building and Testing Applications',
                'short': 'Build & Test', 'weight': '',
                'desc': 'Local development and emulators, Cloud Code, container builds, testing strategies, and instrumenting code for logs, traces and errors.'},
            3: {'slug': '03-deploying-applications', 'title': 'Configuring and Deploying Applications',
                'short': 'Deployment', 'weight': '',
                'desc': 'Deploying to Cloud Run, GKE, App Engine and Cloud Functions, rollouts and traffic splitting, configuration and secrets, operating apps in production.'},
            4: {'slug': '04-integrating-google-cloud-services', 'title': 'Integrating Applications with Google Cloud Services',
                'short': 'Service Integration', 'weight': '',
                'desc': 'Pub/Sub, Eventarc, Cloud Tasks and Workflows, databases and Cloud Storage from code, API management and service-to-service authentication.'},
        },
        'prefix_rules': [],
    },
    'gcdl': {
        'code': 'GCDL',
        'name': 'Cloud Digital Leader',
        'domains': {
            1: {'slug': '01-digital-transformation', 'title': 'Digital Transformation with Google Cloud',
                'short': 'Digital Transformation', 'weight': '~17%',
                'desc': 'Why cloud, cloud models and economics (CapEx vs OpEx, TCO), Google Cloud infrastructure, and leading cloud adoption.'},
            2: {'slug': '02-data-transformation', 'title': 'Exploring Data Transformation with Google Cloud',
                'short': 'Data Transformation', 'weight': '~16%',
                'desc': 'The data value chain, structured vs unstructured data, databases and storage options, BigQuery, Looker and data governance.'},
            3: {'slug': '03-ai-innovation', 'title': 'Innovating with Google Cloud Artificial Intelligence',
                'short': 'AI & ML', 'weight': '~16%',
                'desc': 'AI/ML fundamentals, pre-trained APIs, AutoML, Vertex AI, generative AI and agents, and responsible AI.'},
            4: {'slug': '04-modernize-infrastructure', 'title': 'Modernize Infrastructure and Applications with Google Cloud',
                'short': 'Infrastructure & Apps', 'weight': '~17%',
                'desc': 'Compute options, containers and serverless, migration paths, hybrid and multicloud, APIs and application modernization.'},
            5: {'slug': '05-trust-and-security', 'title': 'Trust and Security with Google Cloud',
                'short': 'Trust & Security', 'weight': '~17%',
                'desc': 'Shared responsibility, zero trust, IAM, encryption, threats, compliance, data sovereignty and residency.'},
            6: {'slug': '06-scaling-operations', 'title': 'Scaling with Google Cloud Operations',
                'short': 'Operations & SRE', 'weight': '~17%',
                'desc': 'Cost management and billing, resource hierarchy, SRE and DevOps, SLAs/SLOs, observability, and sustainability.'},
        },
        'prefix_rules': [],
    },
}


def cert_dir(cid):
    return os.path.join(REPO, CERTS[cid]['code'])


def study_dir(cid):
    return os.path.join(REPO, 'study', CERTS[cid]['code'])


def content_dir(cid):
    return os.path.join(REPO, 'content', cid)


def load_questions(cid):
    return json.load(open(os.path.join(cert_dir(cid), 'questions.json'), encoding='utf-8'))


def domain_resolver(cid):
    """Return f(question) -> domain number, using domain-map.json overrides then Udemy label prefixes."""
    path = os.path.join(cert_dir(cid), 'domain-map.json')
    overrides = json.load(open(path)) if os.path.exists(path) else {}
    rules = CERTS[cid]['prefix_rules']

    def dom(x):
        k = f"{x['exam']}-{x['n']}"
        if k in overrides:
            return overrides[k]
        for p, n in rules:
            if x['domain'].startswith(p):
                return n
        raise ValueError(f'{cid}: no domain for question {k}; add it to {path}')
    return dom


LABEL_RE = re.compile(r'^\**\s*([A-Z]{1,4})[.:)]')


def option_label(text):
    """'B. ...' -> 'B', 'IV. ...' -> 'IV', '**A. ...' -> 'A'."""
    m = LABEL_RE.match(text)
    return m.group(1) if m else None


def apply_fixes(cid, questions, strict=True, path=None):
    """Apply <CODE>/fixes.json corrections in place. Idempotent, so it can run on a fresh parse
    or on questions.json itself. Per "<exam>-<n>" entry:
      question:    [[old, new], ...] text replacements in the stem
      answers:     {label: full option text}
      correct:     label or [labels] that are correct
      explanation: [[old, new], ...] replacements, or a string replacing the whole explanation
      note:        caveat appended to the explanation as "**⚠️ Note:** ..."
      why:         reason (documentation only)
    """
    path = path or os.path.join(cert_dir(cid), 'fixes.json')
    if not os.path.exists(path):
        return 0
    fixes = {k: v for k, v in json.load(open(path, encoding='utf-8')).items() if not k.startswith('_')}
    seen = set()

    def replace(q, field, pairs, k):
        for old, new in pairs:
            if old in new and new in q[field]:
                continue  # already applied (the new text extends the old)
            if old in q[field]:
                q[field] = q[field].replace(old, new)
            elif new not in q[field]:
                raise ValueError(f'{path}: {k}: {field} text not found: {old!r}')

    for q in questions:
        k = f"{q['exam']}-{q['n']}"
        fix = fixes.get(k)
        if not fix:
            continue
        seen.add(k)
        replace(q, 'question', fix.get('question', []), k)
        labels = {option_label(a['text']): a for a in q['answers']}
        for label, text in fix.get('answers', {}).items():
            if label not in labels:
                raise ValueError(f'{path}: {k}: no option {label}')
            labels[label]['text'] = text
        if 'correct' in fix:
            want = fix['correct'] if isinstance(fix['correct'], list) else [fix['correct']]
            if not set(want) <= set(labels):
                raise ValueError(f'{path}: {k}: no option among {want}')
            for label, a in labels.items():
                a['correct'] = label in want
        exp = fix.get('explanation')
        if isinstance(exp, str):
            q['explanation'] = exp
        elif exp:
            replace(q, 'explanation', exp, k)
        if fix.get('note'):
            note = f"**⚠️ Note:** {fix['note']}"
            if note not in q['explanation']:
                q['explanation'] = f"{q['explanation'].rstrip()}\n\n{note}"
    missing = set(fixes) - seen
    if strict and missing:
        raise ValueError(f'{path}: fixes for unknown questions: {sorted(missing)}')
    return len(seen)
