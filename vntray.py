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

# Create a new status bar icon with parameter in ms
icon = StatusIcon(60000)

def parse_vnstat():
    """
    Return an array of the lines from vnstat daily output
    """
    vnstat = commands.getoutput("vnstat -d").split("\n")
    return vnstat

def update():
    """
    Update the icon time, then get vnstat's output. Then find today's 
    line and set the icon tooltip to reflect that.
    Return True so that the interval timer continues. Returning false
    kills it.
    """
    icon.update_time()
    vnstat = parse_vnstat()
    for line in vnstat:
        if "%s/%s/%s" % (icon.day, icon.month, icon.year) in line:
            daily_stat = line.split("|")
            icon.set_tooltip(daily_stat[2].strip())
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


