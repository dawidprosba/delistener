import rtmidi
from connection.bluetooth_connection import BluetoothConnection
from time import sleep

class DigitalPiano:
    def __init__(self, name: str, connection):
        self._connection = connection
        self._name = name
        self._midi_out = rtmidi.MidiOut()
        
    
    def configure_midi_device(self):
        available_ports = self._midi_out.get_ports()
        found_port_number = None
        
        if available_ports:
            print("Available MIDI ports:")
            for i, port in enumerate(available_ports):
                # Check if connection of self is BluetoothConnection if so search fo "Bluetooth" in port
                if type(self._connection) == BluetoothConnection:
                    if "Bluetooth" in port:
                        found_port_number = i
                        break
        else:
            raise Exception("No MIDI ports available")
        
        if found_port_number is None:
            raise Exception(f"No suitable MIDI port found in {[port for port in available_ports]} for {type(self._connection)}")
        else:
            self._midi_out.open_port(found_port_number)
            print(f"Opened MIDI port: {available_ports[found_port_number]}")
        
    @property
    def name(self):
        return self._name
    
    
    def play_test_sound(self):
        #Play 5 note chime sound
        notes = [60, 64, 67, 72, 76]
        for note in notes:
            self._midi_out.send_message([0x90, note, 64])
            sleep(0.5)
            self._midi_out.send_message([0x80, note, 0])
            sleep(0.1)
        
        
        
    
    