"""
------------------------------------------------------------
🧾 Word Counter Tool in Python
------------------------------------------------------------
📘 Description:
This program counts how many words and characters are in a sentence or paragraph 
entered by the user. It's great for practicing loops, strings, and basic text analysis.

👩‍💻 Concepts Covered:
- Strings
- Built-in functions (split, len)
- User input
- Basic print formatting
------------------------------------------------------------
"""

print("🧾 Welcome to the Word Counter Tool!")
print("-----------------------------------")

# Take user input
text = input("✏️ Enter a sentence or paragraph: ")

# Count words and characters
word_count = len(text.split())
char_count = len(text)

# Display results
print("\n-----------------------------------")
print(f"📝 Total Words: {word_count}")
print(f"🔠 Total Characters (including spaces): {char_count}")
print("-----------------------------------")
print("✅ Counting complete! Perfect for your writing stats.")
