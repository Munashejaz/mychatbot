import openai

# Set up your OpenAI API key (Replace with your actual key)
API_KEY = "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"

# Create the OpenAI client with the API key
client = openai.OpenAI(api_key=API_KEY)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Simple chat loop
print("Welcome to your chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = chat_with_gpt(user_input)
    print("Chatbot:", response)