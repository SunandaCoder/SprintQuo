from django.urls import path
from . import views

urlpatterns = [
    path('user_registration', views.UserRegistration.as_view(), name='user_registration'),
]