from django.db import models
from django.contrib.auth.models import User

class follow(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null = True)
    follower = models.CharField(max_length = 50 , null = True)

class post(models.Model):
    posted_by = models.ForeignKey(User , on_delete=models.CASCADE , null = True)
    title = models.CharField(max_length = 40 , null = True)
    content = models.CharField(max_length = 1500 , null = True)
    cover_photo = models.ImageField()
    post_date = models.DateTimeField(auto_now_add=True)

class message(models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE , null = True)
    reciever = models.CharField(max_length = 50 , null = True)
    message = models.CharField(max_length = 500 , null = True)
    sentdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 10, null = True)