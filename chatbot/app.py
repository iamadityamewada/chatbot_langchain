from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
import os

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## langsmith tracking
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

##PromtTemplate

prompt = ChatPromptTemplate.from_messages([
  ("system","You are helpful assitant. Please response to the user Queries"),
  ("user","Question:{Question}")
])

## stramlit framework

st.title = "ChatBot using Langchain and OpenAI"
input_text = st.text_input("Enter The Prompt")

#openai llm

llm = ChatOpenAI(model="gpt-3.5-turbo")
ouput_parser = StrOutputParser()
chain = prompt|llm|ouput_parser

if input_text:
    st.write(chain.invoke({question:input_text}))