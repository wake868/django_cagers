from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    player_name = models.CharField(max_length=200)
    player_number = models.IntegerField
    player_team = models.CharField(max_length=200)
    player_picture = models.ImageField
