from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deliveryConfirmation', methods=['POST'])
def delivery_confirmation():
    data = request.json
    print(f"Confirming delivery: {data}")
    return jsonify({"message": "Delivery Complete"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
