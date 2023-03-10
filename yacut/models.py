import re
from datetime import datetime
from random import sample

from yacut import db
from .error_handlers import ValidationError
from .constants import (
    ITERATION_COUNT, LENGTH_SHORT_ID, LENGTH_CUSTOM_ID,
    ORIGINAL_LINK_LEN, PATTERN_FOR_SHORT, SYMBOLS
)

INVALID_NAME = 'Указано недопустимое имя для короткой ссылки'
NAME_ALREADY_TAKEN = 'Имя "{custom_id}" уже занято.'
NOT_UNIQUE_ID = 'Имя {custom_id} уже занято!'
COMBINATIONS_ERROR = 'Кол-во комбинаций исчерпано'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LEN), nullable=False)
    short = db.Column(db.String(LENGTH_CUSTOM_ID), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)

    @staticmethod
    def get_object(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_unique_short_id(length=LENGTH_SHORT_ID):
        for _ in range(ITERATION_COUNT):
            short_id = ''.join(sample(SYMBOLS, length))
            if URLMap.get_object(short_id) is None:
                return short_id
        raise ValueError(COMBINATIONS_ERROR)

    @staticmethod
    def validate_and_create(orig_link, custom_id=None, validate=False):
        if validate and custom_id or custom_id:
            if len(custom_id) > LENGTH_CUSTOM_ID:
                raise ValidationError(INVALID_NAME)
            if not re.match(PATTERN_FOR_SHORT, custom_id):
                raise ValidationError(INVALID_NAME)
            if URLMap.get_object(custom_id):
                raise ValidationError(
                    NAME_ALREADY_TAKEN.format(custom_id=custom_id)
                    if validate else
                    NOT_UNIQUE_ID.format(custom_id=custom_id)
                )
        if not custom_id:
            custom_id = URLMap.get_unique_short_id()
        urlmap = URLMap(original=orig_link, short=custom_id)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap
