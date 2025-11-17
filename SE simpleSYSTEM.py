def show_menu():
    print("\n=== Simple Task Manager ===")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Exit")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"\n✔ Task added: {task}")
        view_tasks(tasks)  # <-- show updated list automatically
    else:
        print("⚠ Task cannot be empty.")


def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("⚠ Invalid choice, please select 1-3.")


if __name__ == "__main__":
    main()
