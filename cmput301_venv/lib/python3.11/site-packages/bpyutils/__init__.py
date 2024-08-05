from __future__ import absolute_import

try:
    import os

    if os.environ.get("BPYUTILS_GEVENT_PATCH"):
        from gevent import monkey
        monkey.patch_all(threaded = False, select = False)
except ImportError:
    pass

# imports - module imports
from bpyutils.__attr__ import (
    __name__,
    __version__,
    __description__,
    __author__
)
from bpyutils import cli
from bpyutils.__main__    import main
from bpyutils.config      import Settings
from bpyutils.util.jobs   import run_all as run_all_jobs, run_job
from bpyutils.util._dict  import (
    merge_dict,
    dict_from_list,
    autodict
)
from bpyutils.util.array  import (
    compact,
    squash,
    flatten,
    sequencify,
    chunkify
)
from bpyutils.util.datetime import (
    check_datetime_format,
    get_timestamp_str
)
from bpyutils.util.types    import (
    get_function_arguments,
    auto_typecast
)
from bpyutils.i18n import _

settings = Settings()

def get_version_str():
    version = "%s%s" % (__version__, " (%s)" % __build__ if __build__ else "")
    return version