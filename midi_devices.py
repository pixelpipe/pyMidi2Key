import array
import re

import mido
from midi_thread import MidiThread

class MidiDevice:
    def __init__(self, id, name, type, port, keymap):
        self.id = id
        self.name = name
        self.type = type
        self.uid = f'{id}:{type}:{name}'
        self.port = port
        self.keymap = keymap
        self.thread = MidiThread(MidiThread.get_thread_counter(), self.uid, self.name, self.type, self.port, self.keymap)

    def StartMonitoring(self):
        self.thread.start()

    def StopMonitoring(self):
        self.thread.stop()
        self.thread.join()

    def GetQueuedMessages(self):
        queue = self.thread.get_queue()
        if queue.qsize() > 0:
            message = queue.get()
            return message
        return None

    def print(self):
        print(f'{self.type}:{self.id}:{self.name}')

class MidiDevices:
    def __init__(self, keymap):
        self.keymap = keymap
        self.devices = []

    def scan(self, pattern, type):
        id = 0
        if 'in' in type:
            for device in mido.get_input_names():
                port = mido.open_input(device)
                for p in pattern:
                    if p in str(device):
                        self.devices.append(MidiDevice(id, device,'in', port, self.keymap))
                id += 1
        id = 0
        if 'out' in type:
            for device in mido.get_output_names():
                port = mido.open_output(device)
                for p in pattern:
                    if p in str(device):
                        self.devices.append(MidiDevice(id, device,'out', port, self.keymap))
                id += 1

    def GetQueuedMessage(self):
        list = []
        for device in self.devices:
            message = device.GetQueuedMessages()
            if message is not None:
                list.append(message)
        return list


    def StartMonitoring(self):
        for device in self.devices:
            device.StartMonitoring()

    def StopMonitoring(self):
        for device in self.devices:
            device.StopMonitoring()

    def get_input_devices(self):
        return self.input_devices

    def get_output_devices(self):
        return self.input_devices

    def print(self):
        for device in self.devices:
            device.print()

