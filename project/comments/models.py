# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('blogs.Post')
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
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return u'{}: {}'.format(self.post.title, self.title)

    class Meta:
        ordering = '-id',
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
