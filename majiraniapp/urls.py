
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    
    #path('profile_create/', views.profile_create, name = 'profile_create'),
    path('profile/', views.profile, name='view_profile'),
    path('update_profile/<int:id>', views.update_profile, name = 'update_profile'),
]
