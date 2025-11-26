from flask import Flask
import os
import redis
import psycopg2

app = Flask(__name__)

DB_URL = os.environ.get('DATABASE_URL')

def get_db_conn():
    return psycopg2.connect(DB_URL)

redis_host = os.environ.get('REDIS_HOST')
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    return "Olá do serviço App!"

@app.route('/add/<nome>')
def add(nome):
    conn = get_db_conn()
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS pessoas (id SERIAL PRIMARY KEY, nome TEXT)')
    
    cur.execute('INSERT INTO pessoas (nome) VALUES (%s)', (nome,))
    conn.commit()
    cur.close()
    conn.close()
    
    cache.set('ultimo_nome', nome)
    return f"Adicionado: {nome}"

@app.route('/listar')
def listar():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pessoas')
    dados = cur.fetchall()
    cur.close()
    conn.close()
    return str(dados)

@app.route('/cache')
def show_cache():
    ultimo = cache.get('ultimo_nome')
    return f"Último nome no cache: {ultimo.decode() if ultimo else '-'}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)