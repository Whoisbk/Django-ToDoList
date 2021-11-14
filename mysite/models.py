from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE,null =True,blank=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text