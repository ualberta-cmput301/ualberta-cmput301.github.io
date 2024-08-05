import os.path as osp

from selenium import webdriver
from bpyutils.config import PATH, environment
from bpyutils.system import makedirs
from bpyutils.util.request import download_file
from bpyutils._compat import urljoin

_DRIVER = None

_CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.19/"

def get_driver_basedir(exists_ok = True):
    path = osp.join(PATH["CACHE"], "psy", "drivers")
    makedirs(path, exists_ok = exists_ok)

    return path

def get_driver_path(type_, raise_err = True):
    driver_path = osp.join(get_driver_basedir(), type_)
    return driver_path

def download_chrome_driver(target_path):
    env = environment()
    suffix = None

    if "macos" in env["os"].lower() and "arm" in env["os"]:
        suffix = "mac64_m1"
    else:
        raise ValueError("Unsupported OS %s" % env["os"])

    url = urljoin(_CHROME_DRIVER_BASE_URL, "chromedriver_%s.zip" % suffix)

    download_file(url, target_path)

def get_chrome_driver():
    driver_path = get_driver_path("chromedriver")

    if not osp.exists(driver_path):
        download_chrome_driver(driver_path)

    instance = webdriver.Chrome(driver_path)
    
    return instance

_DRIVERS = {
    "chrome": get_chrome_driver,
}

def get_driver(type_ = "chrome"):
    if not type_ in _DRIVERS:
        raise ValueError("Driver type %s not found." % type_)

    driver   = _DRIVERS[type_]
    instance = driver()

    return instance
    
def visit(url):
    if not _DRIVER:
        _DRIVER = get_driver()