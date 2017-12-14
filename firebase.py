import pyrebase
import random

class FirebaseUser():
	firebase = ""
	def __init__(self):
		config = {
			"apiKey": "AIzaSyCcTGEvFm8Jp_9fnsvpFt5fvVQaemVNoOg",
			"authDomain": "regalometro-34fa5.firebaseapp.com",
			"databaseURL": "https://regalometro-34fa5.firebaseio.com",
			"storageBucket": "regalometro-34fa5.appspot.com"
		}
		
		firebase = pyrebase.initialize_app(config)
		self.firebase = firebase

	def createAGiftUser(self,data): #POST
		db = self.firebase.database()
		id_user = 80
		db.child("user_Gift").child(id_user).set(data)
		return db.child("user_Gift").child(id_user).get().val()

	def getTheGiftuser(self): #GET
		db = self.firebase.database()
		return db.child("user_Gift").get().val()
