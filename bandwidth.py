######################################## 
# Vnstat tray icon
# ----------------
# Jon Sowman 2011
# jon@hexoc.com
########################################

import commands
from datetime import datetime

class BandwidthMonitor:
    def __init__(self):
        self.daily = 0
        self.tenday = 0
        self.last_update = 0

    def update(self):
        """
        Run all of the update functions
        """
        self.last_update = datetime.today()
        self.update_daily()
        self.update_ten()

    def update_daily(self):
        """
        Calculate the total bandwidth usage for today
        """
        vnstat = self.stats()

        for line in vnstat:
            items = line.split(";")
            if(items[0] == "d" and items[1] == "0"):
                self.daily = int(items[3]) + int(items[4])

    def update_ten(self):
        """
        Calculate a total for the interface over the last
        ten days.
        """
        vnstat = self.stats()

        self.tenday = 0
        for line in vnstat:
            items = line.split(";")
            if (items[0] == "d"):
                if (int(items[1]) in range(0, 9)):
                    self.tenday += (int(items[3]) + int(items[4]))

    def stats(self):
        """
        Get the output from vnstat's --dumpdb option and return
        it in an array, one line per element
        """
        vnstat_lines = commands.getoutput("vnstat --dumpdb").split("\n")
        return vnstat_lines
