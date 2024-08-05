from bpyutils.exception import DependencyNotFoundError

class HandlerRegistry(dict):
    def __missing__(self, name):
        if '.' not in name:
            handler = __import__(name)
        else:
            module_name, handler_name = name.rsplit('.', 1)

            module  = __import__(module_name, {}, {}, [handler_name])
            handler = getattr(module, handler_name)

        self[name] = handler

        return handler

_HANDLER_REGISTRY = HandlerRegistry()

def import_handler(name):
    """
        Import anything from module path.

        Example
        >>> from bpyutils.util.imports import import_handler
        >>> abspath = import_handler("os.path.abspath")
    """
    handler = _HANDLER_REGISTRY[name]
    return handler

def import_or_raise(package, name = None, dep = "bpyutils"):
    name = name or package

    try:
        return import_handler(package)
    except ImportError:
        raise DependencyNotFoundError((
            "Unable to import {package} for resolving dependencies. "
            "{dep} requires {package} to be installed. "
            "Please install {package} by executing 'pip install {name}'."
        ).format(package = package, name = name, dep = dep))