from flask import Flask, render_template, jsonify, request
from tinydb import TinyDB, Query
from datetime import datetime

app = Flask(__name__)
db = TinyDB('database.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping():
    db.insert({'tipo': "GET", 'timestamp': datetime.now().isoformat()})
    return (jsonify({"resposta": "pong"}))

@app.route('/echo', methods=['POST'])
def echo():
    db.insert({'tipo': "POST", 'timestamp': datetime.now().isoformat()})
    dados = request.args.get("dados")
    return (jsonify({"resposta": dados}))

@app.route('/dash', methods=['GET'])
def dash():
    dados = db.all()
    return render_template('logs.html', itens=dados)
    