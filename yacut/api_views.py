from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .models import URLMap
from .constants import (
    INVALID_NAME,
    URL_REQUIRED,
    NO_BODY,
    NAME_ALREADY_TAKEN,
    BASE_URL,
    NO_ID
)
from .error_handlers import InvalidAPIUsage
from .utils import (
    get_unique_short_url,
    check_unique_short_id,
    check_symbols_in_short_id
)


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    urlmap = URLMap.query.filter_by(short=short).first()
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
        data['custom_id'] = get_unique_short_url()

    custom_id = data['custom_id']
    if len(custom_id) > 16 or check_symbols_in_short_id(custom_id):
        raise InvalidAPIUsage(INVALID_NAME, HTTPStatus.BAD_REQUEST)

    if check_unique_short_id(custom_id):
        raise InvalidAPIUsage(
            NAME_ALREADY_TAKEN.format(custom_id=custom_id),
            HTTPStatus.BAD_REQUEST
        )

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({
        'url': data['url'],
        'short_link': BASE_URL + data['custom_id']
    }), HTTPStatus.CREATED

