from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from .models import URLMap
from .error_handlers import InvalidAPIUsage, ValidationError


URL_REQUIRED = '"url" является обязательным полем!'
NO_BODY = 'Отсутствует тело запроса'
NO_ID = 'Указанный id не найден'


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    urlmap = URLMap.get_object(short)
    if not urlmap:
        raise InvalidAPIUsage(NO_ID, HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_link():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage(NO_BODY, HTTPStatus.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage(URL_REQUIRED, HTTPStatus.BAD_REQUEST)
    try:
        url = URLMap.validate_and_create(
            data.get("url"), data.get("custom_id"), True
        )
        return jsonify({
            'url': data['url'],
            'short_link': url_for(
                'redirect_to_original',
                short=url.short,
                _external=True,
            )
        }), HTTPStatus.CREATED
    except ValidationError as error:
        raise InvalidAPIUsage(message=error.message)
