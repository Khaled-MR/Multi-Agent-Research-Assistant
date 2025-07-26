# 👇 Load كل الـ agents هنا
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os
import requests
from typing import TypedDict, List, Dict
from xml.etree import ElementTree as ET

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import Runnable

from .researcher import researcher_agent, clean_papers
from .analysis import detect_trends, detect_anomalies, suggest_optimizations
from .innovation import innovation_agent

class GraphState(TypedDict):
    query: str
    papers: List[Dict[str, str]]
    cleaned: str
    trends: str
    anomalies: str
    optimizations: str
    innovations: str
    markdown_report: str

graph = StateGraph(GraphState)

graph.add_node("research", researcher_agent)
graph.add_node("clean", clean_papers)
graph.add_node("trends", detect_trends)
graph.add_node("anomalies", detect_anomalies)
graph.add_node("optimizations", suggest_optimizations)
graph.add_node("innovate", innovation_agent)

graph.set_entry_point("research")

graph.add_edge("research", "clean")
graph.add_edge("clean", "trends")
graph.add_edge("trends", "anomalies")
graph.add_edge("anomalies", "optimizations")
graph.add_edge("optimizations", "innovate")
graph.add_edge("innovate", END)

app = graph.compile()

def save_markdown_report(markdown_content: str, filename: str = "report.md") -> str:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    return filename

def run_pipeline(query: str) -> Dict[str, str]:
    output = app.invoke({"query": query})

    final_result = {
        "Query": query,
        "Cleaned Research Papers": output["cleaned"],
        "Research Trends": output["trends"],
        "Detected Anomalies": output["anomalies"],
        "Optimization Suggestions": output["optimizations"],
        "Innovation Ideas": output["innovations"],
        "Markdown Report": output["markdown_report"],
    }

    save_markdown_report(final_result["Markdown Report"])

    return final_result




