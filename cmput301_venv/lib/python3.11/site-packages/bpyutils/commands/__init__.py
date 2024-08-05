# imports - compatibility imports
from __future__ import absolute_import
import sys
import os, os.path as osp

from bpyutils.commands.util 	import cli_format
from bpyutils.util._dict        import merge_dict
from bpyutils.util.types        import lmap, auto_typecast
from bpyutils.util.string       import strip
from bpyutils.util.imports      import import_handler
from bpyutils.util.system       import touch, make_temp_dir, popen, ShellEnvironment
from bpyutils.util.error        import pretty_print_error
from bpyutils.util.test         import generate_tests
from bpyutils.util.doc          import generate_docs
from bpyutils.i18n.util         import generate_translations
from bpyutils.util.git          import resolve_git_url
from bpyutils.util.datetime     import get_timestamp_str
from bpyutils.db                import run_db_shell
from bpyutils 		      	    import (cli, log, parallel)
from bpyutils._compat		    import iteritems, Mapping
from bpyutils.config            import environment, get_config_path
from bpyutils.__attr__      	import __name__ as NAME
from bpyutils.exception         import DependencyNotFoundError

logger    = log.get_logger(level = log.DEBUG)

ARGUMENTS = dict(
    run_job                     = None,
    params                      = None,
    jobs						= 1,
    check		 				= False,
    interactive  				= False,
    yes			 				= False,
    no_cache		            = False,
    no_color 	 				= True,
    output						= None,
    online                      = False,
    ignore_error				= False,
    force						= False,
    generate_tests              = None,
    output_dir                  = None,
    verbose		 				= False
)

@cli.command
def command(**ARGUMENTS):
    try:
        return _command(**ARGUMENTS)
    except Exception as e:
        if not isinstance(e, DependencyNotFoundError):
            cli.echo()

            pretty_print_error(e)

            cli.echo(cli_format("""\
An error occured while performing the above command. This could be an issue with
"bpyutils". Kindly post an issue at https://github.com/achillesrasquinha/bpyutils/issues
""", cli.RED))
        else:
            raise e

def to_params(kwargs):
    class O(object):
        pass

    params = O()

    kwargs = merge_dict(ARGUMENTS, kwargs)

    for k, v in iteritems(kwargs):
        setattr(params, k, v)

    return params

def format_params(params):
    params = params or []
    params = lmap(lambda x: lmap(strip, x.split(";")), params)
    
    args   = {}
    
    for param in params:
        for p in param:
            key, value = p.split("=")
            args[key]  = auto_typecast(value)

    return args
            
def _command(*args, **kwargs):
    a = to_params(kwargs)

    if not a.verbose:
        logger.setLevel(log.NOTSET)

    logger.info("Environment: %s" % environment())
    logger.info("Arguments Passed: %s" % locals())

    file_ = a.output

    if file_:
        logger.info("Writing to output file %s..." % file_)
        touch(file_)
    
    logger.info("Using %s jobs..." % a.jobs)

    if a.dbshell:
        path_config = get_config_path(name = a.dbshell or NAME)
        path_db = osp.join(path_config, "db.db")
        run_db_shell(path_db)

    if a.run_jobs:
        logger.info("Running module %s" % a.run_jobs)

        for module in a.run_jobs:
            jobs = import_handler("%s.jobs" % module)
            args = format_params(a.param)

            for job in jobs:
                name = job

                if isinstance(job, Mapping):
                    name = job["name"]
                
                job_module_runner = import_handler("%s.%s.run" % (module, name))

                try:
                    job_module_runner(**args)
                except Exception as e:
                    pretty_print_error(e)
                    sys.exit(1)
    else:
        if a.run_job:
            for job in a.run_job:
                logger.info("Running a specific job %s" % job)

                job_module_runner = import_handler("%s.run" % job)
                args = format_params(a.param)
                
                try:
                    job_module_runner(**args)
                except Exception as e:
                    pretty_print_error(e)
                    sys.exit(1)

    if a.method:
        for method in a.method:
            args = format_params(a.param)

            callable = import_handler(method)
            callable(**args)

    if a.run_ml:
        args = format_params(a.param)
        pipelines = [
            "data.get_data",
            "data.preprocess_data",
            "pipelines.train"
        ]
        
        args = format_params(a.param)
        callables = []

        for pipeline in pipelines:
            callable = import_handler("%s.%s" % (a.run_ml, pipeline))
            callables.append(callable)

        if a.online:
            with parallel.pool(processes = a.jobs) as pool:
                pool.map(callable)
        else:
            for callable in callables:
                callable(**args)

    if a.generate_tests:
        generate_tests(a.generate_tests, check = a.check, target_dir = a.output_dir)
        
    if a.generate_docs:
        generate_docs(a.generate_docs, check = a.check, target_dir = a.output_dir)

    if a.generate_translations:
        generate_translations(a.generate_translations, check = a.check, target_dir = a.output_dir)

    if a.update_boilpy_project:
        a.update = resolve_git_url(a.update_boilpy_project)
        logger.info("Updating repo %s..." % a.update_boilpy_project)

        with make_temp_dir() as tmp_dir:
            repo_dir = a.update_boilpy_project
            
            if not osp.isdir(a.update_boilpy_project) and not a.overwrite_project:
                logger.info("Cloning to %s..." % tmp_dir)
                repo_dir = osp.join(tmp_dir, "repo")

                clone_options = ""

                if a.project_branch:
                    clone_options += "-b %s" % a.project_branch

                popen("git clone %s %s %s --depth 1" % (clone_options, a.update_boilpy_project, repo_dir), cwd = tmp_dir)

            config = osp.join(repo_dir, ".boilpy.yml")

            if not osp.exists(config):
                raise ValueError("No boilpy configuration found in repository %s." % a.update_boilpy_project)
            else:
                logger.info("Updating template...")

                template_dir = osp.join(tmp_dir, "template")

                popen("cookiecutter %s --output-dir %s --config-file %s --no-input" % (
                    a.boilpy_path, template_dir, config))

                template_repo_dir = osp.join(template_dir, os.listdir(template_dir)[0])

                with ShellEnvironment(cwd = repo_dir) as shell:
                    shell("git config --global user.name  %s" % a.git_username)
                    shell("git config --global user.email %s" % a.git_email)
                    
                    try:
                        shell("git remote add template %s" % template_repo_dir)
                    except:
                        shell("git remote set-url template %s" % template_repo_dir)

                    shell("git fetch template")
                    # shell("git merge")
                    shell("git merge --allow-unrelated-histories template/master", raise_err = False)

                    shell("git add .")
                    shell("git commit -m '[skip ci]: Update template'")

                    target_branch = "boilpy-%s" % get_timestamp_str('%Y%m%d%H%M%S')

                    shell("git checkout -B %s" % target_branch)
                    shell("git push origin %s" % target_branch)

                    GitHub = import_handler("bpyutils.api.github.GitHub")

                    github = GitHub(token = a.github_access_token)
                    github\
                        .repo(
                            a.github_username,
                            a.github_reponame
                        )\
                        .pr()