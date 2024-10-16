from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify({"message": "Покупка получена", "data": data}), 200

if __name__ == "__main__":
    app.run(port=8000)
