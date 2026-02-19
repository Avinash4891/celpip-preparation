"""
CELPIP Writing Section Prompts
Task 1: Writing an Email (27 minutes, 150–200 words)
Task 2: Responding to Survey Questions (26 minutes, 150–200 words)
"""

WRITING_PROMPTS = [
    {
        "section": "writing",
        "part": 1,
        "part_title": "Writing an Email",
        "question_number": 1,
        "question_type": "email",
        "question_text": (
            "You work at a mid-sized accounting firm in Toronto. Your father has been "
            "hospitalized following a serious medical emergency, and you need to travel "
            "to Vancouver immediately to be with your family. You must write a formal "
            "email to your manager, Ms. Patricia Holloway, requesting emergency leave.\n\n"
            "In your email:\n"
            "  - Explain the reason for your emergency leave request and state the dates "
            "you will be away (at least five business days)\n"
            "  - Describe how you plan to ensure your current workload is managed while "
            "you are absent (e.g., delegating tasks, briefing a colleague)\n"
            "  - Request confirmation of the approved leave and provide your personal "
            "contact details so you can be reached if urgently needed\n\n"
            "Write between 150 and 200 words. You have 27 minutes."
        ),
        "options": {
            "task_type": "formal_email",
            "min_words": 150,
            "max_words": 200,
            "time_minutes": 27,
            "scoring_rubric": [
                "Content/Coherence: All three bullet points addressed clearly; logical flow from opening to closing",
                "Vocabulary: Appropriate formal register; varied and precise word choice; no repetition",
                "Readability: Clear sentence structure; correct grammar and punctuation throughout",
                "Task Fulfillment: Tone is appropriately formal and professional; purpose is immediately clear",
            ],
            "model_answer_notes": (
                "Open with a direct subject line and formal salutation. State the emergency "
                "in the first sentence without excessive personal detail. Address each bullet "
                "point in a dedicated paragraph. Close with a formal expression of gratitude "
                "and a professional sign-off. Aim for varied sentence length and formal "
                "connectors such as 'furthermore', 'in addition', and 'I would appreciate'. "
                "Avoid contractions and casual language."
            ),
            "sample_band10_response": (
                "Subject: Emergency Leave Request — Family Medical Crisis\n\n"
                "Dear Ms. Holloway,\n\n"
                "I am writing to request emergency leave beginning Monday, February 23, and "
                "returning on Friday, March 1. My father suffered a serious cardiac event "
                "yesterday and has been admitted to Vancouver General Hospital. I must travel "
                "to be with my family during this critical time.\n\n"
                "To ensure minimal disruption to our team, I have already briefed my colleague "
                "David Osei on the status of the Henderson audit and the quarterly reconciliation "
                "reports. David has agreed to manage both files in my absence. All outstanding "
                "deliverables have been documented and shared via our internal project portal.\n\n"
                "I would sincerely appreciate your written confirmation of this leave approval "
                "at your earliest convenience. Should any urgent matters arise, I can be reached "
                "on my mobile at 416-555-0192 or by email at this address. I will monitor "
                "messages daily when circumstances permit.\n\n"
                "Thank you for your understanding and support.\n\n"
                "Sincerely,\n"
                "James Kowalski\n"
                "Senior Accountant, Holloway & Associates"
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["writing", "task1", "formal-email", "workplace", "emergency-leave"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "writing",
        "part": 2,
        "part_title": "Responding to Survey Questions",
        "question_number": 1,
        "question_type": "survey",
        "question_text": (
            "The City of Ottawa is conducting a public survey to determine how to allocate "
            "a $50 million infrastructure budget surplus. Residents are asked to select one "
            "of two options and explain their reasoning.\n\n"
            "Option A — Expand the OC Transpo Light Rail Transit (LRT) network by adding "
            "two new lines connecting the eastern suburbs to the downtown core, reducing "
            "commute times and lowering vehicle emissions across the city.\n\n"
            "Option B — Undertake a comprehensive repair and resurfacing program for over "
            "400 kilometres of deteriorating city roads, filling potholes, replacing damaged "
            "asphalt, and upgrading pedestrian crossings in all wards.\n\n"
            "In your response:\n"
            "  - Clearly state which option you support\n"
            "  - Give at least two specific reasons why your chosen option is better for "
            "Ottawa residents\n"
            "  - Explain why the other option is less urgent or less effective at this time\n\n"
            "Write between 150 and 200 words. You have 26 minutes."
        ),
        "options": {
            "task_type": "survey_opinion",
            "min_words": 150,
            "max_words": 200,
            "time_minutes": 26,
            "scoring_rubric": [
                "Content/Coherence: A clear position is stated; both options are addressed; arguments are logically sequenced",
                "Vocabulary: Civic and persuasive vocabulary used accurately; synonyms prevent repetition",
                "Readability: Paragraphs are well-structured; transitions between ideas are smooth and natural",
                "Task Fulfillment: Survey question is directly answered; a counter-argument to the rejected option is included",
            ],
            "model_answer_notes": (
                "State your chosen option in the very first sentence — do not hedge. "
                "Use a three-paragraph structure: (1) state choice and primary reason, "
                "(2) secondary reason with a specific local detail, (3) acknowledge and "
                "rebut the alternative option. Use persuasive discourse markers: "
                "'while it is true that...', 'nevertheless', 'a more pressing priority'. "
                "Avoid vague phrases like 'I think' — replace with 'the evidence suggests' "
                "or 'expanding transit would demonstrably'. Keep your rebuttal concise "
                "but specific — one or two sentences is sufficient."
            ),
            "sample_band10_response": (
                "I strongly support Option A: expanding Ottawa's LRT network to the eastern "
                "suburbs. This investment would deliver the greatest long-term benefit to "
                "the largest number of residents.\n\n"
                "First, thousands of commuters in Orléans and Barrhaven currently spend over "
                "ninety minutes daily in traffic due to insufficient rapid transit options. "
                "Extending the LRT would dramatically reduce this burden, improve air quality, "
                "and encourage sustainable transportation habits that benefit the entire city.\n\n"
                "Second, public transit expansion generates economic activity well beyond "
                "construction. Increased ridership supports local businesses near new stations "
                "and reduces the city's long-term road maintenance costs by decreasing the "
                "number of private vehicles.\n\n"
                "While deteriorating roads are undeniably inconvenient, road resurfacing "
                "is a short-term fix requiring repeated expenditure every few years. Transit "
                "infrastructure, by contrast, serves the city for decades. For Ottawa to grow "
                "sustainably, prioritizing public transit over road repair is the more "
                "strategically sound decision.\n\n"
                "Ottawa deserves a forward-thinking investment, and Option A delivers exactly that."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["writing", "task2", "survey", "civic", "public-transit", "opinion"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
]
