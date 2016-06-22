import socket

if 'guinsly' in socket.gethostname():
    from base import *
    from development import *
else:
    from production import *
#this file won't be load in git and in the 
