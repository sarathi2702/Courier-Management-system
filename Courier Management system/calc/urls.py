from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDetailView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.home,name='home'),
    path('detail/<int:pk>/',OrderDetailView.as_view(),name='detail'),
    path('create/',OrderCreateView.as_view(),name='create'),
    path('about/',OrderListView.as_view(),name='about'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('update/',views.update,name='update'),
    path('login/',auth_views.LoginView.as_view(template_name='calc/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='calc/logout.html'),name='logout')
]