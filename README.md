# 🛡️ PII Scanner

This project scans local files for Personally Identifiable Information (PII) across a variety of formats and now includes a Streamlit dashboard for viewing and filtering results.

---

## 🔍 What It Does

The scanner searches for common types of PII including:

- Email addresses
- Phone numbers
- Social Security Numbers (SSNs)
- Dates of Birth (DOB)
- Physical addresses

It supports scanning the following file types:

- `.csv`
- `.txt`
- `.pdf`
- `.xlsx`
- `.pptx` (including tables)
- `.msg` (Outlook messages)

---

## 🆕 Recent Additions

✅ **Recursive Scanning** — The scanner now searches all subfolders within the `samples/` directory.

✅ **Multi-format Support** — Enhanced parsing for `.pptx`, `.msg`, and more.

✅ **Auto Timestamped Output** — Each scan result is saved to a uniquely named CSV like `pii_scan_results_2025-07-28_1132.csv`.

✅ **Streamlit Dashboard** — A new `pii_dashboard.py` provides a visual summary and lets you filter and download results interactively.

---

## 🚀 How to Run the Scanner

1. Place your files (or folders of files) in the `samples/` directory.
2. Run the main scanner script:

```bash
python main.py
