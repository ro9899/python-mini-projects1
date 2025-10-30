"""
------------------------------------------------------------
💡 BMI (Body Mass Index) Calculator in Python
------------------------------------------------------------
📘 Description:
A simple program that calculates your Body Mass Index (BMI)
based on your height and weight, and tells you your health category.

👩‍💻 Concepts Covered:
- Basic math operations
- Conditionals (if-elif-else)
- User input
- Formatting output
------------------------------------------------------------
"""

print("💪 Welcome to the BMI Calculator!")
print("--------------------------------")

# Take user input
weight = float(input("⚖️ Enter your weight (in kilograms): "))
height = float(input("📏 Enter your height (in meters): "))

# BMI formula
bmi = weight / (height ** 2)

# Determine health category
print("\n--------------------------------")
print(f"📊 Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("🟡 Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("🟢 Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("🟠 Category: Overweight")
else:
    print("🔴 Category: Obese")

print("--------------------------------")
print("💡 Tip: Maintain a balanced diet and exercise regularly!")
