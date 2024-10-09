import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../MediStock/config/firebase-key.json")
firebase_admin.initialize_app(cred)
