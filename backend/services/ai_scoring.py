"""
AI-based scoring for Writing and Speaking sections using OpenAI.
"""
import json
from typing import Optional
from config import get_settings

settings = get_settings()


WRITING_SYSTEM_PROMPT = """You are an expert CELPIP examiner. Score the writing response on 4 dimensions, each on a scale of 1–12:
1. content_coherence: logical flow, relevance, development of ideas
2. vocabulary: range, precision, appropriateness
3. readability: sentence variety, grammar, punctuation
4. task_fulfillment: addresses the task requirements, appropriate format/tone, word count adherence

Respond ONLY with valid JSON in this exact format:
{
  "content_coherence": <score 1-12>,
  "vocabulary": <score 1-12>,
  "readability": <score 1-12>,
  "task_fulfillment": <score 1-12>,
  "overall_band": <average rounded to 1 decimal>,
  "strengths": ["..."],
  "weaknesses": ["..."],
  "suggestions": ["..."],
  "model_answer_excerpt": "..."
}"""

SPEAKING_SYSTEM_PROMPT = """You are an expert CELPIP examiner. Score the speaking transcript on 4 dimensions, each on a scale of 1–12:
1. content_coherence: relevance, development, organization
2. vocabulary: range, accuracy, appropriateness
3. listenability: fluency, pronunciation indicators (from text), naturalness
4. task_fulfillment: addresses the task prompt, appropriate length/detail

Respond ONLY with valid JSON in this exact format:
{
  "content_coherence": <score 1-12>,
  "vocabulary": <score 1-12>,
  "listenability": <score 1-12>,
  "task_fulfillment": <score 1-12>,
  "overall_band": <average rounded to 1 decimal>,
  "strengths": ["..."],
  "weaknesses": ["..."],
  "suggestions": ["..."]
}"""


async def score_writing(task_num: int, prompt_text: str, response_text: str) -> Optional[dict]:
    """Score a writing response using OpenAI."""
    if not settings.openai_api_key:
        return _mock_writing_score()

    try:
        from openai import AsyncOpenAI
        client = AsyncOpenAI(api_key=settings.openai_api_key)

        task_desc = "Writing Task 1 (Email)" if task_num == 1 else "Writing Task 2 (Survey Response)"
        user_msg = f"Task: {task_desc}\nPrompt: {prompt_text}\n\nCandidate Response:\n{response_text}"

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": WRITING_SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.3,
            max_tokens=800,
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"AI scoring error: {e}")
        return _mock_writing_score()


async def score_speaking(task_num: int, prompt_text: str, transcript: str) -> Optional[dict]:
    """Score a speaking transcript using OpenAI."""
    if not settings.openai_api_key:
        return _mock_speaking_score()

    try:
        from openai import AsyncOpenAI
        client = AsyncOpenAI(api_key=settings.openai_api_key)

        task_descriptions = {
            1: "Giving Advice",
            2: "Talking about a Personal Experience",
            3: "Describing a Scene",
            4: "Making Predictions",
            5: "Comparing and Persuading",
            6: "Dealing with a Difficult Situation",
            7: "Expressing Opinions",
            8: "Describing an Unlikely Situation",
        }
        task_desc = task_descriptions.get(task_num, f"Task {task_num}")
        user_msg = f"Task: Speaking Task {task_num} — {task_desc}\nPrompt: {prompt_text}\n\nTranscript:\n{transcript}"

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SPEAKING_SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.3,
            max_tokens=600,
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"AI speaking scoring error: {e}")
        return _mock_speaking_score()


def _mock_writing_score() -> dict:
    return {
        "content_coherence": 7,
        "vocabulary": 7,
        "readability": 7,
        "task_fulfillment": 7,
        "overall_band": 7.0,
        "strengths": ["Good attempt at addressing the task"],
        "weaknesses": ["Add OpenAI API key for detailed feedback"],
        "suggestions": ["Configure OPENAI_API_KEY in .env for AI feedback"],
        "model_answer_excerpt": "N/A — configure OpenAI API for model answers",
    }


def _mock_speaking_score() -> dict:
    return {
        "content_coherence": 7,
        "vocabulary": 7,
        "listenability": 7,
        "task_fulfillment": 7,
        "overall_band": 7.0,
        "strengths": ["Good attempt at addressing the task"],
        "weaknesses": ["Add OpenAI API key for detailed feedback"],
        "suggestions": ["Configure OPENAI_API_KEY in .env for AI feedback"],
    }
