from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserBlogs

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('-date_joined',)

class UserBlogsAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'Title', 'BlogImages', 'BlogContent', 'author', 'created_at')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserBlogs, UserBlogsAdmin)