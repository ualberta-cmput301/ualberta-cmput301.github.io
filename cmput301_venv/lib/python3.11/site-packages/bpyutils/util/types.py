# pylint: disable=E1101
from functools import partial

# imports - compatibility imports
from bpyutils             import _compat
from bpyutils._compat     import zip
from bpyutils.util._dict  import dict_from_list

# imports - standard imports
import sys
import inspect

def get_function_arguments(fn):
    """Get arguments of a function

    Args:
        fn (function): The function to retrieve arguments from.

    Returns:
        dict: A dictionary of arguments. If there is no default argument, the value 
        associated to that argument would be inpsect._empty.

    Example

        >>> def add(a = 0, b = 1):
                return a + b
        >>> params = bpy.get_function_arguments(add)
        >>> params
        {'a': 0, 'b': 1}
    """
    # https://stackoverflow.com/a/2677263
    params  = dict()
    success = False
    
    if _compat.PY2: # pragma: no cover
        argspec_getter = inspect.getargspec
        success        = True
    if _compat.PYTHON_VERSION >= (3,0) and _compat.PYTHON_VERSION < (3,5): # pragma: no cover
        argspec_getter = inspect.getfullargspec
        success        = True

    if success: # pragma: no cover
        argspec   = argspec_getter(fn)
        params    = dict_from_list(argspec.args, argspec.defaults or [])

    if _compat.PYTHON_VERSION >= (3,5):
        signature  = inspect.signature(fn)
        parameters = signature.parameters

        params     = { k: v.default for k, v in _compat.iteritems(parameters) }

        success    = True

    if not success: # pragma: no cover
        raise ValueError("Unknown Python Version {} for fetching functional arguments.".format(sys.version))

    return params

# def _str_to_bool(x):
#     if x in ("True", "true"):
#         return True
    
#     if x in ("False", "false"):
#         return False
    
#     if x in ("None", "none", "Null", "null", "NULL", ""):
#         return None

#     return x

def auto_typecast(value):
    """
    Automatically convert a string into its desired data type.

    :param value: The value to be converted.

    Example::

        >>> bpy.auto_typecast("True")
        True
        >>> bpy.auto_typecast("1.2345")
        1.2345
    """
    str_to_bool = lambda x: { "True": True, "False": False, "None": None}[x]

    for type_ in (str_to_bool, int, float):
        try:
            return type_(value)
        except (KeyError, ValueError, TypeError):
            pass

    return value

def _gen_to_seq(gen, type_ = list):
    def fn(*args, **kwargs):
        return type_(gen(*args, **kwargs))
    return fn

lfilter = _gen_to_seq(filter)
lmap    = _gen_to_seq(map)

def build_fn(fn, **kwargs):
    """Build a function caller with default arguments.

    Args:
        fn (function): The function to be called.

    Returns:
        function: A function wrapper with default arguments passed.

    Example:
        
        >>> def add(a, b):
                return a + b
        >>> fn = bpy.build_fn(add, a = 1, b = 2)
        >>> fn()
        3
    """
    return partial(fn, **kwargs)