import streamlit as st
import requests

st.set_page_config(page_title="Multi-Agent Research System", layout="wide")

st.title("🔬 Multi-Agent Research Assistant")
query = st.text_input("Enter your research query", "deep learning in medicine")

if st.button("Run Agents"):
    with st.spinner("Running pipeline..."):
        try:
            response = requests.post("http://127.0.0.1:8000/run", params={"query": query})
            if response.status_code == 200:
                data = response.json()["result"]
                st.success("✅ Pipeline completed!")

                st.subheader("📘 Cleaned Research Papers")
                st.code(data["Cleaned Research Papers"], language="markdown")

                st.subheader("📊 Research Trends")
                st.markdown(data["Research Trends"])

                st.subheader("⚠️ Detected Anomalies")
                st.markdown(data["Detected Anomalies"])

                st.subheader("⚙️ Optimization Suggestions")
                st.markdown(data["Optimization Suggestions"])

                st.subheader("💡 Innovation Ideas")
                st.markdown(data["Innovation Ideas"])

                st.subheader("📄 Full Markdown Report")
                st.download_button("📥 Download report.md", data["Markdown Report"], file_name="report.md")
            else:
                st.error("❌ Error: " + response.text)
        except Exception as e:
            st.error(f"Request failed: {e}")
