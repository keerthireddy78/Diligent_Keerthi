import streamlit as st

st.set_page_config(
    page_title="Jarvis – Personal AI Assistant",
    layout="centered"
)

st.title("🤖 Jarvis – Personal AI Assistant")
st.caption("Enterprise AI Assistant for Governance, Risk & Compliance (Demo Mode)")

# ----------------- KNOWLEDGE BASE -----------------

RESPONSES = {

# ----------------- BASIC -----------------
"hi": "Hello! I’m Jarvis, your enterprise AI assistant. How can I help you today?",
"hello": "Hi there! I’m Jarvis. Ask me anything about AI, governance, or enterprise systems.",
"what is an ai assistant": (
    "An AI assistant is a software system designed to help users by answering questions, "
    "summarizing information, and supporting decision-making using artificial intelligence."
),

# ----------------- COMPANY & DOMAIN -----------------
"what does diligent do as a company": (
    "Diligent is a leading SaaS company that provides governance, risk, and compliance (GRC) solutions. "
    "It helps boards, executives, and leadership teams manage board activities, assess risk, "
    "ensure regulatory compliance, and make informed decisions."
),

"how does diligent help boards and executives make better decisions": (
    "Diligent helps boards and executives by centralizing information, providing real-time insights, "
    "improving transparency, and enabling secure collaboration. This allows leadership teams "
    "to focus on strategy rather than administrative work."
),

"what problems does governance risk and compliance software solve": (
    "GRC software helps organizations manage regulatory requirements, identify and mitigate risks, "
    "improve accountability, and ensure ethical and compliant operations across the enterprise."
),

"how can ai improve board management and compliance workflows": (
    "AI can automate document reviews, highlight key risks, summarize board materials, "
    "track compliance gaps, and provide timely insights to decision-makers."
),

"what are the challenges companies face with regulatory compliance": (
    "Companies face challenges such as frequent regulatory changes, complex reporting requirements, "
    "manual processes, data silos, and the risk of non-compliance penalties."
),

"how can an ai assistant help directors prepare for board meetings": (
    "An AI assistant can summarize large board packs, extract key insights, "
    "highlight risks, and ensure directors are well-prepared in less time."
),

# ----------------- AI + PRODUCT THINKING -----------------
"how can ai be used to summarize long board documents": (
    "AI can analyze long documents, identify important sections, extract key points, "
    "and generate concise summaries tailored to executive-level needs."
),

"how does semantic search help executives find information faster": (
    "Semantic search understands the meaning of a query rather than relying on keywords, "
    "allowing executives to retrieve relevant information quickly even if exact terms are not used."
),

"why are vector databases better than traditional databases for ai": (
    "Vector databases store data as embeddings, enabling similarity-based search. "
    "This makes them ideal for AI applications where meaning and context matter."
),

"how does retrieval augmented generation improve answer accuracy": (
    "Retrieval-Augmented Generation combines AI models with external knowledge sources, "
    "grounding responses in relevant data and reducing incorrect or hallucinated answers."
),

"what are the risks of hallucinations in enterprise ai systems": (
    "AI hallucinations can lead to incorrect insights, poor decisions, and loss of trust. "
    "This is especially risky in enterprise environments where accuracy is critical."
),

"how can ai assistants be made more trustworthy for enterprises": (
    "Trustworthy AI assistants use verified data sources, explainable outputs, "
    "access controls, audit trails, and human oversight."
),

# ----------------- ENTERPRISE & SECURITY -----------------
"why is data privacy important for enterprise ai systems": (
    "Enterprise AI systems often handle sensitive data. Strong data privacy ensures "
    "compliance with regulations, protects reputation, and maintains stakeholder trust."
),

"how can companies prevent sensitive data leakage in ai tools": (
    "Companies can prevent data leakage by using private deployments, access controls, "
    "data masking, encryption, and strict governance policies."
),

"what is role based access control in enterprise software": (
    "Role-based access control (RBAC) ensures users can only access data and features "
    "relevant to their role, improving security and compliance."
),

"why do enterprises prefer private or controlled ai deployments": (
    "Enterprises prefer controlled AI deployments to maintain data ownership, "
    "ensure compliance, reduce risk, and customize models for their needs."
),

# ----------------- ANALYTICS & DECISION MAKING -----------------
"how can ai help leadership make data driven decisions": (
    "AI helps leadership by analyzing large datasets, identifying trends, "
    "providing predictive insights, and reducing bias in decision-making."
),

"what kpis matter most for board level reporting": (
    "Key KPIs include financial performance, risk exposure, compliance status, "
    "operational efficiency, and strategic goal progress."
),

"how can ai reduce decision making time for executives": (
    "AI reduces decision-making time by automating analysis, summarizing insights, "
    "and providing real-time recommendations."
),

"what is the impact of real time insights on governance": (
    "Real-time insights enable proactive governance, faster risk response, "
    "and improved organizational resilience."
),

# ----------------- DEMO FRIENDLY WOW QUESTIONS -----------------
"explain vector databases in simple terms": (
    "A vector database stores information in a way that allows systems to understand meaning. "
    "Instead of matching words, it matches ideas."
),

"what is pinecone used for": (
    "Pinecone is used to store and search vector embeddings, "
    "making it ideal for semantic search and AI-driven applications."
),

"how does semantic search work": (
    "Semantic search works by understanding the intent and context of a question, "
    "not just matching exact keywords."
),

"explain ai to a non technical board member": (
    "AI is a tool that helps organizations analyze information faster, "
    "spot risks earlier, and make better decisions using data."
),

# ----------------- DEFAULT -----------------
"default": (
    "That’s a great question. This assistant is designed to support enterprise decision-making "
    "with a focus on governance, compliance, and AI-driven insights."
)
}

# ----------------- CHAT STATE -----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask Jarvis...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    key = user_input.lower().strip()
    reply = RESPONSES.get(key, RESPONSES["default"])

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
