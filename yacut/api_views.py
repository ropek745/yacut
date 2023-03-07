from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from .models import URLMap
from .constants import (
    INVALID_NAME,
    URL_REQUIRED,
    NO_BODY,
    NAME_ALREADY_TAKEN,
    NO_ID,
)
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    urlmap = URLMap.get_short_object(short).first()
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
    if 'custom_id' not in data or data['custom_id'] is None:
        data['custom_id'] = URLMap.get_unique_short_id()

    custom_id = data['custom_id']
    if not URLMap.check_custom_id(custom_id):
        raise InvalidAPIUsage(INVALID_NAME, HTTPStatus.BAD_REQUEST)

    if not URLMap.is_free_short_id(custom_id):
        raise InvalidAPIUsage(
            NAME_ALREADY_TAKEN.format(custom_id=custom_id),
            HTTPStatus.BAD_REQUEST
        )

    url = URLMap(
        original=data.get("url"),
        short=data.get("custom_id")
    )
    URLMap.save(url)
    return jsonify({
        'url': data['url'],
        'short_link': url_for(
            'redirect_to_original',
            short=url.short,
            _external=True,
        )
    }), HTTPStatus.CREATED
