import scraping_global_blue
import scraping_planet
import scraping_langhevini
from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up the Restful API
api = Api(app)

"""
The base class for the database model
"""
class Base(DeclarativeBase):
    def __init__(self):
        pass

    def __repr__(self):
        return f'<Base>'



db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name}>'


"""
The home controller. It will return a welcome message.
Please move to a separate file if the controller is too large.
"""
class HomeController(Resource):
    def get(self):

        user = User(
            name='test',
            email='test@test.it'
        )
        db.session.add(user)
        db.session.commit()
        print(User.query.all())

        return 'Welcome to Web Scraping API!'



api.add_resource(HomeController, '/')


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

@app.route('/fetch_langhevini/<page>')
def check_langhevini_document(page=None):
    scraping = scraping_langhevini.ScrapingLanghevini()
    result = scraping.run_scraping(page=page)
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

    # Create the database
    with app.app_context():
        db.create_all()

    # Debug/Development
    app.run(debug=True, host='0.0.0.0', port=5400)

    # Production
    # http_server = WSGIServer(('', 5400), app)
    # http_server.serve_forever()
