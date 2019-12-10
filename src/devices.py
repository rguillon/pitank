from pwm.pwm_out_pca9685 import pwm_out
from clk.utc_clk import Utc_Clock
from dimmer import Dimmer


clock = Utc_Clock()

time_table = [ [ 16*3600,0.0],[18*3600,1.0],[20*3600,1.0],[22*3600,0]]


pwm1 = pwm_out(0)
pwm2 = pwm_out(2)
pwm3 = pwm_out(4)

dimmer1 = Dimmer("Output 1", clock, pwm1, time_table)
dimmer2 = Dimmer("Output 2", clock, pwm2, time_table)
dimmer3 = Dimmer("Output 3", clock, pwm3, time_table)

