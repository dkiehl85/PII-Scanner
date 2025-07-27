import os
import csv
from detectors.regex_detector import detect_pii
from parsers.csv_parser import read_csv
from parsers.pdf_parser import read_pdf
from parsers.txt_parser import read_txt
from parsers.xlsx_parser import read_xlsx
from parsers.pptx_parser import read_pptx
from parsers.msg_parser import read_msg

folder_path = 'samples'
output_file = 'pii_scan_results.csv'

# Open CSV for writing results
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(['filename', 'line_number', 'pii_type', 'matches'])

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        ext = filename.lower().split('.')[-1]

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
            continue  # skip unsupported files

        print(f"\n📄 Scanning file: {filename}")

        try:
            lines = reader(file_path)
        except Exception as e:
            print(f"  ⚠️ Could not read {filename}: {e}")
            continue

        for i, line in enumerate(lines):
            results = detect_pii(line)
            if results:
                print(f"  Line {i + 1}:")
                for label, matches in results:
                    print(f"    {label}: {matches}")
                    # Write to CSV
                    writer.writerow([filename, i + 1, label, '; '.join(matches)])

print(f"\n✅ Scan complete. Results saved to {output_file}")
