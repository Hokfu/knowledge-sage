from src.state import KnowledgeState
from src.schema.schema import HistoryKnowledge
from src.llm import generate_response
from src.tools.tools import history_knowledge_tool


def generate_history_knowledge(state: KnowledgeState):
    system_prompt = f"""
    You are an expert in history. You are given a target audience and a user message.
    Here is the target audience: {state["target_audience"].value}
    You must respond to the user message with a comprehensive response that is tailored to the target audience.
    The response must be in {state["detailed_level"].value}.
    """
    tools = [history_knowledge_tool]
    response = generate_response(
        system_prompt,
        state["message"],
        tools=tools,
    )
    history_knowledge = HistoryKnowledge.model_validate_json(response)
    state["response"] = history_knowledge.response
    state["payload"] = {
        "topic": history_knowledge.topic,
    }
    return state
