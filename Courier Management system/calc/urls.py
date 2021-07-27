from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='calc/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='calc/logout.html'),name='logout')
]