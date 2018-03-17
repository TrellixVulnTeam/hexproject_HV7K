from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

PREFERENCES = (('KD', 'Children'),
               ('EL', 'Elderly'),
               ('HO', 'Homeless'),
               ('TE', 'Tech'),
               ('MU', 'Music'),
               ('EV', 'Environmental'),
               ('ED', 'Educational'),
               )

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    preferences = MultiSelectField(choices=PREFERENCES,
                                 max_choices=7,
                                 max_length=14)

class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
