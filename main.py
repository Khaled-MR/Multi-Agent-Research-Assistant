from fastapi import FastAPI, HTTPException
from agents.graph_pipeline import run_pipeline
from db.crud import log_interaction
from db.database import engine
from db.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message":  "Multi-Agent System API"}

@app.post("/run")
def run_all_agents(query: str):
    try:
        result = run_pipeline(query)
        log_interaction("full_pipeline", query, result)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline failed: {str(e)}")

#http://127.0.0.1:8000/docs
#uvicorn main:app --reload

#streamlit run app.py