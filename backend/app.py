import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from clustering.Kmeans import Kmeans_plus_plus

app = Flask(__name__)
CORS(app)  # 允许所有源访问


@app.route('/')
def print_hellp():
    return 'Help Page hello!'


@app.route('/load_data', methods=['GET'])
def get_company_data():
    with open('data/companyData.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)


@app.route('/kmeans', methods=['GET'])
def submit_options():
    print("Query Parameters:", request.args)
    selected_options = request.args.getlist('selectedOption')
    print("Received selected options:", selected_options)
    # return jsonify({"message": "Options received successfully!"}), 200
    return Kmeans_plus_plus(selected_options)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
