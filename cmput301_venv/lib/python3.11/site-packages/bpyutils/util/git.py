import os.path as osp

from bpyutils.util.array  import sequencify
from bpyutils.util.string import check_url
from bpyutils.util.system import ShellEnvironment, popen, makedirs
from bpyutils.exception   import PopenError
from bpyutils.__attr__    import __name__ as NAME
from bpyutils import log

logger = log.get_logger(NAME)

def setup_git_repo(path, remote = None, push = False, git_username = None, git_email = None, **kwargs):
    commit_ = kwargs.get("commit", False)

    with ShellEnvironment(cwd = path) as shell:
        shell("git init", output = False)

        if remote:
            shell("git remote add origin", remote,  output = False)

        if commit_:
            commit(path, message = 'Initial Commit', allow_empty = None, add = ".", push = True,
                remote = "origin", branch = "master"
            )

            shell("git checkout -B develop --track master", output = False)
            shell("git checkout -B hotfix  --track master", output = False)

            if push:
                shell("git push --all origin")

def resolve_git_url(repo, raise_err = True):
    if not check_url(repo, raise_err = False):
        repo = osp.abspath(repo)

        if not osp.exists(repo) and raise_err:
            raise ValueError("Repository %s not found." % repo)

    return repo

def update_git_repo(repo, clone = False, url = None, username = None, password = None,
    branch = "master", raise_err = True):
    repo = osp.abspath(repo)

    if not osp.exists(repo):
        if clone:
            makedirs(repo, exist_ok = True)

            with ShellEnvironment(cwd = repo) as shell:
                _, url = url.split("://")

                shell("git clone https://%s:%s@%s ." % (username, password, url))

                shell("git config user.email 'bot.bpyutils@gmail.com'")
                shell("git config user.name  'bpyutils bot'")
        else:
            if raise_err:
                raise FileNotFoundError("Repository %s not found." % repo)
    else:
        try:
            popen("git pull origin %s" % branch, cwd = repo)
        except PopenError:
            if raise_err:
                raise
            else:
                logger.warning("Unable to pull latest branch")

def commit(repo, message = None, allow_empty = None, add = None, push = None,
    remote = "origin", branch = "master"):
    with ShellEnvironment(cwd = repo) as shell:
        if add:
            add = sequencify(add)

            shell("git add %s" % " ".join(add))

        if not message:
            allow_empty = True
            
        shell("git commit %s %s" % (
            "--allow-empty" if allow_empty else "",
            "-m '%s'" % message if message else ""
        ))

        if push:
            shell("git push %s %s" % (remote, branch))