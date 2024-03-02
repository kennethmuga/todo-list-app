class ToDoList:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        # Add a new task to the list and append
        self.tasks.append({"task": task, "completed": False})

    def mark_task_complete(self, index):
        # Mark a task as complete based on its index
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            # Display error message if index is out of range
            print("Invalid task index.")

    def delete_task(self, index):
        # Delete a task from the list based on its index
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            # Display error message if index is out of range
            print("Invalid task index.")

    def view_tasks(self):
        # Display all tasks in the list along with their completion status
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i+1}. [{status}] {task['task']}")


def main():
    # Create a new ToDoList object
    todo_list = ToDoList()

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new task
            task = input("Enter task to add: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            # Mark a task as complete
            index = int(input("Enter index of task to mark as complete: ")) - 1
            todo_list.mark_task_complete(index)
            print("Task marked as complete.")
        elif choice == "3":
            # Delete a task
            index = int(input("Enter index of task to delete: ")) - 1
            todo_list.delete_task(index)
            print("Task deleted.")
        elif choice == "4":
            # View all tasks
            todo_list.view_tasks()
        elif choice == "5":
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Display error message for invalid choices
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
