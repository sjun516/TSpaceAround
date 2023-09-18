from flask import Flask

app = Flask(__name__, static_folder='static')
from apps.routes import routes_list
routes_list(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001, debug=True)
