import sys
import socket
import threading


def chat(sock, addr, port):
    with sock:
        flag = True
        try:
            while flag:
                message_recv = sock.recv(1024).decode('utf-8')
                if message_recv == "." or len(message_recv) == 0:
                    flag = False
                else:
                    message_resp = f"received '{message_recv}'"
                    print(f'[{port}] {message_resp}')
                    sock.send(message_resp.encode('utf-8'))
        except ConnectionResetError:
            print(f'ConnectionResetError {addr}')
        except BrokenPipeError:
            print(f'BrokenPipeError {addr}')


def serve(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(5)
        print("Server started :", port)
        while True:
            (sock, addr) = s.accept()
            print(f'Connected by {addr}')
            th = threading.Thread(
                target=chat,
                args=[sock, addr, port])
            th.start()


def main(args=None):
    svcs = []
    if len(args) > 1:
        for port_str in args[1:]:
            port = int(port_str)
            th = threading.Thread(
                target=serve,
                args=[port])
            svcs.append(th)
        for svc in svcs:
            svc.start()
        # for svc in svcs:
        #     svc.join()
    else:
        print('Usage: server.py port1, port2, ...')


if __name__ == "__main__":
    main(sys.argv)
