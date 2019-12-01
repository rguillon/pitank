#Copyright (c) 2019 Renaud Guillon. All rights reserved.
#
#This work is licensed under the terms of the MIT license.  
#For a copy, see <https://opensource.org/licenses/MIT>.

from pwm_out_itf import pwm_out_itf

class pwm_out(pwm_out_itf):

    def __init__(self):
        pass

    def set(self, value: float):
        print("Value set: %f"%(value))






pwm = pwm_out()

pwm.set(value = 0.0)
pwm.set(value = 0.5)
pwm.set(value = 1.0)

pwm.set(value = 1.1)
