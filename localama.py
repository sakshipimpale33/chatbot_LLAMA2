from langchain import ChatOpenAI
from langchain_core_prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


prompt=ChatPromptTemplate.from_message([
    ("You are helpful assistant"),
    ("user","Questions:{question}")
])


st.title ('Langchain Demo with OPENAI API ')
input_text=st.text_input("search topic u want")


llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))


