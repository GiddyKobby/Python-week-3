from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'title': data.get('title'),
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201

# PUT update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['done'] = data.get('done', task['done'])
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# DELETE a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Task deleted'})
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

