"""
------------------------------------------------------------
🧮 Multiplication Table Generator in Python
------------------------------------------------------------
📘 Description:
This program prints the multiplication table for any number 
up to a limit chosen by the user.

👩‍💻 Concepts Covered:
- Loops
- User input
- Formatted printing
------------------------------------------------------------
"""

print("🧮 Multiplication Table Generator")
print("----------------------------------")

number = int(input("🔢 Enter a number: "))
limit = int(input("📏 Enter how far the table should go: "))

print(f"\n📘 Multiplication Table of {number}")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")

print("----------------------------------")
print("✅ Table generated successfully!")
