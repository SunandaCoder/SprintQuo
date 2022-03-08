from django.urls import path
from . import views

urlpatterns = [
    path('sprint', views.Sprint.as_view(), name='sprint'),
    path('param_sprint', views.ParameterOfSprint.as_view(), name='param_sprint'),
]