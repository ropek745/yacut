from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .constants import (
    BUTTON_DESC,
    CUSTOM_ID_DESC,
    DATA_REQUIRED,
    INVALID_SYMBOLS,
    LENGTH_CUSTOM_ID,
    ORIGINAL_LINK_DESC,
    ORIGINAL_LINK_LEN,
    URL_MESSAGE,
    REGEX
)


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
            Length(max=LENGTH_CUSTOM_ID, message='Недопустимая длина'),
            Regexp(REGEX, message=INVALID_SYMBOLS)
        ]
    )
    submit = SubmitField(BUTTON_DESC)
