# -*- coding: utf-8 -*-
from gevent import monkey

import os
import sys

import django.core.handlers.wsgi
from socketio.server import SocketIOServer

from runninggame import settings

monkey.patch_all()

os.environ['DJANGO_SETTINGS_MODULE'] = 'runninggame.settings'
application = django.core.handlers.wsgi.WSGIHandler()

sys.path.insert(0, settings.PROJECT_ROOT)

PORT = 8585

if __name__ == '__main__':
    print 'Listening *:%s' % PORT
    SocketIOServer(
        ('', PORT),
        application,
        resource="socket.io"
    ).serve_forever()
