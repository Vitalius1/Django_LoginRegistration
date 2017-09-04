from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, "log_reg/index.html")

def back(request):
    return redirect('/')

def register(request):
    result = User.objects.validate_and_register(request.POST)
    if result[0] == False:
        context = {
            'result':result[1]
        }
        return render(request, "log_reg/index.html", context)
    if result[0] == True:
        context = {
            'result': result[1],
            'action': "registered"
        }
        return render(request, "log_reg/success.html", context)

def login(request):
    result = User.objects.validate_and_login(request.POST)
    if result[0] == False:
        context = {
            'result':result[1]
        }
        return render(request, "log_reg/index.html", context)
    if result[0] == True:
        context = {
            'result': result[1][0].first_name,
            'action': "logged"
        }
        return render(request, "log_reg/success.html", context)
    
# Create your views here.
