"""
AI-based scoring for Writing and Speaking sections.
Priority: Gemini (primary) → Groq (fallback) → Mock scores (last resort)
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


# ---------------------------------------------------------------------------
# Gemini
# ---------------------------------------------------------------------------

async def _score_with_gemini(system_prompt: str, user_msg: str) -> Optional[dict]:
    """Call Gemini 2.0 Flash and return parsed JSON dict, or None on failure."""
    if not settings.gemini_api_key:
        return None
    try:
        import google.generativeai as genai
        genai.configure(api_key=settings.gemini_api_key)
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=system_prompt,
            generation_config={"temperature": 0.3, "max_output_tokens": 800},
        )
        response = await model.generate_content_async(user_msg)
        text = response.text.strip()
        # Strip markdown code fences if present
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text.strip())
    except Exception as e:
        print(f"[Gemini] scoring error: {e}")
        return None


# ---------------------------------------------------------------------------
# Groq
# ---------------------------------------------------------------------------

async def _score_with_groq(system_prompt: str, user_msg: str) -> Optional[dict]:
    """Call Groq LLaMA 3.3 70B and return parsed JSON dict, or None on failure."""
    if not settings.groq_api_key:
        return None
    try:
        from groq import AsyncGroq
        client = AsyncGroq(api_key=settings.groq_api_key)
        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.3,
            max_tokens=800,
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"[Groq] scoring error: {e}")
        return None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def score_writing(task_num: int, prompt_text: str, response_text: str) -> dict:
    """Score a writing response. Tries Gemini → Groq → mock."""
    task_desc = "Writing Task 1 (Email)" if task_num == 1 else "Writing Task 2 (Survey Response)"
    user_msg = f"Task: {task_desc}\nPrompt: {prompt_text}\n\nCandidate Response:\n{response_text}"

    result = await _score_with_gemini(WRITING_SYSTEM_PROMPT, user_msg)
    if result:
        result["_scored_by"] = "gemini-2.0-flash"
        return result

    result = await _score_with_groq(WRITING_SYSTEM_PROMPT, user_msg)
    if result:
        result["_scored_by"] = "groq-llama-3.3-70b"
        return result

    return _mock_writing_score()


async def score_speaking(task_num: int, prompt_text: str, transcript: str) -> dict:
    """Score a speaking transcript. Tries Gemini → Groq → mock."""
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

    result = await _score_with_gemini(SPEAKING_SYSTEM_PROMPT, user_msg)
    if result:
        result["_scored_by"] = "gemini-2.0-flash"
        return result

    result = await _score_with_groq(SPEAKING_SYSTEM_PROMPT, user_msg)
    if result:
        result["_scored_by"] = "groq-llama-3.3-70b"
        return result

    return _mock_speaking_score()


# ---------------------------------------------------------------------------
# Mock fallbacks
# ---------------------------------------------------------------------------

def _mock_writing_score() -> dict:
    return {
        "content_coherence": 7,
        "vocabulary": 7,
        "readability": 7,
        "task_fulfillment": 7,
        "overall_band": 7.0,
        "strengths": ["Good attempt at addressing the task"],
        "weaknesses": ["No AI API key configured — add GEMINI_API_KEY or GROQ_API_KEY for real feedback"],
        "suggestions": ["Set GEMINI_API_KEY (free at aistudio.google.com) or GROQ_API_KEY (free at console.groq.com)"],
        "model_answer_excerpt": "N/A — configure an AI API key for model answers",
        "_scored_by": "mock",
    }


def _mock_speaking_score() -> dict:
    return {
        "content_coherence": 7,
        "vocabulary": 7,
        "listenability": 7,
        "task_fulfillment": 7,
        "overall_band": 7.0,
        "strengths": ["Good attempt at addressing the task"],
        "weaknesses": ["No AI API key configured — add GEMINI_API_KEY or GROQ_API_KEY for real feedback"],
        "suggestions": ["Set GEMINI_API_KEY (free at aistudio.google.com) or GROQ_API_KEY (free at console.groq.com)"],
        "_scored_by": "mock",
    }
