{
    "model": {
        "resource_name": "root",
        "description": "Root object of the API",
        "entity_name": "Root",
        "get": true,
        "package": "todo-list",
        "rest_name": "root",
        "root": true
    },
    "children": {
        "list": {
            "create": true,
            "relationship": "root",
            "get": true
        },
        "user": {
            "create": true,
            "relationship": "root",
            "get": true
        }
    }
}