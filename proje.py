import json
import os
from datetime import datetime

tasks=[]
FILE_NAME = "tasks.json"


def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            tasks = json.load(f)


def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def entr():
    print("To-do List")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Complete Tasks")
    print("5. Exit")

def add_task():
    sntc = input("Add Task: ")
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    tasks.append({"task": sntc, "complete":False, "date": date})
    save_tasks()
    print(f"'{sntc}' added as task.")

def delete_task():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']}")

    try:
        index = int(input("Which task number to delete? ")) - 1
        deleted = tasks.pop(index)
        save_tasks()
        print(f"'{deleted['task']}' was deleted.")
    except (ValueError, IndexError):
        print("Invalid number!")


# def complete_task():
#      cmp= int(input("The task number you want to complete: ")) - 1
#      if 0<= cmp <len(tasks):
#          tasks[cmp]["complete"]=True
#          print(f"Your task '{tasks[cmp]['sentence']}' is complete.")
#      else:
#          print("No such task found!!")

def complete_task():
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["complete"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

    user_input = input("The task number you want to complete: ")

    if not user_input.isdigit():
        print("Please enter a valid number.")
        return

    cmp = int(user_input) - 1

    if 0 <= cmp < len(tasks):
        if tasks[cmp]["complete"]:
            print(f"The task '{tasks[cmp]['task']}' is already completed.")
        else:
            tasks[cmp]["complete"] = True
            save_tasks()
            print(f"Your task '{tasks[cmp]['task']}' is now marked as complete.")
    else:
        print("No such task found.")

load_tasks()

while True:
    entr()
    choose=input("Please enter (1-2-3-4-5):")
    if choose== "1":
        add_task()
    elif choose== "2":
        delete_task()
    elif choose== "3":
        for i, item in enumerate(tasks, start=1):
            print(f"{i}. {item}")
    elif choose== "4":
        complete_task()
    elif choose== "5":
        print("Exit is in progress.")
        break
    else:
        print("You have entered an incorrect number!!")

