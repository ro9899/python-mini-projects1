"""
------------------------------------------------------------
🎲 Dice Roller Simulator in Python
------------------------------------------------------------
📘 Description:
A simple Python program that simulates rolling a dice.
Each roll gives a random number between 1 and 6.
The user can roll multiple times until they quit.

👩‍💻 Concepts Covered:
- Random module
- Loops and conditionals
- User input
------------------------------------------------------------
"""

import random  # To generate random dice numbers

print("🎲 Welcome to the Dice Roller Simulator!")
print("---------------------------------------")

while True:
    # Ask user to roll
    choice = input("👉 Press Enter to roll the dice or type 'q' to quit: ").lower()

    if choice == "q":
        print("👋 Thanks for playing! Goodbye!")
        break

    # Generate random number between 1 and 6
    dice_number = random.randint(1, 6)
    print(f"🎯 You rolled: {dice_number}\n")
