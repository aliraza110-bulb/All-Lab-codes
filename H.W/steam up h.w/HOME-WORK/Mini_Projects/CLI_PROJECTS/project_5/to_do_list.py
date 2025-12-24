tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
    elif choice == "2":
        if tasks:
            for i, t in enumerate(tasks, start=1):
                status = "Done" if t["done"] else "Pending"
                print(f"{i}. {t['task']} - {status}")
        else:
            print("No tasks added.")
    elif choice == "3":
        if tasks:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks added.")
    elif choice == "4":
        if tasks:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed['task']}' deleted.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks added.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
