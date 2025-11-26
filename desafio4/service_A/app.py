from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/users')
def users():
    lista = [
        {"id": 1, "nome": "João"},
        {"id": 2, "nome": "Maria"},
        {"id": 3, "nome": "Pedro"}
    ]
    return jsonify(lista)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
