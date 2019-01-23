# dependency network web API

A **dependency network** is a set of rules that define the _earliest start_, _duration_ and _latest end_ of operational tasks
in the **turnaround** and the dependencies between those tasks.
The duration is not necessarily as long as the time between the earlist start and latest end (eg. sometimes slack is built into the design).
The dependency network is effectively a representation of the process design of ground services, as described in the Ground Operations Manuals (GOMS).
The _earliest start_ and _latest end_ can be defined in terms of number of minutes since the arrival the aircraft (eg. A+1, A+5, etc.)
or the number of minutes until the departure of the aircraft (eg. D-45, D-40, etc.)
t of the tests. If any of the triggered tests fail, the script will exit with a non-zero error code.


### Installation

```cli
    pip install flask
    pip install flask_sqlalchemy
    pip install flask_marshmallow
    pip install marshmallow-sqlalchemy
    pip install flask-security sqlalchemy
```

## Brief Description of the Application Structure

 - `bin`- scripts that will be executed on the command line
 - `app`- contains the application itself
 - `doc`- project related documentation files
 - `test`- contains unit test case
 - `Dockerfile`- contains docker file
 
## How to run the Application
  Run the file app/controller.py to start the dev server.
  
- /api              Health check
- /api/task [POST]  Create a task
- /api/task [GET]  get all the task
- /api/task/<name>[PUT]   To update the task
- /api/task/<name>[DELETE]  Delete the task 

## Features that need to be added to project

*  Authentication 
*  Validation
*  Mock test and Integration test case
*  Versioning
*  api documentation
*  Dependency Management
*  Code Coverage

Doc section contains the "Dependency_API_Design.docx" which gives brief idea about how the API and its request and response will  be.

