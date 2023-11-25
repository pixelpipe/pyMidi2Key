import threading
import time
import queue
from midi_key_map import MidiKeyMap

THREAD_COUNTER = 0

class MidiThread(threading.Thread):
    uid = 0
    def __init__(self, thread_id, name, devicename, type, port, keymap):
        self.queue = queue.Queue()
        self.type = type
        self.port = port
        self.keymap = keymap
        #threading.Thread.__init__(self, target=self.read_midi_input, args=(self,self.queue,), daemon=True)
        threading.Thread.__init__(self,daemon=True)
        self.thread_id = thread_id
        self.name = name
        self.devicename = devicename
        self.is_running = True
        self.last_midi_message = ""
        self.last_sent_message = ""

    def GetThreadCounter():
        global THREAD_COUNTER
        THREAD_COUNTER += 1
        return THREAD_COUNTER

    def run(self):
        print(f"Starting {self.name}")
        while self.is_running:
            #print_time(self.name + "\n", 1)
            if self.type == 'in':
                self.last_midi_message = str(self.port.receive())
                self.keymap.checkAndSend(self.devicename, self.last_midi_message)
                self.queue.put(self.last_midi_message)
            # if self.type == 'out':
            #     if self.queue.qsize() > 0:
            #         self.last_sent_message = self.queue.get()
            #         self.port.send(self.last_sent_message)
        print(f"Exiting {self.name}")

    def stop(self):
        print(f"Stopping {self.name}")
        self.is_running = False

    def get_queue(self):
        return self.queue

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name}: Time - {time.ctime(time.time())}")