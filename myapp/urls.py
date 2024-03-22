from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.Home, name = 'home'),
    path('register/', views.UserRegistration, name = 'register'),
    path('login/', views.UserLogin, name = 'login')
]
