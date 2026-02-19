from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any


class WritingResponseCreate(BaseModel):
    session_id: int
    task_num: int
    task_type: Optional[str] = None
    prompt_text: Optional[str] = None
    response_text: str
    word_count: Optional[int] = None


class WritingResponseOut(BaseModel):
    id: int
    session_id: int
    task_num: int
    task_type: Optional[str]
    response_text: str
    word_count: Optional[int]
    ai_feedback: Optional[Any]
    score: Optional[float]
    score_content: Optional[float]
    score_coherence: Optional[float]
    score_vocabulary: Optional[float]
    score_readability: Optional[float]
    score_task_fulfillment: Optional[float]
    submitted_at: datetime

    model_config = {"from_attributes": True}
