from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import Task, Schema_object
from flask_security.decorators import roles_required
import os
from flask_swagger import swagger
import logging


"""Controller which handles all the incoming REST request"""
logging.basicConfig(level=logging.DEBUG)
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

@app.route("/api/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Network API"
    return jsonify(swag)

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
        print(error)
        logging.error("database connection error: " + error)

    return jsonify(new_task)


# endpoint to show all task form the database.sqlite
@roles_required('dev', 'admin')
@app.route("/api/task", methods=["GET"])
def get_task():
    try:
        all_task = Task.query.all()
        result = Schema_object.task_schema(all_task)
    except Exception as error:
        print(error)
        logging.error("database connection error: " + error)

    return jsonify(result.data)


# endpoint to update task
@roles_required('admin')
@app.route("/api/task", methods=["PUT"])
def task_update(name):
    name = request.json['taskname']
    try:
        task = Task.query.get(name)
        db.session.commit()
    except Exception as error:
        print(error)
        # app.log.error("database connection error: " + error)

    return jsonify(task)


# endpoint to delete task
@roles_required('admin')
@app.route("/api/task/<name>", methods=["DELETE"])
def task_delete(name):
    task = Task.query.get(name)
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as error:
        print(error)
        # app.log.error("database connection error: " + error)

    return jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)
