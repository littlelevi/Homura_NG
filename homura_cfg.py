import getpass
import subprocess

class HomuraCfg(object):
    
    uname   = subprocess.run(['uname', '-rs'], stdout=subprocess.PIPE)
    wine    = subprocess.run(['wine', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    date    = subprocess.run(['date'], stdout=subprocess.PIPE)
    glx     = subprocess.run(['pkg info | grep glx'], stdout=subprocess.PIPE, shell=True)
    gpu     = subprocess.run(['pkg info glx'], stdout=subprocess.PIPE, shell=True)
    gl_info = subprocess.run(['pkg info glx'], stdout=subprocess.PIPE, shell=True)
    vulcan  = subprocess.run(['pkg info glx'], stdout=subprocess.PIPE, shell=True)

    NAME="Homura_NG"
    VER="0.1-Alpha"
    USER = getpass.getuser()
    GPU  = gpu.stdout.decode('utf-8')
    OS   = uname.stdout.decode('utf-8')
    NDIR = '/home/{}/.local/share/{}'.format(USER, NAME)
    DDIR = '{}/Data'.format(NDIR)
    ICO  = '{}/{}'.format(DDIR, NAME)
    DATE = date.stdout
    OPENGL_INFO = gl_info.stdout.decode('utf-8')
    VULCAN_INFO = vulcan.stdout.decode('utf-8')
    WINE_VER    = wine.stdout.decode('utf-8')
