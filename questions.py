# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Lickitung, the Pokemon"

QUESTIONS = [
    {
        "question": "What type of Pokemon is Lickitung?",
        "answer": "Normal",
        "misconception": "Students sometimes say Water because salamanders like water, but Lickitung is actually Normal type"
    },
    {
        "question": "How long is Lickitung's tongue?",
        "answer": "Twice it's body length!",
        "misconception": "Most people would say equal to its body length, but Lickitung's tongue is actually twice as long as its body!"
    },
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a friendly tutor helping a student learn about {TOPIC}.

Here are the questions you should work through with the student:

"""

for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"""Question {i}: {q['question']}
  Correct answer: {q['answer']}
  Common misconception: {q['misconception']}

"""

SYSTEM_PROMPT += """
Briefly greet the student, and ask them if they are ready to learn some Lickitung Trivia. Be formal about, do not be corny. Minmize Emoji use.
Do NOT spoil the questions or answers for the student. If the student asks about the questions, just say "I will not provide answers until you try".
"""
