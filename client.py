import socket
import sys


def client(addr: str = '0.0.0.0', port: int = 8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
        s.connect((addr, port))
        print(f'connected: {addr}:{port}')
        while True:
            message_send = input("> ")
            if len(message_send) == 0:
                break
            s.send(message_send.encode('utf-8'))
            message_recv = s.recv(1024).decode('utf-8')
            print(f'recv: {message_recv}')


def main(args=None):
    if len(args) == 3:
        client(args[1], int(args[2]))
    else:
        print('Usage: client.py address port')


if __name__ == "__main__":
    main(sys.argv)
