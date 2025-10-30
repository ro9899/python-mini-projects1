"""
------------------------------------------------------------
📝 To-Do List App using Python
------------------------------------------------------------
📘 Description:
A simple console-based To-Do List application that allows users 
to add, view, remove, and clear tasks.

👩‍💻 Concepts Covered:
- Lists
- Loops
- Conditional statements
- Functions
- User input
------------------------------------------------------------
"""

# Initialize an empty list to store tasks
tasks = []


# Function to display all tasks
def show_tasks():
    """Display all the tasks in the list."""
    if len(tasks) == 0:
        print("📭 No tasks found! Your to-do list is empty.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):  # enumerate starts counting from 1
            print(f"{i}. {task}")


# Function to add a new task
def add_task():
    """Add a new task entered by the user."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added successfully!")


# Function to remove a specific task
def remove_task():
    """Remove a task using its number."""
    show_tasks()  # Display tasks first
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Task '{removed}' removed successfully!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number.")


# Function to clear all tasks
def clear_tasks():
    """Remove all tasks from the list."""
    confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()
    if confirm == 'y':
        tasks.clear()
        print("🧹 All tasks cleared!")
    else:
        print("❌ Action canceled.")


# Main program starts here
print("📝 Welcome to Your To-Do List App!")
print("----------------------------------")

while True:
    # Display menu options
    print("\nChoose an option:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Clear all tasks")
    print("5. Exit")

    # Get user's choice
    choice = input("Enter your choice (1-5): ")

    # Handle each choice
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        clear_tasks()
    elif choice == '5':
        print("👋 Exiting To-Do List App. Have a productive day!")
        break
    else:
        print("⚠️ Invalid choice! Please select a number between 1 and 5.")
