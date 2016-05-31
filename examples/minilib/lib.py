from __future__ import absolute_import
from builtins import str
import base64
from . import data
import json
import uuid


# auth

def check_auth(request):
    encoded_auth = request.headers['Authorization'][6:]  # XREST stuff
    decoded_auth = base64.urlsafe_b64decode(encoded_auth.encode("utf-8"))
    auth = decoded_auth.decode("utf-8").split(':')
    if auth[1] != "secret-api-key":
        return False
    return True


# Lists

def perform_get_all_lists():
    """
    """
    return json.dumps(data.lists), 200


def perform_get_list(lid):
    """
    """
    lst = data.get_list(lid)

    if not lst:
        return json.dumps(_create_error("", "list not found", "Cannot find list with ID %s" % lid)), 404

    return json.dumps([lst]), 200


def perform_create_list(d):
    """
    """
    d["ID"] = str(uuid.uuid1())

    error = _validate_list(d)
    if error:
        return json.dumps(error), 409

    data.insert_list(d)

    return json.dumps([d]), 201


def perform_delete_list(lid):
    """
    """
    lst = data.get_list(lid)

    if not lst:
        return json.dumps(_create_error("", "list not found", "Cannot find list with ID %s" % lid)), 404

    data.delete_list(lst)

    return "", 204


def perform_update_list(lid, d):
    """
    """
    lst = data.get_list(lid)

    if not lst:
        return json.dumps(_create_error("", "list not found", "Cannot find list with ID %s" % lid)), 404

    if data.list_equals(lst, d):
        return json.dumps(_create_error("", "No changes to modify the entity", "There are no attribute changes to modify the entity.")), 409

    lst.update(d)

    error = _validate_list(lst)
    if error:
        return json.dumps(error), 409

    return json.dumps([lst]), 200


def _validate_list(lst):
    if not lst["title"]:
        return _create_error("title", "Invalid input", "This value is mandatory.")
    if not lst["description"]:
        return _create_error("description", "Invalid input", "This value is mandatory.")
    return None


# Tasks

def perform_get_all_tasks(lid):
    """
    """
    return json.dumps(data.get_tasks_of_lists(lid)), 200


def perform_get_task(tid):
    """
    """
    task = data.get_task(tid)

    if not task:
        return json.dumps(_create_error("", "task not found", "Cannot find task with ID %s" % tid)), 404

    return json.dumps([task]), 200


def perform_create_task(lid, d):
    """
    """
    d["ID"] = str(uuid.uuid1())
    d["parentID"] = lid

    error = _validate_task(d)
    if error:
        return json.dumps(error), 409

    data.insert_task(d)

    return json.dumps([d]), 200


def perform_delete_task(tid):
    """
    """
    task = data.get_task(tid)

    if not task:
        return json.dumps(_create_error("", "task not found", "Cannot find task with ID %s" % tid)), 404

    data.delete_task(task)

    return "", 204


def perform_update_task(tid, d):
    """
    """
    task = data.get_task(tid)

    if not task:
        return json.dumps(_create_error("", "task not found", "Cannot find task with ID %s" % tid)), 404

    if data.task_equals(task, d):
        return json.dumps(_create_error("", "No changes to modify the entity", "There are no attribute changes to modify the entity.")), 409

    task.update(d)

    error = _validate_task(task)
    if error:
        return json.dumps(error), 409

    return json.dumps([task]), 201


def _validate_task(task):
    """
    """
    if not task["title"]:
        return _create_error("title", "Invalid input", "This value is mandatory.")
    if not task["description"]:
        return _create_error("description", "Invalid input", "This value is mandatory.")
    if not task["status"]:
        return _create_error("status", "Invalid input", "This value is mandatory.")
    if not task["status"] in ("TODO", "DONE"):
        return _create_error("status", "Invalid input", "Invalid input")
    return None


# Utils

def _create_error(property_name, title, description):
    """
    """
    return {"errors":
            [
                {
                    "property": property_name,
                    "descriptions":
                        [
                            {
                                "title": title,
                                "description": description
                            }
                        ]
                }
            ],
            "internalErrorCode": "xxx"
            }
