import config
import dimmer
conf = config.Config("conf.yaml")


dimmer = dimmer.Dimmer(conf.get_conf()['dimmer1'])


