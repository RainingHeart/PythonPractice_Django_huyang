# coding:utf-8

import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello, world! <h1> from the5fire 《Django 企业开发实战》 </h1>'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 27 Mar 2019 21:58:22 GMT',
    # 'Content-Type: text/plain; charset=utf-8',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    request = b''
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())  # response转为bytes后传输
    conn.close()


def main():
    # socket.AF_INET 用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM 用于基于TCP的流式 socket 通信
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用，保证我们每次按 Ctrl+C 组合键之后，快速重启
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)  # 设置 backlog——socket 连接最大排队数量
    print('http://127.0.0.1:8000')

    try:
        while True:
            conn, address = server_socket.accept()
            handle_connection(conn, address)
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
