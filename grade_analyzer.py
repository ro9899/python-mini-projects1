"""
------------------------------------------------------------
📊 Student Marks & Grade Analyzer
------------------------------------------------------------
📘 Description:
This simple Python program takes a student's marks in different subjects,
calculates the total, average, and assigns a grade based on the score.

👩‍💻 Concepts Covered:
- Lists
- Loops
- Conditional statements
- User input
- Basic calculations
------------------------------------------------------------
"""

# Welcome message
print("📊 Welcome to the Student Grade Analyzer!")
print("-----------------------------------------")

# Take student name
name = input("Enter student name: ")

# Ask how many subjects
try:
    num_subjects = int(input("Enter number of subjects: "))
except ValueError:
    print("⚠️ Invalid input! Please enter a valid number next time.")
    exit()

# Create an empty list to store marks
marks = []

# Loop to take marks for each subject
for i in range(num_subjects):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i+1} (out of 100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("⚠️ Please enter marks between 0 and 100.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

# Calculate total, average, and percentage
total_marks = sum(marks)
average_marks = total_marks / num_subjects
percentage = average_marks

# Determine grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n-----------------------------------------")
print(f"📖 Student Name : {name}")
print(f"🧮 Total Marks  : {total_marks:.2f}")
print(f"📈 Average      : {average_marks:.2f}")
print(f"🎯 Percentage   : {percentage:.2f}%")
print(f"🏅 Grade        : {grade}")
print("-----------------------------------------")

# Feedback message
if grade == "A+":
    print("🌟 Excellent performance!")
elif grade == "A":
    print("👏 Great job! Keep it up!")
elif grade == "B":
    print("👍 Good work, but you can aim higher.")
elif grade == "C":
    print("🙂 Fair performance. Try to improve.")
elif grade == "D":
    print("😕 Needs improvement. Study harder!")
else:
    print("❌ Failed. Don’t give up, try again next time!")
