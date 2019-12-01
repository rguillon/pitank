
from pwm.pwm_out_pca9685 import pwm_out
from clk.utc_clk import Utc_Clock

from dimmer import Dimmer

import asyncio


def main():
    clock = Utc_Clock()
    
    pwm1 = pwm_out(0)
    pwm2 = pwm_out(1)
    pwm3 = pwm_out(2)


    dimmer1 = Dimmer("Output 1", clock, pwm1, [ [0 , 0.0], [36000 , 1.0]]) 
    dimmer2 = Dimmer("Output 2", clock, pwm2, [ [0 , 0.0], [36000 , 1.0]]) 
    dimmer3 = Dimmer("Output 3", clock, pwm3, [ [0 , 0.0], [36000 , 1.0]]) 

    main_loop = asyncio.get_event_loop()

    main_loop.create_task(dimmer1.get_task())
    main_loop.create_task(dimmer2.get_task())
    main_loop.create_task(dimmer3.get_task())

    main_loop.run_forever()



if __name__ == "__main__":
    # execute only if run as a script
    main()
