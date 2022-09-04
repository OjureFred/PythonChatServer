from asyncore import dispatcher
from asynchat import async_chat
import socket
import asyncore

NAME = 'TestChat'


class ChatSession(async_chat):
    '''
    A class that takes care of a connection between the server and a single user
    '''

    def __init__(self, server, sock):
        # Standard setup tasks
        async_chat.__init__(self, socket)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        # Greet the user
        self.push('Welcome to %s\r\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        '''
        If a terminator is found. that means a full line has
        been read. Broadcast it to everyone
        '''
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)
