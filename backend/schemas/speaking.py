from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any


class SpeakingResponseCreate(BaseModel):
    session_id: int
    task_num: int
    task_type: Optional[str] = None
    prompt_text: Optional[str] = None
    image_path: Optional[str] = None
    audio_path: Optional[str] = None
    transcript: Optional[str] = None


class SpeakingResponseOut(BaseModel):
    id: int
    session_id: int
    task_num: int
    task_type: Optional[str]
    prompt_text: Optional[str]
    image_path: Optional[str]
    audio_path: Optional[str]
    transcript: Optional[str]
    ai_feedback: Optional[Any]
    score: Optional[float]
    score_content: Optional[float]
    score_vocabulary: Optional[float]
    score_listenability: Optional[float]
    score_task_fulfillment: Optional[float]
    submitted_at: datetime

    model_config = {"from_attributes": True}
