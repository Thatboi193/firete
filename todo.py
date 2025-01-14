import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("D:/firetest/firetest/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
print("Database Connected")

tasks_ref = db.collection("todo")

def add_task():
    task_title = input("Enter task name: ").strip().lower()
    task_description = input("Enter task description: ").strip().lower()
    task_day = input("Enter task deadline: ").strip().lower()
    task_prority = input("Enter task prority: ").strip().lower()
    task_complete = input("Is Task complete True/False: ").strip().lower()

    try:
        task_prority = int(task_prority)
        if task_prority not in range(1,6):
            raise ValueError("Priority msut be 1-5")

        task_day = datetime.strptime(task_day ,"%Y-%m-%d")

        if task_complete == "True":
            task_complete = True
        else:
            task_complete = False

        tasks_ref.add({
            "Title": task_title,
            "Description": task_description,
            "Datetime": task_day,
            "Priority": task_prority,
            "Complete": task_complete
        })
        print("Task added successfully")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        


def display_tasks():
    tasks = tasks_ref.stream()
    print("Your todo list")
    print("-" * 30)
    for task in tasks:
        task_data = task.to_dict()
        print(f"ID: {task.id} : {task_data["Title"]} : {task_data["Description"]} : {task_data["Priority"]} : {task_data["Datetime"]} : {task_data["Complete"]}")

    print("-" * 30)

def delete_task():
    task_id = input("Enter task id TO DELETE: ").strip()
    task = tasks_ref.document(task_id)

    try:
        task.delete()
        print("Task deleted")
    except Exception as e:
        print(f"Error: {e}")

def edit_task():
    task_id = input("Enter task id to edit: ").strip()
    task = tasks_ref.document(task_id)
    newtext = input("Enter new title: ").strip()
    
    try:
        task.update({"Title" : newtext})
        print("update success")
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("TO-DO List Manager")
        print("1. Display Tasks")
        print("2. Add Tasks")
        print("3. Edit Tasks")
        print("4. DELETE Tasks")
        print("5. EXIT Tasks")

        choice = input("Enter choice 1-5: ").strip

        match choice:
            case 1:
                display_tasks()
            case 2:
                add_task()
            case 3:
                edit_task()
            case 4:
                delete_task()
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. exiting...")
                break


if __name__ == "__main__":
    #add_task()
    #display_tasks()
    #delete_task()
    #edit_task()
    main()
