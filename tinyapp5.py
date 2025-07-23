#Setup

tasks = []


# Add task

def add_task():
    task_name = input("Enter task: ")
    task = {
        "name": task_name,
        "done": False
    }
    tasks.append(task)
    print("Task added!")


#View tasks

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for idx, t in enumerate(tasks): #enumerate() gives you the index + task.
            status = "✅" if t["done"] else "❌" #✅ or ❌ shows if done.
            print(f"{idx+1}. {t['name']} [{status}]")


#Mark done

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark done: "))
    if 0 < num <= len(tasks):
        tasks[num - 1]["done"] = True
        print("Marked as done!")
    else:
        print("Invalid number.")


#Delete task

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!")
    else:
        print("Invalid number.")


#Save tasks

def save_tasks():
    file = open("tasks.txt", "w")
    for t in tasks:
        line = f"{t['name']},{t['done']}\n"
        file.write(line)
    file.close()
    print("Tasks saved.")


#Load tasks

def load_tasks():
    try:
        file = open("tasks.txt", "r")
        for line in file:
            name, done = line.strip().split(",")
            task = {
                "name": name,
                "done": done == "True"
            }
            tasks.append(task)
        file.close()
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks yet.")


#Main loop

def main():
    load_tasks()
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Mark task done")
        print("4. Delete task")
        print("5. Save tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()


# CRUD for tasks.

# Marks tasks done (status change).

# Deletes tasks.

# Saves & loads tasks to a file.