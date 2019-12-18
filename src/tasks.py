import devices
from  config import conf
from dimmer import Dimmer


class Tasks():
    def __init__(self):
        self.tasks={}
        for dimmer in 'dimmer1', 'dimmer2', 'dimmer3':
            self.tasks[dimmer] = Dimmer(conf.get_conf(dimmer))


    def get_tasks_names(self):
        return self.tasks.keys()


    def get_task(self,name):
        return self.tasks[name]

tasks = Tasks()

