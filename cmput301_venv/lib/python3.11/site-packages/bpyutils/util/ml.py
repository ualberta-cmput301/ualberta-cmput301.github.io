import os.path as osp

from bpyutils.util.system  import makedirs
from bpyutils.util.environ import getenv
from bpyutils.config import get_config_path

def get_data_dir(name, data_dir = None):
    prefix = name.upper()
    config_path = get_config_path(name)

    data_dir = data_dir \
        or getenv("DATA_DIR", prefix = prefix) \
        or osp.join(config_path, "data")

    makedirs(data_dir, exist_ok = True)

    return data_dir

def get_dataset_tag(name):
    prefix = name.upper()
    is_ci  = getenv("CI", prefix = prefix, default = False)

    return "ci" if is_ci else "latest"