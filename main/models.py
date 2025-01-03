from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
class Document(models.Model): 
    title = models.CharField(max_length=100) 
    uploaded_file = models.FileField(upload_to='documents/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)