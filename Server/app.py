from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from routes import initialize_routes
from resources.db import initialize_db

app = Flask(__name__)
api = Api(app)

CORS(app)

initialize_db(app)
initialize_routes(api)

app.run(debug=True)