from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default="hello world")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"blog {self.title} created in {self.create_date}"

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"
