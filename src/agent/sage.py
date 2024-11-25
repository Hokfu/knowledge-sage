import json
from groq import Groq
from src.state import KnowledgeState, Agent

client = Groq()


def generate_sage(state: KnowledgeState):
    prompt = f"""
    You are a sage. You are given a user message.
    You must determine which agent to use to respond to the user message.
    The agent must be one of the following: {[agent.value for agent in Agent]}
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": state["message"]},
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "select_agent",
                    "description": "Select the agent to use to respond to the user message.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "agent": {
                                "type": "string",
                                "enum": [agent.value for agent in Agent],
                                "description": "The agent to use to respond to the user message.",
                            },
                        },
                        "required": ["agent"],
                    },
                },
            }
        ],
        tool_choice="required",
    )
    sage_decision = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    state["agent"] = sage_decision["agent"]

    return state
