from asyncore import dispatcher
from asyn_chat import asyn_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'

class ChatServer(dispatcher):

    def __init__(self, port):
        dispatcher.init (self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)


    def handle_accept(self):
        conn, addr = self.accept()
        print('Connection attempt from ', addr[0])


if __name__ == '__main__':
    s.ChatServer(PORT)
        try:
            asyncore.loop()
        except KeyboardInterrupt:
            print()
