#!/usr/bin/env python3
from socket import *


def create_server():
    """create a simple web server"""
    server_socket = socket(AF_INET, SOCK_STREAM)

    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while(1):
            (client_socket, address) = server_socket.accept()

            rd = client_socket.recv(5000).decode()
            pieces = rd.split('\n')
            if (len(pieces) > 0) : print(pieces[0])

            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello, world!</body></html>\r\n\r\n'
            data += '<html><body>This is FNjakai\'s first web server</body></html>\r\n\r\n'
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print(f'\nShutting down...\n')
    except Exception as exc:
        print(f'Error:\n')
        print(exc)
    
    server_socket.close()

if __name__ == '__main__':
    print(f'Access http://localhost:9000')
    create_server()