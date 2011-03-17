######################################## 
# Vnstat tray icon
# ----------------
# Jon Sowman 2011
# jon@hexoc.com
########################################

import gtk

class StatusIcon:
    def __init__(self, timeout):

        self.icon = gtk.StatusIcon()
        self.icon.set_from_stock(gtk.STOCK_NETWORK)

        self.timeout = timeout

    def set_tooltip(self, text):
        self.icon.set_tooltip("Today's total usage: " + text)
        return True
