import os

# File paths
IN_PROGRESS_FILE = "tasks_in_progress.json"
DONE_FILE = "tasks_done.json"

# Ensure files exist
for file in [IN_PROGRESS_FILE, DONE_FILE]:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass  # Create empty files if they don't exist

def display_tasks(tasks, header):
    """Display tasks with numbered indices."""
    print(f"\n=== {header} ===")
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task.strip()}")

def view_tasks():
    choice = input("1. Tasks that are done\n2. Tasks that are in progress\n3. All Tasks\nSelect an option: ")
    if choice == "1":
        with open(DONE_FILE, 'r') as f:
            tasks = f.readlines()
        display_tasks(tasks, "Done Tasks")
    elif choice == "2":
        with open(IN_PROGRESS_FILE, 'r') as f:
            tasks = f.readlines()
        display_tasks(tasks, "Tasks In Progress")
    elif choice == "3":
        with open(IN_PROGRESS_FILE, 'r') as f:
            in_progress_tasks = f.readlines()
        with open(DONE_FILE, 'r') as f:
            done_tasks = f.readlines()
        print("\n--- In Progress ---")
        display_tasks(in_progress_tasks, "In Progress")
        print("\n--- Done ---")
        display_tasks(done_tasks, "Done")
    else:
        print("Invalid choice.")

def add_task():
    task = input("Enter the name of the task to add: ")
    with open(IN_PROGRESS_FILE, 'a') as f:
        f.write(task + '\n')
    print(f"Task '{task}' added and marked as 'in progress'.")

def mark_task_done():
    with open(IN_PROGRESS_FILE, 'r') as f:
        tasks_in_progress = f.readlines()

    if not tasks_in_progress:
        print("No tasks in progress to mark as done.")
        return

    print("\n=== Tasks In Progress ===")
    for idx, task in enumerate(tasks_in_progress, 1):
        print(f"{idx}. {task.strip()}")

    try:
        task_index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= task_index < len(tasks_in_progress):
            task_to_mark = tasks_in_progress[task_index].strip()
            with open(DONE_FILE, 'a') as done_file:
                done_file.write(task_to_mark + '\n')
            with open(IN_PROGRESS_FILE, 'w') as f:
                for idx, task in enumerate(tasks_in_progress):
                    if idx != task_index:
                        f.write(task)
            print(f"Task '{task_to_mark}' marked as 'done'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
while True:
    print("\n==== Task Tracker ====")
    print("1. View all tasks.")
    print("2. Add task.")
    print("3. Mark task as done.")
    print("4. Exit.")
    print("======================")
    user_input = input("Select a number (1-4): ")

    if user_input == "1":
        view_tasks()
    elif user_input == "2":
        add_task()
    elif user_input == "3":
        mark_task_done()
    elif user_input == "4":
        print("Exiting Task Tracker. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
