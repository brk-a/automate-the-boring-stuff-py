from django.db import models

class Todo(models.Model):
    """schema of a to-do item"""
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """__str__ method"""
        return self.title
