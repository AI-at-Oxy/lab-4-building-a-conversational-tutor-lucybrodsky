[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LkIvP-P-)
# Lab 4: Conversational Tutor with LiteLLM and Ollama

## Overview

In this lab you'll build a web-based chat interface where a student converses with an AI tutor. The tutor is grounded in **hardcoded educational questions** that you embed in the system prompt.

## Setup

### 1. Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Or download from https://ollama.com/download
```

### 2. Pull a model

```bash
ollama pull llama3.2
```

### 3. Set up your Python environment

```bash
conda activate flask-env
pip install -r requirements.txt
```

### 4. Test from the command line first

```bash
python chat_cli.py
```

### 5. Run the web app

```bash
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

## Your Tasks

1. **Replace the example questions** in `questions.py` with at least 5 questions on a topic you know well. Include correct answers and common misconceptions.
2. **Design a system prompt** that tells the LLM how to tutor. This is the creative heart of the lab — what kind of tutor do you want to build?
3. **Build out the chat interface** — the starter gives you a bare minimum. Make it your own.
4. **Test and iterate** on your system prompt. Try correct answers, wrong answers, "I don't know," and off-topic messages.

## Project Structure

```
lab4-starter/
    app.py              # Flask app with / and /chat routes
    questions.py        # Your educational questions (replace the examples!)
    chat_cli.py         # Command-line LLM chat (for testing)
    templates/
        chat.html       # Chat web interface
    requirements.txt
```

## Reflection Questions

Answer each question below by writing in the space provided. This is a markdown file — you can edit it directly in your code editor or on GitHub.

### 1. How did designing a *system prompt* compare to designing *frames* in Lab 3? Which gives you more control over the learning experience? Which is more work?

```
[Your answer here]
```

### 2. Your tutor has hardcoded questions but generates responses dynamically. When is this an advantage over canned feedback? When is it a risk?

```
[Your answer here]
```

### 3. What tutoring strategy did you choose, and why? If you could redesign it, what would you change based on testing?

```
[Your answer here]
```

### 4. Skinner insisted on a low error rate and immediate, predictable reinforcement. Your LLM tutor is neither predictable nor error-free. Is that a problem? For whom?

```
[Your answer here]
```

### 5. A school wants to use your tutor with real students. Name three things you'd worry about.

```
[Your answer here]
```

## Submission Checklist

- [ ] At least 5 educational questions with answers and misconceptions
- [ ] System prompt that defines the tutor's behavior
- [ ] Flask app with /chat route managing conversation history
- [ ] LiteLLM calls to a local Ollama model
- [ ] Working chat interface in the browser
- [ ] Tested with correct, incorrect, and edge-case inputs
- [ ] System prompt iterated at least once based on testing
- [ ] Reflection questions answered (above)
- [ ] Committed with meaningful commit messages
