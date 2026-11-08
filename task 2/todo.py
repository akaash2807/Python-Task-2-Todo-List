
# To-Do List Application

tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for item in tasks:
                file.write(item + "\n")

        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)

                with open("tasks.txt", "w") as file:
                    for item in tasks:
                        file.write(item + "\n")

                print("Task removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice. Try again.")
