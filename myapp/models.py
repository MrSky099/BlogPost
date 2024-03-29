from django.db import models
from django.contrib.auth.models import User


class UserBlogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    BlogImages = models.ImageField(upload_to='images/')
    BlogContent = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'AllBlogs'