import sqlite3
import typer
import time
from rich import print
from datetime import date
from typing import List
import uuid
import os


class Task:
    """
    A Task Class is used to create a task object. It doesn't store task object on database. 
    """
    def __init__(self,task_id:str ,task:str, category:str , status:str= None, date_added:str= None, date_completed:str=None) -> None:
        self.task_id = task_id
        self.task = task
        self.category = category
        self.status = status if status is not None else "open"
        self.date_added = date_added if date_added is not None else date.today()
        self.date_completed = date_completed if date_completed is None else date.today()

class Model:
    """
    A Model class is used to create a model object. It stores task object on database. 
    """
    def __init__(self)->None:
            try:
                self.conn = sqlite3.connect("database.db", uri=True)
                self.cursor = self.conn.cursor()

                table_exists = self.cursor.execute("""
                            SELECT name FROM sqlite_master WHERE type='table' AND name='tasks' 
                               """).fetchone()
                
                if not table_exists:
                    self.cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS tasks(task_id varchar(500) primary key, task text, category varchar(300),status varchar(300) ,date_added text, date_completed text)
                                    """)
               
                
            except Exception as e:
                print(e)

    def insert_task(self, task:Task):
        """
        This function inserts a task object into the database.
        """
        with self.conn:
            self.cursor.execute("INSERT INTO tasks VALUES (?,?,?,?,?,?)",(task.task_id, task.task, task.category, task.status, task.date_added, task.date_completed))
            row = self.cursor.fetchone()
            return row

    def list_all_tasks(self)->List[Task]:
       """  
       This function lists all the tasks in the database.
       """
       self.cursor.execute("SELECT * FROM tasks")
       rows = self.cursor.fetchall()
       return rows
    
    def delete_task(self, id:str)->None:
        """
        This function deletes a task Object from the database
        """
        with self.conn:
            self.cursor.execute("DELETE FROM tasks WHERE task_id=?",[id])
            row = self.cursor.fetchone()

    def update_task(self , id:str, task:str=None , category:str = None, status:str = "open"):
        """
        This function updates a task Object from the database.
        """
        if task is not None:
            with self.conn:
                self.cursor.execute("UPDATE tasks SET task=? where task_id=?",[task,id])
        if category is not None:
            with self.conn:
                self.cursor.execute("UPDATE tasks SET category=? where task_id=?",[category, id])
        if status is not "open":
            with self.conn:
                self.cursor.execute("UPDATE tasks SET status=?, date_completed=? where task_id=?",[status,date.today() ,id])
        else:
            with self.conn:
                self.cursor.execute("UPDATE tasks SET status=?, date_added=?, date_completed=?  where task_id=?",[status,date.today(), None ,id])