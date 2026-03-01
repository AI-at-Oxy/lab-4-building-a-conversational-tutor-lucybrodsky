# // Student name: Cael McDermott
# // Project: Lab 4 - Building a Conversational Tutor
# // File name: app.py
# # app.py
from flask import Flask, render_template, request, session, jsonify
from litellm import completion
from questions import TOPIC, QUESTIONS, SYSTEM_PROMPT

app = Flask(__name__)
app.secret_key = "change-this-to-something-secret"

# Ollama configuration
MODEL = "ollama/qwen3-vl:8b"
API_BASE = "http://localhost:11434"


def get_llm_response(conversation_history):
    """Send conversation history to the LLM and get a response."""
    try:
        response = completion(
            model=MODEL,
            messages=conversation_history,
            api_base=API_BASE,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}. Is Ollama running?"


@app.route("/")
def index():
    # Start a fresh conversation with the system prompt
    session["history"] = [{"role": "system", "content": SYSTEM_PROMPT}]
    return render_template("chat.html", topic=TOPIC, num_questions=len(QUESTIONS))


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Add user message to history
    session["history"].append({"role": "user", "content": user_message})

    # Get LLM response
    reply = get_llm_response(session["history"])

    # Add assistant response to history
    session["history"].append({"role": "assistant", "content": reply})
    session.modified = True

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
