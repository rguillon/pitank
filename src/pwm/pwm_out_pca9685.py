#Copyright (c) 2019 Renaud Guillon. All rights reserved.
#
#This work is licensed under the terms of the MIT license.  
#For a copy, see <https://opensource.org/licenses/MIT>.

# Import the PCA9685 module.
import Adafruit_PCA9685

from .pwm_out_itf import pwm_out_itf

# Initialise the PCA9685 using the default address (0x40).
pca9685 = Adafruit_PCA9685.PCA9685(busnum=0)
# Set frequency to 60hz, good for servos.
pca9685.set_pwm_freq(60)



class pwm_out(pwm_out_itf):

    def __init__(self, out_num):
        global pca9685
        self.out_num = out_num
        self.pwm = pca9685


    def set(self, value: float):
        self.pwm.set_pwm(self.out_num, 0, int(value * 4096.0))
