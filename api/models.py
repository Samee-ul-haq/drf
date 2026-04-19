import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
 
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Team(models.Model):
    team_name=models.CharField(max_length=200)
    team_id=models.UUIDField(primary_key=True,default=uuid.uuid4)

class Student(models.Model):
    enrollment_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="students")
