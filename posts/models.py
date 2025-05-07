from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/{1}.enc'.format(instance.author.id, filename)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    caption = models.CharField(max_length=200)
    img = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)