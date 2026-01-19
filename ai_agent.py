from openai import OpenAI
from prompt import SYSTEM_PROMPT

client = OpenAI(api_key="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")

def analyze_code(user_code):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_code}
        ]
    )
    return response.choices[0].message.content
