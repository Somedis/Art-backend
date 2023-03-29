from django.db import models


class PreviewImage(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    image = models.ImageField(upload_to="preview/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
