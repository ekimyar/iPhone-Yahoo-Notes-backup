import configparser
import os
import easygui_qt

def create_config():
    easy = easygui_qt.get_username_password(title="Enter your yahoo email and password")
    pword = easy['Password']
    user = easy['User name']
##  Assuming that this is a standard yahoo imap thing
    with open('noteconfig.txt', 'w') as configfile:
        configfile.write("[server]\nhostname = imap.mail.yahoo.com\nPort = 993\n\
SSL = True\n\n[account]\nusername = "+user+"\npassword = "+pword)
        configfile.close()    
create_config()


