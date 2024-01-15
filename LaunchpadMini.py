

import random
import time
import mido

class Launchpad:

    def __init__(self) -> None:
        self.port = mido.open_output("Network Wifi-MIDI")
        # self.port = mido.open_output([outputs for outputs in mido.get_output_names() if outputs is "aunchpad"][0])
    
    def led_control(x,y,r,g,b):
        pass


if __name__ == "__main__":
    launchpad = Launchpad()
