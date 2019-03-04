# -*- coding: utf-8 -*-
import codecs
import os
import re
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))


def get_version():
    default_version = datetime.now().strftime('%Y%m%d-%H%M%S')
    current_version = ''
    changes = os.path.join(PROJECT_ROOT, "CHANGES.rst")
    pattern = r'^(?P<version>[0-9]+.[0-9]+(.[0-9]+)?)'
    with codecs.open(changes, encoding='utf-8') as changes:
        for line in changes:
            match = re.match(pattern, line)
            if match:
                current_version = match.group("version")
                break
    return current_version or default_version


version = get_version()
