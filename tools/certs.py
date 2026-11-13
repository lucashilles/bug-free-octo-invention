"""Certification definitions shared by all tools.

Each certification lives in <CODE>/ (questions.json, domain-map.json, exam-N.md),
study/<CODE>/ (guides + question banks) and content/<id>/ (lesson metadata + glossary).
"""
import json, os

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
