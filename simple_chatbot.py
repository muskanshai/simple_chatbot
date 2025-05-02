def chatbot():
    print("Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if 'bye' in user_input:
            print("Chatbot: Goodbye! Take care.")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I help you?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just code, but I'm running fine!")
        elif 'sore throat' in user_input:
            print("Chatbot: You might try warm fluids, rest, and see a doctor if it persists.")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()

