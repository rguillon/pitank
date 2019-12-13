from pwm.pwm_out_pca9685 import pwm_out
from clk.utc_clk import Utc_Clock

devices = { "utc_clock" : Utc_Clock(),
            "pwm0"      : pwm_out(0),
            "pwm1"      : pwm_out(1),
            "pwm2"      : pwm_out(2),
            "pwm3"      : pwm_out(3),
            "pwm4"      : pwm_out(4),
            "pwm5"      : pwm_out(5),
            "pwm6"      : pwm_out(6),
            "pwm7"      : pwm_out(7)}

def get(name):
    global devices
    return devices[name]

