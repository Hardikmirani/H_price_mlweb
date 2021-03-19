
from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_city_names')
def get_city_names():
    response = jsonify({
        'city': util.get_city_names()

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    sqft_living = float(request.form['sqft_living'])
    city = request.form['city']
    bedroom  =request.form['bedroom']
    bathroom = request.form['bathroom']
    floors = request.form['floors']
    condition = request.form['condition']
    price_per_sqft = request.form['price_per_sqft']

    response = jsonify({
        'estimated_price': util.get_estimated_price(city,sqft_living,floors,bedroom,bathroom,price_per_sqft)
    })

    return response


if __name__ == "__main__":
    print("Starting python Flask server")
    app.run()