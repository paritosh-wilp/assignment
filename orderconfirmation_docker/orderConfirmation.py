from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orderConfirmation', methods=['POST'])
def order_confirmation():
    data = request.json
    print(f"Confirming order: {data}")
    return jsonify({"message": "Order Confirmed"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
