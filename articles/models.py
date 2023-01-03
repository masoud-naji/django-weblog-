from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    thumb = models.ImageField(default='default.png', blank=True)
    # add in author later
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    # add this method
    def __str__(self):
        return self.title

    # add this method
    def snippet(self):
        if(len(self.body) > 50):
            return self.body[:50] + '...'
        else:
            return self.body