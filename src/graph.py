from src.agent.sage import generate_sage
from src.agent.animal import generate_animal_knowledge
from src.agent.history import generate_history_knowledge
from src.agent.science import generate_science_knowledge
from src.state import DetailedLevel, KnowledgeState
from langgraph.graph import StateGraph, END

def get_agent(state: KnowledgeState):
    return state["agent"]

def run_graph(message: str, target_audience: str, detailed_level: DetailedLevel):
    builder = StateGraph(KnowledgeState)
    builder.add_node("sage", generate_sage)
    builder.add_node("animal", generate_animal_knowledge)
    builder.add_node("history", generate_history_knowledge)
    builder.add_node("science", generate_science_knowledge)
    builder.set_entry_point("sage")
    builder.add_conditional_edges("sage", get_agent)
    builder.add_edge("animal", END)
    builder.add_edge("history", END)
    builder.add_edge("science", END)
    graph = builder.compile()
    state = KnowledgeState(message=message, target_audience=target_audience, detailed_level=detailed_level)
    return graph.invoke(state)