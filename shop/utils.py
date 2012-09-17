import os
from PyQt4 import uic


def loadUi(path, obj):
    path = os.path.join('ui', path)
    return uic.loadUi(path, obj)