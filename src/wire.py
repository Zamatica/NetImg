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
    def __init__(self, config, system):
        path = None
        if system == 'Posix':
            path = config['tshark_location']

        self.capture = pyshark.LiveCapture(interface='Ethernet 2', tshark_path=path)

    def run(self, callback):
        data = PickleDump()

        for packet in self.capture.sniff_continuously():
            data.reset()

            if packet.transport_layer == 'TCP':
                try:
                    pickle.dump(packet.tcp.payload, data)
                except Exception:
                    pass
            elif packet.transport_layer == 'UDP':
                try:
                    pickle.dump(packet.data.data, data)
                except Exception:
                    pass
            
            if (len(data.data)):
                callback(data.data)

