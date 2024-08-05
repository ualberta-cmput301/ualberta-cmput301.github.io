import os, os.path as osp
import ast

from bpyutils.util.system import (
    get_basename,
    read,
    write,
    makepath
)
from bpyutils.log import get_logger
from bpyutils.util.string import nl, tb, strip, lower
from bpyutils.parallel import no_daemon_pool
from bpyutils.util.types import lmap
from bpyutils.model.package import Package

logger  = get_logger()

_INDENT = 1

def _class_name_to_fn(name):
    fn_name = ""

    for i, letter in enumerate(name):
        if i and letter.isupper() and not name[i - 1].isupper():
            fn_name += "_"

        fn_name += lower(letter)

    return fn_name

def _read_and_sanitize_file(file_):
    content = read(file_)
    content = strip(content)
    content = strip(content, "\n")

    return content

class TestGenerator(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        self._module_name    = kwargs.get("module_name")
        self._module_relpath = kwargs.get("module_relpath")
        self._filter         = kwargs.get("filter_", [])

        self._head_lines     = []

        if "pytest" not in self._filter["imports"]:
            self._head_lines = [
                nl("import pytest"),
                nl()
            ]

        self._body_lines  = []
        self._import_defs = []

    @property
    def head(self):
        imp_len = len(self._import_defs)

        if imp_len:
            module_relimp   = self._module_relpath.replace(osp.sep, ".") 
            module_path     = "%s%s%s" % (
                self._module_name,
                "." if module_relimp else "",
                module_relimp
            )

            self._head_lines.append(nl("from %s import (" % module_path))

            for i, import_def in enumerate(self._import_defs):
                self._head_lines.append(tb("%s" % import_def))
                if i != imp_len - 1:
                    self._head_lines.append(nl(","))

            self._head_lines.append(nl())
            self._head_lines.append(nl(")"))

        return "".join(self._head_lines)

    @property
    def body(self):
        return "".join(self._body_lines)

    @property
    def code(self):
        return "\n".join([self.head, self.body])

    def _add_test_fn(self, name, node_name, import_ = True):
        if name not in self._filter["functions"]:
            if import_ and not node_name in self._filter["imports_from"]:
                self._import_defs.append(node_name)

            self._body_lines.extend([
                nl("def %s():" % name),
                nl(tb("raise NotImplementedError", point = _INDENT, type_ = "\t")),
                nl()
            ])
        
    def visit_ClassDef(self, node):
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                child.parent = node

        fn_name = "test_%s" % _class_name_to_fn(node.name)

        self._add_test_fn(fn_name, node.name)

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        fn_name = node.name
        is_class_fn = False

        if hasattr(node, "parent"):
            parent  = node.parent
            fn_name = "%s_%s" % (_class_name_to_fn(parent.name), fn_name)
            is_class_fn = True

        fn_name = "test_%s" % fn_name
        
        self._add_test_fn(fn_name, node.name, import_ = not is_class_fn)

        self.generic_visit(node)

class NodeFetcher(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        self._functions     = []
        self._imports       = []
        self._imports_from  = []

    @property
    def functions(self):
        return getattr(self, "_functions", [])

    @property
    def imports(self):
        return getattr(self, "_imports", [])

    @property
    def imports_from(self):
        return getattr(self, "_imports_from", [])
    
    def visit_FunctionDef(self, node):
        self._functions.append(node.name)
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self._imports.append(alias.name)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self._imports_from.append(alias.name)

def generate_tests(path, target_dir = None, check = False):
    package = Package.from_path(path)

    # path = osp.abspath(path)
    # package_name = get_basename(path)
    # package_path = osp.join(path, "src", package_name)

    if not osp.exists(package.package_dir):
        raise FileNotFoundError("Path %s not found." % package.package_dir)

    if target_dir:
        target_dir = osp.abspath(target_dir)
    else:
        target_dir = package.test_dir
        logger.info("Using target directory %s" % target_dir)

    for root, dirs, files in os.walk(package.package_dir):
        for file_ in files:
            filepath = osp.join(root, file_)

            if osp.exists(filepath):
                filename, extension = osp.splitext(file_)
            
                if extension == ".py":
                    content = _read_and_sanitize_file(filepath)
                    
                    if content:
                        dir_prefix = root.replace(package.package_dir, "")
                        dir_prefix = strip(dir_prefix, type_ = "/")

                        target_path = osp.join(target_dir, dir_prefix, "test_%s" % file_)

                        filter_fns  = []
                        filter_imps = []
                        filter_imp_from = []
                        
                        if osp.exists(target_path):
                            target_content  = _read_and_sanitize_file(target_path)
                            if target_content:
                                target_ast_tree = ast.parse(target_content)
                                fetcher = NodeFetcher()
                                fetcher.visit(target_ast_tree)

                                filter_fns  = fetcher.functions
                                filter_imps = fetcher.imports
                                filter_imp_from = fetcher.imports_from

                        ast_tree = ast.parse(content)
                        test_generator = TestGenerator(module_name = package.name,
                            module_relpath = osp.join(dir_prefix, filename),
                            filter_ = { "functions": filter_fns, 
                                "imports": filter_imps, "imports_from": filter_imp_from })
                        test_generator.visit(ast_tree)

                        test_code = ""

                        if test_generator.body:
                            test_code = test_generator.code

                        if "__init__" in file_:
                            file_ = "%s%s" % (dir_prefix, file_)

                        logger.info("Generating tests for %s..." % filepath)
                        logger.info("Writing tests to %s..." % target_path)

                        append = False

                        if osp.exists(target_path):
                            append = True
                            test_code = nl(space = 2) + test_code

                        if not check:
                            write(target_path, test_code, force = True, append = append)