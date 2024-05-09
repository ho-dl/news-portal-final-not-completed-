from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class News(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.heading
    




class FavoriteNews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ManyToManyField(News)
