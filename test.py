def sendagain(List):
    List.insert(0, 1)
    List.insert(1, 3)
def send(List):
    sendagain(List)


def othermethod():

    aList= []
    send(aList)
    edgeSwitch =[]

    edgeSwitch.append('3001')
    edgeSwitch.append('192.168.145.130')
    print('sh ovs-vsctl set-controller '+edgeSwitch[0]+' tcp:'+edgeSwitch[1]+':6633')

if __name__ == '__main__':

    othermethod()