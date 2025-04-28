from src.state import KnowledgeState
from src.schema.schema import AnimalKnowledge
from src.tools.tools import animal_knowledge_tool
from src.llm import generate_response


def generate_animal_knowledge(state: KnowledgeState):
    system_prompt = f"""
    You are an expert in animal knowledge. You are given a target audience and a user message.
    Here is the target audience: {state["target_audience"].value}
    You must respond to the user message with a long comprehensive response that is tailored to the target audience.
    The response must be in {state["detailed_level"].value}.
    """

    tools = [animal_knowledge_tool]

    response = generate_response(system_prompt, state["message"], tools)
    animal_knowledge = AnimalKnowledge.model_validate_json(response)
    state["response"] = animal_knowledge.response
    state["payload"] = {
        "animal": animal_knowledge.animal,
        "animal_type": animal_knowledge.animal_type,
        "topic": animal_knowledge.topic,
    }
    return state
