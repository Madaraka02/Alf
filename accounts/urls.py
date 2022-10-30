from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    path('profile/<str:id>/', update_profile, name='update_profile'),

]