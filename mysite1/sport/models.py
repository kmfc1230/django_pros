from django.db import models


# Create your models here.
class Ball(models.Model):
    type = models.CharField(max_length=64, default='ball')
    xz = models.IntegerField(default=1)
