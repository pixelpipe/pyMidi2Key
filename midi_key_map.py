import collections.abc

import yaml
from pyautogui import press, typewrite, hotkey
from top_window import TopWindow
class MidiKeyMap:
    def __init__(self, yamlfile):
        self.topWindow = TopWindow()
        with open(yamlfile, 'r') as file:
            self.yaml = yaml.safe_load(file)
            if self.yaml['type'] != 'midi_key_map':
                print("Invalid File Format")
                return
            self.mappings = self.yaml['input']

    def checkAndSend(self, device, midi):
        app = self.topWindow.getTopWindow()
        for map in self.mappings:
            isDevice = map['device']
            isApp = map['app']
            isMidi = map['midi']
            if isDevice in device:
                if isApp in app:
                    if isMidi in midi:
                        keys = map['key']
                        if isinstance(keys, str):
                            print(f'Press {keys}')
                            press([keys])
                        else:
                            if isinstance(keys,collections.abc.Sequence):
                                if len(keys) == 1:
                                    print(f'hotkey {keys[0]}')
                                    hotkey(keys)
                                else:
                                    if len(keys) == 2:
                                        print(f'hotkey {keys[0]}+{keys[1]}')
                                        hotkey(keys[0],keys[1])
                                    else:
                                        if len(keys) == 3:
                                            print(f'hotkey {keys[0]}+{keys[1]}+{keys[2]}')
                                            hotkey(keys[0],keys[1],keys[2])
                                        else:
                                            if len(keys) == 4:
                                                print(f'hotkey {keys[0]}+{keys[1]}+{keys[2]}+{keys[3]}')
                                                hotkey(keys[0], keys[1], keys[2], keys[3])


    def print(self):
        print(self.yaml)
