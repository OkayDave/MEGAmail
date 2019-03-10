import os 
import sqlite3

class MegaStore:

  def filepath(self):
    if 'APPDATA' in os.environ:
      home = os.environ['APPDATA']
    elif 'XDG_CONFIG_HOME' in os.environ:
      home = os.environ['XDG_CONFIG_HOME']
    else:
      home = os.path.join(os.environ['HOME'], '.config')
    
    home = os.path.join(home, 'megamail')

    os.makedirs(home, exist_ok=True)
    return os.path.join(home, 'mm.sqlite') 

  def cursor(self):
    return self.connection.cursor()

  def create_tables(self):
    c = self.cursor()
  
    print("creating tables")
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                  (name string, email_address string, full_name string, 
                  imap_host string, imap_port int, imap_username string, imap_password string, imap_encrpytion_method string, imap_auth_type string,
                  smtp_host string, smtp_port int, smtp_username string, smtp_password string, smtp_encrpytion_method string, smtp_auth_type string)''')

  def __init__(self, *args, **kwargs):
    print("activating SQlite")
    self.filepath = self.filepath()

    self.connection = sqlite3.connect(self.filepath)

    self.create_tables()