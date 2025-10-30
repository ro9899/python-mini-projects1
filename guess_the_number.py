


"""
------------------------------------------------------------
🎯 Guess the Number Game
------------------------------------------------------------
📘 Description:
A fun Python game where the computer randomly selects a number 
between 1 and 100, and the player tries to guess it.

👩‍💻 Concepts Covered:
- Random number generation
- Loops
- Conditional statements
- User input
------------------------------------------------------------
"""

import random  # Import the random module to generate random numbers

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Welcome message
print("🎯 Welcome to the Guess the Number Game!")
print("----------------------------------------")
print("I'm thinking of a number between 1 and 100...")
print("Try to guess it! 🤔")

# Initialize number of attempts
attempts = 0

# Game loop
while True:
    try:
        # Ask user for their guess
        guess = int(input("\nEnter your guess: "))
        attempts += 1  # Increase attempt count by 1 each time

        # Compare guess with the secret number
        if guess < secret_number:
            print("📉 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📈 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break  # Exit loop when guessed correctly

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")


# Ask if player wants to play again
play_again = input("\nWould you like to play again? (y/n): ").lower()

if play_again == 'y':
    print("🔁 Restart the game to play again!")
else:
    print("👋 Thanks for playing! Goodbye!")
