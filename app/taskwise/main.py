import typer
from rich import print
from rich.progress import track
from questionary import Choice, Style, select
import time
import os
from taskwise.functions import display_all_tasks , update_task, insert_new_task , delete_task, loader


def greet():
    """
    This function greets users...
    """
    time.sleep(0.1)
    print("[red]Welcome to TaskWise!")

    for value in track(range(100), description="Loading..."):
        time.sleep(0.02)
    

def menu():
    """
    This function displays menu
    """
    os.system("clear")

    custom_style = Style([
        ("display", "fg:#f44336 bold"),
        ("insert", "fg:#673ab7 bold"),
        ("update", "fg:#cc5454 bold"),
        ("delete", "fg:#f5b705 italic"),
        ("exit", "fg:#6bf716 italic"),
    ])
    choices = [
                Choice(title=[("class:display", "Display all Tasks")], value="display"),
               Choice(title=[("class:insert", "Insert New Task")], value="insert"),
               Choice(title=[("class:update", "Update Task")], value="update"),
               Choice(title=[("class:delete", "Delete Task")], value="delete"),
               Choice(title=[("class:exit", "Exit")], value="exit"),
               ]
    answer = select(
    "What do you want to do?",
    choices=choices,
    style=custom_style).ask()    
    
    match answer:
        case "display":
            display_all_tasks()
        case "insert":
            insert_new_task()
        case "update":
            update_task()
        case "delete":
            delete_task()
        case "exit":
            loader("Exiting...")
            exit()

def main():
    greet()
    
    while True:
        menu()
        time.sleep(0.5)

if __name__ == "__main__":
    typer.run(main)