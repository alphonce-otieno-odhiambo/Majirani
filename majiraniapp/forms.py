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
        fields = ("neigname", "neiglocation")

class OccupantForm(forms.ModelForm):
    class Meta:
        model = Occupant
        fields = ("name","neighborhood")
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ("bizz_name","bizz_neighborhood", "bizz_email")