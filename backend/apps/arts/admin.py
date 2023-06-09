from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Arts


class ArtscCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'cat', 'get_html_image',
                    'time_create', 'is_publish')
    list_display_links = ('id', 'slug')
    prepopulated_fields = {'slug': ('title', )}

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=70")

    get_html_image.short_description = 'Image'


admin.site.register(Arts, ArtscCardsAdmin)
