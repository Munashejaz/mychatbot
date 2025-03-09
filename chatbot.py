import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"]

print("Welcome to your Chatbox! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chat_with_gpt(user_input)
    print("Chatbot:", response)