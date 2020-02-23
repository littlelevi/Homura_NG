import sys
import argparse
from colorama import Fore
from homura import HomuraCfg
from homura_install import HomuraInstallator
from homura_plugins import plugins

class HomuraCmd:

     def __init__(self):
        self.parser = argparse.ArgumentParser(description='{} installation script'.format(HomuraCfg.NAME))
        self.parser.add_argument('-i', '--install',   dest='plugin', help="Install app")
        self.parser.add_argument('-u', '--uninstall', dest='plugin', help="Uninstall app")
        self.parser.add_argument('-l', '--listapp', help="List App plugins", action="store_true")
        self.args = self.parser.parse_args()

        homurainstallcmd = HomuraInstallator()
        
        if self.args.listapp:
            homurainstallcmd.listapps()
        
        if self.args.plugin in plugins:
            print (Fore.YELLOW + "---------------------------")
            print (Fore.GREEN + "{} - App plugin Found !".format(self.args.plugin))
            homurainstallcmd.install(**plugins[self.args.plugin])
        else:
            print (Fore.RED + "App plugin not found or spelling error - check plugin file")
            #sys.exit()
