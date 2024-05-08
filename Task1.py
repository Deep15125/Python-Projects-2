class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_complete(self, task):
        if isinstance(task, Task):
            task.completed = True
        elif isinstance(task, int) and 0 <= task < len(self.tasks):
            self.tasks[task].completed = True
        else:
            print("Invalid task")

    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "[x]" if task.completed else "[ ]"
            print(f"{status} {i+1}: {task.description}")
            
def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. Mark complete")
        print("3. View tasks")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter task description: ")
            to_do_list.add_task(description)
        elif choice == 2:
            task_num = int(input("Enter task number to mark as complete: ")) - 1
            to_do_list.mark_complete(task_num)
        elif choice == 3:
            to_do_list.view_tasks()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()