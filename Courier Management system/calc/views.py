from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template
from .models import Orders
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import UserRegisterForm

# Create your views here.
def home(response):
    return render(response, 'calc/home.html')
def about(request):
    context={
         'posts':Orders.objects.all()
        }
    return render(request, 'calc/about.html', context)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'calc/register.html', {'form':form})
def profile(request):
    return render(request, 'calc/profile.html')