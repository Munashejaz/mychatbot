import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(user_input):
    try:
        # Use the updated OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit web interface
st.title("Ask OpenAI")
st.write("Enter your question below:")

# Input box for user question
user_input = st.text_input("Your question:")

# When the user presses the button, call OpenAI API and display response
if st.button("Get Answer"):
    if user_input:
        answer = get_openai_response(user_input)
        st.write(f"Answer: {answer}")
    else:
        st.write("Please enter a question.")