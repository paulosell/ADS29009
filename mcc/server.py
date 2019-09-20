#!/usr/bin/env python3
import socket
#from ev3dev2.sound import Sound
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432    # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        if bytes([data[0]]) == b'F':
            #sound = Sound()
            #sound.speak('Forward')
            conn.send(b'frente')
        elif bytes([data[0]]) == b'R':
            #sound = Sound()
            #sound.speak('Back')
            conn.send(b're')
        elif bytes([data[0]]) == b'D':
            #sound = Sound()
            #sound.speak('Right')
            conn.send(b'direita')
        elif bytes([data[0]]) == b'E':
            #sound = Sound()
            #sound.speak('Left')
            conn.send(b'esquerda')