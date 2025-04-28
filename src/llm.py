from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def generate_response(system_prompt: str, user_prompt: str, tools: list[dict]):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        tools=tools,
        tool_choice="required",
    )
    return response.choices[0].message.tool_calls[0].function.arguments
