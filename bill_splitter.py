"""
------------------------------------------------------------
🧾 Bill Splitter in Python
------------------------------------------------------------
📘 Description:
This program helps you split a total bill among friends.
It calculates how much each person needs to pay equally.

👩‍💻 Concepts Covered:
- User input
- Type casting (float and int)
- Basic arithmetic operations
- Conditional logic
- Output formatting
------------------------------------------------------------
"""

print("🧾 Welcome to the Bill Splitter!")
print("--------------------------------")

# Take total bill amount from user
total_bill = float(input("💵 Enter the total bill amount (in ₹): "))

# Take number of friends
num_friends = int(input("👥 Enter the number of friends: "))

# Avoid division by zero
if num_friends <= 0:
    print("⚠️ Number of friends must be greater than 0.")
else:
    # Calculate how much each friend should pay
    per_person = total_bill / num_friends

    print("\n--------------------------------")
    print(f"💰 Total Bill: ₹{total_bill:.2f}")
    print(f"👥 Number of Friends: {num_friends}")
    print(f"🧮 Each Person Pays: ₹{per_person:.2f}")
    print("--------------------------------")
    print("✅ Bill successfully split!")
