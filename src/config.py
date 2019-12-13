
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config():
    def __init__(self, file_name):
        self.file_name = file_name
        self.load_conf()

    def load_conf(self):
        self.conf = yaml.load(open(self.file_name), Loader)


    def get_conf(self):
        return self.conf
    
    def save_conf(self):
        yaml.dump(self.conf, open(self.file_name,"w"), Dumper)


