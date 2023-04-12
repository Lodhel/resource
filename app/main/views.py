from flask.views import MethodView


class TestView(MethodView):

    def get(self):
        return 'ok'
