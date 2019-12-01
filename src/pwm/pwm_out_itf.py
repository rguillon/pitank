#Copyright (c) 2019 Renaud Guillon. All rights reserved.
#
#This work is licensed under the terms of the MIT license.  
#For a copy, see <https://opensource.org/licenses/MIT>.

from abc import ABC, abstractmethod

class pwm_out_itf(object):

    @abstractmethod
    def set(value: float ):
        pass

