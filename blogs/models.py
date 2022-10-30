from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=400, null=True,blank=True)
    snippet=models.CharField(max_length=600, null=True,blank=True)
    # description=models.TextField(null=True, blank=True)
    image=models.FileField(upload_to='blogs', null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes=models.ManyToManyField(User, related_name='dislikes', blank=True)
    approved=models.BooleanField(default=False)


class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)  
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment=models.TextField(null=True, blank=True)
    # created_on = models.DateTimeField(auto_now_add=True, null=True)




