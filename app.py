from langchain import ChatOpenAI
from langchain_core_prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os # Lets you interact with the operating system, like accessing environment variables.
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#Lansmith
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_message([
    ("You are helpful assistant"),
    ("user","Questions:{question}")
])

st.title ('Langchain Demo with OPENAI API ')
input_text=st.text_input("search topic u want")

#openai llM 

llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))
