import socket
import SocketServer

"""multiple thread can afford multiple clients to access and work"""
class MyTCPHandler(SocketServer.BaseRequestHandler):


    def handle(self):
        print("running now")
        print("Got connection from", self.client_address)
        print("yeee")
        while True:
            data=self.request.recv(1024)
            if not data :break
            print(data)


"""single thread can afford one client to access
def recvdata():
    int = 0
    ControllerIP="192.168.208.130"
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ControllerIP
    port = 12345
    serversocket.bind((host,port))
    serversocket.listen(10)

    while True:
        (clientsocket, addr) = serversocket.accept()
        print("running now")
        print("Got connection from", addr)
        print("yeee  "+ str(int) )
        int=int+1
        print (clientsocket.recv(1024))

    #s.close
"""

if __name__ == '__main__':

    host, port ="192.168.208.130",12345
    server = SocketServer.ThreadingTCPServer((host,port), MyTCPHandler)
    server.serve_forever()