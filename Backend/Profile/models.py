from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import requests

# Create your models here.

User = settings.AUTH_USER_MODEL


class ProfileModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    language = models.CharField(max_length=30, blank=True, default='en')

    def __str__(self):
        return self.user.get_username()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #domain = instance.email.split('@')[1]
        ProfileModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
