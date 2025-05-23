from pox.core import core
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4
from pox.lib.addresses import IPAddr
from pox.openflow import libopenflow_01 as of

log = core.getLogger()

victim_ip = IPAddr("10.0.0.1")
attacker_ip = IPAddr("10.0.0.2")
honeypot_ip = IPAddr("10.0.0.3")

def launch():
    def _handle_ConnectionUp(event):
        log.info("Switch %s connected", event.dpid)

        # Drop attacker traffic to victim (you can later dynamically change this)
        msg = of.ofp_flow_mod()
        msg.match.nw_src = attacker_ip
        msg.match.nw_dst = victim_ip
        msg.match.dl_type = 0x0800  # IPv4
        msg.actions.append(of.ofp_action_output(port=3))  # Send to honeypot
        event.connection.send(msg)

    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
