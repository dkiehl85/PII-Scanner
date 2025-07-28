
import streamlit as st
import pandas as pd
import os
import glob

st.set_page_config(page_title="PII Scan Dashboard", layout="wide")

st.title("🔍 PII Scan Results Dashboard")

# Load latest CSV scan file from current folder
csv_files = sorted(glob.glob("pii_scan_results_*.csv"), reverse=True)

if not csv_files:
    st.warning("No scan results found. Make sure you've run the scanner.")
else:
    latest_file = st.selectbox("Select a scan result file:", csv_files)

    df = pd.read_csv(latest_file)

    st.subheader("Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📁 Files Scanned", df['filepath'].nunique())
        st.metric("🧾 Total Findings", len(df))

    with col2:
        pii_counts = df['pii_type'].value_counts()
        st.bar_chart(pii_counts)

    st.subheader("Detailed Results")
    with st.expander("🔍 Filter and Explore"):
        pii_type = st.multiselect("Filter by PII Type", df['pii_type'].unique(), default=df['pii_type'].unique())
        file_filter = st.text_input("Search file path or name")

        filtered_df = df[df['pii_type'].isin(pii_type)]
        if file_filter:
            filtered_df = filtered_df[filtered_df['filepath'].str.contains(file_filter, case=False)]

        st.dataframe(filtered_df, use_container_width=True)

    st.download_button(
        label="📥 Download This Result as CSV",
        data=filtered_df.to_csv(index=False),
        file_name=f"filtered_{os.path.basename(latest_file)}",
        mime='text/csv'
    )
