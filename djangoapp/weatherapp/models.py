from django.db import models

# Create your models here.
class Weather(models.Model):
    select = models.CharField(max_length=200)
    # image = models.ImageField()
    result = models.TextField()

#with evey new model 2 steps:
    #╰─ python3 manage.py makemigrations
    #╰─ python3 manage.py migrate

def __str__(self):
    return self.select