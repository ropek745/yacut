import re
from datetime import datetime
from random import choice

from yacut import db
from .constants import (
    CUSTOM_ID_LEN,
    LENGTH_SHORT_ID,
    LENGTH_CUSTOM_ID,
    ORIGINAL_LINK_LEN
)
from settings import SYMBOLS


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LEN), nullable=False)
    short = db.Column(db.String(CUSTOM_ID_LEN), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    @staticmethod
    def generate_short_id(length):
        return ''.join(choice(SYMBOLS) for _ in range(length))

    @staticmethod
    def save(obj):
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def is_free_short_id(cls, short_id):
        return cls.query.filter_by(short=short_id).first() is None

    @classmethod
    def get_unique_short_id(cls, length=LENGTH_SHORT_ID):
        while True:
            short_id = cls.generate_short_id(length)
            if cls.is_free_short_id(short_id):
                break
        return short_id

    @staticmethod
    def get_short_object(attr):
        return URLMap.query.filter_by(short=attr)

    @staticmethod
    def check_custom_id(custom_id):
        if (
            len(custom_id) > LENGTH_CUSTOM_ID or
            re.match(r"^[a-zA-Z0-9]*$", custom_id) is None
        ):
            return False
        return True
