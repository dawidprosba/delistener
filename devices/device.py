from abc import ABC
import logging

import rtmidi



class Device(ABC):
    __logger = logging.getLogger(__name__)
    def __init__(self, name: str, mac_address: str):
        self._name = name
        self._mac_address = mac_address
        
        # Establishes connection, making sure all ports are
        self.establish_connection()
    
        self._midi_out = rtmidi.MidiOut()
        self._midi_in = rtmidi.MidiIn()

        
    
    @property
    def midi_out(self):
        """Returns the MIDI output port"""
        return self._midi_out
    
    @property
    def midi_in(self):
        """Returns the MIDI input port"""
        return self._midi_in

    
    @property
    def name(self):
        """Returns the name of the device"""
        return self._name
    
    @property
    def mac_address(self):
        """Returns the MAC address of the device"""
        return self._mac_address
    
    def open_output_port(self, port_number):
        """Opens the MIDI output port"""
        self.midi_out.open_port(port_number)
    
    def open_input_port(self, port_number):
        """Opens the MIDI input port"""
        self.midi_in.open_port(port_number)

    def configure_midi_device(self):
        """Configures the MIDI device"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def on_data_from_device(self, data, *args): # The *args is must to make it work :)
        """Handles data received from the device"""
        self.__logger.info(f"Data from device: {data}")

    def play_test_sound(self):
        """Plays a test sound on the device"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def establish_connection(self):
        """Establishes a connection to the device"""
        raise NotImplementedError("Subclasses must implement this method, if not used just pass")
    