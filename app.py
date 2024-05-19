#LLM Conversational ChatBot 
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

#Streamlit UI 
st.set_page_config(page_title="Conversational ChatBot")
st.header("Hey!! Look who's back! What's on your mind? ")

import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

 
chat=ChatOpenAI(openai_api_key=openai_api_key,temperature=0.6,model='gpt-3.5-turbo')

#controls randomness of model's response 

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI Bot ')
    ] 

#Function to get responses 
def chat_response (question):
    st.session_state['flowmessages'].append (HumanMessage(content= question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append (AIMessage(content= answer.content))
    return answer.content 

input = st.text_input("Input: ", key="input")
response= chat_response(input)

submit = st.button("Ask the question ")
if submit: 
    st.subheader("The response is: ")
    st.write(response)
