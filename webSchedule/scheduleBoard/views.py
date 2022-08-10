from django.shortcuts import render, redirect
from .models import Lesson
# Create your views here.

def main(request):
    return render(request, 'home.html')

def add_lesson(request):
    return render(request, 'add_lesson.html')

def process(request):
    if request.method == 'POST':
        time = request.POST['time']
        notes = request.POST['notes']
        instructors = request.POST['instructors']
        Lesson.objects.create(time = time, notes = notes, instructors = instructors).save()
       
    return redirect('http://localhost:8000/scheduleBoard/')