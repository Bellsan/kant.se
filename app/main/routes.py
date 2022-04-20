from flask import render_template, request, Blueprint
import json

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('main/index.html')

@main.route('/produkter')
def products():
    with open('app/static/products.json', encoding='utf-8') as db:
        products = json.load(db)
    return render_template('produkter/index.html', products = products)