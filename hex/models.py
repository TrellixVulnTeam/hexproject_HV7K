from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

PREFERENCES = (('KD', 'Children'),
               ('EL', 'Elderly'),
               ('HO', 'Homeless'),
               ('TE', 'Tech'),
               ('MU', 'Music'),
               ('EV', 'Environmental'),
               ('ED', 'Educational'),
               )

class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
	#telephone
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
	#preferences = MultiSelectField(choices=PREFERENCES, max_choices=7, max_length=14)

class Benefactor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
	#telephone

class Events(models.Model):
	date = models.DateTimeField()
	#x_coordinate = models.DoubleField(null=True) - wrong type
	#y_coordinate = models.DoubleField(null=True)
	title = models.CharField(max_length = 50)
	description = models.TextField()
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
