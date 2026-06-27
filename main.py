import os
import requests

from dotenv import load_dotenv

from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT
from tools import get_random_joke   # ✅ NEW IMPORT

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "poolside/laguna-m.1:free"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


# -----------------------------
# CALL LLM (SAFE VERSION)
# -----------------------------
def call_llm(messages):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages
    }

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        print("STATUS CODE:", response.status_code)
        print("RESPONSE TEXT:", response.text)

        # -----------------------------
        # HANDLE RATE LIMIT (429)
        # -----------------------------
        if response.status_code == 429:
            return {
                "error": "rate_limit",
                "message": "Rate limit exceeded"
            }

        # -----------------------------
        # HANDLE OTHER ERRORS
        # -----------------------------
        if response.status_code != 200:
            return {
                "error": "api_error",
                "message": response.text
            }

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": "network_error",
            "message": str(e)
        }


# -----------------------------
# AGENT LOOP
# -----------------------------
def agent_loop(user_input):

    # -----------------------------
    # STEP 1: Load memory
    # -----------------------------
    memory = load_memory()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(memory)

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # -----------------------------
    # STEP 2: Call LLM
    # -----------------------------
    result = call_llm(messages)

    # -----------------------------
    # STEP 3: FALLBACK LOGIC
    # -----------------------------

    # 🔥 If API failed → use local jokes
    if isinstance(result, dict) and "error" in result:
        return get_random_joke()

    message = result.get("choices", [{}])[0].get("message", {})
    final_answer = message.get("content")

    # 🔥 If model returns empty → fallback
    if not final_answer or final_answer.strip() == "":
        return get_random_joke()

    # -----------------------------
    # STEP 4: Save memory
    # -----------------------------
    messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )

    save_memory(messages[1:])

    return final_answer


# -----------------------------
# CLI RUN
# -----------------------------
if __name__ == "__main__":

    print("====================================")
    print("        Joke AI Agent")
    print("====================================")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            answer = agent_loop(user_input)
            print("Agent:", answer)

        except Exception as e:
            print("Error:", e)