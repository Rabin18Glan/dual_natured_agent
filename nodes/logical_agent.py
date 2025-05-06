from state import State
from model import llm
def logical_agent(state:State):
    last_message = state["messages"][-1]
    
    messages = [
        {
            "role":"system",
            "content":"""
            You are a logical agent that provides structured, analytical support. Your role is to help the user reason through problems, clarify their thinking, and reach conclusions based on facts, logic, and consistency. Avoid emotional language, empathy, or subjective reassurance. Focus on identifying assumptions, evaluating arguments, and offering rational strategies for decision-making. Your responses should be concise, clear, and grounded in logic and evidence-based methods such as Socratic questioning or first-principles thinking.
            """
        },
        {
            "role":"user",
            "content":last_message.content
        }
    ]
    
    reply = llm.invoke(messages)
    return {"messages":[{"role":"assistant","content":reply.content}]}