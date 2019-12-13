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
        global schema

        if schema.check(conf):    

            self.name = conf['name']
            self.clock = devices.get(conf['clock'])
            self.output = devices.get(conf['output'])
            self.time_table = []
            for t, v in conf['schedule'].items():
                h,m,s = t.split(':')
                sec = int(h)*3600+int(m)*60+int(s)
                self.time_table.append([sec, v])
            self.time_table.sort()
        else:
            raise Exception()

    def update(self):
        global logger
        syslog.syslog("time table: " )
        v = 0.0
        t = self.clock.get_time()
        syslog.syslog("time table: " )
        syslog.syslog(str(t))
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
        syslog.syslog("Dimmer %s set %f at time %d" % (self.name, v, t))
        self.output.set(v)


    async def get_task(self):
        while True:
            try:
               await self.update()
            except:
                pass
            await asyncio.sleep(1)
