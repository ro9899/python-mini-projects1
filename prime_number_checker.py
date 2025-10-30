"""
------------------------------------------------------------
🔢 Prime Number Checker in Python
------------------------------------------------------------
📘 Description:
This program checks whether a number entered by the user is a prime number or not.

👩‍💻 Concepts Covered:
- Loops (for)
- Conditionals (if-else)
- User input and output
- Basic number logic
------------------------------------------------------------
"""

print("🔢 Welcome to the Prime Number Checker!")
print("--------------------------------------")

# Take input from the user
num = int(input("Enter a number to check: "))

# Prime number logic
if num <= 1:
    print("❌ Not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"❌ {num} is not a prime number. (Divisible by {i})")
            break
    else:
        print(f"✅ {num} is a prime number!")

print("--------------------------------------")
print("🧠 Tip: Prime numbers are divisible only by 1 and themselves.")
