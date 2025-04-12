from langchain import ChatOpenAI
from langchain_core_prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt=ChatPromptTemplate.from_message([
    ("You are helpful assistant"),
    ("user","Questions:{question}")
])


st.title ('Langchain Demo with LLAMA2 API ')
input_text=st.text_input("search topic u want")


llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))


