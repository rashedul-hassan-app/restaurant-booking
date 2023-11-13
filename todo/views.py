from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return render(request, 'todo_list.html')


def index(request):
    return HttpResponse("This is the HOME PAGE")
