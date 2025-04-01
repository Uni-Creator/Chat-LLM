import streamlit as st
import os
from huggingface_hub import InferenceClient
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

# Load API key
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    st.error("API key not found. Please set the 'HUGGINGFACE_API_KEY' environment variable.")
    st.stop()

st.title("Chat with LLM")

# Sidebar settings
st.sidebar.header("⚙️ Settings")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.1)
model_selection = st.sidebar.selectbox(
    "Choose Model",
    ["mistralai/Mistral-7B-Instruct-v0.3", "google/gemma-3-1b-pt", "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"]
)
max_tokens = st.sidebar.number_input("Max Tokens", min_value=10, max_value=2048, value=500, step=10)

# Initialize Hugging Face Inference Client
client = InferenceClient(model_selection, token=api_key)

# Session state initialization
# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}  # Initial system message
    ]

if "is_chat_input_disabled" not in st.session_state:
    st.session_state.is_chat_input_disabled = False
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None  # Store pending user input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = InMemoryChatMessageHistory()

# Display previous messages
for message in st.session_state.messages:
    if message["role"] == "assistant":  # Don't show system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"].replace("\n", "  \n"), unsafe_allow_html=True)  # Enable word wrap
            
    if message["role"] == "user":
        with st.chat_message(message["role"]):
            st.text(message["content"])
    
# Take user input
user_input = st.chat_input("Enter your message...", key="input", disabled=st.session_state.is_chat_input_disabled)

# Ensure message alternation (remove extra user messages)
while len(st.session_state.messages) > 1 and st.session_state.messages[-1]["role"] == "user":
    st.session_state.messages.pop(-1)  # Remove previous user message if no assistant response

# Store user input and disable chat input
if user_input and not st.session_state.is_chat_input_disabled:
    st.session_state.pending_prompt = user_input  # Save pending user input
    st.session_state.is_chat_input_disabled = True
    st.rerun()  # Re-run to disable input

# Process assistant response
if st.session_state.is_chat_input_disabled and st.session_state.pending_prompt:
    user_prompt = st.session_state.pending_prompt

    # Display user message
    # Store user message
    with st.chat_message("user"):
        st.text(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.session_state.chat_history.add_message(HumanMessage(content=user_prompt))
    
    with st.status("Thinking..."):
        response = client.chat_completion(
            model=model_selection,
            messages=st.session_state.messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
    # print(response)

    # Extract assistant's reply
    response = response["choices"][0]["message"]["content"]

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response.replace("\n", "  \n"), unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.chat_history.add_message(AIMessage(content=response))

    # Reset state for next input
    st.session_state.is_chat_input_disabled = False
    st.session_state.pending_prompt = None  # Clear pending input

    st.rerun()  # Rerun after response is displayed
