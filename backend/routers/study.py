from fastapi import APIRouter, Depends
from models.user import User
from .deps import get_current_user

router = APIRouter(prefix="/study", tags=["study"])

VOCABULARY_LISTS = {
    "band_8_to_9": [
        {"word": "articulate", "definition": "able to speak fluently and coherently", "example": "She gave an articulate response."},
        {"word": "coherent", "definition": "logical and consistent", "example": "His argument was coherent and well-structured."},
        {"word": "persuasive", "definition": "good at convincing people", "example": "The candidate made a persuasive case."},
        {"word": "elaborate", "definition": "involving many carefully arranged parts", "example": "She provided an elaborate explanation."},
        {"word": "concise", "definition": "giving a lot of information clearly and briefly", "example": "Keep your answer concise."},
    ],
    "band_9_to_10": [
        {"word": "nuanced", "definition": "characterized by subtle shades of meaning", "example": "A nuanced understanding of the issue."},
        {"word": "substantiate", "definition": "provide evidence to support a claim", "example": "Can you substantiate that claim?"},
        {"word": "pragmatic", "definition": "dealing with things realistically", "example": "A pragmatic approach to the problem."},
        {"word": "exemplify", "definition": "be a typical example of", "example": "This case exemplifies the problem."},
        {"word": "discern", "definition": "perceive or recognize clearly", "example": "She could discern the main argument."},
    ],
    "band_10_to_11": [
        {"word": "astute", "definition": "having an ability to accurately assess situations", "example": "An astute observation."},
        {"word": "cogent", "definition": "clear, logical, and convincing", "example": "A cogent argument."},
        {"word": "elucidate", "definition": "make clear; explain", "example": "Please elucidate your point."},
        {"word": "juxtapose", "definition": "place side by side for contrast", "example": "The author juxtaposes the two views."},
        {"word": "meticulous", "definition": "very careful and precise", "example": "A meticulous review of the evidence."},
    ],
}

WRITING_TEMPLATES = {
    "email_formal": {
        "title": "Formal Email Template",
        "structure": [
            "Subject line: Clear and specific",
            "Greeting: Dear [Name/Title],",
            "Opening: State purpose immediately",
            "Body para 1: Main point / reason for writing",
            "Body para 2: Supporting details / request",
            "Body para 3: Next steps / additional info",
            "Closing: Formal sign-off (Sincerely, Regards,)",
        ],
        "sample": "Dear Mr. Johnson,\n\nI am writing to inquire about the volunteer opportunities available at your community center...",
    },
    "email_informal": {
        "title": "Informal Email Template",
        "structure": [
            "Greeting: Hi [Name]!",
            "Opening: Friendly opener",
            "Body: Conversational, natural flow",
            "Closing: Casual sign-off (Take care, Talk soon,)",
        ],
        "sample": "Hi Sarah!\n\nI hope you're doing well! I heard you're looking for vacation recommendations...",
    },
    "survey_opinion": {
        "title": "Survey Opinion Response Template (OREO)",
        "structure": [
            "O — Opinion: State your view clearly in the opening",
            "R — Reason 1: First supporting reason",
            "E — Example 1: Concrete example for Reason 1",
            "O — Opinion restated + Reason 2 + Example 2",
            "Conclusion: Restate opinion, acknowledge opposing view briefly",
        ],
        "sample": "In my opinion, parks are a more valuable investment for our city than parking lots...",
    },
}

SPEAKING_TEMPLATES = {
    "PREP": {
        "title": "PREP Structure (for all speaking tasks)",
        "steps": [
            "P — Point: State your main point clearly",
            "R — Reason: Give the reason for your point",
            "E — Example: Provide a specific example",
            "P — Point: Restate your main point",
        ],
        "example": "I think people should exercise every day. (P) The main reason is that regular exercise improves both physical and mental health. (R) For example, studies show that just 30 minutes of walking daily can reduce stress and improve mood significantly. (E) That's why I believe daily exercise is essential for a healthy life. (P)",
    },
    "describe_scene": {
        "title": "Scene Description Framework",
        "steps": [
            "Overall setting: Where / when is this happening?",
            "People: Who is there? What are they doing? How do they look?",
            "Objects/environment: What do you see in the background?",
            "Atmosphere/mood: What is the feeling of the scene?",
            "Speculation: What might be happening or about to happen?",
        ],
    },
}

GRAMMAR_TIPS = [
    {"tip": "Use a variety of tenses", "detail": "Mix present, past, and future tenses to show range. CELPIP rewards tense variety."},
    {"tip": "Avoid repetition", "detail": "Use synonyms and pronouns. Repeating the same word lowers your vocabulary score."},
    {"tip": "Use transition words", "detail": "Words like 'furthermore', 'however', 'in contrast', 'as a result' show coherence."},
    {"tip": "Subject-verb agreement", "detail": "Ensure your verb matches your subject. 'The results show' not 'The results shows'."},
    {"tip": "Use conditionals for speculation", "detail": "'If I were to...', 'Should this happen...' shows grammatical range."},
    {"tip": "Avoid contractions in formal writing", "detail": "Write 'do not' instead of 'don't' in formal email tasks."},
    {"tip": "Passive voice sparingly", "detail": "Mix active and passive voice. 'Mistakes were made' vs 'I made mistakes'."},
]


@router.get("/vocabulary")
def get_vocabulary(band: str = None, current_user: User = Depends(get_current_user)):
    if band and band in VOCABULARY_LISTS:
        return {"status": "success", "data": {band: VOCABULARY_LISTS[band]}}
    return {"status": "success", "data": VOCABULARY_LISTS}


@router.get("/writing-templates")
def get_writing_templates(template_type: str = None, current_user: User = Depends(get_current_user)):
    if template_type and template_type in WRITING_TEMPLATES:
        return {"status": "success", "data": WRITING_TEMPLATES[template_type]}
    return {"status": "success", "data": WRITING_TEMPLATES}


@router.get("/speaking-templates")
def get_speaking_templates(current_user: User = Depends(get_current_user)):
    return {"status": "success", "data": SPEAKING_TEMPLATES}


@router.get("/grammar-tips")
def get_grammar_tips(current_user: User = Depends(get_current_user)):
    return {"status": "success", "data": GRAMMAR_TIPS}
