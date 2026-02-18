from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
import os
import uuid
from database import get_db
from models.user import User
from models.test_session import TestSession
from models.speaking import SpeakingResponse
from schemas.speaking import SpeakingResponseOut
from schemas.session import SessionCreate, SessionOut
from services.ai_scoring import score_speaking
from services.scoring import calculate_speaking_score
from config import get_settings
from .deps import get_current_user
from datetime import datetime

router = APIRouter(prefix="/speaking", tags=["speaking"])
settings = get_settings()

SPEAKING_TASKS = {
    1: {
        "task_type": "giving_advice",
        "title": "Giving Advice",
        "prompt": "Your friend has just moved to a new city and is feeling lonely and homesick. They have asked you for advice on how to make friends and feel at home. Give your friend advice.",
        "prep_time": 30,
        "response_time": 90,
    },
    2: {
        "task_type": "personal_experience",
        "title": "Talking about a Personal Experience",
        "prompt": "Talk about a time when you had to learn something new very quickly. What was the situation? What did you do? How did it turn out?",
        "prep_time": 30,
        "response_time": 60,
    },
    3: {
        "task_type": "describing_scene",
        "title": "Describing a Scene",
        "prompt": "Look at the picture. Describe everything you see in as much detail as possible. Talk about the people, the place, and what might be happening.",
        "image_url": "/images/speaking/task3_scene.jpg",
        "prep_time": 30,
        "response_time": 60,
    },
    4: {
        "task_type": "making_predictions",
        "title": "Making Predictions",
        "prompt": "Look at the two pictures. What do you think will happen next? Describe what you think will happen and why.",
        "image_url": "/images/speaking/task4_predict.jpg",
        "prep_time": 30,
        "response_time": 60,
    },
    5: {
        "task_type": "comparing_persuading",
        "title": "Comparing and Persuading",
        "prompt": "A friend is trying to decide between two options: working from home full-time OR working in an office. Compare these two options and persuade your friend which one is better for them.",
        "prep_time": 30,
        "response_time": 60,
    },
    6: {
        "task_type": "difficult_situation",
        "title": "Dealing with a Difficult Situation",
        "prompt": "You are at a restaurant with your family to celebrate an important occasion. The food takes over an hour to arrive and is not what you ordered. What would you say and do?",
        "prep_time": 30,
        "response_time": 60,
    },
    7: {
        "task_type": "expressing_opinions",
        "title": "Expressing Opinions",
        "prompt": "Some people believe that university education should be free for everyone. Others think students should pay tuition fees. What is your opinion? Use specific reasons and examples to support your view.",
        "prep_time": 30,
        "response_time": 60,
    },
    8: {
        "task_type": "unlikely_situation",
        "title": "Describing an Unlikely Situation",
        "prompt": "If you could have any superpower for one day, what would you choose and what would you do with it? Describe the situation as if it were real.",
        "prep_time": 30,
        "response_time": 60,
    },
}


@router.post("/sessions", response_model=SessionOut, status_code=201)
def start_session(
    payload: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = TestSession(
        user_id=current_user.id,
        section="speaking",
        mode=payload.mode,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.get("/tasks")
def get_all_tasks(current_user: User = Depends(get_current_user)):
    return {"status": "success", "data": SPEAKING_TASKS}


@router.get("/tasks/{task_num}")
def get_task(task_num: int, current_user: User = Depends(get_current_user)):
    task = SPEAKING_TASKS.get(task_num)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "data": {**task, "task_num": task_num}}


@router.post("/sessions/{session_id}/responses", response_model=SpeakingResponseOut, status_code=201)
async def submit_response(
    session_id: int,
    task_num: int = Form(...),
    transcript: Optional[str] = Form(None),
    audio_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    audio_path = None
    if audio_file:
        os.makedirs(settings.audio_dir, exist_ok=True)
        filename = f"{uuid.uuid4()}.webm"
        audio_path = os.path.join(settings.audio_dir, filename)
        content = await audio_file.read()
        with open(audio_path, "wb") as f:
            f.write(content)

    task_info = SPEAKING_TASKS.get(task_num, {})
    prompt_text = task_info.get("prompt", "")

    ai_result = None
    if transcript:
        ai_result = await score_speaking(task_num, prompt_text, transcript)

    dims = {}
    if ai_result:
        dims = {
            "content_coherence": ai_result.get("content_coherence"),
            "vocabulary": ai_result.get("vocabulary"),
            "listenability": ai_result.get("listenability"),
            "task_fulfillment": ai_result.get("task_fulfillment"),
        }

    overall = calculate_speaking_score(dims) if dims else None

    response = SpeakingResponse(
        session_id=session_id,
        task_num=task_num,
        task_type=task_info.get("task_type"),
        prompt_text=prompt_text,
        audio_path=audio_path,
        transcript=transcript,
        ai_feedback=ai_result,
        score=overall,
        score_content=dims.get("content_coherence"),
        score_vocabulary=dims.get("vocabulary"),
        score_listenability=dims.get("listenability"),
        score_task_fulfillment=dims.get("task_fulfillment"),
    )
    db.add(response)
    db.commit()
    db.refresh(response)
    return response


@router.get("/sessions/{session_id}/responses", response_model=List[SpeakingResponseOut])
def get_responses(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return db.query(SpeakingResponse).filter(SpeakingResponse.session_id == session_id).all()


@router.post("/sessions/{session_id}/complete", response_model=SessionOut)
def complete_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    responses = db.query(SpeakingResponse).filter(SpeakingResponse.session_id == session_id).all()
    scores = [r.score for r in responses if r.score is not None]
    session.completed_at = datetime.utcnow()
    session.score = round(sum(scores) / len(scores), 1) if scores else None
    db.commit()
    db.refresh(session)
    return session
