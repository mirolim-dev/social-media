from django.contrib import admin

from .models import Post, Comment, RewritedComment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'uploaded_at', 'updated_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'writed_at', 'updated_at']


class RewritedCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'comment', 'post', 'writed_at', 'updated_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(RewritedComment, RewritedCommentAdmin)