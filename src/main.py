import scraping_global_blue
import scraping_planet
from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)


@app.route('/')
def hello():
    return 'Welcome to Web Scraping API!'


@app.route('/check_gb_tf_form/<docId>/<purchaseAmount>')
def check_gb_document(docId=None, purchaseAmount=None):
    scraping = scraping_global_blue.ScrapingBlobalBlue()
    result = scraping.run_scraping(docId=docId, purchaseAmount=purchaseAmount)
    print(result)
    return result


@app.route('/check_planet_tf_form/<docId>')
def check_planet_document(docId=None):
    scraping = scraping_planet.ScrapingPlanet()
    result = scraping.run_scraping(docId=docId)
    print(result)
    return result


# Configure Swagger UI
SWAGGER_URL = '/swagger1'
API_URL = '/swagger1.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "TaxFree form tracker API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger1.json')
def swagger():
    with open('./swagger1.json', 'r') as f:
        return jsonify(json.load(f))


"""
The entry point
Warning: Use 0.0.0.0 instead of 127.0.0.1 to avoid issue when use docker container   
"""
if __name__ == '__main__':
    # Debug/Development
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5400)
    # Production
    # http_server = WSGIServer(('', 5400), app)
    # http_server.serve_forever()
