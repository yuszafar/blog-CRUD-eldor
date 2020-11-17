from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class Commentary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)




