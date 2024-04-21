from django.db import models


class showtimes(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    max_people = models.IntegerField()
    participants = models.IntegerField(blank=True, null=True)
