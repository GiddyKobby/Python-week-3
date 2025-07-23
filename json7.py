from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Welcome to my first backend server."

@app.route("/add")
def add():
    return "This would add something in a real app!"

@app.route("/api/info")
def info():
    data = {
        "name": "Gideon",
        "role": "Backend Student",
        "languages": ["Python"],
        "week": 2
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import jsonify → lets you send JSON easily.

# @app.route("/api/info") → new API endpoint.

# jsonify(data) → converts your Python dict → JSON → sends it.from flask import jsonify → lets you send JSON easily.

# @app.route("/api/info") → new API endpoint.

# jsonify(data) → converts your Python dict → JSON → sends it.





# JSON = JavaScript Object Notation

# It’s the universal format for sending data between backend & frontend.

# Looks like a Python dict — but is text that apps can read.

# Frontend asks for data.

# Backend sends JSON back.