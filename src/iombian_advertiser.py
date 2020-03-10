#!/usr/bin/env python

import ipaddress
import logging
import threading
import time
from zeroconf import ServiceInfo, Zeroconf

logger = logging.getLogger(__name__)

class IoMBianAdvertiser(object):
    def __init__(self, name, last_name, port=80, ip="192.168.10.100"):
        self.name = name.lower()
        self.last_name = last_name.lower()
        self.hostname = "iombian-{}{}.local".format(self.name[0], self.last_name)
        self.ip = ip
        self.port = port
        self.service = None
        self.alive = False
        self.advertiser_thread = None

    def start(self):
        self.alive = True
        self.advertiser_thread = threading.Thread(target=self.__start_advertising)
        self.advertiser_thread.setDaemon(1)
        self.advertiser_thread.start()

    def stop(self):
        if self.alive:
            self.alive = False
            if self.advertiser_thread:
                self.advertiser_thread.join()
        logger.debug("IoMBian-advertiser ('{}') stopped".format(self.hostname))

    def __start_advertising(self):
        self.service = ServiceInfo(
                type_="_iombian._tcp.local.",
                name="{}._iombian._tcp.local.".format(self.hostname),
                addresses=[ipaddress.ip_address(self.ip).packed],
                port=self.port,
                properties={"Node-RED":"1880", "MQTT-client":"1888", "Monit":"2812"},
                server="{}.".format(self.hostname))

        zeroconf = Zeroconf()
        zeroconf.register_service(self.service)

        while self.alive:
            time.sleep(0.5)

        zeroconf.unregister_service(self.service)
        zeroconf.close()

    

    