from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://gideonz823:Giddy.MongoDB10@cluster0.ry8nbp5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["taskdb"]
tasks_collection = db["tasks"]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        task['_id'] = str(task['_id'])
        tasks.append(task)
    return jsonify(tasks)

# POST new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {
        'title': data.get('title'),
        'done': False
    }
    result = tasks_collection.insert_one(task)
    task['_id'] = str(result.inserted_id)
    return jsonify(task), 201

# PUT update task
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    updated = tasks_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'title': data.get('title'),
            'done': data.get('done')
        }}
    )
    if updated.matched_count == 0:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'message': 'Task updated'})

# DELETE task
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    deleted = tasks_collection.delete_one({'_id': ObjectId(id)})
    if deleted.deleted_count == 0:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
