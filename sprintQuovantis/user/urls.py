from django.urls import path
from . import views

urlpatterns = [
    path('user-registration', views.UserRegistration.as_view(), name='user-registration'),
    path('login', views.Login.as_view(), name='login'),
]