# pylint: disable=E1101

# imports - compatibility imports
from bpyutils._compat    import _is_python_version, range
from bpyutils.util._dict import AutoDict

# imports - standard imports
import itertools

def compact(arr, type_ = list):
    """
    Creates an array with all falsey values removed. The values False, None, 0, "" are falsey.

    :param arr: The array to be compacted.
    :type arr: list, tuple
    :param type_: The type of sequence to be returned, defaults to list.

    :return: Compacted array.

    Example::

        >>> bpy.compact([1, None, 2, False, 3, 4, "", 5])
        [1, 2, 3, 4, 5]
    """
    return type_(filter(bool, arr))

def squash(seq):
    """
    Return the object in an array in case there is just a single element.

    :param arr: The array to be squashed.

    :return: The squashed array.

    Example::

        >>> bpy.squash([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> bpy.squash([1])
        1
    """
    value = seq

    if isinstance(value, (list, tuple)) and len(value) == 1:
        value = value[0]
    
    return value

def flatten(arr):
    """
    Flatten an array in case it is multi-dimensional.

    :param arr: The array to be flattened.

    :return: The flattened array.

    Example::

        >>> bpy.flatten([[1], [2, 3], [4, 5, 6]])
        [1, 2, 3, 4, 5]
    """
    if _is_python_version(major = 2, minor = 6): # pragma: no cover
        chainer = itertools.chain.from_iterable
    else:
        chainer = itertools.chain

    flattened = list(chainer(*arr))

    return flattened

def sequencify(value, type_ = list):
    """
    Convert a value into array-like.

    :param arr: The object to be converted to array-like.

    :return: A sequence.

    Example::

        >>> bpy.sequencify([1])
        [1]
        >>> bpy.sequencify(3)
        [3]
    """
    if not isinstance(value, (list, tuple)):
        value = list([value])

    value = type_(value)
        
    return value

def chunkify(arr, n):
    """
    Divide an array into chunks wherein each chunk contains "n" elements.

    :param arr: The array to be chunked.
    :param n: The number of elements in each chunk.

    :return: A generator consisting of arrays containing "n" elements each.

    Example::

        >>> bpy.sequencify([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
    """
    for i in range(0, len(arr), n):
        yield arr[i:i + n]

def group_by(data, group):
    results = AutoDict(list)

    for d in data:
        key = d.pop(group)
        results[key].append(d)

    return results


def find(arr, kind, default = None, raise_err = False):
    obj = kind

    if not callable(kind):
        kind = lambda x: x == obj
    
    found = list(filter(kind, arr))

    if not found:
        if raise_err:
            raise ValueError("%s not found in array." % obj)
        else:
            found = default
    else:
        found = squash(found)

    return found

def clip(arr, low = None, high = None):
    clipped = []

    for value in arr:
        if low is not None and value < low:
            value = low
        elif high is not None and value > high:
            value = high
            
        clipped.append(value)

    return clipped