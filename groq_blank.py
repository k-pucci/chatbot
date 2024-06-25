import os
from groq import Groq

# Set the API key
os.environ["GROQ_API_KEY"] = "ENTER API KEY HERE"

# Create a Groq client
client = Groq()

# Function to send a message and get the assistant's response
def send_message(messages):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Main chat loop
def main():
    print("Welcome to the Groq Chat Messaging Application!")
    print("Type 'quit' to exit.")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})
        response = send_message(messages)
        messages.append({"role": "assistant", "content": response})
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()