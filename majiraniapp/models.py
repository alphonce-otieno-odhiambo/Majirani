from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    bio = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
    profile_picture = CloudinaryField('image')

    def _str_(self):
        return f'{self.user.username} profile'
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Neighborhood (models.Model):
    neigname = models.CharField(max_length=150)
    neiglocation = models.CharField(max_length=150)
    neigcount = models.IntegerField()

    def _str_(self):
        return f'{self.neigname} '
    @receiver(post_save, sender=User)
    def create_neighborhood(sender, instance, created, **kwargs):
        if created:
            Neighborhood.objects.create()
    @receiver(post_save, sender=User)
    def save_user_pneigborhood(sender, instance, **kwargs):
        instance.neighborhood.save()
