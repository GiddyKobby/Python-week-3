from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ GET route
@app.route("/api/info", methods=["GET"])
def get_info():
    return jsonify({
        "name": "GiddyKobby",
        "course": "Backend with Flask",
        "status": "Learning!"
    })

# ✅ POST route
@app.route("/api/create", methods=["POST"])
def create_data():
    data = request.get_json()  # Get JSON data sent by the client
    name = data.get("name")
    age = data.get("age")

    return jsonify({
        "status": "success",
        "data": {
            "name": name,
            "age": age
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
