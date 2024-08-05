import csv

from bpyutils.util._dict import dict_from_list
from bpyutils.util.types import lmap, auto_typecast

def read(path, *args, **kwargs):
    data  = []
    type_ = kwargs.pop("type", "dict")
    
    with open(path) as f:
        reader = csv.reader(f, *args, **kwargs)
        header = next(reader, None)

        if type_ == "dict":
            data = lmap(lambda x: dict_from_list(header, lmap(auto_typecast, x)), reader)
        else:
            data  = []
            data.append(header)
            data += lmap(lambda x: lmap(auto_typecast, x), reader)

    return data

def write(path, row, mode = "w", *args, **kwargs):
    with open(path, mode = mode) as f:
        writer = csv.writer(f, *args, **kwargs)
        writer.writerow(row)