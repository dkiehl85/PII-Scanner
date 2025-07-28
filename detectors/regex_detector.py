import re

PII_PATTERNS = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
    'phone': r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b',
    'address': r'\b\d{1,5}\s(?:[A-Z][a-z]*\s)+(?:Street|St|Avenue|Ave|Road|Rd|Lane|Ln|Boulevard|Blvd|Drive|Dr|Court|Ct)\b(?:,?\s[A-Za-z\s]+)*(?:,\s[A-Z]{2})?\s?\d{5}?',
    'dob': r'\b(?:\d{1,2}[/-]\d{1,2}[/-](?:19|20)\d{2}|(?:19|20)\d{2}[/-]\d{1,2}[/-]\d{1,2})\b',
}

def detect_pii(text):
    findings = []
    for label, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            findings.append((label, match))
    return findings
