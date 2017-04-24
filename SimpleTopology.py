from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

def myNetwork():

    net = Mininet( topo=None, build=False)

    info( '*** Adding controller\n' )
    
    info( '*** Add switches\n')

    s1 = net.addSwitch("s1")  
    s2 = net.addSwitch("s2")
    
    
    Intf( "eth1", node=s1 ) 
    Intf( "eth2", node=s2 )

    net.addLink(s1,s2)

    c0 = net.addController("controller0", controller = RemoteController ,ip = "192.168.10.144" ,port=6633)  
    c1 = net.addController("controller1", controller = RemoteController ,ip = "192.168.10.145" ,port=6633) 

    c= []

    c.append(c0)
    c.append(c1)

    s1.start([c[0],c[1]])
    s2.start([c[0],c[1]])

    info( '*** Add links\n')
    
    info( '*** Starting network\n')
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':

    setLogLevel( 'info' )
    myNetwork()
