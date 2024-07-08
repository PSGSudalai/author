from django.db import models
from django.contrib.auth.models import User
import os


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

