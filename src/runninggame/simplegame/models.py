# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Game(models.Model):
    user = models.ForeignKey(User, related_name='game_set', null=True,
                             blank=True)
    score = models.IntegerField('Score')
    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        verbose_name = 'Played game'
        verbose_name_plural = 'Played games'
        ordering = ['-score', ]

    def __unicode__(self):
        if self.id:
            return u'%s: %s' % (
                (self.user or u'Anonymous'),
                unicode(self.created)
            )
        else:
            return u'new game'
