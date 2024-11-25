import json
from groq import Groq
from src.state import KnowledgeState
from src.util import extract_payload

client = Groq()


def generate_animal_knowledge(state: KnowledgeState):
    prompt = f"""
    You are an expert in animal knowledge. You are given a target audience and a user message.
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
                    "name": "get_animal_knowledge",
                    "description": "Get the knowledge about the animal according to the target audience.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "animal": {
                                "type": "string",
                                "description": "The animal name, e.g. dog, cat, etc.",
                            },
                            "animal_type": {
                                "type": "string",
                                "enum": [
                                    "mammal",
                                    "bird",
                                    "reptile",
                                    "amphibian",
                                    "fish",
                                    "insect",
                                    "other",
                                ],
                                "description": "The type of the animal, e.g. mammal, bird, etc.",
                            },
                            "topic": {
                                "type": "string",
                                "description": "The topic of the animal.",
                            },
                            "response": {
                                "type": "string",
                                "description": "Long comprehensive response to the user message.",
                            },
                        },
                        "required": ["animal", "animal_type", "topic", "response"],
                    },
                },
            }
        ],
        tool_choice="required",
    )
    animal_knowledge = json.loads(
        response.choices[0].message.tool_calls[0].function.arguments
    )
    state["response"] = animal_knowledge["response"]
    state["payload"] = extract_payload(animal_knowledge)

    return state
