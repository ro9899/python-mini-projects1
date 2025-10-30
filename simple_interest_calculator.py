"""
------------------------------------------------------------
💰 Simple Interest Calculator in Python
------------------------------------------------------------
📘 Description:
This program calculates the Simple Interest and Total Amount
based on the Principal amount, Rate of Interest, and Time period.

👩‍💻 Concepts Covered:
- Basic math operations
- User input
- Type casting
- String formatting
------------------------------------------------------------
"""

print("💰 Welcome to the Simple Interest Calculator!")
print("------------------------------------------------")

# Taking inputs from the user
principal = float(input("🏦 Enter the Principal amount (in ₹): "))
rate = float(input("📈 Enter the Rate of Interest (in %): "))
time = float(input("⏳ Enter the Time (in years): "))

# Formula for Simple Interest
simple_interest = (principal * rate * time) / 100

# Total amount = Principal + Interest
total_amount = principal + simple_interest

# Display the results
print("\n------------------------------------------------")
print(f"💵 Simple Interest: ₹{simple_interest:.2f}")
print(f"💰 Total Amount after {time} years: ₹{total_amount:.2f}")
print("------------------------------------------------")
print("✅ Calculation complete! Save and invest wisely.")
