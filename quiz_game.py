"""
------------------------------------------------------------
🧠 Python Quiz Game
------------------------------------------------------------
📘 Description:
A simple console-based quiz game where the player answers 
multiple-choice questions and gets a score at the end.

👩‍💻 Concepts Covered:
- Lists and dictionaries
- Loops
- Conditional statements
- User input
------------------------------------------------------------
"""

print("🧠 Welcome to the Python Quiz Game!")
print("----------------------------------")
print("Answer the questions below. Type A, B, C, or D.\n")

# List of quiz questions
quiz = [
    {
        "question": "1️⃣ What is the output of: print(2 + 3 * 4)?",
        "options": ["A. 20", "B. 14", "C. 24", "D. 9"],
        "answer": "B"
    },
    {
        "question": "2️⃣ Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "3️⃣ What data type is this: [1, 2, 3]?",
        "options": ["A. Tuple", "B. Set", "C. List", "D. Dictionary"],
        "answer": "C"
    },
    {
        "question": "4️⃣ What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .py", "C. .pyt", "D. .python"],
        "answer": "B"
    },
    {
        "question": "5️⃣ What is the output of: print('Hello' + 'World')?",
        "options": ["A. Hello World", "B. Hello+World", "C. HelloWorld", "D. Error"],
        "answer": "C"
    }
]

score = 0  # Initialize score

# Loop through each question
for q in quiz:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    # Get user answer
    answer = input("👉 Enter your answer (A/B/C/D): ").upper()

    # Check answer
    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

# Final score
print("----------------------------------")
print(f"🏁 Quiz Finished! Your Score: {score}/{len(quiz)}")

# Feedback message
if score == len(quiz):
    print("🌟 Excellent! You got all answers right!")
elif score >= 3:
    print("👏 Good job! You know Python basics well.")
else:
    print("💡 Keep practicing — you’ll get better!")
print("----------------------------------")
