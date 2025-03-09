import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

st.title("?? AI Chatbot")
st.write("Ask me anything!")

# User input
user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
            )
            st.text_area("AI:", response["choices"][0]["message"]["content"], height=150)
        except Exception as e:
            st.error(f"Error: {e}")