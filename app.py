#!/usr/local/bin/python3

from homura import Homura
from homura_cmd import HomuraCmd
from build_gui import BuildGUI

if __name__ == "__main__":
    
    homura = Homura()
    homuracmd = HomuraCmd()
    if homuracmd.args:
        gui = BuildGUI()
    
    
