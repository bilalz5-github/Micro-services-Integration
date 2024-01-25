# api_gateway.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

PRODUCT_MICROSERVICE_URL = 'http://localhost:3002/product/'

@app.route('/get_product/<product_id>', methods=['GET'])
def get_product(product_id):
    # Get product information using the Product Information Microservice
    product_response = requests.get(PRODUCT_MICROSERVICE_URL + str(product_id))

    # Send the product information as the response
    return jsonify(product_response.json())

if __name__ == '__main__':
    app.run(port=3000)
