import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from megawindow import MegaWindow
import sys


class MegaApp(Gtk.Application):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, application_id="today.dave.megamail", **kwargs)

    self.window = None

  def do_startup(self):
    Gtk.Application.do_startup(self)

  def do_activate(self):
    print("activating")
    if not self.window:
      self.window = MegaWindow(application=self, title="Make Email Great Again")

    self.window.present()
    print("activated")
  
  def on_quit(self, action, param):
    self.quit()

if __name__ == "__main__":
  app = MegaApp()
  app.run(sys.argv)
    
                     