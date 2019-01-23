from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.model import Task
from flask_security.decorators import roles_required
import os

"""Controller which handles all the incoming REST request"""
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database using Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
db = SQLAlchemy(app)


# endpoint for health check
@roles_required('dev', 'admin')
@app.route("/api")
def heartbeat():
    return "Alive"


# endpoint to create new Task
@roles_required('admin')
@app.route("/api/task", methods=["POST"])
def add_task():
    name = request.json['taskname']
    new_task = Task(name)
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as error:
        app.log.error("database connection error: " + error)

    return Task.task_schema.jsonify(new_task)


# endpoint to show all task form the database.sqlite
@roles_required('dev', 'admin')
@app.route("/api/task", methods=["GET"])
def get_task():
    try:
        all_task = Task.app.query.all()
        result = Task.task_schema.dump(all_task)
    except Exception as error:
        app.log.error("database connection error: " + error)
    return jsonify(result.data)


# endpoint to update task
@roles_required('admin')
@app.route("/api/task/<name>", methods=["PUT"])
def task_update(name):
    name = request.json['taskname']
    try:
        task = Task.app.query.get(name)
        db.session.commit()
    except Exception as error:
        app.log.error("database connection error: " + error)
    return Task.task_schema.jsonify(task)


# endpoint to delete task
@roles_required('admin')
@app.route("/api/task/<name>", methods=["DELETE"])
def task_delete(name):
    task = Task.app.query.get(name)
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as error:
        app.log.error("database connection error: " + error)
    return Task.task_schema.jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)
