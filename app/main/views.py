from typing import Union
from flask.views import MethodView
from flask import render_template
from app.main import app


def register_url(url: str, name: str = None, methods: Union[list, tuple] = ('GET',)):
    def wrapper(cls):
        view_name = name if name else url.split('/')[1].replace('-', '_')
        kwargs = {'rule': url, 'view_func': cls.as_view(view_name), 'methods': methods}
        app.add_url_rule(**kwargs)
        return cls

    return wrapper


@register_url('/', 'index_view')
class IndexView(MethodView):

    def get(self):
        context = {}
        return render_template('index.html', **context)


@register_url('/store', 'store')
class IndexView(MethodView):

    def get(self):
        context = {}
        return render_template('store.html', **context)


@register_url('/about', 'about')
class IndexView(MethodView):

    def get(self):
        context = {}
        return render_template('about.html', **context)


@register_url('/info', 'info')
class IndexView(MethodView):

    def get(self):
        context = {}
        return render_template('info.html', **context)
