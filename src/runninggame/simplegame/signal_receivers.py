# -*- coding: utf-8 -*-
from django import dispatch

from .models import Game
from websocket import signals


@dispatch.receiver(signals.frontend_send)
def frontend_send_handler(sender, user, data, **kwargs):
    print "game finished handler"
    event = data.get('event')
    if event == 'game_finished':
        game = Game(
            user=user if not user.is_anonymous() else None,
            score=data['score']
        )
        game.save()
