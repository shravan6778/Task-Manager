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
    
    @classmethod
    def from_dict(cls, data: dict):
        task=cls(data["id"], data["title"], data["description"])
        task.is_completed=True
        task.created_at=data["created_at"]
        return task
    