#!/usr/bin/python
from web_srv import config_mws, mws2

import asyncio

from config import Config
from dimmer import Dimmer

def main():
    conf = Config("conf.yaml")

    dimmer1 = Dimmer(conf.get_conf()["dimmer1"])
    dimmer2 = Dimmer(conf.get_conf()["dimmer2"])
    dimmer3 = Dimmer(conf.get_conf()["dimmer3"])

    config_mws()

    main_loop = asyncio.get_event_loop()

    main_loop.create_task(dimmer1.get_task())
    main_loop.create_task(dimmer2.get_task())
    main_loop.create_task(dimmer3.get_task())


    # Starts the server as easily as possible in managed mode,
    mws2.StartManaged()

    main_loop.run_forever()

if __name__ == "__main__":
    # execute only if run as a script
    main()
