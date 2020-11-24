from django.db import models
from django.contrib.auth.models import User

class Shopping_List(models.Model):
    bought = models.BooleanField(default=False) #pra fazer o inativo
    item = models.CharField(max_length=100)

def __str__(self):
    return self.item
