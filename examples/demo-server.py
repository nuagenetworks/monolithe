#!/usr/bin/env python
from flask import Flask, request
import json

import minilib.lib as lib

app = Flask(__name__)


# root

@app.route('/api/v1_0/root')
def index():
    return json.dumps([{"APIKey": "secret-api-key"}])


# lists

@app.route('/api/v1_0/lists')
def get_lists():
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_get_all_lists()


@app.route('/api/v1_0/lists/<lid>')
def get_list(lid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_get_list(lid)


@app.route('/api/v1_0/lists', methods=["POST"])
def create_list():
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_create_list(request.json)


@app.route('/api/v1_0/lists/<lid>', methods=["PUT"])
def update_list(lid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_update_list(lid, request.json)


@app.route('/api/v1_0/lists/<lid>', methods=["DELETE"])
def delete_list(lid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_delete_list(lid)


# tasks

@app.route('/api/v1_0/lists/<lid>/tasks')
def get_tasks(lid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_get_all_tasks(lid)


@app.route('/api/v1_0/tasks/<lid>')
def get_task(lid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_get_task(lid)


@app.route('/api/v1_0/lists/<lid>/tasks', methods=["POST"])
def create_task(lid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_create_task(lid, request.json)


@app.route('/api/v1_0/tasks/<tid>', methods=["PUT"])
def update_task(tid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_update_task(tid, request.json)


@app.route('/api/v1_0/tasks/<tid>', methods=["DELETE"])
def delete_task(tid):
    if not lib.check_auth(request):
        return "", 401
    return lib.perform_delete_task(tid)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5555)
