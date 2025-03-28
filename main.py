import asyncio
import subprocess
from bleak import BleakScanner, BleakClient
import rtmidi
from time import sleep


from devices.pianos.digital_piano import DigitalPiano

import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(name)s] %(message)s ')
logger = logging.getLogger(__name__)

async def main():
    piano = DigitalPiano("FP-10", "F0:71:E9:51:50:1C")
    piano.play_test_sound()
    while True:
        sleep(1)


if __name__ == "__main__":
    asyncio.run(main())