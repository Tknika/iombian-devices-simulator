#!/usr/bin/env python

import ipaddress
import logging
import signal
from zeroconf import ServiceInfo, Zeroconf

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(name)-20s  - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def signal_handler(signal, frame):
    logger.info("Stopping 'iombian-devices-simulator'...")
    zeroconf.unregister_service(service_info)
    zeroconf.close()

if __name__ == "__main__":
    logger.info("Starting 'iombian-devices-simulator'...")

    service_info = ServiceInfo(
        type_="_iombian._tcp.local.",
        name="iombian-jhernandez._iombian._tcp.local.",
        addresses=[ipaddress.ip_address("192.168.10.100").packed],
        port=80,
        properties={"Node-RED":1880, "MQTT-client":1888, "Monit":2812},
        server="iombian-jhernandez.local.")

    zeroconf = Zeroconf()
    zeroconf.register_service(service_info)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
