from django.urls import path
from . import views

urlpatterns = [
    path('sprint/', views.SprintQuo.as_view(), name='add-sprint'),
    path('sprint/<int:id>', views.SprintQuo.as_view(), name='sprint'),
    path('voting-param', views.VotingParameter.as_view(), name='voting-param'),
    path('sprint/<int:id>/votes', views.UserVote.as_view(), name='user-votes-update'),
    path('sprint/<int:id>/votes/<int:vote_for>', views.UserVote.as_view(), name='user-votes'),
    path('sprint/<int:id>/result', views.Result.as_view(), name='sprint'),
]




