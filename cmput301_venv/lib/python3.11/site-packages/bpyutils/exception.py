# imports - standard imports
import subprocess as sp

class BPyUtilsError(Exception):
    pass

class PopenError(BPyUtilsError, sp.CalledProcessError):
    pass

class DependencyNotFoundError(ImportError):
    pass