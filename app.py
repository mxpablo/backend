from flask import Flask, jsonify
from flask import request
import json
from firebase import FirebaseUser

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

if __name__ == '__main__':
	app.run(port = 5000, debug = True)