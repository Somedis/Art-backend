from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='Art-images/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cats_slug': self.slug})

    def get_cat_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title', ]
