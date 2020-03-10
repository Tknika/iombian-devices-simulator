#!/usr/bin/env python

import logging
import signal
from iombian_advertiser import IoMBianAdvertiser
from people import people

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(name)-20s  - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

devices = []

def signal_handler(signal, frame):
    logger.info("Stopping 'iombian-devices-simulator'...")
    for device in devices:
        device.stop()

if __name__ == "__main__":
    logger.info("Starting 'iombian-devices-simulator'...")

    for person in people:
        d = IoMBianAdvertiser(person.get("name"), person.get("last_name"))
        devices.append(d)
        d.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
