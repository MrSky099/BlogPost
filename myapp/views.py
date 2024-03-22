from django.shortcuts import render, redirect
from myapp.models import User
from myapp.forms import UserForm , LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Home(request):
    return render(request, 'index.html')

def UserRegistration(request):
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            email = form.cleaned_data['email']
            Phone_Number = form.cleaned_data['Phone_Number']
            if password != password2:
                return redirect('/register', {'msg': 'password mismatch'})
            if User.objects.filter(Username=Username).exists():
                return render(request, 'register.html', {'form': form, 'msg': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'form': form, 'msg': 'Email already exists'})
            elif User.objects.filter(Phone_Number = Phone_Number).exists():
                return render(request, 'register.html', {'form': form, 'msg': 'Mobile number already registered'})
            form.save()
            return redirect('/home')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def UserLogin(request):
    if request.method == 'POST':
        form = LoginForm()
        print(form)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            password = form.cleaned_data.get('password')
            print(Username)
            user = authenticate(request, Username=Username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    else:
        form = LoginForm()
    return render(request, 'loginpage.html', {'form':form})
        