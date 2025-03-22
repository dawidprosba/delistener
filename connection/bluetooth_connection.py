import logging
from typing import List
from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice


__logger = logging.getLogger(__name__)


class BluetoothDeviceNotFoundError(Exception):
    def __init__(self, name: str, devices: List[BLEDevice]):
        names = [device.name for device in devices]
        super().__init__(f"Could not find Bluetooth device with name {name}, found devices: {names}")
    

    

class BluetoothConnection:
    def __init__(self, device: BLEDevice):
        self._device = device
        self._client = None
    
    async def connect(self):
        logging.info(f"Connecting to {self.device.name} ({self.device.address})")
        self._client = BleakClient(self.device.address)
        await self.client.connect()
    


    @staticmethod
    async def connect_by_name(name: str):
        # type: (str) -> BluetoothConnection 
        logging.info("Discovering devices...")
        devices = await BleakScanner.discover()

        for device in devices:
            if name in device.name:
                connection = BluetoothConnection(device)
                await connection.connect()
                return connection
        logging.error(f"Could not find Bluetooth device with name {name}")

        raise BluetoothDeviceNotFoundError(name, devices)

    @property
    def device(self):
        return self._device
    
    @property
    def client(self) -> BleakClient:
        return self._client

    
class AsyncBluetoothConnectionContextManager():
    def __init__(self, name):
        self._name = name
        
    async def __aenter__(self):
        self._connection = await BluetoothConnection.connect_by_name(self._name)
        return self._connection
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        if self._connection.client is not None and self._connection.client.is_connected:
            await self._connection.client.disconnect()
            logging.info(f"Disconnected from {self._connection.device.name} ({self._connection.device.address})")
        return False
    