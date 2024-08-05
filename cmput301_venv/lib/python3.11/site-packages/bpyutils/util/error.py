import sys
import traceback
import re

from bpyutils.cli import util as _cli
from bpyutils.util.string import strip, nl, tb
from bpyutils.util.types  import lmap
from bpyutils.util.array  import find
from bpyutils.util.system import read

_REGEX_PATTERN_TEXT_QUOTES = r'"([^"]*)"'
_COLOR_LINE_NUMBER = _cli.GRAY
_INDENT = 4

def _extract_and_format_snippet(path_file, from_ = 0, offset = 3, indent = 4):
    formatted = ""

    try:
        content = read(path_file)
        lines       = content.split("\n")

        lines       = lines[ from_ - offset : from_ + offset ]


        for i, line in enumerate(lines):
            line_num = from_ + i - offset + 1
            line_indent = indent

            line_num_format = ""
            line_num_color  = _COLOR_LINE_NUMBER

            if line_num == from_:
                line_num_format = "%s%s" % (_cli.format("→ ", _cli.RED), line_num_format)
                line_indent = 2
                line_num_color = _cli.BOLD

            line_num_format += _cli.format(str(line_num), line_num_color) + _cli.format("|", _COLOR_LINE_NUMBER)

            formatted_line = nl(tb(line_num_format, line_indent) + tb(line, indent))

            formatted += formatted_line
    except FileNotFoundError:
        pass
            
    return formatted

def _get_error_line_info(error_line):
    strips = lmap(strip, error_line.split("\n"))
    strip_info  = find(strips, lambda x: x.startswith("File"))
    info_strips = lmap(strip, strip_info.split(","))

    info_file, info_line, info_method = info_strips

    re_match = re.search(_REGEX_PATTERN_TEXT_QUOTES, info_file)
    re_group = re_match.group()
    
    path_file = re_group.replace('"', "")
    line_num  = int(info_line[5:])
    method    = info_method[3:]

    return path_file, line_num, method

def pretty_print_error(e):
    error_type = type(e)
    error_name = error_type.__name__
    error_msg  = getattr(e, "message", str(e))
    indent     = _INDENT
    
    formatted  = nl(tb(_cli.format(error_name, _cli.RED), indent))
    if error_msg:
        formatted += nl() + nl(tb(_cli.format(error_msg, _cli.BOLD), indent))

    _cli.echo(formatted)

    error_lines = traceback.format_exception(*sys.exc_info())
    error_line  = error_lines[-2]

    path_file, line_num, method = _get_error_line_info(error_line)

    formatted   = \
        nl(tb("at " + _cli.format(path_file, _cli.GREEN)    \
        + _cli.format(":%s in " % line_num, _cli.BOLD)      \
        + _cli.format(method, _cli.CYAN), indent))

    formatted  += _extract_and_format_snippet(path_file, from_ = line_num,
        indent = 4)
    
    _cli.echo(formatted)