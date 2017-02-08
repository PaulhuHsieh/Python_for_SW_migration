#!/usr/bin/python
import socket
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import Controller, RemoteController # node import controller component
from mininet.cli import CLI
from mininet.log import setLogLevel

class FatTreeTopo(Topo):
    # "Create Fat Tree Topology"

    # every nodes list
    coreSwitch = []
    aggrSwitch = []
    edgeSwitch = []
    host = []

    def __init__(self):
        coreSwitchNumber = 4
        self.coreSwitchNumber = coreSwitchNumber
        self.aggrSwitchNumber = coreSwitchNumber*2
        self.edgeSwitchNumber = coreSwitchNumber*2
        self.hostNumber = self.edgeSwitchNumber*2

        # initialize topology
        Topo.__init__(self)

    # add hosts and switches
    def createCoreSwitch(self, number,net):
        for i in range(1, number+1):
            prefix = "100"
            self.coreSwitch.append(net.addSwitch(prefix+str(i)))
        # print self.coreSwitch

    def createAggrSwitch(self, number,net):
        for i in range(1, number+1):
            prefix = "200"
            self.aggrSwitch.append(net.addSwitch(prefix+str(i)))

    def createEdgeSwitch(self, number,net):
        for i in range(1, number+1):
            prefix = "300"
            self.edgeSwitch.append(net.addSwitch(prefix+str(i)))

    def createHost(self, number,net):
        for i in range(1, number+1):
            prefix = "400"
            self.host.append(net.addHost(prefix+str(i)))

    def createSwitchAndHost(self,net):
        self.createCoreSwitch(self.coreSwitchNumber,net)
        self.createAggrSwitch(self.aggrSwitchNumber,net)
        self.createEdgeSwitch(self.edgeSwitchNumber,net)
        self.createHost(self.hostNumber,net)

    # add links
    def createLinks(self,net):
        # link core and aggregation
        for i in range(0, self.aggrSwitchNumber, 2):
            net.addLink(self.coreSwitch[0], self.aggrSwitch[i])
            net.addLink(self.coreSwitch[1], self.aggrSwitch[i])
        for i in range(1, self.aggrSwitchNumber, 2):
            net.addLink(self.coreSwitch[2], self.aggrSwitch[i])
            net.addLink(self.coreSwitch[3], self.aggrSwitch[i])
        # link aggregation and edge
        for i in range(0, self.aggrSwitchNumber, 2):
            net.addLink(self.aggrSwitch[i], self.edgeSwitch[i])
            net.addLink(self.aggrSwitch[i], self.edgeSwitch[i+1])
            net.addLink(self.aggrSwitch[i+1], self.edgeSwitch[i])
            net.addLink(self.aggrSwitch[i+1], self.edgeSwitch[i+1])
        # link edge and host
        for i in range(0, self.edgeSwitchNumber):
            net.addLink(self.edgeSwitch[i], self.host[2*i])
            net.addLink(self.edgeSwitch[i], self.host[2*i+1])



    def returnCoreSwitch(self):
            return self.coreSwitch
    def returnAggrSwitch(self):
            return self.aggrSwitch
    def returnEdgeSwitch(self):
            return self.edgeSwitch

    def returnCoreSwitchNumber(self):
            return self.coreSwitchNumber
    def returnAggrSwitchNumber(self):
            return self.aggrSwitchNumber
    def returnEdgeSwitchNumber(self):
            return self.edgeSwitchNumber

def iperfTest(net, topo):
    h1, h2, h16 =  net.get(topo.host[0], topo.host[1], topo.host[15])
    # iperf server
    h1.popen("iperf -s -u -i 1 > iperf_server_h1_result", shell=True)
    h16.popen("iperf -s -u -i 1 > iperf_server_h16_result", shell=True)
    # iperf client
    h2.cmdPrint("iperf -c "+h1.IP()+" -u -t 10 -i 1 -b 100m")
    print "\n"
    h2.cmdPrint("iperf -c "+h16.IP()+" -u -t 10 -i 1 -b 100m")

def createTopo(topo,coreSwitch,aggrSwitch,edgeSwitch,coreSwitchNumber,aggrSwitchNumber,edgeSwitchNumber):



    net = Mininet(topo=None, link=TCLink, controller=None)

    controllerIP="192.168.78.159"
    controllerIP2="127.0.0.1"

    c = []
    c1 = net.addController("controller", controller=RemoteController, ip=controllerIP, port=6633)
    c2 = net.addController("controller", controller=RemoteController, ip=controllerIP2, port=6633)

    c.append(c1)
    c.append(c2)



    topo.createSwitchAndHost(net)

    topo.createLinks(net)

    print ("coreSwitch0")
    print (coreSwitch[0])

    net.build()

    for i in range(0, coreSwitchNumber / 2):
        coreSwitch[i].start([c[0]])
        coreSwitch[i + 2].start([c[1]])
    for i in range(0, aggrSwitchNumber / 2):
        aggrSwitch[i].start([c[0]])
        aggrSwitch[i + 4].start([c[1]])
    for i in range(0, edgeSwitchNumber / 2):
        edgeSwitch[i].start([c[0]])
        edgeSwitch[i + 4].start([c[1]])

    print "\nDumping host connections\n"
    #dumpNodeConnections(net.hosts)
    print "\nTesting network connectivity\n"
    #net.pingAll()
    print "\nTesting bandwidth between h1 and h2\n"

    #iperfTest(net, topo)



    CLI(net)

    net.stop()

if __name__ == '__main__':

    setLogLevel('info')

    topo = FatTreeTopo()

    tempCoreSwitch = []
    tempAggrSwitch = []
    tempEdgeSwitch = []

    tempCoreSwitchNumber = topo.returnCoreSwitchNumber()
    tempAggrSwitchNumber = topo.returnAggrSwitchNumber()
    tempEdgeSwitchNumber = topo.returnEdgeSwitchNumber()
    tempCoreSwitch = topo.returnCoreSwitch()
    tempAggrSwitch = topo.returnAggrSwitch()
    tempEdgeSwitch = topo.returnEdgeSwitch()

    createTopo(topo,tempCoreSwitch,tempAggrSwitch,tempEdgeSwitch,tempCoreSwitchNumber,tempAggrSwitchNumber,tempEdgeSwitchNumber)
