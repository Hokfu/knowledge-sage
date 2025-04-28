from src.state import KnowledgeState, Agent
from src.schema.schema import Knowledge
from src.llm import generate_response
from src.tools.tools import sage_tool


def generate_sage(state: KnowledgeState):
    system_prompt = f"""
    You are a sage. You are given a user message.
    You must determine which agent to use to respond to the user message.
    The agent must be one of the following: {[agent.value for agent in Agent]}
    """
    tools = [sage_tool]

    response = generate_response(system_prompt, state["message"], tools)
    sage_decision = Knowledge.model_validate_json(response)
    state["agent"] = sage_decision.agent.value

    return state
