import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("D:/firetest/firetest/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()
print("Database Connected")

tasks_ref = db.collection("todo")