from state import State
from model import llm
from classifier import MessageClassifier
def classify_message(state:State):
    last_message = state["messages"][-1]
    classifier_llm =llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {
            "role":"system",
            "content":""""
            Classify the user message as either:
            -'emotional' : if it asks for emotional support, therapy, deals with feelings or personal problems
            -'logical' : if it asks for facts, information, logical analysis, or practical solutions
            """
        },
        {
            "role":"user","content":last_message.content
        }
        
    ])
    return {"message_type":result.message_type}
    