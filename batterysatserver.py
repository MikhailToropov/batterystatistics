#!/usr/bin/python3
import sys
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        if self.data == b'1':
            exit()
        print(self.data)
        self.request.sendall(self.data.upper())

def main():
    print(sys.argv)
    print("Server start")
    HOST, PORT = "localhost", 22222
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
    
if __name__=="__main__":
    main()
