from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('practice/<int:id>/', views.practice),
    path('test_check/<int:id>/', views.test_check),
    path('test/<int:id>/', views.test, name='test'),
    path('lection/<int:id>/', views.lection, name='lection'),
    path('createVideo', views.createVideo),
    path('createTask', views.createTask),
    path('createPractice', views.createPractice),
]
