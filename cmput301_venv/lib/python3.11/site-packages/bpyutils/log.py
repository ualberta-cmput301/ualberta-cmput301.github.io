


from __future__ import absolute_import


# imports - standard imports
import logging

# imports - module imports
from bpyutils.util.cli import CYAN, GRAY, ORANGE
from bpyutils.util import cli as _cli
from bpyutils.__attr__   import __name__ as NAME

NOTSET      = logging.NOTSET
DEBUG       = logging.DEBUG
INFO        = logging.INFO
WARNING     = logging.WARNING
ERROR       = logging.ERROR
CRITICAL    = logging.CRITICAL

SUCCESS     = 10
logging.addLevelName(SUCCESS, "SUCCESS")

def success(self, message, *args, **kwargs):
    if self.isEnabledFor(SUCCESS):
        self._log(SUCCESS, message, args, **kwargs)

logging.Logger.success = success

_FORMAT     = '%(asctime)s | %(levelname)s | %(message)s'
_LOGGER     = {}


class LogFormatter(logging.Formatter):
    COLORS = {
        NOTSET:     _cli.GRAY,
        DEBUG:      _cli.GRAY,
        INFO:       _cli.CYAN,
        WARNING:    _cli.YELLOW,
        ERROR:      _cli.RED,
        CRITICAL:   _cli.RED,
        SUCCESS:    _cli.GREEN
    }

    def format(self, record):
        color     = LogFormatter.COLORS[record.levelno]
        format_   = _cli.format('%(name)s | %(asctime)s | %(levelname)s | ', _cli.BOLD + color) + '%(message)s'
        formatter = logging.Formatter(format_)
        return formatter.format(record)

def get_logger(name = NAME, level = DEBUG, format_ = _FORMAT):
    global _LOGGER

    if not name in _LOGGER:
        formatter = LogFormatter(format_)

        handler   = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger    = logging.getLogger(name)

        logger.setLevel(level)

        logger.addHandler(handler)
        
        _LOGGER[name] = logger
    
    return _LOGGER[name]