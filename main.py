#!/usr/bin/env python3

from midi_devices import MidiDevices
from midi_key_map import MidiKeyMap
import time


def main():
    key_map = MidiKeyMap('midi_key_map.yaml')
    # key_map.checkAndSend('KeyLab','note_on','Chrome')
    key_map.print()
    midi_devices = MidiDevices(key_map)
    midi_devices.scan(['nanoPAD2'], 'in')
    midi_devices.StartMonitoring()
    midi_devices.print()

    while True:
        messages = midi_devices.GetQueuedMessage()
        for message in messages:
            print(message)
        # The rest of your program goes here.
        time.sleep(0.01)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
