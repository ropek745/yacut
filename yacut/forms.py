from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL

from .constants import (
    BUTTON_DESC,
    CUSTOM_ID_DESC,
    CUSTOM_ID_LEN,
    DATA_REQUIRED,
    ORIGINAL_LINK_DESC,
    ORIGINAL_LINK_LEN,
    URL_MESSAGE,
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
            Length(max=CUSTOM_ID_LEN),

        ]
    )
    submit = SubmitField(BUTTON_DESC)
