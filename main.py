import asyncio
import subprocess
from bleak import BleakScanner, BleakClient
import rtmidi
from time import sleep

from connection.bluetooth_connection import AsyncBluetoothConnectionContextManager, BluetoothConnection
from devices.digital_piano import DigitalPiano


async def main():
    async with AsyncBluetoothConnectionContextManager("FP-10") as connection:
        piano = DigitalPiano("FP-10", connection)
        piano.configure_midi_device()
        piano.play_test_sound()


if __name__ == "__main__":
    asyncio.run(main())