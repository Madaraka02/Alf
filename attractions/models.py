from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# from django_autoslug.fields import AutoSlugField

# Create your models here.
class Park(models.Model):
    name = models.CharField(max_length=300, unique=True, blank=False)
    image = models.FileField(upload_to='parks')
    slug = AutoSlugField(populate_from='name', null=True)

    def __str__(self):
        return self.name


class Attraction(models.Model):
    name = models.CharField(max_length=300, blank=False)
    image = models.FileField(upload_to='attimages')
    description = models.TextField()
    slug = AutoSlugField(populate_from='name', null=True)
    likes=models.ManyToManyField(User, related_name='likess', blank=True)


    def __str__(self):
        return self.name
    
class AttractionImages(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    image = models.FileField(upload_to='attimagesm', blank=True, null=True)

    def __str__(self):
        return self.attraction.name

class ParkImages(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE) 
    image = models.FileField(upload_to='parksm', blank=True, null=True)   

    def __str__(self):
        return self.park.name


class Book(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    number_of_people = models.CharField(max_length=100, blank=True,null=True,default=1)
    date = models.DateField(null=True, blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=300,null=True,blank=False)
    email=models.CharField(max_length=300,null=True,blank=False)
    message=models.TextField()


class VisitAttraction(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    preferred_location = models.ForeignKey(Park, on_delete=models.CASCADE) 

    number_of_people = models.CharField(max_length=100, blank=True,null=True,default=1)
    date = models.DateField(null=True, blank=True)
    
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    message=models.CharField(max_length=300, blank=True,null=True)