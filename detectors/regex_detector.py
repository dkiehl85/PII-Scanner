import re

PII_PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
    'phone': r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b',
}

def detect_pii(text):
    findings = []
    for label, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            findings.append((label, matches))
    return findings
