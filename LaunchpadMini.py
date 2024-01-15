

import random
import time
import mido

class Launchpad:

    def __init__(self) -> None:
        self.port = mido.open_output("Network Wifi-MIDI")
        # self.port = mido.open_output([outputs for outputs in mido.get_output_names() if outputs is "aunchpad"][0])
    
    def address_from_coordinate(self, x, y):
        address = x * 10 + y
        return address

    def led_control(self, x, y, red, green, blue):
        address = self.address_from_coordinate(x,y)
        message = mido.Message('sysex', data=[0, 32, 41, 2, 13, 3, 3, address, red, green, blue])
        self.port.send(message)
        pass
    

if __name__ == "__main__":
    launchpad = Launchpad()
    launchpad.led_control(3,6,127,0,0)
