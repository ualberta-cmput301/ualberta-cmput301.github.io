# imports - standard imports
import random
import re

import requests as req
from bpyutils.model.base           import BaseObject
from bpyutils._compat              import (
    urlencode, iteritems,
    Mapping
)
from bpyutils.util.array           import (
    sequencify,
)
from bpyutils.log                  import get_logger

logger = get_logger()

def _path_to_method_name(path):
    # strip leading and trailing "/"
    formatted = path.strip("/")
    # replace all "/" with "_"
    formatted = formatted.replace("/", "_")
    # insert "_" before every capital letter.
    formatted = re.sub(r"(\w)([A-Z])", r"\1_\2", formatted)
    # convert to lowercase
    formatted = formatted.lower()

    method_name = formatted

    return method_name

class BaseAPI(BaseObject):
    _REPR_ATTRS = ("url",)

    """
    :param url: A base URL to use.
    :param proxies: A dictionary/list of proxies to use. If a list is passed,
        each element in the list should be a dictionary of the format 
        ``{ protocol: ip }``.
    :param test: Attempt to test the connection to the base url.
    """
    def __init__(self, url = None, proxies = [ ], test = True, token = None, verbose = False, rate = None):
        self._url     = url or getattr(self, "url")
        
        self._session = req.Session()

        if proxies and \
            not isinstance(proxies, (Mapping, list, tuple)):
            raise TypeError((
                "proxies %s are not of valid type. You must "
                "either a dictionary of a list of dictionaries of the "
                "following format { protocol: ip }."))

        if isinstance(proxies, Mapping):
            proxies = [proxies]

        self._token   = token

        self._proxies = proxies
        self._rate    = rate

        self._build_api()

        if test:
            self.ping()

    @property
    def url(self):
        return getattr(self, "_url", None)

    def _create_api_function(self, api):
        METHOD_CALLERS = {
            "GET": self.get,
            "POST": self.post,
            "PUT": self.put,
            "DELETE": self.delete,
        }

        doc = api.get("doc")

        def fn(*args, **kwargs):
            data = {}

            query = api["path"]
            params = api.get("params")
            method = api.get("method", "GET")
            # auth_required = api.get("auth", False)

            if params:
                parameters = []

                if isinstance(params, Mapping):
                    for param, info in iteritems(params):
                        type_ = info.get("type", "param")
                        required = info.get("required")
                        argument = info.get("argument", param)
                        default = info.get("default")

                        if (type_ == "path" or required) and argument not in kwargs:
                            raise ValueError("Argument %s is not passed." % argument)

                        if type_ == "path":
                            value = kwargs.get(argument)
                            query = query.replace(":%s" % param, str(value))
                        else:
                            kwargs[param] = kwargs.get(argument, default)
                            parameters.append(param)

                parameters = sequencify(parameters)
                for parameter in parameters:
                    if parameter in kwargs:
                        value = kwargs.get(parameter)
                        data[parameter] = value

            args = {"params": data}

            # if auth_required:
            #     auth = OmicsDIAuth(token=self.token)
            #     args.update({"auth": auth})

            method_caller = METHOD_CALLERS.get(method, self.get)

            return method_caller(query, **args)

        if doc:
            fn.__doc__ = doc

        return fn
        
    def _build_api(self):
        api_config = getattr(self, "api", {})
        if api_config:
            if "paths" in api_config:
                for api in api_config["paths"]:
                    query = api["path"]

                    fn = self._create_api_function(api)

                    method_name = api.get("fn_name", _path_to_method_name(query))

                    setattr(self, method_name, fn)

    def _build_url(self, *args, **kwargs):
        params  = kwargs.pop("params", None) 
        prefix  = kwargs.get("prefix", True)
        
        parts   = [ ]

        if prefix:
            parts.append(self.url)

        url = "/".join(map(str, sequencify(parts) + sequencify(args)))

        if params:
            encoded  = urlencode(params)
            url     += "?%s" % encoded

        return url

    def request(self, method, url, *args, **kwargs):
        raise_error = kwargs.pop("raise_error", True)
        token       = kwargs.pop("token",       self._token)
        headers     = kwargs.pop("headers",     { })
        proxies     = kwargs.pop("proxies",     self._proxies)
        data        = kwargs.get("params",      kwargs.get("data"))
        prefix      = kwargs.get("prefix",      True)
        async_      = kwargs.pop("async_",      False)

        if token:

            headers.update({
                "Authorization": "Bearer %s" % token,
            })

        if proxies:
            proxies = random.choice(proxies)
            logger.info("Using proxy %s to dispatch request." % proxies)

        url = self._build_url(url, prefix = prefix)

        logger.info("Dispatching a %s request to URL: %s with Arguments - %s" \
            % (method, url, kwargs))

        # if async_:
        #     response = AsyncRequest(method, url, session = self._session,
        #         headers = headers, proxies = proxies, *args, **kwargs)
        # else:
        response = self._session.request(method, url,
            headers = headers, proxies = proxies, *args, **kwargs)

        if not response.ok and raise_error:
            if response.text:
                logger.error("Error recieved from the server: %s" % response.text)

            response.raise_for_status()

        return response

    def post(self, url, *args, **kwargs):
        """
        Dispatch a POST request to the server.

        :param url: URL part (does not include the base URL).
        :param args: Arguments provided to ``api.request``
        :param kwargs: Keyword Arguments provided to ``api.request``
        """
        response = self.request("POST", url, *args, **kwargs)
        return response

    def put(self, url, *args, **kwargs):
        """
        Dispatch a PUT request to the server.
        """
        response = self.request("PUT", url, *args, **kwargs)
        return response

    def get(self, url, *args, **kwargs):
        """
        Dispatch a PUT request to the server.
        """
        response = self.request("GET", url, *args, **kwargs)
        return response

    def delete(self, url, *args, **kwargs):
        """
        Dispatch a DELETE request to the server.
        """
        response = self.request("DELETE", url, *args, **kwargs)
        return response

    def ping(self):
        """
        Check if the URL is alive.

        Example::

            >>> import bpyutils
            >>> client = bpyutils.Client()
            >>> client.ping()
            'pong'
        """
        response = self.request("HEAD", "")
        return "pong"