from model import generate_response

def chatbot():
    """
    Interactive chat function with Gemma-2b chatbot.
    """
    print("Welcome to the Gemma-2b Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        model_response = generate_response(user_input)
        print("Gemma-2b ---> ", model_response)

    print("Goodbye!")

if __name__ == "__main__":
    chatbot()
