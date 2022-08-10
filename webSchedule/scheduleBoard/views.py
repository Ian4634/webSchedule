from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request, 'home.html')

def add_lesson(request):
    return render(request, 'add_lesson.html')

def process(request):
    if request.method == 'POST':
        time = request.POST['time'], request.POST['amount']
        print(time)
    return redirect('http://localhost:8000/scheduleBoard/')