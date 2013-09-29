# Create your views here.
import json

from django import http
from django.conf import settings

import gevent
from gevent_zeromq import zmq
from socketio import socketio_manage
from socketio.namespace import BaseNamespace

from . import signals

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind('tcp://127.0.0.1:%d' % settings.ZMQ_PORT)


def send_message(socket, auth_code, actor_type, message):
    """
    Send message via socket with auth_code and actor_type
    :param socket: socket for sending
    :type socket: :class:`pyzmq.zmq.Socket`
    :param auth_code: code of connection
    :type auth_code: str
    :param auth_type: type of actor whom sends data
    :type actor_type: str
    :param message: message for sending
    :type message: str
    """
    send_str = '%s:%s:%s' % (str(auth_code), str(actor_type), str(message))
    socket.send(send_str)


def listener(socketio, auth_code, actor_type):
    """
    Connects to zmq port as subscriber listens port. Receives only messages with
    auth_code and actor_type.
    :param socketio: socket for sending recieved data
    :type socketio: object
    :param auth_code: auth_code for listening
    :type auth_code: str
    :param actor_type: actor_type for listening
    :type actor_type: str
    """
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:%d' % settings.ZMQ_PORT)

    subscriber.setsockopt(
        zmq.SUBSCRIBE,
        '%s:%s' % (
            str(auth_code),
            str(actor_type)
        )
    )
    socketio.send(json.dumps({'message': 'connected'}))

    while True:
        message = subscriber.recv()
        if message:
            auth_code, actor_type, message = (lambda *args:(
                args[0],
                args[1],
                ':'.join(args[2:])
            ))(*message.split(':'))
            socketio.send(message)


class GameNamespace(BaseNamespace):
    """
    Namespace for connect pc and phone for play games
    """
    auth_code = None
    actor_type = None

    def __init__(self, *args, **kwargs):
        super(GameNamespace, self).__init__(*args, **kwargs)
        self.auth_code = None
        self.actor_type = None

    def recv_message(self, data):
        self.handle_received_json(json.loads(data))

    def handle_received_json(self, data):
        """
        :param data: received data from client
        :type data: dict
        """
        action = data.get('action', '')
        if action == 'subscribe':
            self.auth_code = data['auth_code']
            self.actor_type = data['actor_type']
            listen_actor_type = data['listen_actor_type']
            gevent.spawn(listener, self, self.auth_code, listen_actor_type)
        if action == 'send' and self.auth_code and self.actor_type:
            data.pop('action')
            print data
            gevent.spawn(send_message, publisher, self.auth_code,
                         self.actor_type, json.dumps(data))
        if action == 'send_signal':
            signals.frontend_send(
                user=self.request.user,
                data=data
            )


def socketio(request):
    """
    Socket io view. gets socketio object and starts listen it
    :param request: http request from client
    :type request: :class:`django.http.HttpRequest`
    """
    socketio_manage(
        request.environ,
        {'': GameNamespace},
        request=request
    )
    return http.HttpResponse()
