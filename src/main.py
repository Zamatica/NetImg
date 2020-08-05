

import wire
import settings


config = settings.Settings('config.json')


wire_data = wire.Wire(config)

wire_data.run(print)
