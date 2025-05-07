from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'user']  

    def __str__(self):
        return f"{self.user.username} liked {self.post.caption}"
