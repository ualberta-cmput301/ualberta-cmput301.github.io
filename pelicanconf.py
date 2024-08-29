AUTHOR = 'University of Alberta'
SITENAME = 'CMPUT 301'
SITESUBTITLE = 'Software Engineering'
SITEURL = ""

PATH = "content"


TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )
LINKS = ()

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'templates/cmput301'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'toc_depth': '3-7',
            'baselevel': '3'
        },
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}
DATE_FORMATS = {
    'en': '%a, %d %b %Y at %H:%M %Z',
}

STATIC_PATHS=[]

PATH_METADATA = r'(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'
STATIC_URL = STATIC_SAVE_AS = '{path}'

DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_PAGES_ON_MENU=False

INDEX_SAVE_AS="all.html"

MENUITEMS=[
    ("Outline", "/general/outline.html"),
    ("eClass & Grades", "https://eclass.srv.ualberta.ca/course/view.php?id=98584"),
    ("Schedule", "/#schedule"),
    ("Labs", "/general/labs.html"),
    ("Project", "/general/project.html"),
    ("Individual", "/general/individual.html"),
    ("Resources", "/general/resources.html"),
    ("Help", "/general/help.html"),
    ("Discussion Forum", "https://eclass.srv.ualberta.ca/mod/forum/view.php?id=8037429"),
    ("News & Notices", "https://eclass.srv.ualberta.ca/mod/forum/view.php?id=8037428"),
    ("Lecture Zoom", "https://eclass.srv.ualberta.ca/mod/lti/view.php?id=8037420"),
    ("Slides", "/general/slides.html"),
]
