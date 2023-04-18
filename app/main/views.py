from typing import Union
from flask.views import MethodView
from app.main import app


def register_url(url: str, name: str = None, methods: Union[list, tuple] = ('GET',)):
    def wrapper(cls):
        view_name = name if name else url.split('/')[1].replace('-', '_')
        kwargs = {'rule': url, 'view_func': cls.as_view(view_name), 'methods': methods}
        app.add_url_rule(**kwargs)
        return cls

    return wrapper


@register_url('/', 'home_view')
class HomeView(MethodView):

    def get(self):
        return 'ok'
