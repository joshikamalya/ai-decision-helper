import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.edge_case_handler import handle_edge_cases
from backend.decision_engine import analyze_decision

st.set_page_config(page_title="AI Decision Helper", layout="centered")

st.title("🧠 AI Decision Helper")
st.write("Make structured, logical, and unbiased decisions")

decision_input = st.text_area(
    "Describe your decision:",
    placeholder="Example: Should I switch my job for a higher salary but longer working hours?"
)

if st.button("Analyze Decision"):
    cleaned_decision, error = handle_edge_cases(decision_input)

    if error:
        st.warning(error)
    else:
        with st.spinner("Analyzing decision logically..."):
            result = analyze_decision(cleaned_decision)

        st.subheader("📊 Analysis Result")
        st.markdown(result)
