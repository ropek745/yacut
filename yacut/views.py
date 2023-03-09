from http import HTTPStatus

from flask import flash, redirect, render_template, url_for, abort

from . import app
from .forms import CutLinkForm
from .models import URLMap
from .error_handlers import ValidationError


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutLinkForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        url = URLMap.validate_and_create(
            form.original_link.data,
            form.custom_id.data)
        return render_template(
            'index.html',
            form=form,
            short_link=url_for(
                'redirect_to_original',
                short=url.short,
                _external=True,
            )
        )
    except ValidationError as error:
        flash(error.message)
        return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_to_original(short):
    url = URLMap.get_object(short)
    return redirect(url.original) if url else abort(HTTPStatus.NOT_FOUND)
