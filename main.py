from src.manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\nTASK MANAGER")
        print("1.List All Tasks")
        print("2.Add a Task")
        print("3.Complete a Task")
        print("4.Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            title = input("Enter task title: ").strip()
            desc = input("Enter task description (optional): ").strip()
            if title:
                manager.add_task(title, desc)
            else:
                print("Title cannot be empty.")
        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid numerical ID.")
        elif choice == "4":
            print("Goodbye! Thanks for staying organized.")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 4.")

if __name__ == "__main__":
    main()