from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Home(request):
    return render(request, 'index.html')

def UserRegister(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
         
        user = User.objects.filter(username=username, email=email)
         
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email
        )
         
        user.set_password(password)
        if password == password:
            user.save()
    
            messages.info(request, "Account created Successfully!")
            return redirect('/home/')
     
    return render(request, 'register.html')

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    return render(request, 'loginpage.html')