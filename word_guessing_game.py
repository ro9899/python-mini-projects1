"""
------------------------------------------------------------
🧠 Word Guessing Game in Python
------------------------------------------------------------
📘 Description:
The computer randomly selects a word, and the player tries
to guess it letter by letter. The game ends when the word
is fully guessed or the player runs out of attempts.

👩‍💻 Concepts Covered:
- Random choice
- Strings and lists
- Loops and conditionals
------------------------------------------------------------
"""

import random

print("🧠 Welcome to the Word Guessing Game!")
print("------------------------------------")

# Word list
words = ["python", "coding", "apple", "banana", "rocket", "planet", "school"]

# Choose a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  # number of wrong guesses allowed

# Game loop
while attempts > 0:
    print("\nWord:", " ".join(guessed))
    guess = input("🔤 Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter!")
        continue

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    # Check if word is fully guessed
    if "_" not in guessed:
        print("\n🎉 You guessed the word:", word)
        break
else:
    print("\n😞 Out of attempts! The word was:", word)
