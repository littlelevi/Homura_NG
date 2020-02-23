from colorama import Fore
from homura_cfg import HomuraCfg
from homura_plugins import plugins
import subprocess
import urllib.request
import os.path

class HomuraInstallator:
    
    def __init__(self):
        pass
    
    def listapps(self):
        print (Fore.YELLOW + "------ APP PLUGINS ------")
        for app in plugins:
                print (Fore.YELLOW + "Plugin: " + app)
        print (Fore.YELLOW + "-----------------------")
                
    def install(self, **app):
        
        print (Fore.YELLOW + "---------------------------")
        print (Fore.YELLOW + "{} - Downloading {} from {}".format(HomuraCfg.NAME, app['NAME'], app['DOWNLOAD'] ))
        
        FILE = '{}-{}.exe'.format(app['NAME'], app['VER'])
        DDIR = "{}/{}".format (HomuraCfg.DDIR, FILE)

        print (Fore.YELLOW + "---------------------------")
        if os.path.isfile(DDIR):
            print (Fore.YELLOW + "{} alredy exists in {} as {}".format(app['NAME'], HomuraCfg.DDIR, FILE))
            print (Fore.YELLOW + "Download aborted")
        else:
            urllib.request.urlretrieve(app['DOWNLOAD'], DDIR)
        
        print ("")
        print ("Starting installer of {}".format(app['NAME']))
        subprocess.run(['wine64', DDIR], stdout=subprocess.PIPE)
        
        print ("")
    
        print (Fore.YELLOW + "===========================")
        print (Fore.YELLOW + "INFO:")
        print (Fore.YELLOW + app['INFO'])
        print (Fore.YELLOW + "---------------------------")
    
        #self.isinstalled(**app)
        self.create_shortcut(**app)
    
    def uninstall(self, **app):
        pass
        print (Fore.YELLOW + "{} - Unistallation of {}".format(HomuraCfg.NAME, app['NAME']))
        # Delete shortcut_file
    
    def isinstalled(self, *app):
        pass
        if os.path.isdir(''):
            print (Fore.YELLOW + "{} - {} is alredy installed".format(HomuraCfg.NAME, app['NAME']))
        
    def create_shortcut(self, **app):
        
        shortcut = '''
          [Desktop Entry]
          Comment=
          Exec=bash /usr/local/bin/{1}
          Icon={2}/{1}.png
          Categories=Game;
          Name={1}
          StartupNotify=false
          Terminal=false
          TerminalOptions=
          Type=Application
          '''.format(app['NAME'], 
                     HomuraCfg.DDIR, 
                     app['NAME'] )
          
        s = "/usr/home/{}/.local/share/applications/{}.desktop".format(HomuraCfg.USER, app['NAME'])
        print ("Test shortcut - " +s)
        
        shortcut_file = open(s,'w')
        shortcut_file.write(shortcut)
        shortcut_file.close()
