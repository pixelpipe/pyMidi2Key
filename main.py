#!/usr/bin/env python3

from pyautogui import press, hotkey
import mido
from midi_thread import MidiThread
from midi_devices import MidiDevice, MidiDevices
from midi_key_map import MidiKeyMap
import time

def main():
    keyMap = MidiKeyMap('midi_key_map.yaml')
    #keyMap.checkAndSend('KeyLab','note_on','Chrome')
    keyMap.print()
    midiDevices = MidiDevices(keyMap)
    midiDevices.scan(['nanoPAD2'], 'in')
    midiDevices.StartMonitoring()
    midiDevices.print()

    while (True):
        messages = midiDevices.GetQueuedMessage()
        for message in messages:
            print(message)
        # The rest of your program goes here.
        time.sleep(0.01)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

