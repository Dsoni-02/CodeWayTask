tasks = []

def createTask():
    task = input("Enter a task ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def updateTask():
    if not tasks:
        print("No tasks to update. Please create a task first.")
        return
    print("Current Tasks : ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}.{task}")

        task_index = int (input("Enter the task number to update : "))

        if 1 <= task_index <= len(tasks):
            newTask = input("Enter the updated task description : ")
            tasks[task_index -1] ["description"] = newTask
            print("Task updated successfully!")
            print("Updated tasks : ")
            for task in tasks:
                print(task)
            
        else:
             print("Invalid task number. Please choose a valid taskl.")

             
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        print("current Tasks :")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {tasks}")
def deleteTasks():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if tasktoDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found. ")

    except:
        print("Invalid input.")
        
    
print("Welcome to the to do list app : )")
while True :
    print("\n")
    print("Select one of the following options")
    print("-----------------------------------")
    print("1. Create a new Task")
    print("2. Update a Task")
    print("3. Current Tasks")
    print("4. Delete the Tasks")
    print("5. Quit")

    choice = input("Enter your choice : ")

    if(choice == "1"):
        createTask()
    elif(choice == "2"):
        updateTask()
    elif(choice == "3"):
        listTasks()
    elif(choice == "4"):
        deleteTasks()
    elif(choice == "5"):
        break
    else:
        print("Invalid input. Please try again.")
        
