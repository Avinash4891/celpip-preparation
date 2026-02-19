"""
CELPIP Listening Section — Seed Data
38 questions across 6 parts, mirroring the official CELPIP exam structure.

Part 1: Listening to Problem Solving         — 8 questions, 3 conversations
Part 2: Listening to a Daily Life Conversation — 5 questions, 1 conversation
Part 3: Listening for Information            — 6 questions, 1 recorded message
Part 4: Listening to a News Item             — 5 questions, 1 news report
Part 5: Listening to a Discussion            — 8 questions, 1 workplace discussion
Part 6: Listening for Viewpoints             — 6 questions, 1 interview
"""

# ---------------------------------------------------------------------------
# AUDIO SCRIPTS — defined once, then referenced inline in each question dict
# ---------------------------------------------------------------------------

_P1_CONV_A = """
[Phone ringing]

TENANT (Marcus): Hello?

PROPERTY MANAGER (Sandra): Hi, is this Marcus Okonkwo? This is Sandra Belliveau calling from Ridgeview Property Management.

MARCUS: Yes, hi Sandra. Thanks for calling back so quickly.

SANDRA: Of course. I got your maintenance request. You mentioned the heating in your unit isn't working properly?

MARCUS: That's right. It's been three days now. The thermostat reads twenty-two degrees but the apartment is freezing. I'd say it feels more like fifteen or sixteen.

SANDRA: I'm sorry to hear that. We did have a technician look at the building's furnace yesterday, and he replaced a faulty sensor, but it sounds like your unit may have an additional issue.

MARCUS: Is there anything I can do in the meantime? I have a young child at home and the cold is really affecting us.

SANDRA: Absolutely. I can send a portable electric heater up to your unit today — we keep a few on hand for exactly these situations. And I'll schedule our HVAC contractor to inspect your unit's baseboard heaters first thing tomorrow morning, between eight and ten a.m. Will someone be home?

MARCUS: Yes, I work from home so that's fine. But I'm a little concerned — this is the second time this winter the heat has gone out. Is there something more seriously wrong with the building system?

SANDRA: I understand your frustration, and that's a very fair question. The furnace is fifteen years old and we have been budgeting for a full replacement next spring. The board approved the capital expenditure at our last meeting. Until then, we're committed to responding to all heating calls within twenty-four hours.

MARCUS: Okay. And what about my heating bill? I've been running the stove to keep the place warm, which I know isn't safe, but I was desperate.

SANDRA: Please don't do that — it's a fire hazard. Use the portable unit we'll send up. As for costs, I'll make a note in your file. If the contractor confirms the baseboard units are faulty, we will credit your next month's rent by a pro-rated amount for the days without heat. I'll send you that in writing by email this afternoon.

MARCUS: That's reassuring. Thank you, Sandra.

SANDRA: Of course. You'll have the heater within two hours, and the contractor will be there tomorrow morning. Don't hesitate to call if anything changes.

MARCUS: Will do. Bye.

SANDRA: Goodbye.
"""

_P1_CONV_B = """
[Busy café background noise fades slightly]

CUSTOMER (Priya): Excuse me — I ordered a medium oat milk latte about fifteen minutes ago and I still haven't received it.

BARISTA (Ethan): Oh, I'm really sorry about that. Can I get your name?

PRIYA: Priya. Priya Sharma.

ETHAN: Let me check — [pause] — ah, I see what happened. Your order was entered under "Freya" by mistake, and that drink was actually called out about ten minutes ago but wasn't picked up. It's probably been sitting on the counter and is cold by now.

PRIYA: That explains it. I didn't recognize the name being called.

ETHAN: I sincerely apologize. I'll remake your drink right now at no charge and bump it to the front of the queue. It'll be ready in under two minutes. Can I also offer you a pastry for the wait?

PRIYA: That's very kind. Actually, can you make it a large instead of a medium since I've been waiting?

ETHAN: Absolutely, no problem at all. And going forward — if you ever order online, you can add a note in the "name" field so it prints exactly how you want it on the cup.

PRIYA: Good tip. I'll do that next time. One more thing — I noticed the loyalty points weren't added to my app for this purchase.

ETHAN: You're right — because I'm remaking it as a comp, the system won't auto-add them. But I can manually credit your account right now if you show me your app.

PRIYA: Here you go. [pause] Great.

ETHAN: Done — I've added two hundred bonus points as well for the inconvenience. Your large oat milk latte will be right up.

PRIYA: Thank you so much. I appreciate how you handled this.

ETHAN: Thank you for your patience. Enjoy your drink!
"""

_P1_CONV_C = """
[Office environment — keyboard clicks in background]

EMPLOYEE (Daniel): Hey Fatima, do you have a minute? I'm having a really frustrating problem with the new project management software.

COLLEAGUE (Fatima): Sure, Daniel. What's going on?

DANIEL: I've been trying to upload the quarterly budget spreadsheet to the Henderson project folder for the past hour, and every time I try, I get an error message that says "file type not supported."

FATIMA: Hmm. What format is the file in?

DANIEL: It's a standard Excel file — dot xlsx.

FATIMA: Okay, that should be fine. Is the file over twenty-five megabytes?

DANIEL: Let me check... it says nineteen point four megabytes.

FATIMA: It's not the size then. Oh — wait. Did you update your version of the software this morning? There was a mandatory update pushed out by IT at nine a.m. If you didn't install it, the system can't authenticate your uploads.

DANIEL: I did get a notification, but I postponed the update because I was in the middle of a call.

FATIMA: That's almost certainly the issue. The new version has a different upload authentication token. Until you update, the server rejects files even though the error message says "file type" — it's a bit misleading.

DANIEL: That's genuinely confusing. Why wouldn't it say "authentication error" instead?

FATIMA: I know, I brought that up with IT as well. They said they'd fix the error messaging in the next patch. For now, save your work, install the update — it takes about four minutes — and then try the upload again.

DANIEL: And if it still doesn't work after the update?

FATIMA: Then log a ticket with the IT helpdesk. Reference incident code UPL-dash-four-four-seven so they know it's related to the upload authentication bug. They're tracking it.

DANIEL: Perfect. Thanks, Fatima. I'll do the update right now.

FATIMA: Good luck. Let me know if you still have trouble.
"""

_P2_CONV = """
[Suburban home — doorbell rings, door opens]

NEIGHBOUR (Helen): Oh, hi Kevin! I wasn't expecting to see you — come in, come in.

KEVIN: Thanks, Helen. Sorry to drop by unannounced. I wanted to talk to you about the community garden plot next to mine.

HELEN: Of course, have a seat. Can I get you some tea?

KEVIN: I'm fine, thank you. So — as you know, I've been in plot number fourteen for about three years, and the plot right beside mine, number fifteen, has been sitting empty since the Nguyens moved away in September.

HELEN: Yes, I noticed that. I actually looked into it at the last garden association meeting. It turns out the Nguyens never formally transferred the lease back to the association, so technically the plot is still registered in their name.

KEVIN: Oh, that's a complication I didn't know about. So I can't just apply for it?

HELEN: Not until the association formally reclaims it. The process takes about two weeks — they have to send a registered letter to the Nguyens' last known address, wait for a response period, then vote at the next meeting to reassign the plot.

KEVIN: When is the next meeting?

HELEN: First Tuesday of next month. March fourth.

KEVIN: That's only two and a half weeks away. If I write a letter of interest now, would that put me at the front of the line?

HELEN: It would certainly help. The association does give priority to existing members in good standing, and you've been a member for three years. You should also mention any plans you have for the plot — they prefer applicants who have a clear growing plan. Last year there was a dispute because two members both wanted the same plot and neither had submitted a plan.

KEVIN: That's good advice. I was actually thinking of converting it into a pollinator garden — native plants, wildflowers, that sort of thing. I've already done some research on which species are native to Southern Ontario.

HELEN: Oh, the association would love that. We've been trying to attract more bees and butterflies to the whole garden. I'm on the committee, and I'll mention your interest informally — that's not against the rules.

KEVIN: I really appreciate that. Is there a specific person I should address the letter to?

HELEN: Send it to Marcella Ortiz — she's the plot allocation coordinator. Her email is on the association's website. Do it by end of this week to make sure she has it before the agenda is finalized.

KEVIN: Perfect. I'll do it tonight. Thanks so much, Helen — you've been incredibly helpful.

HELEN: Happy to help. I hope you get the plot — a pollinator garden would be wonderful.

KEVIN: Me too! Have a great evening.

HELEN: You too, Kevin. Take care.
"""

_P3_SCRIPT = """
[Recorded message — automated but professional tone]

Thank you for calling the City of Brampton Recreation and Culture Department. You have reached the registration information line for the Spring and Summer 2026 programs.

Please listen carefully as our menu options have changed.

For information about aquatic programs, including swimming lessons for children aged six months to seventeen years, adult lane swimming, and lifeguard certification courses, press one or stay on the line to hear general program details.

Spring session registration opens on Monday, March ninth at seven a.m. for residents and Monday, March sixteenth at seven a.m. for non-residents. Registration is available online at brampton-rec dot ca, in person at any of our eleven recreation centres, or by phone Monday through Friday from eight-thirty a.m. to four-thirty p.m.

Program fees vary by activity. Swimming lessons for children range from eighty-nine to one hundred and fifteen dollars per ten-week session. Adult fitness classes start at seventy-two dollars per session. Seniors aged sixty-five and over receive a fifteen percent discount on all programs. Low-income residents may apply for the Access Brampton subsidy, which can cover up to one hundred percent of registration fees. Applications for the subsidy are accepted year-round and processed within five business days.

Please note: the Chinguacousy Wellness Centre will be closed for scheduled maintenance from March second to March fifteenth. Participants registered in programs at that location during that period will be contacted by email and offered either a transfer to an alternate facility or a full refund.

All outdoor programs, including soccer, tennis, and summer camps, are weather-dependent. Cancellations due to weather are posted on the City of Brampton website and announced on the recreation hotline by six-thirty a.m. on the day of the program.

For accessibility accommodations, including programs adapted for individuals with physical or developmental disabilities, please press four or speak with a registration agent.

To repeat this message, press the star key. Thank you for calling the City of Brampton Recreation Department.
"""

_P4_SCRIPT = """
[News broadcast — anchor voice, professional tone]

ANCHOR (Carol Westman): Good evening. I'm Carol Westman. Our top story tonight: the federal government has announced a major investment in affordable housing, pledging eight billion dollars over five years to accelerate the construction of new rental units in cities across Canada.

Housing Minister Raymond Tse made the announcement this morning in Toronto, where the vacancy rate has dropped to one-point-two percent — the lowest in over thirty years.

MINISTER TSE [clip]: This investment will directly fund the construction of sixty thousand new affordable rental units by the year twenty-thirty. We are also streamlining the approval process with municipalities to cut red tape that has historically delayed construction by up to three years.

ANCHOR: The funding will flow through a new entity called the National Housing Acceleration Fund, which will distribute grants and low-interest loans directly to non-profit housing providers and municipal governments. Private developers will not be eligible unless they partner with a non-profit organization and commit to keeping at least forty percent of units below market rent for a minimum of thirty years.

Critics from the opposition and the housing advocacy community have offered mixed responses.

OPPOSITION CRITIC [clip]: Eight billion dollars sounds significant, but when you calculate the cost per unit, this will not come close to closing the gap. Canada needs at minimum two hundred thousand new units per year, and this plan produces only twelve thousand per year. It is too little, too late.

HOUSING ADVOCATE [clip]: The commitment to non-profits is welcome. What concerns us is the timeline — the units won't be ready for five years. People need housing today, not in twenty-thirty.

ANCHOR: The government has also announced a parallel measure: a temporary ban on short-term rental platforms operating in buildings with more than four units in cities with vacancy rates below two percent. The ban is expected to return an estimated twenty-two thousand units to the long-term rental market within six months.

Housing economists say the short-term rental ban could have a faster impact than the construction funding. In our next segment, we speak with urban planner Dr. Anika Rajan about what it will take to truly solve Canada's housing crisis. Stay with us.
"""

_P5_SCRIPT = """
[Office boardroom — sound of chairs, coffee cups]

CHAIR (Vivienne): Alright everyone, let's get started. As you know, we've been asked by senior leadership to develop a recommendation on whether Hartwell Communications should transition to a four-day workweek as a permanent policy. Today I want us to work through the evidence and land on a recommendation we can present by Friday. Let's hear from each of you.

OPERATIONS MANAGER (Greg): I'll start. From an operations standpoint, I ran the numbers from our six-month pilot. Productivity — measured by project completion rates — was up eight percent. Absenteeism dropped by twelve percent. Client satisfaction scores were unchanged. On the face of it, those numbers support making this permanent.

HR DIRECTOR (Amara): I want to add some context to Greg's data. The productivity gains were not uniform across departments. Customer service, which needs coverage five days a week, saw a fourteen percent increase in customer wait times during the pilot. They had to implement a rotating schedule, and honestly, several of those staff told me they found the rotation more stressful than a regular five-day week.

GREG: That's fair, Amara. I probably should have flagged that in my summary. The pilot worked best for knowledge workers — project teams, developers, the marketing group — where output is measurable by deliverables rather than hours.

FINANCE DIRECTOR (Sun-Li): From a financial perspective, we saw some savings — reduced utilities, lower overhead on days the office was closed. But we also absorbed some one-time costs: restructuring service contracts, overtime for customer service during coverage gaps. Net-net, over six months, we saved approximately forty-eight thousand dollars. That extrapolates to about ninety-six thousand annually, which sounds meaningful but is less than one percent of our operating budget.

VIVIENNE: So the financial impact is modest either way. Greg, what's your read on employee sentiment?

GREG: Overwhelmingly positive. Seventy-eight percent of employees said they would prefer the four-day week permanently. More interestingly, thirty-one percent said they would accept a slightly lower salary increase in the next compensation cycle in exchange for keeping the four-day schedule.

AMARA: That's a real data point — it suggests employees genuinely value it. But I worry about a two-tiered system where knowledge workers benefit and front-line staff carry the burden. If we move forward, we need a fair solution for all departments, not just the ones where it's easy to implement.

SUN-LI: What if we piloted a different model for customer service — perhaps a compressed workweek where they work four ten-hour days rather than five eight-hour days? It gives them the three-day weekend benefit without creating coverage gaps.

AMARA: That's worth exploring. It would need consultation with those staff specifically.

VIVIENNE: Okay. Let me try to synthesize. The evidence supports a modified, department-tailored approach rather than a blanket policy. We move forward with a permanent four-day week for knowledge-work departments, and we separately consult with customer service on a compressed schedule option. Agreed?

GREG: Agreed.

AMARA: Agreed — with the condition that we re-evaluate in twelve months with equity across departments as a key metric.

SUN-LI: I'm on board.

VIVIENNE: Good. I'll draft the recommendation document today. Greg, can you get me the department-by-department data by noon?

GREG: I'll have it to you by eleven.

VIVIENNE: Perfect. Thank you all. Let's reconvene Thursday if anyone has additions.
"""

_P6_SCRIPT = """
[Radio studio — interview format]

HOST (James Abara): Welcome back to The Long View on CBC Radio. I'm James Abara. Today we're discussing the growing debate over mandatory financial literacy education in Canadian high schools. I have two guests with very different perspectives. Dr. Nadia Kowalczyk is an economist and curriculum researcher at the University of Waterloo. And Marcus Thibodeau is a high school teacher and president of the Ontario Teachers' Federation. Welcome to you both.

DR. KOWALCZYK: Thank you, James.

MARCUS: Happy to be here.

JAMES: Dr. Kowalczyk, let's start with you. You've been advocating for mandatory financial literacy courses in Grade 11. Why?

DR. KOWALCZYK: Because the evidence is stark. The average Canadian carries over twenty-three thousand dollars in non-mortgage debt, and studies show that most adults cannot correctly explain how compound interest works. We are graduating students who are about to sign student loans, rent apartments, and open credit cards — with no formal instruction on any of it. A standalone mandatory course in Grade 11 would give students practical knowledge at exactly the moment they need it.

JAMES: Marcus, you've pushed back on this proposal. What's your concern?

MARCUS: My concern is not with financial literacy as a goal — I fully support it. My concern is where the time comes from. Ontario's Grade 11 curriculum is already overloaded. Every few years a new mandatory course gets added, and something else gets squeezed out or teachers are expected to cover more in the same time. If we add a financial literacy credit, we need to be honest about what we're removing.

JAMES: Dr. Kowalczyk, how do you respond to that?

DR. KOWALCZYK: I'd say the answer is integration, not addition. We don't necessarily need a brand-new standalone credit. Financial concepts can be integrated into existing mathematics, social studies, and even English courses. Reading a mortgage contract is a literacy skill. Calculating interest is mathematics. But — and this is crucial — integration only works if teachers are trained and if the curriculum explicitly requires it. Right now, it's optional, which means it's inconsistent.

MARCUS: I actually agree with the integration model in principle. Where I get nervous is the training piece. To integrate financial literacy meaningfully, you need teachers who are confident with the material. Most of us were never trained in personal finance ourselves. Professional development is chronically underfunded. So you're asking us to do more, without the tools to do it well.

JAMES: So both of you see the goal the same way but disagree on the mechanism and the support structures?

DR. KOWALCZYK: Essentially, yes. I'd also argue the urgency justifies some investment. The cost of underfunded professional development is real, but so is the cost of a generation managing debt without the knowledge to do it responsibly.

MARCUS: Fair point. I would support a phased approach — pilot programs in willing schools, proper funding for teacher training, then a province-wide rollout. What I resist is a top-down mandate with no resources attached.

JAMES: A reasonable place to meet. We'll take a short break and come back with your calls. Stay with us on The Long View.
"""

# ---------------------------------------------------------------------------
# LISTENING QUESTIONS LIST
# ---------------------------------------------------------------------------

LISTENING_QUESTIONS = [

    # =========================================================================
    # PART 1 — Listening to Problem Solving (8 questions, 3 conversations)
    # Conversation A: Questions 1–3  (heating problem with property manager)
    # Conversation B: Questions 4–5  (café order mix-up)
    # Conversation C: Questions 6–8  (workplace software issue)
    # =========================================================================

    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 1,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_A,
        "question_text": "Why has Marcus contacted the property management office?",
        "options": [
            "His apartment thermostat is broken and needs to be replaced",
            "The heating in his unit has not been working for several days",
            "He wants to dispute a charge on his monthly rent bill",
            "He is concerned about a fire hazard in the building"
        ],
        "correct_answer": "B",
        "explanation": "Marcus states clearly that the heating in his unit has not been working properly for three days, which is why he submitted a maintenance request.",
        "difficulty": 1.0,
        "tags": ["problem solving", "housing", "tenant", "main idea"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 2,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_A,
        "question_text": "What immediate solution does Sandra offer Marcus?",
        "options": [
            "She will send a technician to replace the building furnace today",
            "She will arrange for Marcus to move to a warmer unit temporarily",
            "She will send a portable electric heater to his apartment",
            "She will reduce his rent until the heating system is fixed"
        ],
        "correct_answer": "C",
        "explanation": "Sandra offers to send a portable electric heater to Marcus's unit that same day while the contractor inspection is arranged for the following morning.",
        "difficulty": 1.0,
        "tags": ["problem solving", "housing", "detail", "solution"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 3,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_A,
        "question_text": "What does Sandra say she will do regarding Marcus's heating costs?",
        "options": [
            "She will waive Marcus's rent for the entire month",
            "She will credit his rent by a pro-rated amount if the contractor confirms the fault",
            "She will pay his electricity bill for the month",
            "She will apply for a government heating subsidy on his behalf"
        ],
        "correct_answer": "B",
        "explanation": "Sandra says she will credit Marcus's next month's rent by a pro-rated amount for the days without heat, but only if the contractor confirms the baseboard units are faulty.",
        "difficulty": 1.0,
        "tags": ["problem solving", "housing", "detail", "compensation"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 4,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_B,
        "question_text": "What was the cause of Priya's order not being ready?",
        "options": [
            "The café ran out of oat milk and could not make her drink",
            "Her name was entered incorrectly and the drink was called under a different name",
            "The online ordering system failed to send her order to the kitchen",
            "She had been waiting at the wrong counter in the café"
        ],
        "correct_answer": "B",
        "explanation": "Ethan explains that Priya's order was entered under the name 'Freya' by mistake, so when the drink was called out, Priya did not recognize the name and did not pick it up.",
        "difficulty": 1.0,
        "tags": ["problem solving", "customer service", "café", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 5,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_B,
        "question_text": "In addition to remaking Priya's drink for free, what extra compensation does Ethan offer?",
        "options": [
            "A gift card to use on her next visit to the café",
            "A free pastry and an upgrade to a large size",
            "A full refund and two hundred loyalty points",
            "A coupon for a discount on her next online order"
        ],
        "correct_answer": "B",
        "explanation": "Ethan offers Priya both a free pastry for the wait and agrees to upgrade her drink from a medium to a large at no extra charge. He also adds bonus loyalty points, but the initial offer beyond the free remake is the pastry and the size upgrade.",
        "difficulty": 1.0,
        "tags": ["problem solving", "customer service", "detail", "compensation"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 6,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_C,
        "question_text": "What is the real reason Daniel cannot upload his file, according to Fatima?",
        "options": [
            "The file is too large for the system's upload limit",
            "The Excel file format is not supported by the new software",
            "He has not installed a mandatory software update that changes upload authentication",
            "His user account does not have the correct permissions to access that project folder"
        ],
        "correct_answer": "C",
        "explanation": "Fatima explains that a mandatory software update was pushed out by IT at 9 a.m. and that failing to install it means the server cannot authenticate uploads. The error message saying 'file type not supported' is misleading.",
        "difficulty": 1.0,
        "tags": ["problem solving", "workplace", "technology", "inference"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 7,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_C,
        "question_text": "What does Fatima suggest Daniel do if the problem continues after installing the update?",
        "options": [
            "Contact the software vendor directly to report the bug",
            "Submit a helpdesk ticket referencing a specific incident code",
            "Ask his manager to upload the file on his behalf",
            "Convert the file to a different format before uploading"
        ],
        "correct_answer": "B",
        "explanation": "Fatima advises Daniel to log a ticket with the IT helpdesk and reference incident code UPL-447 so they know it is related to the tracked upload authentication bug.",
        "difficulty": 1.0,
        "tags": ["problem solving", "workplace", "technology", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 1,
        "part_title": "Listening to Problem Solving",
        "question_number": 8,
        "question_type": "multiple_choice",
        "audio_script": _P1_CONV_C,
        "question_text": "What does Fatima say about the misleading error message?",
        "options": [
            "She reported it to the software vendor last week",
            "She raised the issue with IT, who plan to fix it in a future patch",
            "She believes it is intentional to prevent unauthorized uploads",
            "She says the error message will be fixed once Daniel updates his software"
        ],
        "correct_answer": "B",
        "explanation": "Fatima says she raised the issue of the misleading error message with IT, and they acknowledged it would be corrected in the next patch.",
        "difficulty": 1.0,
        "tags": ["problem solving", "workplace", "technology", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },

    # =========================================================================
    # PART 2 — Listening to a Daily Life Conversation (5 questions, 1 conversation)
    # Conversation: Kevin and Helen discuss the community garden plot
    # =========================================================================

    {
        "section": "listening",
        "part": 2,
        "part_title": "Listening to a Daily Life Conversation",
        "question_number": 1,
        "question_type": "multiple_choice",
        "audio_script": _P2_CONV,
        "question_text": "Why is the garden plot next to Kevin's currently unavailable?",
        "options": [
            "The association has already assigned it to another member",
            "It is being renovated by the city's parks department",
            "The previous tenants never formally transferred the lease back to the association",
            "The plot was damaged over the winter and is not ready for use"
        ],
        "correct_answer": "C",
        "explanation": "Helen explains that the Nguyens, who previously held the plot, moved away but never formally returned the lease to the association, so it is still registered in their name.",
        "difficulty": 1.0,
        "tags": ["daily life", "community", "housing", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "part_title": "Listening to a Daily Life Conversation",
        "question_number": 2,
        "question_type": "multiple_choice",
        "audio_script": _P2_CONV,
        "question_text": "When is the next garden association meeting where the plot reassignment could be voted on?",
        "options": [
            "The last Tuesday of February",
            "The first Tuesday of March",
            "The second Monday of March",
            "The first Saturday of April"
        ],
        "correct_answer": "B",
        "explanation": "Helen states clearly that the next meeting is on the first Tuesday of next month — March fourth — which is when the association would vote on reassigning the plot.",
        "difficulty": 1.0,
        "tags": ["daily life", "community", "scheduling", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "part_title": "Listening to a Daily Life Conversation",
        "question_number": 3,
        "question_type": "multiple_choice",
        "audio_script": _P2_CONV,
        "question_text": "What does Helen advise Kevin to include in his letter of interest?",
        "options": [
            "A list of plants he has grown in his current plot over three years",
            "A letter of recommendation from another association member",
            "A detailed growing plan for how he intends to use the plot",
            "A deposit payment to hold his place in the application queue"
        ],
        "correct_answer": "C",
        "explanation": "Helen advises Kevin to mention his plans for the plot, because the association prefers applicants with a clear growing plan. She references a past dispute where neither applicant had submitted one.",
        "difficulty": 1.0,
        "tags": ["daily life", "community", "advice", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "part_title": "Listening to a Daily Life Conversation",
        "question_number": 4,
        "question_type": "multiple_choice",
        "audio_script": _P2_CONV,
        "question_text": "What type of garden does Kevin plan to create in the new plot?",
        "options": [
            "A vegetable and herb garden for personal food production",
            "A children's educational garden with raised beds",
            "A pollinator garden with native wildflowers and plants",
            "A fruit orchard with apple and pear trees"
        ],
        "correct_answer": "C",
        "explanation": "Kevin tells Helen he wants to create a pollinator garden using native plants and wildflowers, and mentions he has already researched species native to Southern Ontario.",
        "difficulty": 1.0,
        "tags": ["daily life", "community", "environment", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 2,
        "part_title": "Listening to a Daily Life Conversation",
        "question_number": 5,
        "question_type": "multiple_choice",
        "audio_script": _P2_CONV,
        "question_text": "What does Helen offer to do to help Kevin's application?",
        "options": [
            "Write a formal letter of support on his behalf as a committee member",
            "Mention his interest informally to the committee before the meeting",
            "Reserve the plot for him until the next association meeting",
            "Contact the Nguyens to ask them to release the lease sooner"
        ],
        "correct_answer": "B",
        "explanation": "Helen says that as a committee member she can informally mention Kevin's interest before the meeting, and notes this is permitted within the rules. She does not offer to write a formal letter.",
        "difficulty": 1.0,
        "tags": ["daily life", "community", "inference", "support"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },

    # =========================================================================
    # PART 3 — Listening for Information (6 questions, 1 recorded message)
    # Recording: City of Brampton Recreation Department automated phone message
    # =========================================================================

    {
        "section": "listening",
        "part": 3,
        "part_title": "Listening for Information",
        "question_number": 1,
        "question_type": "multiple_choice",
        "audio_script": _P3_SCRIPT,
        "question_text": "When can Brampton residents begin registering for Spring programs?",
        "options": [
            "Monday, March second at seven a.m.",
            "Monday, March ninth at seven a.m.",
            "Monday, March sixteenth at seven a.m.",
            "Monday, March twenty-third at eight-thirty a.m."
        ],
        "correct_answer": "B",
        "explanation": "The recorded message states that Spring session registration opens on Monday, March ninth at seven a.m. for residents. Non-residents must wait until March sixteenth.",
        "difficulty": 1.0,
        "tags": ["information", "municipal services", "scheduling", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "part_title": "Listening for Information",
        "question_number": 2,
        "question_type": "multiple_choice",
        "audio_script": _P3_SCRIPT,
        "question_text": "Which discount is available to seniors aged 65 and over?",
        "options": [
            "Ten percent off all registered programs",
            "Fifteen percent off all programs",
            "Twenty percent off aquatic programs only",
            "Free registration for one program per season"
        ],
        "correct_answer": "B",
        "explanation": "The message specifies that seniors aged sixty-five and over receive a fifteen percent discount on all programs.",
        "difficulty": 1.0,
        "tags": ["information", "municipal services", "discount", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "part_title": "Listening for Information",
        "question_number": 3,
        "question_type": "multiple_choice",
        "audio_script": _P3_SCRIPT,
        "question_text": "What will happen to participants registered at the Chinguacousy Wellness Centre during its closure?",
        "options": [
            "Their programs will be cancelled with no compensation offered",
            "They will be placed on a waiting list for the following session",
            "They will be contacted and offered a transfer or a full refund",
            "Their programs will be relocated to the nearest available centre automatically"
        ],
        "correct_answer": "C",
        "explanation": "The message states that participants in programs at the Chinguacousy Wellness Centre during the March second to fifteenth closure period will be contacted by email and offered either a transfer to an alternate facility or a full refund.",
        "difficulty": 1.0,
        "tags": ["information", "municipal services", "policy", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "part_title": "Listening for Information",
        "question_number": 4,
        "question_type": "multiple_choice",
        "audio_script": _P3_SCRIPT,
        "question_text": "How can residents find out if an outdoor program has been cancelled due to weather?",
        "options": [
            "By calling the program instructor directly before the class",
            "By checking the City of Brampton website or the recreation hotline by six-thirty a.m.",
            "By subscribing to the city's text message alert service",
            "By checking the notice board at their local recreation centre"
        ],
        "correct_answer": "B",
        "explanation": "The message explains that weather-related cancellations are posted on the City of Brampton website and announced on the recreation hotline by six-thirty a.m. on the day of the program.",
        "difficulty": 1.0,
        "tags": ["information", "municipal services", "weather", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "part_title": "Listening for Information",
        "question_number": 5,
        "question_type": "multiple_choice",
        "audio_script": _P3_SCRIPT,
        "question_text": "What is the Access Brampton subsidy designed to help with?",
        "options": [
            "Paying for transportation to and from recreation centres",
            "Covering up to one hundred percent of program registration fees for low-income residents",
            "Providing free equipment rental for registered program participants",
            "Funding after-school childcare at recreation facilities"
        ],
        "correct_answer": "B",
        "explanation": "The message states that the Access Brampton subsidy is available to low-income residents and can cover up to one hundred percent of registration fees. Applications are accepted year-round.",
        "difficulty": 1.0,
        "tags": ["information", "municipal services", "subsidy", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 3,
        "part_title": "Listening for Information",
        "question_number": 6,
        "question_type": "multiple_choice",
        "audio_script": _P3_SCRIPT,
        "question_text": "Which of the following is NOT listed as a way to register for programs?",
        "options": [
            "Online at the city recreation website",
            "In person at any of the eleven recreation centres",
            "By mailing a completed registration form to the department",
            "By phone on weekdays during business hours"
        ],
        "correct_answer": "C",
        "explanation": "The message lists three registration methods: online, in person at any of eleven recreation centres, and by phone Monday through Friday. Mailing a form is not mentioned.",
        "difficulty": 1.0,
        "tags": ["information", "municipal services", "registration", "inference"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },

    # =========================================================================
    # PART 4 — Listening to a News Item (5 questions, 1 news report)
    # Report: Federal affordable housing investment announcement
    # =========================================================================

    {
        "section": "listening",
        "part": 4,
        "part_title": "Listening to a News Item",
        "question_number": 1,
        "question_type": "multiple_choice",
        "audio_script": _P4_SCRIPT,
        "question_text": "What is the main purpose of the federal government's eight billion dollar investment?",
        "options": [
            "To purchase and renovate existing rental buildings across Canada",
            "To fund the construction of sixty thousand new affordable rental units by 2030",
            "To provide direct rent subsidies to low-income Canadians",
            "To give tax credits to private developers who build affordable housing"
        ],
        "correct_answer": "B",
        "explanation": "Housing Minister Tse states in his clip that the investment will directly fund the construction of sixty thousand new affordable rental units by the year 2030.",
        "difficulty": 1.0,
        "tags": ["news", "housing", "government policy", "main idea"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 4,
        "part_title": "Listening to a News Item",
        "question_number": 2,
        "question_type": "multiple_choice",
        "audio_script": _P4_SCRIPT,
        "question_text": "Under what condition can private developers access the National Housing Acceleration Fund?",
        "options": [
            "If they agree to build in cities where vacancy rates are below two percent",
            "If they partner with a non-profit and keep at least forty percent of units below market rent for thirty years",
            "If they commit to constructing a minimum of five hundred units per project",
            "If they receive approval from both the federal and provincial housing ministries"
        ],
        "correct_answer": "B",
        "explanation": "The anchor explains that private developers are not eligible unless they partner with a non-profit organization and commit to keeping at least forty percent of units below market rent for a minimum of thirty years.",
        "difficulty": 1.0,
        "tags": ["news", "housing", "government policy", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 4,
        "part_title": "Listening to a News Item",
        "question_number": 3,
        "question_type": "multiple_choice",
        "audio_script": _P4_SCRIPT,
        "question_text": "What is the opposition critic's main criticism of the housing investment plan?",
        "options": [
            "The funding is directed to non-profits rather than experienced private developers",
            "The plan only produces about twelve thousand units per year, far less than what is needed",
            "The government has not consulted with municipalities before making the announcement",
            "The money will be used to renovate existing units rather than build new ones"
        ],
        "correct_answer": "B",
        "explanation": "The opposition critic argues that at twelve thousand units per year, the plan falls far short of the estimated two hundred thousand new units Canada needs annually, calling it 'too little, too late.'",
        "difficulty": 1.0,
        "tags": ["news", "housing", "opinion", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 4,
        "part_title": "Listening to a News Item",
        "question_number": 4,
        "question_type": "multiple_choice",
        "audio_script": _P4_SCRIPT,
        "question_text": "What is the purpose of the government's ban on short-term rentals?",
        "options": [
            "To generate additional tax revenue from the short-term rental industry",
            "To protect tourists from fraudulent short-term rental listings",
            "To return thousands of units to the long-term rental market",
            "To ensure rental platforms comply with new federal safety regulations"
        ],
        "correct_answer": "C",
        "explanation": "The anchor explains that the short-term rental ban is expected to return an estimated twenty-two thousand units to the long-term rental market within six months.",
        "difficulty": 1.0,
        "tags": ["news", "housing", "government policy", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 4,
        "part_title": "Listening to a News Item",
        "question_number": 5,
        "question_type": "multiple_choice",
        "audio_script": _P4_SCRIPT,
        "question_text": "According to the news report, what does the housing advocate find most concerning about the construction funding?",
        "options": [
            "That non-profit organizations do not have the capacity to manage large construction projects",
            "That the units will not be ready for approximately five years",
            "That the funding favours large cities over smaller communities",
            "That the government has not committed to maintaining affordability after thirty years"
        ],
        "correct_answer": "B",
        "explanation": "The housing advocate says the commitment to non-profits is welcome but expresses concern about the timeline — the units won't be ready for five years, while people need housing today.",
        "difficulty": 1.0,
        "tags": ["news", "housing", "opinion", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },

    # =========================================================================
    # PART 5 — Listening to a Discussion (8 questions, 1 workplace discussion)
    # Discussion: Hartwell Communications four-day workweek recommendation meeting
    # =========================================================================

    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 1,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "What is the overall purpose of this meeting?",
        "options": [
            "To review the financial results of the last fiscal quarter",
            "To develop a recommendation on whether to permanently adopt a four-day workweek",
            "To address complaints from customer service staff about their scheduling",
            "To decide how to allocate the company's professional development budget"
        ],
        "correct_answer": "B",
        "explanation": "Vivienne opens the meeting by stating they have been asked by senior leadership to develop a recommendation on whether Hartwell Communications should transition to a four-day workweek as a permanent policy.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "main idea"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 2,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "According to Greg's data from the pilot, which outcome improved the most?",
        "options": [
            "Client satisfaction scores increased by eight percent",
            "Absenteeism decreased by twelve percent",
            "Project completion rates increased by twenty percent",
            "Employee turnover dropped to a historic low"
        ],
        "correct_answer": "B",
        "explanation": "Greg reports that productivity was up eight percent and absenteeism dropped by twelve percent, making the drop in absenteeism the largest single improvement mentioned.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "data", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 3,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "What concern does Amara raise about the pilot's results?",
        "options": [
            "Productivity gains were lower than projected for the marketing team",
            "The customer service department saw increased wait times and staff stress during the pilot",
            "Several senior managers refused to participate in the pilot program",
            "The pilot was not long enough to produce statistically reliable data"
        ],
        "correct_answer": "B",
        "explanation": "Amara notes that customer service had to implement a rotating schedule, which increased customer wait times by fourteen percent, and that some staff found the rotation more stressful than a regular five-day week.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "concern", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 4,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "What does Sun-Li say about the financial impact of the pilot?",
        "options": [
            "The company lost money overall due to overtime and service contract costs",
            "The savings were significant and represented more than five percent of the operating budget",
            "Net savings were approximately ninety-six thousand dollars annually but less than one percent of the operating budget",
            "Financial data from the pilot was inconclusive and requires further analysis"
        ],
        "correct_answer": "C",
        "explanation": "Sun-Li states that the net savings over six months were approximately forty-eight thousand dollars — extrapolating to about ninety-six thousand annually — but notes this is less than one percent of the operating budget.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "finance", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 5,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "What does the employee survey data reveal about staff preferences?",
        "options": [
            "Sixty percent of employees prefer a traditional five-day workweek for work-life balance",
            "Seventy-eight percent prefer the four-day week, with some willing to accept lower salary increases to keep it",
            "Most employees were neutral and said the schedule had no effect on their satisfaction",
            "Employees in the customer service department voted against the four-day week"
        ],
        "correct_answer": "B",
        "explanation": "Greg reports that seventy-eight percent of employees prefer the four-day week permanently, and thirty-one percent would accept a slightly lower salary increase in exchange for keeping the schedule.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "employee sentiment", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 6,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "What alternative model does Sun-Li suggest for customer service staff?",
        "options": [
            "A staggered five-day schedule with flexible start times",
            "A compressed four-day week with ten-hour shifts to maintain coverage",
            "A rotating part-time contract with premium pay for weekend hours",
            "A fully remote work option to allow greater scheduling flexibility"
        ],
        "correct_answer": "B",
        "explanation": "Sun-Li proposes that customer service staff work four ten-hour days instead of five eight-hour days — a compressed workweek that gives them a three-day weekend without creating coverage gaps.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "solution", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 7,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "What condition does Amara attach to her agreement with Vivienne's summary recommendation?",
        "options": [
            "Customer service staff must be consulted before any policy is announced company-wide",
            "The policy must be reviewed in twelve months with departmental equity as a key metric",
            "A separate budget must be allocated for customer service overtime costs",
            "Senior leadership must approve the final recommendation before it takes effect"
        ],
        "correct_answer": "B",
        "explanation": "Amara agrees to the recommendation on the condition that the policy is re-evaluated in twelve months, with equity across departments listed as a key assessment metric.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "condition", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 5,
        "part_title": "Listening to a Discussion",
        "question_number": 8,
        "question_type": "multiple_choice",
        "audio_script": _P5_SCRIPT,
        "question_text": "Based on the discussion, which type of employee benefited most from the four-day workweek pilot?",
        "options": [
            "Customer service representatives who deal with clients directly",
            "Senior managers who attend frequent inter-departmental meetings",
            "Knowledge workers in project teams, development, and marketing",
            "Part-time and contract employees on flexible schedules"
        ],
        "correct_answer": "C",
        "explanation": "Greg explicitly states that the pilot worked best for knowledge workers — project teams, developers, and the marketing group — where output is measurable by deliverables rather than hours of coverage.",
        "difficulty": 1.0,
        "tags": ["discussion", "workplace", "inference", "synthesis"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },

    # =========================================================================
    # PART 6 — Listening for Viewpoints (6 questions, 1 interview)
    # Interview: CBC Radio debate on mandatory financial literacy in schools
    # =========================================================================

    {
        "section": "listening",
        "part": 6,
        "part_title": "Listening for Viewpoints",
        "question_number": 1,
        "question_type": "multiple_choice",
        "audio_script": _P6_SCRIPT,
        "question_text": "What evidence does Dr. Kowalczyk use to support her argument for mandatory financial literacy education?",
        "options": [
            "A survey showing that high school students request more practical courses",
            "Statistics showing high Canadian household debt and poor understanding of compound interest",
            "Data comparing Canadian graduation rates to countries with mandatory financial education",
            "Research showing that financial stress is the leading cause of student dropout"
        ],
        "correct_answer": "B",
        "explanation": "Dr. Kowalczyk cites that the average Canadian carries over twenty-three thousand dollars in non-mortgage debt and that most adults cannot correctly explain how compound interest works.",
        "difficulty": 1.0,
        "tags": ["viewpoints", "education", "evidence", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 6,
        "part_title": "Listening for Viewpoints",
        "question_number": 2,
        "question_type": "multiple_choice",
        "audio_script": _P6_SCRIPT,
        "question_text": "What is Marcus Thibodeau's primary concern about adding a mandatory financial literacy course?",
        "options": [
            "He believes students are not mature enough to understand financial concepts in Grade 11",
            "He argues that the course would be too expensive for school boards to implement",
            "He is worried about an already overloaded curriculum and what would be removed to make space",
            "He thinks financial education is better delivered by parents at home"
        ],
        "correct_answer": "C",
        "explanation": "Marcus states clearly that his concern is with the already overloaded Ontario Grade 11 curriculum and asks where the time would come from — what would be cut to add the new course.",
        "difficulty": 1.0,
        "tags": ["viewpoints", "education", "concern", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 6,
        "part_title": "Listening for Viewpoints",
        "question_number": 3,
        "question_type": "multiple_choice",
        "audio_script": _P6_SCRIPT,
        "question_text": "What approach does Dr. Kowalczyk propose as an alternative to a standalone course?",
        "options": [
            "Offering financial literacy as an optional elective in Grades 10 through 12",
            "Partnering with banks to deliver financial education through after-school workshops",
            "Integrating financial concepts into existing subjects like math, social studies, and English",
            "Creating an online self-directed financial literacy module students complete at home"
        ],
        "correct_answer": "C",
        "explanation": "Dr. Kowalczyk suggests integrating financial concepts into existing subjects — she gives examples such as reading mortgage contracts as a literacy skill and calculating interest as mathematics.",
        "difficulty": 1.0,
        "tags": ["viewpoints", "education", "solution", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 6,
        "part_title": "Listening for Viewpoints",
        "question_number": 4,
        "question_type": "multiple_choice",
        "audio_script": _P6_SCRIPT,
        "question_text": "Why does Marcus express concern about the integration model that Dr. Kowalczyk proposes?",
        "options": [
            "He believes students learn financial skills better in a dedicated course environment",
            "He argues that current teachers lack the personal finance training needed to teach it effectively",
            "He worries that integrating financial concepts would confuse students in core subjects",
            "He thinks the integration model has already been tried and proven ineffective in other provinces"
        ],
        "correct_answer": "B",
        "explanation": "Marcus supports the integration model in principle but warns that it only works if teachers are properly trained — and that most teachers were never trained in personal finance themselves. He adds that professional development is chronically underfunded.",
        "difficulty": 1.0,
        "tags": ["viewpoints", "education", "concern", "inference"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 6,
        "part_title": "Listening for Viewpoints",
        "question_number": 5,
        "question_type": "multiple_choice",
        "audio_script": _P6_SCRIPT,
        "question_text": "On which key point do Dr. Kowalczyk and Marcus Thibodeau fundamentally agree?",
        "options": [
            "That a mandatory standalone credit is the best solution for financial literacy",
            "That financial literacy education is an important goal for Ontario students",
            "That the provincial government should fully fund all teacher professional development",
            "That financial literacy belongs exclusively in the mathematics curriculum"
        ],
        "correct_answer": "B",
        "explanation": "Marcus explicitly says 'My concern is not with financial literacy as a goal — I fully support it.' Both guests agree on the goal; their disagreement is about the mechanism and resources.",
        "difficulty": 1.0,
        "tags": ["viewpoints", "education", "agreement", "inference"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "listening",
        "part": 6,
        "part_title": "Listening for Viewpoints",
        "question_number": 6,
        "question_type": "multiple_choice",
        "audio_script": _P6_SCRIPT,
        "question_text": "What approach does Marcus propose as a compromise for implementing financial literacy education?",
        "options": [
            "Waiting for the federal government to create a national curriculum framework first",
            "A phased approach — pilot programs in willing schools with proper funding, then a province-wide rollout",
            "Introducing financial literacy only in vocational and trades-focused high schools",
            "Allowing individual teachers to voluntarily incorporate financial topics into their lessons"
        ],
        "correct_answer": "B",
        "explanation": "Marcus proposes a phased approach: pilot programs in willing schools with proper teacher training funding, followed by a province-wide rollout. He says he resists a top-down mandate with no resources attached.",
        "difficulty": 1.0,
        "tags": ["viewpoints", "education", "compromise", "detail"],
        "passage_text": None,
        "audio_path": None,
        "image_path": None,
    },
]

# ---------------------------------------------------------------------------
# Sanity checks (run when module is imported directly)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from collections import Counter

    total = len(LISTENING_QUESTIONS)
    by_part = Counter(q["part"] for q in LISTENING_QUESTIONS)
    print(f"Total questions: {total}  (expected 38)")
    for part_num in sorted(by_part):
        print(f"  Part {part_num}: {by_part[part_num]} questions")

    required_keys = {
        "section", "part", "part_title", "question_number", "question_type",
        "audio_script", "question_text", "options", "correct_answer",
        "explanation", "difficulty", "tags", "passage_text", "audio_path",
        "image_path",
    }
    for i, q in enumerate(LISTENING_QUESTIONS):
        missing = required_keys - q.keys()
        if missing:
            print(f"  WARNING: Question index {i} missing keys: {missing}")
        if not isinstance(q["options"], list) or len(q["options"]) != 4:
            print(f"  WARNING: Question index {i} options not a list of 4")
        if q["correct_answer"] not in ("A", "B", "C", "D"):
            print(f"  WARNING: Question index {i} invalid correct_answer: {q['correct_answer']}")

    print("Validation complete.")
