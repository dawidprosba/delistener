import logging
from time import sleep
import rtmidi

from devices.bluetooth_device import BluetoothDevice

class DigitalPiano(BluetoothDevice):
    __logger = logging.getLogger(__name__)

    def __init__(self, name: str, mac_address: str):
        super().__init__(name, mac_address)

    
    def play_test_sound(self):
        self.__logger.info("Playing test sound")

        notes = [60, 64, 67, 72, 76]
        for note in notes:
            self._midi_out.send_message([0x90, note, 64])
            sleep(0.01)
            self._midi_out.send_message([0x80, note, 0])
        
        
        
    
    