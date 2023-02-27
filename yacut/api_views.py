from flask import jsonify, request

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_url, check_unique_short_id, check_symbols_in_short_id


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if not urlmap:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': urlmap.original}), 200


@app.route('/api/id/', methods=['POST'])
def add_link():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    if 'url' not in data or 'custom_id' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)
    if 'custom_id' not in data or data['custom_id'] is None:
        data['custom_id'] = get_unique_short_url()

    custom_id = data['custom_id']
    if len(custom_id) > 16 or check_symbols_in_short_id(custom_id):
        raise InvalidAPIUsage(f'Указано недопустимое имя для короткой ссылки', 400)

    if check_unique_short_id(custom_id):
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.', 400)

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({
        'url': data['url'],
        'short_link': 'http://localhost/' + data['custom_id']
    }), 201

