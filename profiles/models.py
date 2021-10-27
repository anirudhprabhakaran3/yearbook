from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=False)
    branch = models.CharField(max_length=3, default="ECE", blank=False, null=False)

    def __str__(self):
        return self.name
