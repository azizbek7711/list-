from django.db import models

# Create your models here.
class Category(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='category/')
    def __str__(self):
        return self.name

class Student(models.Model):
    objects = None
    category = models.ForeignKey( Category,on_delete=models.CASCADE )
    name = models.CharField(max_length=250)
    title = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE )
    name = models.CharField(max_length=299)
    bio = models.TextField()
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='order/',blank=True)
    video = models.FileField(upload_to='video/',blank=True )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

