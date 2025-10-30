"""
------------------------------------------------------------
⏳ Countdown Timer in Python
------------------------------------------------------------
📘 Description:
A simple timer that counts down from the number of seconds 
you enter and displays the time left in seconds.

👩‍💻 Concepts Covered:
- Loops
- Time module
- Basic math
------------------------------------------------------------
"""

import time

print("⏳ Welcome to the Countdown Timer!")
print("----------------------------------")

seconds = int(input("⏰ Enter time in seconds: "))

while seconds > 0:
    print(f"⏳ Time remaining: {seconds} seconds", end="\r")
    time.sleep(1)
    seconds -= 1

print("\n🎉 Time's up!")
