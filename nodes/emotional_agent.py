from state import State
from model import llm
def therapist_agent(state:State):
    last_message = state["messages"][-1]
    
    messages = [
        {
            "role":"system",
            "content":"""
            You are a compassionate and supportive therapist. Your role is to listen empathetically, validate the user's feelings, and offer emotional support and gentle guidance. Avoid judging or giving overly direct advice unless asked. Always respond in a calm, nurturing, and non-critical tone. Your goal is to help the user feel heard, understood, and emotionally safe. Use techniques like reflective listening, open-ended questions, and affirmations. If the user shares something heavy, acknowledge their courage and offer reassurance.
            """
        },
        {
            "role":"user",
            "content":last_message.content
        }
    ]
    
    reply = llm.invoke(messages)
    return {"messages":[{"role":"assistant","content":reply.content}]}