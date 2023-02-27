from flask import flash, redirect, render_template

from . import app, db
from .constants import TEMPLATE, INVALID_SYMBOLS, NOT_UNIQUE_ID, BASE_URL
from .forms import CutLinkForm
from .models import URLMap
from .utils import (
    get_unique_short_url,
    check_symbols_in_short_id,
    check_unique_short_id
)


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutLinkForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_url()
        if check_unique_short_id(custom_id):
            flash(NOT_UNIQUE_ID.format(custom_id=custom_id))
            return render_template(TEMPLATE, form=form)
        if check_symbols_in_short_id(custom_id):
            flash(INVALID_SYMBOLS)
            return render_template(TEMPLATE, form=form)
        url = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(url)
        db.session.commit()
        return render_template(
            TEMPLATE,
            form=form,
            short_link=BASE_URL + custom_id
        )
    return render_template(TEMPLATE, form=form)


@app.route('/<string:short>')
def redirect_to_original(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
