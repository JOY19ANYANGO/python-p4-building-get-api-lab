#!/usr/bin/env python3

#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    bakeries_dict_list = []
    for bakery in bakeries:
        bakery_dict = bakery.to_dict()
        bakeries_dict_list.append(bakery_dict)

    response = make_response(bakeries_dict_list, 200)
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id=id).first()
    bakery_dict = bakery.to_dict()
    response = make_response(bakery_dict, 200)
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods_list = []
    baked_goods_by_price = BakedGood.query.order_by(BakedGood.price.desc()).all()
    for bakery in baked_goods_by_price:
        bakery_dict = bakery.to_dict()
        baked_goods_list.append(bakery_dict)
    response = make_response(baked_goods_list, 200)
    return response


@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive_baked_good = BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first()
    bakery_dict = most_expensive_baked_good.to_dict()
    response = make_response(bakery_dict, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)