# Diligent_Keerthi
Diligent Assessment

🤖 Jarvis – Personal AI Assistant (Enterprise Demo)
📌 Overview

Jarvis is a lightweight, enterprise-focused AI assistant built to demonstrate how modern AI systems can support governance, risk, compliance (GRC) and executive decision-making workflows.
The project is designed as a clear, reliable demo rather than a research prototype.

🧠 Key Idea

Enterprise AI systems must be:

Accurate

Trustworthy

Hallucination-free

To achieve this, Jarvis follows a hybrid approach:

Controlled Knowledge Layer (Hardcoded Q&A) for critical enterprise concepts

LLM Fallback (TinyLLaMA via Ollama) for general or open-ended queries

This mirrors real-world enterprise AI design, where sensitive or business-critical information is never left entirely to a generative model.

⚙️ How It Works

Streamlit provides an interactive chat-based UI

Hardcoded Knowledge Base answers common questions about:

Diligent

GRC

AI in governance

Vector databases & semantic search

Ollama + TinyLLaMA acts as a fallback for unknown questions

Simple intent detection ensures:

Short, clear responses

No hallucinated company details

Consistent enterprise tone

🏢 Sample Supported Questions

What does Diligent do?

How can AI improve board management?

What is governance, risk, and compliance?

Explain AI to a non-technical board member

What is a vector database?

🚀 Why This Design?

Enterprise-safe (no hallucinations for key topics)

Demo-ready (works instantly, no heavy setup)

Product-thinking oriented, not just model-centric

Reflects how AI assistants are actually built for SaaS and governance products

🛠️ Tech Stack

Python

Streamlit – UI

Ollama – Local LLM runtime

TinyLLaMA – Lightweight self-hosted language model

🎯 Use Case

This project was built as a technical assignment / product demo to showcase:

AI assistant architecture

Enterprise AI thinking

Governance-focused product alignment

🧩 Future Enhancements

Vector database integration for document ingestion

Role-based responses for different users (Board, Legal, Admin)

Secure document upload and summarization

Analytics for usage and insights
