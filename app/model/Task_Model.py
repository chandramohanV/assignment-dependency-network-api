from app.main import *
from flask_marshmallow import Marshmallow
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Task(db.Model):

    def __init__(self, taskName):
        self.taskName = taskName

    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(80), unique=True)


class TaskSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('taskName',)


task_schema = TaskSchema()
task_schema = TaskSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)
