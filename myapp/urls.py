from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.Home, name = 'home'),
    path('register/', views.UserRegister, name = 'register'),
    path('login/', views.UserLogin, name = 'login'),
    path('logout/', views.UserLogout, name='logout'),
    path('<str:username>/', views.UserProfile, name='profile'),
    path('uploadblog/', views.UploadBlog, name='uploadblog'),
    path('viewblog/<int:blog_id>/', views.ViewBlog, name='viewblog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)