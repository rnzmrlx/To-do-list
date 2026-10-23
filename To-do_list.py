tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        priority = input("Priority (High/Medium/Low): ").capitalize()

        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"
            print("Invalid priority. Defaulting to Medium.")

        tasks.append({
            "name": task,
            "priority": priority,
            "completed": False
        })
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for number, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(
                    f'{number}. {task["name"]} '
                    f'| Priority: {task["priority"]} '
                    f'| Status: {status}'
                )

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f'{number}. {task["name"]}')

            try:
                number = int(input("Enter task number to complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f'{number}. {task["name"]}')

            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f'Task "{removed["name"]}" deleted!')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
