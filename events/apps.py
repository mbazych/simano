from django.db import models

# Create your models here.

class Events(models.Model):
    # event title
    title = models.CharField(max_length=255, null=False)
    # name of author of event
    author = models.CharField(max_length=255, null=False)
    

    def __str__(self):
        return "{} - {}".format(self.title, self.author)