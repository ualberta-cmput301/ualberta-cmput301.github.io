# imports - standard imports
import os

# imports - module imports
import bpyutils
from   bpyutils.util.types 	import auto_typecast
from   bpyutils._compat		import string_types

PREFIX 	= "%s" % bpyutils.__name__.upper()

def getenvvar(name, prefix = PREFIX, seperator = "_"):
	if not prefix:
		prefix	  = ""
		seperator = ""

	envvar = "%s%s%s" % (prefix, seperator, name)
	return envvar

def getenv(name, default = None, cast = True, prefix = PREFIX, seperator = "_", raise_err = False):
    envvar = getenvvar(name, prefix = prefix, seperator = seperator)

    if not envvar in list(os.environ) and raise_err:
        raise KeyError("Environment Variable %s not found." % envvar)

    value  = os.getenv(envvar, default)
    value  = auto_typecast(value) if cast else value

    return value

def setenv(name, value, overwrite = False, prefix = PREFIX, seperator = "_", raise_err = False):
	envvar = getenvvar(name, prefix = prefix, seperator = seperator)
	set_   = False
	
	if envvar in list(os.environ):
		if overwrite:
			set_ = True
		else:
			if raise_err:
				raise ValueError("Environment Variable %s already set." % envvar)
	else:
		set_ = True

	if set_:
		os.environ[envvar] = value

def value_to_envval(value):
	"""
	Convert python types to environment values
	"""

	if not isinstance(value, string_types):
		if   value == True:
			value = "true"
		elif value == False:
			value = "false"
		elif isinstance(value, int):
			value = str(value)
		else:
			raise TypeError("Unknown parameter type %s with value %r" % (value, type(value)))

	return value

SECRETS = (
	getenvvar("JOBS_GITHUB_TOKEN"),
)