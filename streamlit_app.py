import os
import json
import streamlit as st
from groq import Groq

# Streamlit page configuration
st.set_page_config(
    page_title="ChatLlama 🦙",
    page_icon="🦙",
    layout="centered"
)

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data["GROQ_API_KEY"]

# Save the API key to environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

# Initialize the chat history as Streamlit session state if not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Add custom CSS to center elements and change text color
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    .grey-text {
        color: #808080; /* Light grey */
    }
    </style>
    """, unsafe_allow_html=True)

# Centered Chatbot name
st.markdown("<h1 class='center-text'>ChatLlama 🦙</h1>", unsafe_allow_html=True)

# Powered by text in grey, not as a heading
st.markdown("<p class='center-text grey-text'>Powered by Llama 3.1-70b</p>", unsafe_allow_html=True)

# Display a centered prompt above the input field
st.markdown("<h4 class='center-text'>What can I help with?</h4>", unsafe_allow_html=True)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.chat_input("Ask LLAMA...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send user's message to the LLM and get a response
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        *st.session_state.chat_history
    ]

    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
















