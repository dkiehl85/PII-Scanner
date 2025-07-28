import os
import csv
from datetime import datetime

from detectors.regex_detector import detect_pii
from parsers.csv_parser import read_csv
from parsers.pdf_parser import read_pdf
from parsers.txt_parser import read_txt
from parsers.xlsx_parser import read_xlsx
from parsers.pptx_parser import read_pptx
from parsers.msg_parser import read_msg

# Folder containing files to scan
folder_path = 'samples'

# Generate a unique output file using current date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
output_file = f"pii_scan_results_{timestamp}.csv"

# Open CSV for writing scan results
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filepath', 'line_number', 'pii_type', 'match'])

    # Recursively walk through all files in all subfolders
    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            ext = filename.lower().split('.')[-1]

            # Choose appropriate parser for file type
            if ext == 'csv':
                reader = read_csv
            elif ext == 'pdf':
                reader = read_pdf
            elif ext == 'txt':
                reader = read_txt
            elif ext == 'xlsx':
                reader = read_xlsx
            elif ext == 'pptx':
                reader = read_pptx
            elif ext == 'msg':
                reader = read_msg
            else:
                continue  # Unsupported file type

            print(f"\n📄 Scanning file: {file_path}")

            try:
                lines = reader(file_path)
            except Exception as e:
                print(f"  ⚠️ Could not read {file_path}: {e}")
                continue

            # Scan each line for PII
            for i, line in enumerate(lines):
                results = detect_pii(line)

                if results:
                    print(f"  Line {i + 1}:")
                    for label, match in results:
                        print(f"    {label}: {match}")
                        writer.writerow([file_path, i + 1, label, match])

print(f"\n✅ Scan complete. Results saved to {output_file}")
