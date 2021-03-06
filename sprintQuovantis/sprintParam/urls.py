from django.urls import path
from . import views

urlpatterns = [
    path('sprint/', views.SprintQuo.as_view(), name='add-sprint'),
    path('sprint/<int:id>', views.SprintQuo.as_view(), name='sprint'),
    path('voting-param', views.VotingParameter.as_view(), name='voting-param')
]
