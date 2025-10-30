"""
------------------------------------------------------------
🧮 Simple Calculator using Python
------------------------------------------------------------
📘 Description:
A beginner-friendly Python program that performs basic arithmetic
operations: addition, subtraction, multiplication, and division.

👩‍💻 Concepts Covered:
- Functions
- Loops
- Conditional statements (if-else)
- User input
- Error handling
------------------------------------------------------------
"""

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers (with error handling)
def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    else:
        return a / b


# Main program starts here
print("🧮 Welcome to the Simple Calculator!")
print("-----------------------------------")

# Infinite loop allows user to perform multiple calculations
while True:
    # Display menu options
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")

    # Take user's choice
    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == '5':
        print("👋 Exiting Calculator. Have a nice day!")
        break

    # Take user inputs for numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
        continue

    # Perform the selected operation
    if choice == '1':
        print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"✅ Result: {num1} × {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"✅ Result: {num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("⚠️ Invalid choice! Please select a number between 1 and 5.")
