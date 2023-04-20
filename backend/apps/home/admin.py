from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import PreviewImage


class PreviewImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'get_html_image', 'time_create')

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=70")

    get_html_image.short_description = 'Image'


admin.site.register(PreviewImage, PreviewImageAdmin)
