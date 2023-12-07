import collections.abc

import yaml
from pyautogui import press, hotkey
from top_window import TopWindow


class MidiKeyMap:
    def __init__(self, yaml_file):
        self.topWindow = TopWindow()
        with open(yaml_file, 'r') as file:
            self.yaml = yaml.safe_load(file)
            if self.yaml['type'] != 'midi_key_map':
                print("Invalid File Format")
                return
            self.mappings = self.yaml['input']

    def check_and_send(self, device, midi):
        app = self.topWindow.get_top_window()
        for current_map in self.mappings:
            is_device = current_map['device']
            is_app = current_map['app']
            is_midi = current_map['midi']
            if is_device in device:
                if is_app in app:
                    if is_midi in midi:
                        keys = current_map['key']
                        if isinstance(keys, str):
                            print(f'Press {keys}')
                            press([keys])
                        else:
                            if isinstance(keys, collections.abc.Sequence):
                                if len(keys) == 1:
                                    print(f'hotkey {keys[0]}')
                                    hotkey(keys[0])
                                else:
                                    if len(keys) == 2:
                                        print(f'hotkey {keys[0]}+{keys[1]}')
                                        hotkey(keys[0], keys[1])
                                    else:
                                        if len(keys) == 3:
                                            print(f'hotkey {keys[0]}+{keys[1]}+{keys[2]}')
                                            hotkey(keys[0], keys[1], keys[2])
                                        else:
                                            if len(keys) == 4:
                                                print(f'hotkey {keys[0]}+{keys[1]}+{keys[2]}+{keys[3]}')
                                                hotkey(keys[0], keys[1], keys[2], keys[3])

    def print(self):
        print(self.yaml)
