from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'title', 'likes')
    list_display_links = ('name', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
