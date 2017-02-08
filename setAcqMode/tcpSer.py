# -*- coding: utf-8 -*-

import socket
import threading
import socketserver
import traceback

clientaddrs = set()
client_socket = []

structpack = bytearray(b'')

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        clientaddrs.add((self.client_address))
        client_socket.append(self.request)  #列表

    def handle(self):

        while True:
            # 当客户端主动断开连接时，self.recv(1024)会抛出异常
            try:
                # 一次读取1024字节,并去除两端的空白字符(包括空格,TAB,\r,\n)
                data = self.request.recv(1024).strip()

                if  data == b'':#客户端已经中断
                    clientaddrs.remove(self.client_address)
                    break

                # self.client_address是客户端的连接(host, port)的元组
                print ("receive from (%r):%r" % (self.client_address, data))

            except:
                traceback.print_exc()
                break
    def finish(self):
        clientaddrs.remove(self.client_address)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self,server_address, RequestHandlerClass, bind_and_activate=True):
        socketserver.TCPServer.__init__(self,server_address, RequestHandlerClass, bind_and_activate)

    def sendautotime(self):

        pass

    def sendacqno(self):
        pass


def startsocket( HOST, PORT):
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    #server_thread.setDaemon(True)
    server_thread.start()
    server.serve_forever()


def listallclient():
    for client in clientaddrs:
        print("已连接设备：(%s)" % (client,))
    print("已连接设备:%d" % len(clientaddrs))



startsocket('127.0.0.1', 5000)