from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9, streaming=True)


st.header("AI Cooking Assistant")

topic = st.text_input("Enter topic:")
number_of_lines = st.text_input("Enter number of lines:")
style = st.text_input("Enter style:")
language = st.text_input("Enter language:")

if st.button("Generate"):
    prompt = f"""
    You are a helpful cooking assistant.
    Answer about {topic}.
    Use {style} style.
    Write only {number_of_lines} lines.
    Answer in {language}.
    """

    def stream_response():
        for chunk in cm.stream(prompt):
            if chunk.content:
                yield chunk.content

    st.write_stream(stream_response)