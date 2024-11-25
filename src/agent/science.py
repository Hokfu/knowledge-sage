import json
from groq import Groq
from src.state import KnowledgeState
from src.util import extract_payload

client = Groq()


def generate_science_knowledge(state: KnowledgeState):
    prompt = f"""
    You are an expert in science knowledge. You are given a target audience and a user message.
    Here is the target audience: {state['target_audience'].value}
    You must respond to the user message with a long comprehensive response that is tailored to the target audience.
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
                    "name": "get_science_knowledge",
                    "description": "Get the knowledge about the science according to the target audience.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "topic": {
                                "type": "string",
                                "description": "The topic of the science.",
                            },
                            "field": {
                                "type": "string",
                                "description": "The field of the science. e.g. physics, chemistry, biology, etc.",
                            },
                            "response": {
                                "type": "string",
                                "description": "The response to the user message.",
                            },
                        },
                        "required": ["topic", "field", "response"],
                    },
                },
            },
        ],
        tool_choice="required",
    )
    science_knowledge = json.loads(
        response.choices[0].message.tool_calls[0].function.arguments
    )
    state["response"] = science_knowledge["response"]
    state["payload"] = extract_payload(science_knowledge)

    return state
