from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=256)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-time_create', ]
