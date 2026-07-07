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