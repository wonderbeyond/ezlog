#!/usr/bin/python
# coding=utf-8
from ezlog.core.extension.mountpoints import *

#==================================================
# Action instance example

class Action1(PostSave):
    pass

class Action2(PostSave):
    pass

if __name__ == '__main__':
    for ac in PostSave.actions:
        print ac()

