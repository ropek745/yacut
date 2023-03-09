import re
from random import sample

from yacut import db
from .error_handlers import ValidationError
from .constants import (
    ITERATION_COUNT, LENGTH_SHORT_ID, LENGTH_CUSTOM_ID,
    ORIGINAL_LINK_LEN, REGEX, SYMBOLS
)


INVALID_NAME = 'Указано недопустимое имя для короткой ссылки'
NAME_ALREADY_TAKEN = 'Имя "{custom_id}" уже занято.'
NOT_UNIQUE_ID = 'Имя {custom_id} уже занято!'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LEN), nullable=False)
    short = db.Column(db.String(LENGTH_CUSTOM_ID), unique=True)
    timestamp = db.Column(db.DateTime, index=True)

    @staticmethod
    def get_object(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def generate_short_id(length):
        return ''.join(sample(SYMBOLS, length))

    @classmethod
    def get_unique_short_id(cls, length=LENGTH_SHORT_ID):
        for _ in range(ITERATION_COUNT):
            short_id = cls.generate_short_id(length)
            if cls.get_object(short_id):
                break
        return short_id

    @staticmethod
    def validate_and_create(orig_link, custom_id=None, api=False):
        if not custom_id:
            custom_id = URLMap.get_unique_short_id()
        if api:
            if len(custom_id) > LENGTH_CUSTOM_ID:
                raise ValidationError(INVALID_NAME)
            if not re.match(REGEX, custom_id):
                raise ValidationError(INVALID_NAME)
        if URLMap.get_object(custom_id):
            raise ValidationError(
                NAME_ALREADY_TAKEN.format(custom_id=custom_id)
                if api else NOT_UNIQUE_ID.format(custom_id=custom_id)
            )
        url = URLMap(original=orig_link, short=custom_id)
        db.session.add(url)
        db.session.commit()
        return url




