# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import time
import datetime as dt

now = dt.datetime.now

_DEFAULT_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

def get_timestamp_str(format_ = _DEFAULT_TIMESTAMP_FORMAT):
    """
    Get current timestamp string.

    :param format_: Python-compatible datetime format. (optional)

    Example:
        
        >>> bpy.get_timestamp_str()
        '2021-09-15 14:24:11'
        >>> bpy.get_timestamp_str(format_ = '%d/%m/%Y')
        '15/09/2021'
    """
    now       = time.time()
    
    datetime_ = dt.datetime.fromtimestamp(now)
    string    = datetime_.strftime(format_)

    return string

def check_datetime_format(datetime, format_, raise_err = False):
    """
    Check if a given "date-string" is of the format given.

    :param datetime: Datetime string.
    :param format: Python-compatible datetime format.
    :param raise_err: Raise a `ValueError` in case the format is not compliant.

    :return: bool
    :raises: ValueError

    Example:

        >>> bpy.check_datetime_format('2011-11-11', '%Y-%m-%d')
        True
        >>> bpy.check_datetime_format('2011-11-11 11:12:13', '%Y-%m-%d')
        False
        >>> bpy.check_datetime_format('2011-11-11 11:12:13', '%Y-%m-%d', raise_err = True)
        ValueError: Incorrect datetime format, expected %Y-%m-%d
    """
    try:
        dt.datetime.strptime(datetime, format_)
    except ValueError:
        if raise_err:
            raise ValueError("Incorrect datetime format, expected %s" % format_)
        else:
            return False
    
    return True