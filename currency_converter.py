"""
------------------------------------------------------------
💰 Currency Converter using Python
------------------------------------------------------------
📘 Description:
A simple console-based currency converter that converts an amount
from Indian Rupees (INR) to other currencies (USD, EUR, GBP, JPY)
using predefined exchange rates.

👩‍💻 Concepts Covered:
- Dictionaries
- Loops
- Conditional statements
- User input
- Basic math operations
------------------------------------------------------------
"""

# Predefined currency exchange rates (for example purpose)
# Note: In a real app, these would be fetched from an API
exchange_rates = {
    "USD": 0.012,  # 1 INR = 0.012 USD
    "EUR": 0.011,  # 1 INR = 0.011 EUR
    "GBP": 0.009,  # 1 INR = 0.009 GBP
    "JPY": 1.80    # 1 INR = 1.80 JPY
}

print("💰 Welcome to the Currency Converter!")
print("-------------------------------------")
print("Supported currencies: USD, EUR, GBP, JPY")

# Main loop
while True:
    try:
        # Take input from user
        amount_in_inr = float(input("\nEnter amount in INR (₹): "))
        target_currency = input("Enter target currency code (USD/EUR/GBP/JPY): ").upper()

        # Check if currency is supported
        if target_currency not in exchange_rates:
            print("⚠️ Invalid currency code! Please try again.")
            continue

        # Conversion logic
        converted_amount = amount_in_inr * exchange_rates[target_currency]

        # Display result
        print(f"✅ {amount_in_inr:.2f} INR = {converted_amount:.2f} {target_currency}")

        # Ask if user wants another conversion
        again = input("\nDo you want to convert another amount? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for using Currency Converter! Goodbye!")
            break

    except ValueError:
        print("⚠️ Invalid input! Please enter a number for amount.")
