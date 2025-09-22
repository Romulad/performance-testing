from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title
