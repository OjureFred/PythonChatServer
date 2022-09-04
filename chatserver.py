from asyncore import dispatcher
from asynchat import async_chat
import socket
import asyncore

PORT = 5005
NAME = 'TestChat'


class ChatServer(dispatcher):
    '''
    A class that recieves connections and spawns individual sessions
    It also handles broadcasts to the sessions
    '''

    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(self, conn))
        print('Connection attempt from ', addr[0])


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()
