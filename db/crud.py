from .models import Interaction
from .database import SessionLocal

def log_interaction(agent_name: str, input_text: str, output_text: str):
    db = SessionLocal()
    interaction = Interaction(
        agent_name=agent_name,
        input_text=str(input_text),
        output_text=str(output_text)
    )
    db.add(interaction)
    db.commit()
    db.close()
