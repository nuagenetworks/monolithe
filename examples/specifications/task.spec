{
    "resource_name": "tasks", 
    "description": "Represent a task to do in a list", 
    "entity_name": "Task", 
    "package": "todo-list", 
    "get": true, 
    "update": true, 
    "rest_name": "task", 
    "extends": [
        "@description", 
        "@title"
    ], 
    "attributes": {
        "status": {
            "min_length": 1, 
            "description": "The status of the task", 
            "exposed": true, 
            "filterable": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "TODO", 
                "DONE"
            ], 
            "max_length": 2048, 
            "orderable": true, 
            "type": "enum"
        }
    }, 
    "children": [
        {
            "specification": "user", 
            "update": true, 
            "relationship": "member", 
            "get": true
        }
    ], 
    "delete": true
}