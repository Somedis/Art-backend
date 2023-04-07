from django.contrib import admin

from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'time_create')


admin.site.register(Posts, PostsAdmin)
