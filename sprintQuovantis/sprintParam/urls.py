from django.urls import path
from . import views

urlpatterns = [
    path('sprint/', views.SprintQuo.as_view(), name='add-sprint'),
    path('param-sprint', views.ParameterOfSprint.as_view(), name='param-sprint'),
    path('sprint/<int:id>', views.SprintQuo.as_view(), name='sprint'),
]
