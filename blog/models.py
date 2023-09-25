from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.


class Post(models.Model):
    postName = models.CharField(max_length=255)
    postDescript = models.CharField(max_length=255)
    postCreator  = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    dateCreate = models.DateTimeField(default=timezone.now())
