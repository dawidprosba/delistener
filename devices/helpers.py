

from enum import StrEnum
from typing import List, Tuple

from devices.exceptions import MidiPortNotFoundError

class MidiPortType(StrEnum):
    """
    Enum for different types of MIDI ports.
    """
    BLUETOOTH = "BLUETOOTH"

def get_midi_port_number_by_type(available_ports: List[str], midi_port_type: MidiPortType) -> Tuple[int, str]:
    """
    Returns the index of the first Bluetooth MIDI port found in the list of available ports.
    If no Bluetooth port is found, returns None.
    """
    for i, port in enumerate(available_ports):
        if midi_port_type in port.upper():
            return (i, port)
        
    raise MidiPortNotFoundError(
        f"No suitable {midi_port_type} MIDI port found in {[port for port in available_ports]}"
    )
    
    
    