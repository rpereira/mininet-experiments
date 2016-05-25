
#!/usr/bin/python
#
# From Mininet CLI: sudo mn --custom vlanhost.py --host vlan,vlan=1000

def run( vlan ):
    """
    vlan (type: int): VLAN ID to be used by all hosts
    """
    host = partial( VLANHost, vlan=vlan )

    # Start a basic network using our VLANHost
    topo = SingleSwitchTopo( k=2 )
    net = Mininet( host=host, topo=topo )
    net.start()
    CLI( net )
    net.stop()
