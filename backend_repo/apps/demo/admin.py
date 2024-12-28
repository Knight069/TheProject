from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("text", "timestamp", "user")
    search_fields = ("text", "user__username")
    list_filter = ("timestamp",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "timestamp", "post", "user")
    search_fields = ("text", "post__text", "user__username")
    list_filter = ("timestamp",)
