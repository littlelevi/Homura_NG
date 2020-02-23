import os
import pyfiglet
import subprocess
from colorama import Fore, init
from zenipy import error, message
from homura_cfg import HomuraCfg

class Homura:

    def __init__(self):
    
        homura_banner = pyfiglet.figlet_format("Homura NG")
        print(homura_banner)
    
        init(autoreset=True)

        print (Fore.YELLOW + "Copyright (c) 2019-2020, The Homura Project All rights reserved.")
        print (Fore.YELLOW + "Welcome to {} {} have fun!".format(HomuraCfg.NAME, HomuraCfg.VER))
        print (Fore.YELLOW + "Running on {} ".format(HomuraCfg.OS))
        print (Fore.YELLOW + "Wine Version: {}".format(HomuraCfg.WINE_VER))
        print (Fore.YELLOW + "GPU Info OpenGL: {}".format(HomuraCfg.OPENGL_INFO))
        print (Fore.YELLOW + "GPU Info Vulkan: {} + GPU id".format(HomuraCfg.VULCAN_INFO))
    
        self.is_root()
        self.firstrun()
        self.detect_gpu()
    
    def is_root(self):
	    if HomuraCfg.USER == 'root':
		    zenipy.error(title='{} - {}'.format(HomuraCfg.NAME, HomuraCfg.VER),text='{} can not be executed as {}'.format(HomuraCfg.Name, HomuraCfg.USER))
		    sys.exit()

    def firstrun(self):
        if os.path.isdir(HomuraCfg.NDIR):
            print (HomuraCfg.NDIR+' ...' + Fore.GREEN + 'already exists(OK!)')
        else:
            print ("Seems like you are running {} for the first time".format(HomuraCfg.NAME))
            subprocess.run(['mkdir', '-p', HomuraCfg.NDIR], stdout=subprocess.PIPE)

    def detect_gpu(self):
	    if HomuraCfg.GPU == "VMware, Inc.":
		    zenipy.message(title='{} - {}'.format(HomuraCfg.NAME, HomuraCfg.VER), width=310, text='{} have detected that you are using the fallbackdrivers, please check your gpu driver installation. If you should run {} in a virtual machine or you have enabled software rendering then you can ignore this message.'.format(HomuraCfg.NAME) )

        

    
        



