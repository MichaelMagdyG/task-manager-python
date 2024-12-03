# Task Manager

This Python project is a simple **Task Manager** that uses an SQLite database to manage tasks. It allows users to:

- Add tasks
- View a list of tasks
- Update the status of tasks (mark as complete or incomplete)
- Delete tasks

## Features

1. **Add a New Task**  
   Users can add tasks with a title, description, deadline, and priority (High, Medium, Low). 

2. **View Task List**  
   Displays all tasks with their details, including:
   - Task ID
   - Title
   - Priority
   - Deadline
   - Completion status (✅ for complete, ❌ for incomplete)

3. **Update Task Status**  
   Allows toggling between complete and incomplete for a specific task.

4. **Delete a Task**  
   Removes a task from the database permanently.

5. **Persistence with SQLite**  
   All tasks are stored in an SQLite database (`tasks.db`), ensuring data is retained between sessions.

## Prerequisites

- Python 3.x installed on your system.
- `sqlite3` module (included in Python's standard library).

## Setup Instructions

1. Clone the repository or copy the script.
2. Run the Python script:
   ```bash
   python task_manager.py
   ```
3. The program will create a SQLite database file (`tasks.db`) in the same directory if it doesn't exist.

## Usage

1. Run the script:
   ```bash
   python task_manager.py
   ```
2. Use the menu to interact with the program:
   - **Option 1**: Add a new task.
   - **Option 2**: View all tasks.
   - **Option 3**: Update the status of a task.
   - **Option 4**: Delete a task.
   - **Option 5**: Exit the program.

3. Follow the prompts for each menu option.

## Code Overview

### Database Schema
- **Table Name**: `tasks`
- **Columns**:
  - `id`: Auto-incrementing primary key.
  - `title`: Text (required).
  - `description`: Text (optional).
  - `deadline`: Text (formatted as `YYYY-MM-DD`).
  - `priority`: Text (`High`, `Medium`, `Low`).
  - `completed`: Integer (`0` for incomplete, `1` for complete, default is `0`).

### Key Functions
- `add_task()`: Adds a task to the database.
- `list_tasks()`: Displays all tasks in the database.
- `update_task()`: Toggles a task's completion status.
- `delete_task()`: Deletes a task by ID.
- `main_menu()`: The main interface for user interaction.

## Example Usage

### Adding a Task
```
Enter task title: Complete project
Enter task description: Finish the Python project by the weekend.
Enter task deadline (YYYY-MM-DD): 2024-12-01
Enter task priority (High, Medium, Low): High
✅ Task added successfully!
```

### Viewing Tasks
```
📋 Task List:
1. [❌] Complete project - (Priority: High, Deadline: 2024-12-01)
```

### Updating Task Status
```
Enter the task ID to change its status: 1
🔄 Task status updated!
```

### Deleting a Task
```
Enter the task ID to delete: 1
🗑️ Task deleted successfully!
```

## Screenshots
<div align="center">
  <img src="Screenshot%202024-11-27%20163939.jpg" alt="task Manager Python Screenshot">
</div>
