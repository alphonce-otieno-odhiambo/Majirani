from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, related
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from cloudinary.models import CloudinaryField
from django.utils import timezone
import sys
sys.setrecursionlimit(2000)



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
    neiglocation = models.CharField(max_length=150 )
    neigcount = models.IntegerField(null= True ) 
    
    def save_neighborhood(self):
        self.save()

    def update__neighborhood(self):
        self.update()
    
    def delete__neighborhood(self):
        self.delete()

    
    
    def _str_(self):
        return f'{self.neigname}'
    

class Occupant(models.Model):
    name = models.CharField(max_length=50)
    occ_id = models.AutoField(primary_key=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neigborhood')
    email = models.EmailField( null=True )

    def save_occupant(self):
        self.save()

    def update__occupant(self):
        self.update()
    
    def delete__occupant(self):
        self.delete()

    
    
    def _str_(self):
        return f'{self.name}'
    


    

class Business(models.Model):
    bizz_name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
    bizz_id = models.AutoField(primary_key=True)
    bizz_neighborhood = models.ManyToManyField(Neighborhood)
    bizz_email = models.CharField(max_length=50)

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

class Post(models.Model):
    title= models.CharField(max_length=150)
    info = models.TextField(max_length=400)
    date_posted = models.DateTimeField(default=timezone.now)

    def save_post(self):
        self.save()

    def __str__(self):
        return self.title

