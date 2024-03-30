import socket
from threading import Thread
import random

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip= '127.0.0.1'
port=8000
server.bind(ip, port)
server.listen()

clients= []
nicknames= []
questions= [
    
]