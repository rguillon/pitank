
from datetime import datetime

class Utc_Clock():

    def __init__(self):
        pass

    def get_time(self):
        now = datetime.now()
        return now.second + 60* now.minute + 3600 * now.hour



utc_clock = Utc_Clock()

print("Current cclk: %d " %(utc_clock.get_time())) 
