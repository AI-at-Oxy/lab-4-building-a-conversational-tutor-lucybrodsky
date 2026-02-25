# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Ditto: Pokemons Most Unique Pokemon"

QUESTIONS = [
    {
        "question": "What type of Pokemon is Ditto",
        "answer": "Normal",
        "misconception": "Students sometimes guess Psychic because Ditto seems mysterious and magical"
    },
    {
        "question": "What is the name of Ditto's signature move?",
        "answer": "Transform",
        "misconception": "Students sometimes say Copy or Mimic, which are different moves"
    },
    {
        "question": "What is Ditto's hidden ability called?",
        "answer": "Imposter, which lets it automatically transform into the opposing Pokemon when it enters battle",
        "misconception": "Students often confuse this with Transform the move, but Imposter is an ability not a move"
    },
    {
        "question": "Can Ditto breed with another Ditto?",
        "answer": "No, Ditto cannot breed with other Ditto",
        "misconception": "Students assume since Ditto can breed with almost anyone it can breed with itself too"
    },
    {
        "question": "What happens to Ditto's transformation if it starts laughing?",
        "answer": "It cannot maintain the transformation and reverts back",
        "misconception": "Students assume once transformed Ditto stays transformed no matter what"
    },
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a friendly tutor helping a student learn about Ditto: Pokemon's Most Unique Pokemon.

Here are the questions you should work through with the student:

"""

for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"""Question {i}: {q['question']}
  Correct answer: {q['answer']}
  Common misconception: {q['misconception']}

"""

SYSTEM_PROMPT += """
Work through the questions one at a time in order.
IMPORTANT RULES:
- NEVER reveal the correct answer or say "Correct answer:" to the student
- Ask ONE question at a time and WAIT for the student to respond before doing anything else
- If correct, say so briefly and ask the next question
- If wrong, give a small hint only, do not reveal the answer
- If they don't know, give a clue and encourage a guess
- Keep responses SHORT — 2-3 sentences maximum
- Do NOT use markdown, hashtags, or bullet points in your responses
- Do NOT simulate the student's answers or write "User:" or "Assistant:" in your replies
"""
