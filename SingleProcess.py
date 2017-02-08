import socket
import cPickle as pickle

def getGAdata(GAlist):
    temp = []

    for i in range(0,len(GAlist)):
        print(GAlist[i])

def recvdata():
    #int = 0

    ControllerIP="192.168.145.131"
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ControllerIP
    port = 12345
    serversocket.bind((host,port))
    serversocket.listen(5)

    string = []
    GA=[]
    result=[]
    while True:
        (clientsocket, addr) = serversocket.accept()

        while True:
            data = clientsocket.recv(4096)
            buffer= data
            f = open('temp.txt','w+')
            f.write(buffer)
            f= open('temp.txt','r')
            string2 = f.read()
            GA=string2.split('w')
          #  for i in range(0,15):
               # string2[i] = string[i]
            for i in range(0,15):
                result.append(GA[i])

            if len(result) == 15:
                getGAdata(result)
                break

            if not data:
                break

        clientsocket.close()


        #s.close


if __name__ == '__main__':


    recvdata()