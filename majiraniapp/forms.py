from django.db.models import fields
from django import forms
from . models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio","location","contact", "profile_picture")

class NeigborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ("neigname", "neiglocation" ,"neigcount")

class OccupantForm(forms.ModelForm):
    class Meta:
        model = Occupant
        fields = ("name", "occ_id", "neighborhood" , "email")
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ("bizz_name","bizz_neighborhood", "bizz_email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","info", "date_posted")