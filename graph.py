from langgraph.graph import StateGraph,START,END
from state import State
from nodes.classify_message import classify_message

from nodes.emotional_agent import therapist_agent

from nodes.logical_agent import logical_agent

from nodes.router import router


graph_builder = StateGraph(State)

graph_builder.add_node("classifier",classify_message)
graph_builder.add_node("router",router)
graph_builder.add_node("therapist",therapist_agent)
graph_builder.add_node("logical",logical_agent)

graph_builder.add_edge(START,"classifier")
graph_builder.add_edge("classifier","router")
graph_builder.add_conditional_edges(
    "router",
    lambda state:state.get("next"),
    {"emotional":"therapist","logical":"logical"}
)

graph_builder.add_edge("therapist",END)
graph_builder.add_edge("logical",END)

compiled_graph = graph_builder.compile()
