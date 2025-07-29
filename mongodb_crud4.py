from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection (replace if needed)
client = MongoClient(
    "mongodb+srv://gideonz823:Giddy.MongoDB10@cluster0.ry8nbp5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

db = client["test_db"]
collection = db["tasks"]

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
    return jsonify(tasks)

# POST new task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    result = collection.insert_one({
        "title": data["title"],
        "done": False
    })
    return jsonify({"_id": str(result.inserted_id)})

# PUT update task
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    result = collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {
            "title": data["title"],
            "done": data["done"]
        }}
    )
    if result.modified_count == 1:
        return jsonify({"msg": "Task updated!"})
    else:
        return jsonify({"msg": "No changes made."})

# DELETE task
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    result = collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 1:
        return jsonify({"msg": "Task deleted!"})
    else:
        return jsonify({"msg": "Task not found."})

if __name__ == "__main__":
    print("Databases:", client.list_database_names())
    app.run(debug=True)
