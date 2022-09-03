from asyncore import dispatcher
from asynchat import asyn_chat
import socket, asyncore

NAME = 'TestChat'

class ChatSession(self, sock):
	'''
	A class that takes care of a connection between the server and a single user
	'''
	def __init__(self, sock):
		#Standard setup tasks
		asyn_chat.init(self, socket)
		self.server = server
		self.set_terminator('\r\n')
		self.data = []
		#Greet the user
		self.push('Welcome to %s\r\n' %self.server.name)

	def collect_incoming_data(self, dat):
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
		asyn_chat.handle_close(self)
		self.server.disconnect(self)