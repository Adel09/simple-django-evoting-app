from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Candidate(models.Model):
    POSITIONS = (
    ("President", "President"),
    ("Vice President", "Vice President"),
    ("General Secretary", "General Secretary"),
    ("Assistant General Secretary", "Assistant General Secretary"),
    ("Financial Secretary", "Financial Secretary"),
    ("Welfare Director", "Welfare Director"),
    ("Hardware Director", "Hardware Director"),
    ("Software Director", "Software Director"),
    ("Sports Director", "Sports Director"),
    ("Social Director", "Social Director"),
    ("Public Relations Officer", "Public Relations Officer"),
    #("2", "2"),
    )

    name = models.CharField(max_length=200, blank=True)
    level = models.CharField(max_length=70, blank=True)
    position = models.CharField(max_length=80, choices=POSITIONS, blank=True)
    votes = models.IntegerField(default=0)
    image = models.FileField(upload_to="media/images/candidates", null=True)
