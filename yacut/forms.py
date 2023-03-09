from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .constants import LENGTH_CUSTOM_ID, ORIGINAL_LINK_LEN, REGEX


DATA_REQUIRED = 'Обязательное поле!'
ORIGINAL_LINK_DESC = 'Ссылка для укорачивания'
CUSTOM_ID_DESC = 'Введите свою ссылку (опционально)'
URL_MESSAGE = 'Должна быть ссылка!'
BUTTON_DESC = 'Укоротить'
INVALID_SYMBOLS = 'Присутствуют недопустимые символы'
INVALID_LENGTH = 'Недопустимая длина'


class CutLinkForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LINK_DESC,
        validators=[
            DataRequired(message=DATA_REQUIRED),
            Length(max=ORIGINAL_LINK_LEN),
            URL(message=URL_MESSAGE)
        ]
    )
    custom_id = URLField(
        CUSTOM_ID_DESC,
        validators=[
            Optional(),
            Length(max=LENGTH_CUSTOM_ID, message=INVALID_LENGTH),
            Regexp(REGEX, message=INVALID_SYMBOLS)
        ]
    )
    submit = SubmitField(BUTTON_DESC)
