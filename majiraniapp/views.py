
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *
from . models import *
# Create your views here.
@login_required(login_url="/accounts/login/")
def home (request):
    return render(request, 'home.html' )

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()           
    return render(request, "profile/view_profile.html", {"profile": profile, })

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')
    return render(request, 'profile/profile_form.html', {"form":form})

