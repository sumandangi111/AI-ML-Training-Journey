def load__tasks():
    tasks=[]
    try:
        with open("sample.txt","r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("No previous task file found!")
    return tasks


def save_tasks(tasks):
    with open("sample.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")

def add_task(tasks):
    task=input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task Added Successfully!")

def view_tasks(tasks):
    if len(tasks)==0:
        print("No Tasks Available")
    else:
        print("\n----------Your Tasks---------")
        for index,task in enumerate(tasks, start=1):
            print(f"{index}. {task}")