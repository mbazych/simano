from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name
class Country(models.Model):
    country = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.country

class Category(models.Model):
    category = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.category

class City(models.Model):
    city = models.CharField(max_length=32, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

class Events(models.Model):

    title = models.CharField(max_length=255, null=False)

    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    Description = models.CharField(max_length=255, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=32, null=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    participants = models.ManyToManyField(User, related_name="participants")

    tags = models.ManyToManyField(Tags, related_name="tags")

    img = models.ImageField(upload_to='tmp/photos', blank=True)

    

    def __str__(self):
        return "{} - {}".format(self.title, self.author)

