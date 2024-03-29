#!/usr/bin/python3
import subprocess
from flask import *
import shlex
import socket
from subprocess import Popen, PIPE

app = Flask(__name__)

con = None

@app.route("/language/python", methods=['GET', 'POST'])
def language_python():
    process = Popen(['./script.sh', 'python'], stdout=PIPE, stderr=PIPE)
    return "socket python aberto"   

@app.route("/language/c", methods=['GET', 'POST'])
def language_c():
    process = Popen(['./script.sh', 'c'], stdout=PIPE, stderr=PIPE)
    return "socket c aberto"

@app.route("/frente", methods=['GET', 'POST'])
def frente():
    data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        s.send(b'F00000000000000')
        data = s.recv(1024)
    return data

@app.route("/re", methods=['GET', 'POST'])
def re():
    data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        s.send(b'B00000000000000')
        data = s.recv(1024)
    return data

@app.route("/esquerda", methods=['GET', 'POST'])
def esquerda():
    data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        s.send(b'L00000000000000')
        data = s.recv(1024)
    return data

@app.route("/direita", methods=['GET', 'POST'])
def direita():
    data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        s.send(b'R00000000000000')
        data = s.recv(1024)
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)