import hashlib
import re
import time
import string

from django.utils.crypto import get_random_string
from django.core.validators import EMPTY_VALUES


def sanitize(raw_number):
    return re.sub(r"[^0-9]", "", raw_number)


def is_equal(words):
    return all(c == words[i - 1] for i, c in enumerate(words) if i > 0)


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_cpf(value):
    """Value can be either a string in the format XXX.XXX.XXX-XX or an 11-digit number."""
    if value in EMPTY_VALUES:
        return ''
    orig_value = value[:]
    if not value.isdigit():
        value = sanitize(value)
        if not value:
            return False

    if len(value) != 11:
        return False
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = dv_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx])
                   for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = dv_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        return False
    if value.count(value[0]) == 11:
        return False
    return orig_value


def validate_cnpj(value):
    """Value can be either a string in the format XX.XXX.XXX/XXXX-XX or a group of 14 characters."""
    if value in EMPTY_VALUES:
        return ''
    orig_value = value[:]
    if not value.isdigit():
        value = sanitize(value)
        if not value:
            return False

    if len(value) != 14:
        return False
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = dv_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(list(range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = dv_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        return False
    return orig_value


def generate_code(length=10):
    allowed = string.ascii_uppercase + string.digits
    code = get_random_string(length=length, allowed_chars=allowed)
    return code


def generate_md5_hashcode(key_word):
    keyword = '{}-{}'.format(key_word, time.time())
    hashcode = hashlib.md5(keyword.encode('utf-8')).hexdigest()
    return hashcode
