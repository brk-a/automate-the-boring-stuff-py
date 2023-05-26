#!/usr/bin/env python3

import socket
# import importlib
# simple_server = importlib.import_module('2_simple_server')
# simple_server = __import__('2_simple_server')


def simple_client():
    """simple web client"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 9000))
    cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    sock.send(cmd)

    while True:
        data = sock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    sock.close()

if __name__ == '__main__':
    simple_server.create_server()
    simple_client()