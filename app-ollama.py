
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

llm = ChatOllama(model="llama3", temperature=0.3, request_timeout=30)

prompt = ChatPromptTemplate.from_template("""
You are an assistant for analyzing logs or answering technical questions.

If the input is a log, summarize the issue.
If it's a question, provide a clear answer.

Input:
{user_input}

Response:
""")

chain = prompt | llm | StrOutputParser()

st.set_page_config(page_title="🧠 Local Log Analyzer")
st.title("📄 Log Analyzer & QA (LLM: llama3 via Ollama)")

input_type = st.radio("Choose Input Type", ["Text Input", "Upload Log File"])
user_input = ""

if input_type == "Text Input":
    user_input = st.text_area("Paste logs or ask a question:")
else:
    uploaded_file = st.file_uploader("Upload a log file", type=["log", "txt"])
    if uploaded_file:
        user_input = uploaded_file.read().decode("utf-8")

analyze = st.button("🔎 Analyze")

if analyze:
    if not user_input.strip():
        st.warning("Please provide input.")
    else:
        with st.spinner("Processing via llama3..."):
            start = time.time()
            result = chain.invoke({"user_input": user_input})
            st.success(f"✅ Done in {round(time.time() - start, 2)}s")
            st.subheader("💡 Response")
            st.write(result)
