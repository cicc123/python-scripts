# coding:utf-8

import socket

from multiprocessing import Process


def handle_client(client_socket):
    """
    ´¦À¿ͻ§¶Ëë
    """
    request_data = client_socket.recv(1024)
    print("request data:", request_data)
    # ¹¹ÔÏӦÊ¾Ý    response
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "<h1>Python HTTP Test</h1>"
    response = response_start_line + response_headers + "\r\n" + response_body

    # Ï¿ͻ§¶˷µ»ØìÊ¾Ý    client_socket.send(bytes(response, "utf-8"))

    # ¹رտͻ§¶Ë¬½Ó    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]user connected" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
