from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SessionCreate(BaseModel):
    section: str
    mode: str = "practice"


class SessionOut(BaseModel):
    id: int
    user_id: int
    section: str
    mode: str
    started_at: datetime
    completed_at: Optional[datetime]
    score: Optional[float]
    raw_score: Optional[int]
    total_questions: Optional[int]

    model_config = {"from_attributes": True}


class SessionComplete(BaseModel):
    session_id: int
