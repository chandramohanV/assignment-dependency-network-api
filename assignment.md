# Assignment

The goal of this assignment is to build a simple first version of a **Dependency Network Service**. 

#### What is a **dependency network**? 

A **dependency network** is a set of rules that define the _earliest start_, _duration_ and _latest end_ of operational tasks in the **turnaround** and the dependencies between those tasks. The duration is not necessarily as long as the time between the earlist start and latest end (eg. sometimes slack is built into the design). The dependency network is effectively a representation of the process design of ground services, as described in the Ground Operations Manuals (GOMS). The _earliest start_ and _latest end_ can be defined in terms of number of minutes since the arrival the aircraft (eg. A+1, A+5, etc.) or the number of minutes until the departure of the aircraft (eg. D-45, D-40, etc.)

If you visualize this in Excel, it would look like this for example:

![Goms in Excel](goms-in-excel.png)

And if you also visualize the _dependencies_ between tasks, you'd get something like this:

![dependencies](dependency-network.png)

In actuality, multiple Dependency Networks exist, because the tasks in the turnaround and their dependencies differ between aircraft types. Eg. a 777 requires different tasks to be completed during the turnaround than a 737. **But for the purpose of this assignment we'll assume there is only possible way to do a turnaround and so there's only 1 dependency network**

#### Dependency Network Service

The **Dependency Network Service** should be a central service in which the dependency network is stored and accessible through an API. It serves both as a central place where other applications can access the dependency network, should they need it, as well as a central place where the dependency network can be _changed/updated_ when needed. This happens quite often, as process designers are constantly trying to optimize the turnaround - and by extension all of its tasks.

## Functional Requirements

The **Dependency Network Service** has the following _functional requirements_:

- It stores tasks with their dependencies on other tasks
- The dependency network can be retrieved as a whole
- Given a task, you can retrieve all other tasks it depends on (ie. _upstream tasks_)
- Given a task, you can retrieve all other tasks that are dependent on it (ie. _downstream tasks_)
- You can add a new task, including dependencies with other tasks
- You can create new dependencies between existing tasks
- You can delete tasks
- You can remove dependencies between tasks
- The dependency network (or parts of it) should be viewable/retrievable by anyone
- Only a select few should be able to change the dependency network (eg. add tasks or dependencies, change tasks/dependencies, remove tasks/dependencies), so some form of user/API authentication/authorization is required
- All of the above is accessible through an API

#### Bonus objectives

The following are not necessarily needed to make an impression with your product, but can be seen as cool challenges for yourself:

- Make it possible to define multiple dependency networks, per aircraft type (eg. Boeing 777, Boeing 737, Airbus A380)
- Add a GUI to visualize the dependency network. Think of the best way to view a dependency network.
- Add a GUI for end-users to administrate the dependency network(s). The aforementioned functionality should be available through the GUI so process designers can add new tasks, see the tasks and their dependencies, change them, etc.



## Non-functional Requirements

- All components of the **Dependency Network Service** run in Docker containers, and communicatie via Docker's networking features. **This includes any databases/storage solutions that you use**
- Each component runs in a **separate** Docker container
- The **Dependency Network Service** is built using **Python**. If you build a GUI, choose whatever language and frameworks you like
- It should be possible to run the **Dependency Network Service** and all of its components on a laptop



## Deliverables

This assignment should be delivered in the following way:

- All code is pushed to this repository. You are allowed to add additional repositories if you think this is needed
- Documentation is provided in the [README.md](README.md) on how the service works, and **how to run it**.
- Any information, (dummy)-data, files, and other assets that are needed to run this service, are provided in this repository. This includes a `docker-compose.yml` for starting Docker containers for all components

## Tips

Here are some tips to get you going:

- Think of what you're building as a real **Product**. Think of your end-users and what they want. In the case of a service with an API but no GUI, your end-users are developers, so provide them with an awesome developer-experience. If you do build a GUI, think of the process designers that use the Dependency Network Service to change the dependency network according to their process design. How would they be able to do that in the most intuitive way?
- Think hard on what kind of storage solution is most suitable for storing a dependency network (ie. what sort of database fits best)
- Design a proper data model for storing the dependency network in your chosen storage solution
- Make a concious decision on what API architecture/technology you use. There are many flavours, so choose what you think best: REST API (can be JSON or XML for example), SOAP, gRPC, ...
- Design your API in an intuitive way, design it according to the best practices of the API technology you choose
- There are many existing libraries/packages that can solved common problems for you. Don't hesitate to use a library where applicable, instead of writing everything from scratch (eg. web frameworks, api frameworks, database access libraries, user authentication libraries)
- For any decision you make - like technology choices, framework choices, etc. - you should be able to put forth good arguments. You should basically be able to defend your choices.
- Work in an agile way! You might not be able to implement all of the features for this assignment in the alotted time, so be smart in picking the features you work on first.
- Make use of the coaching that is offered. Daan can answer questions you have, and you can always discuss your ideas with him.



