"""
------------------------------------------------------------
🎯 Hangman Game in Python
------------------------------------------------------------
📘 Description:
Classic hangman — guess the word letter by letter before 
you run out of lives. A fun word challenge game!

👩‍💻 Concepts Covered:
- Loops
- Random choice
- Lists and conditionals
------------------------------------------------------------
"""

import random

print("🎯 Welcome to Hangman!")
print("------------------------")

# Word list
words = ["python", "developer", "computer", "science", "keyboard", "hangman"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    guess = input("🔤 Guess a letter: ").lower()

    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    if "_" not in guessed:
        print("\n🎉 You saved the hangman! The word was:", word)
        break
else:
    print("\n💀 Game Over! The word was:", word)
