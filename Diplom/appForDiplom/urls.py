from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('practice', views.practice),
    path('laba', views.laba),
    path('lection', views.lection),
    path('createVideo', views.createVideo),
    path('createTask', views.createTask),
]
