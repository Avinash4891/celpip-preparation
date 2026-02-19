"""
CELPIP Speaking Section Prompts
Tasks 1–8: All task types with 30-second preparation and variable response times.
"""

SPEAKING_PROMPTS = [
    {
        "section": "speaking",
        "part": 1,
        "part_title": "Giving Advice",
        "question_number": 1,
        "question_type": "giving_advice",
        "question_text": (
            "Your neighbour, Marcus, recently moved to Calgary from another country and is "
            "struggling to find his first job in Canada. He has a degree in civil engineering "
            "from his home country but his credentials have not yet been recognized here. "
            "He feels discouraged and is not sure where to start.\n\n"
            "Give Marcus advice on what he should do. You have 30 seconds to prepare and "
            "90 seconds to speak."
        ),
        "options": {
            "task_type": "giving_advice",
            "prep_seconds": 30,
            "response_seconds": 90,
            "tips": [
                "Open with empathy — acknowledge Marcus's situation before jumping into advice",
                "Give 3 concrete, actionable steps (e.g., contact Engineers Canada, join LinkedIn, volunteer) — vague advice scores lower",
                "Use advisory language throughout: 'I would suggest', 'it might be worth', 'one effective approach is'",
                "Mention at least one Canadian-specific resource such as a provincial licensing body or settlement agency",
                "Close with an encouraging statement to show task fulfillment and natural closure",
            ],
            "scoring_rubric": [
                "Content/Coherence: Practical advice given; ideas flow logically; opening and closing are present",
                "Vocabulary: Advisory and professional vocabulary used accurately; no awkward repetition",
                "Listenability: Pace is comfortable; pronunciation is clear; filler words are minimal",
                "Task Fulfillment: Advice is relevant to Marcus's specific situation; Canadian context acknowledged",
            ],
            "sample_band10_response": (
                "Marcus, I really understand how frustrating this situation must be, especially "
                "after working so hard to build your career. Here is what I would suggest. "
                "First, contact Engineers Canada and the Association of Professional Engineers "
                "of Alberta as soon as possible — they can guide you through the credential "
                "recognition process and tell you exactly what exams or bridging programs you "
                "need. Second, I would strongly recommend updating your LinkedIn profile and "
                "connecting with other engineers in Calgary. Many job opportunities come through "
                "professional networks, not just job boards. Third, consider volunteering with "
                "a local engineering firm or community project while your credentials are being "
                "processed. This builds Canadian work experience and references, which employers "
                "here value highly. Finally, your local newcomer settlement centre can connect "
                "you with mentorship programs designed specifically for internationally trained "
                "professionals. You have strong skills, Marcus — with the right strategy, "
                "I am confident you will find your footing here."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task1", "giving-advice", "newcomer", "employment", "calgary"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 2,
        "part_title": "Talking about a Personal Experience",
        "question_number": 1,
        "question_type": "personal_experience",
        "question_text": (
            "Describe a time when you had to adapt quickly to an unexpected change in your "
            "life — such as a sudden move to a new city, an unexpected career shift, or a "
            "change in your family situation. What happened, how did you handle it, and "
            "what did you learn from the experience?\n\n"
            "You have 30 seconds to prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "personal_experience",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "Use the STAR structure: Situation, Task/Challenge, Action you took, Result/Lesson — cover all four in 60 seconds",
                "Use consistent past tense throughout; mix simple and complex past forms for variety",
                "Be specific — name a real-sounding city, job, or detail to make your story vivid and credible",
                "Include one clear emotional reflection ('I initially felt overwhelmed, but...') to show depth",
                "Finish with the lesson learned in a single, memorable sentence — this completes the task",
            ],
            "scoring_rubric": [
                "Content/Coherence: A complete narrative arc is present; events are in logical order",
                "Vocabulary: Narrative and reflective vocabulary used naturally; past tense forms are accurate",
                "Listenability: Story is easy to follow; speaker sounds natural and engaged",
                "Task Fulfillment: All three elements addressed — what happened, how handled, what learned",
            ],
            "sample_band10_response": (
                "Two years ago, I was living in Winnipeg and working as a graphic designer when "
                "my company announced it was closing our office with only three weeks' notice. "
                "I had a mortgage and a family to support, so the pressure was enormous. "
                "I immediately updated my portfolio, reached out to my professional network, "
                "and registered with two recruitment agencies. Within ten days, I had secured "
                "a contract position with a marketing firm in Toronto, which meant relocating "
                "my entire family within a month. It was stressful and exhausting, but we "
                "managed it together. That experience taught me that being adaptable and "
                "maintaining strong professional relationships are far more valuable than "
                "any single job. I now actively invest in my network so I am never starting "
                "from scratch in a difficult situation."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task2", "personal-experience", "adaptability", "narrative"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 3,
        "part_title": "Describing a Scene",
        "question_number": 1,
        "question_type": "describing_scene",
        "question_text": (
            "Look at the image of a busy farmers market in Vancouver on a Saturday morning. "
            "The market is set up in an outdoor plaza surrounded by maple trees just beginning "
            "to show autumn colours. There are approximately twelve vendor stalls selling "
            "fresh produce, baked goods, handmade crafts, and cut flowers. A musician plays "
            "acoustic guitar near the entrance. Customers of various ages browse the stalls — "
            "some carry reusable shopping bags, others push strollers. A young child reaches "
            "toward a display of orange pumpkins while her parent pays a vendor.\n\n"
            "Describe what you see in as much detail as possible. You have 30 seconds to "
            "prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "describing_scene",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "Organize spatially — describe from foreground to background, or left to right; avoid random jumping between elements",
                "Use present continuous tense throughout ('a vendor is arranging', 'children are running') to show the scene is alive",
                "Include colours, quantities, and textures to demonstrate vocabulary range — 'vibrant orange pumpkins', 'weathered wooden stalls'",
                "Mention the overall atmosphere or mood in one sentence to show higher-level observation",
                "Do not list items mechanically — use sentence variety and linking phrases like 'in the background', 'to the left of'",
            ],
            "scoring_rubric": [
                "Content/Coherence: Scene is described systematically; multiple elements covered; organized structure evident",
                "Vocabulary: Descriptive and spatial vocabulary used accurately; present continuous used correctly",
                "Listenability: Description flows naturally; listener can visualize the scene clearly",
                "Task Fulfillment: Enough detail provided to demonstrate observation; time is well used",
            ],
            "sample_band10_response": (
                "This image shows a lively outdoor farmers market on what appears to be a bright "
                "autumn morning in Vancouver. In the foreground, a young child is reaching "
                "excitedly toward a colourful display of large orange pumpkins while her parent "
                "is paying a smiling vendor. Surrounding them, roughly twelve wooden stalls are "
                "arranged across the plaza, overflowing with fresh vegetables, artisan bread, "
                "bunches of sunflowers, and handcrafted jewellery. Shoppers of all ages are "
                "browsing leisurely — several are carrying large reusable bags already filled "
                "with produce. Near the entrance, a musician is seated on a stool playing "
                "acoustic guitar, adding a warm, relaxed atmosphere to the scene. In the "
                "background, tall maple trees are displaying brilliant shades of amber and "
                "red, signalling the start of fall. The overall mood is cheerful and "
                "community-oriented — this market clearly brings the neighbourhood together."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task3", "describing-scene", "farmers-market", "vancouver", "autumn"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 4,
        "part_title": "Making Predictions",
        "question_number": 1,
        "question_type": "making_predictions",
        "question_text": (
            "Look again at the image of the Vancouver farmers market. Based on what you can "
            "see in this scene, predict what will likely happen at the market later in the "
            "afternoon. Consider what might happen with the vendors, the customers, the "
            "weather, and the overall activity level.\n\n"
            "You have 30 seconds to prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "making_predictions",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "Use a variety of future and prediction structures: 'will', 'is likely to', 'I expect that', 'it is probable that', 'may well' — mixing these scores higher",
                "Base each prediction directly on a visual clue from the scene to show logical reasoning",
                "Make 3 to 4 distinct predictions rather than one vague general statement",
                "Include both positive and slightly negative predictions (e.g., market gets busy then winds down) for realism",
                "Close with a summarizing sentence about the overall expected outcome of the afternoon",
            ],
            "scoring_rubric": [
                "Content/Coherence: Multiple logical predictions made; each is grounded in the scene; clear organization",
                "Vocabulary: Future tense and modal language used accurately and with variety",
                "Listenability: Predictions are delivered confidently; pace allows listener to follow reasoning",
                "Task Fulfillment: Predictions cover multiple aspects of the scene as prompted",
            ],
            "sample_band10_response": (
                "Based on the scene, I expect the market will become significantly busier over "
                "the next few hours as more weekend shoppers arrive after mid-morning errands. "
                "The pumpkin display near the front is likely to sell out quickly — it is "
                "already attracting a lot of attention, and with autumn in full swing, pumpkins "
                "are in high demand. The musician near the entrance will probably draw a small "
                "crowd, which may encourage people to linger longer and spend more at the "
                "surrounding stalls. However, by mid-afternoon I would predict that some "
                "vendors will begin packing up their remaining inventory, particularly the "
                "baked goods and cut flowers, which do not keep well. As the temperature "
                "drops with the autumn sun, the crowd will likely thin out. Overall, I think "
                "this will be a very successful and profitable morning for most vendors at "
                "this market."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task4", "making-predictions", "farmers-market", "future-tense"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 5,
        "part_title": "Comparing and Persuading",
        "question_number": 1,
        "question_type": "comparing_persuading",
        "question_text": (
            "Your friend Amara is trying to decide between two options for her daily commute "
            "in Edmonton. She currently drives her own car to work, which takes 25 minutes "
            "but costs her approximately $400 per month in gas, insurance, and parking. "
            "Her second option is to take the Edmonton Metro LRT, which takes 45 minutes "
            "door-to-door but costs only $100 per month in transit passes.\n\n"
            "Compare both options and try to persuade Amara to choose the one you think "
            "is better for her. You have 30 seconds to prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "comparing_persuading",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "State your recommendation in the first sentence — do not build up to it; examiners reward directness",
                "Use comparative structures: 'significantly cheaper', 'far less stressful', 'more environmentally responsible'",
                "Acknowledge the disadvantage of your chosen option honestly, then counter it — this shows sophisticated argumentation",
                "Include at least one benefit that goes beyond the obvious (e.g., productivity on transit, reduced carbon footprint)",
                "End with a direct appeal: 'Amara, I genuinely believe you will be happier choosing...'",
            ],
            "scoring_rubric": [
                "Content/Coherence: Both options compared; a clear recommendation made; counter-argument acknowledged",
                "Vocabulary: Comparative and persuasive language used with accuracy and variety",
                "Listenability: Tone is engaging and confident; argument is easy to follow",
                "Task Fulfillment: Persuasion is genuine and directed at Amara specifically; both commute aspects addressed",
            ],
            "sample_band10_response": (
                "Amara, I would strongly encourage you to switch to the LRT. I know the extra "
                "twenty minutes sounds frustrating, but consider what you gain. You would save "
                "three hundred dollars every single month — that is thirty-six hundred dollars "
                "a year you could put toward travel, savings, or anything else you value. "
                "Beyond the money, driving in Edmonton traffic is genuinely stressful, "
                "especially in winter. On the LRT, you could read, listen to podcasts, or "
                "simply decompress before and after work rather than battling icy roads. "
                "Yes, forty-five minutes is longer, but it is productive time rather than "
                "lost time behind a wheel. Driving also means ongoing maintenance costs, "
                "unexpected repairs, and the environmental cost of daily emissions. The LRT "
                "is cleaner, cheaper, and frankly less stressful. I genuinely think you "
                "will adjust to the longer commute within two weeks and wonder why "
                "you did not switch sooner."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task5", "comparing-persuading", "commute", "transit", "edmonton"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 6,
        "part_title": "Dealing with a Difficult Situation",
        "question_number": 1,
        "question_type": "difficult_situation",
        "question_text": (
            "You are a customer service manager at a retail electronics store in Mississauga. "
            "A long-time customer, Mr. Chen, arrives at your service desk extremely upset. "
            "He purchased a laptop three weeks ago for $1,200 and it has stopped working "
            "completely. He does not have his receipt but insists he bought it at your store. "
            "Your store policy requires a receipt for returns, but the manufacturer's warranty "
            "should still apply. Mr. Chen is speaking loudly and other customers are watching.\n\n"
            "What do you say to Mr. Chen to resolve this situation professionally? "
            "You have 30 seconds to prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "difficult_situation",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "Start by acknowledging the customer's frustration before offering any solution — this de-escalates immediately",
                "Speak calmly and use the customer's name at least once; it personalizes the interaction and reduces tension",
                "Offer a concrete, actionable next step even if you cannot fully resolve it on the spot (e.g., check purchase records, contact manufacturer)",
                "Never blame the customer or quote policy in a cold, robotic way — frame it as 'what we can do' not 'what we cannot do'",
                "Close with a reassurance that you will personally ensure the matter is resolved — this restores confidence",
            ],
            "scoring_rubric": [
                "Content/Coherence: Situation is addressed diplomatically; a realistic resolution path is proposed",
                "Vocabulary: Professional customer service language used; tone is calm and solution-focused",
                "Listenability: Delivery is measured and reassuring; no aggressive or flustered language",
                "Task Fulfillment: Both the emotional and practical aspects of the situation are handled",
            ],
            "sample_band10_response": (
                "Mr. Chen, thank you for bringing this to my attention, and I sincerely apologize "
                "for the trouble you are experiencing with your laptop. I can hear how frustrated "
                "you are, and a twelve-hundred-dollar purchase not working is absolutely "
                "unacceptable. Let me assure you, we are going to find a solution today. "
                "While our return policy does require a receipt, I want to look up your "
                "purchase in our system right now using your name, email address, or the "
                "credit card you used — we keep detailed records and this may resolve things "
                "immediately. Additionally, regardless of the receipt, your laptop is still "
                "within the one-year manufacturer's warranty period, which means we can "
                "initiate a warranty claim on your behalf directly with the manufacturer. "
                "I will personally handle this file and make sure you receive a repair, "
                "replacement, or refund. Could you please come with me to a quieter area "
                "so we can sort this out properly? I want to give this my full attention."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task6", "difficult-situation", "customer-service", "retail", "mississauga"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 7,
        "part_title": "Expressing Opinions",
        "question_number": 1,
        "question_type": "expressing_opinions",
        "question_text": (
            "Many Canadian cities are debating whether to introduce a four-day workweek — "
            "where employees work the same total hours across four days instead of five — "
            "as a way to improve work-life balance and productivity. Some employers support "
            "this change while others believe it would harm business operations.\n\n"
            "What is your opinion on the four-day workweek? Do you think it should be "
            "adopted more widely in Canada? Give specific reasons to support your view. "
            "You have 30 seconds to prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "expressing_opinions",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "State your position clearly in sentence one — 'I strongly believe...' or 'In my view...' — do not hedge for too long",
                "Use the PREP method: Point, Reason, Example, Point — give your main reason, support it with an example or evidence, restate",
                "Acknowledge the opposing view briefly before countering it — this demonstrates critical thinking",
                "Use opinion markers with confidence: 'It is my firm belief that', 'The evidence clearly suggests', 'I am convinced that'",
                "Avoid speaking in circles — each sentence should add new information, not restate the same idea differently",
            ],
            "scoring_rubric": [
                "Content/Coherence: A clear opinion stated; supported by specific reasons; counter-argument acknowledged",
                "Vocabulary: Opinion and argumentative language used accurately; topic-specific vocabulary present",
                "Listenability: Opinion is delivered with appropriate conviction; pace and clarity maintained throughout",
                "Task Fulfillment: Both sides of the debate touched on; position is clearly defended by end of response",
            ],
            "sample_band10_response": (
                "I strongly believe that Canada should adopt the four-day workweek more broadly, "
                "and here is why. Research from pilot programs in Iceland and New Zealand "
                "consistently shows that employee productivity either stays the same or actually "
                "improves when people work compressed schedules. Workers are more focused, "
                "take fewer sick days, and report significantly higher job satisfaction — all "
                "of which benefit employers directly. For Canadians specifically, a three-day "
                "weekend would mean more time for family, volunteer work, and personal health, "
                "which reduces the burden on our healthcare system in the long term. "
                "I understand that some industries, like healthcare or retail, cannot simply "
                "compress hours the same way an office can. However, the policy does not need "
                "to be one-size-fits-all — each sector can adapt the model to its own needs. "
                "The four-day workweek is not a radical idea; it is a practical evolution of "
                "how we think about work, and Canada should lead on this."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task7", "expressing-opinions", "four-day-workweek", "workplace", "policy"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
    {
        "section": "speaking",
        "part": 8,
        "part_title": "Describing an Unlikely Situation",
        "question_number": 1,
        "question_type": "unlikely_situation",
        "question_text": (
            "Imagine that the Canadian government announces a program that allows every "
            "citizen to live for one year completely free of cost — housing, food, "
            "transportation, and healthcare are all provided at no charge for exactly "
            "twelve months, after which normal life resumes.\n\n"
            "What would you do during that year? How would you spend your time, and how "
            "do you think this experience would change you? Be as specific and creative "
            "as possible. You have 30 seconds to prepare and 60 seconds to speak."
        ),
        "options": {
            "task_type": "unlikely_situation",
            "prep_seconds": 30,
            "response_seconds": 60,
            "tips": [
                "Use conditional and hypothetical structures naturally: 'I would spend', 'I would finally be able to', 'This would give me the freedom to'",
                "Be specific and personal — name real places, goals, or activities rather than speaking vaguely ('I would travel' is weak; 'I would spend three months cycling through British Columbia' is strong)",
                "Organize your year with a rough timeline — 'In the first few months... then later...' — this shows coherent planning",
                "Include a personal growth or reflection element — how would the experience change your values or priorities?",
                "Enjoy the creative freedom of this task — examiners respond positively to enthusiastic, vivid, and well-organized responses",
            ],
            "scoring_rubric": [
                "Content/Coherence: A specific, organized plan described; ideas build on each other logically",
                "Vocabulary: Hypothetical and aspirational vocabulary used accurately; descriptive language is vivid",
                "Listenability: Response is enthusiastic and natural; listener is engaged throughout",
                "Task Fulfillment: Both what you would do and how it would change you are addressed",
            ],
            "sample_band10_response": (
                "What an extraordinary opportunity that would be. If I had a full year free of "
                "financial pressure, I would divide it very intentionally. In the first three "
                "months, I would travel across Canada — places I have always wanted to see but "
                "never had time for: the fjords of Newfoundland, the Badlands of Alberta, and "
                "the old-growth rainforests of Vancouver Island. In the middle months, I would "
                "volunteer full-time with a literacy program in my city, because I have always "
                "wanted to give back in a meaningful way but could never commit the hours. "
                "In the final stretch, I would take a serious writing course and finally finish "
                "the novel I have had half-written for five years. "
                "I think this year would fundamentally shift my relationship with time. Right "
                "now, I often feel like I am rushing through life to meet financial obligations. "
                "A year of freedom would remind me what I actually value — community, creativity, "
                "and connection — and I would carry those priorities back into my regular life "
                "with real intention."
            ),
        },
        "correct_answer": None,
        "explanation": None,
        "difficulty": 1.0,
        "tags": ["speaking", "task8", "unlikely-situation", "hypothetical", "creative", "canada"],
        "passage_text": None,
        "audio_script": None,
        "audio_path": None,
        "image_path": None,
    },
]
