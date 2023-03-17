from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.task
    
    def to_dict(self):
        returned = {
            'task': self.task,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return returned