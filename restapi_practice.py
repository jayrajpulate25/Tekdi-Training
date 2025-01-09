# basic application with CRUD operations (Create, Read, Update, Delete).
# baseline course

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "ABC", "email": "demo1@example.com"},
    {"id": 2, "name": "XYZ", "email": "demo2@example.com"},
    {"id": 3, "name": "PQR", "email": "demo3@example.com"},
    {"id": 4, "name": "IJK", "email": "demo4@example.com"},
]


# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    new_user["id"] = max(user["id"] for user in users) + 1
    users.append(new_user)
    return jsonify(new_user), 201


# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update(request.json)
    return jsonify(user)


# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)


