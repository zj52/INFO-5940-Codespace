import streamlit as st
from openai import OpenAI


client = OpenAI()


st.set_page_config(page_title="Hello Codespaces", layout="centered", page_icon="👋")


st.title("Let's chat :blush:")

#read knowledge base from data/important_knowledge.txt
with open("data/important_knowledge.txt", "r") as f:
    knowledge_base = f.read()   

if "messages" not in st.session_state:
   st.session_state["messages"] = [{"role": "system", "content": "You are a helpful pirate assistant."},
                                    {"role": "user", "content": "I want you to answer questions based on this knowledge base" + knowledge_base},
                                    {"role": "assistant", "content": "Howdy partner!"}]


for message in st.session_state["messages"]:
   if message["role"] != "system" and msg['content'] != "I want you to answer questions based on this knowledge base" + knowledge_base:
       st.chat_message(message["role"]).write(message["content"])


if prompt := st.chat_input():
   
   st.session_state["messages"].append({"role": "user", "content": prompt})
   st.chat_message("user").write(prompt)


   with st.chat_message("assistant"):
       stream = client.chat.completions.create(
           model="openai.gpt-4o",
           messages=st.session_state["messages"],
           stream=True
       )
       response = st.write_stream(stream)


   st.session_state["messages"].append({"role": "assistant", "content": response})
