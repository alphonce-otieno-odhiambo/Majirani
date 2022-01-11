
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    
    #path('profile_create/', views.profile_create, name = 'profile_create'),
    path('profile/', views.profile, name='view_profile'),
    path('update_profile/<int:id>', views.update_profile, name = 'update_profile'),
    path('neigborhoods/<int:id>', views.neigborhoods, name = 'neigborhood'),
    path('occupants/', views.occupants, name='occupants'),
    path('resident/', views.resident, name='resident'),
    path('business/', views.business, name='business'),
    path('post/', views.post, name='post'),
    path('post_view/', views.post_view, name='post_view'),
]
