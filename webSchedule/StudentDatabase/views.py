from django.shortcuts import render, redirect
from .models import Student
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'StudentDatabase.html')

def addStudent(request):
    return render(request, 'add_studentData.html')
def process(request):
    name = request.POST['student_name']
    shoe = request.POST['shoe']
    board = request.POST['board']
    stance = request.POST['stance']
    bindingSize = request.POST['bindingSize']
    Student.objects.create(
        name = name,
        shoe = shoe,
        board = board,
        stance = stance,
        bindingSize = bindingSize
    ).save()
    return HttpResponseRedirect(reverse('home'))