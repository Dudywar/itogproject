from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

databaseURL = 'https://zakazedi-3c538-default-rtdb.europe-west1.firebasedatabase.app/'

cred = credentials.Certificate("zakazedi-3c538-firebase-adminsdk-xe6q5-273c0f0e8f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': databaseURL
})
ref = db.reference("/")

@app.route("/", methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        data = request.get_json()
        ref.child(f'id: {data["id"]}').set({"product": data["product"]})
        socketio.emit("new_order", {"id": data["id"], "product": data["product"]})
        print(f"Emitted new_order: id={data['id']}, product={data['product']}")
        return jsonify({"message": "Заказ получен", "data": data}), 200

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == "__main__":
    socketio.run(app, port=8000)
