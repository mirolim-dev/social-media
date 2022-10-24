from enum import auto
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = RichTextUploadingField()
    viewers = models.ManyToManyField(User, related_name='viewers', blank=True)
    likers = models.ManyToManyField(User, related_name='likers', blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    def number_ob_views(self):
        return self.viewers.count()
    
    def number_ob_likes(self):
        return self.likers.count()

    def get_all_comments(self):
        return self.comment_set.all()

    def number_of_comments(self):
        return self.get_all_comments().count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)

    writed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"auther: {self.author}|post: {self.post}"

    def get_all_rewrited_comments(self):
        r_comments = self.rewritedcomment_set.all()
        return r_comments
    
    def number_of_rewrited_comments(self):
        return self.get_all_rewrited_comments().count()


class RewritedComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)

    writed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"auther: {self.author}| post: {self.post}"
