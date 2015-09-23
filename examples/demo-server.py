#!/usr/bin/env python
from flask import Flask, request
import json

app = Flask(__name__)

_lists_ = [{
    "ID": "1",
    "title": "Shopping List",
    "description": "Things to buy"
},
{
    "ID": "2",
    "title": "Secret List",
    "description": "You should not see this"
}]

_tasks_ = [{
        "ID": "11",
        "parentID": "1",
        "title": "Buy Milk",
        "description": "because it is good",
        "status": "TODO"
    },
    {
        "ID": "12",
        "parentID": "1",
        "title": "Buy Chocolate",
        "description": "because it is even better",
        "status": "TODO"
    },
    {
        "ID": "21",
        "parentID": "2",
        "title": "Explain Monolithe",
        "description": "We are doing it right now",
        "status": "TODO"
    },
    {
        "ID": "22",
        "parentID": "2",
        "title": "Make Garuda popular",
        "description": "Almost done",
        "status": "TODO"
    },

    {
        "ID": "23",
        "parentID": "2",
        "title": "Dominate the world",
        "description": "That is the plan",
        "status": "TODO"
    }
]

def _get_tasks_of_lists(lid):
    return filter((lambda t: t["parentID"] == lid), _tasks_)

def _get_tasks(tid):
    return filter((lambda t: t["ID"] == tid), _tasks_)[0]


@app.route('/api/v1_0/root')
def index():
    return "{}"

@app.route('/api/v1_0/lists')
def get_lists():
    return json.dumps(_lists_)

@app.route('/api/v1_0/lists/<tid>/tasks')
def get_tasks(tid):
    return json.dumps(_get_tasks_of_lists(tid))

@app.route('/api/v1_0/tasks/<tid>', methods=["PUT"])
def update_tasks(tid):
    task = _get_tasks(tid)
    task.update(request.json)
    return json.dumps(request.json)


if __name__ == "__main__":
    app.run(debug=True)