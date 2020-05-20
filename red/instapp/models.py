from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_info(models.Model):


    username = models.CharField(max_length=264)
    password = models.CharField(max_length=264)

    def __str__(self):
        return self.username
