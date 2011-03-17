######################################## 
# Vnstat tray icon
# ----------------
# Jon Sowman 2011
# jon@hexoc.com
########################################

from datetime import datetime

class IconTime:
    def __init__(self):
        self.today = datetime.today()
        self.day = self.today.strftime("%d")
        self.month = self.today.strftime("%m")
        self.year = self.today.strftime("%y")

    def update(self):
        self.today = datetime.today()
        self.day = self.today.strftime("%d")
        self.month = self.today.strftime("%m")
        self.year = self.today.strftime("%y")
