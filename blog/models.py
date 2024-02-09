from re import T
from django.db import models
# from django.contrib.auth.models import User  before
from accounts.models import User   # after


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default="hello world")
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f"blog {self.title} created in {self.create_date}"

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"



class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    reply = models.ForeignKey("self", related_name='comment_reply', on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.blog.title}"

    
    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "نظرات"
