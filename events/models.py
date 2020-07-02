from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name

class Events(models.Model):

    title = models.CharField(max_length=255, null=False)

    author = models.ForeignKey(User, on_delete = models.CASCADE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    participants = models.ManyToManyField(User, related_name="participants")

    tags = models.ManyToManyField(Tags, related_name="tags")
    category = models.ManyToManyField(Categories, related_name="category")

    img = models.ImageField(upload_to='../../static/photos')

    

    def __str__(self):
        return "{} - {}".format(self.title, self.author)

