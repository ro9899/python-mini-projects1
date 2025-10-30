"""
------------------------------------------------------------
🎮 Rock, Paper, Scissors Game
------------------------------------------------------------
📘 Description:
A simple Python game where you play Rock, Paper, Scissors against the computer.
The computer makes a random choice, and the program decides the winner.

👩‍💻 Concepts Covered:
- Random module
- Conditional statements
- Loops
- User input
------------------------------------------------------------
"""

import random  # Import random for computer's move

# Available choices
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("------------------------------------")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' anytime to quit the game.\n")

# Game loop
while True:
    # Get user choice
    user_choice = input("👉 Your choice: ").lower()

    # Exit condition
    if user_choice == "exit":
        print("👋 Thanks for playing! Goodbye!")
        break

    # Validate user input
    if user_choice not in choices:
        print("⚠️ Invalid choice! Please type rock, paper, or scissors.")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"💻 Computer chose: {computer_choice}")

    # Decide winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🏆 You win!")
    else:
        print("😞 Computer wins!")

    print("------------------------------------")
