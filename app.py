#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask import request, redirect, json
import requests
import liverpool 
import linio

app = Flask(__name__)

@app.route('/params', methods = ['POST','GET'])
def params():
	if request.method == 'POST':
		return True

	elif request.method == 'GET':
		parametro = request.args.get('params1','valor por default')
		response1 = liverpool.busqueda(parametro)
		response2 = linio.busqueda(parametro)
		response3 = response1 + response2
		return jsonify({"data":response3})


if __name__ == '__main__':
	app.run(port = 5000, debug = True)