# Tankos, aquarium monitoring and control for MicroPython
# Copyright (c) 2019 Renaud Guillon
# SPDX-License-Identifier: MIT

import logging
import asyncio
import devices
import syslog
import yaml
from rxjson import Rx
logger = logging.getLogger("Dimmer")


schema = Rx.Factory({ "register_core_types": True }).make_schema(yaml.load("""
type: //rec
required:
    name : //str
    clock : //str
    output : //str
    schedule: //any
"""))
#        type : //arr
#        length: { min: 1 }
#        contents : //any

class Dimmer():

    def __init__(self, conf):
        self.update_conf(conf)

    def update_conf(self, conf):
        new_name = None
        new_clock = None
        new_output = None
        new_time_table = None
        try:
            new_name = conf['name']
            new_clock = devices.get(conf['clock'])
            new_output = devices.get(conf['output'])
            new_time_table = []
            for t, v in conf['schedule'].items():
                h,m,s = t.split(':')
                sec = int(h)*3600+int(m)*60+int(s)
                new_time_table.append([sec, v])
            new_time_table.sort()
        except :
            raise Exception()
        self.name = new_name
        self.clock = new_clock
        self.output = new_output
        self.time_table = new_time_table

    def update(self):
        global logger
        v = 0.0
        t = self.clock.get_time()
        if t is not None:
            if t <= self.time_table[0][0]:
                v = self.time_table[0][1]
            elif t < self.time_table[-1][0]:
                for i in range(1, len(self.time_table)):
                    if t <= self.time_table[i][0]:
                        t1, v1 = self.time_table[i - 1]
                        t2, v2 = self.time_table[i]
                        v = v1 + float(v2 - v1) * (t - t1) / float(t2 - t1)
                        break
            else:
                v = self.time_table[-1][1]
        else:
            v = self.safe_output

        logger.info("Dimmer %s set %f at time %d" % (self.name, v, t))
        self.output.set(v)


    async def get_task(self):
        while True:
            try:
               await self.update()
            except:
                pass
            await asyncio.sleep(1)
