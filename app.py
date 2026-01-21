import streamlit as st
import ollama

# ================= STREAMLIT UI =================
st.set_page_config(page_title="Jarvis – Personal AI Assistant", layout="centered")
st.title("🤖 Jarvis – Personal AI Assistant")
st.caption("Enterprise AI Assistant for Governance & Decision Support")

# ================= HARDCODED KNOWLEDGE =================
KNOWLEDGE_BASE = {
    "what does diligent do": 
    "Diligent is a SaaS company that provides governance, risk, and compliance (GRC) solutions to help boards, executives, and legal teams make better, more informed decisions.",

    "how does diligent help boards":
    "Diligent helps boards and executives by centralizing board materials, improving visibility into risks, ensuring compliance, and enabling secure collaboration for decision-making.",

    "what is grc":
    "Governance, Risk, and Compliance (GRC) software helps organizations manage regulations, identify risks, enforce policies, and ensure accountability across the enterprise.",

    "how can ai improve board management":
    "AI can summarize board documents, highlight key risks, surface relevant insights, and help directors prepare more efficiently for meetings.",

    "challenges of regulatory compliance":
    "Companies face challenges such as frequent regulatory changes, data silos, manual reporting, audit risks, and lack of real-time visibility.",

    "how can ai help board meetings":
    "An AI assistant can summarize agendas, answer governance-related questions, retrieve past decisions, and highlight action items before meetings.",

    "what is a vector database":
    "A vector database stores data as numerical embeddings and allows semantic search, making it ideal for AI applications that require understanding meaning rather than exact keywords.",

    "what is pinecone":
    "Pinecone is a managed vector database used to store and retrieve embeddings efficiently for AI-driven search and retrieval systems.",

    "what is an ai assistant":
    "An AI assistant is a system that understands user queries, retrieves relevant information, and provides contextual, conversational responses.",

    "how does semantic search work":
    "Semantic search converts text into embeddings and finds results based on meaning rather than exact keyword matches.",

    "explain ai to a non technical person":
    "AI is like a smart assistant that learns from data and helps people make faster and better decisions by finding patterns humans might miss."
}

# ================= FUNCTIONS =================
def llm_fallback(query):
    response = ollama.chat(
        model="tinyllama:latest",
        messages=[{"role": "user", "content": query}]
    )
    return response["message"]["content"]

def respond(query):
    q = query.lower().strip()

    if q in ["hi", "hello", "hey"]:
        return "Hello 👋 I’m Jarvis. How can I assist you today?"

    for key in KNOWLEDGE_BASE:
        if key in q:
            return KNOWLEDGE_BASE[key]

    return llm_fallback(query)

# ================= CHAT STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask Jarvis...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        reply = respond(user_input)
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
