######################################## 
# Vnstat tray icon
# ----------------
# Jon Sowman 2011
# jon@hexoc.com
########################################

import gtk

class StatusIcon:
    def __init__(self, timeout, monitor):
        """
        Create a new status icon with the stock network image from GTK.
        """
        self.monitor = monitor

        self.icon = gtk.StatusIcon()
        self.icon.set_from_stock(gtk.STOCK_NETWORK)

        self.icon.connect("popup-menu", self.construct_menu)
        self.icon.set_visible(True)

        self.timeout = timeout

    def set_tooltip(self):
        """
        Set the tooltip of the status icon
        """
        text = self.monitor.daily
        self.icon.set_tooltip("Today's total usage: " + str(text) + " MiB")
        return True

    def construct_menu(self, event_icon, event_button, event_time):
        """
        Make a right click menu for the status icon and populate it
        """
        self.menu = gtk.Menu()

        # Quit item on the menu
        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.destroy)

        # Last update time
        mtime = self.monitor.last_update.strftime("%H:%M")
        self.mtime_item = gtk.MenuItem("Last updated at " + mtime)

        # Daily total
        self.daily_item = gtk.MenuItem("Daily total: " + 
                str(self.monitor.daily) + " MiB")

        # Append the items to the menu in the correct order
        self.menu.append(self.daily_item)
        self.menu.append(self.mtime_item)
        self.menu.append(self.quit_item)

        self.menu.show_all()
        self.menu.popup(None, None, gtk.status_icon_position_menu, 
            event_button, event_time, event_icon)

    def destroy(self, event_button):
        """ Shut down all GTK items """
        gtk.main_quit()

