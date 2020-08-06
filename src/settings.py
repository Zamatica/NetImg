
import json
import os


class Settings:
    def __init__(self, file_name):
        self.config = None
        self.read_config(file_name)

        self.system = None
        self.read_os()


    def __getitem__(self, key):
        return self.config[key]


    def read_config(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.config = json.load(file)

        except FileNotFoundError:
            with open(file_name, 'w') as file:
                json.dump({}, file)

    
    def read_os(self):
        if os.name == 'nt':
            self.system = 'Win'
        elif os.name == 'posix':
            self.system = 'Posix'

