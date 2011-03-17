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
        self.weekly = 0
        self.monthly = 0
        self.tenday = 0

    def update(self):
        self.update_daily()

    def update_daily(self):
        vnstat = commands.getoutput("vnstat -d").split("\n")

        self.today = datetime.today()
        self.day = self.today.strftime("%d")
        self.month = self.today.strftime("%m")
        self.year = self.today.strftime("%y")

        for line in vnstat:
            if "%s/%s/%s" % (self.day, self.month, self.year) in line:
                daily_stat = line.split("|")
                self.daily = daily_stat[2].strip()
