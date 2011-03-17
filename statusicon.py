######################################## 
# Vnstat tray icon
# ----------------
# Jon Sowman 2011
# jon@hexoc.com
########################################

import gtk
from datetime import datetime

class StatusIcon:
    def __init__(self, timeout):

        self.update_time()

        self.icon = gtk.StatusIcon()
        self.icon.set_from_stock(gtk.STOCK_NETWORK)

        self.icon.connect("popup-menu", self.construct_menu)
        self.icon.set_visible(True)

        self.timeout = timeout

    def set_tooltip(self, text):
        self.icon.set_tooltip("Today's total usage: " + text)
        return True

    def construct_menu(self, event_icon, event_button, event_time):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.destroy)

        mtime = self.today.strftime("%H:%M")
        self.mtime_item = gtk.MenuItem("Last updated at " + mtime)

        self.menu.append(self.mtime_item)
        self.menu.append(self.quit_item)

        self.menu.show_all()
        self.menu.popup(None, None, gtk.status_icon_position_menu, 
            event_button, event_time, event_icon)

    def destroy(self, event_button):
        gtk.main_quit()

    def update_time(self):
        self.today = datetime.today()
        self.day = self.today.strftime("%d")
        self.month = self.today.strftime("%m")
        self.year = self.today.strftime("%y")
