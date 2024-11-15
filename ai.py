import os
import openai

# Load API key from environment variable
openai.api_key = os.getenv("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")

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print("Chatbot initialized! Type 'quit', 'exit', or 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
