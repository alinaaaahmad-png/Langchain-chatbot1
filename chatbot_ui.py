"""
LangChain Chatbot - Streamlit UI
A beautiful conversational AI chatbot built with LangChain, Streamlit, and Ollama.
"""
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:1.5b")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TURNS = int(os.getenv("MAX_TURNS", "6"))

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }

    /* Chat container */
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    /* User message bubble */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 20px 20px 5px 20px;
        margin: 10px 0;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }

    /* AI message bubble */
    .ai-message {
        background: linear-gradient(135deg, #2d3436 0%, #1a1a2e 100%);
        color: #e0e0e0;
        padding: 15px 20px;
        border-radius: 20px 20px 20px 5px;
        margin: 10px 0;
        max-width: 80%;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* Message label */
    .message-label {
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Input container */
    .input-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 800px;
    }

    /* Title styling */
    .title {
        text-align: center;
        color: white;
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.6);
        font-size: 14px;
        margin-bottom: 30px;
    }

    /* Turn counter */
    .turn-counter {
        text-align: center;
        color: rgba(255, 255, 255, 0.5);
        font-size: 12px;
        padding: 10px;
    }

    /* Clear button */
    .clear-btn {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        border: none;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .clear-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(231, 76, 60, 0.4);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Message div styling */
    .message-content {
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize the LLM
@st.cache_resource
def get_llm():
    return ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

# Create the chain
def create_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful, friendly, and knowledgeable AI assistant. Provide clear, concise, and accurate responses."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}")
        ]
    )
    llm = get_llm()
    return prompt | llm | StrOutputParser()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chain" not in st.session_state:
    st.session_state.chain = create_chain()
if "turns_remaining" not in st.session_state:
    st.session_state.turns_remaining = MAX_TURNS

# Sidebar with info
with st.sidebar:
    st.markdown("### 🤖 Chat Info")
    st.markdown(f"**Model:** {MODEL_NAME}")
    st.markdown(f"**Temperature:** {TEMPERATURE}")
    st.markdown(f"**Max Turns:** {MAX_TURNS}")
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.turns_remaining = MAX_TURNS
        st.rerun()

# Title
st.markdown('<div class="title">💬 AI Chatbot</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">Powered by LangChain + Ollama ({MODEL_NAME})</div>', unsafe_allow_html=True)

# Display chat messages
chat_container = st.container()
with chat_container:
    for i, message in enumerate(st.session_state.chat_history):
        if isinstance(message, HumanMessage):
            st.markdown(f'''
                <div class="user-message">
                    <div class="message-label" style="color: #a8c0ff;">👤 You</div>
                    <div class="message-content">{message.content}</div>
                </div>
            ''', unsafe_allow_html=True)
        elif isinstance(message, AIMessage):
            st.markdown(f'''
                <div class="ai-message">
                    <div class="message-label" style="color: #c8a8ff;">🤖 AI</div>
                    <div class="message-content">{message.content}</div>
                </div>
            ''', unsafe_allow_html=True)

# Turn counter
current_turns = len(st.session_state.chat_history) // 2
st.session_state.turns_remaining = MAX_TURNS - current_turns

if st.session_state.turns_remaining <= 2:
    st.markdown(f'<div class="turn-counter">⚠️ Only {st.session_state.turns_remaining} turn(s) remaining</div>', unsafe_allow_html=True)

# Input area at bottom
st.markdown('<div class="input-container">', unsafe_allow_html=True)

col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        "Message AI...",
        placeholder="Type your message here...",
        label_visibility="collapsed",
        key="user_input"
    )
with col2:
    send_button = st.button("Send ➤", use_container_width=True)

# Handle sending message
if send_button and user_input.strip():
    # Check if context window is full
    if st.session_state.turns_remaining <= 0:
        st.error("Context window is full! Please clear the chat to continue.")
    else:
        # Add user message
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        # Get AI response
        with st.spinner("🤔 Thinking..."):
            try:
                response = st.session_state.chain.invoke({
                    "question": user_input,
                    "chat_history": st.session_state.chat_history[:-1]
                })
                st.session_state.chat_history.append(AIMessage(content=response))
            except Exception as e:
                st.error(f"Error: {str(e)}")

        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
