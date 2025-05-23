from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Connection established with switch: %s", event.connection)

def _handle_PacketIn(event):
    log.info("Packet received: %s", event.parsed)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("IDS Controller Loaded")

