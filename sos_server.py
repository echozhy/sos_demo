# -*- coding: utf-8 -*-
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

class DemoTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        print("[receiving]")
        self.start_flag = self.request.recv(1).strip()  #开始标志
        print(self.start_flag)
        self.factory = self.request.recv(2).strip() #厂商
        print(self.factory)
        self.seperate1 = self.request.recv(1).strip() #分隔符
        print(self.seperate1)
        self.device_id = self.request.recv(10).strip() #设备ID
        print(self.device_id)
        self.seperate2 = self.request.recv(1).strip() #分隔符2
        print(self.seperate2)
        self.data_len = self.request.recv(4).strip() #长度
        print(self.data_len)
        self.data = self.request.recv(1024).strip() #内容
        print(self.data)
        self.end_flag = self.request.recv(1).strip()    #结束标志
        print(self.end_flag)
        print("[receive end]")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()