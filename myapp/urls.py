from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.Home, name = 'home'),
    path('register/', views.UserRegister, name = 'register'),
    path('login/', views.UserLogin, name = 'login'),
    path('logout/', views.UserLogout, name='logout'),
    path('profile/', views.UserProfile, name='profile')

]
