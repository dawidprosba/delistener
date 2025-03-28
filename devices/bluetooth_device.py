from abc import ABC

import logging
from devices.device import Device
from devices.helpers import MidiPortType, get_midi_port_number_by_type



class BluetoothDevice(Device,ABC):
    __logger = logging.getLogger(__name__)
    def __init__(self, name, mac_address):    
        super().__init__(name, mac_address)

        self.configure_midi_device()

    def configure_midi_device(self):
        out_port, _ = get_midi_port_number_by_type(self.midi_out.get_ports(), MidiPortType.BLUETOOTH)
        self.open_output_port(out_port)
        
        in_port, in_port_name = get_midi_port_number_by_type(self.midi_in.get_ports(), MidiPortType.BLUETOOTH)

        self.__logger.info(f"Opening input port: {in_port_name}")
        
        self.midi_in.open_port(in_port)
        self.midi_in.set_callback(self.on_data_from_device)
    
    def on_data_from_device(self, data, *args):
        return super().on_data_from_device(data, *args)
    
    def connect(self):
        # Here it should make sure that device is connected to bluetooth
        pass
    
    def establish_connection(self):
        # Currently I do it manually, because I don't have energy to implement connecting automatically
        # Since you need to just connect once..
        pass