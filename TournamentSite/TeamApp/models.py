from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=15)
    colours = models.CharField(max_length=15)

class Player(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age= models.IntegerField()
    team= models.ForeignKey(Team, on_delete=models.CASCADE)
    