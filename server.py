import streamlit as st
from medgpt import med_gpt
import time

def generator(response):
    words = response.split(" ")
    for word in words:
        yield word + " "
        time.sleep(0.02)
    
st.title("MedBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = med_gpt(prompt)
        st.write_stream(generator(response))
    st.session_state.messages.append({"role": "assistant", "content": response})