# // Student name: Cael McDermott
# // Project: Lab 4 - Building a Conversational Tutor
# // File name: app.py
# 
# # chat_cli.py
# A simple command-line chat with Ollama using requests.
# Use this to verify Ollama is running before building the web app.

import requests


def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "ollama/qwen3-vl:8b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
    )
    return response.json()["message"]["content"]


if __name__ == "__main__":
    print("Chat with Ollama (type 'quit' to exit)")
    print("-" * 40)

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        print(f"\nLLM: {ask_llm(user_input)}")
