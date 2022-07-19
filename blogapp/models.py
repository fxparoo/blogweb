from django.db import models


class BlogPost(models.Model):
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.created_date.strftime('%H: %M: %S')}"

    class Meta:
        ordering = ['created_date']
