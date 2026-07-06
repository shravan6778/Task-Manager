from datetime import datetime

class Task:
    def __init__(self, task_id: int, title: str, description: str = ""):
        self.id = task_id
        self.title = title
        self.description = description
        self.is_completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        
    
    def mark_complete(self):
        self.is_completed = True
        
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
            "created_at": self.created_at
        }