from src.schema.schema import ScienceKnowledge
from src.llm import generate_response
from src.state import KnowledgeState
from src.tools.tools import science_knowledge_tool


def generate_science_knowledge(state: KnowledgeState):
    system_prompt = f"""
    You are an expert in science knowledge. You are given a target audience and a user message.
    Here is the target audience: {state["target_audience"].value}
    You must respond to the user message with a long comprehensive response that is tailored to the target audience.
    The response must be in {state["detailed_level"].value}.
    """

    tools = [science_knowledge_tool]

    response = generate_response(system_prompt, state["message"], tools)
    science_knowledge = ScienceKnowledge.model_validate_json(response)
    state["response"] = science_knowledge.response
    state["payload"] = {
        "topic": science_knowledge.topic,
        "field": science_knowledge.field,
    }

    return state
