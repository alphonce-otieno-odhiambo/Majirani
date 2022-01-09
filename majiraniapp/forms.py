from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio","location", "profile_picture")

class NeigborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ("neigname","neigcount", "neiglocation")
