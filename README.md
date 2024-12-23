# TaskTracker

A simple command-line task management program to help you keep track of tasks in two states: In Progress and Done. Tasks are stored persistently in files, allowing you to add, view, and mark tasks as done across sessions.

Features
  -Add Tasks
  -Add new tasks, which are automatically marked as "In Progress."
  -View Tasks

View tasks that are:
  -In Progress
  -Done
  -All tasks (both categories combined)
  
Mark Tasks as Done
  -Move tasks from the "In Progress" list to the "Done" list by selecting their number.
  
Persistent Storage
  -Tasks are saved in text files for persistence:
  -tasks_in_progress.txt: Stores tasks marked as "In Progress."
  -tasks_done.txt: Stores tasks marked as "Done."
  
How to Use
  -Run the script:
    python TaskTracker.py
    
Choose an option from the menu:

==== Task Tracker ====
1. View all tasks.
2. Add task.
3. Mark task as done.
4. Exit.
======================
Follow the on-screen prompts:

  -Add a Task: Type the name of the task when prompted.
  -View Tasks: Choose to view tasks that are done, in progress, or all tasks.
  -Mark Task as Done: Enter the number corresponding to the task in progress to move it to the "Done" list.
  
File Structure:

  -tasks_in_progress.txt: Stores tasks that are still in progress.
  -tasks_done.txt: Stores tasks that have been completed.
  -These files are automatically created if they don't already exist.

Example
  -Adding a Task:
Enter the name of the task to add: Write documentation
Task 'Write documentation' added and marked as 'in progress'.

Viewing Tasks:

=== Tasks In Progress ===
1. Write documentation
2. Review pull requests

=== Done Tasks ===
1. Fix login bug

Marking a Task as Done:

=== Tasks In Progress ===
1. Write documentation
2. Review pull requests

Enter the number of the task to mark as done: 1
Task 'Write documentation' marked as 'done'.

Requirements:
Python 3.6 or higher

Notes
-Ensure that you run the program in the same directory where the files (tasks_in_progress.txt and tasks_done.txt) are stored.
-To reset your tasks, simply delete the .txt files and run the program again.
-License
-This program is open-source and available for personal or educational use. Modify and distribute as needed. Contributions are welcome!
[https://github.com/Asollos/TaskTracker](https://roadmap.sh/projects/task-tracker)






