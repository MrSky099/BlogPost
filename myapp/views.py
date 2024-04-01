from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserBlogsForm
from django.contrib.auth.decorators import login_required
from .models import UserBlogs

def Home(request):
    return render(request, 'index.html')

@login_required
def UserProfile(request, username):
    user = request.user
    user = User.objects.get(username=username)
    print(user)
    blogs = UserBlogs.objects.filter(author=user)
    blog_count = UserBlogs.objects.filter(author=user).count()
    return render(request, 'profile.html', {'blogs':blogs ,'blog_count':blog_count , 'usern':user})

def ViewBlog(request, blog_id):
    blog = get_object_or_404(UserBlogs, id=blog_id)
    return render(request, 'blogview.html', {'blog':blog})

def UserRegister(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not (first_name and last_name and username and email and password and password2):
            messages.error(request, "Please fill in all fields.")
            return render(request, 'register.html')
        
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')
         
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Username or email already taken.")
            return render(request, 'register.html')
         
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email
        )
         
        user.set_password(password)
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

def UserLogout(request):
    #if request.method == 'POST':
    logout(request)
    return redirect('/home/')

@login_required
def UploadBlog(request):
    if request.method == 'POST':
        form = UserBlogsForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.info(request, "Upload Blog Successfully")
            return redirect('/uploadblog/')
        else:
            messages.info(request, "blog is not uploading")
            return redirect('/uploadblog/')
    else:
        form = UserBlogsForm()
    return render(request, 'uploadblog.html' , {'form': form})

