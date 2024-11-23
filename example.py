import os
from openai import OpenAI
client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are an intelligent scheduling assistant. Your job is to interpret natural language inputs, detect conflicts, and produce structured schedules. If conflicts occur, suggest alternative time slots."
        },
        {
            "role": "user",
            "content": "I have a class at 3 PM on Wednesdays and Fridays and a meeting on Fridays at 2 PM."
        }
    ]
)
print()
print(completion.choices[0].message)
print()
print(f"API Key: {api_key}")