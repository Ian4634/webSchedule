from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name = 'main'),
    path('addLesson/', views.add_lesson, name = 'add_lesson'),
    path('process/', views.process, name = 'process')
]