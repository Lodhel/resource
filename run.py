from app.main import app
from flask_cors import CORS

from app.main.views import TestView


CORS(app)
app.add_url_rule('/', 'test', view_func=TestView.as_view('test'))
app.run(host='0.0.0.0', debug=True)
