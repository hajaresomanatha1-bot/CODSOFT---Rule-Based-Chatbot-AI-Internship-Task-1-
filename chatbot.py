# Rule-Based Chatbot
# CODSOFT AI Internship - Task 1

print("Chatbot: Hello! I am your simple chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Greetings
    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi there! How can I help you?")

    elif "how are you" in user_input:
        print("Chatbot: I am just a chatbot, but I am doing great!")

    elif "your name" in user_input:
        print("Chatbot: I am a simple rule-based chatbot.")

    elif "help" in user_input:
        print("Chatbot: I can respond to greetings and simple questions.")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break

    else:
        print("Chatbot: Sorry, I don't understand that. Try something else.")
