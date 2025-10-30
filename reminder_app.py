"""
------------------------------------------------------------
⏰ Simple Reminder App using Python
------------------------------------------------------------
📘 Description:
A simple console-based reminder app that asks the user
for a reminder message and time delay (in seconds), then
notifies them when the time is up.

👩‍💻 Concepts Covered:
- time module (sleep)
- User input
- Loops and conditionals
------------------------------------------------------------
"""

import time

print("⏰ Welcome to the Simple Reminder App!")
print("--------------------------------------")

# Ask user for reminder details
reminder = input("📝 What would you like me to remind you about? ")
seconds = int(input("⏳ In how many seconds should I remind you? "))

print(f"✅ Reminder set! I’ll remind you in {seconds} seconds.\n")

# Wait for the given time
time.sleep(seconds)

# Reminder message
print("🔔 Time’s up!")
print(f"📢 Reminder: {reminder}")
