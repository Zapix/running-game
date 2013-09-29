# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField('Username', max_length=255, unique=True)

    USERNAME_FIELD = 'username'
    objects = auth_models.UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        if self.id:
            return self.username
        else:
            return u'New user'

    @property
    def is_staff(self):
        """
        Only superusers is staff
        """
        return self.is_superuser

    @property
    def top_game_played_by_score(self):
        return self.game_set.all()[:10]
