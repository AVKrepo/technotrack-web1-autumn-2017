# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    company_name = models.CharField(max_length=255, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = '-id',
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
