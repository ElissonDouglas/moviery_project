from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField('Movie_id',max_length=100)
    watched = models.BooleanField('Watched', default=False)
