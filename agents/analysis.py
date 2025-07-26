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


def detect_trends(state: GraphState) -> GraphState:
    text = state["cleaned"]
    
    vectorizer = TfidfVectorizer(stop_words="english", max_features=10)
    tfidf_matrix = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    
    prompt = PromptTemplate.from_template("""
You are an expert in scientific literature analysis.
The following text is from multiple research papers. Also, here are the top TF-IDF keywords: {keywords}

Please summarize the 3–5 main research trends present in the text.

Content:
{cleaned}
""")
    chain = prompt | llm
    try:
        response = chain.invoke({"cleaned": text, "keywords": ", ".join(keywords)})

    except Exception as e:
        response = f"❌ LLM Error: {str(e)}"
    
    return {**state, "trends": response.content, "keywords": list(keywords)}




def detect_anomalies(state: GraphState) -> GraphState:
    text = state["cleaned"]
    prompt = PromptTemplate.from_template("""
You are an anomaly detection assistant.

1. Identify any **unusual, surprising, or contradicting** ideas in the research text below.
2. For each anomaly:
   - Classify it as **Positive** (novel/innovative) or **Negative** (unjustified, contradicting).
   - Indicate the paper title or source it was extracted from if possible.

Text:
{cleaned}
""")
    chain = prompt | llm
    try:
        response = chain.invoke({"cleaned": text})
    except Exception as e:    
        response = f"❌ LLM Error: {str(e)}"
    return {**state, "anomalies": response.content}


def suggest_optimizations(state: GraphState) -> GraphState:
    text = state["cleaned"]
    prompt = PromptTemplate.from_template("""
You are an optimization researcher.

Based on the research text below, suggest **ONLY the top 3** most impactful and unique optimization ideas (based on evolutionary, heuristic, or hybrid methods). Avoid repetition or common knowledge.

Content:
{cleaned}
""")
    chain = prompt | llm
    try:
        response = chain.invoke({"cleaned": text})
    except Exception as e:    
        response = f"❌ LLM Error: {str(e)}"    
    
    return {**state, "optimizations": response.content}


__all__ = ["detect_trends", "detect_anomalies", "suggest_optimizations"]
