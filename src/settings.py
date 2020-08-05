
import json
import os


class Settings:
    def __init__(self, file_name):
        self.config = None
        self.read_config(file_name)

        self.os = None
        self.read_os()


    def read_config(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.config = json.load(file)
            print(self.config)
        except FileNotFoundError:
            with open(file_name, 'w') as file:
                json.dump({}, file)

    
    def read_os(self):
        if os.name == 'nt':
            self.os = 'Win'
        elif os.name == 'posix':
            self.os = 'Posix'
