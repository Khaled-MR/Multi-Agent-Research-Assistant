import os
import requests
from typing import TypedDict, List, Dict
from xml.etree import ElementTree as ET

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import Runnable

class GraphState(TypedDict):
    query: str
    papers: List[Dict[str, str]]
    cleaned: str


def fetch_arxiv(query: str, max_results=3) -> List[Dict[str, str]]:
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
        papers.append({"title": title, "summary": summary, "source": "arXiv"})
    return papers


def fetch_semantic_scholar(query: str, max_results=3) -> List[Dict[str, str]]:
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={max_results}&fields=title,abstract"
    headers = {"User-Agent": "ResearchAgent/1.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return []
    
    data = response.json()
    papers = []
    for paper in data.get("data", []):
        title = paper.get("title", "")
        summary = paper.get("abstract", "")
        if title and summary:
            papers.append({"title": title, "summary": summary, "source": "Semantic Scholar"})
    return papers


def fetch_simulated(query: str) -> List[Dict[str, str]]:
    return [
        {"title": f"Simulated Paper on {query} 1", "summary": "This is a simulated abstract 1.", "source": "SimulatedAPI"},
        {"title": f"Simulated Paper on {query} 2", "summary": "This is a simulated abstract 2.", "source": "SimulatedAPI"},
    ]


def researcher_agent(state: GraphState) -> GraphState:
    query = state["query"]
    arxiv_papers = fetch_arxiv(query)
    semantic_papers = fetch_semantic_scholar(query)
    simulated_papers = fetch_simulated(query)
    
    all_papers = arxiv_papers + semantic_papers + simulated_papers
    return {"query": query, "papers": all_papers}


def clean_papers(state: GraphState) -> GraphState:
    papers = state["papers"]
    cleaned = ""
    for paper in papers:
        title = paper["title"].strip().replace("\n", " ")
        summary = paper["summary"].strip().replace("\n", " ")
        source = paper["source"]
        cleaned += f"[{source}] Title: {title}\nSummary: {summary}\n\n"
    return {"query": state["query"], "papers": papers, "cleaned": cleaned}

__all__ = ["researcher_agent", "clean_papers"]