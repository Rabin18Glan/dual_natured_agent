from state import State
def router(state:State):
    message_type = state.get("message_type","logical")
    if message_type == "emotional":
        return {"next":"emotional"}
    
    return {"next":"logical"}
