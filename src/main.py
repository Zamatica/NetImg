import os

import settings

import image
import wire


# Setup
def setup():
    if (os.path.exists('output') == False):
        os.mkdir('output')

    return settings.Settings('config.json')


# Main
def main():
    config = setup()

    imageWriter = image.ImageWriter(config['image'])

    wire_data = wire.Wire(config['wire'], config.system)

    wire_data.run(imageWriter.callback)

main()

