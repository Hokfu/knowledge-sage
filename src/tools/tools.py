from src.state import Agent


animal_knowledge_tool = {
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

history_knowledge_tool = {
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

science_knowledge_tool = {
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
}

sage_tool = {
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
