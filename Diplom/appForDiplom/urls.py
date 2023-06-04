from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('practice/<int:id>/', practice),
    path('test_check/<int:id>/', test_check),
    path('test/<int:id>/', test, name='test'),
    path('lection/<int:id>/', lection, name='lection'),
    path('createVideo', createVideo),
    path('createTask', createTask),
    path('deleteTask', deleteTask),
    path('createPractice', createPractice),
    path('newTask', newTask),
    
]
