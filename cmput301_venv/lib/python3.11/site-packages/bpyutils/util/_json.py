import os.path as osp
from threading import Lock
import json

from bpyutils.util._dict  import AutoDict, autodict, merge_dict
from bpyutils.util.system import write, read
from bpyutils.util.string import strip

class JSONLogger(AutoDict):
    locks = {
        "io": Lock()
    }

    def __init__(self, path, indent = 2, *args, **kwargs):
        if not len(args):
            args = [ autodict ]

        self._super  = super(JSONLogger, self)
        self._super.__init__(*args, **kwargs)

        self._path   = osp.abspath(path)
        self._indent = indent

        self._store  = self.read()

    @property
    def store(self):
        return getattr(self, "_store", {})

    def _get_content(self):
        path    = self._path
        content = json.loads(strip(read(path)) or r"{}")

        return content

    def read(self):
        path = self._path
        data = self.store

        if not osp.exists(path):
            if data:
                self.save()
        else:
            with self.locks['io']:
                content = self._get_content()
                data    = merge_dict(data, content)

        return autodict(data)

    def __getitem__(self, key):
        value = self._store[key]
        return value

    def __setitem__(self, key, value):
        self._store[key] = value
        self.save()

    def __delitem__(self, key):
        del self._store[key]
        self.save()

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def save(self):
        path    = self._path
        indent  = self._indent
        store   = self.store

        with self.locks["io"]:
            if osp.exists(path):
                content = self._get_content()
                store   = merge_dict(content, store)

            data = json.dumps(store, indent = indent)
                
            write(path, data, force = True)

    def __repr__(self):
        return str(self.store)