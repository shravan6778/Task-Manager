import json 
import os
from typing import List
from tabulate import tabulate
from src.task import Task

class TaskManager:
    def __init__(self, storage_file: str = 'tasks.json'):
        self.storage_file=storage_file
        self.tasks: List[Task] = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        if not os.path.exists(self.storage_file):
            return []
        else:
            try:
                with open(self.storage_file, 'r') as f:
                    data=json.load(f)
                    return [Task.from_dict(t) for t in data]
            except json.JSONDecodeError:
                return []
            
    def save_tasks(self):
        with open(self.storage_file, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)
            
    def add_task(self, title: str, description: str = ""):
        next_id = max([t.id for t in self.tasks], default=0) + 1
        new_task = Task(next_id, title, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully (ID: {next_id}).")
        
    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                self.save_tasks()
                print(f"Task {task_id} marked as complete!")
                return
        print(f"Error: Task with ID {task_id} not found.")