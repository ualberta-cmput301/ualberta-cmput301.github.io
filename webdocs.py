# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://webdocs.cs.ualberta.ca/~hazelcam/301"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

for i in range(len(MENUITEMS)):
    if MENUITEMS[i][1].startswith('/'):
        MENUITEMS[i] = (MENUITEMS[i][0], SITEURL+MENUITEMS[i][1])
