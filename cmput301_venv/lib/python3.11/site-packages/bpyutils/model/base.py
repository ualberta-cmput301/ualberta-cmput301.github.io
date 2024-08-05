from bpyutils._compat import iteritems

class BaseObject(object):
    def __init__(self, *args, **kwargs):
        for kwarg, value in iteritems(kwargs):
            setattr(self, kwarg, value)

    def __repr__(self):
        klass  = self.__class__.__name__

        prefix = ""

        if hasattr(self, "_REPR_ATTRS"):
            attrs = getattr(self, "_REPR_ATTRS")
            for attr in attrs:
                prefix += " %s='%s'" % (attr, getattr(self, attr))

        repr_ = "<%s%s>" % (klass, prefix)
        return repr_