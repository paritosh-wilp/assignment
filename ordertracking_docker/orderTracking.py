from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/orderTracking', methods=['POST'])
def order_tracking():
    data = request.json
    print(f"Tracking order: {data}")
    return jsonify({"message": "Order is being tracked"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
