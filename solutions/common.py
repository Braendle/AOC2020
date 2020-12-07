from typing import Any, Dict, List

import parse


def parselines(parse_format: str, data: str) -> List[Dict[str, Any]]:
    lines = data.splitlines()
    format_compiled = parse.compile(parse_format)
    try:
        return [format_compiled.parse(line).named for line in lines]
    except AttributeError:
        raise SyntaxError("Parse format '%s' does not match file content of file '%s'" % (parse_format, data))
