from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    COUNTRY_CHOICES = (
        ('Uzbekistan', 'Uzbekistan'),
        ("USA", "USA"),
        ("Russia", "Russia"),
        ('Turkey', 'Turkey'),
        ('Other', 'Other'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    AGE_CHOICES = (
        ('14-17', '14-17'),
        ('18-27', '18-27'),
        ('28-45', '28-45'),
        ('46-60', '46-60'),
        ('61-', '61-'),
    )
    alternative_email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.CharField(max_length=5, choices=AGE_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=25, choices=COUNTRY_CHOICES, blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True)
    followings = models.ManyToManyField('self', blank=True)

    def __str__(self) -> str:
        return super().username