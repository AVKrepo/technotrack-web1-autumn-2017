from django.contrib import admin
from .models import Post, Category


admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author'
