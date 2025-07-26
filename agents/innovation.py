import os
import requests
from typing import TypedDict, List, Dict
from xml.etree import ElementTree as ET

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import Runnable



llm = ChatGroq(
    api_key="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", 
    model="llama3-70b-8192",  
    temperature=0.6
)

class GraphState(TypedDict):
    query: str
    papers: List[Dict[str, str]]
    cleaned: str
    trends: str
    anomalies: str
    optimizations: str
    innovations: str 
    markdown_report: str

def innovation_agent(state: GraphState) -> GraphState:
    prompt = PromptTemplate.from_template("""
You are an AI innovation researcher.

Given the following:
- Key Research Trends:
{trends}

- Detected Anomalies (with classification):
{anomalies}

- Optimization Ideas:
{optimizations}

Generate 2–3 novel research ideas that:
- Are not directly copied from existing ones
- Build on trends and anomalies
- Propose a research motivation and a proposed method

Then format your response as a Markdown report:
### 📘 Research Idea Title
**Motivation**: ...
**Proposed Method**: ...
**Potential Impact**: ...
---

Repeat for each idea.
""")
    chain = prompt | llm
    try:
        output = chain.invoke({
        "trends": state["trends"],
        "anomalies": state["anomalies"],
        "optimizations": state["optimizations"]
    })
        innovations = output.content
    except Exception as e:
       innovations = f"❌ Innovation Agent Error: {str(e)}"
    return {
        **state,
        "innovations": innovations,
        "markdown_report": output.content
    }

__all__ = ["innovation_agent"]

