from __future__ import absolute_import

# imports - standard imports
import sys
import os.path as osp
import sqlite3

# imports - module imports
from bpyutils.config        import PATH
from bpyutils.util.string   import strip
from bpyutils.util.system   import makedirs, read, popen, which
from bpyutils.util.array    import sequencify, chunkify
from bpyutils.util.types    import lmap
from bpyutils.model.base    import BaseObject
from bpyutils               import config, log, cli
from bpyutils._compat       import iterkeys, itervalues, iteritems

logger = log.get_logger()

IntegrityError      = sqlite3.IntegrityError
OperationalError    = sqlite3.OperationalError

def detect_dtype(dtype):
    type_ = "TEXT"

    if isinstance(dtype, float):
        type_ == "REAL"
    elif isinstance(dtype, int):
        type_ == "INTEGER"

    return type_

def _get_queries(buffer):
    queries = [ ]
    lines   = buffer.split(";")

    for line in lines:
        line = strip(line)
        queries.append(line)

    return queries

class Table(BaseObject):
    def __init__(self, db, name):
        self._db    = db
        self._name  = name

    @property
    def db(self):
        return getattr(self, "_db", None)

    @property
    def name(self):
        return getattr(self, "_name", None)

    @property
    def exists(self):
        result = self.db.query("""
            select name
            from sqlite_master
            where type='table' and name='%s'
        """ % (self.name))

        return bool(result)

    def create(self):
        self.db.query("""
            create table '%s' (
                _id integer primary key
            )
        """ % self.name)

    def add_columns(self, *columns):
        for column in columns:
            self.db.query("""
                alter table '%s'
                add column %s %s
            """ % (self.name, column["name"], column["type"]))

    def insert(self, data, homogeneous = True):
        logger.info("Inserting into table %s..." % self.name)

        if not self.exists:
            self.create()

        data = sequencify(data)

        if data:
            sample  = data[0]
            columns = None

            if homogeneous:
                columns = [ ]

                for column_name, column_value in iteritems(sample):
                    type_ = detect_dtype(column_value)
                    columns.append({
                        "type": type_,
                        "name": column_name
                    })
            else:
                # TODO: resolve...
                columns = set()

                for item in data:
                    keys = list(iterkeys(item))
                    columns.add(keys)

            self.add_columns(*columns)

            if homogeneous:
                records = [list(itervalues(d)) for d in data]

                n_cols  = len(sample)
                columns_placeholder = ", ".join([column["name"] for column in columns])
                values_placeholder = ",".join(["?" for _ in range(n_cols)])

                query   = """
                    insert into %s
                        (%s)
                        values (%s)
                """ % (self.name, columns_placeholder, values_placeholder)

                self.db.query(query, records, many = True)

    def all(self):
        if self.exists:
            return self.db.query("select * from %s" % self.name)

class DB(BaseObject):
    def __init__(self, path, timeout = 10):
        self.path        = path
        self.location    = osp.dirname(self.path)
        self._connection = None
        self.timeout     = timeout

    @property
    def connected(self):
        _connected = bool(self._connection)
        return _connected

    def connect(self, bootstrap = True, **kwargs):
        """
        Connect to database.
        """
        if not self.connected:
            self._connection = sqlite3.connect(self.path,
                timeout = self.timeout, **kwargs)
            self._connection.row_factory = sqlite3.Row

    def query(self, *args, **kwargs):
        if not self.connected:
            self.connect()

        script = kwargs.pop("script", False)
        many   = kwargs.pop("many",  False)

        type_  = ""
        if many:
            type_ = "many"
        if script:
            type_ = "script"

        cursor = self._connection.cursor()
        getattr(cursor,
            "execute%s" % type_
        )(*args, **kwargs)

        self._connection.commit()

        results = cursor.fetchall()
        results = [dict(result) for result in results]

        if len(results) == 1:
            results = results[0]

        cursor.close()

        return results

    def from_file(self, path):
        buffer  = read(path)
        queries = _get_queries(buffer)

        for query in queries:
            _CONNECTION.query(query)

    def __getitem__(self, key):
        table = Table(self, key)
        return table

_CONNECTION = None

def get_connection(location = PATH["CACHE"], bootstrap = True, log = False):
    global _CONNECTION

    if not _CONNECTION or _CONNECTION.location != location:
        if log:
            logger.info("Establishing a DataBase connection...")

        makedirs(location, exist_ok = True)

        abspath  = osp.join(location, "db.db")

        _CONNECTION = DB(abspath)
        _CONNECTION.connect(
            detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )

        if bootstrap:
            if log:
                logger.info("Bootstrapping DataBase...")

            abspath = osp.join(config.PATH["DATA"], "bootstrap.sql")
            _CONNECTION.from_file(abspath)

    return _CONNECTION

def run_db_shell(path):
    exec_sqlite = which("litecli")

    if not exec_sqlite:
        cli.echo(cli.format("For a more interactive shell, install litecli (https://github.com/dbcli/litecli) using the command: pip install litecli", cli.YELLOW))
        exec_sqlite = which("sqlite3", raise_err = True)
    
    code = popen("%s %s" % (exec_sqlite, path))

    sys.exit(code)