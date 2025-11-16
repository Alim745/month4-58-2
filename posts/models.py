from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=1000, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.content}"

