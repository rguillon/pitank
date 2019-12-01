#Copyright (c) 2019 Renaud Guillon. All rights reserved.
#
#This work is licensed under the terms of the MIT license.  
#For a copy, see <https://opensource.org/licenses/MIT>.

from abc import ABC, abstractmethod
from contracts import contract

class pwm_out_itf(object):

    @abstractmethod
    @contract
    def set(value: 'float,>=0.0,<=1.0' ):
        pass

