import pyshark
import pickle


class PickleDump:
    def __init__(self):
        self.data = []
    
    def write(self, data):
        self.data.append(data)
    
    def reset(self):
        self.data = []


class Wire:
    def __init__(self, config):
        path = None
        if config.os == 'Posix':
            path = config.config['tshark_location']

        self.capture = pyshark.LiveCapture(interface='Ethernet 2', tshark_path=path)

    def run(self, callback):
        data = PickleDump()

        for packet in self.capture.sniff_continuously():
            data.reset()
            pickle.dump(packet, data)

            callback(data.data[0])

