from django.db import models


# Create your models here.


# 短评
class DBShorts(models.Model):
    # id 自动创建
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    info = models.CharField(max_length=500)
    star = models.CharField(max_length=5)
