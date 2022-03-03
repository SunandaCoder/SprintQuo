from django.urls import path
from . import views

urlpatterns = [
    path('user_registration', views.UserRegistration.as_view(), name='user_registration'),
    path('user_login', views.Login.as_view(), name='user_login'),
]