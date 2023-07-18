from django.db import models
from django.contrib.auth.models import User


class user(models.Model):
    username = models.CharField('Название', max_length=50)
    password = models.CharField('Анонс', max_length=250)
    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.username
