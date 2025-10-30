"""
------------------------------------------------------------
🔐 Password Generator using Python
------------------------------------------------------------
📘 Description:
This project generates a strong random password based on 
user-defined length. The password includes uppercase letters, 
lowercase letters, numbers, and special characters.

👩‍💻 Concepts Covered:
- Random module
- Strings
- Loops
- User input
------------------------------------------------------------
"""

import random
import string  # contains letters, digits, and punctuation

# Welcome message
print("🔐 Welcome to the Password Generator!")
print("-------------------------------------")

# Ask the user for desired password length
try:
    length = int(input("Enter the desired password length (e.g., 8-20): "))
except ValueError:
    print("⚠️ Invalid input! Please enter a number next time.")
    exit()

# Define all possible characters for the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# Check if length is valid
if length < 4:
    print("⚠️ Password too short! Minimum length should be 4.")
else:
    # Randomly generate password using the user's chosen length
    password = "".join(random.choice(all_characters) for _ in range(length))

    # Display the generated password
    print(f"\n✅ Your secure password is:\n👉 {password}")

    # Optional: Ask user if they want another one
    again = input("\nWould you like to generate another password? (y/n): ").lower()
    if again == 'y':
        length = int(input("Enter new password length: "))
        password = "".join(random.choice(all_characters) for _ in range(length))
        print(f"\n🔁 Your new password is:\n👉 {password}")
    else:
        print("👋 Thank you for using Password Generator! Stay secure!")
