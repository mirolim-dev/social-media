from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=60)
    shortage = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    


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
    avatar = models.ImageField(upload_to='profile', blank=True, null=True)
    alternative_email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.CharField(max_length=5, choices=AGE_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=25, choices=COUNTRY_CHOICES, blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True)
    followings = models.ManyToManyField('self', blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    def __str__(self) -> str:
        return super().username

    
    @admin.display(description='followers')
    def number_of_followers(self):
        return f'{self.followers.count()}'

    @admin.display(description='followings')
    def number_of_followings(self):
        return f'{self.followings.count()}'