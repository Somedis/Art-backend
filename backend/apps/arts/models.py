from django.db import models
from django.urls import reverse

from category.models import Category


class Arts(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='Art-images/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    is_publish = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT,
                            null=True, verbose_name='Category')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('art', kwargs={'art_slug': self.slug})

    class Meta:
        verbose_name = 'Art'
        verbose_name_plural = 'Arts'
        ordering = ['-time_create', ]
