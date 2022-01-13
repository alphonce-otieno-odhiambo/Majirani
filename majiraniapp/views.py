
from django.db.models import query
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
    else:
        form = ProfileForm()
    return render(request, 'profile/profile_form.html', {"form":form})

def neigborhoods(request , id):
    majirani = Neighborhood.objects.all()
    neigborhood = Neighborhood.objects.filter(id=id)
    return render(request, 'neighborhood/majirani.html', {"neigborhood":neigborhood, "majirani":majirani})

def occupants(request):
    
    ocupant = Occupant.objects.all()
    form = OccupantForm()
    if request.method == "POST or None":
            form = OccupantForm(request.POST or None,instance=ocupant)
            if form.is_valid():
                ocupant = form.save(commit=False)
                ocupant.save()
                return redirect('residents')
    else:
        form = OccupantForm()
    return render(request, 'neighborhood/occupants.html',{"form":form})

def resident(request):
    ocupant = Occupant.objects.all()
    return render (request, 'neighborhood/residents.html', {"ocupant":ocupant})

def business(request):
    bizz= Business.objects.all()
    return render(request, 'neighborhood/business.html', {"bizz":bizz})

def post(request):    
    posted = Post.objects.all()
    form = OccupantForm()
    if request.method == "POST or None":
            form = PostForm(request.POST or None,instance=posted)
            if form.is_valid():
                ocupant = form.save(commit=False)
                ocupant.save()
                return redirect('post_view')
    else:
        form = PostForm()
    return render(request, 'neighborhood/post.html',{"form":form})

def post_view(request):
    posted = Post.objects.all()
    return render(request, 'neighborhood/post_view.html', {"posted":posted})

@login_required(login_url="/accounts/login/")
def search_business(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_bizz = Business.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"
        return render(request, "search.html", {"message": message, "bizz": searched_bizz})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})