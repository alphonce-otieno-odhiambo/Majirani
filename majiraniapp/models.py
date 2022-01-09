from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
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
    @receiver(post_save)
    def create_neighborhood(sender, instance, created, **kwargs):
        if created:
            Neighborhood.objects.create()
    @receiver(post_save, sender=User)
    def save_user_neigborhood(sender, instance, **kwargs):
        instance.neighborhood.save()

class Occupant(models.Model):
    name = models.CharField(max_length=50)
    occ_id = models.AutoField(primary_key=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neigborhood')
    email = models.EmailField()

    def _str_(self):
        return f'{self.name} neigborhood'
    @receiver(post_save, sender=User)
    def create_occupant(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(occupant=instance)
    @receiver(post_save, sender=User)
    def save_occupant(sender, instance, **kwargs):
        instance.occupant.save()
    @receiver(post_delete, sender=User)
    def delete_occupant(sender, instance, **kwargs):
        instance.occupant.delete()

class Business(models.Model):
    bizz_name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neigborhood')
    bizz_email = models.CharField()

    def save_business(self):
        self.save()

    def update_business(self):
        self.update()
    
    def delete_business(self):
        self.delete()

    def create_business(self):
        Business.objects.create(business = isinstance)

    def find_business(business_id):
        business_id.find_business()

    def __str__(self):
        return self.bizz_name
