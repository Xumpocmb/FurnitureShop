from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', verbose_name='Изображение', null=True, blank=True)
    phone = models.CharField(max_length=9, verbose_name='Телефон', null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username

    def display_id(self):
        return f'ID: {self.id:05}'
