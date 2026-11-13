# Shared domain metadata and question→domain mapping.
DOMAINS = {
 1: ('01-bootstrapping-gcp-organization', 'Domain 1 — Bootstrapping and Maintaining a Google Cloud Organization'),
 2: ('02-cicd-pipelines', 'Domain 2 — Building and Implementing CI/CD Pipelines'),
 3: ('03-sre-practices', 'Domain 3 — Applying Site Reliability Engineering Practices'),
 4: ('04-observability-troubleshooting', 'Domain 4 — Implementing Observability Practices and Troubleshooting Issues'),
 5: ('05-performance-and-cost', 'Domain 5 — Optimizing Performance and Cost'),
}
PREFIX = [('Bootstrapping', 1), ('Set up and manage', 1), ('Building and implementing CI/CD', 2),
          ('Applying site reliability', 3), ('Implementing observability', 4), ('Optimiz', 5)]
MANUAL = {'1-55':2,'2-2':2,'5-1':4,'5-2':2,'5-3':4,'5-4':5,'5-5':1,'5-6':3,'5-7':5,'5-8':1,'5-9':2,'5-10':4,
 '5-11':3,'5-12':3,'5-13':4,'5-14':2,'5-15':3,'5-16':2,'5-17':3,'5-18':5,'5-19':2,'5-20':3,'5-21':2,'5-22':5,
 '5-23':3,'5-24':1,'5-25':2,'5-26':2,'5-27':5,'5-28':4,'5-29':2,'5-30':2,'5-31':2,'5-32':3,'5-33':1,'5-34':2,
 '5-35':5,'5-36':3,'5-37':1,'5-38':1,'5-39':4,'5-40':1,'5-41':5,'5-42':4,'5-43':2,'5-44':3,'5-45':1,'5-46':3,
 '5-47':1,'5-48':3,'5-49':3,'5-50':2,'5-51':3,'5-52':2,'5-53':2,'5-54':4,'5-55':3,'5-56':2,'5-57':1,'5-58':2,
 '5-59':5,'5-60':3,'5-61':2,'5-62':1,'5-63':1,'5-64':5,'5-65':2}
def dom(x):
    k = f"{x['exam']}-{x['n']}"
    if k in MANUAL: return MANUAL[k]
    for p, n in PREFIX:
        if x['domain'].startswith(p): return n
    raise ValueError(k)

