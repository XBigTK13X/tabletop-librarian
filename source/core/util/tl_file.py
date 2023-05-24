import os

def path(*args,**kwargs):
    return os.path.normpath(os.path.join(*args,**kwargs))