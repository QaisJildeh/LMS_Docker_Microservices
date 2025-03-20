from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)