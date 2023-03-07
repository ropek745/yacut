from flask import flash, redirect, render_template, url_for

from . import app
from .constants import NOT_UNIQUE_ID
from .forms import CutLinkForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutLinkForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = URLMap.get_unique_short_id()
    if not URLMap.is_free_short_id(custom_id):
        flash(NOT_UNIQUE_ID.format(custom_id=custom_id))
        return render_template('index.html', form=form)
    url = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    URLMap.save(url)
    return render_template(
        'index.html',
        form=form,
        short_link=url_for(
            'redirect_to_original',
            short=url.short,
            _external=True,
        )
    )


@app.route('/<string:short>')
def redirect_to_original(short):
    return redirect(
        URLMap.get_short_object(short).first_or_404().original
    )
