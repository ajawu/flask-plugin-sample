from flask import Flask,jsonify
from marshmallow import fields, Schema, validates, ValidationError

app = Flask(__name__)

class TodoSchema(Schema):
	id = fields.Int()
	title = fields.Str()
	description = fields.Str()
	status = fields.Bool()
    

@app.route('/')
def index():
    return "Hello, World!"

tasks = [
    {
        'id': 1,
        'title': u'Test',
        'description': u'Basis test', 
        'status': False
    },
    {
        'id': 2,
        'title': u'Test1',
        'description':u'Test2', 
        'staus': False
    }
]

@app.errorhandler(422)
def validation_error(err):
    """Handles 422 errors"""
    messages = err.data.get('messages').get('json')
    return jsonify(messages)
    


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'status': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
@validates('title')
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        raise ValidationError('Request is not json.')
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
    
if __name__ == '__main__':
    app.run(debug=True)
