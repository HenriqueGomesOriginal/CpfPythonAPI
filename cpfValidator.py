#/usr/bin/env python
# -*- coding:UTF-8 -*-
from flask import Flask
from flask import send_file
from flask import request, jsonify
import json
from cpf import CPF

app = Flask(__name__)

# Estes números foram gerados aleatoriamente :)
# qualquer um dos dois formatos (com pontos ou não) pode ser usado

@app.route('/validateCPF',  methods=['POST'])
def validateCPF():
    content = request.get_json()
    cpf = content['cpf']
    valido = CPF(cpf)
    valid = valido.isValid()
    return '{"cpf": "' + str(valido) + '", "valid":"' + str(valid) + '"}'

@app.route('/index',  methods=['GET'])
def index():
    print('Connect')
    return '{"success":"ok"}'

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)
