"""
------------------------------------------------------------
💬 Simple Chatbot Simulation in Python
------------------------------------------------------------
📘 Description:
A fun chatbot that replies to basic greetings and questions.

👩‍💻 Concepts Covered:
- If-elif conditions
- User input
- String matching
------------------------------------------------------------
"""

print("🤖 Hello! I’m PyBot — your friendly chatbot.")
print("💬 Type 'bye' to exit.")
print("--------------------------------------------")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("PyBot: Hello there! How are you?")
    elif "how are you" in user_input:
        print("PyBot: I'm just code, but I feel awesome! 😄")
    elif "name" in user_input:
        print("PyBot: My name is PyBot. What's yours?")
    elif "bye" in user_input:
        print("PyBot: Goodbye! 👋 Have a great day!")
        break
    else:
        print("PyBot: Sorry, I didn’t understand that 🤔")
