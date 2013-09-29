# -*- coding: utf-8 -*-
import random
import datetime

from django.views import generic as cbv

from . import models


class BaseConnectorTemplateView(cbv.TemplateView):
    listen_actor_type = None
    actor_type = None

    def get_listen_actor_type(self):
        return self.listen_actor_type

    def get_actor_type(self):
        return self.actor_type

    def get_auth_code(self):
        raise NotImplemented

    def get_context_data(self, **kwargs):
        context = super(
            BaseConnectorTemplateView,
            self
        ).get_context_data(**kwargs)

        context.update({
            'actor_type': self.get_actor_type(),
            'auth_code': self.get_auth_code(),
            'listen_actor_type': self.get_listen_actor_type()
        })
        return context


class IndexGameView(BaseConnectorTemplateView):
    template_name = 'game/index.html'
    listen_actor_type = 'gamepad'
    actor_type = 'gamespace'

    def get_auth_code(self):
        """
        Generates authorization code
        """
        rand_str = str(random.randint(1, 255))
        return datetime.datetime.now().strftime("%d%m%Y%H%M%S") + rand_str


class GamePadView(BaseConnectorTemplateView):
    template_name = 'game/pad.html'
    listen_actor_type = 'gamespace'
    actor_type = 'gamepad'

    def get_auth_code(self):
        """
        Gets auth code from request url
        """
        return self.kwargs.get('auth_code', '')


class PlayedGameListView(cbv.ListView):
    model = models.Game
    template_name = 'game/game_list.html'

    paginate_by = 20
