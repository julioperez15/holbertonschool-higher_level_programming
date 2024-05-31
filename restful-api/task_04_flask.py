from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# /status endpoint
@app.route('/status')
def status():
    return "OK"

# /data endpoint: returns all usernames
@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

# /users/<username> endpoint: returns user details
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint: accepts POST requests to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.is_json:
        new_user = request.get_json()
        username = new_user.get('username')
        if username in users:
            return jsonify({"error": "User already exists"}), 400
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True)
