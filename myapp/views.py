from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "myapp/home.html", context = {"context_var" : "context_value"})

def contact(request):
    return HttpResponse("This is my contact page.")

def about(request):
    return HttpResponse("This is my about page.")

def login(request):
    if request.method == 'POST':
        return render(request, "myapp/success.html")
    else:
        return render(request, "myapp/login.html")

def success(request):
    return render(request, "myapp/success.html")