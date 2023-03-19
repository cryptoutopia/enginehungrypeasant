from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)


class DailyMenu(models.Model):
    DAYS = [
        ('MON', 'Monday'),
        ('TUES', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THURS', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    ]

    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    day = models.CharField(max_length=12, choices=DAYS)
    meal = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    TYPES = [
        ('P', 'Phone'),
        ('E', 'Email'),
        ('W', 'Web'),
        ('O', 'Other')
    ]

    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TYPES)
    value = models.CharField(max_length=256)