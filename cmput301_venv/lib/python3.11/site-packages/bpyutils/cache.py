import os, os.path as osp

import bpyutils
from   bpyutils.util.system import makedirs

class Cache:
    def __init__(self, location = None, dirname = None):
        self.location = location or osp.join(osp.expanduser("~"), ".config")
        self.dirname  = dirname  or bpytuils.__name__

    @property
    def path(self):
        return osp.join(self.location, self.dirname)

    def create(self, exist_ok = True):
        path = self.path
        makedirs(path, exist_ok = exist_ok)