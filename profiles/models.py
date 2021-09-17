from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    profile = models.ForeignKey('profiles.Profile',related_name='comments',on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    report_comment = models.BooleanField(default=False)

    def report(self):
        self.report_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('profile_detail')

    def __str__(self):
        return self.text
