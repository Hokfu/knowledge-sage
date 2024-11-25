import json
from groq import Groq
from src.state import KnowledgeState
from src.util import extract_payload

client = Groq()


def generate_history_knowledge(state: KnowledgeState):
    prompt = f"""
    You are an expert in history. You are given a target audience and a user message.
    Here is the target audience: {state['target_audience'].value}
    You must respond to the user message with a comprehensive response that is tailored to the target audience.
    The response must be in {state['detailed_level'].value}.
    """

    response = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": state["message"]},
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_history_knowledge",
                    "description": "Get the knowledge about the history according to the target audience.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "The topic of the history.",
                            },
                            "response": {
                                "type": "string",
                                "description": "The response to the user message.",
                            },
                        },
                        "required": ["topic", "response"],
                    },
                },
            }
        ],
        tool_choice="required",
    )
    history_knowledge = json.loads(
        response.choices[0].message.tool_calls[0].function.arguments
    )
    state["response"] = history_knowledge["response"]
    state["payload"] = extract_payload(history_knowledge)

    return state
