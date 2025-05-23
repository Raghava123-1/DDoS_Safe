from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel

class DDOSTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')
        victim = self.addHost('h1', ip='10.0.0.1')
        attacker = self.addHost('h2', ip='10.0.0.2')
        honeypot = self.addHost('h3', ip='10.0.0.3')

        self.addLink(victim, switch)
        self.addLink(attacker, switch)
        self.addLink(honeypot, switch)

def run():
    topo = DDOSTopo()
    net = Mininet(topo=topo, controller=RemoteController)
    net.start()
    net.pingAll()
    CLI(net)

if __name__ == '__main__':
    from mininet.cli import CLI
    setLogLevel('info')
    run()
