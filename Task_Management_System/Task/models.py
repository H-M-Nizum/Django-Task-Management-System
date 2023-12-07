from django.db import models
from Category.models import CategoryModel

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField()
    assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(CategoryModel)
    
    def __str__(self):
        return self.taskTitle 