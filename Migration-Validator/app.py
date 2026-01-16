import streamlit as st
import pandas as pd

from engine import RuleEngine
from validator import Validator

st.set_page_config(
    page_title="Migration Validator",
    layout="wide"
)

st.title("📦 Migration Validator")

# Upload CSV files
rules_file = st.file_uploader("Upload Rules CSV", type="csv")
legacy_file = st.file_uploader("Upload Legacy CSV", type="csv")
target_file = st.file_uploader("Upload Target CSV", type="csv")

if rules_file and legacy_file and target_file:
    rules_df = pd.read_csv(rules_file)
    legacy_df = pd.read_csv(legacy_file)
    target_df = pd.read_csv(target_file)

    if st.button("Run Validation"):
        engine = RuleEngine(rules_df)
        expected_df = engine.apply_rules(legacy_df)

        result = Validator.validate(expected_df, target_df)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", result["total"])
        col2.metric("Failed Records", result["failed"])
        col3.metric("Accuracy %", result["accuracy"])

        if result["failed"] > 0:
            st.subheader("❌ Failed Records")
            st.dataframe(result["failed_rows"])

            csv = result["failed_rows"].to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Failed Records",
                csv,
                "failed_records.csv",
                "text/csv"
            )
        else:
            st.success("✅ All records validated successfully!")
