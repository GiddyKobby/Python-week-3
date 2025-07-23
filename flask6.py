from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Welcome to my first backend server."

@app.route("/add")
def add():
    return "This would add something in a real app!"

if __name__ == "__main__":
    app.run(debug=True)


# Flask(__name__) → sets up the server.

# @app.route("/") → creates a route → like a “menu option” for your web server.

# home() → what happens when someone visits /.

# app.run(debug=True) → runs the server in debug mode → easy to test.

# Flask runs a server.

# @app.route handles URLs.

# Functions return responses.

# This is the start of APIs.