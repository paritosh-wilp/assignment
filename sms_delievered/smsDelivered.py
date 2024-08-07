from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/smsDelivered', methods=['POST'])
def sms_delivered():
    data = request.json
    print(f"SMS delivery status: {data}")
    return jsonify({"message": "SMS Delivery Confirmed"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)