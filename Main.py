import openai
import time

class Juno:
    def __init__(self, api_key):
        openai.api_key = api_key  # Set the OpenAI API key for the assistant
        self.running = True
        self.name = "Juno 1.0"

    def greet(self):
        print("Juno 1.0: Hello! I am Juno, your AI assistant.")
        print("Type 'exit' to end the conversation.")

    def chat(self):
        self.greet()
        while self.running:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Juno 1.0: Goodbye!")
                self.running = False
            else:
                response = self.get_ai_response(user_input)
                print(f"Juno 1.0: {response}")

    def get_ai_response(self, user_input):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Using GPT-4 for AI responses
                messages=[{"role": "system", "content": "You are Juno, a helpful AI assistant."},
                          {"role": "user", "content": user_input}]
            )
            return response["choices"][0]["message"]["content"].strip()  # Extracting the AI response
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual OpenAI API key
    juno = Juno(api_key)  # Create a new instance of Juno with the API key
    juno.chat()  # Start the chat loop
