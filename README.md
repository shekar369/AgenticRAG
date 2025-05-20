# 🧠 AgenticRAG

> Smarter Retrieval. Autonomous Reasoning.

![banner](./assets/banner.png)

[![Build](https://img.shields.io/github/actions/workflow/status/shekar369/AgenticRAG/ci.yml)](https://github.com/shekar369/AgenticRAG/actions)
![License](https://img.shields.io/github/license/shekar369/AgenticRAG)
![Stars](https://img.shields.io/github/stars/shekar369/AgenticRAG?style=social)

---

## 📚 Table of Contents
- [🎬 Demo](#-demo)
- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [⚙️ Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [🧭 Project Architecture](#-project-architecture)
- [💡 Use Cases](#-use-cases)
- [🧠 Prompt Engineering Examples](#-prompt-engineering-examples)
- [🤝 How to Contribute](#-how-to-contribute)
- [🛣 Roadmap](#-roadmap)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [🧭 GitHub Push Instructions](#-github-push-instructions)

---

## 🎬 Demo

![Demo GIF](./assets/demo.gif)

Try it live:
- [🌐 Streamlit App](https://agenticrag.streamlit.app) *(optional)*
- [🤗 Hugging Face Spaces](https://huggingface.co/spaces/shekar369/AgenticRAG) *(optional)*

---

## ✨ Features
- 🧠 LangGraph-powered agent state transitions
- 📚 Retrieval-Augmented Generation with FAISS + OpenAI Embeddings
- 🧰 Tool calling and reasoning logic with LangChain agents
- 🔍 LangSmith integration for tracing and debugging
- 📦 Modular, production-ready structure
- 🎯 Prompt engineering examples included

---

## 🛠 Tech Stack
- Python 3.11+
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangSmith](https://smith.langchain.com)
- FAISS
- OpenAI API
- Streamlit
- dotenv

---

## ⚙️ Installation

```bash
git clone https://github.com/shekar369/AgenticRAG.git
cd AgenticRAG
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

```
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=agentic-rag-demo
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

---

## 🚀 Quick Start

### 🔁 CLI

```bash
python main.py
```

### 🖥️ Streamlit App

```bash
streamlit run app/app.py
```

---

## 🧭 Project Architecture

```
AgenticRAG/
├── agentic_rag/        # Core logic
│   ├── retriever.py
│   ├── agent.py
│   ├── graph.py
│   └── prompts/
├── app/               # Streamlit app
│   └── app.py
├── tests/             # Unit tests
├── assets/            # Screenshots, GIFs
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

## 💡 Use Cases
- 🧾 Research assistants with citation tracking
- 💬 Domain-specific copilots (law, healthcare, HR)
- 🕵️ LLM evaluation and debugging tools
- 🧠 Agents that reflect and improve responses

---

## 🧠 Prompt Engineering Examples

| Use Case | Prompt |
|----------|--------|
| Retrieval | "Search Lilian Weng’s blogs about hallucination." |
| Agent Reasoning | "Think step-by-step about the answer before retrieving context." |

---

## 🤝 How to Contribute

```bash
# Fork the repo
# Clone your fork
# Create your feature branch
git checkout -b feature/your-feature

# Make changes
git commit -m "Add feature"
git push origin feature/your-feature

# Create a pull request 🎉
```

Got ideas or feedback? [Open an issue](https://github.com/shekar369/AgenticRAG/issues)

---

## 🛣 Roadmap
- [x] Basic Agentic RAG flow with LangChain
- [x] LangSmith integration
- [x] Streamlit frontend demo
- [ ] Hugging Face demo version
- [ ] LangGraph-powered multi-agent RAG
- [ ] Evaluation framework using LangChain metrics

---

## 📄 License

MIT License © 2025 [Shekar Kaki](https://github.com/shekar369)

---

## 🙏 Acknowledgments
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangSmith](https://smith.langchain.com)
- [Lilian Weng](https://lilianweng.github.io)

---

## 🧭 GitHub Push Instructions

```bash
cd AgenticRAG
git init
git remote add origin https://github.com/shekar369/AgenticRAG.git
git add .
git commit -m "Initial commit: Agentic RAG with LangChain, LangGraph, LangSmith"
git push -u origin master
```

> ⭐️ Star this repo if you find it useful and share it with your AI community!
