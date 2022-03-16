from django.urls import path
from . import views

urlpatterns = [
    path('sprint', views.Sprint.as_view(), name='sprint'),
    path('param-sprint', views.ParameterOfSprint.as_view(), name='param-sprint'),
    path('sprint/<int:sprint_id>/votes', views.UserVote.as_view(), name='user-votes-update'),
    path('sprint/<int:sprint_id>/votes/<int:user_id>', views.UserVote.as_view(), name='user-votes'),
    path('sprint/<int:sprint_id>/result', views.Result.as_view(), name='sprint'),
]