from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from textblob import TextBlob
from django.urls import reverse

def valcalc(s):
    value = TextBlob(s).sentiment
    return list(value)[0]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('blog-home')




