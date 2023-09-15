from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=300,unique=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300,unique=True)
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=300,blank=True)
    url = models.URLField(max_length=600)
    rank = models.IntegerField()
    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=300,unique=True)
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=300,blank=True)
    rank = models.IntegerField()
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300,unique=True)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    slug = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')
    comment = models.TextField()
    post = models.CharField(max_length=100)
    star = models.IntegerField()
    def __str__(self):
        return self.name

class SiteInfo(models.Model):
    address = models.TextField()
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=15)
    twitter = models.URLField(max_length=500,blank=True)
    facebook = models.URLField(max_length=500,blank=True)
    linkden = models.URLField(max_length=500,blank=True)
    youtube = models.URLField(max_length=500,blank=True)

    def __str__(self):
        return self.address
