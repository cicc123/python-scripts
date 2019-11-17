# coding:utf-8

import socket
import re
import sys
from multiprocessing import Process

class HTTPServer(object):
    num = 0
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s]user conneted" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def application(self,start_response):
        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        #    return time.ctime()
        self.num += 1
        return str(self.num)

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header

        self.response_headers = response_headers

    def handle_client(self, client_socket):
        """
        ´¦À¿ͻ§¶Ëë
        """
        # »ñͻ§¶ËëÊ¾Ý
        request_data = client_socket.recv(1024)
#        print("request data:", request_data)
        request_lines = request_data.splitlines()
#        for line in request_lines:
#            print(line)
        response_body = self.application(self.start_response)
        response = self.response_headers + "\r\n" + response_body
        # Ï¿ͻ§¶˷µ»ØìÊ¾Ý        client_socket.send(bytes(response, "utf-8"))
        # ¹رտͻ§¶Ë¬½Ó        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(("", port))


def main():
#    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()


if __name__ == "__main__":
    main()
