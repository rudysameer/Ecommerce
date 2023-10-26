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


STOCK = (('In Stock','in Stock'),('Out of Stock','ut of Stock'))
LABELS = (('default','default'),('hot','hot'),('new','New'),('sale','sale'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    slug = models.TextField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100, choices=STOCK)
    labels = models.CharField(max_length=100,choices=LABELS)

    def __str__(self):
        return self.name


class ProductReviews(models.Model):
    username = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 500)
    date = models.DateField(auto_now_add = True)
    star = models.IntegerField()
    review = models.TextField()
    slug = models.SlugField(max_length = 200)
    image = models.ImageField(upload_to= 'media',null = 'True')

    def __str__(self):
        return self.username

class Cart(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    slug = models.SlugField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checkout = models.BooleanField(default = False)

    def __str__(self):
        return self.name


class Checkout(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    Address = models.CharField(max_length=100)
    phone = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    shipfirstname = models.CharField(max_length=100)
    shiplastname = models.CharField(max_length=100)
    shipEmail = models.EmailField(max_length=200)
    shipAddress = models.CharField(max_length=100)
    shipphone = models.IntegerField()
    shipcountry = models.CharField(max_length=100)
    shipcity = models.CharField(max_length=100)
    shipstate = models.CharField(max_length=100)
    shipzipcode = models.IntegerField()



    def __str__(self):
        return self.firstname

