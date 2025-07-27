import pdfplumber

def read_pdf(file_path):
    lines = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Split by newline to get line-by-line analysis
                lines.extend(text.split('\n'))
    return lines
