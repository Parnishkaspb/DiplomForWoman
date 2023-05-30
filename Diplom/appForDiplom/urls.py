from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('practice/<int:id>/', views.practice),
    path('laba', views.laba),
    path('lection/<int:id>/', views.lection, name='lection'),
    path('createVideo', views.createVideo),
    path('createTask', views.createTask),
    path('createPractice', views.createPractice),
]
