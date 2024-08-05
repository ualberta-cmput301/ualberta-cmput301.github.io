from bpyutils.i18n.util import (
    get_locale,
    generate_translations
)

def _(string):
    locale = get_locale()
    
    return string

def register(module):
    pass