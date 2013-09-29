# -*- coding: utf-8 -*-
from django import dispatch

frontend_send = dispatch.Signal(providing_args=['user', 'data'])
