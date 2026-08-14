tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

def complete_task():
    show_tasks()

    if not tasks:
        return

    number = int(input("Enter task number to complete: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid task number.")

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")