from django.urls import path
from moodbot import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.moodbot, name='moodbot'),
]
