from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name = 'home',),
    path('addData/', views.addStudent, name = 'addData'),
    path('process/', views.process, name = 'process')
]