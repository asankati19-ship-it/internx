from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9,
    streaming=True
)

st.set_page_config(
    page_title="AI Cooking Assistant",
    page_icon="🍳",
    layout="centered"
)

st.markdown("""
<style>
    .title-box {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #ff914d, #ffcc70);
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    }

    .title-box h1 {
        color: white;
        font-size: 42px;
        margin-bottom: 5px;
    }

    .title-box p {
        color: white;
        font-size: 18px;
    }

    .logo {
        font-size: 70px;
        text-align: center;
    }

    .stButton button {
        background-color: #ff7a00;
        color: white;
        border-radius: 12px;
        padding: 10px 25px;
        font-size: 18px;
        border: none;
    }

    .stButton button:hover {
        background-color: #e86c00;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <div class="logo">👨‍🍳🍳</div>
    <h1>AI Cooking Assistant</h1>
    <p>Get recipe ideas, cooking tips, and food suggestions instantly</p>
</div>
""", unsafe_allow_html=True)

topic = st.text_input("Enter topic:", placeholder="Example: Pasta, Biryani, Salad")
number_of_lines = st.text_input("Enter number of lines:", placeholder="Example: 5")
style = st.text_input("Enter style:", placeholder="Example: simple, funny, professional")
language = st.text_input("Enter language:", placeholder="Example: English, Telugu, Hindi")

if st.button("Generate Recipe"):
    if not topic or not number_of_lines or not style or not language:
        st.warning("Please fill all fields before generating.")
    else:
        prompt = f"""
        You are a helpful cooking assistant.
        Answer about {topic}.
        Use {style} style.
        Write only {number_of_lines} lines.
        Answer in {language}.
        """

        st.subheader("🍽️ Your Cooking Response")

        def stream_response():
            for chunk in cm.stream(prompt):
                if chunk.content:
                    yield chunk.content

        st.write_stream(stream_response())