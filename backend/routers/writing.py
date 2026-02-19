from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.user import User
from models.test_session import TestSession
from models.writing import WritingResponse
from schemas.writing import WritingResponseCreate, WritingResponseOut
from schemas.session import SessionCreate, SessionOut
from services.ai_scoring import score_writing
from services.scoring import calculate_writing_score
from .deps import get_current_user
from datetime import datetime

router = APIRouter(prefix="/writing", tags=["writing"])

WRITING_PROMPTS = {
    1: {
        "task_type": "email",
        "prompt": (
            "You received an email from your friend asking for recommendations about where to go "
            "for a vacation in Canada. Write a reply email giving your friend advice. "
            "In your email:\n"
            "- Suggest a specific destination\n"
            "- Give at least two reasons why it is a good choice\n"
            "- Offer to help plan the trip\n\n"
            "Write 150–200 words."
        ),
    },
    2: {
        "task_type": "survey",
        "prompt": (
            "A city is deciding whether to invest in building more parks or building more parking lots. "
            "Some people believe parks improve quality of life, while others say parking is essential "
            "for economic growth.\n\n"
            "Write a response that considers BOTH points of view and states YOUR opinion clearly. "
            "Give reasons and examples to support your view.\n\n"
            "Write 150–200 words."
        ),
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
        section="writing",
        mode=payload.mode,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.get("/prompts/{task_num}")
def get_prompt(task_num: int, current_user: User = Depends(get_current_user)):
    prompt = WRITING_PROMPTS.get(task_num)
    if not prompt:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "data": prompt}


@router.post("/sessions/{session_id}/responses", response_model=WritingResponseOut, status_code=201)
async def submit_response(
    session_id: int,
    payload: WritingResponseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    word_count = len(payload.response_text.split())
    prompt_info = WRITING_PROMPTS.get(payload.task_num, {})

    # AI scoring
    ai_result = await score_writing(
        task_num=payload.task_num,
        prompt_text=payload.prompt_text or prompt_info.get("prompt", ""),
        response_text=payload.response_text,
    )

    dims = {}
    if ai_result:
        dims = {
            "content_coherence": ai_result.get("content_coherence"),
            "vocabulary": ai_result.get("vocabulary"),
            "readability": ai_result.get("readability"),
            "task_fulfillment": ai_result.get("task_fulfillment"),
        }

    overall = calculate_writing_score(dims)

    response = WritingResponse(
        session_id=session_id,
        task_num=payload.task_num,
        task_type=prompt_info.get("task_type"),
        prompt_text=payload.prompt_text or prompt_info.get("prompt"),
        response_text=payload.response_text,
        word_count=word_count,
        ai_feedback=ai_result,
        score=overall,
        score_content=dims.get("content_coherence"),
        score_coherence=dims.get("content_coherence"),
        score_vocabulary=dims.get("vocabulary"),
        score_readability=dims.get("readability"),
        score_task_fulfillment=dims.get("task_fulfillment"),
    )
    db.add(response)
    db.commit()
    db.refresh(response)
    return response


@router.get("/sessions/{session_id}/responses", response_model=List[WritingResponseOut])
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
    return db.query(WritingResponse).filter(WritingResponse.session_id == session_id).all()


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

    responses = db.query(WritingResponse).filter(WritingResponse.session_id == session_id).all()
    scores = [r.score for r in responses if r.score is not None]
    session.completed_at = datetime.utcnow()
    session.score = round(sum(scores) / len(scores), 1) if scores else None
    db.commit()
    db.refresh(session)
    return session
