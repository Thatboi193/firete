import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("D:/firetest/firetest/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
print("Database Connected")

#Create data


data = {"Name" : "Joakim", "age": 20, "City": "Altas"}

db.collection("students").document("tor").collection("movies").add({"part": 1,"writer": "jk"})
print("Data inserted")