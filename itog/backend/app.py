from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, db

databaseURL = 'https://zakazedi-3c538-default-rtdb.europe-west1.firebasedatabase.app/'

cred = credentials.Certificate("zakazedi-3c538-firebase-adminsdk-xe6q5-273c0f0e8f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': databaseURL
})
ref = db.reference("/")

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        data = request.get_json()
        ref.set({
            "id":
                {
                    "product": data.product,
                }
        })
        print(data)
        return jsonify({"message": "Заказ получен", "data": data}), 200

if __name__ == "__main__":
    app.run(port=8000)
