from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load .env
load_dotenv()

app = Flask(__name__)

print("✅ MONGO_URI from env:", os.getenv("MONGO_URI"))
print("✅ PORT from env:", os.getenv("PORT"))

# Enable CORS for all routes — customize origin later
CORS(app, origins=["https://giddykobby.netlify.app"])

# MongoDB connection from .env
try: 
   MONGO_URI = os.getenv("MONGO_URI")
   client = MongoClient(MONGO_URI)

   db = client["test_db"]
   collection = db["tasks"]

except Exception as e:
    print("❌ MongoDB connection failed:", e)
    raise e  # re-raise to crash visibly

# Helper: success response
def success(msg, data=None):
    res = {"success": True, "message": msg}
    if data:
        res["data"] = data
    return jsonify(res), 200

# Helper: error response
def error(msg, code=400):
    return jsonify({"success": False, "error": msg}), code

# GET all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = []
    for task in collection.find():
        tasks.append({
            "_id": str(task["_id"]),
            "title": task["title"],
            "done": task["done"]
        })
    return success("Tasks fetched", tasks)

# POST new task
@app.route("/tasks", methods=["POST"])
def add_task():
    if not request.is_json:
        return error("Request must be JSON", 415)

    data = request.json
    title = data.get("title")

    if not title:
        return error("Title is required", 400)

    result = collection.insert_one({
        "title": title,
        "done": False
    })
    return success("Task created", {"_id": str(result.inserted_id)})

# PUT update task
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    if not request.is_json:
        return error("Request must be JSON", 415)

    data = request.json
    title = data.get("title")
    done = data.get("done")

    if title is None or done is None:
        return error("Title and done are required", 400)

    try:
        obj_id = ObjectId(task_id)
    except InvalidId:
        return error("Invalid task ID", 400)

    result = collection.update_one(
        {"_id": obj_id},
        {"$set": {"title": title, "done": done}}
    )

    if result.matched_count == 0:
        return error("Task not found", 404)

    return success("Task updated")

# DELETE task
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        obj_id = ObjectId(task_id)
    except InvalidId:
        return error("Invalid task ID", 400)

    result = collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        return error("Task not found", 404)

    return success("Task deleted")

@app.route("/ping")
def ping():
    return "Server is alive", 200

if __name__ == "__main__":
    print("Databases:", client.list_database_names())
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
