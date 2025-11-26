from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/combine')
def combine():
    resp = requests.get('http://servico_a:5000/users')
    users = resp.json()
    return jsonify({"msg": "Usuários recebidos!", "users": users})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
