
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from flask import request, redirect, json
import requests
import json
from firebase import FirebaseUser
import liverpool 
import linio

app = Flask(__name__)
database = FirebaseUser()

@app.route('/gift-users', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		data = database.getTheGiftuser()
		lista = []
		lista.append(data)
		return jsonify({'Gifts': lista})

	elif request.method == 'POST':
		data = request.json
		user = database.createAGiftUser(data)
		lista = []
		lista.append(user)
		return jsonify({'Gift-user':lista})

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

@app.route('/')
def home():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(port = 5000, debug = True)