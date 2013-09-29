# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField('Username', max_length=255, unique=True)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        if self.id:
            return self.username
        else:
            return u'New user'
