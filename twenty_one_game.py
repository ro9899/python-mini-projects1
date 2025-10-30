"""
------------------------------------------------------------
🃏 21 Number Game in Python
------------------------------------------------------------
📘 Description:
The player and computer take turns adding numbers (1–3)
to a total. Whoever reaches exactly 21 wins.

👩‍💻 Concepts Covered:
- Loops
- Conditionals
- Random module
------------------------------------------------------------
"""

import random

print("🃏 Welcome to the 21 Number Game!")
print("----------------------------------")

total = 0

while total < 21:
    user = int(input("👉 Enter a number (1–3): "))

    if user not in [1, 2, 3]:
        print("⚠️ Invalid choice! Choose between 1 and 3.")
        continue

    total += user
    print(f"🧍 You: {user}, Total = {total}")

    if total >= 21:
        print("🎉 You reached 21! You win!")
        break

    comp = random.randint(1, 3)
    total += comp
    print(f"💻 Computer: {comp}, Total = {total}")

    if total >= 21:
        print("💀 Computer reached 21! You lose!")
        break
