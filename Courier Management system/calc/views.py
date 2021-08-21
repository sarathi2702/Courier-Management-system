from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template
from .models import Orders
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import UserRegisterForm, UserUpdateForm
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(response):
    return render(response, 'calc/home.html')

class OrderListView(ListView):
    model = Orders
    template_name='calc/about.html'
    context_object_name = 'posts'
    ordering = ['-order_date']

class OrderDetailView(DetailView):
    model = Orders

class OrderCreateView(LoginRequiredMixin,CreateView):
    model = Orders
    fields=['weight','from_place','destination']
    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context ={
        'u_form':u_form
    }
    return render(request, 'calc/profile.html', context)

def update(response):
    return render(response, 'calc/profile_update.html')