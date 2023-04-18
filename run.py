from app.main import app, create_app
from flask_cors import CORS


CORS(app)
app = create_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
