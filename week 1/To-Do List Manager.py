import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Task file is corrupted. Starting fresh.")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    due_date = input("Enter due date (optional): ")
    tags = input("Enter tags (comma-separated, optional): ")

    task = {
        "title": title,
        "done": False,
        "due_date": due_date if due_date else None,
        "tags": [tag.strip() for tag in tags.split(",")] if tags else []
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- To-Do List ---")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        due = f" | Due: {task['due_date']}" if task["due_date"] else ""
        tags = f" | Tags: {', '.join(task['tags'])}" if task["tags"] else ""

        print(f"{index}. [{status}] {task['title']}{due}{tags}")


def mark_task_done(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark done: "))
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
