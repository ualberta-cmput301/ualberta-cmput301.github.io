import os.path as osp

from bpyutils.util.system import check_path, get_basename
from bpyutils.model.base  import BaseObject

class Package(BaseObject):
    def __init__(self, path = None):
        if path:
            self._path = check_path(path)
            self._package_name = get_basename(self._path)
    
    def from_path(path):
        return Package(path = path)

    @property
    def name(self):
        return self._package_name
    
    @property
    def package_dir(self):
        return osp.join(self._path, "src", self._package_name)

    @property
    def docs_dir(self):
        return osp.join(self._path, "docs", self._package_name)

    @property
    def test_dir(self):
        return osp.join(self._path, "tests", self._package_name)