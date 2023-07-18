from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    current_user = models.ForeignKey(User, on_delete=models.PROTECT)


    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'