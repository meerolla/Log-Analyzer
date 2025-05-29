import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3, api_key=openai_key)

# Define the modern LangChain LCEL chain
prompt = ChatPromptTemplate.from_template("""
You are an expert log analysis assistant.

If the input is a user question, answer it.

If the input is a log file, summarize the key issue(s).

Input:
{user_input}

Your Response:
""")

chain = prompt | llm | StrOutputParser()

# Streamlit UI
st.set_page_config(page_title="Log Analyzer", layout="centered")
st.title("🧠 Log Analyzer & Q&A")

input_type = st.radio("Choose Input Type", ["Text Input", "Upload Log File"])
user_input = ""

if input_type == "Text Input":
    user_input = st.text_area("Paste your question or log:")
else:
    uploaded_file = st.file_uploader("Upload .log or .txt file", type=["log", "txt"])
    if uploaded_file:
        user_input = uploaded_file.read().decode("utf-8")

#if user_input and st.button("Analyze"):
analyze = st.button("🔎 Analyze")

if analyze:
    if not user_input.strip():
        st.warning("Please provide a question or upload a log file.")
    else:
        with st.spinner("Processing..."):
            result = chain.invoke({"user_input": user_input})
            st.subheader("🔎 Result")
            st.write(result)
