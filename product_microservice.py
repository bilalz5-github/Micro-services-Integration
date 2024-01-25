# product_microservice.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    # Simulate product information retrieval
    product_info = {
        'id': product_id,
        'name': 'Sample Product',
        'price': 19.99,
    }

    return jsonify(product_info)

if __name__ == '__main__':
    app.run(port=3002)
