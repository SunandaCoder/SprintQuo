from django.urls import path
from . import views

urlpatterns = [
    path('sprint', views.Sprint.as_view(), name='sprint'),
    path('param_sprint', views.ParameterOfSprint.as_view(), name='param_sprint'),
    path('user_vote', views.UserVote.as_view(), name='user_vote'),
    path('result', views.Result.as_view(), name='result'),
]