from django.urls import path
from . import views

urlpatterns = [
    path('sprint/', views.SprintQuo.as_view(), name='sprint'),
    path('param-sprint', views.ParameterOfSprint.as_view(), name='param-sprint'),
]
