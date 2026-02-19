"""
Seed script — populates the database with CELPIP-style practice questions.
Run: python -m data.seed   (from the backend/ directory)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from database import SessionLocal, engine, Base
from models.question import Question
import json

Base.metadata.create_all(bind=engine)

LISTENING_QUESTIONS = [
    # ── Part 1: Problem Solving (8 questions) ──────────────────────────────
    {
        "section": "listening",
        "part": 1,
        "question_number": 1,
        "type": "multiple_choice",
        "audio_script": (
            "Man: Hi Sarah, I just got a notice that my internet has been cut off. "
            "I paid the bill online last week but apparently it never went through. "
            "What should I do?\n"
            "Woman: Oh no! First, call your bank to confirm the payment was processed. "
            "If the bank confirms it went through, call the internet company with the "
            "transaction reference number and they should restore your service within a few hours."
        ),
        "content": "What is the man's problem?",
        "options": json.dumps([
            "He forgot to pay his internet bill",
            "His online payment did not go through",
            "His bank account was closed",
            "He lost his transaction reference number"
        ]),
        "correct_answer": "B",
        "explanation": "The man says he paid online but 'it never went through', meaning the payment failed to process.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 2,
        "type": "multiple_choice",
        "audio_script": (
            "Man: Hi Sarah, I just got a notice that my internet has been cut off. "
            "I paid the bill online last week but apparently it never went through. "
            "What should I do?\n"
            "Woman: Oh no! First, call your bank to confirm the payment was processed. "
            "If the bank confirms it went through, call the internet company with the "
            "transaction reference number and they should restore your service within a few hours."
        ),
        "content": "What does the woman recommend the man do FIRST?",
        "options": json.dumps([
            "Call the internet company immediately",
            "Pay the bill again with a different card",
            "Contact his bank to verify the payment",
            "Wait a few hours for service to be restored"
        ]),
        "correct_answer": "C",
        "explanation": "The woman says 'First, call your bank to confirm the payment was processed.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 3,
        "type": "multiple_choice",
        "audio_script": (
            "Woman: I have a job interview tomorrow but my suit is at the dry cleaner and they "
            "close at 6 pm. My shift ends at 5:45 and it takes 20 minutes to get there. "
            "I'm really stressed.\n"
            "Man: You might just make it if you leave work a few minutes early. "
            "Talk to your manager — explain the situation. Most managers are understanding "
            "about job interviews. Alternatively, do you have a friend who could pick it up for you?"
        ),
        "content": "Why is the woman stressed?",
        "options": json.dumps([
            "She has nothing to wear to her interview",
            "She may not reach the dry cleaner before it closes",
            "Her manager will not let her leave early",
            "She does not know where the dry cleaner is"
        ]),
        "correct_answer": "B",
        "explanation": "The dry cleaner closes at 6 pm, her shift ends at 5:45, and the commute takes 20 minutes — she cannot make it in time normally.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 4,
        "type": "multiple_choice",
        "audio_script": (
            "Woman: I have a job interview tomorrow but my suit is at the dry cleaner and they "
            "close at 6 pm. My shift ends at 5:45 and it takes 20 minutes to get there. "
            "I'm really stressed.\n"
            "Man: You might just make it if you leave work a few minutes early. "
            "Talk to your manager — explain the situation. Most managers are understanding "
            "about job interviews. Alternatively, do you have a friend who could pick it up for you?"
        ),
        "content": "What TWO solutions does the man suggest? Select the BEST answer.",
        "options": json.dumps([
            "Reschedule the interview and buy a new suit",
            "Leave work early with manager's permission, or ask a friend to collect it",
            "Call the dry cleaner and ask them to stay open late",
            "Take a taxi and leave immediately after the shift"
        ]),
        "correct_answer": "B",
        "explanation": "The man suggests asking the manager to leave early and asking a friend to pick it up.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 5,
        "type": "multiple_choice",
        "audio_script": (
            "Man: My landlord is refusing to fix the broken heating in my apartment even though "
            "I've asked three times. It's been two weeks and it's getting really cold at night.\n"
            "Woman: That's unacceptable. You should document everything — save your text messages "
            "and emails. Then contact your local tenant rights organization. In most provinces, "
            "landlords are legally required to maintain a minimum temperature. If he still refuses, "
            "you can apply to the landlord-tenant board for a rent reduction or repair order."
        ),
        "content": "What problem is the man experiencing?",
        "options": json.dumps([
            "His landlord raised his rent",
            "His apartment heating has not been repaired",
            "He is being evicted from his apartment",
            "His landlord is not responding to any messages"
        ]),
        "correct_answer": "B",
        "explanation": "The man explicitly states his heating is broken and the landlord has not fixed it.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 6,
        "type": "multiple_choice",
        "audio_script": (
            "Man: My landlord is refusing to fix the broken heating in my apartment even though "
            "I've asked three times. It's been two weeks and it's getting really cold at night.\n"
            "Woman: That's unacceptable. You should document everything — save your text messages "
            "and emails. Then contact your local tenant rights organization. In most provinces, "
            "landlords are legally required to maintain a minimum temperature. If he still refuses, "
            "you can apply to the landlord-tenant board for a rent reduction or repair order."
        ),
        "content": "According to the woman, what is the LAST step the man should take if the landlord still refuses?",
        "options": json.dumps([
            "Move out of the apartment immediately",
            "Call the police about the situation",
            "Apply to the landlord-tenant board",
            "Stop paying rent until repairs are made"
        ]),
        "correct_answer": "C",
        "explanation": "The woman says 'If he still refuses, you can apply to the landlord-tenant board' — this is described as the final escalation step.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 7,
        "type": "multiple_choice",
        "audio_script": (
            "Woman: I signed up for a gym membership six months ago but I've only been twice. "
            "I keep meaning to go but something always comes up. The membership auto-renews next month.\n"
            "Man: Maybe the gym isn't the right fit for you. Have you considered cancelling and "
            "trying something you enjoy more — like cycling or swimming? Or you could commit to "
            "going with a friend; having accountability makes a real difference. If you decide "
            "to keep the gym, set a non-negotiable schedule, like every Tuesday and Thursday morning."
        ),
        "content": "What does the man imply about the woman's situation?",
        "options": json.dumps([
            "She is wasting money on a gym she does not use",
            "She should exercise at home instead",
            "The gym membership is too expensive",
            "She needs to find a different gym location"
        ]),
        "correct_answer": "A",
        "explanation": "By suggesting she cancel and try something she enjoys more, the man implies she is paying for a gym she rarely uses.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "question_number": 8,
        "type": "multiple_choice",
        "audio_script": (
            "Woman: I signed up for a gym membership six months ago but I've only been twice. "
            "I keep meaning to go but something always comes up. The membership auto-renews next month.\n"
            "Man: Maybe the gym isn't the right fit for you. Have you considered cancelling and "
            "trying something you enjoy more — like cycling or swimming? Or you could commit to "
            "going with a friend; having accountability makes a real difference. If you decide "
            "to keep the gym, set a non-negotiable schedule, like every Tuesday and Thursday morning."
        ),
        "content": "If the woman keeps her membership, what does the man suggest?",
        "options": json.dumps([
            "Hire a personal trainer",
            "Set fixed days and times to attend",
            "Go every morning before work",
            "Join group fitness classes"
        ]),
        "correct_answer": "B",
        "explanation": "The man says 'set a non-negotiable schedule, like every Tuesday and Thursday morning' — fixed scheduled days.",
        "image_path": None,
        "audio_path": None,
    },

    # ── Part 2: Daily Life Conversation (5 questions) ───────────────────────
    {
        "section": "listening",
        "part": 2,
        "question_number": 1,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: Two neighbours are talking outside their apartment building.\n"
            "Anna: Hi David! I haven't seen you in ages. How have you been?\n"
            "David: Really good, thanks! I just got back from a work trip to Vancouver. "
            "Three weeks — it felt like forever. How about you?\n"
            "Anna: Not bad. Oh, by the way — there was a notice posted in the lobby about "
            "construction starting next Monday. They're redoing all the elevators. It'll take "
            "about four weeks apparently.\n"
            "David: Four weeks without elevators? I'm on the 14th floor! How are we supposed "
            "to manage?\n"
            "Anna: The notice said they'll keep one elevator running at all times, but expect delays. "
            "They also mentioned that residents with mobility issues can request priority access.\n"
            "David: That's something at least. I hope they actually stick to the four-week timeline."
        ),
        "content": "Where has David recently been?",
        "options": json.dumps([
            "On a vacation to Vancouver",
            "On a business trip to Vancouver",
            "Visiting family in Vancouver",
            "At a conference in Victoria"
        ]),
        "correct_answer": "B",
        "explanation": "David says 'I just got back from a work trip to Vancouver' — it was a work trip, not a vacation.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "question_number": 2,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: Two neighbours are talking outside their apartment building.\n"
            "Anna: Hi David! I haven't seen you in ages. How have you been?\n"
            "David: Really good, thanks! I just got back from a work trip to Vancouver. "
            "Three weeks — it felt like forever. How about you?\n"
            "Anna: Not bad. Oh, by the way — there was a notice posted in the lobby about "
            "construction starting next Monday. They're redoing all the elevators. It'll take "
            "about four weeks apparently.\n"
            "David: Four weeks without elevators? I'm on the 14th floor! How are we supposed "
            "to manage?\n"
            "Anna: The notice said they'll keep one elevator running at all times, but expect delays. "
            "They also mentioned that residents with mobility issues can request priority access.\n"
            "David: That's something at least. I hope they actually stick to the four-week timeline."
        ),
        "content": "What is the main subject of the building notice?",
        "options": json.dumps([
            "Lobby renovations starting next week",
            "Elevator upgrades lasting approximately four weeks",
            "New rules about using the stairwell",
            "A rent increase for all residents"
        ]),
        "correct_answer": "B",
        "explanation": "The notice is about redoing all the elevators, expected to take four weeks.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "question_number": 3,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: Two neighbours are talking outside their apartment building.\n"
            "Anna: Hi David! I haven't seen you in ages. How have you been?\n"
            "David: Really good, thanks! I just got back from a work trip to Vancouver. "
            "Three weeks — it felt like forever. How about you?\n"
            "Anna: Not bad. Oh, by the way — there was a notice posted in the lobby about "
            "construction starting next Monday. They're redoing all the elevators. It'll take "
            "about four weeks apparently.\n"
            "David: Four weeks without elevators? I'm on the 14th floor! How are we supposed "
            "to manage?\n"
            "Anna: The notice said they'll keep one elevator running at all times, but expect delays. "
            "They also mentioned that residents with mobility issues can request priority access.\n"
            "David: That's something at least. I hope they actually stick to the four-week timeline."
        ),
        "content": "Why is David particularly concerned about the elevator work?",
        "options": json.dumps([
            "He has a mobility issue",
            "He lives on a high floor",
            "He works from home and needs frequent access",
            "He just moved in and does not know the building well"
        ]),
        "correct_answer": "B",
        "explanation": "David says 'I'm on the 14th floor!' — living high up makes elevator outages much more inconvenient.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "question_number": 4,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: Two neighbours are talking outside their apartment building.\n"
            "Anna: Hi David! I haven't seen you in ages. How have you been?\n"
            "David: Really good, thanks! I just got back from a work trip to Vancouver. "
            "Three weeks — it felt like forever. How about you?\n"
            "Anna: Not bad. Oh, by the way — there was a notice posted in the lobby about "
            "construction starting next Monday. They're redoing all the elevators. It'll take "
            "about four weeks apparently.\n"
            "David: Four weeks without elevators? I'm on the 14th floor! How are we supposed "
            "to manage?\n"
            "Anna: The notice said they'll keep one elevator running at all times, but expect delays. "
            "They also mentioned that residents with mobility issues can request priority access.\n"
            "David: That's something at least. I hope they actually stick to the four-week timeline."
        ),
        "content": "What accommodation is available for residents with mobility issues?",
        "options": json.dumps([
            "A temporary elevator installed outside",
            "Priority access to the one operating elevator",
            "A reduced rent for the duration of construction",
            "Assistance carrying items up the stairs"
        ]),
        "correct_answer": "B",
        "explanation": "Anna says 'residents with mobility issues can request priority access' to the elevator that remains in service.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "question_number": 5,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: Two neighbours are talking outside their apartment building.\n"
            "Anna: Hi David! I haven't seen you in ages. How have you been?\n"
            "David: Really good, thanks! I just got back from a work trip to Vancouver. "
            "Three weeks — it felt like forever. How about you?\n"
            "Anna: Not bad. Oh, by the way — there was a notice posted in the lobby about "
            "construction starting next Monday. They're redoing all the elevators. It'll take "
            "about four weeks apparently.\n"
            "David: Four weeks without elevators? I'm on the 14th floor! How are we supposed "
            "to manage?\n"
            "Anna: The notice said they'll keep one elevator running at all times, but expect delays. "
            "They also mentioned that residents with mobility issues can request priority access.\n"
            "David: That's something at least. I hope they actually stick to the four-week timeline."
        ),
        "content": "What does David's final comment suggest about his attitude?",
        "options": json.dumps([
            "He is satisfied with the building management",
            "He is relieved the work will be done quickly",
            "He is doubtful the project will finish on schedule",
            "He plans to move out during the construction"
        ]),
        "correct_answer": "C",
        "explanation": "'I hope they actually stick to the four-week timeline' implies skepticism that it will be completed on time.",
        "image_path": None,
        "audio_path": None,
    },

    # ── Part 3: Listening for Information (6 questions) ─────────────────────
    {
        "section": "listening",
        "part": 3,
        "question_number": 1,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: You will hear a recorded message from Lakewood Community Centre.\n"
            "Thank you for calling Lakewood Community Centre. Our facility offers a wide range "
            "of programs for all ages. The centre is open Monday to Friday from 6 am to 10 pm, "
            "and Saturday and Sunday from 8 am to 8 pm. We are closed on statutory holidays.\n"
            "For aquatics programs, press 1. For fitness classes, press 2. For youth programs, "
            "press 3. For senior programs, press 4. To speak with a program coordinator, press 0 "
            "or stay on the line. Program registration for the spring session opens on March 1st "
            "and can be completed online at lakewoodcc.ca or in person at the front desk. "
            "Early registration discounts are available for members who register before February 15th."
        ),
        "content": "What are the community centre's weekend hours?",
        "options": json.dumps([
            "6 am to 10 pm",
            "7 am to 9 pm",
            "8 am to 8 pm",
            "9 am to 6 pm"
        ]),
        "correct_answer": "C",
        "explanation": "The recording states 'Saturday and Sunday from 8 am to 8 pm.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "question_number": 2,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: You will hear a recorded message from Lakewood Community Centre.\n"
            "Thank you for calling Lakewood Community Centre. Our facility offers a wide range "
            "of programs for all ages. The centre is open Monday to Friday from 6 am to 10 pm, "
            "and Saturday and Sunday from 8 am to 8 pm. We are closed on statutory holidays.\n"
            "For aquatics programs, press 1. For fitness classes, press 2. For youth programs, "
            "press 3. For senior programs, press 4. To speak with a program coordinator, press 0 "
            "or stay on the line. Program registration for the spring session opens on March 1st "
            "and can be completed online at lakewoodcc.ca or in person at the front desk. "
            "Early registration discounts are available for members who register before February 15th."
        ),
        "content": "When does spring session registration open?",
        "options": json.dumps([
            "February 1st",
            "February 15th",
            "March 1st",
            "March 15th"
        ]),
        "correct_answer": "C",
        "explanation": "The recording states 'Program registration for the spring session opens on March 1st.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "question_number": 3,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: You will hear a recorded message from Lakewood Community Centre.\n"
            "Thank you for calling Lakewood Community Centre. Our facility offers a wide range "
            "of programs for all ages. The centre is open Monday to Friday from 6 am to 10 pm, "
            "and Saturday and Sunday from 8 am to 8 pm. We are closed on statutory holidays.\n"
            "For aquatics programs, press 1. For fitness classes, press 2. For youth programs, "
            "press 3. For senior programs, press 4. To speak with a program coordinator, press 0 "
            "or stay on the line. Program registration for the spring session opens on March 1st "
            "and can be completed online at lakewoodcc.ca or in person at the front desk. "
            "Early registration discounts are available for members who register before February 15th."
        ),
        "content": "How can a caller reach a program coordinator?",
        "options": json.dumps([
            "Press 5 on the keypad",
            "Call back during weekday hours",
            "Press 0 or stay on the line",
            "Visit the front desk in person"
        ]),
        "correct_answer": "C",
        "explanation": "The recording says 'To speak with a program coordinator, press 0 or stay on the line.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "question_number": 4,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: You will hear a recorded message from Lakewood Community Centre.\n"
            "Thank you for calling Lakewood Community Centre. Our facility offers a wide range "
            "of programs for all ages. The centre is open Monday to Friday from 6 am to 10 pm, "
            "and Saturday and Sunday from 8 am to 8 pm. We are closed on statutory holidays.\n"
            "For aquatics programs, press 1. For fitness classes, press 2. For youth programs, "
            "press 3. For senior programs, press 4. To speak with a program coordinator, press 0 "
            "or stay on the line. Program registration for the spring session opens on March 1st "
            "and can be completed online at lakewoodcc.ca or in person at the front desk. "
            "Early registration discounts are available for members who register before February 15th."
        ),
        "content": "Who qualifies for an early registration discount?",
        "options": json.dumps([
            "All residents of Lakewood",
            "Seniors who register in person",
            "Members registering before February 15th",
            "Anyone who registers online before March 1st"
        ]),
        "correct_answer": "C",
        "explanation": "The recording says 'Early registration discounts are available for members who register before February 15th.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "question_number": 5,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: You will hear a recorded message from Lakewood Community Centre.\n"
            "Thank you for calling Lakewood Community Centre. Our facility offers a wide range "
            "of programs for all ages. The centre is open Monday to Friday from 6 am to 10 pm, "
            "and Saturday and Sunday from 8 am to 8 pm. We are closed on statutory holidays.\n"
            "For aquatics programs, press 1. For fitness classes, press 2. For youth programs, "
            "press 3. For senior programs, press 4. To speak with a program coordinator, press 0 "
            "or stay on the line. Program registration for the spring session opens on March 1st "
            "and can be completed online at lakewoodcc.ca or in person at the front desk. "
            "Early registration discounts are available for members who register before February 15th."
        ),
        "content": "Which button should a parent press to find programs for their 12-year-old child?",
        "options": json.dumps([
            "Press 1",
            "Press 2",
            "Press 3",
            "Press 4"
        ]),
        "correct_answer": "C",
        "explanation": "Press 3 is for 'youth programs' — a 12-year-old is a youth, not a senior.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "question_number": 6,
        "type": "multiple_choice",
        "audio_script": (
            "Narrator: You will hear a recorded message from Lakewood Community Centre.\n"
            "Thank you for calling Lakewood Community Centre. Our facility offers a wide range "
            "of programs for all ages. The centre is open Monday to Friday from 6 am to 10 pm, "
            "and Saturday and Sunday from 8 am to 8 pm. We are closed on statutory holidays.\n"
            "For aquatics programs, press 1. For fitness classes, press 2. For youth programs, "
            "press 3. For senior programs, press 4. To speak with a program coordinator, press 0 "
            "or stay on the line. Program registration for the spring session opens on March 1st "
            "and can be completed online at lakewoodcc.ca or in person at the front desk. "
            "Early registration discounts are available for members who register before February 15th."
        ),
        "content": "On which days is the community centre closed?",
        "options": json.dumps([
            "Every Sunday",
            "Weekends only",
            "Statutory holidays",
            "All federal holidays and Sundays"
        ]),
        "correct_answer": "C",
        "explanation": "The recording states 'We are closed on statutory holidays' — no other closure days are mentioned.",
        "image_path": None,
        "audio_path": None,
    },
]

READING_QUESTIONS = [
    # ── Part 1: Reading Correspondence ──────────────────────────────────────
    {
        "section": "reading",
        "part": 1,
        "question_number": 1,
        "type": "multiple_choice",
        "passage": (
            "Subject: Follow-up on Your Application — Marketing Coordinator Position\n\n"
            "Dear Ms. Chen,\n\n"
            "Thank you for submitting your application for the Marketing Coordinator position "
            "at Brightline Communications. We received over 200 applications and have carefully "
            "reviewed each one.\n\n"
            "I am pleased to inform you that you have been selected for a first-round interview. "
            "The interview will be conducted via video call and will last approximately 45 minutes. "
            "Please use the link below to select a time slot that works for you between "
            "March 10th and March 14th.\n\n"
            "Before the interview, we ask that you prepare a brief portfolio of two to three "
            "past marketing projects. You do not need to create new materials — existing work "
            "samples are perfectly appropriate. You will be given five minutes at the start of "
            "the interview to present these.\n\n"
            "If you have any questions or need to reschedule, please contact our HR team directly "
            "at hr@brightlinecomms.ca. We look forward to speaking with you.\n\n"
            "Sincerely,\n"
            "Jordan Park\n"
            "Talent Acquisition, Brightline Communications"
        ),
        "content": "What is the main purpose of this email?",
        "options": json.dumps([
            "To reject Ms. Chen's application",
            "To invite Ms. Chen to a job interview",
            "To request additional documents from Ms. Chen",
            "To offer Ms. Chen the Marketing Coordinator position"
        ]),
        "correct_answer": "B",
        "explanation": "The email says 'you have been selected for a first-round interview' — this is an interview invitation.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 1,
        "question_number": 2,
        "type": "multiple_choice",
        "passage": (
            "Subject: Follow-up on Your Application — Marketing Coordinator Position\n\n"
            "Dear Ms. Chen,\n\n"
            "Thank you for submitting your application for the Marketing Coordinator position "
            "at Brightline Communications. We received over 200 applications and have carefully "
            "reviewed each one.\n\n"
            "I am pleased to inform you that you have been selected for a first-round interview. "
            "The interview will be conducted via video call and will last approximately 45 minutes. "
            "Please use the link below to select a time slot that works for you between "
            "March 10th and March 14th.\n\n"
            "Before the interview, we ask that you prepare a brief portfolio of two to three "
            "past marketing projects. You do not need to create new materials — existing work "
            "samples are perfectly appropriate. You will be given five minutes at the start of "
            "the interview to present these.\n\n"
            "If you have any questions or need to reschedule, please contact our HR team directly "
            "at hr@brightlinecomms.ca. We look forward to speaking with you.\n\n"
            "Sincerely,\n"
            "Jordan Park\n"
            "Talent Acquisition, Brightline Communications"
        ),
        "content": "How long will the interview last?",
        "options": json.dumps([
            "30 minutes",
            "45 minutes",
            "60 minutes",
            "90 minutes"
        ]),
        "correct_answer": "B",
        "explanation": "The email states the interview 'will last approximately 45 minutes.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 1,
        "question_number": 3,
        "type": "multiple_choice",
        "passage": (
            "Subject: Follow-up on Your Application — Marketing Coordinator Position\n\n"
            "Dear Ms. Chen,\n\n"
            "Thank you for submitting your application for the Marketing Coordinator position "
            "at Brightline Communications. We received over 200 applications and have carefully "
            "reviewed each one.\n\n"
            "I am pleased to inform you that you have been selected for a first-round interview. "
            "The interview will be conducted via video call and will last approximately 45 minutes. "
            "Please use the link below to select a time slot that works for you between "
            "March 10th and March 14th.\n\n"
            "Before the interview, we ask that you prepare a brief portfolio of two to three "
            "past marketing projects. You do not need to create new materials — existing work "
            "samples are perfectly appropriate. You will be given five minutes at the start of "
            "the interview to present these.\n\n"
            "If you have any questions or need to reschedule, please contact our HR team directly "
            "at hr@brightlinecomms.ca. We look forward to speaking with you.\n\n"
            "Sincerely,\n"
            "Jordan Park\n"
            "Talent Acquisition, Brightline Communications"
        ),
        "content": "What does the email say about the portfolio materials?",
        "options": json.dumps([
            "They must be newly created for this interview",
            "Only digital formats will be accepted",
            "Existing work samples from past projects are acceptable",
            "The portfolio must contain at least five projects"
        ]),
        "correct_answer": "C",
        "explanation": "The email says 'You do not need to create new materials — existing work samples are perfectly appropriate.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 1,
        "question_number": 4,
        "type": "multiple_choice",
        "passage": (
            "Subject: Follow-up on Your Application — Marketing Coordinator Position\n\n"
            "Dear Ms. Chen,\n\n"
            "Thank you for submitting your application for the Marketing Coordinator position "
            "at Brightline Communications. We received over 200 applications and have carefully "
            "reviewed each one.\n\n"
            "I am pleased to inform you that you have been selected for a first-round interview. "
            "The interview will be conducted via video call and will last approximately 45 minutes. "
            "Please use the link below to select a time slot that works for you between "
            "March 10th and March 14th.\n\n"
            "Before the interview, we ask that you prepare a brief portfolio of two to three "
            "past marketing projects. You do not need to create new materials — existing work "
            "samples are perfectly appropriate. You will be given five minutes at the start of "
            "the interview to present these.\n\n"
            "If you have any questions or need to reschedule, please contact our HR team directly "
            "at hr@brightlinecomms.ca. We look forward to speaking with you.\n\n"
            "Sincerely,\n"
            "Jordan Park\n"
            "Talent Acquisition, Brightline Communications"
        ),
        "content": "Who should Ms. Chen contact if she needs to change the interview time?",
        "options": json.dumps([
            "Jordan Park directly by email",
            "The HR team at hr@brightlinecomms.ca",
            "The hiring manager listed on the job posting",
            "The receptionist at Brightline Communications"
        ]),
        "correct_answer": "B",
        "explanation": "The email says 'contact our HR team directly at hr@brightlinecomms.ca' for rescheduling.",
        "image_path": None,
        "audio_path": None,
    },

    # ── Part 3: Reading for Information (article) ────────────────────────────
    {
        "section": "reading",
        "part": 3,
        "question_number": 1,
        "type": "multiple_choice",
        "passage": (
            "The Rise of Micro-Credentials in Canadian Workplaces\n\n"
            "Over the past decade, micro-credentials have transformed how Canadians approach "
            "professional development. Unlike traditional degrees that require years of study, "
            "micro-credentials are short, focused certifications that validate specific skills — "
            "often completable in weeks rather than years.\n\n"
            "Employers in technology, healthcare, and finance sectors have been among the fastest "
            "adopters. A 2024 survey by the Conference Board of Canada found that 67% of employers "
            "now accept micro-credentials as equivalent to partial post-secondary education for "
            "certain roles, a significant increase from just 31% in 2019.\n\n"
            "Critics, however, argue that the proliferation of micro-credentials risks creating a "
            "fragmented education landscape. Dr. Maria Santos, an education researcher at the "
            "University of Toronto, warns that 'without standardization, employers may find it "
            "difficult to assess the true value of a credential issued by an unrecognized provider.'\n\n"
            "Despite these concerns, enrolment in micro-credential programs at Canadian colleges "
            "and universities surged by 140% between 2020 and 2024, driven largely by workers "
            "displaced during the pandemic seeking rapid upskilling. The federal government has "
            "responded with a $200 million investment in the Upskilling for Industry Initiative, "
            "aimed at aligning micro-credential programs with labour market needs.\n\n"
            "Proponents argue that micro-credentials democratize education by lowering cost and "
            "time barriers. A full university degree may cost upwards of $60,000 and take four "
            "years, whereas a comparable micro-credential program might cost $500 and take six weeks."
        ),
        "content": "According to the 2024 survey, what percentage of employers now accept micro-credentials as equivalent to partial post-secondary education?",
        "options": json.dumps([
            "31%",
            "54%",
            "67%",
            "87%"
        ]),
        "correct_answer": "C",
        "explanation": "The article states '67% of employers now accept micro-credentials as equivalent to partial post-secondary education.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 3,
        "question_number": 2,
        "type": "multiple_choice",
        "passage": (
            "The Rise of Micro-Credentials in Canadian Workplaces\n\n"
            "Over the past decade, micro-credentials have transformed how Canadians approach "
            "professional development. Unlike traditional degrees that require years of study, "
            "micro-credentials are short, focused certifications that validate specific skills — "
            "often completable in weeks rather than years.\n\n"
            "Employers in technology, healthcare, and finance sectors have been among the fastest "
            "adopters. A 2024 survey by the Conference Board of Canada found that 67% of employers "
            "now accept micro-credentials as equivalent to partial post-secondary education for "
            "certain roles, a significant increase from just 31% in 2019.\n\n"
            "Critics, however, argue that the proliferation of micro-credentials risks creating a "
            "fragmented education landscape. Dr. Maria Santos, an education researcher at the "
            "University of Toronto, warns that 'without standardization, employers may find it "
            "difficult to assess the true value of a credential issued by an unrecognized provider.'\n\n"
            "Despite these concerns, enrolment in micro-credential programs at Canadian colleges "
            "and universities surged by 140% between 2020 and 2024, driven largely by workers "
            "displaced during the pandemic seeking rapid upskilling. The federal government has "
            "responded with a $200 million investment in the Upskilling for Industry Initiative, "
            "aimed at aligning micro-credential programs with labour market needs.\n\n"
            "Proponents argue that micro-credentials democratize education by lowering cost and "
            "time barriers. A full university degree may cost upwards of $60,000 and take four "
            "years, whereas a comparable micro-credential program might cost $500 and take six weeks."
        ),
        "content": "What is Dr. Maria Santos's main concern about micro-credentials?",
        "options": json.dumps([
            "They are too expensive for most workers",
            "Lack of standardization makes it hard for employers to evaluate them",
            "They take too long to complete",
            "Universities are not offering enough programs"
        ]),
        "correct_answer": "B",
        "explanation": "Dr. Santos warns that 'without standardization, employers may find it difficult to assess the true value' of credentials.",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 3,
        "question_number": 3,
        "type": "multiple_choice",
        "passage": (
            "The Rise of Micro-Credentials in Canadian Workplaces\n\n"
            "Over the past decade, micro-credentials have transformed how Canadians approach "
            "professional development. Unlike traditional degrees that require years of study, "
            "micro-credentials are short, focused certifications that validate specific skills — "
            "often completable in weeks rather than years.\n\n"
            "Employers in technology, healthcare, and finance sectors have been among the fastest "
            "adopters. A 2024 survey by the Conference Board of Canada found that 67% of employers "
            "now accept micro-credentials as equivalent to partial post-secondary education for "
            "certain roles, a significant increase from just 31% in 2019.\n\n"
            "Critics, however, argue that the proliferation of micro-credentials risks creating a "
            "fragmented education landscape. Dr. Maria Santos, an education researcher at the "
            "University of Toronto, warns that 'without standardization, employers may find it "
            "difficult to assess the true value of a credential issued by an unrecognized provider.'\n\n"
            "Despite these concerns, enrolment in micro-credential programs at Canadian colleges "
            "and universities surged by 140% between 2020 and 2024, driven largely by workers "
            "displaced during the pandemic seeking rapid upskilling. The federal government has "
            "responded with a $200 million investment in the Upskilling for Industry Initiative, "
            "aimed at aligning micro-credential programs with labour market needs.\n\n"
            "Proponents argue that micro-credentials democratize education by lowering cost and "
            "time barriers. A full university degree may cost upwards of $60,000 and take four "
            "years, whereas a comparable micro-credential program might cost $500 and take six weeks."
        ),
        "content": "By how much did enrolment in micro-credential programs grow between 2020 and 2024?",
        "options": json.dumps([
            "67%",
            "100%",
            "140%",
            "200%"
        ]),
        "correct_answer": "C",
        "explanation": "The article states enrolment 'surged by 140% between 2020 and 2024.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 3,
        "question_number": 4,
        "type": "multiple_choice",
        "passage": (
            "The Rise of Micro-Credentials in Canadian Workplaces\n\n"
            "Over the past decade, micro-credentials have transformed how Canadians approach "
            "professional development. Unlike traditional degrees that require years of study, "
            "micro-credentials are short, focused certifications that validate specific skills — "
            "often completable in weeks rather than years.\n\n"
            "Employers in technology, healthcare, and finance sectors have been among the fastest "
            "adopters. A 2024 survey by the Conference Board of Canada found that 67% of employers "
            "now accept micro-credentials as equivalent to partial post-secondary education for "
            "certain roles, a significant increase from just 31% in 2019.\n\n"
            "Critics, however, argue that the proliferation of micro-credentials risks creating a "
            "fragmented education landscape. Dr. Maria Santos, an education researcher at the "
            "University of Toronto, warns that 'without standardization, employers may find it "
            "difficult to assess the true value of a credential issued by an unrecognized provider.'\n\n"
            "Despite these concerns, enrolment in micro-credential programs at Canadian colleges "
            "and universities surged by 140% between 2020 and 2024, driven largely by workers "
            "displaced during the pandemic seeking rapid upskilling. The federal government has "
            "responded with a $200 million investment in the Upskilling for Industry Initiative, "
            "aimed at aligning micro-credential programs with labour market needs.\n\n"
            "Proponents argue that micro-credentials democratize education by lowering cost and "
            "time barriers. A full university degree may cost upwards of $60,000 and take four "
            "years, whereas a comparable micro-credential program might cost $500 and take six weeks."
        ),
        "content": "What does the federal government's $200 million investment aim to do?",
        "options": json.dumps([
            "Replace university degree programs with micro-credentials",
            "Fund research into education standardization",
            "Align micro-credential programs with labour market needs",
            "Subsidize tuition at Canadian universities"
        ]),
        "correct_answer": "C",
        "explanation": "The investment is 'aimed at aligning micro-credential programs with labour market needs.'",
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "reading",
        "part": 3,
        "question_number": 5,
        "type": "multiple_choice",
        "passage": (
            "The Rise of Micro-Credentials in Canadian Workplaces\n\n"
            "Over the past decade, micro-credentials have transformed how Canadians approach "
            "professional development. Unlike traditional degrees that require years of study, "
            "micro-credentials are short, focused certifications that validate specific skills — "
            "often completable in weeks rather than years.\n\n"
            "Employers in technology, healthcare, and finance sectors have been among the fastest "
            "adopters. A 2024 survey by the Conference Board of Canada found that 67% of employers "
            "now accept micro-credentials as equivalent to partial post-secondary education for "
            "certain roles, a significant increase from just 31% in 2019.\n\n"
            "Critics, however, argue that the proliferation of micro-credentials risks creating a "
            "fragmented education landscape. Dr. Maria Santos, an education researcher at the "
            "University of Toronto, warns that 'without standardization, employers may find it "
            "difficult to assess the true value of a credential issued by an unrecognized provider.'\n\n"
            "Despite these concerns, enrolment in micro-credential programs at Canadian colleges "
            "and universities surged by 140% between 2020 and 2024, driven largely by workers "
            "displaced during the pandemic seeking rapid upskilling. The federal government has "
            "responded with a $200 million investment in the Upskilling for Industry Initiative, "
            "aimed at aligning micro-credential programs with labour market needs.\n\n"
            "Proponents argue that micro-credentials democratize education by lowering cost and "
            "time barriers. A full university degree may cost upwards of $60,000 and take four "
            "years, whereas a comparable micro-credential program might cost $500 and take six weeks."
        ),
        "content": "According to the article, what is a key advantage of micro-credentials over traditional degrees?",
        "options": json.dumps([
            "They are recognized by more employers",
            "They lower both the cost and time required",
            "They provide more in-depth subject knowledge",
            "They are issued by more reputable institutions"
        ]),
        "correct_answer": "B",
        "explanation": "Proponents argue micro-credentials 'democratize education by lowering cost and time barriers.'",
        "image_path": None,
        "audio_path": None,
    },
]

WRITING_PROMPTS = [
    {
        "section": "writing",
        "part": 1,
        "question_number": 1,
        "type": "email",
        "content": (
            "You recently stayed at a hotel for a business conference. During your stay you "
            "experienced several problems: the room was not as advertised, the Wi-Fi did not "
            "work, and the checkout process took over an hour.\n\n"
            "Write an email to the hotel manager. In your email:\n"
            "- Describe the problems you experienced\n"
            "- Explain how these issues affected your stay\n"
            "- Request appropriate compensation or resolution\n\n"
            "Write 150–200 words."
        ),
        "options": json.dumps({
            "task_type": "email",
            "min_words": 150,
            "max_words": 200,
            "time_minutes": 27,
            "scoring_rubric": [
                "Content and Coherence: Does the email address all three bullet points?",
                "Vocabulary: Is the language formal and appropriately varied?",
                "Readability: Is the email organized with clear paragraphs?",
                "Task Fulfillment: Does the writer make a specific, reasonable request?"
            ],
            "model_answer_notes": (
                "A band-10 response would use formal register throughout, open with a clear "
                "statement of purpose, address each problem with specific detail, connect problems "
                "to impact, and close with a polite but firm request such as a refund or discount "
                "on a future stay."
            )
        }),
        "correct_answer": None,
        "explanation": None,
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "writing",
        "part": 2,
        "question_number": 1,
        "type": "survey",
        "content": (
            "Some people believe that university education should be free for all citizens. "
            "Others believe that students should pay tuition fees because they are the primary "
            "beneficiaries of higher education.\n\n"
            "Survey question: Should university education be free for all citizens?\n\n"
            "In your response:\n"
            "- State and support your own opinion\n"
            "- Explain why you disagree with the opposing view\n\n"
            "Write 150–200 words."
        ),
        "options": json.dumps({
            "task_type": "survey",
            "min_words": 150,
            "max_words": 200,
            "time_minutes": 26,
            "scoring_rubric": [
                "Content and Coherence: Is a clear position stated and supported with reasons?",
                "Vocabulary: Is the language academic and appropriately varied?",
                "Readability: Are ideas logically connected with transitions?",
                "Task Fulfillment: Does the writer address both their view and the opposing view?"
            ],
            "model_answer_notes": (
                "A band-10 response would clearly state a position in the opening sentence, "
                "provide two to three specific supporting reasons with examples, acknowledge and "
                "refute the opposing view, and conclude with a restatement of position. "
                "Phrases like 'In my view', 'While some argue that...', 'However, this overlooks' "
                "are characteristic of high-band responses."
            )
        }),
        "correct_answer": None,
        "explanation": None,
        "image_path": None,
        "audio_path": None,
    },
]

SPEAKING_PROMPTS = [
    {
        "section": "speaking",
        "part": 1,
        "question_number": 1,
        "type": "advice",
        "content": (
            "Your friend recently moved to a new city for work and is feeling lonely and "
            "isolated. They have difficulty meeting new people and miss their support network.\n\n"
            "What advice would you give your friend?"
        ),
        "options": json.dumps({
            "task_type": "giving_advice",
            "prep_seconds": 30,
            "response_seconds": 90,
            "scoring_rubric": [
                "Content and Coherence: Is the advice specific, relevant, and logically structured?",
                "Vocabulary: Is the language natural and varied?",
                "Listenability: Is the speech clear, appropriately paced, and easy to follow?",
                "Task Fulfillment: Does the response address the friend's specific situation?"
            ],
            "tips": [
                "Use the PREP structure: Point, Reason, Example, Point",
                "Give at least two concrete suggestions",
                "Use connecting phrases: 'First of all...', 'Another thing you could do is...'",
                "Speak at a natural pace — not too fast or too slow"
            ]
        }),
        "correct_answer": None,
        "explanation": None,
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "speaking",
        "part": 2,
        "question_number": 1,
        "type": "personal_experience",
        "content": (
            "Talk about a time when you had to adapt to a significant change in your life. "
            "What happened? How did you handle it? What did you learn from the experience?"
        ),
        "options": json.dumps({
            "task_type": "personal_experience",
            "prep_seconds": 30,
            "response_seconds": 60,
            "scoring_rubric": [
                "Content and Coherence: Is the experience clearly described with a beginning, middle, and outcome?",
                "Vocabulary: Is narrative language used naturally?",
                "Listenability: Is the delivery clear and engaging?",
                "Task Fulfillment: Does the response answer all three questions?"
            ],
            "tips": [
                "Set the scene quickly in the first 10 seconds",
                "Use past tense verbs naturally",
                "Include specific details — names, places, feelings",
                "End with a reflection or lesson learned"
            ]
        }),
        "correct_answer": None,
        "explanation": None,
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "speaking",
        "part": 3,
        "question_number": 1,
        "type": "scene_description",
        "content": (
            "Describe what you see in this image. Talk about the people, the setting, "
            "and what might be happening."
        ),
        "options": json.dumps({
            "task_type": "scene_description",
            "prep_seconds": 30,
            "response_seconds": 60,
            "image_description": (
                "A busy farmers market on a sunny Saturday morning. "
                "Several vendor stalls with colourful awnings display fresh vegetables, "
                "fruits, and baked goods. Shoppers of various ages browse the stalls. "
                "A family with a young child is buying tomatoes. An elderly couple examines "
                "jars of honey. A vendor in an apron arranges loaves of bread."
            ),
            "scoring_rubric": [
                "Content and Coherence: Are multiple elements of the scene described?",
                "Vocabulary: Are descriptive and location words used accurately?",
                "Listenability: Is the description organized and easy to follow?",
                "Task Fulfillment: Are people, setting, and activity all addressed?"
            ],
            "tips": [
                "Start with the overall setting, then describe specific details",
                "Use present continuous tense: 'A woman is buying...'",
                "Use spatial language: 'In the foreground...', 'On the right...'",
                "Speculate about what might be happening: 'It looks like...'"
            ]
        }),
        "correct_answer": None,
        "explanation": None,
        "image_path": None,
        "audio_path": None,
    },
    {
        "section": "speaking",
        "part": 7,
        "question_number": 1,
        "type": "opinion",
        "content": (
            "Some people believe that remote work is better for employees than working in an office. "
            "What is your opinion? Give reasons and examples to support your view."
        ),
        "options": json.dumps({
            "task_type": "expressing_opinions",
            "prep_seconds": 30,
            "response_seconds": 60,
            "scoring_rubric": [
                "Content and Coherence: Is a clear position stated with supporting reasons?",
                "Vocabulary: Are opinion phrases and hedging language used naturally?",
                "Listenability: Is the speech organized and easy to follow?",
                "Task Fulfillment: Does the response express a clear opinion with support?"
            ],
            "tips": [
                "Open with a clear position: 'In my opinion...' or 'I strongly believe that...'",
                "Give two or three reasons with brief examples",
                "Acknowledge the other side briefly before reaffirming your view",
                "Conclude decisively"
            ]
        }),
        "correct_answer": None,
        "explanation": None,
        "image_path": None,
        "audio_path": None,
    },
]


def seed():
    db = SessionLocal()
    try:
        existing = db.query(Question).count()
        if existing > 0:
            print(f"Database already has {existing} questions. Skipping seed.")
            return

        all_questions = (
            LISTENING_QUESTIONS
            + READING_QUESTIONS
            + WRITING_PROMPTS
            + SPEAKING_PROMPTS
        )

        for q in all_questions:
            question = Question(
                section=q["section"],
                part=q["part"],
                question_number=q.get("question_number", 1),
                type=q["type"],
                content=q["content"],
                options=q.get("options"),
                correct_answer=q.get("correct_answer"),
                explanation=q.get("explanation"),
                audio_script=q.get("audio_script"),
                audio_path=q.get("audio_path"),
                image_path=q.get("image_path"),
                passage=q.get("passage"),
            )
            db.add(question)

        db.commit()
        print(f"Seeded {len(all_questions)} questions successfully.")
    except Exception as e:
        db.rollback()
        print(f"Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
