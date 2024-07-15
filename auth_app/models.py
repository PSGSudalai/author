from django import forms
from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    # tags = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-date_created',)

    def __str__(self):
       return self.title
    


class comments(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    blog=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    text=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    lastupdated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('lastupdated','-created')

    def __str__(self):
        return self.text

    
class Tags:
    tags = models.CharField(max_length=50)
    
    class Meta:
        ordering =('tags') 
        
    def __str__(self):
        return self.tags
    


