import streamlit as st
from agents import LANG_APP
import os
import time
import google.api_core.exceptions

lang_app = LANG_APP()

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")


st.write("""
### Instructions for Creating Your Bot Profile

1. **Enter Attributes for the Bot**:
    - **Name**: Provide the name you want for your bot.
    - **Age**: Specify the age of your bot.
    - **Nationality**: Indicate the nationality of your bot.
    - **Native Language**: State the native language of your bot.
    - **Other Languages**: List any additional languages your bot can understand or speak.
    - **Additional Attributes (if any)**: Include any other relevant attributes you want to provide.

This information will be used to create your personalized bot profile.
""")

# Take user input for name
attribute = st.text_input("Please provide a description of the bot you envision:")
if attribute:
    response = lang_app.Character_Development_Agent(attribute)

    if response:

        st.empty()  # Clear the screen

        # Store LLM generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

        # Display or clear chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        def clear_chat_history():
            st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
        st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

        # User-provided prompt
        if prompt := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

        # Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    i = 0
                    while i == 0:
                            try:
                                answer = lang_app.chat_w(prompt, response)
                                i = 1
            
                            except google.api_core.exceptions.InternalServerError as e:
                                print(f"InternalServerError: {e}. Retrying in 30 seconds...")
                                time.sleep(30)

                    placeholder = st.empty()
                    full_response = ''
                    for item in answer:
                        full_response += item
                        placeholder.markdown(full_response)
                    placeholder.markdown(full_response)
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)
