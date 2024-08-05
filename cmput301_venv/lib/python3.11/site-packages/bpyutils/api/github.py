from bpyutils.api.base import BaseAPI
from bpyutils import request as req

class GitHub(BaseAPI):
    url = "https://api.github.com"

    def __init__(self, *args, **kwargs):
        self._super = super(GitHub, self)
        self._super.__init__(*args, **kwargs)

        self._repo_username = None
        self._repo_reponame = None

    def repo(self, username, reponame, create = False,
        description = None, homepage = None, private = False):
        self._repo_username = username
        self._repo_reponame = reponame

        if create:
            url = "user/repos"
            response = self.post(url, json = {
                "name": self._repo_reponame,
                "description": description,
                "homepage": homepage,
                "private": private
            })
            response.raise_for_status()

        return self

    def pr(self):
        if not self._repo_username or not self._repo_reponame:
            raise ValueError("Repo username or reponame not found.")

        url = "repos/%s/%s/pulls" % (self._repo_username, self._repo_reponame)
        response = self.post(url)
        return response