# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=u'Название'
    )

    def __str__(self):
        return '#' + self.title

    class Meta:
        ordering = 'title',
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    categories = models.ManyToManyField(Category, related_name='posts')
    title = models.CharField(
        max_length=255,
        verbose_name=u'Заголовок'
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=u'Дата последнего изменения'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = '-id',
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
