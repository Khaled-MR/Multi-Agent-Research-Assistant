# 🔬 Multi-Agent Research Insight Generator

This project leverages a **Multi-Agent System** using `LangGraph`, `LangChain`, and `Groq` to analyze research queries and generate actionable insights, trends, anomalies, and innovations — all delivered through a clean `FastAPI` backend and optional `Streamlit` interface.

---

## 🚀 Features

- 🧠 **Automated Research Agents**: Performs deep research from APIs like arXiv/Semantic Scholar.
- ✨ **Multi-Agent Pipeline**: Clean → Analyze → Detect anomalies → Optimize → Innovate.
- 📄 **Markdown Report Generation**: Automatically exports a full Markdown report.
- 🖥️ **FastAPI API**: Easily test and integrate via `/run?query=...` endpoint.
- 🌐 **Ngrok Support**: Share your local API with anyone for testing.
- 🧩 **Modular Architecture**: Clean, extensible, and agent-based by design.
- 🖼️ **Optional Streamlit UI**: Clean interface to input queries and view insights.

---
````

## 📦 Project Structure

📁 sprits\_internship/
├── main.py               # FastAPI app
├── graph\_pipeline.py     # LangGraph pipeline
├── agents/
│   ├── researcher.py     # Research + Cleaning agents
│   ├── analysis.py       # Trends + Anomaly + Optimization
│   └── innovation.py     # Innovation idea generator
├── db/
│   ├── crud.py           # Interaction logging
│   ├── database.py       # SQLite/SQLAlchemy setup
│   └── models.py         # DB schema
├── report.md             # Auto-generated Markdown Report
├── ui\_streamlit.py       # Optional Streamlit interface
├── requirements.txt
└── README.md             

````

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
cd sprits_internship

# Create virtual env
python -m venv Sprints_internships
.\Sprints_internships\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🧪 Usage

### Run FastAPI App

```bash
uvicorn main:app --reload
```

Then open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Test the API

```http
POST /run?query=deep learning in medicine
```

### Enable Public Access via ngrok

```bash
ngrok http 8000
```

---

## 🖼️ Optional: Run Streamlit UI

```bash
streamlit run ui_streamlit.py
```

---

## 📄 Sample Markdown Report

Auto-generated reports saved as `report.md`, including:

* 📌 Research Trends
* ⚠️ Detected Anomalies
* 🛠️ Optimization Suggestions
* 💡 Innovation Ideas

---

## ✅ Requirements

```
langgraph
langchain
langchain_groq
fastapi
uvicorn
requests
scikit-learn
numpy
python-dotenv
streamlit
```

---

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🧠 Acknowledgments

This project uses the power of:

* [LangGraph](https://github.com/langchain-ai/langgraph)
* [LangChain](https://www.langchain.com/)
* [Groq API](https://console.groq.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)


