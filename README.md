
# 🔍 Log Analyzer & Q&A App (Streamlit + LangChain + Ollama)

This app analyzes log files or answers user questions using LLMs. It supports both **OpenAI (cloud)** and **Ollama (local)** for private, offline log analysis.

---

## 🚀 Features

- 📤 Upload `.log` or `.txt` files
- 🧠 Summarize logs or answer tech questions
- 🌐 Supports OpenAI + 🖥️ Ollama (local LLMs like llama3)

---

## 🛠️ Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Using Local LLM (Ollama + llama3)

1. Install Ollama: https://ollama.com/download

2. Pull the model:

```bash
ollama pull llama3
```

3. Run the local app:

```bash
streamlit run app-ollama.py
```

> ✅ No OpenAI key required. Everything runs locally using your CPU/RAM.

---

## 📄 Example Log Input

```log
[ERROR] nginx failed to bind to port 80
[INFO] nginx restarted
[ERROR] Port already in use
```

---

## 📁 Project Structure

```
log-analyzer/
├── app.py              # OpenAI version
├── app-ollama.py       # Local LLM (Ollama) version
├── .env.example        # For OpenAI use
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📜 License

MIT License
