import sqlite3
from datetime import datetime

# Create or connect to the database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    deadline TEXT,
    priority TEXT,
    completed INTEGER DEFAULT 0
)
""")
conn.commit()

# Function to add a new task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    priority = input("Enter task priority (High, Medium, Low): ")

    cursor.execute("""
    INSERT INTO tasks (title, description, deadline, priority)
    VALUES (?, ?, ?, ?)
    """, (title, description, deadline, priority))
    conn.commit()
    print("✅ Task added successfully!\n")

# Function to list all tasks
def list_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("📭 No tasks available yet.\n")
        return

    print("\n📋 Task List:")
    for task in tasks:
        status = "✅" if task[5] == 1 else "❌"
        print(
            f"{task[0]}. [{status}] {task[1]} - (Priority: {task[4]}, Deadline: {task[3]})"
        )
    print()

# Function to update task status
def update_task():
    list_tasks()
    task_id = int(input("Enter the task ID to change its status: "))

    cursor.execute("SELECT completed FROM tasks WHERE id = ?", (task_id,))
    result = cursor.fetchone()
    if result:
        new_status = 0 if result[0] == 1 else 1
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (new_status, task_id))
        conn.commit()
        print("🔄 Task status updated!\n")
    else:
        print("❌ Invalid task ID.\n")

# Function to delete a task
def delete_task():
    list_tasks()
    task_id = int(input("Enter the task ID to delete: "))

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("🗑️ Task deleted successfully!\n")

# Main menu
def main_menu():
    while True:
        print("🎯 Options Menu:")
        print("1. Add a new task")
        print("2. View task list")
        print("3. Update task status")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye!")
            conn.close()  # Close the database connection
            break
        else:
            print("❌ Invalid choice.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
1