from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True,null=True)
    bio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='commented_posts', blank=True)

    def comment(self, user, text):
        Comment.objects.create(post=self, user=user, text=text)

    def like(self, user):
        self.likes.add(user)

    def unlike(self, user):
        self.likes.remove(user)
    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self}'

