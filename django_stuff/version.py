import codecs
import os
import re


def get_version(project_root=''):
    default_version = '0.0.0'
    current_version = ''
    changes = os.path.join(project_root, "CHANGES.rst")
    pattern = r'^(?P<version>[0-9]+.[0-9]+(.[0-9]+)?)'
    if not os.path.exists(changes):
        return default_version

    with codecs.open(changes, encoding='utf-8') as changes:
        for line in changes:
            match = re.match(pattern, line)
            if match:
                current_version = match.group("version")
                break
    return current_version or default_version


version = get_version()
