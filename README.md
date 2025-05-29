# 🔍 Log Analyzer & Q&A (LangChain + Streamlit)

This app uses LangChain and OpenAI to analyze logs or answer questions.

## 🚀 Features
- Paste logs or upload `.log/.txt` files
- Get summaries of log issues
- Ask questions and get smart answers from LLMs
- Built with Streamlit and LangChain (LCEL)

## 📦 Setup

```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env      # Add your OpenAI key to .env
streamlit run app.py

