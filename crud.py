import copy
import json
from os import abort

from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from classes.models.soup import Soup

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "postgres+psycopg2://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class PumpkinSoup(Soup, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_in_UAH = db.Column(db.Float, unique=False)
    mass_in_grams = db.Column(db.Integer, unique=False)
    time_for_cooking_in_minutes = db.Column(db.Integer, unique=False)
    name_of_dish = db.Column(db.String(64), unique=False)
    ingredients = db.Column('ingredients', db.String(255), default='[]', server_default='[]')
    specifications = db.Column('ingredients', db.Specification, default='[]', server_default='[]')
    condition = db.Column(db.Condition, unique=False)
    consistence = db.Column(db.String(32), unique=False)
    country_of_origin = db.Column(db.String(32), unique=False)

    def __init__(self, price_in_UAH=0.0, mass_in_grams=0, time_for_cooking_in_minutes=0, name_of_dish=None,
                 ingredients=None,
                 specifications=None, condition=None, consistence=None, countryOfOrigin=None):
        super().__init__(price_in_UAH, mass_in_grams, time_for_cooking_in_minutes, name_of_dish, ingredients,
                         specifications, condition, consistence)
        self.countryOfOrigin = countryOfOrigin


class PumpkinSoupSchema(ma.Schema):
    class Meta:
        fields = ('price_in_UAH', 'mass_in_grams',
                  'time_for_cooking_in_minutes', 'name_of_dish', 'ingredients',
                  'specifications', 'condition',
                  'consistence', 'country_of_origin')


pumpkin_soup_schema = PumpkinSoupSchema()
pumpkin_soups_schema = PumpkinSoupSchema(many=True)


@app.route("/pumpkin_soup", methods=["POST"])
def add_pumpkin_soup():
    price_in_UAH = request.json['price_in_UAH']
    mass_in_grams = request.json['mass_in_grams']
    time_for_cooking_in_minutes = request.json['time_for_cooking_in_minutes']
    name_of_dish = request.json['name_of_dish']
    ingredients = request.json['ingredients']
    specifications = request.json['specifications']
    condition = request.json['condition']
    consistence = request.json['consistence']
    country_of_origin = request.json['country_of_origin']
    pumpkin_soup = PumpkinSoup(price_in_UAH,
                               mass_in_grams,
                               time_for_cooking_in_minutes,
                               name_of_dish,
                               ingredients,
                               specifications,
                               condition,
                               consistence,
                               country_of_origin)

    db.session.add(pumpkin_soup)
    db.session.commit()
    return pumpkin_soup_schema.jsonify(pumpkin_soup)


@app.route("/pumpkin_soup", methods=["GET"])
def get_pumpkin_soups():
    all_pumpkin_soups = PumpkinSoup.query.all()
    result = pumpkin_soups_schema.dump(all_pumpkin_soups)
    return jsonify({'pumpkin_soups': result})


@app.route("/pumpkin_soup/<id>", methods=["GET"])
def get_pumpkin_soup(id):
    pumpkin_soup = PumpkinSoup.query.get(id)
    if not pumpkin_soup:
        abort(404)
    return pumpkin_soup_schema.jsonify(pumpkin_soup)


@app.route("/pumpkin_soup/<id>", methods=["PUT"])
def update_pumpkin_soup(id):
    pumpkin_soup = PumpkinSoup.query.get(id)
    if not pumpkin_soup:
        abort(404)
    old_pumpkin_soup = copy.deepcopy(pumpkin_soup)
    pumpkin_soup.power_consumption = request.json['power_consumption']
    pumpkin_soup.hours_per_month_usage = request.json['hours_per_month_usage']
    pumpkin_soup.repair_price = request.json['repair_price']
    pumpkin_soup.location_in_house = request.json['location_in_house']
    pumpkin_soup.appliance_name = request.json['appliance_name']
    pumpkin_soup.plugged_into_socket = request.json['plugged_into_socket']
    pumpkin_soup.connection_protocol = request.json['connection_protocol']
    pumpkin_soup.data_transfer_amount = request.json['data_transfer_amount']
    db.session.commit()
    return pumpkin_soup_schema.jsonify(old_pumpkin_soup)


@app.route("/smart_home_appliance/<id>", methods=["DELETE"])
def delete_pumpkin_soup(id):
    pumpkin_soup = PumpkinSoup.query.get(id)
    if not pumpkin_soup:
        abort(404)
    db.session.delete(pumpkin_soup)
    db.session.commit()
    return pumpkin_soup_schema.jsonify(pumpkin_soup)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
