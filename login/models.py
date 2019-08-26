from django.db import models
from django.contrib.auth.models import User

class infor(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    passwordkey = models.CharField(max_length = 10 , null = True)
    paypal_url = models.URLField(null = True)

    def __str__(self):
        return (self.name)