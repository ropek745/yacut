from random import choice
from string import ascii_letters, digits

from .models import URLMap


def get_unique_short_url():
    return ''.join([choice(ascii_letters + digits) for _ in range(6)])


def check_symbols_in_short_id(custom_id):
    for symbol in custom_id:
        if symbol not in (ascii_letters + digits):
            return True
    return False


def check_unique_short_id(custom_id):
    if URLMap.query.filter_by(short=custom_id).first():
        return custom_id
    return False
