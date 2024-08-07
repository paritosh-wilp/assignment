from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webOrder', methods=['POST'])
def web_order():
    data = request.json
    print(f"Received web order: {data}")
    return jsonify({"message": "Order Received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
