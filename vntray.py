######################################## 
# Vnstat tray icon
# ----------------
# Jon Sowman 2011
# jon@hexoc.com
########################################

import commands
import gobject
import gtk

from statusicon import StatusIcon
from bandwidth import BandwidthMonitor

monitor = BandwidthMonitor()

# Create a new status bar icon with parameter in ms
icon = StatusIcon(60000, monitor)

def update():
    """
    Update the icon time, then get vnstat's output. Then find today's 
    line and set the icon tooltip to reflect that.
    Return True so that the interval timer continues. Returning false
    kills it.
    """
    monitor.update()
    icon.set_tooltip()
    return True

def main():
    """
    Add a timeout to update the icon at the specified timeout, then
    start GTK.
    """
    gobject.timeout_add(icon.timeout, update)
    gtk.main()

if __name__ == "__main__":
    update()
    main()


