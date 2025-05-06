import os
import getpass
import streamlit as st
from graph import compiled_graph

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Setup environment variables
os.environ["LANGSMITH_TRACING"] = "true"
if "LANGSMITH_API_KEY" not in os.environ:
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key (optional): ")
if "LANGSMITH_PROJECT" not in os.environ:
    os.environ["LANGSMITH_PROJECT"] = getpass.getpass("Enter your LangSmith Project Name (default = 'default'): ") or "default"
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")
if not os.environ.get("USER_AGENT"):
    os.environ["USER_AGENT"] = getpass.getpass("User Agent: ")



def main():
    state = {"messages":[],"message_type": None}
    st.title("Dual Natured Agent",help="Give logical or emotional reponse based on input")



    user_input = st.chat_input("Ask Anything")
    if(user_input):
        
          state["messages"] = state.get("messages",[])+[
           {
            "role":"user",
            "content":user_input
           }
          ]
    
          state = compiled_graph.invoke(state)
    
          if(state).get("messages") and len(state["messages"])>0:
              last_message = state["messages"][-1]
              st.write(last_message.content)
        
  
    
if __name__ == "__main__":
    main()