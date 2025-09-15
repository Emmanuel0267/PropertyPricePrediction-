from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_area_names', methods=['GET'])
def get_area_names():
    response = (jsonify({
        'area': util.get_area_names()
    }))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    area = request.form['area']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(area, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
