from colorama import Fore
from homura import HomuraCfg
from zenipy import zlist
from homura_install import HomuraInstallator
from homura_plugins import plugins

class BuildGUI(object):
    
    def __init__(self):

        columns = ["Application Name"]
        app_list = list(plugins.keys())
        
        app = zlist(columns, app_list, text='Install software', title='{} - {}'.format(HomuraCfg.NAME, HomuraCfg.VER))
        
        if app is not None:
            app = ''.join(app)
            print (app)
        
            homurainstall = HomuraInstallator()
            homurainstall.install(**plugins[app])
            homurainstall.create_shortcut(**plugins[app])
        else:
            print (Fore.YELLOW + "Nothing to install, quitting")
