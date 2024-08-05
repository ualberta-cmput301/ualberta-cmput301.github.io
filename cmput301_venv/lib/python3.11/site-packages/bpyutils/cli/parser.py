from __future__ import absolute_import

# imports - standard imports
import sys
import argparse
import multiprocessing as mp

# imports - module imports
from bpyutils.__attr__     import (
    __name__,
    __version__,
    __description__,
    __command__,
    __author__,
    __email__
)
from bpyutils.i18n import _
from bpyutils.util.environ    import getenv
from bpyutils.cli             import util as _cli
from bpyutils.cli.formatter   import ArgumentParserFormatter
from bpyutils.cli.util        import _CAN_ANSI_FORMAT, add_github_args
from bpyutils.util.git        import resolve_git_url

_DESCRIPTION_JUMBOTRON = \
"""
%s (v %s)

%s
""" % (
    _cli.format(__name__,        _cli.RED),
    _cli.format(__version__,     _cli.BOLD),
    _cli.format(__description__, _cli.BOLD)
)

def get_parser():
    parser = argparse.ArgumentParser(
        prog            = __command__,
        description     = _DESCRIPTION_JUMBOTRON,
        add_help        = False,
        formatter_class = ArgumentParserFormatter
    )

    # boilpy
    parser.add_argument("--update-boilpy-project",
        type    = resolve_git_url,
        help    = _("Update project")
    )
    parser.add_argument("--project-branch",
        help    = "Project branch to checkout from"
    )
    parser.add_argument("--overwrite-project",
        action  = "store_true",
        help    = "Overwrite changes within project"
    )
    parser.add_argument("--boilpy-path",
        type    = resolve_git_url,
        help    = "Path to BoilPy repostitory",
        default = "https://github.com/achillesrasquinha/boilpy"
    )

    parser = add_github_args(parser, env_prefix = __name__.replace("-", "_").upper())

    parser.add_argument("--run-job",
        action  = "append",
        help    = "Run a specific job"
    )
    parser.add_argument("--run-jobs",
        action  = "append",
        help    = "Run all jobs"
    )
    parser.add_argument("-m", "--method",
        action  = "append",
        help    = "Run Method"
    )
    parser.add_argument("--run-ml",
        help    = "Run ML pipeline"
    )
    parser.add_argument("--online",
        action  = "store_true",
        help    = "Run ML pipeline in online mode"
    )
    parser.add_argument("-p", "--param",
        action  = "append",
        help    = "Parameters"
    )
    parser.add_argument("-y", "--yes",
        action  = "store_true",
        default = getenv("ACCEPT_ALL_DIALOGS", False),
        help    = "Confirm for all dialogs."
    )
    parser.add_argument("-c", "--check",
        action  = "store_true",
        default = getenv("DRY_RUN", False),
        help    = "Perform a dry-run."
    )
    parser.add_argument("-i", "--interactive",
        action  = "store_true",
        default = getenv("INTERACTIVE", False),
        help    = "Interactive Mode."
    )
    parser.add_argument("-j", "--jobs",
        type    = int,
        help    = "Number of Jobs to be used.",
        default = getenv("JOBS", max(mp.cpu_count(), 4))
    )
    parser.add_argument("-o", "--output",
        default = getenv("OUTPUT_FILE"),
        help    = "Print Output to File."
    )
    parser.add_argument("--ignore-error",
        action  = "store_true",
        default = getenv("IGNORE_ERROR", False),
        help    = "Ignore Error in case of failure."
    )
    parser.add_argument("--force",
        action  = "store_true",
        default = getenv("FORCE", False),
        help    = "Force."
    )
    parser.add_argument("--dbshell",
        default = getenv("DATABASE_SHELL"),
        help    = "Activate database shell."
    )

    parser.add_argument("--generate-tests",
        help    = "generate test cases for a package"
    )
    parser.add_argument("--generate-docs",
        help    = "generate doc strings for a package"
    )
    parser.add_argument("--generate-translations",
        help    = "generate translations for a package"
    )
    parser.add_argument("--output-dir",
        help    = "output directory for generator"
    )
    parser.add_argument("--git-username",
        help    = "Git Username",
        default = getenv("GIT_USERNAME", __author__)
    )
    parser.add_argument("--git-email",
        help    = "Git Email",
        default = getenv("GIT_EMAIL", __email__)
    )

    if _CAN_ANSI_FORMAT or "pytest" in sys.modules:
        parser.add_argument("--no-color",
            action  = "store_true",
            default = getenv("NO_COLOR", False),
            help    = "Avoid colored output."
        )

    parser.add_argument("-V", "--verbose",
        action  = "store_true",
        help    = "Display verbose output.",
        default = getenv("VERBOSE", False)
    )
    parser.add_argument("-v", "--version",
        action  = "version",
        version = __version__,
        help    = "Show %s's version number and exit." % __name__
    )

    if any("bpyutils" in arg for arg in sys.argv):
        parser.add_argument("-h", "--help",
            action  = "help",
            default = argparse.SUPPRESS,
            help    = "Show this help message and exit."
        )

    return parser

def get_args(args = None, known = True, as_dict = True):
    parser  = get_parser()

    if known:
        args, _ = parser.parse_known_args(args)
    else:
        args    = parser.parse_args(args)

    if as_dict:
        args = args.__dict__
        
    return args