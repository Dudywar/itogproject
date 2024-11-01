from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

databaseURL = 'https://zakazedi-3c538-default-rtdb.europe-west1.firebasedatabase.app/'

cred = credentials.Certificate("zakazedi-3c538-firebase-adminsdk-xe6q5-dc1e53ee64.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': databaseURL
})
ref = db.reference("/")

@app.route("/", methods=['POST'])
def order():
    data = request.get_json()
    ref.child(f'id: {data["id"]}').set({"product": data["product"]})
    socketio.emit("new_order", {"id": data["id"], "product": data["product"]})
    return jsonify({"message": "Заказ получен", "data": data}), 200

@app.route("/complete_order", methods=['POST'])
def complete_order():
    zak = request.get_json()
    ref.child(f'id: {zak["id"]}').delete()
    socketio.emit('order_completed', {'order_id': zak["id"]})
    return jsonify({'message': 'Заказ завершен!'})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == "__main__":
    socketio.run(app, port=8000)