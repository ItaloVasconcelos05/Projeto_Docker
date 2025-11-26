from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/users')
def get_users():
    resp = requests.get('http://users:5001/users')
    return jsonify(resp.json())

@app.route('/orders')
def get_orders():
    resp = requests.get('http://orders:5002/orders')
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
