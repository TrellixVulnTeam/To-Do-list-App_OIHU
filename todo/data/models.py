from django.db import models
from datetime import datetime, timedelta


class User(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=200)
    Password = models.Charfield(max_length=200)
    join_date = models.DateTimeField(editable=False, default=datetime.now())

    class ToDo(models.Model):
        todo_job = models.TextField()
        user = models.ForeignKey('User')
        created_date = models.DateTimeField(editable=False,default=datetime.now())
