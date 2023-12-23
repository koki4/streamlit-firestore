from google.cloud import firestore
db = firestore.Client.from_service_account_json("./serviceAccountKey.json")
docs = db.collection("iris").stream()
for d in docs:
    print(d)