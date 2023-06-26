from django.db import models
from django.contrib.auth.models import User
import uuid




# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, blank = True, null = True , on_delete= models.CASCADE)
    username = models.CharField(max_length=200, blank = True, null = True)
    e_mail = models.EmailField(blank = True, null = True)
    id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True, primary_key=True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username
    
    @property
    def counttask(self):
        task_no = self.task_set.all()
        incomplete_task = task_no.filter(complete = False).count()
        return incomplete_task
 


class Task(models.Model):
    profile = models.ForeignKey(Profile, blank = True, null = True, on_delete=models.CASCADE)
    name =  models.CharField(max_length= 150, blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    complete = models.BooleanField(default=False )
    created = models.TimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True, primary_key=True)

    def __str__(self):
        return self.name

