from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-5.1-mini", temperature=0.9)

st.header("AI cooking assistant")

topic = st.text_input("Enter topic: ")
number_of_lines = st.text_input("Enter number of lines: ")
style = st.text_input("Enter style: ")
language = st.text_input("Enter language: ")

system_prompt = f"You are a helpful assistant. You need to answer the questions in {style} form and in {number_of_lines} lines only about {topic} in {language}"

if st.button("Generate"):    
    result = cm.invoke(system_prompt)
    st.write(result.content)

