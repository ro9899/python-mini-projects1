"""
------------------------------------------------------------
💰 Expense Tracker in Python
------------------------------------------------------------
📘 Description:
A simple program to track daily expenses. 
You can add expenses with names and amounts, 
and it will show the total spent so far.

👩‍💻 Concepts Covered:
- Lists and dictionaries
- Loops
- User input
- Sum calculation
------------------------------------------------------------
"""

print("💰 Welcome to the Expense Tracker!")
print("----------------------------------")

expenses = []  # list to store (name, amount) pairs

while True:
    name = input("🛍️ Enter expense name (or 'q' to quit): ")

    if name.lower() == "q":
        break  # stop when user types 'q'

    amount = float(input("💵 Enter amount spent (in ₹): "))
    expenses.append({"name": name, "amount": amount})

# Display results
print("\n----------------------------------")
print("📋 Your Expense Summary:")
total = 0
for item in expenses:
    print(f"- {item['name']}: ₹{item['amount']}")
    total += item["amount"]

print("----------------------------------")
print(f"💰 Total Spent: ₹{total}")
print("✅ Tracking complete. Stay mindful of your budget!")
