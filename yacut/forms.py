from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField, StringField
from wtforms.validators import DataRequired, URL, Length, Optional, Regexp


class CutLinkForm(FlaskForm):
    original_link = URLField(
        'Ссылка для укорачивания',
        validators=[
            DataRequired(message='Обязательное поле!'),
            Length(1, 256),
            URL(message='Должна быть ссылка!')
        ]
    )
    custom_id = URLField(
        'Введите свою ссылку (опционально)',
        validators=[
            Optional(),
            Length(1, 16),

        ]
    )
    submit = SubmitField('Укоротить')